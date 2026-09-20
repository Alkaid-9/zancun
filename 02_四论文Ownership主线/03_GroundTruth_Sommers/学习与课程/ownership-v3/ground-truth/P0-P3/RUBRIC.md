# Ground Truth P0-P3 Rubric

继承 [Common Rubric](../../../../../00_共享合同_计划_验收/学习与课程/ownership-v3/RUBRIC_COMMON.md)。

| 维度 | 2 分条件 | hard gate |
|---|---|---|
| full coverage | RQ/requirements/method/DS/AQ/results/limits/conclusion 齐全 | yes |
| formal roles | `M0/M^S/M^L/L'/pi/h/Psi` 不混同 | yes |
| cause separation | BI/RI/randomness/projection/sampling 分开 | yes |
| generator/consumer | 每对象谁生成、谁消费、谁可见明确 | yes |
| unseen world | 结构变体先预测后检查 | yes |
| protocol | DS1-3 与 AQ1-3、缺失复现字段正确 | yes |
| EdgeIM transfer | 能套/不能套具体到 operator/parameter | yes |
| oracle hygiene | sampler 不见 oracle，target 预声明 | yes |
| claim ceiling | 不夸大 qualitative demo | yes |
| retention | D+2/D+7 完成后才从 PASS 进入 RETAINED | no (RETAINED gate) |

Hard fail：把 sampling 当 BI/RI；把 `M'`、`M^L`、`L'` 混写；把 oracle tag 喂给 sampler；声称论文实验评估了 EdgeIM。
