# Ground Truth Approach Full-Paper Coverage Matrix

| ID/对象 | 原文坐标 | 最低学习动作 | 验收动作 | 阶段 | 当前状态 | 开放边界 |
|---|---|---|---|---|---|---|
| G-O01 problem/RQ | pp.1-3,8 | 重述因果 GT 需求 | 改评估任务后重述 | P0 | ASSET-COVERED / USER-NOT-ASSESSED | complete/quantitative 过强 |
| G-O02 related work | pp.3-5/Fig.1 | 分类来源 | 前作标源 | P0 | ASSET-COVERED / USER-NOT-ASSESSED | primary 未核 |
| G-O03 requirements | pp.5-8/Table 1 | 三需求映射 | 指出未覆盖项 | P0 | ASSET-COVERED / USER-NOT-ASSESSED | model diversity out of scope |
| G-O04 world chain | pp.8-9 | 重建 M0/MS/ML/L' | oracle-leak contract holdout | P1 | ASSET-COVERED / USER-NOT-ASSESSED | course suffix 另标源 |
| G-O05 transform | pp.13-14 Eq.1/Figs.4-5 | 手推 Psi/pi/h | 区分 M'/ML/L' | P1 | ASSET-COVERED / USER-NOT-ASSESSED | blueprint 部分外引 |
| G-O06 BI/RI | pp.6-7,10-13/Tables 1-2 | 分类 operators | unseen operator | P1 | ASSET-COVERED / USER-NOT-ASSESSED | stale numbering |
| G-O07 simulation | pp.15-17 Eq.2 | 参数/seed/consumer | 改参数预测 | P1 | ASSET-COVERED / USER-NOT-ASSESSED | exact params open |
| G-O08 DS1-3 | pp.17-23/Figs.6-10 | 重建组合与用途 | 指出只评 DS1 | P2 | ASSET-COVERED / USER-NOT-ASSESSED | DS2/3 scale missing |
| G-O09 protocol/results | pp.23-27/Table 3/Fig.12 | AQ1-3 与三方法 | claim audit | P2 | ASSET-COVERED / USER-NOT-ASSESSED | raw/variance missing |
| G-O10 limits/conclusion | pp.27-28 | explicit/derived 分层 | defense | P3 | ASSET-COVERED / USER-NOT-ASSESSED | realism open |

## Major claims

| Claim | 原文坐标 | 最低学习动作 | 验收动作 | source label | verdict | 当前状态 | 冻结 ceiling |
|---|---|---|---|---|---|---|---|
| G-C01 linked world supports task-specific GT | pp.8-9 | 画 provenance | hidden/visible 变体 | PRIMARY | PROXY | CLAIM-MAPPED / USER-NOT-ASSESSED | framework + qualitative demo |
| G-C02 additive patterns preserve base | p.13 | 标 AUTHOR-FRAMING | 组合反例 | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | 无 theorem/systematic test |
| G-C03 n*m*k families | pp.17-23 | 重建轴 | 对 examples 检查 | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | design；examples sparse |
| G-C04 DS1 approximable by existing methods | p.19 | 对照 novelty | ceiling | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | method structure |
| G-C05 interacting/duplicate cases unavailable elsewhere | pp.22-23 | source boundary | 前作未核标 OPEN | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | author argument |
| G-C06 detection/explanation results | pp.24-27/Table 3 | 逐 method/issue | 找 conflation | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | DS1 qualitative CC |
| G-C07 each RI detected by each method | p.24 | 与 RI_mi 句对照 | internal conflict | PRIMARY | CONFLICT | CLAIM-MAPPED / USER-NOT-ASSESSED | internal conflict |
| G-C08 timing depends on pattern | pp.25,27/Fig.12 | qualitative order | 不报精确柱值 | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | no variance |
| G-C09 exponential increase | pp.25,28 | 找 size axis | 无则 UNSUPPORTED | PRIMARY | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | scaling law 未证 |
| G-C10 quantitative and qualitative insight | pp.1,28 | 对照 future work | 收窄 | PRIMARY | CONFLICT | CLAIM-MAPPED / USER-NOT-ASSESSED | mainly qualitative |
| G-C11 GT indispensable | p.27 | useful/unique 分开 | 替代 oracle 追问 | PRIMARY | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | useful not unique |
| G-C12 formalism/params/pattern limits | p.28 | 列 explicit limits | attack | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | author-explicit |
