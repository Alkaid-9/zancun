Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# 10 · sigRank（TSC 2026）第一性原理全拆（上：§0–§4）—— 桥线 T1 辅助篇

> 主输入：原 PDF `research/papers_lu/sigRank-2026-TSC.pdf`（13 页，`Read` 全文逐页判读）。`_launch/pdftxt/SIGRANK.txt` 仅用于定位行与核对字符串，不作判定依据。
> 页码约定：全文 `[PDF p.N]` 为物理页；印刷页 = 1605 + N（换算表见 §0）。
> 体量说明：13 页期刊文 = 正文约 6 页（p.1–7、p.11 上半）+ 整页表图约 3.5 页（p.8 Table II、p.9–10 Fig. 6、p.11 Table III）+ 参考文献 1.5 页（p.12–13）+ 作者简介（p.13）。方法部分实际只占 p.4–5 约 1.5 页，拆解密度按此控制。
> 边界声明：本篇不与 EdgeIM 做比较、不转述 EdgeIM 算法；sigRank 原文对 EdgeIM 只有一处引用（见 §3.1 I-D），原样引述并标注。需要 EdgeIM 内容处一律写"见 EdgeIM 原文 §IV.B，用户自读"。

---

## 0. 身份卡

- **题录**：Xuan Su (Graduate Student Member, IEEE), Cong Liu (Member, IEEE), Shuaipeng Zhang, Qingtian Zeng (Member, IEEE), Qi Mo, Long Cheng (Senior Member, IEEE). "Toward Efficient Support for Business Process Event Log Sampling". IEEE Transactions on Services Computing, vol. 19, no. 2, March/April 2026, pp. 1606–1618 [PDF p.1 页眉]。DOI 10.1109/TSC.2026.3665370（原件 p.1 左栏脚注末行印有 "Digital Object Identifier 10.1109/TSC.2026.3665370"）[PDF p.1]。
- **时间线** [PDF p.1 脚注]：Received 26 May 2025；revised 1 February 2026；accepted 9 February 2026；date of publication 16 February 2026；date of current version 10 April 2026。
- **许可**：页脚 "© 2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License" [PDF p.1 页脚]，即开放获取版。
- **通讯作者**：Cong Liu；Qi Mo（脚注 "Corresponding authors: Cong Liu; Qi Mo"）[PDF p.1]。
- **作者单位** [PDF p.1 脚注；p.13 简介]：Xuan Su、Qingtian Zeng — 山东科技大学计算机科学与工程学院（青岛 266590）；Cong Liu — NOVA Information Management School（里斯本）+ 山东理工大学计算机学院（淄博 255000）双署名；Shuaipeng Zhang — 山东大学软件学院（济南）；Qi Mo — 云南大学软件学院（昆明）；Long Cheng — 华北电力大学控制与计算机工程学院（北京）。
- **与 EdgeIM 作者群的关系（仅陈述作者栏事实）**：鲁法明**不在本文作者栏** [PDF p.1]；他作为 EdgeIM（本文引文 [13]）的作者出现在参考文献 [PDF p.12 ref [13]]。两文作者交集 = Su / Liu / Cheng / Zeng。
- **基金** [PDF p.1 脚注]：国家重点研发 2022ZD0119501；NSFC 62472264、52374221、62562063；山东省自然科学杰出青年基金 ZR2025QA13；葡萄牙 FCT UIDB/04152/2025（MagIC/NOVA IMS）与 UID/PRR/04152/2025。
- **PDF 物理页 ↔ 印刷页**：p.1=1606（题名/摘要/引言）；p.2=1607（相关工作 + 背景 III.A 起）；p.3=1608（Fig. 1、L_C、Def 2–4、IV.A 起、式 (1)）；p.4=1609（Fig. 2、IV.B、Def 5–6、式 (2)–(6)）；p.5=1610（Fig. 3、Step 1–4、复杂度、L_C^{s'}、IV.C、式 (7)–(8)）；p.6=1611（Fig. 4–5、Table I、V、VI.A、VI.B 起）；p.7=1612（基线续、VI.C）；p.8=1613（Table II 整页）；p.9=1614、p.10=1615（Fig. 6 两整页）；p.11=1616（Table III、效率讨论、VI.D Threats、VII 起）；p.12=1617（结论尾 + 参考文献 [1]–[39]）；p.13=1618（参考文献 [40]–[47] + 作者简介）。
- **文件 sha256**：`e20cac7b2b1c562b12342d07f33b5621e50dcdb15f2dc7ea42fb6da632c09800`。
- **来源出处**：`[需核实]` —— 该 PDF 2026-09-03 落盘、未登记 MANIFEST；从页脚看是 CC BY 4.0 开放获取版，具体下载渠道待用户核实。
- **工具产出**：ProM 6 插件 "sigRank-based Event Log Sampling"，代码脚注 `https://github.com/promworkbench/SoftwareProcessMining` [PDF p.6 脚注 1]。
- **venue 定位**：IEEE TSC 为服务计算领域期刊；CCF 目录等级原文不含，`[需验证]`。相对 ICWS 会议短文，本篇是期刊完整版体裁（13 页），但方法本体只有 1.5 页，其余为评估。
- **家族位置**：桥线 T1 辅助篇。本篇属"事件日志采样"子线，与一作 Su 的 CCPE 2024 "Sampling business process event logs with guarantees"（本文引 [12]）同源 [PDF p.12 ref [12]]。

## 1. Task：解决什么问题？形式化

**非形式陈述** [PDF p.1 摘要 + 引言]：信息系统积累了大量事件日志；现有发现算法（Alpha/Heuristic/Inductive/Hierarchical/Split/CrossOrg Miner）在大规模日志上"meet severe performance problem"（引 [8]）；分布式重编程成本高；事件日志采样被视为最有前景的加速手段之一（引 [12]、[13]、[14]）；但"achieving high performance in sampling while maintaining superior sample log quality remains a challenge"，尤其是"thousands of variants"的大而复杂日志。目标：提出一个采样技术 sigRank，同时改善采样效率与样本质量。

**形式化（按原文 Def 1–6 + 式 (1)、(7)、(8) 恢复）**：

基础对象：
- Def 1（事件日志）[PDF p.2]：U_A 为活动全集；迹 σ ∈ U_A* 是活动/事件序列；日志 L ∈ B(U_A*)，B(U_A*) 是 U_A 上序列的所有多重集之集。**范围限制**：本文只处理活动序列日志，resource、timestamp、cost 等属性一律不考虑 [PDF p.2 III.A 末段]。
- Def 2（过程发现）[PDF p.3]：U_M 为过程模型全集；发现技术 Θ: L ∈ B(U_A*) → M ∈ U_M，Θ(L) = M。
- Def 3（Petri 网，引 [35]）[PDF p.3]：PN = (P, T, F, l)，(1) P 库所集、T 变迁集，P ∩ T = ∅ 且 P ∪ T ≠ ∅；(2) F ⊆ (P×T) ∪ (T×P)；(3) l: T → 𝒜 标注函数，τ ∈ 𝒜 为不可见标签。前集 •x = {y | (y,x) ∈ F}，后集 x• = {y | (x,y) ∈ F}；标识 m ∈ B(P)；带标识网 (PN, m0)。
- Def 4（日志采样技术）[PDF p.3]：U_L 为日志全集；采样技术 Π: L_0 ∈ B(U_A*) → L_s ∈ B(U_A*)，Π(L_0) = L_s，且 ∀σ ∈ L_s: σ ∈ L_0，"i.e., L_s is a subset of L_0"。注意原文只写了迹成员关系，未写多重集包含（L_s ≤ L_0 的重数约束）[推断：按字面，L_s 中某变体重数超过 L_0 并不违反 Def 4]。
- Def 5（活动集）[PDF p.4]：actS(L) = ∪_{σ∈L} {σ(i) | 1 ≤ i ≤ |σ|}，σ(i) 为第 i 个元素。
- Def 6（直接跟随关系集）[PDF p.4]：dfgS(L) = ∪_{σ∈L} {(σ(i), σ(i+1)) | 1 ≤ i ≤ |σ|−1}。

评估侧对象：
- 质量比 式 (1) [PDF p.3]：Qua(L_S, L_0) = Q(L_0, M_S) / Q(L_0, M_0)，M_S = Θ(L_S)、M_0 = Θ(L_0)，Q 是"模型对原日志"的质量度量。实例化为 式 (8) [PDF p.5]：Quality(L_S, L_0) = F-measure(L_0, M_S) / F-measure(L_0, M_0)，F-measure 由 式 (7) 定义。
- 效率判据 [PDF p.3 IV.A "Efficiency Evaluation"]：t_sample(L_0) + t_disc(L_S) < t_disc(L_0) 则"sampling is effective"。
- 发现算法固定为 IM（引 [4]），理由是它保证 100% replay fitness，否则"makes no sense" [PDF p.5 IV.C 首段]。

**输入/输出/参数**：
- 输入：原日志 L_0；用户给定采样比例 r（原文 "user-defined ratio" / "sampling ratio"）[PDF p.3 IV.A Phase 1；p.5 Step 4]。
- 输出：样本日志 L_S（XES 格式，工具层）[PDF p.6 V]。
- 内部参数：w_act、w_dfr（默认各 0.5）[PDF p.4 式 (6) 下]；top-N 的 N 由 r 派生 [PDF p.5 Step 4]。

**问题陈述（本人重构，[推断]，原文没有以优化问题形式写出）**：给定 L_0 与 r，求 L_S ⊆ L_0、|L_S| ≈ r·|L_0|，使 Quality(L_S, L_0) 尽量接近 1，且 t_sample 远小于 t_disc(L_0)。sigRank 不显式求解此目标，而是用一个训练无关的打分启发式替代（原文自述 "lightweight and training-free heuristic techniques that can be applied directly to event logs" [PDF p.2 II.C 末段]）。

## 2. Challenge：传统方法的挑战

原文声称的挑战，按出现位置恢复：

1. **集中式发现在大规模日志上性能差** [PDF p.1 引言首段引 [8]；p.2 II.B "typically running on a single machine, i.e., CPU, GPU, memory... limited"]。
2. **分布式重编程路线成本高** [PDF p.1 引言第二段；p.2 II.B]：MapReduce/Spark 上重写 Alpha/Heuristic Miner（Evermann [11]）"actually not easy"，需要深入了解发现算法与编程语法；"high-end computer clusters or cloud instances are always required"，终端用户分析成本高。
3. **现有采样技术本身可能很慢** [PDF p.2 II.C 末段]："may be very slow if the original event log is large and complex"；LogRank 的采样时间"may be much longer than the discovery time required from the original log for some special cases"；PROMISE+、K-medoids 等"require model training or iterative optimization"。
4. **采样效率与样本质量兼得难** [PDF p.1 摘要]："achieving high performance in sampling while maintaining superior sample log quality remains a challenge"。
5. **复杂日志（数千变体）** [PDF p.1 引言第三段]："existing techniques may still struggle on large and complex event logs, e.g., those with thousands of variants"。

**哪些是真挑战、哪些是套话（[推断]）**：
- (3) 是本文真正对准的靶子，且有本文自己的实验证据支撑：LogRank 在 BPI2012_A 上采样 141549 ms，"approximately 100 times longer than other techniques"，原因是逐对相似度 + PageRank 迭代 [PDF p.11 左栏]。这是可量化、可复现的挑战。
- (4) 是 (3) 的摘要级复述，不是独立挑战。
- (1)(2) 属于 LogRank 系列论文的惯常开场 [推断]，本文没有给出集中式瓶颈的新证据，也没有与分布式路线做任何实验比较；(2) 中"需要高端集群"是成本论断而非技术难点。
- (5) "thousands of variants" 与实验数据集对应关系弱：Table I 中 12 个日志变体数 9–2513 [PDF p.6 Table I]，没有一个达到"thousands"量级以上（最大 2513），该说法更像动机修辞 [推断]。

**原文未言明但方法内含的挑战（[推断]）**：
- 质量判据式 (1)/(8) 的分母 Q(L_0, M_0) 要求先在原日志上跑一次发现。评估场景可行，部署场景自相矛盾（若能在 L_0 上发现，就不必采样）。原文未讨论。
- 比例 r 的选取无指导；原文 Threats to Validity 第三条承认固定 5–30% "may not generalize well across different event logs" [PDF p.11 右栏]。
- 频次即重要性的假设会丢弃"infrequent yet important behavior"（合规违规、风险敏感例外）——原文 Threats 第一条自认 [PDF p.11 右栏]。

## 3. Insight & Novelty

### 3.1 Inspiration 来源

- **I-A（范式）**：LogRank 家族确立的"内部排序 + 取高分迹"采样范式——原文明说 "event log sampling techniques typically implement an inner trace ranking mechanism to build sample logs by selecting highly-ranked traces" [PDF p.3 IV.C 首段]，Fig. 2 Phase 1 第四框 "Traces ranking and top-N traces selecting" [PDF p.4]。
- **I-B（信号）**：[25] 的 frequency-based（高频优先）与 similarity-based（主流 DFR 覆盖）采样 [PDF p.2 II.C；p.7 基线描述]——sigRank 的两个分量分别对应这两类信号 [推断]。
- **I-C（算法接口）**：IM、Split Miner 等发现算法以直接跟随关系为主要输入——原文 "sigRank is especially compatible with discovery approaches that rely on directly-follows relations (e.g., IM and Split Miner)" [PDF p.7 左栏]。
- **I-D（作者自家线）**：p.1 引言一句 "event log sampling techniques are proved to be one of the most promising techniques to improve process discovery efficiency [12], [13], [14]"，其中 [13] = "Edgeim: An efficient edge-based process model discovery technique"（ICWS 2025）[PDF p.1 右栏；p.12 ref [13]]。`[sigRank 原文转述，非 EdgeIM 原文]`：本文对 [13] 仅此一处并列引用，未转述其任何内容。EdgeIM 内容见 EdgeIM 原文 §IV.B，用户自读。

### 3.2 Insight 逐条

- **Insight 1（可分解性，对应 I-A）**：迹的重要性可以拆成它所含行为单元（活动、直接跟随关系）的重要性再取平均——"the significance of a trace can be quantified by the significance of its activities and directly-follows relations" [PDF p.4 IV.B 首段]。方面：打分对象从"迹间关系"（LogRank 的相似度图）降为"迹内成分"，去掉 O(n²) 的配对。
- **Insight 2（支持度而非频次，对应 I-B）**：活动/DFR 的重要性定义为**包含它的迹数占比**（式 (2)(3) 的 "number of traces that contain..."）[PDF p.4]，不是事件级出现次数。推论 [推断，由式 (2)(3) 的集合写法直接得出]：一条迹内同一活动或同一 DFR 重复多次（循环）不增加其 sig；循环体在打分中只算一次。
- **Insight 3（互补等权，对应 I-B/I-C）**："sigAvgAct captures activity frequency, while sigAvgDfr reflects structural connectivity. Equal weighting avoids bias toward either frequent activities or dense directly-follows relations" [PDF p.4 式 (6) 下]。原文对 0.5/0.5 没有给消融或敏感性分析 [PDF p.7–11 未见]。
- **Insight 4（效率来源）**：单遍扫描算 sig（O(n·m)）+ 一次排序（O(n log n)），无配对相似度、无 PageRank 迭代、无训练 [PDF p.5 复杂度段]；与 LogRank 慢的归因（"computes the similarity between each pair of trace and then implements a PageRank-based ranking"）正相反 [PDF p.11 左栏]。
- **Insight 5（长度归一化的双刃，[推断]）**：式 (4)(5) 除以 |σ| 与 |σ|−1，使长迹不因累加占优；代价是含罕见活动的迹整体被拉低。原文 p.11 "sigRank prioritizes statistically dominant activities and relations... which can under-sample rare but informative variants" 与 trainingLog7 的反例 [PDF p.7 右栏末段、p.11 左栏首段] 是这一双刃的经验证据。

### 3.3 Novelty 清单

- N1（方法）：sigRank 迹显著性打分（式 (2)–(6)）与四步采样流程 [PDF p.4–5]。
- N2（评估框架）：效率 + 质量双维评估（Fig. 2 Phase 2；式 (1)、(7)、(8)）[PDF p.3–5]。
- N3（工具）：ProM 6 插件 [PDF p.6 V、Fig. 5]。
- N4（实验）：12 公开日志 × 7 采样基线 + IMi 过滤式发现对照，6 档比例 [PDF p.6–11]。

### 3.4 Novelty 严格三段式

- **N1 sigRank 打分**
  - 相比什么：LogRank（引 [24]，PageRank 图排序）、LogRank+（引 [14]，对其余全部迹的相似度）、[25] 的 frequency / similarity / hybrid / longer / shorter 五种偏置选择 [PDF p.6 右栏–p.7 左栏基线描述]。
  - 新在哪：把迹的重要性定义为"活动支持度均值"与"DFR 支持度均值"的凸组合（默认等权），只需两次线性扫描 + 排序；不建图、不算配对相似度、不设阈值（similarity-based 需输入阈值 [PDF p.7 左栏]）。
  - 证据在哪：定义与公式 [PDF p.4]；Fig. 3 手算例 [PDF p.5]；复杂度声明 [PDF p.5]；质量证据 Table II "sigRank attains the highest F-measure (10/12)" [PDF p.7 右栏；表在 p.8]；效率证据 Table III "lowest average total time in 9/12 datasets" [PDF p.11]。
- **N2 双维评估框架**
  - 相比什么：[8][24] 系列已有 F-measure 质量评估 [推断，原文未声称此框架为新]。
  - 新在哪：把"采样时间 + 样本发现时间"之和与原日志发现时间比较作为效率判据，并以 F-measure 比值定义样本质量 [PDF p.3 IV.A；p.5 式 (8)]。新意有限，原文措辞也只是 "introduce how to quantitatively compare different sampling techniques" [PDF p.3 IV 引言]。
  - 证据在哪：[PDF p.3 式 (1)、p.5 式 (7)(8)]；Fig. 2 [PDF p.4]。
- **N3 ProM 插件**
  - 相比什么：LogRank 等亦有 ProM 实现 [需验证，原文未比较工具层]。
  - 新在哪：以 XES 日志 + 比例为输入的独立插件 [PDF p.6 V]。
  - 证据在哪：Fig. 5 截图 [PDF p.6]；GitHub 脚注 [PDF p.6]。
- **N4 实验**
  - 相比什么：本文自己的先前工作评估规模 [需验证]。
  - 新在哪：加入 IMi（发现时过滤）作为"非采样"对照，噪声阈值 θ = 1 − r 与比例对齐 [PDF p.7 左栏 VI.C 首段]；每个设置跑 5 次取均值 [PDF p.7 右栏]。
  - 证据在哪：Table I [PDF p.6]、Table II [PDF p.8]、Fig. 6 [PDF p.9–10]、Table III [PDF p.11]。

## 4. 方法全恢复

### 4.0 数据流总图（文字版，对应 Fig. 2 [PDF p.4]）

Input {Sampling Ratio, Original Log} → **Phase 1: SigRank Sampling Technique**（四框顺序：① Activity set and directly-follows relation set → ② The significance of activity and directly-follows relation → ③ The significance of each trace → ④ Traces ranking and top-N traces selecting）→ Output {Sample Log} → **Phase 2: Accuracy Evaluation Metrics**（左半 Process Model Quality：Fitness、Precision → F-measure；右半 Time Performance Analysis：Sampling Time、Discovery Time → Sum Time）。Original Log 另有一条虚线直接进入 Phase 2（作为 F-measure 与发现时间的参照）[PDF p.4 Fig. 2]。

### 4.1 Phase 1：sigRank 采样（原文 Step 1–4 [PDF p.5]；**原文无编号 Algorithm 伪码**，下列行号为本人按 Step 1–4 与式 (2)–(6) 复原，标 [复原]）

```
输入: 原日志 L_0 ∈ B(U_A*); 采样比例 r（用户给定）
参数: w_act, w_dfr ≥ 0, w_act + w_dfr = 1, 默认 0.5 / 0.5           [PDF p.4]
输出: 样本日志 L_S
1  A ← actS(L_0)                                  // Step 1, Def 5        [PDF p.4–5]
2  D ← dfgS(L_0)                                  // Step 1, Def 6
3  for a ∈ A:  sig(a, L_0) ← |{σ ∈ L_0 : ∃i, σ(i) = a}| / |L_0|          // Step 2, 式 (2)
4  for (a,b) ∈ D: sig(⟨a,b⟩, L_0) ← |{σ ∈ L_0 : ∃i, σ(i)=a ∧ σ(i+1)=b}| / |L_0|  // 式 (3)
5  for σ ∈ L_0:                                   // Step 3
6      sigAvgAct(σ) ← Σ_{i=1..|σ|} sig(σ(i), L_0) / |σ|                    // 式 (4)
7      sigAvgDfr(σ) ← Σ_{i=1..|σ|−1} sig(⟨σ(i),σ(i+1)⟩, L_0) / (|σ|−1)      // 式 (5)
8      sigTotal(σ) ← w_act · sigAvgAct(σ) + w_dfr · sigAvgDfr(σ)           // 式 (6)
9  按 sigTotal 降序排序全部迹                       // Step 4                 [PDF p.5]
10 N ← 由 r 与 |L_0| 派生（取整规则原文未写）
11 L_S ← 排序后前 N 条
12 return L_S
```

**参数/排序/阈值逐项**：
- r：用户输入，实验取 5%–30% 步长 5% [PDF p.5 Step 4；p.7 VI.C]。
- N：Step 4 "top-N ranked traces are selected ... based on the input sample ratio" [PDF p.5]。取整规则未写；两处算例：L_C 例 15% × 75 = 11.25 → 样本 12 条 [PDF p.5]；Fig. 3 例 15% × 20 = 3 → 样本 3 条 [PDF p.5 Fig. 3]。由前者看是向上取整 [推断]。
- w_act、w_dfr：默认 0.5/0.5，理由为"避免偏向"；无调参实验 [PDF p.4]。
- 排序键：sigTotal 降序 [PDF p.5 "rank traces in descending order by sigTotal"]。并列（tie）处理未写。
- 阈值：无。预算之外的其他参数：无。迭代：无（单遍）。

**复杂度声明** [PDF p.5 左栏]：总体 O(n log n)，n = 日志中迹数；主要操作为迹显著性计算 O(n·m) 与排序 O(n log n)；"Since m ≪ n in real-world event logs, the sorting step dominates"。m 在该段未定义，按上下文应是迹的最大长度 [推断]。同段未计入第 3–4 行的活动/DFR 统计遍历，该遍历也是 O(n·m) [推断]。

**两处口径不一致（原文内部）**：
- (a) 选择单位：Fig. 3 中 L_S = [⟨a,b,c,e,f⟩², ⟨a,b,c,e,g⟩]（原日志 ⟨a,b,c,e,g⟩⁶）——取排名第一的变体全部 2 条，再取排名第二的变体 1 条凑满 N = 3，即**按迹计数、末位变体截断** [PDF p.5 Fig. 3]。而 L_C 算例的 L_C^{s'} 是 12 个**互异**变体各 ¹（原日志 ⟨a,c,d,e,h⟩¹⁶）[PDF p.5 右下]，若按迹计数，前 12 名会被 ⟨a,c,d,e,h⟩ 的 16 份填满 [推断]，故该算例看起来是**按变体各取一份**。两处不能同时成立 `[⚠️矛盾]`。ProM 实现取哪一种，原文未写 `[需验证]`。
- (b) 正文 "An illustrative example ... is given in Fig. 3, by taking the example log L_C and 15% sampling ratio as input" [PDF p.5 左栏]，但 Fig. 3 图内标注 "Original log L_E"，且其 8 个变体、7 个活动（a–g）与 L_C（23 变体、8 活动，含 h）不同 [PDF p.5 Fig. 3 vs p.3 L_C]。正文与图指向两个不同日志 `[⚠️矛盾]`。

**Def 5/6 示例排版错误** [PDF p.4]：例日志写作 L_E = [σ1 = ⟨a,b,d,e⟩, σ2 = ⟨a,c,e⟩, σ3 = ⟨b,c⟩, σ4 = ⟨b,d⟩]，随后却写 actS(L_C) = {a,b,c,d,e} 与 dfgS(L_C) = {⟨a,b⟩,⟨b,d⟩,⟨d,e⟩,⟨a,c⟩,⟨c,e⟩,⟨b,c⟩}——下标应为 L_E；集合内容与 L_E 一致（本人核对）。

### 4.2 Fig. 3 手算例复核 [PDF p.5 Fig. 3]（数值为原图所印；"复算"列为本人验算）

原日志 L_E = [⟨a,b,c,e,g⟩⁶, ⟨a,b,c,d,e,f,g⟩⁴, ⟨a,b,c,e,f⟩², ⟨a,c,b,e,f⟩¹, ⟨a,d,e⟩², ⟨b,c,d,e,f⟩³, ⟨b,d,c⟩¹, ⟨a,b,d,e,f⟩¹]，共 20 条迹、8 变体。

活动显著性（原图）：a 0.8、b 0.9、c 0.85、d 0.55、e 0.95、f 0.55、g 0.5。复算：a 出现在 σ1,σ2,σ3,σ4,σ5,σ8 → (6+4+2+1+2+1)/20 = 0.8 ✓；g 出现在 σ1,σ2 → 10/20 = 0.5 ✓；其余同法均吻合。**结论**：分母 |L| 与分子均按**多重集**计数（重复迹各算一次），不是按变体去重 [由复算得出]。

DFR 显著性（原图）：⟨a,b⟩ 0.65、⟨b,c⟩ 0.75、⟨c,e⟩ 0.40、⟨e,g⟩ 0.30、⟨c,d⟩ 0.35、⟨d,e⟩ 0.50、⟨e,f⟩ 0.55、⟨f,g⟩ 0.20、⟨a,c⟩ 0.05、⟨c,b⟩ 0.05、⟨b,e⟩ 0.05、⟨a,d⟩ 0.10、⟨b,d⟩ 0.10、⟨d,c⟩ 0.05。复算：⟨a,b⟩ ∈ σ1,σ2,σ3,σ8 → 13/20 = 0.65 ✓；⟨b,d⟩ ∈ σ7,σ8 → 2/20 = 0.10 ✓；其余吻合。

迹显著性（原图；sigAvgAct / sigAvgDfr / sigTotal）：σ1 0.8 / 0.525 / 0.6625；σ2 0.7286 / 0.5 / 0.6143；σ3 0.81 / 0.5875 / 0.69875；σ4 0.81 / 0.175 / 0.4875；σ5 0.77 / 0.3 / 0.535；σ6 0.76 / 0.5375 / 0.64875；σ7 0.77 / 0.075 / 0.4225；σ8 0.75 / 0.45 / 0.6。复算 σ1：(0.8+0.9+0.85+0.95+0.5)/5 = 0.8 ✓；(0.65+0.75+0.40+0.30)/4 = 0.525 ✓；0.5·0.8 + 0.5·0.525 = 0.6625 ✓。排序：σ3 > σ1 > σ6 > σ2 > σ8 > σ5 > σ4 > σ7。比例 15% → N = 3 → L_S = [⟨a,b,c,e,f⟩², ⟨a,b,c,e,g⟩¹]（原图右下）。

### 4.3 L_C 算例（LogRank 样本 vs sigRank 样本）[PDF p.3、p.5、p.6]

- 原日志 L_C：75 条迹、23 变体、8 活动（a–h）[PDF p.2 末行；p.3 列表]。IM 发现的模型 Fig. 1：a 起，并行块 {b, c, d}，e，f 回环至并行块前，h 或 g 终止 [PDF p.3 Fig. 1]。
- LogRank 15% 样本 L_C^s：12 迹/变体、152 事件、8 活动 [PDF p.3 右栏]；IM 模型 M_S 为 Fig. 4（原文称 "flower like structure"）[PDF p.6 Fig. 4]。
- sigRank 15% 样本 L_C^{s'}：12 迹、132 事件、8 活动，列表见 [PDF p.5 右下]（本人按列表逐条累加事件数 = 5×4 + 9×2 + 17×2 + 21 + 13×3 = 132 ✓）；原文称 IM 从 L_C^{s'} 发现的 M_S' 与 Fig. 1 相同，"model re-discoverability is guaranteed in this case" [PDF p.6 左栏]。
- 数值 [PDF p.6 左栏]：fitness(L_C, M_S) = 0.89，fitness(L_C, M_S') = 1；precision(L_C, M_S) = 0.38，原文接着写 "fitness(L_C, M_S') = 0.92"——按上下文应为 precision(L_C, M_S') = 0.92（排版错误，[推断]；由 F = 2·1·0.92/1.92 = 0.958 ≈ 0.96 反推吻合）；F-measure(L_C, M_S) = 0.53，F-measure(L_C, M_S') = 0.96。

### 4.4 Phase 2：效果评估流程 [PDF p.3 IV.A；p.5 IV.C]

```
输入: L_0, L_S, 发现算法 Θ = IM
1  M_0 ← IM(L_0);  M_S ← IM(L_S)
2  fitness(L_0, M_S)  ← 对齐式 fitness（引 [36]）
3  precision(L_0, M_S) ← 对齐式 precision（引 [37]）
4  F(L_0, M_S) ← 式 (7);  F(L_0, M_0) 同法
5  Quality(L_S, L_0) ← 式 (8)
6  效率: T = t_sample(L_0) + t_disc(L_S);  与 t_disc(L_0) 比较
```
说明：fitness 定义为"能被模型重放的迹的比例"，precision 为"模型生成行为被日志覆盖的比例"；引 [38] 说明二者存在权衡故用 F-measure [PDF p.5 右栏]。实验中的具体口径（比例档、重复次数、IMi 阈值映射）属下半部分 §5 范围，此处不展开。

### 4.5 公式全量恢复（纯文本，编号对齐原文）

- 式 (1) [PDF p.3]：Qua(L_S, L_0) = Q(L_0, M_S) / Q(L_0, M_0)。
- 式 (2) [PDF p.4]：sig(a, L) = | ∪_{σ∈L} {σ | ∃ 1 ≤ i ≤ |σ| ∧ σ(i) = a} | / |L|。分子释义："the number of traces that contain activity a in L"。
- 式 (3) [PDF p.4]：sig(⟨a,b⟩, L) = | ∪_{σ∈L} {σ | ∃ 1 ≤ i ≤ |σ|−1 ∧ σ(i) = a ∧ σ(i+1) = b} | / |L|。分子释义："the number of traces that contain directly-follows relation ⟨a,b⟩ in L"。
- 式 (4) [PDF p.4]：sigAvgAct(σ, L) = ( Σ_{i=1}^{|σ|} sig(σ(i), L) ) / |σ|。
- 式 (5) [PDF p.4]：sigAvgDfr(σ, L) = ( Σ_{i=1}^{|σ|−1} sig(⟨σ(i), σ(i+1)⟩, L) ) / (|σ| − 1)。
- 式 (6) [PDF p.4]：sigTotal(σ, L) = w_act · sigAvgAct(σ, L) + w_dfr · sigAvgDfr(σ, L)，w_act, w_dfr ≥ 0，w_act + w_dfr = 1；默认 w_act = w_dfr = 0.5。
- 式 (7) [PDF p.5]：F-measure = 2 × fitness × precision / (fitness + precision)。
- 式 (8) [PDF p.5]：Quality(L_S, L_0) = F-measure(L_0, M_S) / F-measure(L_0, M_0)。

**记法备注**：
- 式 (2)(3) 用 "∪_{σ∈L} {σ | …}" 的集合并写法。若严格按集合语义，L 中重复迹并入后只剩一个元素，分子将变成"变体数"而分母 |L| 是迹数；Fig. 3 的数值（a: 16/20 = 0.8）表明实际实现按多重计数（§4.2 复算）。原文记法与实际口径之间有这一处松动 [推断]。
- 式 (2)(3) 中 "∃1 ≤ i ≤ |σ| ∧ σ(i) = a" 是原文写法（量词与合取混写），此处照录不改。
- 式 (5) 在 |σ| = 1 时分母为 0，原文未处理 [推断]；实验日志是否含单事件迹未说明 `[需验证]`。
- 式 (1) 与式 (8) 的关系：式 (8) 是式 (1) 取 Q = F-measure 的实例；原文两处符号不同（Qua vs Quality）[PDF p.3、p.5]。

---

`[§0–§4 完成；§5 及以后为下半部分，本文件不含]`


---

## 合并说明与 errata（主窗 2026-09-04 02:5x，依据 `10_SIGRANK_p2_tables.md` 校验段 C1–C7 与"对照"段）

本文件 = `10_SIGRANK_p1.md`（§0–4）+ `10_SIGRANK_p2.md`（§5–9）+ `10_SIGRANK_p2_tables.md`（三表逐格）按顺序拼接；三份 part 文件保留不删。p2 写作时三张表尚未回填（图像嵌入，文本层无数字），下列 p2 叙述与回填后的表**不一致**，以表为准，p2 原句不改（改了就看不出谁先谁后）：

| p2 位置 | p2 原叙述 | 表回填后的事实 | 处置 |
|---|---|---|---|
| §5.4 | Fig. 6 为"采样时间曲线/折线图" | Fig. 6 是**堆叠柱状图**（采样时间 + 发现时间），柱身无数字 `[PDF p.9–10 图读数]` | 读 §5.4 时按柱图理解 |
| §5.5 / §5.7-5 | "IMi 无采样步骤，其总时间如何计入 Table III" `[需验证]` | Table III **没有 IMi 列**；9/12 的分母不含 IMi | 该质疑不成立，撤销 |
| §5.1 第 7 条 | Table II 逐档还是六档均值 `[需验证]` | **逐档**列示（6 比例 × 9 方法 × 12 日志），已拆成 6 张子表 | 已解 |
| §5.6-1 | 原文自报"10/12 相对 LogRank/LogRank+ 最高" | 按逐格表三种计数规则（六档全胜 6/12、多数档 11/12、均值 12/12）都不得 10/12 | 作者计数规则不明 `[需验证]`，见 tables「对照」段 |
| §5.7-3 | "逐档赢输表原文未给" | 逐档 F-measure 已在 Table II；只有逐档**时间**没有数字（Fig. 6 柱图） | 措辞收窄 |

另有一处原文内部疑点由表回填暴露：ETMC4200 在 Table III 的 LogRank 总时间 84306 ms，与 Fig. 6(i) 最高柱刻度读数 ≈180k–190k 不符，分辨率不足以定读，标 `[⚠️矛盾·图读数不清]`（tables C6）。


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


---

# 10 · sigRank（TSC 2026）Table I / II / III / Fig. 6 逐格抄录（补 p2 §5.2–§5.5 四处 `[待补]`）

> 来源：`research/papers_lu/sigRank-2026-TSC.pdf`，`Read` 带 `pages` 逐页判读 p.6 / p.8 / p.11 / p.9 / p.10。三张表均为图像嵌入，**每个数字都是页面图像判读**，全表统一标 `[PDF p.N 图读数]`；单格另加 `[?]` 表示该格数字辨识把握较低（3/8、6/0、1/7 易混）。不含任何 EdgeIM 内容。

---

## Table I `[PDF p.6 图读数]`

- 原文表题：*BASIC STATISTICAL INFORMATION (#Trace: NUMBER OF TRACES, #Event: NUMBER OF EVENTS, #Variant: NUMBER OF VARIANTS, AND #Activity: NUMBER OF ACTIVITIES)*
- 单位：计数（无单位）。表内无 "-"、无加粗。
- 注意：表体列序为 **Event Log | #Event | #Trace | #Variant | #Activity**（#Event 在 #Trace 前），与表题列举顺序（#Trace 先）不同；p2 §5.1/§5.2 写的 "#Trace/#Event" 是表题顺序。
- 行分组标签（表左侧竖排）：前 6 行 "Synthetic Logs"，后 6 行 "Real-life Logs"。

| 分组 | Event Log | #Event | #Trace | #Variant | #Activity |
|---|---|---|---|---|---|
| Synthetic | trainingLog1 | 13608 | 1000 | 851 | 18 |
| Synthetic | trainingLog2 | 9251 | 1000 | 907 | 20 |
| Synthetic | trainingLog3 | 8197 | 1000 | 590 | 22 |
| Synthetic | trainingLog5 | 22299 | 1000 | 976 | 28 |
| Synthetic | trainingLog7 | 15187 | 1000 | 993 | 28 |
| Synthetic | SimulateLog2000 | 52000 | 2000 | 2000 | 26 |
| Real-life | 2000AllNoise | 128823 | 2000 | 2000 | 113 |
| Real-life | NASA | 73638 | 2566 | 2513 | 47 |
| Real-life | ETMC4200 | 23168 | 4203 | 16 | 7 |
| Real-life | order | 6358 | 1000 | 9 | 8 |
| Real-life | Final | 21348 | 4580 | 226 | 14 |
| Real-life | BPI2012_A | 146044 | 13087 | 32 | 10 |

---

## Table II `[PDF p.8 图读数]`

- 原文表题：*QUALITY COMPARISON RESULTS (F-MEASURE–BASED SAMPLE-LOG QUALITY COMPARISON ACROSS SAMPLING RATIOS (5% - 30%, STEP -5%) ON 12 EVENT LOGS; HIGHER IS BETTER)*
- 单位：F-measure（无量纲，[0,1]）。原表每个日志一个子块（"Sample Ratio" 6 列：5% 10% 15% 20% 25% 30%；"Techniques" 9 行，行序 IMi、Fre_Based、Sim_Based、hybrid、Longer、shorter、LogRank、LogRank+、sigRank）。**原表是逐档列示，不是六档均值**（回应 p2 §5.1 第 7 条 `[需验证]`）。
- 标记：表内**无 "-"**（p2 §5.3 "-" 含义一项无需补）；加粗 = 该日志该比例列中的最高值（表注只写 "Higher is better"，"加粗=最优"是从版面推断，未见文字表注）。下面按**采样比例拆 6 张子表**（每张 12 日志 × 9 法），加粗照原表抄。
- 方法列缩写：Fre = Fre_Based，Sim = Sim_Based，hyb = hybrid，Lon = Longer，sho = shorter，LR = LogRank，LR+ = LogRank+，sig = sigRank。

### II-a · 5%

| Log | IMi | Fre | Sim | hyb | Lon | sho | LR | LR+ | sig |
|---|---|---|---|---|---|---|---|---|---|
| trainingLog1 | 0.8943 | 0.8126 | 0.915 | 0.8875 | 0.7914 | 0.8835 | 0.7902 | 0.7902 | **0.9253** |
| trainingLog2 | 0.6789 | 0.24438 [?五位小数，照抄] | **0.7859** | 0.6634 | 0.5812 | 0.2443 | 0.4147 | 0.5014 | 0.7038 |
| trainingLog3 | 0.7387 | 0.5994 | 0.8576 | 0.8374 | 0.4167 | 0.5597 | 0.5994 | 0.401 | **0.9018** |
| trainingLog5 | 0.5929 | 0.2097 | 0.3281 | 0.3281 | 0.1865 | **0.6226** | 0.2171 | 0.2137 | 0.2754 |
| trainingLog7 | 0.3662 | 0.2205 | 0.2085 | 0.3074 | 0.2052 | **0.7202** | 0.3593 | 0.2457 | 0.6935 |
| SimulateLog2000 | **0.9338** | 0.4457 | 0.5613 | 0.5613 | 0.4457 | 0.4457 | 0.5678 | 0.4824 | 0.5613 |
| 2000AllNoise | **0.8490** | 0.7072 | 0.6099 | 0.6125 | 0.7017 | 0.6105 | 0.6403 | 0.1888 | 0.3146 |
| NASA | 0.1366 | 0.3683 | 0.346 | 0.346 | 0.2105 | 0.3432 | **0.3696** | 0.2105 | 0.3146 |
| ETMC4200 | 0.9773 | 0.867 | 0.867 | 0.867 | 0.9284 | 0.967 [?] | 0.9036 | 0.9773 | **1** |
| order | **0.8938** | 0.4351 | 0.1584 | 0.5706 | 0.7097 | 0.6837 | 0.214 | 0.5295 | 0.8076 |
| Final | 0.6789 | 0.9551 | 0.9551 | 0.9551 | 0.6099 | 0.9513 | 0.641 | 0.6312 | **0.9712** |
| BPI2012_A | 0.5050 | **0.5251** | 0.1556 | 0.2593 | 0.1556 | 0.1782 | 0.0926 | 0.2622 | 0.5243 |

### II-b · 10%

| Log | IMi | Fre | Sim | hyb | Lon | sho | LR | LR+ | sig |
|---|---|---|---|---|---|---|---|---|---|
| trainingLog1 | 0.8943 | 0.8006 | **0.8999** | 0.8999 | 0.7902 | 0.8824 | 0.8186 | 0.7902 | 0.8344 |
| trainingLog2 | 0.6789 | 0.6590 | **0.7819** | 0.7819 | 0.4707 | 0.4802 | 0.4802 | 0.6675 | 0.7123 |
| trainingLog3 | 0.7387 | 0.8773 | 0.8054 | 0.8576 | 0.3605 | 0.5994 | 0.5994 | 0.4073 | **0.9018** |
| trainingLog5 | 0.5929 | 0.1708 | 0.3281 | 0.3281 | 0.1652 | **0.6226** | 0.2092 | 0.1901 | 0.2877 |
| trainingLog7 | 0.3393 | 0.2055 | 0.2001 | 0.2001 | 0.2004 | **0.4811** | 0.253 | 0.2337 | 0.3769 |
| SimulateLog2000 | **0.9338** | 0.4458 | 0.5613 | 0.5613 | 0.4458 | 0.4458 | 0.5678 | 0.4825 | 0.5613 |
| 2000AllNoise | **0.8490** | 0.7159 | 0.7273 | 0.7159 | 0.7226 | 0.6105 | 0.6403 | 0.5015 | 0.6878 |
| NASA | 0.1333 | 0.2333 | 0.3361 | 0.3361 | 0.2105 | 0.349 | **0.3597** | 0.2105 | 0.3587 |
| ETMC4200 | 0.9773 | 0.867 | 0.867 | 0.867 | 0.9773 | 0.867 | 0.9161 | 0.9773 | **1** |
| order | **0.8938** | 0.4351 | 0.5337 | 0.5706 | 0.7097 | 0.6837 | 0.214 | 0.5295 | 0.8076 |
| Final | 0.6789 | 0.9551 | 0.9551 | 0.9551 | 0.6099 | 0.9513 | 0.6096 | 0.6312 | **0.9712** |
| BPI2012_A | 0.5050 | **0.569** | 0.2633 | 0.2593 | 0.2633 | 0.1782 | 0.2622 | 0.2622 | 0.5243 |

### II-c · 15%

| Log | IMi | Fre | Sim | hyb | Lon | sho | LR | LR+ | sig |
|---|---|---|---|---|---|---|---|---|---|
| trainingLog1 | 0.8943 | 0.8787 | **0.8999** | 0.8999 | 0.8186 | 0.8824 | 0.8186 | 0.8186 | 0.8787 |
| trainingLog2 | 0.6789 | 0.5304 | 0.6191 | 0.5896 | 0.4531 | 0.6512 | 0.3327 | 0.4775 | **0.7135** |
| trainingLog3 | 0.7387 | 0.8826 | 0.8054 | 0.8054 | 0.3605 | 0.7343 | 0.3413 | 0.4073 | **0.9018** |
| trainingLog5 | **0.6406** | 0.1761 | 0.2546 | 0.2546 | 0.1661 | 0.5262 | 0.2092 | 0.1661 | 0.2766 |
| trainingLog7 | 0.4534 | 0.2018 | 0.2021 | 0.2021 | 0.2004 | **0.6061** | 0.2218 | 0.2174 | 0.2367 |
| SimulateLog2000 | **0.9071** | 0.4442 | 0.5613 | 0.5613 | 0.4442 | 0.4442 | 0.5235 | 0.5677 | 0.5613 |
| 2000AllNoise | **0.8490** | 0.7273 | 0.7363 | 0.7273 | 0.7226 | 0.6105 | 0.6826 | 0.6037 | 0.7379 |
| NASA | 0.1333 | 0.2333 | 0.3417 | 0.3417 | 0.2105 | 0.3422 | **0.3886** | 0.2105 | 0.3489 |
| ETMC4200 | 0.9773 | 0.9251 | 0.9236 | 0.9251 | 0.9773 | 0.9236 | 0.9773 | 0.9773 | **1** |
| order | **0.8938** | 0.4351 | 0.5337 | 0.5706 | 0.7097 | 0.6837 | 0.3512 | 0.5295 | 0.8076 |
| Final | 0.6789 | 0.9551 | 0.9551 | 0.9551 | 0.5768 | 0.9513 | 0.6373 | 0.6295 | **0.9629** |
| BPI2012_A | 0.5050 | 0.3892 | 0.2593 | 0.2593 | 0.2593 | 0.2157 | 0.2622 | 0.2622 | **0.5243** |

### II-d · 20%

| Log | IMi | Fre | Sim | hyb | Lon | sho | LR | LR+ | sig |
|---|---|---|---|---|---|---|---|---|---|
| trainingLog1 | **0.8943** | 0.8464 | 0.7767 | 0.8097 | 0.8186 | 0.8859 | 0.8186 | 0.8186 | 0.8491 |
| trainingLog2 | 0.6789 | 0.5215 | 0.4502 | 0.5367 | 0.6879 | 0.7170 | 0.6080 | **0.7275** | 0.6123 |
| trainingLog3 | 0.8062 | 0.6229 | 0.8153 | 0.8153 | 0.3605 | 0.4599 | 0.3376 | 0.4073 | **0.9018** |
| trainingLog5 | **0.5987** | 0.1724 | 0.1974 | 0.1974 | 0.1661 | 0.565 | 0.2056 | 0.1661 | 0.2349 |
| trainingLog7 | **0.4368** | 0.2018 | 0.1997 | 0.1997 | 0.2004 | 0.3323 | 0.2004 | 0.1919 | 0.1927 |
| SimulateLog2000 | **0.9071** | 0.4786 | 0.5613 | 0.5613 | 0.4786 | 0.4786 | 0.4786 | 0.4785 | 0.5613 |
| 2000AllNoise | **0.8490** | 0.7273 | 0.7363 | 0.7791 | 0.7226 | 0.6105 | 0.7363 | 0.6045 | 0.828 |
| NASA | 0.1333 | 0.2333 | 0.342 | 0.342 | 0.2105 | 0.3422 | 0.2425 | 0.2105 | **0.349** |
| ETMC4200 | 0.9773 | 0.9251 | 0.9236 | 0.9251 | 0.9773 | 0.9236 | 0.9773 | 0.9773 | **1** |
| order | **0.8938** | 0.4351 | 0.5337 | 0.5706 | 0.7097 | 0.6837 | 0.3512 | 0.5295 | 0.8076 |
| Final | 0.7717 | 0.9551 | 0.9551 | 0.9551 | 0.6646 | 0.9513 | 0.6015 | 0.6295 | **0.9629** |
| BPI2012_A | 0.5050 | 0.3942 | 0.2593 | 0.2593 | 0.2593 | 0.2593 | 0.3128 | 0.4352 | **0.5243** |

### II-e · 25%

| Log | IMi | Fre | Sim | hyb | Lon | sho | LR | LR+ | sig |
|---|---|---|---|---|---|---|---|---|---|
| trainingLog1 | **0.8943** | 0.849 | 0.7767 | 0.7767 | 0.8186 | 0.8859 | 0.8186 | 0.8186 | 0.847 |
| trainingLog2 | 0.6789 | 0.4632 | 0.4963 | 0.5246 | 0.5574 | 0.3863 | 0.4831 | 0.6013 | **0.6802** |
| trainingLog3 | 0.8404 | 0.5568 | 0.5568 | 0.5988 | 0.3605 | 0.4599 | 0.3376 | 0.4073 | **0.9018** |
| trainingLog5 | **0.5987** | 0.1661 | 0.1824 | 0.1824 | 0.1661 | 0.5403 | 0.2056 | 0.1661 | 0.1857 |
| trainingLog7 | **0.6347** | 0.2018 | 0.2085 | 0.2085 | 0.2004 | 0.2566 | 0.1997 | 0.2036 | 0.2118 |
| SimulateLog2000 | **0.9188** | 0.4786 | 0.5613 | 0.5613 | 0.4786 | 0.4786 | 0.5154 | 0.4785 | 0.5613 |
| 2000AllNoise | **0.8490** | 0.7363 | 0.7363 | 0.7791 | 0.8305 | 0.6105 | 0.7363 | 0.6394 | 0.8341 |
| NASA | 0.1333 | 0.2333 | 0.3421 | **0.3528** | 0.2105 | 0.3422 | 0.2425 | 0.2105 | 0.3424 |
| ETMC4200 | 0.9773 | 0.9251 | 0.9762 | 0.9762 | 0.9773 | 0.9762 | 0.9773 | 0.9773 | **1** |
| order | **0.8363** | 0.689 | 0.5337 | 0.5706 | 0.7097 | 0.6837 | 0.4009 | 0.5295 | 0.8076 |
| Final | 0.7717 | 0.9551 | 0.9551 | 0.9551 | 0.6645 | 0.9513 | 0.6015 | 0.6295 | **0.9629** |
| BPI2012_A | 0.5050 | 0.3479 | 0.2672 | 0.2672 | 0.2672 | 0.2672 | 0.3128 | 0.4352 | **0.5243** |

### II-f · 30%

| Log | IMi | Fre | Sim | hyb | Lon | sho | LR | LR+ | sig |
|---|---|---|---|---|---|---|---|---|---|
| trainingLog1 | 0.8281 | 0.8351 | 0.8464 | 0.7767 | 0.8186 | **0.8859** | 0.8186 | 0.8186 | 0.8404 |
| trainingLog2 | 0.4882 | 0.5880 | 0.6611 | **0.6937** | 0.6204 | 0.4949 | 0.5353 | 0.6252 | 0.6629 |
| trainingLog3 | 0.8916 | 0.5568 | 0.5978 | 0.5988 | 0.3605 | 0.4654 | 0.3366 | 0.4073 | **0.9018** |
| trainingLog5 | 0.5062 | 0.1661 | 0.1824 | 0.1824 | 0.1661 | **0.5689** | 0.1904 | 0.1676 | 0.1857 |
| trainingLog7 | **0.6170** | 0.2026 | 0.2085 | 0.2085 | 0.2004 | 0.238 | 0.1997 | 0.2036 | 0.2342 |
| SimulateLog2000 | **0.9188** | 0.4787 | 0.5613 | 0.5613 | 0.4787 | 0.4787 | 0.5154 | 0.4787 | 0.5613 |
| 2000AllNoise | **0.8490** | 0.7363 | 0.7363 | 0.7791 | 0.8414 | 0.6105 | 0.7363 | 0.6924 | 0.8463 |
| NASA | 0.1481 | 0.2333 | 0.3528 | 0.3528 [?是否加粗不清] | 0.2105 | **0.368** | 0.2333 | 0.2105 | 0.3424 |
| ETMC4200 | 0.9773 | 0.9762 | 0.9762 | 0.9762 | 0.9773 | 0.9762 | 0.9773 | 0.9773 | **1** |
| order | **0.8363** | 0.689 | 0.5337 | 0.5706 | 0.7097 | 0.6837 | 0.4645 | 0.5295 | 0.8076 |
| Final | 0.7717 | 0.9551 | 0.9551 | 0.9551 | 0.6646 | 0.9513 | 0.6015 | 0.6295 | **0.9629** |
| BPI2012_A | 0.5050 | 0.3124 | 0.286 | 0.2672 | 0.286 | 0.286 | 0.3128 | 0.4352 | **0.5243** |

---

## Table III `[PDF p.11 图读数]`

- 原文表题：*OVERALL TIME PERFORMANCE (SUMMARY OF TIME PERFORMANCE IN MILLISECONDS: SAMPLING TIME PLUS DISCOVERY TIME, AVERAGED OVER SAMPLING RATIOS FROM 30% TO 5% (STEP -5%) FOR EACH EVENT LOG; LOWER IS BETTER.)*
- 单位：ms（六档均值）。首列表头原文 "Average Overall Time(ms)"。表内无 "-"；加粗 = 该行最低（p.11 右栏正文 "the most efficient technique for each dataset is boldfaced"）。
- **列只有 8 个方法：Fre_Based、Sim_Based、hybrid、Longer、shorter、LogRank、LogRank+、sigRank——没有 IMi 列。**

| Event Log | Fre_Based | Sim_Based | hybrid | Longer | shorter | LogRank | LogRank+ | sigRank |
|---|---|---|---|---|---|---|---|---|
| trainingLog1 | 5171.16 | 6608.83 | 6876.83 | 5557.66 | 5665.16 | 29018.66 | 2625.49 | **2057.99** |
| trainingLog2 | 9257.16 | 7638.33 | 7095.32 | 7618.83 | 6886.99 | 29548.99 | 4972.16 | **3564.5** |
| trainingLog3 | 4978.66 | 6541.66 | 6518.16 | 6013.99 | 6907.5 | 17089.66 | 3225 | **2585.33** |
| trainingLog5 | 8201.82 | 8309.33 | 9554.49 | 8277.66 | 7545.16 | 65275.49 | 7194.33 | **5739.16** |
| trainingLog7 | 6906.32 | 8700.16 | 8047.32 | 7188.16 | 7560.33 | 65152.82 | 8024.99 | **5486** |
| SimulateLog2000 | 19137.82 | 18623.33 | 18232.66 | 21001.66 | 20523.66 | 524498.5 | 24589.66 | **13539.83** |
| 2000AllNoise | 18426.49 | **15846.49** | 26591.66 | 26850.16 | 27145.66 | 2622291.82 | 40099.99 | 25360.82 |
| NASA | 9125 | 9489.49 | 10089.99 | 8839.49 | **8426.66** | 746341.5 | 33092.16 | 12119.83 |
| ETMC4200 | 14949.99 | 16685.32 | 17269.49 | 15819.49 | 18144.66 | 84306.16 | 13286.66 | **5799.49** |
| order | 1499.16 | 1341.32 | 4875.33 | 3989.66 | 4257.49 | 14872.16 | 685.66 | **359.33** |
| Final | 10367.82 | 11319.83 | 10884.49 | 11258.49 | 11240.16 | 130979.33 | 8325.82 | **3380.5** |
| BPI2012_A | 10260.32 | 6961.66 | 7705.16 | 6989.83 | **6559.16** | 147261.16 | 88527.16 | 9899.32 |

---

## Fig. 6 `[PDF p.9–10 图读数]`

- 图题："Fig. 6. Time performance comparison results."（p.9）/ "Fig. 6. Continued."（p.10）。12 个子图 (a)–(l) 按 Table I 行序各一日志。
- **图型是分组堆叠柱状图，不是折线图**（p2 §5.4 写"折线图"，不符）。图例 16 项（p.9 (a) 左上）：Mine-SigRank / Sample-SigRank / Mine-LogRank+ / Sample-LogRank+ / Mine-LogRank / Sample-LogRank / Mine-shorter / Sample-shorter / Mine-Longer / Sample-Longer / Mine-hybrid / Sample-hybrid / Mine-Similarity / Sample-Similarity / Mine-Frequency / Sample-Frequency，即 8 法 × (发现时间 + 采样时间) 堆叠；无 IMi。纵轴标签 "Sampling Time / Milliseconds"，横轴 "Sample Ratio"（5–30）。
- 逐柱数值**图读数不清**（柱身无数字标注），只能读纵轴量级；可读的仅为每子图最高柱（LogRank）落在的刻度区间：

| 子图 | 日志 | LogRank 堆叠柱高度区间（纵轴刻度读数） | 其余 7 法量级 |
|---|---|---|---|
| (a) | trainingLog1 | ≈27500–29500 | ≈2000–8000 |
| (b) | trainingLog2 | ≈28000–31000 | ≈3000–11000 |
| (c) | trainingLog3 | ≈16000–18500 | ≈2000–10000 |
| (d) | trainingLog5 | ≈63000–66000（断轴） | ≈4000–12000 |
| (e) | trainingLog7 | ≈64000–67000（断轴） | ≈5000–10000 |
| (f) | SimulateLog2000 | ≈513000–532000（断轴）；**横轴只有 10/15/20/25/30，无 5% 组** | ≈10000–24000 |
| (g) | 2000AllNoise | ≈2450000–2950000（三段断轴） | ≈15000–30000 |
| (h) | NASA | ≈735000–755000（断轴）；LogRank+ ≈31000–33000 | ≈5000–13000 |
| (i) | ETMC4200 | 上段刻度读作 180000/185000/190000 `[图读数不清·见校验 C6]` | ≈5000–20000 |
| (j) | order | ≈14500–15000 | ≈500–6000 |
| (k) | Final | ≈115000–145000（断轴） | ≈3000–12000 |
| (l) | BPI2012_A | ≈140000–155000（断轴）；LogRank+ ≈85000–90000 | ≈3000–12000 |

---

## 校验

- C1 Table I：#Variant ≤ #Trace 12/12 成立；#Event ≥ #Trace 12/12 成立；#Variant 极值 9（order）/ 2513（NASA）与 p1:L70 "9–2513" 一致。2000AllNoise 被归入 "Real-life Logs" 组——按名字像合成噪声日志，`[⚠️存疑]`，只记不判。
- C2 Table II 值域：全部落在 [0,1]；trainingLog2 Fre_Based 5% 为五位小数 "0.24438"，全表唯一，`[⚠️存疑：排版]`。
- C3 Table II 加粗 = 列最大：逐列复核，加粗值均为该列最大（含 NASA 30% shorter 0.368 > 0.3528）。并列但只加粗一个的格：trainingLog1 10%/15%（Sim 0.8999 = hyb 0.8999，加粗在 Sim）、trainingLog2 10%（Sim 0.7819 = hyb 0.7819，加粗在 Sim）——`[⚠️矛盾：并列处理规则未说明]`。
- C4 Table III 加粗 = 行最小：12/12 成立（trainingLog1–7、SimulateLog2000、ETMC4200、order、Final = sigRank；2000AllNoise = Sim_Based；NASA、BPI2012_A = shorter）。sigRank 最低 9/12，例外三者与 p.11 左栏正文 "Exceptions are the 2000AllNoise, NASA and BPI2012_A logs" 一致。
- C5 Table III 与正文：LogRank BPI2012_A 采样 141549 ms（p.11 左栏）< 总时间 147261.16 ms，方向自洽。
- C6 Table III 与 Fig. 6：LogRank 各日志总时间落在 Fig. 6 对应柱区间内 11/12（(a)(b)(c)(d)(e)(f)(g)(h)(j)(k)(l)）；**ETMC4200 不符**：Table III LogRank = 84306.16，而 (i) 上段刻度我读作 180000–190000。若刻度实为 80000/85000/90000 则一致；分辨率下无法定读，`[⚠️矛盾·图读数不清]`。
- C7 Fig. 6 (f) SimulateLog2000 横轴缺 5% 组，与"6 档比例"协议 `[⚠️矛盾]`（可能是 5% 组柱被裁出画幅，图读数不清）。

## 与 p2 正文 §5.6/5.7 的对照

- §5.6-1 "10/12 最高 F-measure（相对 LogRank/LogRank+）"：**不一致（计数规则未知）**。按抄录表：sigRank 六档全胜 LogRank 且全胜 LogRank+ 的日志 = 6/12（trainingLog1、trainingLog3、ETMC4200、order、Final、BPI2012_A）；按"多数档胜"= 11/12（NASA 对 LogRank 3/6 例外）；按六档均值 = 12/12。三种规则均不得 10。
- §5.6-2 "相对 Similarity-based 8/12"：**一致**（六档均值口径：胜 8 = tL1、tL2、tL3、tL7、ETMC4200、order、Final、BPI2012_A；负 3 = tL5、2000AllNoise、NASA；平 1 = SimulateLog2000）。
- §5.6-3 "相对 IMi 8/12 更好或交替"：**一致（条件性）**——全档胜 6（tL2 除 20% 一档、tL3、NASA、ETMC4200、Final、BPI2012_A），tL1、tL7 各 2/6 档反超即"交替"，6+2 = 8；纯"更好"只有 6/12。
- §5.6-4 "总时间 9/12 最低"：**一致**（C4）。
- §5.7-3 "Table III 把 6 档压成一个数"：**一致**；但 Table II 是逐档列示，"逐档赢输表原文未给"应改读为"逐档 F-measure 已给（Table II），逐档时间只有 Fig. 6 柱图无数字"。
- §5.5 / §5.7-5 "IMi 无采样步骤如何计入 Table III"：**不一致**——Table III 无 IMi 列，9/12 的分母里没有 IMi；该 `[需验证]` 与 §5.7-5 的口径质疑不成立。
- §5.4 "折线图"：**不一致**——Fig. 6 为堆叠柱状图。
- §5.1 第 7 条 "Table II 逐档还是均值"：**已解**——逐档。
