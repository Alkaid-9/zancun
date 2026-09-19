# B-S2 Training Fixture

这是教学题，不是 holdout。事件顺序已经给定；同刻事件按列出顺序相邻处理。

`k=2`，固定映射：`A->0, B->1, C->0, D->1`。

| case | ordered events |
|---|---|
| c1 | `A@1, B@2, C@2, D@3` |
| c2 | `A@1, B@2, B@3, D@4` |
| c3 | `C@1` |

任务：

1. 每个事件写 `case, current, previous, j, state before, update, state after`。
2. 给出最终 `S_0,E_0,R_0,S_1,E_1,R_1`。
3. 标出哪个关系跨越节点所有权；说明论文伪码把该关系写到哪个 `R_j`。
4. 说明 `B@2,C@2` 会触发什么；不要把这个规则推广成任意同刻事件的全连接。
5. 实现并用断言验证纸面结果，再做活动重命名但保持映射结构的变体。

reference 由验收者在训练提交后释放。
