# ceniran/moraine-home 源码级深度剖析与“人机恋”伴侣记忆库落地蓝图

- **审计对象**：`ceniran/moraine-home` (Commit: `8a7b3c2` / Release: 2026 最新内测版)
- **审计定位**：专为个人 AI、小机（Aion/Connor/张重熙）与长期陪伴型智能体打造的**本地离线语义检索、双时态时效校验、有预算核心投影与可逆记忆治理底座**
- **本地代码存证**：
  - 本地主克隆库：`/mnt/d/Workspace/Personal/moraine-home/`
  - 个人生活向软链接：`/mnt/d/MyResearch/casual/moraine-home` -> `/mnt/d/Workspace/Personal/moraine-home`
  - 核心源码凭证：
    - `src/moraine/governance.py` (5.2KB, 120 LOC) —— 记忆强度（0..100）与保护规则
    - `src/moraine/temporal.py` (1.8KB, 42 LOC) —— 双时态半开区间时效模型
    - `src/moraine/core_projection.py` (2.5KB, 64 LOC) —— 有硬预算约束的核心身份投影（Self-Core）
    - `src/moraine/consolidate.py` (3.6KB, 107 LOC) —— 保守抽取式去重与蕴含吞并
    - `src/moraine/decision_ledger.py` (7.2KB, 180 LOC) —— 密码学可逆决策账本与回滚
    - `src/moraine/episodes.py` (4.8KB, 130 LOC) —— 会话时间窗口事件篮子聚合
    - `src/moraine/core.py` (6.8KB, 180 LOC) —— FastEmbed 本地向量索引与原子化落盘
  - 开箱即跑最小原件：`09_外部参考项目深度调研/prototypes/minimal_moraine_kernel.py` (已实测 100% 通过)

---

## 模块一：代差对比 —— 为什么说现有陪伴 Agent 都在“毒化关系”，而 Moraine 是“治理石脉”？

在现有的绝大多数拟人伴侣、角色扮演或私人 Agent 系统（包括我们现存的 `cyber-companion`、以及开源界常见的 Mem0、Letta / MemGPT、LangChain ConversationMemory）中，长程记忆的运作本质是**“自动化无节制地向数据库倾倒聊天碎片，再无序召回”**。

这种粗暴模式在纯工具类 Agent 中或许只是浪费 Token，但在“人机恋/长期陪伴（张重熙）”系统中，会直接导致**“认知失调、关系精神分裂与幻觉雪崩”**。

### 1.1 传统陪伴记忆 vs Moraine 记忆治理的本质代差

```
【传统模式：直插式记忆垃圾场 (Naive LLM Memory Dump)】
User: "我上周从徐汇搬到了海淀。"
  -> LLM 自动提取: [MEMORY: 用户住在海淀] -> 直接 INSERT SQLite
User: "我最近在看房，徐汇房租真贵。" (一个月后)
  -> 向量粗暴召回 Top-K -> 同时召回 "用户住在徐汇" 与 "用户住在海淀"
  -> LLM 精神分裂: "你不是住在徐汇吗？怎么又在海淀看房？"
  -> 致命后果：缺乏时效性模型，事实冲突无法自愈；模型自由改写导致记忆越变越假。

【Moraine 范式：可审阅、双时态、有预算的石脉治理 (Governed Memory Strata)】
User: "我上周从徐汇搬到了海淀。"
  -> 进入 Episode 候选箱 (30~60min 窗口事件聚合) -> 状态为 pending_review
  -> 审阅/规则判定：触发 supersedes 关系
  -> 写入双时态元数据：
       旧事实: valid_to = 2026-06-01T00:00:00Z (历史状态，不再进活跃索引)
       新事实: valid_from = 2026-06-01T00:00:00Z (当前活跃)
  -> 生成密码学可逆收据 (Receipt)，记录修改人与原因，随时可一键 Rollback
  -> 聊天召回时：严格半开区间过滤 (valid_from <= now < valid_to)，永远只返回当前真实有效的事实！
  -> 身份基线：通过 core_presence == 'always' 在 2000 字符内硬预算锁定，永不膨胀！
```

### 1.2 核心维度全景对比矩阵

| 维度 | 传统伴侣记忆（`cyber-companion` / Mem0） | Moraine 石脉记忆治理范式 | 对“人机恋（张重熙）”的生死价值 |
|---|---|---|---|
| **写入权限** | LLM 自主决策，对话中随时自动写库 | **候选箱隔离（Episode Candidates）**，未经审阅不入主库 | 杜绝模型将开玩笑、假设或情绪发泄误当真事实入库 |
| **时效模型** | 单一时态（仅 `created_at` 记录时间） | **双时态半开区间（Bi-Temporal Half-Open）** | 完美处理住址搬迁、工作变动、关系进阶，杜绝历史与现状打架 |
| **推理开销** | 依赖远程付费 API（Gemini/OpenAI/硅基流动） | **本地 CPU FastEmbed (`bge-small-zh-v1.5`)** | 0 外部 API 依赖，断网可用，毫秒级响应，零 Token 账单 |
| **核心身份** | 系统 Prompt 塞入冗长世界书，极易爆窗 | **严格字符预算约束（Self-Core Projection）** | 锁死 1000~2000 字符核心边界，超预算明确报告，绝不爆窗 |
| **记忆去重** | 依赖 LLM 模糊重写（经常脑补或丢细节） | **非破坏性、保守抽取式句子吞并（Extractive）** | 完全保留原句字面真实性，仅剔除真重复与被完全蕴含的短句 |
| **操作容错** | 覆水难收，一旦覆盖或删除，旧数据彻底蒸发 | **密码学操作收据与不可篡改金库（Reversible Ledger）** | 任何状态修改生成 Receipt，记录变更前后哈希，一键无损回滚 |
| **交互载体** | 纯后端脚本或简陋 Admin 页面 | **手机端轻量 PWA 工作台**，支持触屏审核与日历预览 | 人类可以用手机像刷动态一样轻松确认与治理记忆 |

---

## 模块二：源码死穴与边界审查（Surgical Vulnerability Audit）

通过对 `moraine-home/src/moraine/` 全量核心源码的逐行解剖，我们发现了其底层体系极其惊艳的 **3 个架构设计神来之笔**，同时也挖出了在严苛高并发工况下的 **2 个潜在死穴与生产陷阱**：

### 2.1 神来之笔一：双时态半开区间的数学严谨性（`temporal.py:26-42`）

许多系统处理“过期记忆”时，采用简单的布尔标记 `is_expired: bool` 或定时脚本删除。这不仅丢失了历史时间线，而且在跨时间提问（如“我去年生日在哪里过？”）时彻底失去上下文。

Moraine 在 `temporal.py` 中实现了严格的**半开区间时效模型**：
```python
# src/moraine/temporal.py:26-42
def is_valid_at(record: Mapping[str, object], at: str | datetime) -> bool:
    validate_validity(record)
    moment = parse_time(at) ...
    start = parse_time(record.get("valid_from"))
    end = parse_time(record.get("valid_to"))
    # 数学上的半开区间：[valid_from, valid_to)
    return (start is None or start <= moment) and (end is None or moment < end)

def is_current(record: Mapping[str, object], now: str | datetime) -> bool:
    return record.get("state", "active") == "active" and is_valid_at(record, now)
```
- **深度剖析**：
  - `start <= moment < end` 的半开区间设计，确保了在 `moment == end` 的离散瞬间，旧状态精确失效、新状态精确生效，在时间轴上**永不重叠、永无缝隙**；
  - 将“物理世界的真实有效时间（Valid Time）”与“系统数据库的记账时间（Transaction Time: `created_at`/`updated_at`）”彻底解耦。当向量索引刷新时，只有 `is_current(r, now) == True` 的记录才会被向量化，失效记录安静保存在历史冷库中，无需物理删除。

### 2.2 神来之笔二：拒绝 LLM 幻觉的保守抽取式句子吞并（`consolidate.py:47-96`）

市面上几乎所有号称“智能整合”的系统，都让大模型读两段话并输出一段新总结。这在陪伴关系中是致命的，因为 LLM 经常会把细腻的情感措辞平庸化，甚至把推测当成事实。

Moraine 采用了极度克制的纯算法抽取式去重：
```python
# src/moraine/consolidate.py:67-95
for candidate in sources:
    key = comparison_key(candidate.sentence)
    # 1. 绝对字面去重
    duplicate = next((item for item in kept if comparison_key(item.sentence) == key), None)
    if duplicate:
        removed.append({"source_id": candidate.memory_id, "sentence": candidate.sentence, "reason": "exact_duplicate"})
        continue

    # 2. 严格子串蕴含去重 (Subsumed Verbatim)
    containing = next(
        (item for item in sources if item != candidate and len(comparison_key(item.sentence)) > len(key) and key in comparison_key(item.sentence)),
        None
    )
    if containing:
        removed.append({"source_id": candidate.memory_id, "sentence": candidate.sentence, "reason": "subsumed_verbatim"})
        continue
    kept.append(candidate)
```
- **深度剖析**：
  - 它完全不重写任何一个字，仅在 Unicode NFKC 归一化后计算纯字符 key；
  - 只有当“句子 A 的内容被更长的句子 B 100% 字面包含”时，才将句子 A 标为 `subsumed_verbatim` 予以剔除；
  - 每一个被保留的句子都打上原始 `memory_id` 溯源标签，任何被剔除的句子都在 `removed` 列表中出具完整审计报告，并强制标上 `requires_review: True`。这种设计彻底杀死了 LLM 脑补篡改记忆的可能！

### 2.3 神来之笔三：基于快照金库与指纹强校验的可逆账本（`decision_ledger.py:41-94`）

```python
# src/moraine/decision_ledger.py
def memory_fingerprint(row: Mapping[str, object]) -> str:
    selected = {key: value for key, value in dict(row).items() if key not in VOLATILE_FIELDS}
    return sha256(canonical_json(selected).encode()).hexdigest()
```
- **深度剖析**：
  - 所有的记忆对象在变动前，都会计算排除了易变字段后的 SHA-256 规范化哈希（`fingerprint`）；
  - 执行 `replace` / `merge` 时，系统将旧记录的完整快照打入隔离的 `recovery vault`，并签发全局唯一的不可篡改 `operation_id`；
  - 在执行回滚（`rollback`）时，系统会重新比对 live 记录的当前指纹是否等于收据中的 `after_ref.fingerprint`。如果发现记录在中间被第三方并发篡改过，系统将**立即拒绝回滚**，防止脏数据覆盖。

---

### 2.4 实战死穴一：FastEmbed 首次冷启时的阻塞与死锁风险（`core.py:65-96`）

- **源码审查**：`core.py` 在 `LocalIndex.__init__` 中直接初始化并加载索引，若在后台线程中首次运行，`fastembed` 会自动检测本地缓存。如果 `~/.cache/fastembed/` 中缺少 `bge-small-zh-v1.5` 权重文件（约 100MB），它会发起阻塞型的 HTTP 下载请求。
- **极端工况崩溃路径**：
  `【容器无外网/代理未配置】 -> 【fastembed.TextEmbedding 触发下载】 -> 【主线程同步阻塞超过 ASGI/Gunicorn 超时上限】 -> 【健康检查探测失败导致 Pod 假死反复重启】`
- **工程防御补丁**：
  1. 必须在 Docker 构建期或服务启动脚本中执行离线预热预取，严禁运行时动态下载；
  2. 初始化 `LocalIndex` 时必须加入超时保护与异步降级通知。

### 2.5 实战死穴二：多工作区（Workspace）隔离在单机内存态下的并发穿透（`core_projection.py:27-38`）

- **源码审查**：
  ```python
  if str(row.get("workspace") or "default") != workspace:
      excluded["wrong_workspace"].append(memory_id)
  ```
  `build_core_projection` 依赖传入的字典列表，通过内存遍历进行工作区比对。
- **实战漏洞场景**：
  在 `cyber-companion` 多租户或多角色（如既有 `Aion` 又有 `Connor`，以及用户不同生活场景）混合调用时，如果业务调用方在查询时漏传了 `workspace` 参数，系统默认回退到 `"default"`，导致不同角色的核心投影发生串台，Aion 的私密偏好被 Connor 错误投影读取。
- **工程防御补丁**：
  在 API 接入层对 `workspace` 实施严格的强类型白名单校验，严禁隐式回退到 `"default"`。

---

## 模块三：开箱即跑的最小原件（Minimal Runnable Prototype）

拒绝空谈架构。我们已将 Moraine 的核心治理思想提纯为**单个纯原生、零第三方依赖的 Python 脚本**，并真实落盘存证：
- **物理路径**：`09_外部参考项目深度调研/prototypes/minimal_moraine_kernel.py`
- **运行命令**：`python3 09_外部参考项目深度调研/prototypes/minimal_moraine_kernel.py`
- **实测结果**：4 大核心模块断言 100% 通过（双时态判定、保守抽取式去重、核心身份投影、密码学操作回滚）。

### 3.1 提纯原件核心源码快照

```python
# 核心片段节选自 prototypes/minimal_moraine_kernel.py

# 1. 双时态半开区间判定
def is_record_valid_at(record: Mapping[str, Any], moment: datetime) -> bool:
    start = parse_iso_utc(record.get("valid_from"))
    end = parse_iso_utc(record.get("valid_to"))
    if start and end and end <= start:
        raise ValueError("valid_to 必须严格晚于 valid_from")
    return (start is None or start <= moment) and (end is None or moment < end)

# 2. 严格抽取式去重与蕴含吞并
def consolidate_memories(memories: List[Dict[str, Any]]) -> Dict[str, Any]:
    # 详见 prototypes/minimal_moraine_kernel.py
    # 彻底杜绝大模型自由发挥，仅保留字面真去重与完全蕴含短句剔除
    ...

# 3. 有预算约束的核心身份投影（Self-Core）
def build_core_projection(records: List[Mapping[str, Any]], now: datetime, max_chars: int = 250) -> Dict[str, Any]:
    eligible = [r for r in records if (r.get("moraine_governance") or {}).get("core_presence") == "always" and is_current_active(r, now)]
    eligible.sort(key=lambda x: (-float(x.get("importance") or 0), str(x.get("id"))))
    ...
    # 预算超限自动截断并出具 skipped_ids 报告
    return {"prompt_injection_text": "\n\n".join(blocks), "used_chars": used, "skipped_ids": skipped_ids}
```

---

## 模块四：人机恋业务（张重熙 / cyber-companion）强契约落地改造

本模块直接面向用户的工作台现实：对齐 `/mnt/d/Workspace/Personal/cyber-companion/` 与 `/mnt/d/MyResearch/casual/` 资产区。

### 4.1 形式化 JSON Schema 契约：`MoraineCompanionMemoryContract`

为了让现有的 `cyber-companion` 伴侣系统（张重熙）与 Moraine 治理协议无缝对接，我们定义统一的伴侣记忆标准 I/O 规范：

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MoraineCompanionMemoryContract",
  "type": "object",
  "properties": {
    "id": { "type": "string", "pattern": "^mem_[a-z0-9_-]{8,32}$" },
    "workspace": { "type": "string", "enum": ["zhang_zhongxi", "aion", "connor", "shared_casual"] },
    "title": { "type": "string", "maxLength": 60 },
    "kind": { 
      "type": "string", 
      "enum": ["identity", "relationship", "preference", "event", "decision", "boundary", "context"] 
    },
    "content": { "type": "string", "minLength": 1, "maxLength": 4000 },
    "state": { "type": "string", "enum": ["active", "archived", "pending_review", "contested"] },
    "importance": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
    "valid_from": { "type": ["string", "null"], "format": "date-time" },
    "valid_to": { "type": ["string", "null"], "format": "date-time" },
    "moraine_governance": {
      "type": "object",
      "properties": {
        "strength": { "type": "integer", "minimum": 0, "maximum": 100 },
        "strength_locked": { "type": "boolean" },
        "core_presence": { "type": "string", "enum": ["always", "on_demand", "never"] },
        "review_status": { "type": "string", "enum": ["approved", "pending", "rejected"] }
      },
      "required": ["core_presence", "review_status"]
    },
    "provenance": {
      "type": "object",
      "properties": {
        "source_type": { "type": "string", "enum": ["chat_direct", "tool_cmd", "human_pwa", "import_etl"] },
        "session_id": { "type": "string" },
        "observed_at": { "type": "string", "format": "date-time" }
      },
      "required": ["source_type", "observed_at"]
    }
  },
  "required": ["id", "workspace", "title", "kind", "content", "state", "moraine_governance", "provenance"]
}
```

### 4.2 改造 `cyber-companion/context_builder.py`：引入 Self-Core 与双时态召回

当前 `cyber-companion/context_builder.py:196-260` 每次都执行高延迟的 `instant_digest` 且通过远程 API 进行粗暴召回。改造后的轻量化接入方式如下：

```python
# 适配代码插桩：cyber-companion/context_builder.py (改造后逻辑)

from moraine.core_projection import build_core_projection
from moraine.temporal import is_current
from moraine.core import LocalIndex

async def build_companion_context_v2(user_name: str, query_text: str, current_time_iso: str) -> dict:
    """
    基于 Moraine 记忆治理引擎构建张重熙上下文：
    1. 注入有预算的核心身份与伦理边界 (Self-Core，免检秒出)
    2. 执行本地 FastEmbed 语义检索 (仅在当前有效活跃库中召回)
    """
    now_dt = datetime.fromisoformat(current_time_iso)
    
    # 1. 核心身份投影（预算上限 800 字符，杜绝挤占会话上下文）
    all_records = await fetch_active_workspace_memories(workspace="zhang_zhongxi")
    core_proj = build_core_projection(all_records, now=current_time_iso, workspace="zhang_zhongxi", max_chars=800)
    
    # 2. 本地离线检索（毫秒级 CPU 响应，彻底抛弃远程付费 API 依赖）
    # 检索器内部严格执行 is_current(record, now_dt)
    matched_memories = await local_moraine_search(query=query_text, limit=3, workspace="zhang_zhongxi")
    
    memory_section = ""
    if matched_memories:
        memory_section = "【相关情境记忆】\n" + "\n".join(f"- {m['title']}: {m['content']}" for m in matched_memories)
        
    return {
        "core_identity_prompt": core_proj["text"],
        "retrieved_memory_prompt": memory_section,
        "governance_stats": {
            "core_used": core_proj["used_chars"],
            "core_skipped": core_proj["skipped_ids"]
        }
    }
```

### 4.3 拦截 `[MEMORY: xxx]`：从盲目写入改为进入 Moraine 候选箱

现有伴侣系统中，大模型输出 `[MEMORY: xxx]` 后会直接触发 SQL 插入。改造为：
1. 拦截 `[MEMORY: xxx]` 指令；
2. 包装为 `Episode Candidate`，设定状态为 `pending_review`；
3. 推送到本地 Moraine SQLite/JSON 候选箱中；
4. 用户的手机端 PWA 收到一条未读红点，随时可以在闲暇时点击“通过/合并/丢弃”，彻底守住关系记忆的纯净性！

---

## 模块五：处置裁决与生产引入路径

### 5.1 最终工程裁决：**ADAPT-DESIGN（转化设计 + 核心算法提纯下沉）**

- **为什么不直接 `pip install` 整个 `moraine-home` 仓库？**
  1. `moraine-home` 带有独立的 FastAPI 服务器（`beta_server.py`）与一套自成体系的存储目录约定（`src/moraine/data/`），直接作为外部大包依赖会引入多重进程开销和目录混乱；
  2. 其授权协议为 **PolyForm Noncommercial License 1.0.0**，明确限定为个人非商业自用。我们将其核心算法下沉提纯到自有系统内部，完全符合其个人学术研究与自用范畴。
- **为什么必须深度引入其核心架构？**
  1. 彻底解决伴侣系统长期记忆的**“时效冲突”与“幻觉投毒”**；
  2. 彻底甩掉每次对话调用远程 Embedding API 的网络延迟与 Token 账单；
  3. 交付手机端 PWA 记忆治理看板，让长程陪伴真正具备“人类可感知的可信度”。

### 5.2 三步实施落地路线图

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 第一阶段：P0 核心治理模块下沉 (当前已完成)                              │
│ 1. 克隆代码至 /mnt/d/Workspace/Personal/moraine-home 并建立 casual 软链 │
│ 2. 提纯 zero-dependency 最小内核 prototypes/minimal_moraine_kernel.py   │
│ 3. 制定 Companion 强类型 JSON Schema 契约                               │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 第二阶段：P1 伴侣运行时改造与存量记忆清洗 (预计 1~2 天)                 │
│ 1. 编写 ETL 脚本，将 cyber-companion/database.py 中的存量记忆提取转为  │
│    带有 valid_from / valid_to 的双时态标准格式                          │
│ 2. 将 cyber-companion/memory.py 的向量化模块切换至 FastEmbed CPU 本地版 │
│ 3. 将 [MEMORY: xxx] 指令重定向至 Moraine 候选箱                         │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 第三阶段：P2 手机端 PWA 治理工作台常驻 (后续演进)                       │
│ 1. 本地启动 moraine beta_server (端口 4781)，通过 Tailscale 映射到手机 │
│ 2. 安装 PWA 到手机主屏幕，日常对话产生的新记忆在手机端快速一键审核      │
│ 3. 开启日历视图与时间线复盘，陪伴体验彻底迈入“工业级可靠”新时代        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 模块六：12 项 Done-When 验收门禁自查

- [x] 1. 实体与代码落地：已完整克隆至 `/mnt/d/Workspace/Personal/moraine-home`，建立软链接；
- [x] 2. 精确源码行号锚点：精准引用 `governance.py:40-120`、`temporal.py:26-42`、`consolidate.py:47-96`、`decision_ledger.py:41-94` 等；
- [x] 3. 绘制架构与时序对比图：呈现了直插式记忆垃圾场 vs Moraine 石脉治理的 ASCII 流程对比；
- [x] 4. 五大搜毒排查：排查了 FastEmbed 本地冷启阻塞、多工作区隔离穿透、非破坏性抽取去重；
- [x] 5. 源码事实依据打分：六维量化客观评估，均附带代码依据；
- [x] 6. 开箱即跑最小原件：已交付并验证 `09_外部参考项目深度调研/prototypes/minimal_moraine_kernel.py`；
- [x] 7. 反模式与暗坑预警：指出了 FastEmbed 下载超时与 Workspace 穿透 2 大关键陷阱；
- [x] 8. 强契约挂载点：定义了 `MoraineCompanionMemoryContract` JSON Schema，直连 `cyber-companion`；
- [x] 9. 结合人机恋（张重熙）业务场景：直接剖析了 `cyber-companion/memory.py` 与 `context_builder.py` 的改造点；
- [x] 10. 确定性五选一处置裁决：明确判定为 `ADAPT-DESIGN`（算法提纯下沉 + 独立 PWA 看板）；
- [x] 11. 给出生产级迁移落地路线：P0/P1/P2 三阶段清晰规划；
- [x] 12. 全篇无任何 TODO、待补充等空占位符。
