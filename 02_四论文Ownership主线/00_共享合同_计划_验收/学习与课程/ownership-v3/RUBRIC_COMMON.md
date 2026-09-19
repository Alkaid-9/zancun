# Common Rubric Contract

所有模块的 `RUBRIC.md` 都继承本页；模块页只能加严，不能临场降低。

## 证据闭环

每个核心任务必须有：

1. H0 独立预答和用时；
2. exposure 与提示等级；
3. 关闭材料后的 redo；
4. 未见 holdout 的“先预测、后检查”；
5. feedback update 与 claim ceiling；
6. D+2/D+7 到期日和实际结果。

## 提示上限

| hint | 允许内容 | 当次上限 |
|---|---|---|
| H0 | 只给题面 | 可评 PASS |
| H1 | 澄清术语/重述问题 | 可评 PASS，必须记录 |
| H2 | 给步骤框架或关键对象 | 最多 SUBMITTED；换未见题重做 |
| H3 | 给推导、关键反例或代码骨架 | RE-OPEN |
| H4 | 看完整 reference/holdout 答案 | SEEN；换题并延迟复测 |

## 评分

每个维度：`0=缺失或错误`，`1=方向正确但不完整`，`2=正确、可定位且边界清楚`。

通用 PASS 门：

- 所有 hard-gate 维度必须为 2；
- 无 hard fail；
- 其余维度总分至少达到 80%；
- holdout 必须 H0/H1 完成；
- 当前 PASS 只使用 pretest/redo/holdout 与模块 hard gates；D+2/D+7 不得作为当前 PASS 的前置。

RETAINED 门：

- 已先获得当前 PASS；
- D+2 与 D+7 的冻结实例均按各自评分条件通过；
- 任一次失败都进入 `RE-OPEN`，但不篡改历史 PASS 记录。

## 通用 hard fail

- 捏造论文未报告的参数、结果、代码或来源；
- 用 teardown/AI 总结冒充 primary source；
- 检查结果写在预测之前；
- 看到密封答案后仍沿用同题申请 PASS；
- 把课程 BUILT/QA-PASS 写成用户 PASS/OWNED；
- 代写 Ledger 或学习者证据。
