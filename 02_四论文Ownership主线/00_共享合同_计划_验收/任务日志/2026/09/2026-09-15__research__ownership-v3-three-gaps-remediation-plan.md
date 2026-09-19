---
id: TASK-20260915-005
title: ownership-v3 三缺口(独立QA/研究问题出口/跨论文连接点)落地方案
date: 2026-09-15
runtime:
  model: Fable 5
  effort: high
  effort_source: 会话内多轮独立核实深度
  launch: Claude Code CLI（用户交互会话，非无人值守）
type: research
status: design_only
area: learning/training/lu-edgeim-algo1
project: lu-side
todo_ids: []
owners:
  - user
related:
  - progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md
  - progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md
  - learning/training/lu-edgeim-algo1/ownership-v3/BUILD_STATUS.md
  - learning/training/lu-edgeim-algo1/ownership-v3/SHARED_ARTIFACTS.md
  - learning/training/lu-edgeim-algo1/BRIEF.md
  - progress/task_logs/2026/09/2026-09-15__research__bridge-freeze-date-decoupling-and-plan-review.md
---

# 目标

用户追问"补充之后的点(三个缺口)有没有具体落地实施计划和标准线"，并明确要求"现在做"。本任务把三个此前只是口头报告的缺口（独立QA、mycelium研究问题出口、跨论文连接落地点）各自写出可执行方案，交用户批准。

# 最终结果

三个缺口各给出方案A（推荐）/方案B 两个选项，均已落盘 `progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md`。执行方案前，对之前口头报告的判断做了三处独立重新核实，发现并纠正一处实质性误判：缺口2("mycelium无出口")的准确说法不是"机制不存在"，而是"旧站序已有Transfer Card机制，`SHARED_ARTIFACTS.md`已预留consumer字段指向它，但新建的B-DEFENSE六任务没有真正接上"——这把缺口2从"从零设计"降级为"接线未接完"，方案随之改为轻量桥接文档而非新机制设计。

# 修改内容

- 新建 `progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md`：三缺口各两方案，含推荐理由、成本估计、验收标准草案、给用户的决策面表格。
- 本条目：新建本任务日志；`progress/task_logs/INDEX.md` 用 `ledger_edit.py` 保形插入登记行。
- 未修改 `ownership-v3/` 任何文件（Sol独占写域）、未修改 `BRIEF.md`/`MASTERY_GATE.md`/`FOUR_PAPER_TRAINING_LOOP.md`/`CONNECTIONS.md` 任何已冻结正本。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 缺口2判断纠正有实据 | Transfer Card机制在BRIEF.md确有定义，SHARED_ARTIFACTS.md确有预填consumer字段 | PASS | `BRIEF.md:123`；`SHARED_ARTIFACTS.md` Genealogy表第49行"downstream consumer"列值="Transfer Card / B-DEFENSE" |
| 缺口1"独立QA"现状准确 | git log确认ownership-v3全部来自单一作者单次commit | PASS | `git log --format="%an"` 只返回"张重熙"一人 |
| 缺口3两个连接点强度区分有据 | sigRank/CrossEdgeIM两条连接分别重新grep原文 | PASS | sigRank critique 第11行自称"非本文范围"；CrossEdgeIM critique 第32/99/142行三处同引用 |
| 方案不逾越写域 | 不改ownership-v3/BRIEF.md等正本，只新建决策档 | PASS | 本次唯一改动是新建decision档+task log+INDEX一行 |
| task_id中央领号 | 通过看板服务POST获取 | PASS | 返回`TASK-20260915-005`（跳过004=他窗并发领号，非异常） |

# 当前状态

方案已交付用户决策面，状态 `DRAFT / AWAITING-USER-APPROVAL`（决策档内自述状态）。三个缺口的方案互相独立，可分别批准/否决/搁置。缺口2方案A有一个明确的前置阻塞：Transfer Card的完整判定选项枚举（PROMOTE之外的态）在当前所有已读文件中都没有定义全，需要用户确认或指出更早的定义来源，本任务未越权替BRIEF.md正本编造。

# 尚未完成

- 用户尚未对三个方案的任一项表态（批准/否决/改方案）。
- 缺口2方案A执行前置：Transfer Card判定枚举缺口未解决。
- 缺口1方案A若批准，需要一个"不带建设过程上下文"的独立会话/窗口执行，本任务未启动该会话。
- 缺口3方案A若批准，涉及CrossEdgeIM P0-P3任务文本调整，属于Sol写域，需要重新走一次施工窗口，本任务未发起。
- Desktop 导出材料中4份EdgeIM训练原始会话日志（最大7830行）仍未逐行通读，若其中含Transfer Card枚举的更早定义，本次未覆盖到（已在决策档§6记录此局限）。

# 下一步

1. 等用户对 §5 决策面表格三行表态。
2. 若缺口2方案A获批，先解决Transfer Card判定枚举问题（问用户或搜索桌面导出材料），再写`TRANSFER_CARD_BRIDGE.md`。
3. 若缺口1方案A获批，开一个独立会话按`CONTROLLER_ACCEPTANCE.md`先例格式抽样复核3个模块。
4. 若缺口3方案A获批，记录的具体锚点交下一次Sol施工窗口或用户自行引用。

# 可拓展方向

- 若三个缺口均获批推进，三份产物之间有依赖顺序建议：缺口1（QA）应先做，因为它验证的是缺口2/3将要依赖的底层模块本身是否可信；缺口2和3互相独立，无顺序要求。

# 风险与回滚

- 风险：方案档中标注的"待查"项（Transfer Card枚举）如果用户直接照方案A执行而不先解决这个前置问题，桥接文档可能被迫编造未经证实的判定态。缓解：方案A条款已显式写明这一步是阻塞项，不能跳过。
- 回滚：本任务只新增文件，删除决策档、task log和对应INDEX行即可完全回滚，不影响任何其他文件。

# 文件和产物

- `progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md`
- 本文件

## Amendment

（无，本次为首次记录）
