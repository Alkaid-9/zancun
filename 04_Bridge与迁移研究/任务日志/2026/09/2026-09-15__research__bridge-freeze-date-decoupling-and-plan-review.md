---
id: TASK-20260915-003
title: 09-20/09-25 冻结日脱钩改条件触发 + ownership-v3 计划复审
date: 2026-09-15
runtime:
  model: Fable 5
  effort: high
  effort_source: 会话内用户可见的多轮工具调用与核验深度
  launch: Claude Code CLI（用户交互会话，非无人值守）
type: research
status: completed_with_open_gates
area: learning/training/lu-edgeim-algo1
project: lu-side
todo_ids: []
owners:
  - user
related:
  - progress/decisions/2026-09-03__research__bridge-lu-execution-plan-v1.0.md
  - learning/training/lu-edgeim-algo1/BRIEF.md
  - progress/decisions/2026-09-12__research__four-paper-full-ownership-design-for-sol.md
  - progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md
  - learning/training/lu-edgeim-algo1/ownership-v3/BUILD_STATUS.md
  - progress/projects/lu-side.md
  - progress/projects/jinzu-sprint.md
---

# 目标

两件事：(1) 复核用户描述的"计划改动史"（四论文差异化吃透计划 → 发现进组计划v2.1质量/架构问题后写的优化计划），判断优化计划是否还有要改的地方；(2) 执行用户对其中一个已发现问题（09-20 核心冻结日与 09-12 新工作量冲突）的明确裁定——脱钩日历改条件触发。

# 最终结果

第二件事已完整落地：`bridge-lu-execution-plan-v1.0.md` 新增 §13 修订记录，`BRIEF.md` 新增 A9，两处互相引用，原文数字保留未删，日历日期改为 `ownership-v3/` 四个 EdgeIM 桥接模块（B-S2/B-S3A/B-S3B/B-EVAL）用户能力轴全 PASS 的条件触发。

第一件事完成分析交付但未获用户后续指示：确认 `2026-09-12__research__four-paper-full-ownership-design-for-sol.md` 是用户所说"改过的计划"，`2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md` 是"发现质量/架构问题后写的优化计划"；后者已在磁盘建成 `ownership-v3/`（`BUILT/QA-PASS`，75 文件，commit `f9f42db`）。复审中发现三处目标相关缺口（课程无独立内容 QA、B-DEFENSE 无"茂盛线长成独立研究问题"出口、已核实的跨论文文本连接点——sigRank 引用 EdgeIM [13]、CrossEdgeIM 将 EdgeMiner/EdgeIM 并列前作——无处落地记录），已口头报告，用户尚未就是否要为这三处设计实施方案给出方向。

# 修改内容

- `progress/decisions/2026-09-03__research__bridge-lu-execution-plan-v1.0.md`：header 与首段 blockquote 加订正指针；§2 表格两行原位标注"已被 §13 订正"；文末两处 09-20/09-25 prose 同样标注；追加完整 §13（背景 + 5 点裁定 + 待办清单）。原文数字未删。
- `learning/training/lu-edgeim-algo1/BRIEF.md`：Amendment 追加 A9，格式对齐既有 A1-A8；明确区分"第 103 行 22–28h 是 09-12 既有事实，本次不动"与"本次改的是这个工作量和日历日期之间悬空 3 天的冲突"。
- 本条目：新建本任务日志；`progress/task_logs/INDEX.md` 用 `ledger_edit.py` 保形插入登记行（见下）。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 两处编辑未被并行窗口覆盖/损坏 | `git diff` 逐行核对与本任务记忆一致 | PASS | 本会话内 `git diff -- <两文件>` 输出与编辑意图完全一致 |
| §13 与 A9 互相指向且不循环矛盾 | 两文件各自的 basis/related 字段互相点名对方新增章节 | PASS | §13 标题行 basis 含 `BRIEF.md A9`；A9 basis 含 `bridge-lu-execution-plan-v1.0.md §13` |
| 原文 09-20/09-25 数字未被删除 | grep 仍能命中原始数字 | PASS | `git diff` 显示原表格行内容保留，仅追加括注 |
| 条件触发的判据边界清晰（不与资产轴混用） | 文本显式区分资产轴 BUILT/QA-PASS 与用户能力轴 PASS | PASS | §13 第 4 点、A9 第 4 点均有该句 |
| task_id 中央领号 | 通过看板服务 POST 获取，非目测自增 | PASS | `POST /api/next-task-id` 返回 `TASK-20260915-003` |
| INDEX.md 保形写入 | 用 `ledger_edit.py`，CAS 校验通过，行尾不变 | 待本条目登记后核验 | 见下方登记步骤 |

# 当前状态

09-20/09-25 冻结日已从固定日历日期正式改为条件触发，两处正本（决策档 + BRIEF）文字一致、互相可追溯，未影响其他任何站序、PASS 条件、密封答案或 Ledger 规则。`ownership-v3/` 课程本身状态不变（仍是 `BUILT/QA-PASS`，rubric `NOT-FROZEN`，用户能力轴未开始）。三个目标相关缺口已识别但未设计解决方案，等待用户方向。两张路由卡（`lu-side.md`/`jinzu-sprint.md`）仍停留在 2026-09-05 的 `last_verified`，未反映 `ownership-v3/` 存在或本次触发条件变更。

# 尚未完成

- `progress/projects/lu-side.md`、`progress/projects/jinzu-sprint.md` 路由卡更新——两处编辑均已显式标注"本次不动，需单独一轮"，原因是用户当时的指令聚焦在冻结日本身，未涉及路由卡。
- 三个课程设计缺口（独立内容 QA、mycelium 研究问题出口、跨论文连接落地点）——已分析完成，用户尚未拍板是否要做、怎么做。
- 用户对"计划还有没有要改的地方"这一原始问题的后续回应未到——本任务只完成了分析交付，未获批准继续动手。

# 下一步

1. 等用户对三个缺口给方向（是否要设计实施方案；若要，按什么优先级）。
2. 若用户认为路由卡更新更紧迫，可独立开一轮，只改 `last_verified` 和 DDL 表两处，不涉及本次决策内容变动。
3. 不主动推进 `ownership-v3/` 用户能力轴的实际学习——那是用户侧动作，不是本任务范围。

# 可拓展方向

- 若三个缺口中"跨论文连接落地点"缺口被采纳，`SHARED_ARTIFACTS.md` 当前四张表全是空占位，是最直接的落点，但需要用户先确认这类"已核实文本引用"是否够格写入该文件的回写门（pretest→redo→holdout 证据要求可能过重，需要用户判断是否要为纯文本发现单开一条轻量通道）。
- Desktop `导出的` 文件夹中仍有 4 份 EdgeIM 训练原始会话日志（最大 7830 行）未逐行读过，仅按头尾采样分类；若后续需要精确复核某个站点的历史训练细节，需要针对性通读。

# 风险与回滚

- 风险：条件触发把一个原本"到点必须交"的硬期限变成了无日期软条件，理论上可被无限拖延。缓解：触发条件本身钉死在四个具体模块的用户能力 PASS（不是资产轴，不是模糊描述），且 §13/A9 都显式禁止把 BUILT/QA-PASS 当 PASS 用，避免"课程建好了就算数"的偷换。
- 回滚：若用户后悔想恢复固定日历日期，直接在 §13 之后追加新的修订记录条目（不删 §13），把日期重新钉回去即可；两处编辑都是追加式，未破坏可回滚性。

# 文件和产物

- `progress/decisions/2026-09-03__research__bridge-lu-execution-plan-v1.0.md`
- `learning/training/lu-edgeim-algo1/BRIEF.md`
- 本文件

## Amendment

（无，本次为首次记录）
