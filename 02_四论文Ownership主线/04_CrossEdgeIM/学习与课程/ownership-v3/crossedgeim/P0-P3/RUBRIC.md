# CrossEdgeIM P0-P3 Rubric

继承 [Common Rubric](../../../../../00_共享合同_计划_验收/学习与课程/ownership-v3/RUBRIC_COMMON.md)。

| 维度 | 2 分条件 | hard gate |
|---|---|---|
| authorship | 五位作者与鲁法明边界准确 | yes |
| full coverage | problem/method/all visuals/eval/limits/conclusion 齐全 | yes |
| I/S/delta/O | 三层输入、状态、更新、输出、consumer 正确 | yes |
| open semantics | transport/clock/lifecycle/remerge 不伪造 | yes |
| unseen update | 结构变体先预测后追踪 | yes |
| evidence | protocol、公式、全部 major claims 与 ceiling 正确 | yes |
| genealogy | author framing 与独立 verdict 分开 | yes |
| residual | interaction/multimodal/semantic loss 具体 | no |
| attack/defense | assumption、falsifier、让步边界齐全 | yes |
| retention | D+2/D+7 完成后才从 PASS 进入 RETAINED | no (RETAINED gate) |

Hard fail：归错作者；把架构推论写成通信/隐私测量；声称 local PN merge 已证明全局 behavioral completeness；把活动改名当未见结构题。
