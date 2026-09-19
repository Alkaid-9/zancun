# B-S3A Rubric

继承 [Common Rubric](../../RUBRIC_COMMON.md)。

| 维度 | 2 分条件 | hard gate |
|---|---|---|
| union/sum | endpoints 幂等 union、关系计数加法不混淆 | yes |
| 状态表 | 每个 local 的贡献可追踪 | yes |
| 实现不变量 | 节点排列与空节点不改变聚合结果 | yes |
| 信息边界 | 保留与丢失信息逐项明确 | yes |
| weight ceiling | 不声称未公开的 cut-weight 用法 | yes |
| unseen | 先预测后检查结构变体 | yes |
| consumer | 能说明 weighted DFG 到 B-S3B 的接口 | no |

Hard fail：把 union 用于关系计数；把 sum 用于 endpoint 集合；把局部来源仍可恢复写成既定事实。
