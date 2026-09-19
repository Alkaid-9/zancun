Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# sigRank 知识图谱提取与批判性分析（B2 独立视角）

**论文**：Xuan Su, Cong Liu, Shuaipeng Zhang, Qingtian Zeng, Qi Mo, Long Cheng. "Toward Efficient Support for Business Process Event Log Sampling". IEEE Transactions on Services Computing, vol. 19, no. 2, March/April 2026, pp. 1606–1618. DOI 10.1109/TSC.2026.3665370。CC BY 4.0 [PDF p.1]。
**通讯作者**："Corresponding authors: Cong Liu; Qi Mo." [PDF p.1]。收稿 2025-05-26，修回 2026-02-01，录用 2026-02-09，出版 2026-02-16 [PDF p.1]。
**页码约定**：[PDF p.X] 指 PDF 物理页 X（1..13），对应印刷页 1605+X（p.1=1606 … p.13=1618）。
**证据来源**：`Read` PDF 全 13 页（`pages` 参数分三批）；三张表数值引自 `10_SIGRANK_p2_tables.md`（标 `[tables:行号]`），并自抽格对 PDF 图像复核（见 §3 末尾）。**未读** `10_SIGRANK_p1.md` / `10_SIGRANK_p2.md`。
**非本文范围**：不含 EdgeIM 内容；[13] 处仅原样引述。

---

# 第一部分：知识图谱提取

## 1. 核心概念及其关系

| # | 概念 | 原文定义/原句 | 关系 | 出处 |
|---|------|--------------|------|------|
| C1 | 事件日志 Event log | Def. 1："Let U_A be the universe of activities. A trace σ ∈ U_A* is defined as a sequence of activities/events. L ∈ B(U_A*) is an event log such that B(U_A*) is the set of all multisets of sequences on U_A." 且 "this paper is limited to event logs of activity sequences and other attributes are not considered." | 迹 part-of 日志；日志 = 迹的多重集；input-of C10 | [PDF p.2] |
| C2 | 迹 / 变体 Trace / Variant | "an event log L_C with 75 traces (23 distinct traces, also known as variants) and 8 activities" | 变体 = 去重后的迹（is-a 等价类）；C1 的元素 | [PDF p.2] |
| C3 | 活动集 actS(L) | Def. 5："its activity set is: actS(L) = ⋃_{σ∈L}{σ(i)\|1 ≤ i ≤ \|σ\|}" | derived-from C1；input-of C5 | [PDF p.4] |
| C4 | 直接跟随关系集 dfgS(L) | Def. 6："its directly-follows relation set is: dfgS(L) = ⋃_{σ∈L}{(σ(i), σ(i+1))\|1 ≤ i ≤ \|σ\|−1}" | derived-from C1；input-of C6 | [PDF p.4] |
| C5 | 活动显著性 sig(a,L) | 式(2)：sig(a,L) = \|⋃_{σ∈L}{σ\|∃1≤i≤\|σ\| ∧ σ(i)=a}\| / \|L\|，"denotes the number of traces that contain activity a in L" | measured-on C3；分母为迹数（多重集大小）；input-of C7 | [PDF p.4] |
| C6 | 直接跟随关系显著性 sig(⟨a,b⟩,L) | 式(3)：含 ⟨a,b⟩ 的迹数 / \|L\| | measured-on C4；input-of C8 | [PDF p.4] |
| C7 | 迹平均活动显著性 sigAvgAct(σ,L) | 式(4)：Σ_{i=1}^{\|σ\|} sig(σ(i),L) / \|σ\|（按迹内位置求算术平均，重复活动重复计入） | aggregates C5；input-of C9 | [PDF p.4] |
| C8 | 迹平均 DFR 显著性 sigAvgDfr(σ,L) | 式(5)：Σ_{i=1}^{\|σ\|−1} sig(⟨σ(i),σ(i+1)⟩,L) / (\|σ\|−1) | aggregates C6；input-of C9 | [PDF p.4] |
| C9 | 迹总显著性 sigTotal(σ,L) | 式(6)：w_act·sigAvgAct + w_dfr·sigAvgDfr，"w_act, w_dfr ≥ 0 and w_act + w_dfr = 1. By default, w_act = w_dfr = 0.5"；"Equal weighting avoids bias toward either frequent activities or dense directly-follows relations" | 排序键 for C11；权重固定 0.5/0.5 | [PDF p.4] |
| C10 | 日志采样技术 Log sampling technique | Def. 4："a function Π from an original log L_0 ∈ B(U_A*) to a sample log L_s ∈ B(U_A*), i.e., Π(L_0) = L_s, where ∀σ ∈ L_s : σ ∈ L_0, i.e., L_s is a subset of L_0." | sigRank is-a C10；LogRank/LogRank+/[25] 五法 is-a C10 | [PDF p.3] |
| C11 | sigRank 四步流程 | Step 1 活动集与 DFR 集；Step 2 按(2)(3)算显著性；Step 3 按(4)–(6)算迹显著性；Step 4 "all traces are ranked according to their significance values, and the top-N ranked traces are selected to build the sample log based on the input sample ratio" | composed-of C3–C9；output = 样本日志 | [PDF p.5] |
| C12 | 采样比例 Sampling ratio | 输入之一（Fig. 2 "Sampling Ratio"）；实验用 "ratios 30% → 5% (step -5%)" | parameter-of C11；决定 N | [PDF p.4, p.7] |
| C13 | 复杂度声明 | "overall time complexity of O(n log n), where n is the number of traces … computing trace significance (O(n·m)) and sorting traces by significance (O(n log n)). Since m ≪ n in real-world event logs, the sorting step dominates" | property-of C11；m 未定义 | [PDF p.5] |
| C14 | 效果评估两维 | "Efficiency Evaluation: The sum of sampling time and model discovery time using the sample log … compared to the model discovery time using the original log"；"Quality Evaluation … Qua(L_S, L_0) = Q(L_0, M_S)/Q(L_0, M_0)"（式(1)，p.5 式(8) 以 F-measure 重述） | measures C10 的输出 | [PDF p.3, p.5] |
| C15 | fitness / precision / F-measure | fitness 采 [36]，precision 采 [37]，式(7) F = 2·fit·prec/(fit+prec)；"we select Inductive Miner [4] as the underlying process discovery technique, as it guarantees perfect fitness" | instantiates C14 的 Q；IM 为固定发现器 | [PDF p.5] |
| C16 | 基线家族 | LogRank [24]（"graph-based ranking model that applied PageRank"）；LogRank+ [14]（"similarity against all remaining traces"）；Frequency/Similarity/Hybrid/Longer/Shorter-based [25]；IMi [20]（"filter-based model discovery technique"，非采样） | compared-with C11；[25] 五法同源 | [PDF p.6–7] |
| C17 | ProM 插件 | "implemented as an independent tool called sigRank-based Event Log Sampling in the open-source framework ProM 6"，脚注 1 = github.com/promworkbench/SoftwareProcessMining；输入原始日志+比例，输出 XES 样本日志 | implements C11 | [PDF p.6] |
| C18 | 数据集 | "12 public event logs, including 6 synthetic logs and 6 real-life ones"（Table I） | input-of 实验 | [PDF p.6] |

**关系邻接表**（原文明示）：
- C1 → 派生 → C3, C4 [PDF p.4]；C3/C4 → 逐元素打分 → C5/C6 [PDF p.4]；C5/C6 → 沿迹平均 → C7/C8 [PDF p.4]；C7+C8 → 加权 → C9 [PDF p.4]；C9 + C12 → 排序取 top-N → 样本日志 [PDF p.5]。
- 样本日志 → IM 发现 M_S → 对原日志算 C15 → 与 M_0 比（C14）[PDF p.3, p.5]。
- C16 各法与 C11 → 同一评估协议（6 比例 × 12 日志 × 5 次）[PDF p.7]。
- LogRank/LogRank+ ← 作者前作 [8][24][14]；[25] 五法 ← Sani 等；IMi ← Leemans [20] [PDF p.6–7, p.12]。

## 2. 理论框架图（文字描述，含推断）

```
输入：原始日志 L_0（活动序列多重集）+ 采样比例 r            [原文 Fig.2, PDF p.4]
├─ 计算层
│  ├─ Step1 actS(L_0), dfgS(L_0)                          [原文 p.5]
│  ├─ Step2 sig(a), sig(⟨a,b⟩)：含该元素的迹数 / |L_0|     [原文 式(2)(3) p.4]
│  │     └─ [推断] 一趟遍历全部事件即可得，代价 O(#events)
│  └─ Step3 每条迹：sigAvgAct, sigAvgDfr → sigTotal=0.5/0.5 加权 [原文 式(4)-(6) p.4]
│        └─ [推断] 同一变体的所有迹得分相同 → 排序中大量并列
├─ 排序层：按 sigTotal 降序                                [原文 p.5]
├─ 选择层：取 top-N，N 由 r 决定                             [原文 p.5]
│     ├─ [原文 Fig.3] N = 15%×20 = 3 条迹，含同一变体 2 份 → 单位=迹(带重数)
│     └─ [原文 p.5 例] L_C(75 迹) 15% → 12 条互异变体各 1 份 → 单位疑为变体
│        ⚠️ 两个示例口径不一致，见第二部分 §1(c)
└─ 评估层                                                   [原文 Fig.2, p.5]
   ├─ 质量：IM(L_s) → M_S；fitness/precision/F-measure 对 L_0   [原文 式(7)]
   │     └─ [原文 式(1)(8)] Quality = F(L_0,M_S)/F(L_0,M_0)；[推断] 结果表未用此比值
   └─ 效率：采样时间 + 发现时间（Fig.6 堆叠、Table III 六档均值）  [原文 p.7, p.11]
```

明说的边：输入→四步→top-N→样本→IM→三指标；效率=两段时间之和。推断的边：Step2 的一趟扫描成本、并列得分、评估层实际未使用式(8)。

## 3. 关键数据表（逐数值解释）

**Table I（p.6，12 日志基本统计）** `[tables:18-31]`。在说什么：6 合成 + 6 "真实"日志的 #Event/#Trace/#Variant/#Activity。最关键的格：(i) 最大日志 BPI2012_A 146044 事件 / 13087 迹 / **32 变体 / 10 活动** `[tables:31]`——事件最多但结构最简单；(ii) SimulateLog2000 2000 迹 / 2000 变体、NASA 2566 迹 / 2513 变体 `[tables:25,27]`——"迹即变体"型日志，是频率类打分最不利的场景；(iii) ETMC4200 4203 迹 / 16 变体、order 1000 迹 / 9 变体 `[tables:28-29]`——变体极少，任何"取主流"的采样都容易得满分。为什么关键：论文动机是"large and complex event logs, e.g., those with thousands of variants" [PDF p.1]，但表内只有 5 个日志变体数 ≥ 900，且都不到 3000；最大事件数 14.6 万，规模上不构成"大规模"论据。另：2000AllNoise 被归入 Real-life Logs `[tables:26]`，名称暗示合成噪声日志 `[⚠️存疑]`。

**Table II（p.8，F-measure，12 日志 × 6 比例 × 9 法）** `[tables:44-142]`。在说什么：每个日志一个子块，逐比例列示样本日志上 IM 所得模型对原日志的 F-measure，加粗为该列最高。最关键的格：(i) sigRank 六档全为 **1** 的 ETMC4200 `[tables:54,71,88,105,122,139]` 与全为 0.9018 的 trainingLog3——得分随比例不变，说明 5% 已抓到全部"主流"结构；(ii) trainingLog5/trainingLog7 sigRank 多数档 ≈ 0.19–0.29 而 shorter 0.53–0.72 `[tables:49-50,66-67]`——sigRank 在高变体日志上明显落后；(iii) BPI2012_A sigRank 恒 0.5243，5%/10% 被 Fre_Based 0.5251/0.569 压过 `[tables:57,74]`；(iv) IMi 在 SimulateLog2000/2000AllNoise/trainingLog5/7 上大幅领先所有采样法（0.93/0.85 vs ≤ 0.56/0.85）`[tables:51-52]`。为什么关键：正文 "sigRank attains the highest F-measure (10/12)" [PDF p.7] 依赖计数规则；按本文自算（六档均值、仅 8 个采样法互比）sigRank 最优 6 个（tL2、tL3、ETMC4200、order、Final、BPI2012_A）+ 1 个并列（SimulateLog2000 与 Sim/hyb 同 0.5613），得不出 10 `[推断]`；把 IMi 计入则只剩 5。

**Table III（p.11，六档均值总时间 ms，8 法无 IMi）** `[tables:152-165]`。在说什么：采样+发现时间对 30%→5% 六档取均值，加粗为行最低。最关键的格：(i) LogRank 列 2622291.82 ms（2000AllNoise）、746341.5（NASA）、524498.5（SimulateLog2000）`[tables:159-161]`——比其他法高 1–2 个数量级，决定了"LogRank 最慢"的结论；(ii) sigRank 行最低 9/12 `[tables:154-159,162-164]`，例外 2000AllNoise（Sim 15846 vs sig 25361）、NASA（shorter 8427 vs sig 12120）、BPI2012_A（shorter 6559 vs sig 9899）`[tables:160-161,165]`——例外恰是 3 个最大/最多变体的日志；(iii) LogRank+ 在 BPI2012_A 为 88527 ms，是其自身其他日志的 2–30 倍 `[tables:165]`。为什么关键：正文 "the sampling time of LogRank is 141549 ms, which is approximately 100 times longer than other techniques" [PDF p.11]——按 Table III 总时间，LogRank 147261 对其余 6559–10260 仅约 14–22 倍，"100 倍"若成立只能是对采样时间单独比 `[需验证]`。

**自抽复核（PDF 图像 vs tables 文件）**：Table II trainingLog1-5%-sigRank = 0.9253 加粗（PDF p.8 ✓ = `[tables:46]`）；Table III order-sigRank = 359.33 加粗（PDF p.11 ✓ = `[tables:163]`）；Table I BPI2012_A = 146044/13087/32/10（PDF p.6 ✓ = `[tables:31]`）；Table III 2000AllNoise-LogRank = 2622291.82（PDF p.11 ✓ = `[tables:160]`）。四格均一致。另自查 Fig. 3（PDF p.5）：sig(a)=16/20=0.8、sigAvgAct(σ1)=(0.8+0.9+0.85+0.95+0.5)/5=0.8、sigAvgDfr(σ1)=(0.65+0.75+0.40+0.30)/4=0.525、sigTotal=0.6625，与图中数字一致，公式与示例自洽。

## 4. 引用网络（TOP 5 + 引用方式分析）

正文出现次数用 pdftxt 定位后逐处对 PDF 页面核对（不含参考文献表本身）：

| 排名 | 文献 | 正文次数 | 用法 | 出处 |
|---|---|---|---|---|
| 1 | [25] Sani et al. 2020, Comput. Sci. Inf. Syst. | 6 | 相关工作里的"biased trace selection strategies"来源 + **五个基线**（Frequency/Similarity/Hybrid/Longer/Shorter）的唯一出处 | [PDF p.2, p.7] |
| 2 | [4] Leemans et al. 2013 IM | 4 | 背景（p.1、p.2 "state-of-the-art"）、Fig. 1 发现器、评估固定发现器（"guarantees perfect fitness"） | [PDF p.1, p.2, p.3, p.5] |
| 3 | [8] Liu et al. 2018 CCPE LogRank（+ [24] KSEM 2018 同名，2 次） | 3+2 | 自家前作：p.1 动机句、p.2 相关工作首例、p.3 运行示例 L_C^s（15%）取自 [8]；基线列表引 [24] | [PDF p.1, p.2, p.3, p.6] |
| 4 | [14] Liu et al. 2020 WISE LogRank+ | 3 | 自家前作：p.1 与 [12][13] 并列"most promising"、p.2 作为 LogRank 提速版、p.6 基线 | [PDF p.1, p.2, p.6] |
| 5 | [20] Leemans et al. 2013 IMi | 2 | p.2 背景；p.7 作为"filter-based"对照（noise_threshold 0.70→0.95） | [PDF p.2, p.7] |

次一档：[11] Evermann 2016（2 次，分布式 MapReduce 方案作为反衬）[PDF p.1, p.2]；[2] Alpha（2 次，背景）；[36][37][38]（各 1 次，fitness/precision/F-measure 定义）[PDF p.5]。

引用方式分析：(a) 基线全部来自两个来源——自家 LogRank 族与 Sani [25]，没有引入 2022–2025 的采样/摘要方法作基线（[26] PROMISE+、[27] K-medoids 仅在相关工作提及并以"require model training or iterative optimization" [PDF p.2] 排除）；(b) 自家前作 [12]（Su et al. 2024 CCPE "Sampling … with guarantees"）只在 p.1 并列引用一次，既未说明与 sigRank 的关系也未作基线 `[PDF p.1]`；(c) [13] 原文为 "X. Su, C. Liu, F. Lu, L. Cheng, Q. Zeng, and S. Zhang, 'Edgeim: An efficient edge-based process model discovery technique,' in Proc. 2025 IEEE Int. Conf. Web Serv., 2025, pp. 404–410." [PDF p.12]，仅在 p.1 "event log sampling techniques are proved to be one of the most promising techniques to improve process discovery efficiency [12], [13], [14]" 出现一次 `[sigRank 原文转述，非 EdgeIM 原文]`；内容见 EdgeIM 原文 §IV.B，用户自读；(d) 47 条参考文献中含作者组（Liu/Zeng/Cheng/Su）署名的约 22–24 条 `[需验证·按作者名粗数]` [PDF p.12–13]，结论段的六个未来方向 [39]–[46] 亦以自引为主。

---

# 第二部分：批判性分析

## 1. 方法论审视

**(a) 显著性定义的内生偏置。** 式(2)(3) 把活动/DFR 的显著性定义为"含该元素的迹数占比" [PDF p.4]，式(4)(5) 再沿迹取算术平均。三点后果：(1) 分子按迹计数，一条迹内重复出现的活动只算一次，但式(4) 的平均却按位置重复计入——循环体由高频活动组成的长迹会被平均值"抬"上去，而含一个低频活动的短迹会被单个低分拖下去，评分对**迹内组成的均匀性**敏感而不是对**行为覆盖**敏感；(2) 平均而非求和意味着迹长被归一化，长短迹在同一尺度比较，但式(5) 分母 |σ|−1 在 |σ|=1 时为 0，单事件迹未定义 `[推断]`；(3) 作者在 Threats to Validity 自认 "it can omit infrequent yet important behavior and overlook critical aspects of the global process" [PDF p.11]，但摘要仍写 "guaranteeing superior sample log quality" [PDF p.1]。另：式(2)(3) 用集合并记号 ⋃_{σ∈L}{σ|…} 表述分子，按字面是**去重后的变体数**，而 Fig. 3 的数值（sig(a)=0.8=16/20）用的是**带重数的迹数** [PDF p.5]，记号与示例语义不一致 `[推断]`。

**(b) 权重 0.5/0.5 无调参、无敏感性分析。** 原文只给一句理由 "Equal weighting avoids bias toward either frequent activities or dense directly-follows relations, yielding a more stable and representative importance score" [PDF p.4]；全文无任何 w_act ∈ {0,0.25,…,1} 的扫描，也未报告只用 sigAvgAct 或只用 sigAvgDfr 的消融。Fig. 3 里 sigAvgAct 范围 0.73–0.81、sigAvgDfr 范围 0.075–0.5875 [PDF p.5]，两个分量的方差相差数倍，等权实际上让 DFR 项主导排序 `[推断]`——"avoids bias"的说法没有证据。

**(c) top-N 的单位在两个示例中不一致。** Fig. 3：20 条迹、15% → 样本 3 条，含 ⟨a,b,c,e,f⟩ **2 份**（σ3 得分 0.69875 最高、重数 2）+ ⟨a,b,c,e,g⟩ 1 份（σ1 次高，原重数 6）[PDF p.5]——单位是"迹（带重数）"，且同一变体只取到需要的份数。p.5 示例：L_C 75 条迹、15% → L_C^{s'} "12 traces, 132 events"，12 条**互异**变体各上标 1 [PDF p.5]——若按 Fig. 3 的口径，⟨a,c,d,e,h⟩^16 这类高频短迹应占满 12 个名额 `[推断]`。两者不能同时成立；Step 4 只说 "top-N ranked traces" [PDF p.5]，未说明并列处理与去重规则。这直接影响 Table II 的可解释性（同一变体所有迹同分，N 落在并列段内时取谁）。

**(d) 复杂度声明口径。** "O(n·m)" 中 m 未定义；"Since m ≪ n … the sorting step dominates" [PDF p.5] 把 m 与 n 比，而正确的比较对象是 m 与 log n。以 Table I 估算：BPI2012_A 平均迹长 ≈ 146044/13087 ≈ 11.2，log₂n ≈ 13.7；trainingLog5 平均迹长 ≈ 22.3，log₂n ≈ 10 `[tables:23,31]`——m 与 log n 同量级或更大，"排序主导"不成立，总复杂度应写 O(n·m + n log n) `[推断]`。这不改变"比 LogRank 的成对相似度 O(n²) 快"的结论，但声明本身不严谨。

**(e) 评估协议。** 每比例跑 5 次取均值 [PDF p.7]，无方差/置信区间；无硬件、JVM、ProM 版本说明；IMi 阈值 θ = 1−r 是作者自设的启发式（"were not tuned for each event log" [PDF p.7]），使 IMi 对照的强弱取决于这一映射；Table III 对六档取均值把比例维度压掉，LogRank 的极端值（2000AllNoise 2.6×10⁶ ms）会主导任何跨法平均。

## 2. 逻辑审视

**(a) 计数型断言与表格对不上。** (1) "sigRank attains the highest F-measure (10/12)" [PDF p.7]：按加粗格数只有 7 个日志出现过 sigRank 加粗，按六档均值 6+1 并列（§3）；(2) "LogRank and LogRank+ … Each method performs best on six event logs" [PDF p.7]：Table II 中 LogRank 加粗只在 NASA 三档、LogRank+ 只在 trainingLog2-20% `[tables:53,70,87,98]`，无法得到"各六个"；(3) "Similarity-based … higher than … Frequency-based … (9/12). An exception is the Final log" [PDF p.7]：六档均值下 trainingLog7、order、BPI2012_A 三处 Fre 更高，Final 持平，得 8/12 而非"9/12 且唯一例外 Final" `[推断]`；(4) "sigRank outperforms IMi in most of the evaluated logs (8/12) or exhibits alternating performance" [PDF p.7]——"or alternating" 让 8/12 不可证伪。全文没有任何一处给出计数规则（逐档？均值？多数档？）。

**(b) 时间数字的两套口径。** p.11 正文列举例外日志的时间 "10296 ms vs 9127 ms vs 12006 ms, 6093 ms vs 5690 ms vs 6544 ms, 4933 ms vs 4448 ms vs 6217 ms vs 3040 ms vs 4929 ms vs 6984 ms" [PDF p.11]，与 Table III 对应格（如 NASA Fre_Based 9125、sigRank 12119.83；BPI2012_A shorter 6559.16、sigRank 9899.32 `[tables:161,165]`）既不相等也不成比例，正文未说明这些数字来自哪一档/哪一列 `[⚠️矛盾]`。"approximately 100 times longer" [PDF p.11] 与 Table III 的 14–22 倍不符（§3）。Fig. 6(i) ETMC4200 上段纵轴读作 180000–190000 而 Table III LogRank = 84306.16 `[tables:162]`；Fig. 6(f) 横轴缺 5% 组 [PDF p.9]——图表之间也未对齐 `[⚠️矛盾·图读数]`。

**(c) 定义了却未使用的质量比值。** 式(1) Qua = Q(L_0,M_S)/Q(L_0,M_0) [PDF p.3] 与式(8) Quality = F(L_0,M_S)/F(L_0,M_0) [PDF p.5] 是同一比值的两次定义；Table II 标题与正文均报 "F-measure values" [PDF p.7–8]，即只报分子，从未给出 F(L_0,M_0) 基准，读者无法判断 sigRank 的 0.5243（BPI2012_A）离"原日志模型"差多远。ETMC4200 的 "1" 只能理解为 F-measure = 1 而非比值 = 1 `[推断]`。

**(d) "guarantees perfect fitness" 的错位。** 选 IM 的理由是 "it makes no sense if the model discovered in the sample log cannot guarantee 100% (replay) fitness … we select Inductive Miner [4] … as it guarantees perfect fitness" [PDF p.5]；但 IM 保证的是对**样本**的 fitness，论文测的是对**原日志**的 fitness（示例中 LogRank 样本模型 fitness(L_C,M_S)=0.89 [PDF p.6]），理由与度量对象不同。同段落两处笔误："precision(L_C,M_S)=0.38 and fitness(L_C,M'_S)=0.92"（应为 precision）、"F-measure(L_C,M_S)=0.53 and F-measure(L_C,M_S)=0.96"（第二个应为 M'_S）[PDF p.6]。

**(e) 措辞升级链。** 引言 "sigRank can significantly accelerate the sampling efficiency while guaranteeing superior sample log quality" [PDF p.1] → 结果段 "achieves the best sample log quality and sampling efficiency" [PDF p.11] → 威胁段承认三条限制 [PDF p.11]。证据支持的是"总时间 9/12 最低、质量在低变体日志上最优、在高变体日志上落后于 shorter/Sim"，"guaranteeing"无对应证据。对失利日志的解释（"many unique or low-frequency variants and sparse, weakly connected directly-follows relations" [PDF p.7]）是事后归因，且与 2000AllNoise（2000/2000 变体但 sigRank ≥10% 时表现尚可 `[tables:69-137]`）不完全一致 `[推断]`。

**(f) 细节可靠性。** Def. 5/6 示例日志名为 L_E，随后写 "actS(L_C)" "dfgS(L_C)" [PDF p.4]；Fig. 2 Phase 2 标 "Accuracy Evaluation Metrics" 而正文称 "Effectiveness Evaluation" [PDF p.3–4]；Fig. 6 纵轴标 "Sampling Time" 但柱为 Mine+Sample 堆叠 [PDF p.9]；Table II NASA 与 2000AllNoise 的 sigRank-5% 同为 0.3146 `[tables:52-53]` `[⚠️存疑·疑复制]`；trainingLog2 Fre_Based-5% 为五位小数 0.24438 `[tables:47]`。

## 3. 贡献审视

**相对自家 LogRank/LogRank+ 家族 [8][24][14]**：LogRank 是"成对迹相似度 + PageRank"（p.11 自述 "computes the similarity between each pair of trace and then implements a PageRank-based ranking"），LogRank+ 是"一条迹对其余全部迹的相似度" [PDF p.6–7]，二者都是 O(n²) 量级的相似度计算；sigRank 把打分改成两趟频率统计 + 排序，去掉了成对计算。这是真实的工程增量，Table III 的 9/12 最低总时间与 LogRank 列的 1–2 个数量级差距是最硬的证据。但 (1) 论文没有说明 sigRank 与 [12]（Su et al. 2024 CCPE，同一作者组、同一主题）的关系，也没拿它做基线 [PDF p.1]，读者无法判断 2024→2026 的增量是什么；(2) LogRank 的慢主要来自成对相似度，任何线性打分器（包括 [25] 的 Frequency-based）都能获得类似加速——Table III 中 Fre/Sim/hybrid/Longer/shorter 与 sigRank 同一量级 `[tables:154-165]`，"比 LogRank 快"不是 sigRank 独有的贡献。

**相对 [25] Frequency/Similarity/Hybrid**：按论文自己的描述，Similarity-based "counting the number of mainstream directly-follows relations"（DFR 权重超阈值者），Hybrid "normalizes them to values between 0 and 1 and uses a weighting average mechanism" [PDF p.7]。sigRank 的 sigAvgDfr 可视为 Similarity-based 的无阈值、按迹长平均版本，sigTotal 的等权平均与 Hybrid 的加权平均同构；差别在把"变体频率"换成"活动出现率的迹内平均" `[推断]`。质量上 sigRank 对 Sim 六档均值 8 胜 3 负 1 平（§3），时间上同量级。增量存在但属于打分函数的细节调整，不是新范式。

**相对 IMi [20]**：IMi 不是采样法，Table III 也未计入其时间。Table II 中 IMi 在 4 个高变体日志上大幅领先所有采样法 `[tables:49-52]`，论文用"potential information loss, sensitivity to the noise threshold, and the absence of a reusable sampled log" [PDF p.11] 解释——这三点是定性主张，未量化。

**novelty 定位** `[推断]`：合理表述是"一个训练无关、线性时间、基于活动/DFR 出现率的迹打分器 + ProM 插件 + 12 日志对比"。工具化（XES 输入输出、ProM 6 集成 [PDF p.6]）与系统性实验是对该小方向的实际贡献；方法层面的新颖性受 [25] Hybrid 与自家 [12] 的挤压，论文未做区隔。

## 4. 可复现性

| 项 | 有无 | 出处 |
|---|---|---|
| 代码 | 部分：ProM 6 插件 "sigRank-based Event Log Sampling"，脚注 1 指向 github.com/promworkbench/SoftwareProcessMining（包级仓库，未给插件路径/版本/commit） | [PDF p.6] |
| 数据 | 声称 "12 public event logs"，但无 URL/DOI；trainingLog1–7、Final、order、SimulateLog2000、2000AllNoise 等名称在公开语料中不唯一 | [PDF p.6] |
| 参数 | sigRank：w_act=w_dfr=0.5、比例 5–30% 步 5；IMi：θ=1−r；**基线参数缺失**（Similarity-based 的 DFR 阈值、Hybrid 的权重、LogRank 的阻尼/迭代数均未给） | [PDF p.4, p.7] |
| 硬件/软件 | **无**：无 CPU/内存/JVM/ProM 版本/操作系统 | 全文未见 |
| 随机性 | sigRank 确定性；5 次重复只用于计时 [PDF p.7]；排序并列（同变体同分）的破平规则未说明 | [PDF p.5, p.7] |
| 指标实现 | fitness [36]、precision [37] 为对齐式定义，所用 ProM 插件与配置未说明；F(L_0,M_0) 基准未报 | [PDF p.5] |
| 原始数据 | Table II 逐档 F-measure 已给；逐档时间只在 Fig. 6 柱图无数字标注 | [PDF p.8–11] |

综合：**算法可重实现（公式与 Fig. 3 示例自洽），数字不可复现**（数据来源、基线参数、硬件、破平规则四缺）。

## 5. 总评（审稿人视角）

**判定：大修（major revision）** `[推断]`。作为 TSC 正刊论文（已录用出版），其可取之处是明确的：一个简单、无训练、线性的迹打分器；ProM 插件落地；12 日志 × 6 比例 × 8 法的对比矩阵并公开逐档 F-measure；Threats to Validity 诚实列出频率假设的盲区 [PDF p.11]。但按论文自己的主张（"guaranteeing superior sample log quality"、"10/12"、"100 times"）衡量，正文断言与表格之间存在多处不一致，方法定义有两处口径歧义，且与最相关的自家前作 [12] 和 Sani [25] Hybrid 的区隔没有做。

**三条最重要的修改意见** `[推断]`：

1. **统一并公开所有计数与时间口径。** 给出 "10/12"、"9/12"、"8/12"、"six event logs" 的计数规则并按 Table II 重新核算；解释 p.11 正文时间数与 Table III 的对应关系及 "100 times" 的比较基准；修正 Fig. 6(i) 纵轴与 Table III、Fig. 6(f) 缺档；报告 F(L_0,M_0) 基准使式(8) 真正被使用 [PDF p.7, p.8, p.9–11]。
2. **钉死 top-N 的语义并补消融。** 明确选择单位（迹带重数 / 变体）、并列破平、|σ|=1 的处理，使 Fig. 3 与 p.5 示例一致 [PDF p.5]；补 w_act 扫描与单分量消融，替换 "Equal weighting avoids bias" 的无证断言 [PDF p.4]；把复杂度改为 O(n·m + n log n) 并定义 m [PDF p.5]。
3. **补齐与最近邻工作的区隔和复现材料。** 说明 sigRank 相对 [12]（2024 CCPE）与 [25] Hybrid 的具体差别，最好把 [12] 纳入基线 [PDF p.1, p.7]；给出数据集 DOI、基线参数、硬件与 ProM 版本、插件路径；把摘要/结论的 "guaranteeing" 收缩到"在低变体日志上最优、在高变体日志上不及 shorter/Similarity"的证据范围 [PDF p.1, p.11]。
