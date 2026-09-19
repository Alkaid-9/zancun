# B-DEFENSE Rubric

继承 [Common Rubric](../../RUBRIC_COMMON.md)。

| 维度 | 2 分条件 | hard gate |
|---|---|---|
| full paper | problem/method/eval/limits/conclusion 均覆盖 | yes |
| compression invariance | 三档长度变化不改变 claim ceiling | yes |
| source attribution | EdgeIM text 与 predecessor primary 不混同 | yes |
| limitations | explicit/derived/external-open 分层 | yes |
| adversarial response | 能守住支持项并明确让步 | yes |
| D1 | 未见链路题完整且不靠 teardown | yes |
| retention | D+2/D+7 变体通过后才从 PASS 进入 RETAINED | no (RETAINED gate) |
| ownership language | 不夸大独立复现或贡献 | yes |

Hard fail：将 EdgeAlpha 评价写成独立核验事实；把 privacy/scalability/soundness 写成已证实；30 秒版本用更强主张换取简短。
