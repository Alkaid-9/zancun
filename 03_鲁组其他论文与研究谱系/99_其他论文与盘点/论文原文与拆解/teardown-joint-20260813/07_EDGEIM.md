# 07 · EdgeIM（ICWS 2025）第一性原理全拆 —— D3 流程挖掘线首篇入档

> 主输入：`_launch/pdftxt/EDGEIM.txt` + 原 PDF `EdgeIM-2025-ICWS.pdf`（7 页，印刷页码 p.404–410，PDF 物理页 = 印刷页 − 403）。乱码处已用 pdftotext 分页重取核对：投影函数符号、Definition 5 集合条件、Algorithm 3 标题等错误属**原文排版/编辑问题**，非提取失真，下文逐处标明。
> 体量说明：7 页会议短文（正文约 4.5 页 + 1.5 页表 + 1 页参考文献），拆解密度按实际体量控制。

---

## 0. 身份卡

- **题录**：Xuan Su, Cong Liu, Faming Lu*, Long Cheng, Qingtian Zeng, Shouli Zhang. "EdgeIM: An Efficient Edge-based Process Model Discovery Technique". 2025 IEEE International Conference on Web Services (ICWS), Helsinki, pp. 404–410. DOI 10.1109/ICWS67624.2025.00057 [PDF p.404]。
- **作者线**：一作苏旋（山东科技大学计算机学院）——其 CCPE 2024 论文"Sampling business process event logs with guarantees"（本文引文 [27]，Definition 1 直接引用）是本文 Stage 1 采样技术的直系前身；二作刘聪（山东理工大学 + NOVA 里斯本信息管理学院双署名，D3 线的国际接口，鲁侧图标注"刘聪 NOVA 兼职[需验证]"）；**鲁法明通讯**（p.404 脚注"* Faming Lu is the corresponding author"）；曾庆田（山科大，苏旋的曾系师承）；Long Cheng（华北电力，中文名文中未给出）；Shouli Zhang（山东农业大学）[PDF p.404 作者栏]。
- **基金**：NSFC 62472264、52374221；科技创新 2030 重大项目 2022ZD0119501；山东省基金 ZR2024ZD22、ZR2024QF230；青岛西海岸新区专项 202209 [PDF p.404 脚注]。
- **venue 定位**：ICWS 是 IEEE 服务计算旗舰会（CCF-B），比家族前四篇的 IEEE Access/JAS/TST 期刊阵地更偏"会议短平快"；7 页短文体裁决定了它是**占位声明**而非完整方法学论文。
- **家族位置**：本卷 01–04 覆盖 D1（概率根因）与 D2（并发验证），本篇是 **D3（流程挖掘）主线首篇入档**——三主线并列格局自此在拆解卷内补全。方法论 DNA 与 01–04 完全同构（详见 §9）：找主流方法的信息丢失点（EdgeAlpha 丢环结构、丢时间戳冲突下的并发）→ 换更强形式底座补上。

## 1. Task：解决什么问题？形式化

**非形式陈述**：IoT 场景下事件数据生于分散的边缘节点，集中式过程发现（把全量日志运到中心再挖）受制于传输、存储、算力 [PDF p.404 摘要]；已有边缘式发现（EdgeMiner/EdgeAlpha）效率低且无法处理带环流程 [PDF p.404]。目标：在边缘架构下高效发现质量不低于集中式 Inductive Miner（IM）的 Petri 网模型。

**形式化（纯文本，按原文 Def 1–5 恢复 + 约束重构）**：

基础对象 [PDF p.405]：
- 活动集 A；事件日志 L ⊆ B(A*)，即迹（trace）的多重集；迹 σ = ⟨a1, ..., an⟩ 是活动序列（Def 1，引 [27]）。
- start(σ) = a1，end(σ) = an（Def 2）。
- 直接跟随关系集 R_L = { (ak, ak+1) | σ = ⟨a1, ..., ak, ak+1, ..., am⟩ ∈ L }（Def 3）。
- 权重函数 w: R_L → N+，w(a,b) = Σ_{σi∈L} Σ_{k=1..|σi|−1} δ(a, σ[k]) · δ(b, σ[k+1])，其中 δ(x,y) = 1 若 x=y 否则 0（式 2、式 3）。
- DFG G = (V, E, w)：V 活动集，E 直接跟随边集，w 边频次（Def 4，[PDF p.406]）。
- Petri 网 PN = (P, T, F, l)：库所集 P、变迁集 T、流关系 F ⊆ (P×T)∪(T×P)、标注函数 l: T → A，τ 为不可见标签（Def 5，[PDF p.406]；原文"P ∩ T = ∅, P ∩ T ≠ ∅"自相矛盾，应读作 P ∩ T = ∅ 且 P ∪ T ≠ ∅——原文排版错误）。

**问题**：设事件日志 L 需分派到 k 个边缘节点处理（分派规则：活动类型经一致性哈希映射到节点，j = hash(activity) mod k，[PDF p.407]）。求 Petri 网 PN，满足：
- (C1) 存储/计算约束：任一边缘节点只维护局部三元组 Local_i = (S_i, E_i, R_i)（局部起始活动集、终止活动集、带权直接跟随关系），规模 O(|A| + |A|^2)，与 |L| 解耦；
- (C2) 通信约束：上传中心的只有 k 份三元组，总通信量 O(k · |A|^2)，而非集中式的 O(|L|)；
- (C3) 质量约束：fitness(PN, L) ≈ fitness(IM(L), L) = 1，precision 与 F-measure 与集中式 IM 可比，且 PN 为 sound 的块结构模型（能表达顺序、并行、选择、循环四类结构）；
- (C4) 时间戳约束：事件时间戳不唯一（分布式采集导致冲突），t(ak) = t(ak+1) 时并发关系不得丢失 [PDF p.404 限制(2)、p.407]。

**本文的立足恒等式（未被原文明说，但整个方法建立在它之上）**：在 DFG 抽象上运行的 IM 只消费 (S, E, R_w) 三元组——它是该类算法的**充分统计量**。因此 (a) 凡不改变 (S,E,R) 的 case 删掉无损（Stage 1 采样合法性），(b) (S,E,R) 可按任意分片各自统计再做并集/求和（Stage 2–3 分布式合法性）。整篇论文 = 这一个恒等式的工程化。

## 2. Challenge：传统方法的挑战

按原文 Related Work 的四路对手逐一恢复 [PDF p.404–405]：

1. **集中式发现（AM/HM/IM/Split Miner 等，引 [3–8]）**：依赖全量日志集中存储与处理；大规模分布式数据下产生存储与计算瓶颈，且敏感数据集中传输有隐私暴露面 [PDF p.405 Related Work 首段]。
2. **分布式计算框架并行化（MapReduce 实现 alpha 算法，引 [20]；边缘预处理 + 中心聚合，引 [21]）**：仍依赖部分集中的数据聚合，本地与中心间需频繁数据交换，通信开销上升，难以满足实时要求 [PDF p.404 摘要、p.405]。
3. **流式发现（滑动窗口/近似计数/动态更新，引 [22,23]）**：实时性好，但在噪声处理、模型稳定性与精度之间做交换，"实时与高精度难以兼得" [PDF p.405]。
4. **差分隐私类（引 [26]）**：换取隐私时牺牲精度或增加计算开销 [PDF p.405]。
5. **直接对手 EdgeMiner/EdgeAlpha（Andersen, Rathje, Landsiedel 等，Kiel 系，引 [24,25]）**：在数据源（边缘节点）构建局部足迹矩阵、中心聚合出全局模型，降低中心开销并增强隐私。但有三个明确指出的缺陷 [PDF p.404]：
   - (1) 发现效率低：即便有 Most-Frequent-Predecessors（MFPs）与批处理优化，计算负担仍高，复杂流程下延迟显著；
   - (2) 时间同步处理不足：假设事件时间戳唯一，无法处理时间戳冲突，导致局部足迹矩阵中的并发关系被错误表示；
   - (3) 算法底座限制：现有实现 edgeAlpha 基于 Alpha Miner，**不能处理环结构**，复杂流程不适用。

**挑战的本质（第一性归纳）**：足迹矩阵（footprint）是 Alpha 系的充分统计量，但 Alpha 系本身表达力弱（无环、无不可见变迁、fitness 无保证）；IM 系表达力强且有 fitness 保证，但经典 IM 的递归发生在**日志**上（每层切分后要重建子日志的 DFG），日志不在中心手里时递归无法执行。所以真正的技术问题是：**能否把 IM 的递归从"切日志"降级为"切图"，使得边缘只需上传一次图摘要？**

## 3. Insight & Novelty

### 3.1 Inspiration 来源

- **I-A（架构）**：EdgeMiner 的"数据源本地统计 + 中心一次聚合"架构 [PDF p.404]——证明了"上传摘要而非日志"在过程发现里可行。
- **I-B（算法）**：IM 家族的 DFG 递归分解（引 [5] Leemans IM 原文；其引文列表中的 [6]（SoSyM 2018 可扩展发现）正是"直接在 DFG 上递归"的 IMd 变体出处，但正文未点破这一对应——推断标注）。
- **I-C（数据）**：一作苏旋自己的日志采样线（引 [27]，"带保证的日志采样"）——特征覆盖式采样可以在保证结构特征零丢失的前提下砍数据量。
- **I-D（领域常识）**：过程挖掘中"双向直接跟随 ⇒ 并行"的经典判据（IM 的 cut 检测基础）。

### 3.2 Insight 逐条

- **Insight 1（对应 I-B）**：IM-on-DFG 的全部输入是 (S, E, 带权 R)。这个三元组关于日志分片满足**可加性**：S = ∪S_i，E = ∪E_i，R 的权重逐边求和。所以分布式化不需要动算法本身，只需把统计量的构建下推到边缘。——方面：架构可行性。
- **Insight 2（对应 I-C）**：同一恒等式反过来读：凡是不给 (S,E,R) 带来新元素的 case，对最终模型零贡献（对不使用频次的 cut 判定而言），可以在进入边缘计算前丢弃。大日志里绝大多数 trace 是特征冗余的 ⇒ 砍掉它们就是免费加速。——方面：效率。
- **Insight 3（对应 I-D）**：时间戳冲突（t 相等）意味着顺序观测失效，而顺序观测失效恰好可以**主动翻译成并发证据**：同时注入 ⟨a,b⟩ 与 ⟨b,a⟩ 双向边，让 IM 的并行 cut 自然接住 [PDF p.406–407]。EdgeMiner 把冲突当脏数据，EdgeIM 把冲突当信号。——方面：数据质量→模型质量。
- **Insight 4（对应 I-A + I-B）**：EdgeAlpha 的无环缺陷不是边缘架构的固有代价，而是底座算法（AM）的表达力问题。换底座（AM→IM）即同时解决环结构与 fitness 保证，架构不用变。——方面：表达力。

### 3.3 Novelty 清单

- N1（流水线/架构）：三阶段边缘发现流水线"预处理与特征保持采样 → 边缘节点局部特征构建 → 中心合并与模型发现" [PDF p.406 Fig.3]。
- N2（策略）：特征覆盖式 case 过滤（Algorithm 1）。
- N3（方法）：带时间戳冲突处理的分布式 DFR 构建（Algorithm 2）。
- N4（方法）：中心侧"并集聚合 + DFG 递归分解"发现（Algorithm 3）。

### 3.4 Novelty 严格三段式

- **N1 三阶段流水线**
  - 解决什么问题：集中式的传输/存储瓶颈 + EdgeMiner 的效率低（§2 挑战 1、5(1)）。
  - 受哪个 insight 启发：Insight 1（统计量可加）+ Insight 4（架构与底座解耦）。
  - 设计了什么：Stage 1 对输入 case 按 ⟨CaseID, Timestamp⟩ 全排序并做覆盖采样；Stage 2 用一致性哈希把活动类型分派到 k 个边缘节点，各节点独立维护 (S_i, E_i, R_i)；Stage 3 中心做集合并/权重求和得全局 DFG，再递归分解产出 Petri 网 [PDF p.406 概览、p.407–408 细节]。
- **N2 特征覆盖采样**
  - 解决什么问题：冗余 case 造成的无效计算与节点间通信（§2 挑战 5(1)）。
  - 受哪个 insight 启发：Insight 2。
  - 设计了什么：维护全局特征集 (S, E, R)；遍历排序后的 case，仅当该 case 的起始活动 ∉ S、或终止活动 ∉ E、或其 DFR 集 Rtmp ⊄ R 时保留并更新全局集，否则过滤。用集合包含检查 Si ⊆ S ∧ Ei ⊆ E ∧ Ri ⊆ R 判定冗余，声称"关键过程结构特征零丢失" [PDF p.407 Algorithm 1]。
- **N3 冲突感知的分布式 DFR 构建**
  - 解决什么问题：EdgeMiner 的时间戳唯一性假设导致并发关系表示错误（§2 挑战 5(2)）。
  - 受哪个 insight 启发：Insight 3。
  - 设计了什么：边缘节点按时间戳排序活动构建局部 DFR；当相邻事件 t(ak) = t(ak+1) 时，把 ⟨ak, ak+1⟩ 与 ⟨ak+1, ak⟩ **同时**计入局部关系集，保留潜在并发结构；同时记录每个 case 的起止活动 [PDF p.406–407 Algorithm 2]。
- **N4 中心侧 DFG 递归发现**
  - 解决什么问题：EdgeAlpha 无法处理环结构、无 soundness（§2 挑战 5(3)）。
  - 受哪个 insight 启发：Insight 1 + Insight 4。
  - 设计了什么：中心并集合并局部三元组成全局 DFG；识别四类基础模式——顺序(→)、并行(∧)、选择(×)、循环(⟲)；把活动集切成互斥子集，对每个子集取 sub-DFG 递归挖掘，最后按检出模式拼装子网成完整 Petri 网 [PDF p.408 Algorithm 3]。**与标准 IM 的关键分叉：递归对象是 DFG 而非日志**（标准 IM 每层递归要切出子日志并重建其 DFG；EdgeIM 只有一次全局 DFG 构建，之后全在图上做 SplitDFG/Subgraph）。

## 4. 方法全恢复

### 4.0 数据流总图（文字版，对应 Fig.3 [PDF p.406]）

原始 cases（Case-1..Case-n）→ [Stage 1] 排序 + 特征提取（case 起始/终止/DFR 与全局集逐一"VS"比较）+ 采样 → 过滤后日志 D′ → [Stage 2] 按活动哈希分派到边缘节点 1..n，各节点产出 Node-i_start / Node-i_end / Node-i_dfr → [Stage 3] 中心节点收齐 AllNodes_start/end/dfr → Convert 成 DFG → IM 递归 → Petri 网。

### 4.1 Stage 1：预处理与特征保持采样（Algorithm 1 [PDF p.407]）

逐行恢复：
```
输入: cases 集 {σ1, ..., σn}
输出: 过滤后日志 D′, 全局特征 (S, E, R)
1  按 ⟨CaseID, Timestamp⟩ 字典序排序, 得有序 Case_ord
2  初始化 S ← ∅, E ← ∅, R ← ∅
3  for Case_ord 中每条迹 σ:
4      提取 s ← σ[0], e ← σ[-1], Rtmp ← {(σ[k], σ[k+1]) | 1 ≤ k < |σ|}
5      if (s ∉ S) ∨ (e ∉ E) ∨ (Rtmp ⊄ R):
6          D′ ← D′ ∪ {σ}
7          S ← S ∪ {s}
8          E ← E ∪ {e}
9          R ← R ∪ Rtmp
10     end
11 end
12 return D′, S, E, R
```
讲解：
- 第 1 行的全排序有双重作用：(a) 消除分布式采集造成的时间戳不确定性，建立确定性事件序 [PDF p.407]；(b) 使采样结果可复现（贪心保留依赖遍历序）。
- 第 5 行是核心判据的**否命题**：正文表述为"若 Si ⊆ S ∧ Ei ⊆ E ∧ Ri ⊆ R 则过滤"[PDF p.407]。保留条件 = 至少带来一个新特征。
- 正确性论证（原文只给一句"set-theoretic coverage strategy…fully represent the key features"[PDF p.407]，此处补全）：对任意特征 f ∈ S∪E∪R_L，考察 f 在遍历序中首次出现的迹 σf——处理 σf 时 f 尚不在全局集中，故第 5 行判真、σf 必被保留。因此 D′ 的特征并集 = L 的特征并集，即 (S,E,R) 层面零丢失。**注意保证只到集合层面，不到频次层面**（后果见 §6）。
- 复杂度 [PDF p.407]：排序 O(n·log n)（n = 事件总数）；特征检查逐迹进行，每次集合操作 O(m^2)（m = 单迹最大活动数），总体 O(n·m^2)。（点评：用哈希集合实现时子集检查可到 O(m)，O(m^2) 是朴素实现口径的保守界——推断。）

### 4.2 Stage 2：边缘节点局部特征构建（Algorithm 2 [PDF p.407]）

逐行恢复：
```
输入: 过滤后 D′, 全局特征 (S, E, R)
输出: 各节点局部特征 {Local_i = (Si, Ei, Ri)}
1-5  for 每个节点 ni ∈ N: Si ← ∅; Ei ← ∅; Ri ← ∅
6    for D′ 中每条迹 σ:
7        for σ 中每个事件 e:
8            j ← hash(e.activity) mod k
9-11         if e 是 σ 首事件: Sj ← Sj ∪ {e.activity}
12-14        if e 是 σ 末事件: Ej ← Ej ∪ {e.activity}
15           if 存在前驱事件 e_prev:
16-18            if e_prev.timestamp == e.timestamp:
                     Rj[⟨e_prev.activity, e.activity⟩] += 1
                     Rj[⟨e.activity, e_prev.activity⟩] += 1
19-21            else:
                     Rj[⟨e_prev.activity, e.activity⟩] += 1
22-24    end; end
25   return {Local_i = (Si, Ei, Ri)}
```
讲解：
- 分派规则：一致性哈希把**活动类型**（非 case、非事件）映射到节点，声称保证负载均衡 [PDF p.407]。关系 ⟨e_prev, e⟩ 按**后继活动** e 的哈希落点入桶（第 8 行 j 由 e.activity 决定）。
- 时间戳冲突分支（16–18 行）是 N3 的落点：双向关系同时进入**同一个桶 j**。按分派规则，反向对 ⟨e, e_prev⟩ 本应属于 hash(e_prev.activity) 的桶——分片规则在此被打破，但因为 Stage 3 对所有桶做无差别并集，全局正确性不受影响（推断；原文未讨论）。这说明分片仅是**计数分工**，不是语义分区。
- 复杂度 [PDF p.407]：哈希 O(1)/事件；特征构建 O(n)，n = 过滤后事件数。
- 【篇幅所限未展开：伪代码签名把全局 (S,E,R) 列为输入，但循环体从未使用它，用途原文未说明；k 的取值、一致性哈希的具体实现、节点故障处理均未给出。】

### 4.3 Stage 3：中心合并与模型发现（Algorithm 3 [PDF p.408]）

原文标题误写为"Feature-Preserving Sampling"（与 Algorithm 1 重名，复制粘贴错误——内容实为中心合并与发现）。逐行恢复：
```
输入: {Local_i = (Si, Ei, Ri)}
输出: Petri 网 PN
1   S ← ∅, E ← ∅, DFG ← 空图
2-8 for 每个 Local_i:
        S ← S ∪ Si;  E ← E ∪ Ei
        for (a,b) ∈ Ri: DFG(a,b) ← DFG(a,b) + Ri(a,b)   // 权重逐边求和
9   函数 MineModel(DFG, S, E):
10-12   if |DFG.nodes| = 1: return CreateLeafNode(DFG.nodes[0])
13      pattern ← DetectBasePattern(DFG)    // → 顺序, ∧ 并行, × 选择, ⟲ 循环
14      partitions ← SplitDFG(DFG, pattern) // 活动集切成互斥子集
15-20   for 每个分块 P ∈ partitions:
            subDFG ← Subgraph(DFG, P)
            subnet ← MineModel(subDFG, S, E)
            subnets ← subnets ∪ {subnet}
21      PN ← MergeSubnets(subnets, pattern)
22      return PN
23  PN ← MineModel(DFG, S, E)
24  return PN
```
讲解：
- 第 2–8 行就是 §1 恒等式的可加性方向：S/E 取并集、R 逐边加权重，得到与"在 D′ 上集中构建"完全相同的全局 DFG。
- 第 9–22 行沿用经典 IM 的递归分解骨架 [PDF p.408 引 [5]]：检测四类基础模式 → 按模式切分活动集 → 子图递归 → 按模式拼装（顺序模式拼成串联、并行模式拼成 AND 块、选择拼成 XOR 块、循环拼成重做块，块结构保证 soundness）。
- **与标准 IM 的分叉点（全文最重要的技术判断，原文自己在 p.408 实验讨论里承认）**："recursive discovery approach from the DFG, compared to the IM's divide-and-conquer approach applied to the event log"——标准 IM 每层递归切的是**日志**（子日志能看到活动的非相邻共现、频次分布，用于 fall-through 与过滤），EdgeIM 切的是**图**（只剩邻接信息）。这正是文献中 IMd（Inductive Miner–directly-follows，其引文 [6] 的核心）走过的路，原文引了 [6] 却未点破等价性（推断标注）。后果：不可见变迁的放置方式不同 → precision 出现双向偏移（见 §5 Table II：4 个日志升、1 个日志降）。
- 复杂度 [PDF p.408]：聚合 O(k·m)（k = 边缘节点数，m = 单节点最大关系数）；递归发现沿用 IM 的 O(A^3)（A = 活动数），主要开销在 DFG 递归划分与子图抽取。

### 4.4 公式全量恢复（纯文本）

- 式(1) 投影函数 [PDF p.405]：⟨⟩↾Q = ⟨⟩；(⟨x⟩ ◦ σ)↾Q = σ↾Q 若 x ∉ Q；= ⟨x⟩ ◦ (σ↾Q) 若 x ∈ Q。（原文"↾Q ∈ X* ß Q*"为排版乱码，应读作 ↾Q : X* → Q*。）
- 式(2) DFR 权重 [PDF p.405]：w(a,b) = Σ_{σi ∈ L} Σ_{k=1..|σi|−1} δ(a, σ[k]) · δ(b, σ[k+1])。
- 式(3) Kronecker delta [PDF p.405]：δ(x,y) = 1 若 x = y，否则 0。
- 式(4) F-measure [PDF p.408]：F = 2 × fitness × precision / (fitness + precision)。
- 序列拼接（背景，无编号 [PDF p.405]）：σ = u ◦ v ⟺ σ(i) = u(i)（1 ≤ i ≤ |u|），σ(i) = v(i − |u|)（|u|+1 ≤ i ≤ |u|+|v|）。
- 原文例子勘误 [PDF p.405 Def 3 下方]：对其声明的日志 L = [⟨x,a,b,c,e,y⟩^2, ⟨x,a,c,b,e,y⟩^2, ⟨x,a,b⟩]，(a,b) 实出现 3 次（2+1）、(a,c) 实出现 2 次；原文称"(a,b) occurs twice, (a,c) occurs 4 times"，数字对不上（疑似沿用了 Def 1 例子里指数为 4 的另一份日志）。Def 2 例子的 σ1 = ⟨x,a,c,e,y⟩ 也与 Def 1 例子的 σ1 = ⟨x,a,b,c,e,y⟩ 不一致。短文编辑粗糙的直接证据。

## 5. 实验协议与结果批判

### 5.1 协议

- 实现：PM4Py 平台上实现 EdgeIM [PDF p.408]。
- 硬件：Intel Xeon Silver 4210R（2.4GHz，10 核/20 线程，"total 40 cores"），27.5MB L3，Ubuntu 22.04.2 LTS [PDF p.408]。（自相矛盾：4210R 单颗为 10C/20T，"共 40 核"若为双路应是 20C/40T——原文表述内部不一致。）
- 数据：9 个公开日志（4TU 仓库，脚注 2）[PDF p.408]。
- 对比：Alpha Miner（AM）、Inductive Miner（IM）、EdgeAlpha、EdgeIM [PDF p.409 Table II]。
- 指标：fitness [30]、precision [31]、F-measure [29]（式 4）；时间性能只比 EdgeAlpha vs EdgeIM（理由：AM/IM 不含边缘数据处理，不可直接比 [PDF p.409]），每数据集跑 5 次取平均 [PDF p.409]。

### 5.2 Table I 日志统计逐格抄录 [PDF p.409]

| 日志 | #Trace | #Event | #Activity | 迹长Min | 迹长Avg | 迹长Max |
|---|---|---|---|---|---|---|
| Sepsis Cases | 1050 | 15214 | 16 | 3 | 14 | 185 |
| exercise | 21 | 552 | 20 | 11 | 26 | 47 |
| ETM Configuration | 100 | 590 | 7 | 5 | 6 | 6 |
| BPI2013Incidents | 7554 | 65533 | 13 | 1 | 9 | 123 |
| TSL.anon | 17812 | 83286 | 40 | 3 | 5 | 47 |
| ICP.anon | 582 | 2956 | 6 | 5 | 5 | 9 |
| fightCar | 300 | 1467 | 7 | 4 | 5 | 7 |
| BPI2017OfferLog | 12899 | 58129 | 8 | 3 | 5 | 5 |
| ALLTrace | 2000 | 18364 | 10 | 8 | 9 | 12 |

### 5.3 Table II 模型质量逐格抄录 [PDF p.409]（每格：fitness / precision / F-measure；"-" = 无法发现或无法评估）

| 日志 | Alpha Miner | Inductive Miner | EdgeAlpha | EdgeIM |
|---|---|---|---|---|
| Sepsiscases | 0.16 / 0.4272 / 0.2328 | 1 / 0.0866 / 0.1594 | 0.16 / 0.4272 / 0.2328 | 1 / 0.1213 / 0.2166 |
| exercise | 1 / 0.6458 / 0.7848 | 1 / 0.2876 / 0.4467 | 1 / 0.6458 / 0.7848 | 1 / 0.3008 / 0.4625 |
| ETMconfig | 0.99 / 0.9918 / 0.9909 | 1 / 0.9918 / 0.9959 | 0.99 / 0.9918 / 0.9909 | 1 / 0.9918 / 0.9959 |
| BPI13Incid | 0.58 / 0.1489 / 0.2370 | 1 / 0.2672 / 0.4217 | 0.17 / 0.2837 / 0.2126 | 1 / 0.2837 / 0.4420 |
| TSL.anon | - / - / - | 1 / 0.66 / 0.7952 | - / - / - | 1 / 0.7801 / 0.8765 |
| ICP.anon | 0.62 / 0.2593 / 0.3657 | 1 / 0.5489 / 0.7088 | 0.62 / 0.2593 / 0.3657 | 1 / 0.443 / 0.6140 |
| fightCar | 0.81 / 1 / 0.8950 | 0.92 / 0.8525 / 0.8850 | 0.81 / 1 / 0.8950 | 0.81 / 1 / 0.8950 |
| BPI17Offe | - / - / - | 1 / 0.8246 / 0.9039 | - / - / - | 1 / 0.8246 / 0.9039 |
| AllTrace | 0.9 / 0.375 / 0.5294 | 1 / 0.9216 / 0.9592 | 0.9 / 0.375 / 0.5294 | 1 / 0.9216 / 0.9592 |

### 5.4 Table III 时间性能逐格抄录 [PDF p.410]（**原文未标注单位**；EdgeIM sum time = sampling time + discovery time，逐行验算成立）

| 日志 | EdgeAlpha time | EdgeIM sum | EdgeIM sampling | EdgeIM discovery |
|---|---|---|---|---|
| Sepsis Cases | 1957.3217 | 174.2978 | 4.732 | 169.5658 |
| exercise | 86.5827 | 90.6906 | 2.125 | 88.5656 |
| ETM Configuration | 85.4518 | 24.5927 | 4.214 | 20.3787 |
| BPI2013Incidents | 7574.9726 | 765.4889 | 5.299 | 760.1899 |
| TSL.anon | - | 580.5401 | 32.325 | 548.2151 |
| ICP.anon | 1200.6847 | 25.7998 | 6.877 | 18.9228 |
| fightCar | 125.6428 | 21.4605 | 6.215 | 15.2455 |
| BPI2017OfferLog | - | 681.4961 | 36.245 | 645.2511 |
| AllTrace | 2013.5815 | 21.0402 | 3.851 | 17.1892 |

我方计算的加速比（EdgeAlpha / EdgeIM sum，仅 7 个双方都能跑的日志）：Sepsis 11.2×、exercise 0.95×（**EdgeIM 更慢**）、ETM 3.5×、BPI13 9.9×、ICP 46.5×、fightCar 5.9×、AllTrace 95.7×；7 日志合计 13044.24 vs 1123.37 ≈ 11.6×。原文对 exercise 变慢的解释：数据集小、无冗余 case、预处理与采样固定开销占比高 [PDF p.409]。

### 5.5 支撑住的结论

1. **时间优势**：除 exercise 外全线大幅快于 EdgeAlpha（3.5×–95.7×），且 EdgeAlpha 在 TSL.anon/BPI2017OfferLog 直接失败（"-"）而 EdgeIM 可跑 [PDF p.410 Table III]——效率 claim 成立。
2. **fitness 保证**：EdgeIM 在 9 日志中 8 个 fitness = 1（继承 IM 家族保证）；唯一例外 fightCar 0.81，原文归因于日志含重复任务（duplicate tasks），模型把重复任务当同一任务 [PDF p.408]。
3. **环结构与 soundness**：Sepsis 含多起止活动与环结构，EdgeIM 用更多不可见变迁保证 soundness，EdgeAlpha/AM 无不可见变迁导致环节点从模型分离、soundness 受损 [PDF p.409]——"能处理环"的 claim 有 Table II 的 fitness=1 与该段定性讨论支撑。
4. **时间戳冲突处理**：EdgeAlpha 在 BPI13 上 fitness 从 AM 的 0.58 崩到 0.17（其余 6 个可比日志上 EdgeAlpha 与 AM 逐格全同），恰与 intro 攻击的"时间戳唯一性假设破坏足迹"一致；EdgeIM 同日志 fitness = 1 [PDF p.409 Table II]。（注意：这个最有力的证据链原文自己没有点出，是本拆解的连线——推断标注。）

### 5.6 没撑住的 claim（逐条）

1. **"EdgeIM's F-measure is comparable to that of the IM and superior to both EdgeAlpha and AM" [PDF p.409]**——被自家 Table II 两行否定：exercise 上 EdgeIM 0.4625 < AM/EdgeAlpha 0.7848（差 0.32，未被承认）；Sepsis 上 EdgeIM 0.2166 < AM/EdgeAlpha 0.2328（原文仅以"slightly lower"承认 Sepsis 一处）。fightCar 打平（0.8950）。"superior to both"实际是 9 行里 6 胜 1 平 2 负。
2. **"precision is about 40% higher than that of the IM"（针对 Sepsis 与 BPI2013Incidents 两个复杂日志）[PDF p.408]**——Sepsis 成立：0.0866 → 0.1213 = +40.07%；BPI13 不成立：0.2672 → 0.2837 = +6.2%（我方计算）。一半证据不达标；且 ICP.anon 上 precision 反而**降** 19.3%（0.5489 → 0.443），原文未提。
3. **通信开销 claim 零测量**：摘要与结论反复以"高通信开销"立论 [PDF p.404]，正文解释加速来自"removing redundant cases significantly reduces the mutual accesses among edge nodes" [PDF p.409]，但全文没有任何通信量/网络指标；实验在**单台服务器**上做 [PDF p.408]，边缘节点是进程模拟（推断），k（节点数）从未报告，无随 k 变化的扩展性实验。
4. **隐私 claim 无机制**：摘要与结论称"privacy-preserving model discovery" [PDF p.409 结论]，全文无任何隐私机制、威胁模型或实验；该叙事整体继承自 EdgeMiner [PDF p.404]，在本文中是空头支票。
5. **"IoT 场景"与数据错位**：立论全部围绕 IoT [PDF p.404]，但 9 个日志全是业务流程日志（医院 Sepsis、BPI 挑战赛、教学日志），无一 IoT 传感器日志。
6. **Table III 无单位**：正文与表头均未给时间单位。若按秒读，15K 事件的日志 IM 类发现要 169.6 无单位时间显得过大；若按毫秒读则量级合理（推断，无法从原文裁定）。同时 AM/IM 的集中式运行时间被以"不可比"为由整体隐去 [PDF p.409]，读者无法判断"边缘化税"相对集中式基线是赚是赔。
7. **采样率/压缩率未报告**：Stage 1 是效率卖点的一半，但 D′ 相对 L 的规模、各日志被过滤的 case 比例全文未给，只能从 sampling time 一列间接感知。【篇幅所限未展开：原文对 fall-through 处理与不可见变迁放置差异如何影响 precision 只有两句定性（p.408），无消融实验；N2/N3 两个机制各自贡献多少无从分离。】

## 6. Potential flaw

### 6.1 情境局限与延伸架构

- **"边缘"是逻辑分片而非物理现实**：Stage 1 需要对全体事件按 ⟨CaseID, Timestamp⟩ 全排序 [PDF p.407]——谁持有全量数据谁才能排序，排序发生处就是事实上的中心。这与"数据生于边缘节点"的 EdgeMiner 叙事（数据源即节点 [PDF p.404]）根本不同：EdgeIM 的节点按**活动类型**哈希分派，同一 case 的相邻事件散在不同节点，计算 ⟨a_k, a_k+1⟩ 需要后继节点看见前驱事件——真实部署里每个事件要路由到至多两个节点，这笔通信恰恰没被建模、没被测量。延伸架构维度：按 case 分片 vs 按活动分片的通信下界对比、节点动态合并/分裂（原文结论自己列为未来工作 [PDF p.409]）、层级聚合（边-雾-云）。
- **一致性哈希不保证负载均衡**：活动频次是重尾分布（高频活动占绝对多数事件），按活动**类型**哈希只均衡类型数不均衡事件量；单个热点活动节点会成为瓶颈。原文"ensuring balanced workload distribution" [PDF p.407] 无依据。

### 6.2 坏数据性质下的困难

- **噪声的结构性反向放大（最重要的缺陷）**：Algorithm 1 的保留判据是"带来新特征"。噪声迹（乱序、缺失、插入）的特征几乎必然是新的 ⇒ **覆盖采样对噪声迹的保留率趋近 100%，对干净迹反而过滤**。下游 IM-on-DFG 又不做频次过滤（权重在 cut 检测中未被使用，见 §4.3），一条噪声边足以改变 cut 结构。EdgeIM 在干净日志上无损的那个恒等式，在噪声日志上精确地反转成"噪声无损保留"。原文全程假设日志干净，噪声一词只出现在对流式方法的批评里 [PDF p.405]。
- **概念漂移无遗忘**：全局特征集 (S,E,R) 单调增长，无任何老化/遗忘机制。流程改版后旧行为的 DFR 永久留在集合里，发现的模型是新旧行为的叠加体。
- **不完整分片**：case 被截断（跨采集窗口、节点掉线）会制造假 start/end 活动，直接污染 S/E 集——而 S/E 恰是 IM 递归的 base 判定输入，错误会被递归放大到整个模型骨架。
- **等时间戳的粒度悖论**：双向边注入把"时钟粗"当"真并发"。若日志时间戳粒度是秒/分钟（业务系统常态），大量真顺序对会共享时间戳，被批量误判为并行块 ⇒ precision 塌陷。原文没有讨论时间戳粒度的适用条件，也没有消融。

### 6.3 哪个困难值得写 paper

**噪声/漂移感知的特征覆盖采样**是最值得写的：它是结构性缺陷（贪心集合覆盖必然全收新颖迹，而噪声天然新颖），修复需要把"新颖性"与"频次支持度"联合决策（例如：新特征进入候选区，达到支持度阈值才晋升全局集；配 decay 实现漂移遗忘）——问题定义干净、baseline 明确（本文 + IMf）、评测可用注入噪声的合成日志控制 ground truth，正对 05_FAMILY_SYNTHESIS 总结的组内评测惯式。次优选择：把"边缘"做实（真实多机部署 + 通信量实测 + 按 case/按活动两种分片的对比），补上本文最大的实验空洞。

## 7. Motivation 还原（问句形式）

1. IM 递归真正消费的最小信息是什么？——是 (S, E, 带权 R) 三元组。既然如此，为什么要把原始事件运到中心？（→ Insight 1，N1/N4）
2. 这个三元组关于日志分片可加吗？——可加（并集/求和）。那边缘节点只上传三元组，通信量就与日志规模解耦了？（→ N1）
3. 大日志里有多少 case 对三元组毫无贡献？——绝大多数（重复行为）。那在计算发生前把它们丢掉，是不是免费的加速？丢弃的合法性边界在哪里？——只到集合层面，不到频次层面。（→ Insight 2，N2）
4. EdgeAlpha 慢与无环，是边缘架构的错还是 Alpha 底座的错？——底座的错。那换成 IM 底座，架构要改吗？——不用，因为 IM-on-DFG 的充分统计量恰好也能分布式聚合。（→ Insight 4，N4）
5. 时间戳冲突为什么杀死 EdgeMiner 的并发表示？——它假设时间戳唯一，冲突时序列化是任意的。冲突本身是不是恰好就是并发的证据？——注入双向边，让 IM 的并行 cut 自己接住。（→ Insight 3，N3）
6. （反事实自问，原文未答）如果日志有噪声，"带来新特征就保留"还成立吗？——不成立，会精确反转。这暴露了整套方法的隐含前提：日志干净、时间戳粒度足够细、流程平稳。

## 8. 张力结构分析

**改变谁的想法**：
- 对 EdgeMiner 阵营（Kiel 系）：你们证明了"边缘统计 + 中心聚合"可行，但选错了底座——足迹矩阵绑定 Alpha 系，天花板是无环、无 soundness、低效；换成 DFG 三元组绑定 IM 系，同一架构立刻获得环结构、fitness 保证与一个数量级的加速。
- 对集中式 IM 用户：你们以为 IM 质量必须以集中日志为代价；实际上 IM 的 DFG 变体只需要一份可分布式聚合的摘要，"集中"从必需品降级为习惯。
- 对流式挖掘阵营：实时与精度的折衷不是唯一出路——把计算下推到边缘同样砍掉集中传输，且不牺牲模型质量的稳定性 [PDF p.405 对 [22,23] 的批评]。

**But 在哪里**：领域默认"分布式化 = 信息损失 = 质量损失"。本文的 But：对 DFG 类发现算法，分布式聚合在数学上无损（可加性），损失只可能发生在两个可控点——采样（集合层面无损、频次层面有损）与 DFG 抽象本身（丢弃非相邻依赖）。**残余张力（原文回避）**：第二个损失点正是它与标准 IM 的 precision 分歧来源（ICP.anon 降 19.3%），也是 DFG 抽象的表达力天花板——EdgeIM 的"无损"是相对于 IMd 类算法的无损，不是相对于日志全信息的无损。

**综述的张力结构**（Related Work 的四路对手构成一张 2×2 棋盘：数据位置 × 质量保证）：集中式占"集中+高质量"、MapReduce 并行占"半集中+高质量但通信贵"、流式占"分散+实时但质量不稳"、EdgeMiner 占"边缘+低质量（无环）"——EdgeIM 声称占领"边缘+高质量+高效"的空格。支撑该占位的证据链中，质量与时间两条腿是实的（Table II/III），通信与隐私两条腿是虚的（§5.6 第 3、4 条）。

## 9. D3 线定位注记

对照 LU_SIDE_MAP（W1 收拢版）：

- **坐标**：D3 = 流程挖掘主线；地图判定"边缘 PM 并跑点（全球仅 3-4 组：Bayreuth/HU Berlin/Sapienza）"。本篇的直接对手 EdgeMiner/EdgeAlpha 出自 Kiel 系（Andersen/Rathje/Landsiedel，Koschmider 参与 [25]）——EdgeIM 以"跟随者换底座超车"的姿态入场：架构承认对方原创（[24,25] 被完整致敬 [PDF p.404]），在对方主场指标（时间）上打出 3.5×–95.7×，并补上环结构与时间戳冲突两个能力缺口。**并跑成立**：鲁组（苏旋/刘聪/曾系）自此可算边缘 PM 的第 4-5 个玩家之一；但"并跑"的成色受限于单机模拟与零通信实测（§5.6），尚不是部署级并跑。
- **方法论 DNA 验证**：与 05_FAMILY_SYNTHESIS 提炼的选题公式（已有模型 X + 被忽略信息 Y → X+Y 消一类缺陷）完全同构——X = EdgeMiner 架构，Y = {IM 底座的环结构与 soundness、时间戳冲突的并发证据}；评测惯式同样吻合（小基准 + 2–4 个经典对比 + 精度/开销双报告），且弱点也同构：无真实规模场景、与所在领域最新 SOTA（IMd/IMf 的系统对比）脱节。D3 与 D1/D2 的差异：D3 用的是"图近似 + 现成算法族"，全程无 PN 理论机制创新（Petri 网只是输出格式）——这条线的技术门槛在数据工程侧，不在形式化侧。
- **人事接口**：苏旋（一作，采样线 [27] 的延续者，D3 学生主力）、刘聪（NOVA 双署名，D3 国际通道，也是本卷 03 篇的交点人物）、曾庆田/鲁法明（资源与通讯位）。进组后 D3 线的对话对象优先苏旋。
- **为 agentic 方向留下的接口**（只列不展开，bridge 卡另有 Agent 负责）：
  1. (S, E, R) 特征三元组 = "分布式行为摘要的最小充分统计量"这一设计模式，可平移为多 agent 系统中各宿主上传的 agent 行为摘要（活动 → agent 动作/工具调用）；
  2. 等时间戳双向边技巧与 LLM-MAS 日志的粗时钟并发问题同构（多 agent 动作时间戳冲突是常态）；
  3. 覆盖采样 = 轨迹新颖性过滤，可作 agent 轨迹去冗/异常初筛原语（但 §6.2 的噪声反转缺陷在对抗性 agent 场景会更致命——对手可以刻意制造"新颖"轨迹，这既是风险也是研究缝）；
  4. 本篇只做 discovery，不做 conformance、不做流式、不做漂移——恰好是地图 T2（轨迹 conformance + 边缘下沉二次差异化）要填的三块空白；EdgeIM 提供的是 T2 的"边缘基础设施存量"，不是竞争者。

---
*三道安全门自检：全部数字与引文均有 [PDF p.X] 锚点；EdgeAlpha-BPI13 崩溃与时间戳冲突的连线、O(m^2) 的保守界判断、单位为毫秒的猜测、IMd 等价性等推断处均已显式标注"推断"；正文 I–VI 节、三算法、四公式、五定义、三张表全覆盖，无跳过。*
