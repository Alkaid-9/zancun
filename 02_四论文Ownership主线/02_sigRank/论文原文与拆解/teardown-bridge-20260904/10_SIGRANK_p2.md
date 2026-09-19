Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# 10 · sigRank（TSC 2026）第一性原理全拆（下：§5–§9）—— 桥线 T1 辅助篇

> 主输入：`research/papers_lu/sigRank-2026-TSC.pdf`（13 页），`[PDF p.N]` 为物理页，印刷页 = 1605 + N（换算表见上半部 `10_SIGRANK_p1.md` 第 23 行）。上半部 §0–§4 不重复，只引其行号（记作 p1:L#）。
> 判定依据：p.7 整页 `Read` 判读 + 文本层定位（`_launch/pdftxt/SIGRANK.txt` 仅定位）。Table I/II/III 为图像嵌入，文本层无数字（SIGRANK.txt 第 351–360、463–465、482–484 行只有表题）。
> 边界声明：本篇不与 EdgeIM 做任何机制比较、不转述 EdgeIM；不读 bridge 卡。§9 只写 sigRank 在桥线中的辅助角色。

---

## 5. 实验协议与结果批判

### 5.1 协议（逐项标页）

- **数据集**：12 个公开日志，6 合成 + 6 真实 [PDF p.6 VI.A]；Table I 列 = #Trace、#Event、#Variant、#Activity [PDF p.6 Table I 表题]。变体数跨度 9–2513（p1:L70）。原文点名的日志：Final（相似度式与频次式 F-measure 相同的例外）[PDF p.7 右栏]、trainingLog7（sigRank 被反超）[PDF p.7 右栏末段]、BPI2012_A（LogRank 采样 141549 ms）[PDF p.11 左栏；p1:L67]。数据来源 URL：文本层未见，`[需验证]`。
- **对比方法**：7 个采样基线 + 1 个过滤式发现 [PDF p.6 右栏–p.7 左栏]：LogRank [24]（PageRank 图排序）；LogRank+ [14]（迹对其余全部迹的相似度，取主流迹）；Frequency-based [25]（按频次取最频繁迹）；Similarity-based [25]（先算 DFR 及其权重，权重超过**输入阈值**者为主流行为，迹相似度 = 所含主流 DFR 个数）；Hybrid-based [25]（频次与相似度归一到 [0,1] 后加权平均）；Longer-based [25]（按变体长度取最长，"leaves out incomplete traces"）；Shorter-based [25]（取最短，"may keeps variants with simpler behavior"）；IMi [20]（IM 各阶段加不频繁行为过滤）。
- **比例网格**：30% → 5%，步长 −5%，共 6 档 [PDF p.7 左栏 VI.C 首段]。IMi 以 noise_threshold 0.70 → 0.95（步长 +0.05）对齐，规则 θ = 1 − r，"not tuned for each event log" [PDF p.7 左栏]。
- **下游发现算法**：固定 IM；理由 "produces sound, block-structured models with deterministic outputs and exhibits strong robustness to noise, which isolates the effect of sampling" [PDF p.7 左栏]。跨算法（Heuristics Miner、ILP）留作未来工作 [PDF p.7 左栏]。
- **指标**：fitness、precision、F-measure，均以样本模型对**原日志**计算 [PDF p.7 左栏]；效率 = 采样时间（Fig. 6，"quantifying their respective sampling time"）[PDF p.7 右栏] 与 采样 + 发现总时间（Table III，单位毫秒，跨 6 档比例取均值，逐日志最优加粗）[PDF p.11 Table III 表题及右栏]。
- **重复次数**："run each sampling technique five times for a given sampling ratio and report the average values" [PDF p.7 右栏]。
- **聚合口径**："Unless otherwise stated, results per dataset are averages across the six settings for each technique" [PDF p.7 左栏]；Table II 表题却写 "across sampling ratios (5% - 30%, step -5%)" [PDF p.8 表题]——是逐档列示还是均值，表题与正文口径不一，`[需验证：待 Table II 逐格]`。表题 "5% - 30%, step -5%" 方向与步长自相矛盾（排版）。
- **硬件**：文本层 grep（GHz/RAM/Intel/CPU/machine）无命中，p.7 整页判读亦无 → 原文未给硬件配置 `[需验证]`。
- **统计检验**：无。文本层 grep（t-test/p-value/deviation/variance）无命中；5 次重复只报均值，未报方差 [PDF p.7 右栏]。

### 5.2 Table I 数据集统计逐格抄录 [PDF p.6]

`[待补]` 表为图像嵌入；本轮单页渲染未能在写盘时回放到逐格数值，按铁律 1/2 不凭记忆填数。已确认的骨架：12 行 × 4 列（#Trace / #Event / #Variant / #Activity）[PDF p.6 表题]；#Variant 极值 9 与 2513（p1:L70）。

### 5.3 Table II 质量对比逐格抄录 [PDF p.8]

`[待补]` 同上。已确认骨架：行 = 12 日志；列 = LogRank、LogRank+、sigRank、Frequency、Similarity、Hybrid、Longer、Shorter、IMi 共 9 法 [PDF p.7 右栏列举]；格值 = F-measure，"higher is better" [PDF p.8 表题]；比例 6 档 [PDF p.8 表题]。"-" 含义：表注未在文本层出现，`[待补]`。

### 5.4 Fig. 6 采样时间曲线 [PDF p.9–10]

`[待补·图读数]` 两整页折线图，横轴比例、纵轴时间；数值需图读。文本层仅有 "Fig. 6. Time performance comparison results." 与 "Continued."（SIGRANK.txt 第 471、478 行）。

### 5.5 Table III 总时间逐格抄录 [PDF p.11]

`[待补]` 已确认骨架：格值 = 采样时间 + 发现时间，毫秒，跨 30%→5% 六档均值，逐日志最低加粗 [PDF p.11 表题]。IMi 无采样步骤，其"总时间"如何计入 `[需验证]`。IV.A 定义的效率判据 t_sample + t_disc(L_S) < t_disc(L_0)（p1:L46）是否在 Table III 中以 t_disc(L_0) 列显式对照，`[需验证]`。

### 5.6 支撑住的结论（以原文自报计数为限）

1. sigRank 在 12 日志中 10 个取得最高 F-measure（相对 LogRank/LogRank+）——原句 "Table II shows that sigRank attains the highest F-measure (10/12)" [PDF p.7 右栏]。计数是作者自报，逐格核验待 5.3。
2. 相对 Similarity-based，8/12 更好 [PDF p.7 右栏 "performs better in most cases (8/12)"]。
3. 相对 IMi，8/12 更好或"随比例交替" [PDF p.7 右栏]。
4. 总时间 9/12 最低 [PDF p.11 右栏]；LogRank 在 BPI2012_A 上采样 141549 ms、约 100 倍于其他方法，归因于逐对相似度 + PageRank [PDF p.11 左栏；p1:L67]——效率优势方向与 §4 复杂度声明（p1:L153）一致。
5. 作者对失效场景的自认是实的：trainingLog7 类日志 "(i) many unique or low-frequency variants and sparse, weakly connected directly-follows relations; (ii) rare structural patterns that frequency-weighted signals capture poorly" [PDF p.7 右栏末段]；"sigRank prioritizes statistically dominant activities and relations ... which can under-sample rare but informative variants" [PDF p.11 左栏]。

### 5.7 没撑住的 claim（逐条）

1. **"achieves the best sample log quality and sampling efficiency" [PDF p.11 右栏总结句；p.12 结论 "guaranteeing superior sample log quality"]**——自家计数是 10/12、8/12、8/12、9/12，且 IMi 在 "substantial noise or unstable control-flow" 日志上更好 [PDF p.11 左栏]。"best/guaranteeing" 是全称表述，证据是多数票。
2. **"Each method performs best on six event logs"（LogRank vs LogRank+）[PDF p.7 右栏]**——6 + 6 = 12 意味着无并列，与 Final 日志上出现并列的事实（同段）相冲突，计数规则未说明 `[需验证]`。
3. **"exhibits alternating performance depending on the sampling ratio"（对 IMi）[PDF p.7 右栏]**——承认结果随比例翻转，但 Table III 与"per dataset averages"把 6 档压成一个数 [PDF p.7 左栏；p.11 表题]，比例依赖被均值抹平；逐档赢输表原文未给。
4. **5 次重复无方差、无检验 [PDF p.7 右栏]**——毫秒级时间对比（Table III）在无硬件、无方差条件下不可复现，`[需验证]`。
5. **IMi 对照的时间口径不对等**：Table III 定义为"采样 + 发现" [PDF p.11 表题]，IMi 无采样步骤；若只计发现时间，则 9/12 的分母里含一个不同口径的对手 `[需验证]`。
6. **等权 0.5/0.5 无消融**（p1:L90）与 **比例 r 无选取指导**（p1:L74）——Threats 第三条自认固定 5–30% "may not generalize well" [PDF p.11 右栏]。
7. **"thousands of variants" 动机与数据错位**（p1:L70）——仅引，不重复。

## 6. Potential flaw

### 6.1 情境局限与延伸架构

- **只读活动序列** [PDF p.2 III.A 末段；p1:L37]：资源、时间戳、成本全部丢弃。延伸：多视角显著性（活动 × 资源 × 时段）。
- **单一下游算法**：只验 IM，作者自认 "especially compatible with discovery approaches that rely on directly-follows relations" [PDF p.7 左栏]；对 Heuristics Miner/ILP 未测 [PDF p.7 左栏]。延伸：把"显著性单位"参数化到下游算法所消费的关系类型。
- **批处理、全量两遍扫描**：sig 需先遍历 L_0 得全局支持度 [PDF p.5 Step 1–2]，无增量/流式版本。延伸：增量维护支持度计数与 top-N 堆。
- **质量判据部署悖论**（p1:L73）——仅引。
- **选择单位口径不一**（迹计数 vs 变体各一，p1:L156 `[⚠️矛盾]`）——在高重复日志上两种口径的样本可以完全不同（见 6.2）。

### 6.2 坏数据性质下的困难

- **高重复日志**（少数变体占绝大多数迹）[推断，由式 (2)–(6) 直接得出]：主导变体的每个活动/DFR 支持度都最高，其全部副本 sigTotal 并列第一；若按迹计数取 top-N（Fig. 3 口径，p1:L156），r·|L_0| 个名额可被单一变体的副本填满，样本变体数塌到 1，IM 发现出顺序模型，对 L_0 的 fitness 下降。若按变体各取一份（L_C 口径），则正相反。原文未给样本变体数统计 `[需验证]`。
- **长尾变体**：作者自认 [PDF p.7 右栏末段；p.11 左栏]。长度归一化（p1:L92）把"含一个罕见活动的长迹"整体拉低，尾部行为在任何比例下都排在末尾。
- **噪声**：噪声事件制造低支持度活动/DFR，含噪迹被排到末尾——sigRank 客观上是噪声过滤器 [推断]。但作者称 IMi 在 "substantial noise or unstable control-flow" 上更好 [PDF p.11 左栏]；两者张力的解释 [推断]：sigRank 按迹整条丢，噪声与合法罕见行为一起丢；IMi 按边过滤，可保留迹主体。
- **并发**：并行块产生多种交错，每种交错特有的 DFR（如 ⟨b,c⟩ 与 ⟨c,b⟩）支持度被摊薄；若样本只保留高支持度交错，IM 看不到反向 DFR，会把并行判成顺序（precision 升、fitness 降）[推断]。L_C 算例中 15% 样本仍复现了并行块（p1:L175）[PDF p.6 左栏]，但那是 75 迹小例，规模化证据无。
- **单事件迹**：式 (5) 分母为 0（p1:L205）——仅引。

### 6.3 哪个困难值得写 paper [推断]

首选：**带覆盖约束的显著性采样**——在 top-N 之外加一个硬约束"dfgS(L_S) ⊇ 支持度 ≥ ε 的 DFR 集合"，使样本对 DFG 类算法的可再发现性有可陈述的保证。理由：原文自己把 "model re-discoverability" 当卖点 [PDF p.6 左栏]，结论又把 "sampling techniques that preserve behavioral invariants" 列为 "critical direction" [PDF p.12 左栏]，问题定义与评测协议（§5.1）现成。次选：**比例自适应停止**（以 DFR 覆盖饱和替代固定 r），直接回应 Threats 第三条 [PDF p.11 右栏]。

## 7. Motivation 还原（问句形式，从远到近）

1. 大日志上集中式发现为什么慢，而分布式重编程为什么不划算？[PDF p.1 引言；p.2 II.B]
2. 不改发现算法、只缩小输入，能否把发现时间降下来又不伤模型？[PDF p.1 摘要；p.3 IV.A]
3. "不伤模型"怎么量化？——样本模型对原日志的 F-measure 相对原模型的比值 [PDF p.3 式 (1)；p.5 式 (8)]。
4. 已有排序式采样为什么自己也慢？——逐对相似度 + 迭代排序 [PDF p.2 II.C；p.11 左栏]。
5. 迹的重要性能否不经迹间比较、只由迹内成分决定？[PDF p.4 IV.B 首段]
6. 用哪些成分？——活动与 DFR，因为 IM/Split Miner 消费 DFR [PDF p.7 左栏]。
7. 成分的重要性按事件频次还是按含它的迹数占比？——后者 [PDF p.4 式 (2)(3)]。
8. 两个分量怎么合成？——等权，"avoids bias toward either" [PDF p.4 式 (6) 下]。
9. 采样 + 样本发现的总时间是否真低于原日志发现？[PDF p.3 IV.A；p.11 Table III]

## 8. 张力结构分析

| # | 张力 | 拉向 A | 拉向 B | 作者选了 | 证据页 |
|---|---|---|---|---|---|
| 1 | 显著性 vs 覆盖 | 主流行为、效率 | 罕见变体、多样性 | A，且自认代价 | [PDF p.4 IV.B；p.11 左栏] |
| 2 | 支持度 vs 事件频次 | 循环不被放大 | 频次反映行为强度 | 支持度 | [PDF p.4 式 (2)(3)] |
| 3 | 长度归一化 vs 累加 | 长迹不占优 | 长迹含更多行为 | 归一化 | [PDF p.4 式 (4)(5)；症状 p.7 右栏末段] |
| 4 | 等权 vs 调参 | 简单、无偏 | 数据自适应 | 等权，无消融 | [PDF p.4 式 (6) 下] |
| 5 | 迹级 top-N vs 变体级 | 保留主流重数 | 覆盖更多变体 | 两处口径不一 | [PDF p.5 Fig. 3 vs 右下算例；p1:L156] |
| 6 | 固定比例 r vs 质量驱动停止 | 可控、可比 | 逐日志最优 | 固定网格 | [PDF p.5 Step 4；p.11 Threats] |
| 7 | 单算法 IM vs 跨算法 | 隔离采样效应 | 外推力 | IM | [PDF p.7 左栏] |
| 8 | 采样（可复用样本）vs 发现时过滤 IMi | 样本可复用于多任务 | 噪声日志上质量更高 | 采样，以"reusable sampled log"为由 | [PDF p.11 左栏] |
| 9 | 跨比例均值 vs 逐比例 | 一张表可读 | 暴露比例依赖 | 表用均值、图用逐比例 | [PDF p.7 左栏；p.9–11] |

## 9. 桥线定位注记

**角色**：T1 论文集辅助篇——"事件日志采样"子线的期刊态代表，供桥线做**采样邻近方法与定位**：提供该子线的基线家族清单（§5.1）、评测协议与作者自报的失效条件（§5.6 第 5 条）。不做与 EdgeIM 的机制比较；需要指向 EdgeIM 时，见 EdgeIM 原文 §IV.B，用户自读。sigRank 原文对 EdgeIM 仅一处并列引用（p1:L84）`[sigRank 原文转述，非 EdgeIM 原文]`。

**通用词汇表（术语 → 原文定义页）**：
- event log / trace / multiset B(U_A*) → Def 1 [PDF p.2]；process discovery Θ → Def 2 [PDF p.3]；sampling technique Π、L_s ⊆ L_0 → Def 4 [PDF p.3]。
- activity set actS(L) → Def 5 [PDF p.4]；directly-follows relation set dfgS(L) → Def 6 [PDF p.4]。
- significance of activity / DFR（含它的迹数占比）→ 式 (2)(3) [PDF p.4]；sigAvgAct / sigAvgDfr / sigTotal → 式 (4)–(6) [PDF p.4]。
- sampling ratio r、top-N → [PDF p.3 IV.A；p.5 Step 4]。
- sample-log quality Qua/Quality（F-measure 比值）→ 式 (1) [PDF p.3]、式 (8) [PDF p.5]；fitness / precision 口径 → [PDF p.5 右栏]。
- efficiency criterion t_sample + t_disc(L_S) < t_disc(L_0) → [PDF p.3 IV.A]；sampling time / discovery time / sum time → Fig. 2 [PDF p.4]、Table III [PDF p.11]。
- model re-discoverability → [PDF p.6 左栏]；mainstream behavior（DFR 权重超阈值）→ [PDF p.7 左栏 Similarity-based]；noise_threshold θ = 1 − r → [PDF p.7 左栏]；training-free heuristic → [PDF p.2 II.C 末段]。
- under-sample rare but informative variants / reusable sampled log → [PDF p.11 左栏]；behavioral invariants（未定义，仅作未来方向）→ [PDF p.12 左栏]。

**值得桥线借用的实验设置（只列）**：
1. 12 日志 = 6 合成 + 6 真实，四列统计 [PDF p.6 Table I]。
2. 比例网格 30%→5% 步长 5%，六档 [PDF p.7 左栏]。
3. 过滤式发现以 θ = 1 − r 对齐采样比例，不逐日志调参 [PDF p.7 左栏]。
4. 每档 5 次重复取均值 [PDF p.7 右栏]。
5. 质量 = 样本模型对原日志 F-measure / 原模型 F-measure [PDF p.5 式 (8)]。
6. 时间 = 采样 + 发现（毫秒）跨档均值表 + 逐档曲线图双呈现 [PDF p.11 Table III；p.9–10 Fig. 6]。
7. 固定 IM 为下游以隔离采样效应，并明说局限 [PDF p.7 左栏]。
8. 点名困难日志（trainingLog7、BPI2012_A）并给失效条件描述 [PDF p.7 右栏；p.11 左栏]。
9. 桥线应补而本文缺的：硬件、方差、逐档赢输表、样本变体数（§5.1、§5.7、§6.2）。

---

`[PARTIAL · 时间盒到 · §5.2/5.3/5.4/5.5 表格逐格数值待补（图像嵌入表，需逐页 Read 判读回填）；其余章节完成]`
