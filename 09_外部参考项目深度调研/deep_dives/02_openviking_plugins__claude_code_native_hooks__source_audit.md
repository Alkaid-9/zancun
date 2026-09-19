# L3 源码深度剖析 02 · Castor6/openviking-plugins 基于 Claude Code 原生 Hooks 的记忆持久化闭环

- **审查对象**：`Castor6/openviking-plugins` (深度适配 `volcengine/OpenViking`)
- **审计深度**：**L3 源码与安全级（Source-Code Static Audit & Mechanism Extraction）**
- **本地源码凭证**：
  - `receipts/sources/openviking-plugins/hooks.json`（Claude Code 原生 Hook 调度入口）
  - `receipts/sources/openviking-plugins/auto-recall.mjs`（12.8 KB 提示词提交前静默召回引擎）
  - `receipts/sources/openviking-plugins/auto-capture.mjs`（11.3 KB 回合停止后增量沉淀引擎）
  - `receipts/sources/openviking-plugins/config.mjs`（5.5 KB 客户端环境与连接配置）
  - `receipts/sources/openviking-plugins/memory-server.ts`（26.4 KB 官方 MCP 服务端源码）

---

## 1. 架构突破：告别“人工记住”，实现 Claude Code 全自动记忆闭环

在以往的开发模式中，Claude 每次开新窗口就会“失忆”，必须靠人工在 Prompt 里反复粘贴过往背景；或者靠 Agent 主动调用 `remember` 工具，极其容易被模型漏调或忽略。

`openviking-plugins` 是目前开源界**最优雅、最纯粹利用 Claude Code 原生 Hook 机制实现长效记忆自动流转的工程样板**。它不需要修改 Claude Code 核心二进制，而是通过两端 Hook 形成闭环：

```
                              用户输入 Prompt
                                     │
                                     ▼
        ┌────────────────────────────────────────────────────────┐
        │  [Hook] UserPromptSubmit (auto-recall.mjs)              │
        │  - 词法 + 意图打分 (Lexical + Preference + Temporal)  │
        │  - 探查 OpenViking REST API: /api/v1/search            │
        │  - 通过 additionalContext 静默注入 <relevant-memories> │
        └────────────────────────────┬───────────────────────────┘
                                     │
                                     ▼
                        Claude 处理业务，给出答复
                                     │
                                     ▼
        ┌────────────────────────────────────────────────────────┐
        │  [Hook] Stop (auto-capture.mjs)                        │
        │  - 读取 transcript_path (JSONL 会话日志)               │
        │  - 按 capturedTurnCount 仅提取增量对话                │
        │  - 命中决策/偏好正则后，异步存入 viking://memories/    │
        └────────────────────────────────────────────────────────┘
```

---

## 2. 核心源码逐行解剖：`auto-recall.mjs`（提问前无感召回）

### 2.1 注入机制：Claude Code 官方合规协议
看 `auto-recall.mjs:27-31`：
```javascript
function approve(msg) {
  const out = { decision: "approve" };
  if (msg) out.hookSpecificOutput = { hookEventName: "UserPromptSubmit", additionalContext: msg };
  output(out);
}
```
**关键机制**：
很多非官方插件试图通过修改标准输入或直接替换 prompt 文本，这会导致 Claude Code 出现乱码或安全警告。
本项目严格遵循 Anthropic 规范：通过输出 `{ decision: "approve", hookSpecificOutput: { hookEventName: "UserPromptSubmit", additionalContext: msg } }`，系统会将 `additionalContext` 优雅地附加在本次提问的系统上下文缓冲区，模型感知自然，用户终端完全无感知！

### 2.2 多维度记忆重排序算法（防止污染上下文）
如果每次召回把一堆不相关的旧记忆全塞给模型，上下文会迅速耗尽。看 `auto-recall.mjs:62-108` 的多加权打分机制：
```javascript
const PREFERENCE_QUERY_RE = /prefer|preference|favorite|favourite|like|偏好|喜欢|爱好|更倾向/i;
const TEMPORAL_QUERY_RE = /when|what time|date|day|month|year|yesterday|today|tomorrow|last|next|什么时候|何时|哪天|几月|几年|昨天|今天|明天/i;

function getRankingBreakdown(item, profile) {
  const base = clampScore(item.score);
  const abstract = (item.abstract || item.overview || "").trim();
  const cat = (item.category || "").toLowerCase();
  const uri = item.uri.toLowerCase();
  
  // 1. 叶子节点加权（具体条目比抽象目录优先）
  const leafBoost = (item.level === 2 || uri.endsWith(".md")) ? 0.12 : 0;
  // 2. 时间意图加权（如果问题涉及日期，优先召回 events 分类）
  const eventBoost = profile.wantsTemporal && (cat === "events" || uri.includes("/events/")) ? 0.1 : 0;
  // 3. 偏好意图加权（如果问题涉及习惯，优先召回 preferences 分类）
  const prefBoost = profile.wantsPreference && (cat === "preferences" || uri.includes("/preferences/")) ? 0.08 : 0;
  // 4. 词法重叠度加权（命中用户词干增加权重）
  const overlapBoost = lexicalOverlapBoost(profile.tokens, `${item.uri} ${abstract}`);
  
  return {
    finalScore: base + leafBoost + eventBoost + prefBoost + overlapBoost,
  };
}
```
**设计精妙点**：
它不是单纯盲信向量数据库的余弦相似度（向量相似度在短 query 上常年不准），而是将**余弦基础分 + 语法树深度分 + 意图正则分 + 关键词词法重叠分**四合一融合，筛选出 Top-K 最紧凑的记忆（且只取 L0/L1 摘要，确有必要才读 L2 全文）。

---

## 3. 核心源码逐行解剖：`auto-capture.mjs`（回合结束增量记忆提炼）

### 3.1 增量轮次游标控制（State Cursor Tracking）
很多日志采集脚本每次都把几万行的完整 `transcript.jsonl` 重读一遍，极其消耗 CPU 并造成记忆重复沉淀。看 `auto-capture.mjs:67-86`：
```javascript
function stateFilePath(sessionId) {
  const safe = sessionId.replace(/[^a-zA-Z0-9_-]/g, "_");
  return join(STATE_DIR, `${safe}.json`);
}

async function loadState(sessionId) {
  try {
    const data = await readFile(stateFilePath(sessionId), "utf-8");
    return JSON.parse(data);
  } catch {
    return { capturedTurnCount: 0 };  // 首次运行从第 0 轮开始
  }
}
```
**机制剖析**：
为每个 `sessionId` 维护独立的本地快照文件，记录 `capturedTurnCount`。在 `Stop` Hook 被唤醒时，跳过前 $N$ 轮已处理内容，**仅流式读取自上次交互以来新增加的 1~2 轮增量对话**。

### 3.2 记忆触发感知器（Memory Triggers）
看 `auto-capture.mjs:92-100`，只对有信息密度的增量内容触发沉淀：
```javascript
const MEMORY_TRIGGERS = [
  /remember|preference|prefer|important|decision|decided|always|never/i,
  /记住|偏好|喜欢|喜爱|崇拜|讨厌|害怕|重要|决定|总是|永远|优先|习惯|爱好|擅长|最爱|不喜欢/i,
  /[\w.-]+@[\w.-]+\.\w+/,
  /(?:我|my)\s*(?:是|叫|名字|name|住在|live|来自|from|生日|birthday|电话|phone|邮箱|email)/i,
  /(?:我|i)\s*(?:喜欢|崇拜|讨厌|害怕|擅长|不会|爱|恨|想要|需要|希望|觉得|认为|相信)/i,
];
```
一旦检测到用户表达了约束、技术决策或个人习惯，才将其递交给 OpenViking 后台管道，编译提取为条目，杜绝了把日常“好的”、“谢谢”等废话存进知识库。

---

## 4. 对我们“两台架构”与当前工程的落地复用方案

本项目可以直接作为我们正在搭建的“科研台/学习台外置大脑”的底层接入桥：

1. **直接提取 Hook 脚本**：
   无需重新研发 Hook 逻辑，将 `auto-recall.mjs` 和 `auto-capture.mjs` 提取到我们工作区的工具目录中，针对本地的 `MEMORY.md` 和 SQLite 账本进行微调即可。
2. **意图正则与打分公式复用**：
   直接将其 `buildQueryProfile`、`lexicalOverlapBoost` 与四维打分排序函数合入我们的文献检索前置过滤层，提高科研论文检索的精准度。
