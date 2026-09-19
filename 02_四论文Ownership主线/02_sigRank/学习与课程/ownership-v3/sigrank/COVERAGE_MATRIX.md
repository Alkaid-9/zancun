# sigRank Full-Paper Coverage Matrix

| ID/对象 | 原文坐标 | 最低学习动作 | 验收动作 | 阶段 | 当前状态 | 开放边界 |
|---|---|---|---|---|---|---|
| S-O01 problem | p.1 Abstract/section I | 闭卷重述效率-质量问题 | 改 consumer 后重述 | P0 | ASSET-COVERED / USER-NOT-ASSESSED | guarantee 过强 |
| S-O02 prior work | pp.1-2 sections I-II | 画 predecessor/gap | 标 AUTHOR-FRAMING | P0/P3 | ASSET-COVERED / USER-NOT-ASSESSED | primary 未核 |
| S-O03 formal objects | pp.2-4 Definitions 1-6 | 定义六对象 | multiplicity 边界题 | P0/P1 | ASSET-COVERED / USER-NOT-ASSESSED | activity sequence only |
| S-O04 Phase 1 | pp.3-5 Eq.2-6/Step 1-4 | 手算与实现 | debug 型 holdout | P1 | ASSET-COVERED / USER-NOT-ASSESSED | rounding/tie open |
| S-O05 Phase 2 | pp.3,5-6 Eq.1,7-8 | quality/efficiency dataflow | 改 metric/denominator | P1/P2 | ASSET-COVERED / USER-NOT-ASSESSED | evaluator open |
| S-O06 tool | p.6 section V/Fig.5 | artifact contract | 缺 version 标 OPEN | P2 | ASSET-COVERED / USER-NOT-ASSESSED | plugin runtime open |
| S-O07 protocol | pp.6-7 VI.A-C/Table I | 12 logs/9 methods/ratios | 协议缺口题 | P2 | ASSET-COVERED / USER-NOT-ASSESSED | params/env missing |
| S-O08 results | pp.7-11 Table II/Fig.6/Table III | 复算与 errata | 新 aggregation rule | P2 | ASSET-COVERED / USER-NOT-ASSESSED | counting unresolved |
| S-O09 limits/conclusion | pp.2,11-12 | map/attack/defense | rare-critical 变体 | P0/P3 | ASSET-COVERED / USER-NOT-ASSESSED | generalization limits |

## Major claims

| Claim | 原文坐标 | 最低学习动作 | 验收动作 | source label | verdict | 当前状态 | 冻结 ceiling |
|---|---|---|---|---|---|---|---|
| S-C01 efficient without quality loss/guarantee | p.1 | 拆 efficiency/quality | rare-critical 反例 | PRIMARY | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | 条件化，不是保证 |
| S-C02 15% LC illustration | pp.5-6 Figs.1/4 | 重算 F | 不外推 | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | 单例 |
| S-C03 O(n log n) | p.5 | 展开 n,m | 检查 O(nm+nlogn) | PRIMARY | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | 论证不足 |
| S-C04 highest F 10/12 | p.7 prose；p.8 Table II | 三口径复算 | 解释无一得 10 | PRIMARY | CONFLICT | CLAIM-MAPPED / USER-NOT-ASSESSED | counting rule OPEN |
| S-C05 beats Similarity 8/12 | p.8 Table II | 六-ratio mean | win/loss/tie | PRIMARY | DERIVED | CLAIM-MAPPED / USER-NOT-ASSESSED | 该口径支持 |
| S-C06 beats/alternates IMi 8/12 | p.7 prose；p.8 Table II | all-ratio/mean/any-win 分开 | 禁止合并 | PRIMARY | DERIVED | CLAIM-MAPPED / USER-NOT-ASSESSED | all-six=5/12；mean=6/12；any-win=8/12 |
| S-C07 Similarity beats Frequency 9/12 | p.7 prose；p.8 Table II | 六-ratio mean 重算 | win/loss/tie | PRIMARY | CONFLICT | CLAIM-MAPPED / USER-NOT-ASSESSED | 该口径为 7/4/1 |
| S-C08 lowest time 9/12 | p.11/Table III | 核对 12 rows | 列三例外 | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | table-supported |
| S-C09 LogRank about 100x | p.11 | 定位 comparator | 无依据标 OPEN | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | comparator SOURCE-OPEN |
| S-C10 rare-important limitation | p.11 VI.D | 改 objective 预测 | attack holdout | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | explicit limitation |
