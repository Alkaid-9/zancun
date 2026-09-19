# B-S2 Rubric

继承 [Common Rubric](../../RUBRIC_COMMON.md)。

| 维度 | 2 分条件 | hard gate |
|---|---|---|
| 对象分离 | 明确 Stage 1 `R` 是 support set，Stage 2 `R_i` 是重算计数 | yes |
| 分派 | 每个 event 的 `j`、写入哪个局部状态均正确 | yes |
| 状态追踪 | `S_i/E_i/R_i` before/update/after 可逐行复查 | yes |
| timestamp | 两事件同刻双向累计正确；三事件同刻保持 OPEN | yes |
| 实现 | 映射、零默认、顺序策略显式，测试覆盖要求项 | yes |
| 来源纪律 | 论文规则、实现 policy、未知项未混写 | yes |
| unseen transfer | holdout 先预测后检查且能解释 miss | yes |
| 全文回接 | 能说明 local weights 如何成为 Stage 3 输入 | no |

Hard fail：把 `hash(activity) mod k` 写成已经证明负载均衡；把关系计数从 Stage 1 直接复制；为未规定 tie policy 编造标准答案。
