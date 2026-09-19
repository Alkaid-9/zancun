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
