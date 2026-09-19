# sigRank Training Fixture

这是 multiset，共 5 个 trace occurrences：

- `t1=<A,B,C>`，出现 2 次
- `t2=<A,C>`，出现 1 次
- `t3=<A,B,B,C>`，出现 1 次
- `t4=<A,D,C>`，出现 1 次

设 `w_act=w_dfr=0.5`，sampling ratio 40%，本题预算恰为整数。

任务：

1. 按“含该 activity/DFR 的 trace occurrences 比例”计算 support。
2. 按 trace position 计算 Eq.4/5；特别处理 t3 的重复 B。
3. 计算 Eq.6，排序并说明 duplicate t1 occurrences 是否会占多个位置。
4. 给出 top-N；若你认为 selection unit 仍不明确，列 competing interpretations 和最低成本代码/原文检查。
5. 构造一个 rare-critical trace，使其分数低但对另一个 downstream consumer 很重要。
6. 写 matched-retained-count 的 EdgeIM 对比合同，不运行也可，但字段必须完整。
