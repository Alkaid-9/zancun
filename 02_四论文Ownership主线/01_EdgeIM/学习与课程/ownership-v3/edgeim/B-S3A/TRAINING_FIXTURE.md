# B-S3A Training Fixture

给定三个局部产物：

- `L0: S={A}, E={C}, R={(A,B):2,(B,C):1}`
- `L1: S={A,D}, E={C}, R={(A,B):1,(D,C):2}`
- `L2: S={}, E={}, R={(B,C):3}`

任务：

1. 分开计算全局 `S`、`E` 和每条关系的 global weight。
2. 画 global weighted DFG；对每个值标来源 local。
3. 交换 L0/L2 顺序，预测后运行实现检查。
4. 把 `(A,B):3` 重新分配为不同 local 拆分但总和不变，说明哪些输出不变、哪些 provenance 已变。
5. 回答：仅凭聚合结果能否恢复三条原始 trace？给出 claim ceiling。
