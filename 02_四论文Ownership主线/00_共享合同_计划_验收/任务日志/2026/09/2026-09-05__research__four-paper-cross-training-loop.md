---
id: TASK-20260905-002
title: EdgeIM 四论文十字训练闭环
date: 2026-09-05
runtime:
  model: Codex GPT-5
  effort: n/a
  effort_source: 当前托管会话未暴露可审计 reasoning-effort 字段
  launch: codepocket
type: research
status: completed_with_open_gates
area: learning-plan
project: jinzu-sprint
todo_ids: [BR-13]
owners:
  - user
  - codex
related:
  - learning/training/lu-edgeim-algo1/FOUR_PAPER_TRAINING_LOOP.md
  - progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md
---

# 目标

把 EdgeIM、sigRank、Ground Truth Approach 和 CrossEdgeIM 组织为一篇主干与三个观察镜头，避免“只学 EdgeIM，其余无限后置”，同时避免四篇平均逐页精读打断主线。

# 最终结果

已形成四论文十字训练调度：EdgeIM 为 ownership 主干；sigRank 在 EX-01/EX-05 后分两次做横向 sparring；Ground Truth 在 EX-06 后、EX-07 前形成 world contract；CrossEdgeIM 在 EX-06 后重建 genealogy，并可在 Transfer Card 阶段二次打开。当前全部镜头仍 LOCKED，唯一游标是 EX-00 v2 §6。

# 修改内容

- 新增 `FOUR_PAPER_TRAINING_LOOP.md`。
- EdgeIM BRIEF 追加 A5。
- CONNECTIONS 增加 L-S1/L-S2/L-GT/L-CX1/L-CX2 解锁表。
- 计划差分追加 A1，修正原 P3 统一后置读法。
- TASK-20260905-001 追加关联 amendment。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 角色分明 | 主干/横向/实验/纵向各一 | PASS | FOUR_PAPER §1-2 |
| 不平均用力 | 每篇有不同读法与深度 | PASS | FOUR_PAPER §4/§6 |
| 不无限后置 | 三镜头均有明确站点解锁 | PASS | FOUR_PAPER §5 |
| 地基不动 | 原站序/PASS/当前游标不变 | PASS | BRIEF A5；计划 A1 |
| 实验证据门 | EX-07 前须有 world contract | PASS | FOUR_PAPER L-GT |

# 当前状态

调度已落盘，内容学习尚未发生；不得把课程设计记为用户能力。

# 尚未完成

- EX-00 尚未 PASS。
- L-S1/L-S2/L-GT/L-CX1/L-CX2 均未解锁。
- 四篇相关事实仍按各论文原文与现有拆解件的 claim ceiling 管理。

# 下一步

1. 用户完成 EdgeIM EX-00 v2 §6。

# 可拓展方向

- L-S2 后把 fair-comparison contract 接入 EX-07。
- L-CX1 后决定 interaction-semantics residual 是否值得开 Transfer Card。

# 风险与回滚

- 风险：观察镜头膨胀成三套新课程。控制：固定时间盒和停止点。
- 风险：拆解件剧透主干。控制：所有镜头受站点 PASS 解锁。
- 回滚：移除 FOUR_PAPER、BRIEF A5、CONNECTIONS 镜头表和计划 A1；不影响原站点文件。

# 文件和产物

- `learning/training/lu-edgeim-algo1/FOUR_PAPER_TRAINING_LOOP.md`
- `learning/training/lu-edgeim-algo1/BRIEF.md`
- `learning/training/lu-edgeim-algo1/CONNECTIONS.md`
- `progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md`
