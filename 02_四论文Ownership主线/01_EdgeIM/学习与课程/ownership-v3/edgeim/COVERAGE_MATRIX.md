# EdgeIM Full-Paper Coverage Matrix

| ID/对象 | 原文坐标 | 最低学习动作 | 验收动作 | 课程落点 | 当前状态 | 开放边界 |
|---|---|---|---|---|---|---|
| E-O01 problem/motivation | p.1 Abstract/section I | 闭卷重述对象、瓶颈和约束 | 改部署约束后重述问题 | B-DEFENSE | ASSET-COVERED / USER-NOT-ASSESSED | IoT 外推是作者 framing |
| E-O02 prior work | pp.1-2 sections I-II | 区分本文叙述与前作事实 | 对 EdgeAlpha 评价标源 | B-DEFENSE | ASSET-COVERED / USER-NOT-ASSESSED | 前作 primary 未取得 |
| E-O03 event-log/projection | pp.2-3 Definitions 1-2, Eq.1 | 定义对象与投影损失 | 未见 schema 指出保留/丢失 | B-S2 前置/B-DEFENSE | ASSET-COVERED / USER-NOT-ASSESSED | 不改既有 EX PASS |
| E-O04 weight | p.2 Definition 3, Eq.2-3 | 手算相邻关系次数 | 重复 relation 未见题 | B-S2 | ASSET-COVERED / USER-NOT-ASSESSED | trace/event multiplicity 分开 |
| E-O05 DFG | p.3 Definition 4 | 画 weighted DFG | 与 set-like R 对照 | B-S2/B-S3A | ASSET-COVERED / USER-NOT-ASSESSED | DFG 不等于模型语言 |
| E-O06 Petri net | p.3 Definition 5 | 列 tuple/marking/soundness 对象 | 识别排版矛盾 | B-S3B | ASSET-COVERED / USER-NOT-ASSESSED | 完整语义 SOURCE-OPEN |
| E-O07 Stage 1 interface | pp.3-4 section IV.A-B, Algorithm 1 | 回接既有本人证据 | 解释 D' 的 consumer | 既有 EX/B-S2 | ASSET-COVERED / USER-NOT-ASSESSED | 本目录不重教 |
| E-O08 Stage 2 | pp.3-4 section IV.A/C, Algorithm 2 | 手算并实现 local triplets | debug 型 holdout | B-S2 | ASSET-COVERED / USER-NOT-ASSESSED | hash/tie/transport 未规定 |
| E-O09 aggregation | p.5 Algorithm 3 lines 1-8 | union/sum 与信息损失 | implementation-audit holdout | B-S3A | ASSET-COVERED / USER-NOT-ASSESSED | weight 是否进 cut 未说明 |
| E-O10 discovery | p.5 Algorithm 3 lines 9-23 | 追踪递归 orchestration | unseen recursion/non-progress | B-S3B | ASSET-COVERED / USER-NOT-ASSESSED | cut/merge/fall-through 开放 |
| E-O11 protocol | pp.5-7 section V, Tables I-III | 重建实验合同 | 缺项逐一标 OPEN | B-EVAL | ASSET-COVERED / USER-NOT-ASSESSED | code/data/params 缺失 |
| E-O12 limits/conclusion | p.6 section VI；无独立 limits section | explicit/derived/open 分层 | 四档 defense | B-DEFENSE | ASSET-COVERED / USER-NOT-ASSESSED | reviewer inference 另标源 |

## Major claims

| Claim | 原文坐标 | 最低学习动作 | 验收动作 | source label | verdict | 当前状态 | 冻结 ceiling |
|---|---|---|---|---|---|---|---|
| E-C01 Stage 1 zero loss | p.4 section IV.B | 写 preserved/lost 表 | 给频次反例 | PRIMARY | DERIVED | CLAIM-MAPPED / USER-NOT-ASSESSED | start/end 与 unweighted DFR support |
| E-C02 hashing balances workload | p.4 section IV.C | 找直接证据 | 设计 node-load 检查 | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | 未测 node-load balance |
| E-C03 equal timestamps preserve concurrency | p.4 section IV.C | 重建双向机制 | coarse timestamp 反例 | PRIMARY | PROXY | CLAIM-MAPPED / USER-NOT-ASSESSED | bidirectional mechanism direct；accuracy 未测 |
| E-C04 fitness comparable to IM | pp.5-6/Table II | 逐日志读取 | 指出 fightCar 差异 | PRIMARY | DIRECT | CLAIM-MAPPED / USER-NOT-ASSESSED | 限九日志/未知参数 |
| E-C05 precision about 40% | p.5/Table II | 对 Sepsis/BPI2013 复算 | 分别裁定 | PRIMARY | CONFLICT | CLAIM-MAPPED / USER-NOT-ASSESSED | 约 40% 与约 6.2% |
| E-C06 F comparable/superior | p.6/Table II | 全九日志 win/tie/loss | 禁止只报胜例 | PRIMARY | CONFLICT | CLAIM-MAPPED / USER-NOT-ASSESSED | mixed |
| E-C07 loops and sound models | p.6 section V.B | 区分 fitness/soundness | 写 proof obligation | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | soundness 未直接测 |
| E-C08 faster across all datasets | p.6/Table III | 复算 total | 找 exercise 反例 | PRIMARY | CONFLICT | CLAIM-MAPPED / USER-NOT-ASSESSED | exercise 反例，文本过宽 |
| E-C09 lower communication | p.6 section V.C | 查 bytes/messages | 无字段写 NONE | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | 未直接测 |
| E-C10 privacy-preserving | p.6 section VI | 写 threat-model 缺口 | 攻击者/泄漏题 | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | 未定义、未测 |
| E-C11 superior scalability | pp.6 section V.C-VI | 区分 runtime/scaling | 设计 k/size sweep | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | 单机有限日志不足 |
| E-C12 timestamp improves reliability | p.6 section VI | 分开机制与因果 | 要求 ablation | AUTHOR-FRAMING | UNSUPPORTED | CLAIM-MAPPED / USER-NOT-ASSESSED | 因果收益未隔离 |
