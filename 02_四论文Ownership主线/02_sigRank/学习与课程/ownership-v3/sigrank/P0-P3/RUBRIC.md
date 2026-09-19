# sigRank P0-P3 Rubric

继承 [Common Rubric](../../RUBRIC_COMMON.md)。

| 维度 | 2 分条件 | hard gate |
|---|---|---|
| full coverage | 九类 coverage 与全部 major claims 齐全 | yes |
| formal correctness | Definitions/Eq.1-8、multiplicity、position average 正确 | yes |
| mechanism | Step 1-4 与 Phase 2 可在未见题执行 | yes |
| open policies | rounding/tie/duplicate/singleton 不伪造 | yes |
| experiment | data/method/ratio/miner/metric/repeat/time 完整 | yes |
| errata | 三条已知转录错误不传播 | yes |
| claim ceiling | aggregation/comparator 与证据强度准确 | yes |
| fair comparison | matched interface/cost 明确且 F 不乱并表 | yes |
| attack | 预测先于检查，因果解释成立 | no |
| retention | D+2/D+7 完成后才从 PASS 进入 RETAINED | no (RETAINED gate) |

Hard fail：把 prose Step 1-4 叫正式 Algorithm；说 Eq.4/5 对重复 position 只算一次；直接采用 teardown 错数；宣称实验保证所有日志/矿工下质量。
