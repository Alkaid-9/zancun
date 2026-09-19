# CrossEdgeIM Training Fixture

无关领域，两个 organization：

- O1 activities：A、B；O2 activities：C、D。
- case c1：`A@1,B@2`；c2：`A@1,B@1`；c3：`C@1,D@2`。
- fixture transport 显式给每个 activity node：case id、previous activity/timestamp、first/last marker。该 transport 是题面假设，不是论文已规定机制。

任务：

1. 逐事件产生 `DeltaDFR/DeltaStart/DeltaEnd`；处理 c2 同刻双向关系。
2. 在 organization 端累计 triplet，画两个 Org-DFG。
3. 题面假设 miner 分别返回 local PN branch；只追踪 central common source/split/join/sink 的 merge，不声称 soundness。
4. 删除 previous-activity 字段，说明哪个 activity-node update 变得不可执行。
5. 让一个 delta 重复投递，先预测 count，再说明论文欠缺什么 delivery contract。
6. 写一个仍无法表达 cross-organization message causality 的 residual。
