---
id: TASK-20260915-014
title: lu-side/jinzu-sprint 两张路由卡指针从09-06旧游标同步到v3合同§1.3恢复包
date: 2026-09-15
runtime:
  model: Fable 5
  effort: high
  effort_source: 会话内逐条核对v3合同§1.3原文+两张卡全文grep排查矛盾遗留
  launch: Claude Code CLI（用户交互会话，非无人值守）
type: research
status: completed_with_open_gates
area: learning/training/lu-edgeim-algo1
project: lu-side
todo_ids: []
owners:
  - user
related:
  - progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md
  - progress/decisions/2026-09-15__research__lu-onboarding-supplement-next-plan.md
  - progress/handoff/2026-09-15__lu-onboarding-and-desks-window__handoff.md
  - progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md
  - learning/training/lu-edgeim-algo1/MASTERY_GATE.md
---

# 目标

执行另一独立窗口（`TASK-20260915-012`）在其[进组补充计划](../../../decisions/2026-09-15__research__lu-onboarding-supplement-next-plan.md)中排定的 J1 步骤（"更新入口"）：`lu-side.md` 和 `jinzu-sprint.md` 两张路由卡此前锁定在 2026-09-06 的旧游标（`MASTERY_GATE.md` v2.1"15题Whole-Paper Diagnostic优先"），但更晚的 [v3合同](../../../decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md)（2026-09-13）已用 D0/D1/D2 三阶段诊断取代此规则，两张卡均未同步，构成两个独立窗口都已确认的真实权威冲突。本任务只做"指针接续"，不改 `MASTERY_GATE.md` 正本、不裁定其他未决事项。

# 最终结果

两张卡均已更新，新旧游标关系清晰可辨，未发现新的表述矛盾遗留：

1. **`jinzu-sprint.md`**：§2版本里程碑增补一行标注09-06接入已被09-15取代；§3 DDL表"下一次学习窗口"行从"15题诊断"改写为v3合同§1.3六项恢复包，并注明`MASTERY_GATE.md`该句本身尚未同步；§7游标整段重写，新增订正说明+历史行保留；§8更新记录追加一行。
2. **`lu-side.md`**：新增"本行承接…不把进组面试当研究线终点"的定位句（此前遗漏，属于本次顺带发现的表述缺口，非强制项，但有助于避免下次误读）——**核查后确认这句其实在会话中断前已经写入**（见git diff），本任务只补充§5当前技术门整段重写（新增订正说明+六项恢复包原文转述+历史行保留）及§5更新记录追加一行；frontmatter `last_verified` 两张卡均刷新到 2026-09-15。
3. **过程修正**：编辑`lu-side.md`时Edit工具两次插入了乱码字节（`本��`应为"本卡"、`结果��能`应为"结果才能"），在写入后立即用`grep "�"`扫描发现并修正，最终复扫确认全文无残留乱码。这是本任务执行中的真实错误，已现场修正，如实记录不隐瞒。

# 修改内容

- `progress/projects/jinzu-sprint.md`：§2/§3/§7/§8 四处编辑；frontmatter `last_verified` 09-05→09-15。
- `progress/projects/lu-side.md`：§5 当前技术门整段重写；§5更新记录追加一行；frontmatter `last_verified` 09-05→09-15；修正两处乱码字节。
- 本条目：新建本任务日志；`progress/task_logs/INDEX.md` 待用 `ledger_edit.py` 保形插入（见下方登记步骤）。
- 未修改 `MASTERY_GATE.md` 正本、`ownership-v3/`、任何已冻结正本；未裁定 `TASK-20260906-004` 状态冲突；未裁定"I01方案A授权矛盾"（该项已在另一任务`TASK-20260915-007`处理）。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| v3合同§1.3恢复包六项转述准确 | 逐字核对合同原文，非凭摘要复述 | PASS | `sed -n '54,68p'` 合同原文六项与两张卡转述逐项对应 |
| 两张卡不再有"15题=当前门槛"的现行断言 | grep 全文排查，历史行必须显式标注"09-06/旧文" | PASS | 两文件grep结果：`lu-side.md`仅剩2处历史标注行；`jinzu-sprint.md`剩余6处均标注"09-15订正/已被取代/现称D2/旧文"字样，无一处裸写"当前门槛=15题" |
| 乱码字节问题已发现并修正 | 写入后用`grep "�"`全文扫描 | PASS | 首次扫描命中第48/61行，修正后复扫`exit=1`（无匹配） |
| `MASTERY_GATE.md`正本未被触碰 | git diff范围核对 | PASS | 本任务全程只用Read/Edit工具作用于两张路由卡，未对`MASTERY_GATE.md`发起任何写操作 |
| 两文件最终纯LF无CRLF混杂 | python3哈希探测 | PASS | `lu-side.md` CRLF=0/LF=61；`jinzu-sprint.md` CRLF=0/LF=90，与编辑前探测的纯LF格式一致，未引入行尾混杂 |

# 当前状态

J1（更新入口）已完成。J0（当前证据对账）在此前会话中已确认权威冲突证据链、EX-05目录文件存在性核对完毕，视为完成到"足以支撑J1"的程度；更深入的作答内容核对（不打开密封答案的前提下）仍可视为J0的可选延伸，非阻塞项。

# 尚未完成

- J2安排补修：用三缺口交接加旧教学债构成有优先级队列——仍是"方案已存，内容未补"，本任务未触碰。
- J3接研究出口：Transfer Card桥接consumer接线——仍是"部分前置证据已有，接线未做"。
- J4排一个真实学习窗口——仍"未安排"，这项本质上需要用户本人参与，AI不能代排。
- J5材料消费核验——仍"未开始"。
- `MASTERY_GATE.md`正本本身是否需要更新以反映v3合同——本任务刻意不做这个决定，只在路由卡上加了"该句尚未同步"的旁注；是否要动正本需要用户表态或走Sol/主控分工确认。

# 下一步

1. 若用户示意继续，下一个自然顺位是J2（安排补修队列）：合并三缺口交接（`TASK-20260915-007`）与本任务发现的教学债，产出一份有优先级的待办清单，不代替用户做真正的学习动作。
2. `MASTERY_GATE.md`正本是否需要同步更新，建议留给用户或下一次专门讨论，不在本任务顺带处理。

# 可拓展方向

- 两张路由卡目前各自独立维护"当前门槛"叙述，未来若v3合同再迭代（比如出现v4），同样的"双卡不同步"风险会重演；可考虑让路由卡统一从合同文件单一来源生成这一段落，而非手工转述——但这是架构改动，不属于本次指针接续范围，仅记录供后续参考。

# 风险与回滚

- 风险：本任务转述的六项恢复包如果后续合同再修订，路由卡会再次滞后；缓解手段已在"可拓展方向"提出但未执行。
- 回滚：本任务只编辑两个已跟踪文件的内容，`git checkout -- progress/projects/lu-side.md progress/projects/jinzu-sprint.md` 即可完全回滚到编辑前状态（对应commit `33b29a5`版本，注意此commit早于会话中此前已发生的其他未提交改动，回滚前需与用户确认是否连带撤销那些改动）。

# 文件和产物

- `progress/projects/jinzu-sprint.md`（编辑）
- `progress/projects/lu-side.md`（编辑）
- 本文件
