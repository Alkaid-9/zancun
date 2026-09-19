# B-EVAL Rubric

继承 [Common Rubric](../../RUBRIC_COMMON.md)。

| 维度 | 2 分条件 | hard gate |
|---|---|---|
| protocol | data/preprocess/miner/params/env/repeats/output/metric 全列且缺失标 OPEN | yes |
| arithmetic | F、relative change、total time 可复算 | yes |
| all claims | 主要 claim 全覆盖并有坐标 | yes |
| causal validity | runtime 不冒充 communication/privacy/scalability/soundness | yes |
| contradictions | 至少一处冲突被正确收窄 | yes |
| reproduction ceiling | 不把局部复算写成全文复现 | yes |
| unseen | holdout 先预测后检查 | yes |
| source hygiene | PDF、作者解释、derived、teardown 分层 | yes |

## 冻结 reproduction contract

| 字段 | 本课程冻结值/状态 | 2 分判定 |
|---|---|---|
| data | Table I 的九个日志名与表内统计可逐格引用；entity URI、下载时间、版本、checksum 为 `REPRO-CONTRACT-OPEN` | 不把同名日志当已锁版本；缺 entity 不称 reproduction-ready |
| preprocessing | 论文给 Stage 1/投影机制；case ordering、schema mapping、node/hash mapping、清洗与 failure policy 未完整公开 | 逐项写确定规则与 OPEN，不自行补默认值 |
| miner variants | 论文比较 AM、IM、EdgeAlpha、EdgeIM；具体 PM4Py class/version/preset 与 EdgeAlpha/EdgeIM code revision 未公开 | 名称与实现版本分开；本机 PM4Py 不回填原实验 |
| parameters | sampling/order/hash/timestamp、cut/fall-through、miner/evaluator 参数未形成可重放配置 | 所有缺项显式 OPEN；不得用 library defaults 代填 |
| environment/repeats | PDF physical p.5 section V.A 的 CPU/OS 描述与 5-run average 可引用；完整 dependency/container、raw runs、variance 缺失 | 保留硬件表述冲突和 raw-run 缺口 |
| model artifacts | 完整重放至少需每 run 的 discovered PN、initial/final marking、failure/timeout status；本地论文包未提供 | 无 artifact 不评 soundness/replay 细节，不把 `-` 数值化 |
| metric implementation | Eq. (4) 固定 `F=2fp/(f+p)`；fitness/precision 的具体 implementation/version/cost semantics 未公开 | F 可复算；底层 metric 实现保持 OPEN |
| allowed difference | synthetic fixture 的 F/mean/speedup 绝对误差 `<=1e-4`；论文表格转录匹配印刷精度 | paper-level rerun tolerance 在 raw scale/variance 未知时保持 OPEN，不临场放宽 |

任何必要字段为 OPEN 时，结论必须写 `REPRO-CONTRACT-OPEN`；这不阻止局部表格复算，但阻止“整篇复现完成”。

Hard fail：虚构参数；把 fitness 当 soundness；声称论文测量了通信字节或隐私；把七个可运行日志写成九个全胜；在 reproduction contract 未闭合时声称 full reproduction。
