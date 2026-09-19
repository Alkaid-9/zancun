# Batch 2 · OpenViking 上下文与插件生态三仓深度调研报告

- **任务编号**：`TASK-20260919-REF-B2`
- **审查范围**：`volcengine/OpenViking`（主仓）、`ruansheng8/openviking-ui`（管理后台）、`Castor6/openviking-plugins`（Claude Code 插件）
- **定位**：自 Bridge 24 仓 Tier B 第 18 仓（关注其 `viking://` 虚拟文件系统）以来的完整生态演进核查。
- **证据存证**：原始元数据与完整 README/Tree 已落盘至 `receipts/`。

---

## 1. volcengine/OpenViking（生态主仓）

```yaml
id: REF-20260919-005
repo: volcengine/OpenViking
branch: main
stars: 38061
license: AGPL-3.0 (注意传染性)
depth_achieved: L2/L3-MECHANISM
primary_slot: research-desk / learning-desk (底层上下文底座)
safety_tier: SAFE-READONLY (本地服务架构)
disposal_recommendation: ADAPT-DESIGN
```

### 1.1 基础画像与环境基建
- **官方地址**：`https://github.com/volcengine/OpenViking`
- **定位**：字节跳动/火山引擎开源的 Agent 原生上下文数据库（Self-evolving Context Database for AI Agents）。
- **运行环境**：Python 3.10+，可通过 `pip install openviking` 安装，提供本地 REST API 与 CLI 服务。
- **开源协议**：**AGPL-3.0**（若修改源码并作为网络服务提供，有传染开源要求；但如果仅作为本地独立进程通过 HTTP API 调用，不影响我们上层独立系统的代码归属）。

### 1.2 核心架构与工作流机制（两大核心机制）
1. **统一虚拟文件系统 (`viking://`)**：
   - 将 Agent 的所有上下文抽象为一个虚拟文件树：
     - `viking://resources/`：存放项目文档、源码、文献、网页（只读知识）；
     - `viking://memories/`：存放用户习惯、过往经验、学习错题（演进记忆）；
     - `viking://skills/`：存放 Agent 执行特定任务的 SOP 与技能。
   - Agent 统一使用熟悉的 POSIX 命令操作上下文：`ls`、`tree`、`read`、`write`、`find`。
2. **三层分级按需加载（Context Layers - 解决 Token 爆炸）**：
   - **L0 目录抽象 (Abstract)**：仅几十字的极简摘要，Agent 浏览目录时不加载正文；
   - **L1 结构概览 (Overview)**：章节纲要与关键实体关系；
   - **L2 完整正文 (Full Content)**：仅当 Agent 明确需要精读时才读取 L2。
3. **会话编译为记忆 (Context Compilation)**：
   - 对话结束后，后台自动运行记忆提取算法，将非结构化长对话编译为 Wiki 条目或知识图谱。

### 1.3 源码除魅与纸老虎检验
- **除魅结论**：这是**工业级高质量工程项目**，绝非简单的向量数据库 Wrapper。其核心亮点在于将“文件系统隐喻（Filesystem Metaphor）”与“分层上下文缓存（L0/L1/L2）”做到了极致，直接击中了 LLM 上下文窗口限制与 Token 成本痛点。
- **自主性**：内建独立的向量检索（VikingDB）与语义索引调度，具备完整的错误处理与恢复能力。

### 1.4 业务场景映射与可偷师资产
- **槽位匹配**：**两台（科研台与学习台）统一上下文组织底座**。
- **对齐痛点**：
  - 我们此前在两台讨论中一直困惑“论文全文太长怎么放进 Agent 上下文”。OpenViking 的 **L0（摘要）-> L1（章节）-> L2（原文）按需晋升机制**，就是标准解法！
- **可偷师资产**：
  - 借鉴其 `viking://` URI 寻址与分层索引协议，可以在我们自己的两台设计中直接实现 `desk://papers/`、`desk://memories/` 的分级加载逻辑。

### 1.5 五选一处置建议
- **处置结论**：**转化设计 (ADAPT-DESIGN)**（吸收其 L0/L1/L2 分层加载与虚拟文件系统架构思想，融入两台）。

---

## 2. ruansheng8/openviking-ui（可视化管理后台）

```yaml
id: REF-20260919-006
repo: ruansheng8/openviking-ui
branch: main
stars: 26
license: Apache-2.0
depth_achieved: L2-MECHANISM
primary_slot: workbench
safety_tier: SAFE-READONLY
disposal_recommendation: BORROW-PRINCIPLE
```

### 2.1 基础画像与环境基建
- **官方地址**：`https://github.com/ruansheng8/openviking-ui`
- **定位**：基于 Next.js 19 + Tailwind CSS v4 + shadcn/ui 打造的 OpenViking 可视化 Web 管理后台。
- **协议**：Apache-2.0（宽松友好）。

### 2.2 核心架构与工作流
- **BFF (Backend-For-Frontend) 安全架构**：在 Next.js Route Handler 中转发 OpenViking 核心接口，不在前端暴露管理员秘钥 (`root_api_key`)。
- **功能特性**：
  - 资源树浏览器（原生支持切换查看 L0 抽象、L1 概览、L2 原文）；
  - 语义检索测试台（可视化输入 Query，观察返回的文档片段得分）；
  - 租户与权限管理面板。

### 2.3 源码除魅与业务借鉴
- **除魅结论**：这是一个干净、规范的现代全栈 Web 前端脚手架，代码无多余花哨，专注于将 OpenViking 的底层能力图形化。
- **槽位匹配**：**工作台 (Workbench) 页面参考**。
- **可偷师资产**：其前端展示“L0 摘要 / L1 概览 / L2 全文”的切换卡片交互组件（React/Tailwind），非常适合直接复用进我们未来的桌面工作台 UI！
- **处置建议**：**借鉴原则 (BORROW-PRINCIPLE)**。

---

## 3. Castor6/openviking-plugins（Claude Code 深度适配插件）

```yaml
id: REF-20260919-007
repo: Castor6/openviking-plugins
branch: main
stars: 18
license: Apache-2.0
depth_achieved: L2/L3-MECHANISM
primary_slot: infra / workbench
safety_tier: SAFE-READONLY (仅调本地服务)
disposal_recommendation: ADAPT-DESIGN / TRIAL-CANDIDATE
```

### 3.1 基础画像与定位
- **官方地址**：`https://github.com/Castor6/openviking-plugins`
- **定位**：专门为 **Claude Code** 开发的 OpenViking 记忆持久化与自动召回插件（利用 Claude Code 原生 Hooks + MCP）。
- **协议**：Apache-2.0。

### 3.2 核心机制（极高价值的设计模式）
- **自动语义召回 (Auto-Recall)**：
  - 挂载在 Claude Code 的 `UserPromptSubmit` Hook 上；
  - 在用户发送消息前，静默调用 OpenViking 执行语义匹配，将相关的历史偏好和项目上下文注入到当前的 prompt 中。
- **自动知识沉淀 (Auto-Capture)**：
  - 挂载在 Claude Code 的 `Stop` Hook 上；
  - 每轮交互结束后，异步分析本次会话新产出的决策与知识，自动存入 OpenViking。
- **显式 MCP 控制**：同时暴露 MCP Tools，供 Agent 在需要时显式执行 `memory_search`、`memory_store`、`memory_delete`。

### 3.3 源码除魅与业务场景映射
- **除魅结论**：虽然只有 18 星，但这恰恰是**真正理解 Claude Code 扩展机制的干货实现**！它没有自己重造轮子，而是把 Claude Code 的原生 Hook 体系和 OpenViking 的语义存储完美桥接了起来。
- **槽位匹配**：**底层工程基建 (Infra) & 两台跨窗口记忆连续性**。
- **解决的痛点**：我们在 `agent-stack-notes (R12)` 中讨论的外置记忆写入、存储、检索、注入全流程，本项目给出了**一份现成的、可运行的 Claude Code Hook 实现代码**！
- **处置建议**：**转化设计 (ADAPT-DESIGN)**。直接借用其 Hook 脚本的设计结构，实现我们本地记忆系统的静默唤醒与知识沉淀。

---

## 4. OpenViking 生态综合横向矩阵

| 仓库 | 生态角色 | 代码质量 | 核心借鉴价值 | 处置裁定 |
|---|---|---|---|---|
| **OpenViking** | 上下文数据库本体 | 工业级/架构卓越 | `viking://` 虚拟文件系统隐喻 + L0/L1/L2 按需分层加载 | **ADAPT** (转化设计) |
| **openviking-ui** | Web 可视化后台 | 清晰简洁 (Next.js) | L0/L1/L2 可视化分层切换与检索测试台组件 | **BORROW** (借鉴) |
| **openviking-plugins** | Claude Code 专属插件 | 极高契合度 | 利用 Claude Code `UserPromptSubmit` 与 `Stop` Hooks 实现无感记忆注入与沉淀 | **ADAPT** (转化设计) |
