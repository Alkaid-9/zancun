# EX-05 事件导出格式设计说明

**patch 分支**: `training/ex05-event-export`(mindbridge 仓,基线 9e1e239,4 个 commit)
**产出 log**: `EX-05/logs/scenario-{chat,consult,risk}.jsonl`(同一份复制到 `research/pm4py_toy/data/`)
**日期**: 2026-08-12(降级路径:Agent 代做,用户做逆向 review)

## 1. 行格式与四字段语义

每行一个 JSON 对象,一行 = 黑板上的一个协作事件。必备四字段:

| 字段 | 语义 | 取值来源 |
|---|---|---|
| `case_id` | 一个 case = 一轮用户回合(turn)。同一 turn 内全部事件共享此 id | `CollaborationBlackboard.turn_id`(uuid hex,runtime 每 turn 生成) |
| `activity` | 事件类型,即黑板协议动作 | `AgentEventType.value`,枚举见 §3 |
| `timestamp` | 事件**上板时刻**,ISO8601 带 UTC 时区(微秒精度) | `AgentEvent.created_at`,由 `append_event` 统一打戳 |
| `agent_id` | 产生该事件的行动者 | `AgentEvent.actor`(CoordinatorAgent / UnderstandingAgent / SafetyAgent / ContextAgent / ResponseAgent) |

辅助字段(下游可选用):`seq`(turn 内 1 起连续序号,时间戳相同时的稳定排序键)、`task_id`(黑板任务 id,如 `task:assess-safety`)、`artifact_id`(产物事件关联的 artifact)、`message`(人读描述,如认领理由)、`metadata`(事件级键值,如 `confidence`、`round`、`risk`)、`session_id`(会话 id,跨 turn 关联用)。

设计取舍:时间戳在**上板时**(`append_event`)而非事件对象构造时打戳。原因:agent 在 `act()` 内构造的事件(如 SAFETY_OVERRIDE)先于部分黑板事件构造、后于它们上板,若按构造时刻打戳,时间序与黑板逻辑序会错位,PM4Py 按时间排序后 DFG 会畸变。上板序即协作时间线权威序,已用脚本校验三份 log 每 case 时间戳单调不减且与 `seq` 一致。

## 2. 到 XES / PM4Py 的映射建议

标准列名映射(pandas 路径):

```python
import pandas as pd
import pm4py

df = pd.read_json("scenario-risk.jsonl", lines=True)
df = df.rename(columns={
    "case_id": "case:concept:name",
    "activity": "concept:name",
    "timestamp": "time:timestamp",
    "agent_id": "org:resource",
})
df["time:timestamp"] = pd.to_datetime(df["time:timestamp"])
df = df.sort_values(["case:concept:name", "seq"])   # 稳定排序,防同微秒并列
log = pm4py.convert_to_event_log(pm4py.format_dataframe(df))
```

- `agent_id → org:resource` 是 XES 标准资源扩展,直接支持资源视角(handover-of-work、黑板拓扑对照正需要这个)。
- 活动粒度:`activity` 只含事件类型(13 值低基数),适合先看生命周期骨架。若要区分"认领的是哪类任务",用 `activity + task_id` 派生细粒度活动列,如 `TASK_CLAIMED:task:assess-safety`;`task_id` 已按此预留。
- `ROUND_STARTED` / `MESSAGE_SENT` 可按需过滤:前者是协调器心跳,后者是 agent 间通信,做纯任务生命周期挖掘时可丢弃,做协作拓扑时保留 `MESSAGE_SENT`(`metadata.recipient` 含收件方)。
- 每场景文件含 3 个 case;三文件合并分析时 `case_id` 全局唯一(uuid),可直接 concat,scenario 标签用文件名或加列注入。

## 3. 事件类型覆盖(实测)

三场景实际产生 9/13 种事件类型（2026-08-13 ra26 接入复算更正：下表 9 行，且未出现类型共 4 种，13−4=9；原“10/13”为计数笔误）:

| activity | chat | consult | risk |
|---|---|---|---|
| TURN_STARTED | 3 | 3 | 3 |
| ROUND_STARTED | 9 | 9 | 6 |
| TASK_CREATED | 15 | 15 | 15 |
| TASK_CLAIMED | 12 | 15 | 15 |
| TASK_CLOSED | 12 | 15 | 15 |
| MESSAGE_SENT | 9 | 12 | 12 |
| ARTIFACT_PUBLISHED | 12 | 15 | 15 |
| SAFETY_OVERRIDE | 0 | 0 | 3 |
| FINAL_ACCEPTED | 3 | 3 | 3 |
| 合计 | 75 | 87 | 87 |

未出现的 4 种及原因(读码确认,非猜测):

- `TASK_RELEASED`:枚举已定义但**全仓无发射点**(死枚举成员,EX-01 类 finding)。
- `CRITIQUE_PUBLISHED` / `REVISION_REQUESTED`(否决路径):`SafetyAgent._review_response` 仅在 risk=HIGH 且候选回复缺安全用语时否决;但候选回复的 messages 恒含 HIGH 风险系统提示词(内嵌"高风险处理规则/当前安全/可信任的人/紧急"),审查的是 prompt 而非最终生成文本,故现行逻辑下否决分支**运行时不可达**。这是实现事实,不是本 patch 引入;伪造输入触发会违反"禁止手工编造 log"红线,故如实留空。
- `BUDGET_EXHAUSTED`:三场景均在预算内(≤3 轮)达成 FINAL_ACCEPTED,未触发。

## 4. mock 边界说明

环境缺 MySQL / Redis / Ollama,场景由 `scripts/run_event_export_scenarios.py` 驱动。**被 mock 的仅服务接缝层**:

| 层 | 替身 | 说明 |
|---|---|---|
| LLM | `ai_provider="mock"` | 用仓内 `AiClient._mock` 自带确定性 provider,驱动脚本未注入任何自造 completion |
| 短期记忆 + agent 私有记忆 | `InMemoryShortTermMemoryStore` | 与 `RedisShortTermMemoryStore` 同接口,轮间历史真实流转 |
| DB 会话 | `StubDbSession` | 历史查询返回空(等价冷启动会话) |
| 知识检索 | `StaticKnowledgeService` | 固定 4 条校园心理语料,喂给真实 ContextAgent |

**未被 mock**:黑板、协调器、五个 agent 的 decide/act、任务派生、安全门槛、最终采纳、事件导出本身——log 每一行都由真实 runtime 事件流转产生,驱动脚本只负责发起 turn 与校验四字段。轮次流程照抄 `MindBridgeAgentHarness.run` 的顺序(先跑 turn,再落用户/助手消息进记忆)。

局限如实声明:mock LLM 是确定性的,同场景三个 turn 的事件结构高度相似(轮数、事件数一致);拓扑对照(黑板 vs 编排)不受影响,但若下游要研究行为方差,需换真 LLM 重跑(patch 的导出开关与真实环境兼容,无需改代码)。

## 5. 回滚说明

4 个 commit 按依赖顺序独立可回滚,全部改动不触碰 main、gguf/jsonl 数据目录:

| commit | 内容 | 回滚方式 |
|---|---|---|
| 1f16fda | `AgentEvent.created_at` 上板打戳 | `git revert`;字段带默认值,无调用方改动 |
| 3bf2d7a | 导出器 + Settings 开关 + runtime 一行 hook | `git revert`;或不回滚,运行时置 `agent_event_export_enabled=false`(默认即 false,生产零行为变化) |
| 1bf1ea7 | 单元测试(7 个,全套 24 个通过) | `git revert`,不影响功能 |
| 7d7fe18 | 离线场景驱动脚本 | `git revert`,纯新增文件 |

整分支放弃:`git branch -D training/ex05-event-export`(worktree 已按训练纪律移除,main/master 未动)。
