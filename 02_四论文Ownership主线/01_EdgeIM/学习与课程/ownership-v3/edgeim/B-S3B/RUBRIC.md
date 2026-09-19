# B-S3B Rubric

继承 [Common Rubric](../../RUBRIC_COMMON.md)。

| 维度 | 2 分条件 | hard gate |
|---|---|---|
| recursion | base/split/recurse/merge/termination 全部可追踪 | yes |
| source layers | EdgeIM、外部理论、PM4Py 行为严格分层 | yes |
| formal objects | DFG、process tree、Petri net、marking、language 不混同 | yes |
| no-invention | cut/priority/fall-through 未被冒充论文规则 | yes |
| soundness | 不用 fitness 或论文一句话替代 checker/proof | yes |
| unseen | 在新 oracle 结构上先预测后追踪 | yes |
| implementation | 版本、输入接口、输出与 claim ceiling 齐全 | no |

Hard fail：声称 EdgeIM 原文输出 process tree；声称 Algorithm 3 给出完整 IM；用一批 trace replay 证明模型语言等价或 soundness。
