# Ground Truth Training Fixture

无关领域“包裹履约”：

- `M0`：Create -> Pack -> Ship -> Deliver。
- BI：fragile 包裹在 Pack 后真实执行 Inspect。
- RI：扫描器对已执行的 Ship 事件漏记；`L'` 的可见序列中没有 Ship，evaluator 另持 omission/provenance sidecar。
- simulation：按预先给定 fragile 比例、时长和 seed 生成论文层的 imperfect `L'`。
- course projection：隐藏 transition id、BI/RI tag 和 evaluator sidecar，只留下 case/activity/timestamp 得 `D_obs`；这是课程迁移后缀，不是 Sommers 原文新增阶段。
- sampling：在 `D_obs` 上运行一个选择器得到 `D'`。

任务：

1. 画每一步的对象、generator、consumer、visible/hidden。
2. 给“观察日志缺 Ship”至少两个竞争解释，并指出 oracle 怎样区分。
3. 说明 sampling 可以改变什么统计量，不能改变哪个 true executed process。
4. 分别选择 `M0`、`M^S` 和 unsampled `D_obs` 作为 referent，说明它们回答的不是同一问题。
5. 写一个 matched-`|D'|` comparator 和一个 falsifier。
