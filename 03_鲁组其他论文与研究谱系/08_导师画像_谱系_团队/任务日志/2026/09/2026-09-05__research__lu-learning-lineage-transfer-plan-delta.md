---
id: TASK-20260905-001
title: 鲁组学习—谱系—迁移研究计划差分
date: 2026-09-05
runtime:
  model: Codex GPT-5
  effort: n/a
  effort_source: 当前托管会话未暴露可审计 reasoning-effort 字段
  launch: codepocket
type: research
status: completed_with_open_gates
area: learning-and-research-planning
project: jinzu-sprint
todo_ids: [BR-3, BR-13]
owners:
  - user
  - codex
related:
  - progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md
  - learning/training/lu-edgeim-algo1/BRIEF.md
  - learning/training/ra2716-survey/BRIEF.md
  - ../research_growth/反思与思考/2026-09-05_鲁法明研究谱系与稳定Research-Grammar.md
---

# 目标

把 2026-09-05 新形成的鲁法明研究谱系与迁移判别框架接入当前学习/研究计划，同时保留 EdgeIM ownership-first 地基，不启动实验、不修改冻结 OS。

# 最终结果

用户批准“外围重排、地基不动”方案。已形成 P0-P5 计划差分，追加 EdgeIM Amendment A4 和导师画像 Amendment A1，纠正项目卡中过期 `09-10`，并扩展 BR-3 semantic scan 语义。当前状态为 `completed_with_open_gates`：计划已落盘，执行仍停在 EX-00 v2 §6；P1-P5 均未解锁。

# 修改内容

- 新增计划差分决策档，固定依赖、产出、PASS 与停止条件。
- EdgeIM 站序、题面、PASS 条件保持不变，只追加外围解锁点。
- 导师画像增加 EX-01R 反证式谱系证据审计，不追认历史空白 EX-01。
- jinzu-sprint / lu-side 项目卡把进组预期纠正为 9 月底、精确日期待定。
- BR-3 检索单位扩展为 action + object + result；新增 BR-13 执行项。
- 未找到独立 weekly-scan 权威文件，未虚构自动任务。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 地基不动 | 原站序/PASS/题面不改 | PASS | EdgeIM BRIEF A4 |
| 分层可执行 | P0-P5 有依赖、产出和停止条件 | PASS | 决策档 §3/§8 |
| 当前游标准确 | EX-00 v2 §6 是唯一动作 | PASS | 决策档 §3 P0/§10 |
| 谱系不冒充能力 | P1 后置且需 citation audit | PASS | 决策档 §3 P1 |
| 日期不伪精确 | 9 月底、精确日期待定 | PASS | 决策档 §7；项目卡 |
| 无越权执行 | 无实验/代码/OS 改动 | PASS | scoped git diff + 文件检查 |

# 当前状态

计划层已调整；学习能力、论文事实和 research hypothesis 均未因文档写入升级。P0 ACTIVE，P1-P5 BLOCKED。

# 尚未完成

- 用户尚未提交 EX-00 v2 §6 脱稿答案。
- 鲁法明谱系中的作者、官网、年份、方法和数字尚未完成 P1 citation audit。
- DFR-equivalence / EdgeIM / sigRank 横向比较尚未解锁。
- 首张 Transfer Card 与 toy experiment 尚未解锁。
- 进组精确日期与 OE1 新日期仍未知。

# 下一步

1. 用户完成 `learning/training/lu-edgeim-algo1/EX-00/README.md` v2 §6 脱稿提交。

# 可拓展方向

- P1 后把核验完成的 lineage map 作为进组交流输入。
- P4 后再决定是否把首张 Transfer Card 注册为正式研究候选。

# 风险与回滚

- 风险：宏观谱系再次抢占核心学习。控制：P1-P5 明确阻断。
- 风险：把合作网络当组织架构。控制：P1 本人/网络零混称门。
- 风险：日期被伪精确。控制：保持“9 月底、精确日期待定”。
- 回滚：删除本决策档与 task log，移除两个 Amendment 和两张项目卡的 2026-09-05 增量；原题面、OS 和实验未改。

# 文件和产物

- `progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md`
- `learning/training/lu-edgeim-algo1/BRIEF.md`
- `learning/training/ra2716-survey/BRIEF.md`
- `progress/projects/jinzu-sprint.md`
- `progress/projects/lu-side.md`
- `progress/task_logs/2026/09/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md`

## Amendment

后续状态变化只追加，不把计划落盘改写成能力或实验完成。

### 2026-09-05 · TASK-20260905-002

用户纠正“三篇相邻论文统一后置”的设计，明确四论文十字训练闭环。新增 `FOUR_PAPER_TRAINING_LOOP.md`，并在 EdgeIM BRIEF A5、CONNECTIONS 和计划差分 A1 中登记：sigRank 横向对照、Ground Truth 实验方法论、CrossEdgeIM 纵向 genealogy 均按站点穿插解锁。原站序/PASS/当前 EX-00 游标不变。
