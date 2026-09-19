Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# Sommers 2025 知识图谱提取与批判性分析（B2 独立视角）

**题录**：Sommers D., Sidorova N., van Dongen B. "A ground truth approach for assessing process mining techniques". *Process Science* (2025) 2:1, Springer, DOI 10.1007/s44311-025-00006-8, Open Access CC BY 4.0 [PDF p.1]。30 页。Received 2024-12-11 / Accepted 2025-02-18 / Published online 2025-03-20 [PDF p.28]。
**体裁**：期刊长文；ICPM 2024 会议文（Sommers et al. 2024, pp. 41-48）的受邀扩展版 [PDF p.3, p.28]。
**页码约定**：[PDF p.N] = PDF 第 N 页 = 印刷页 "Page N of 30"，二者一致。
**证据来源**：PDF 30 页 vision 逐页读一遍（每页 ≤2 次）；`_launch/pdftxt/SOMMERS.txt` 仅作定位。
**本文件层级**：EVIDENCE，独立视角；未读 10_/11_/12_SOMMERS_p1/p2 与 bridge/。

---

# 第一部分：知识图谱提取

## 1. 核心概念及其关系

| # | 概念 | 论文内定义 / 角色 | 出处 |
|---|---|---|---|
| C1 | Ground truth（本文义） | 不是单个"真模型"，而是四元组 M0（期望行为的基模型）、M^S（叠加行为偏差的"真"过程模型）、M^L（再叠加记录错误的模型）、L'（模拟 M^L 所得日志）"together with the links between them"；每个日志事件可回链到 M^L 的变迁点火，再回链到 M^S / M0 的变迁，或被标记为对应偏差 | [PDF p.8] |
| C2 | gt 函数与距离 d | 评估者自定义 gt^f(M0, L', M^S, M^L) 得目标结果，再选距离 d；通用式 d(f(M0,L'), gt^f(M0,L',M^S,M^L))。CC 的 gt^CC = "the optimal alignment"：M0 原变迁的点火→synchronous move，偏差模式变迁→log/model move；d 可为序列或图编辑距离 | [PDF p.9] |
| C3 | Oracle | 动机层："able to tell whether the deviation detected in the alignments is a true deviation and whether we provide a correct explanation" [PDF p.2]；实现层："provides explanations by knowledge of which transitions have fired in the simulation" | [PDF p.2, p.24] |
| C4 | 偏差模式 π ∈ Π = Π^S ∪ Π^L | 形式上是含通配符 ⟨∗⟩ 的抽象过程模型 M̄（行为描述 + 抽象模型片段）；Π^S 行为偏差，Π^L 记录错误 | [PDF p.8, p.10] |
| C5 | Recording error 模式 RI | 采 Bose et al. 2013 的 Table 1（missing / incorrect / imprecise / irrelevant × case / event / belongs-to / C_attribute / position / activity name / timestamp / resource / E_attribute）；Table 2 已实现 7 个：RI^e_mi, RI^e_in, RI^o_mi, RI^o_in, RI^p_mi, RI^p_in, RI^a_in | [PDF p.6, p.10] |
| C6 | Behavioral deviation 模式 BI | 源于 Russell et al. 2006 建模模式的违反；Table 2 已实现 11 个：BI1 switching correlation, BI2 multitasking, BI3 skipping activity, BI4 neglecting object(s), BI5 overtaking in queue, BI6 in/decreasing capacity, BI7 switching roles, BI8 same resource on 4-eyes principle, BI9 different resource on resource memory, BI10 ignoring batching, BI11 long duration；RI 与 BI 之间以彩色连线标"counterpart"（日志表现相同、成因不同） | [PDF p.10] |
| C7 | 模型变换 Ψ | Ψ(M, π, h) = M ∪ h(π)（式 1），h 为通配符→M 元素的单射，源自 Ehrig & Padberg 2003；所有模式"additive in behavior"，只加不减，故"multiple deviation patterns do not interfere with each other" | [PDF p.13] |
| C8 | t-PNID | typed Petri nets with Identifiers（van der Werf et al. 2022）：变迁、带类型库所、带标签弧，令牌携带对象标识；方法宣称与形式无关，只要模式与基模型同形式 | [PDF p.10-11, p.13] |
| C9 | 模拟 sim | 对 M^L 做离散事件模拟得 L'；可加变迁权重（式 2：p(t^s_μ = t_μ \| w) = w(t)/Σ w(t')）与延时（如弧上 +N(15,6)）；条件权重 w: T×𝒯→R+_0 可按仿真时刻暂时禁用变迁，用于控制偏差频率 | [PDF p.15] |
| C10 | Object-centric 事件日志 | 框架"can therefore also be used to generate logs of object-centric processes"（对接 OPIDs / OC nets / synchronizing proclets）；对齐输入的日志是 "partially ordered set"；Basmer et al. 2024 把数据质量问题扩展到 object-centric 数据 | [PDF p.6, p.16, p.24] |
| C11 | 对齐三法 | γ°：per-object，逐对象孤立对齐，忽略交互（Carmona et al. 2018）；γ：systemic，整日志对模型、计入交互违反（Sommers et al. 2022）；γ̃：relaxed systemic，允许在日志与模型两侧放松对象交互（Sommers et al. 2024） | [PDF p.24] |
| C12 | 移动类型 | synchronous / log / model move；γ̃ 另有 relaxed synchronous move 与"alterings of correlations"（Fig. 11 的 τ_destroy / τ_create） | [PDF p.24-25] |
| C13 | 评估问题 AQ1-3 | AQ1 偏差是否被正确检测；AQ2 对齐多大程度反映 GT 解释；AQ3 偏差对计算时间的影响 | [PDF p.24] |
| C14 | 实际使用的评估量 | Table 3：responsible 对象集 + affected 对象集（下标）对 GT + 文字解释；Fig. 11 子对齐定性比对；Fig. 12 计算时长 | [PDF p.24-27] |

**关系邻接表**：
- C4 ⊇ C5, C6（is-a：Π^S、Π^L 是 Π 的子集）[PDF p.8]；C5 derived-from Bose 2013，C6 derived-from Russell 2006 [PDF p.10]。
- C7 uses C4 + C8（Ψ 把 π 经 h 并入 M）[PDF p.13]；C1 produced-by C7 链（M0→M^S→M^L）+ C9（M^L→L'）[PDF p.8-9]。
- C2 uses C1；C3 instantiates C1（oracle = 点火知识）[PDF p.9, p.24]。
- C11 evaluated-by C14，目标为 C2 的 gt^CC [PDF p.9, p.24]；C12 part-of C11 的输出 [PDF p.24]。
- C13→C14：AQ1/AQ2 由 Table 3 + Fig. 11 回答，AQ3 由 Fig. 12 回答 [PDF p.27]。
- C10 output-of C9 [PDF p.16]。
- C5 ↔ C6 counterpart：如 "RI^e_mi ... Skipping an activity ... (BI1) is a behavioral deviation being a counterpart of a missing event" [PDF p.10]——但 Table 2 同页把 skipping 编为 BI3、BI1 为 switching correlation [⚠️矛盾，见第二部分 §2]。

## 2. 理论框架图（文字描述，含推断）

主链（Fig. 1b）[PDF p.5, p.8-9]：
1. 输入 M0：已有的真实/手工/自动生成模型；论文只处理需求 (2) 偏差变化与 (3) ground truth，需求 (1) 模型多样性交给 PTALG 等 [PDF p.5]。
2. 选 Π^S 子集并给映射 h，逐个 Ψ 施加 → M^S；再选 Π^L 子集 → M^L [PDF p.8-9]。
3. sim(M^L) → L'，L' 编码"the complete information about the transitions that generated events" [PDF p.9]。
4. 只把部分信息（如变迁标签）交给被评技术，其余构成 GT [PDF p.9]。
5. f(M0, L') 与 gt^f(M0, L', M^S, M^L) 经 d 比较 [PDF p.9]。

对比链（Fig. 1a）：现有工具 M0 → sim → 干净日志 L → 日志操纵函数 ε^L → L'；论文指其两处不足：无"真系统"模型、操纵与过程行为无关而失去模型—日志链接 [PDF p.5, p.7]。

扩展链（Fig. 6）：n 个 Π^S 组合 × m 个 Π^L 组合 × k 组仿真参数 → n·m·k 个日志 [PDF p.17]。DS1 实例化为 Fig. 8 的树：M0 → M^S_∅ 与 M^S_1..n；只有 M^S_∅ 分支承接 {π^L_1}..{π^L_m}，M^S_i 分支以 ∅ 直通 M^L_{i,∅}；每叶一份日志 [PDF p.20]。

[推断] 评估回路在实验中未走到第 5 步的数值 d：p.24-27 只出现对象集比对、文字解释与时长，无任何 d 值；d 停留在 p.9 的"e.g."层面。
[推断] 通配符映射的角色约束（p.14："could be either checked in the model transformation, or the user should be instructed clearly"）在通用实现里未定；仅 Trident 因 RC ν-nets 的强限制"can be easily checked" [PDF p.16]。
[推断] "additive"（p.13）保证 M^S 的行为 ⊇ M0 的行为，故 L' 的任何轨迹都可由 M^S 解释；GT 解释是隐变量"具体哪条偏差变迁点火"，而非可从日志唯一辨识的量——这一点论文未讨论（见第二部分 §1）。

## 3. 关键数据表（逐数值解释）

**Table 1** [PDF p.6]：Bose 2013 分类的复制，4 行（missing / incorrect / imprecise / irrelevant）× 9 列；imprecise 行无 case/event 格，irrelevant 行只有 case/event 两格。要点：符号 RI^o_mi / RI^o_in / RI^o_im 同时出现在 "Belongs to" 列与 "Resource" 列（两列共用上标 o）[⚠️矛盾，同页符号碰撞]。论文后文只用 missing 与 incorrect 两类 [PDF p.6]。

**Table 2** [PDF p.10]：左 7 个 RI、右 11 个 BI（清单见 §1 C5/C6），中间多色连线表示 counterpart，连线未逐条编号，无法从图中确定每条 RI↔BI 对应 [图读数不清]。

**Fig. 7 / 9 / 10** [PDF p.18, p.20, p.22]：三个数据集的抽象基模型，紫色闪电 = 施加的 BI、黄色闪电 = 施加的 RI，闪电旁标模式号与短语。Fig. 7 可数出 6 紫 + 6 黄，与 p.18-19 清单一致；Fig. 9 可辨 3 黄，而 p.21 列 4 条 RI，第四条（cancel previous contract 的 false 标签）在图中未辨出 [图读数不清]；Fig. 10 为 7 阶段 A–G、3 操作员、每阶段 Capacity 1，标 3 紫 + 2 黄，与 p.23 一致。

**三个数据集的构成**（正文数字）：
- DS1 包裹递送：6 个 BI（BI5, BI7, BI10, BI3, BI9, BI2）各建一个 M^S，加 M^S_∅；6 个 RI（RI^e_in(1), RI^e_in(2), RI^e_mi, RI^o_mi, RI^o_in, RI^p_mi）全施于 M^S_∅ → 12 个 M^L、12 份日志，每份 2 个包裹、共用同一辆车 [PDF p.18-19, p.24]。
- DS2 能源合同：5 个 BI（BI7, BI9, BI10, BI2, BI11）合成单个 M^S，4 个 RI（RI^e_mi, RI^o_in, RI^o_in, RI^p_in）合成单个 M^L；"frequencies ... low"、"a large number of contract applications"，无具体数 [PDF p.21]。
- DS3 装配（Omron 规范模型）：3 个 BI（BI6, BI7, BI2）+ 2 个 RI（RI^o_in, RI^p_in）；"standard simulation parameters"，无具体数 [PDF p.23]。

**Table 3** [PDF p.26]（横排整页）：列 = Dev. | GT | γ° | γ | γ̃ | Interpretation；12 行按 DS1 的 6 RI + 6 BI 排列；格内为对象集（p 包裹、c 快递员、v 车、q 队列、d 仓库，[推断] 字母义），下标括号为 affected 对象集。正文给出的读法：γ° 只见"deviation's responsible object"；γ 见"all objects involved in the corresponding activity"；γ̃ "correctly separating responsible objects from affected objects"；RI^p_mi 行 "not considered a deviation in the context of alignments"（全空）[PDF p.24]。BI 侧：BI7、BI3 属孤立活动/对象层，三法都检出；其余 BI（交互层）γ° 不检出，"Except for BI9"；γ 全检出但不分责任对象；γ̃ 对 BI7、BI3 分得清，对其余 BI "the involved objects are detected without log and (labeled) model moves" [PDF p.25]。格内具体对象集 [表读数不清]，只可确认上述文字模式。标题写 "relaxed systematic (γ̃)"，正文为 "relaxed systemic" [⚠️矛盾 p.26 vs p.24]。

**Fig. 11** [PDF p.25]：两栏（RI^e_in "log as depot order"、BI2 multitasking）× 四行（GT, γ°, γ, γ̃），黄 = log move、紫 = model move、绿 = synchronous。定性结论：RI^e_in(1) 三法"none ... resolve the deviation correctly, as all conclude that the ring event is incorrectly logged instead of the order depot event" [PDF p.24]；BI2 下 γ° "show no deviations"，γ 检出但"explanation differs from the deviation pattern used to generate the log"，γ̃ 给出 relaxed synchronous move + 相关性改变，但"still allow for variance in their interpretation" [PDF p.25]。

**Fig. 12** [PDF p.27]：上图 "All methods" 对数轴 Duration (s) 约 10^0–10^4 量级，12 模式 × 3 法柱状；下排三分图 Object / Systemic / Relaxed 各自对数轴。正文结论：(1) 除 BI5、BI10、BI7 外三法呈"exponential increase"；(2) BI5、BI10 从 γ° 到 γ 增，到 γ̃ 无显著增；(3) BI7 三法无显著差 [PDF p.25]；下排：γ° 各模式相近、BI7 例外；γ 双峰（快/显著慢）；γ̃ 方差更大 [PDF p.27]。具体数值与是否有误差棒 [图读数不清]；上图第 6 个横轴标签疑与 Table 3 第 6 行 RI^p_mi 不同 [图读数不清][需验证]。

## 4. 引用网络（TOP 5 + 引用方式分析）

参考文献共 46 条 [PDF p.29-30，计数][需验证]。按承重排序：

| 序 | 被引 | 被引位置（句） | 引用方式 |
|---|---|---|---|
| 1 | Bose, Mans, van der Aalst 2013 | p.3 "BPIC event data was realistically noisy ... (Bose et al. 2013)"；p.6 Table 1 标题 "taken from Bose et al. (2013)" 与 "recording errors are subdivided into four categories"；p.10 "originating from the issues presented in Bose et al. (2013)" | 方法沿用：RI 分类整体采纳，是 Table 1/2 左半的骨架 |
| 2 | Sommers, Sidorova, van Dongen 2024 (ICPM) | p.3 "This paper is an extension of work originally presented in ICPM (Sommers et al. 2024)"；p.12-13 "In Sommers et al. (2024), a similar pattern ..." / "We refer to Sommers et al. (2024) for four more examples"；p.16 高级实现 | 自引·前身：模式细节外包给会议版 |
| 3 | Sommers, Sidorova, van Dongen 2022 (Petri Nets) | p.9 "multi-object alignments (Sommers et al. 2022)"；p.16 RC ν-nets 与 Trident 界面；p.24 "systemic alignments (γ) ... (Sommers et al. 2022)" | 自引·被评技术 γ 的来源 |
| 4 | Sommers, Sidorova, van Dongen 2024 (Petri Nets, model projections) | p.9 "relaxed multi-object alignments (Sommers et al. 2024)"；p.24 "relaxed systemic alignments (γ̃) ... (Sommers et al. 2024)" | 自引·被评技术 γ̃ 的来源 |
| 5 | Russell, ter Hofstede, van der Aalst, Mulyar 2006 | p.6 "A process model ties together a set of modeling patterns (Russell et al. 2006)"；p.10 "originating from violations of the modeling patterns discussed in Russell et al. (2006)" | 方法沿用：BI 一侧的来源，但未逐条说明哪条 BI 违反哪条工作流模式 |

次级：Jouck & Depaire 2019 (PTALG) / Burattin et al. 2022 (PURPLE) / Ko et al. 2020 (AIR-BAGEL) 在 p.2、p.4-5、p.19、p.21 作对比靶（"inject noise directly into simulated logs"），且 p.21 反过来把 PURPLE 当可互补的引导仿真；Rozinat et al. 2008 p.1-2 作动机框架（"challenges ... still remain relevant"）；Aalst et al. 2012 manifesto p.1 供"完整评估"六要素定义；van der Werf et al. 2022 p.10-11 供形式（t-PNID 语义"we refer to"）；Ehrig & Padberg 2003 p.13 为 Ψ 定义背书；Carmona et al. 2018 p.24 供基线 γ°。

引用方式判断：(a) 两条 "Sommers et al. (2024)" 与两条 "Sommers et al. (2023)" 在参考文献中并存 [PDF p.30]，正文未用 2024a/b 区分，读者须自行猜测 p.9/p.24 指 Petri Nets 版而 p.3/p.13/p.16 指 ICPM 版 [推断]；(b) 作者重叠的条目（Sommers 系 5 条 + van Dongen 的 BPIC 数据集 9 条 + Carmona 2018 + Dijkman 2011）约 16/46 [计数][需验证]，其中 BPIC 9 条只在 p.3 一句里成串出现，属"背景堆引"；(c) 被评的三种对齐中两种为自研，评估对象与评估框架同源。

---

# 第二部分：批判性分析

## 1. 方法论审视

**(1) "模式注入生成 ground truth"的含义**。GT 解释被定义为"哪条偏差变迁点火"[PDF p.24]，而模式"additive"[PDF p.13]，即 M^S 行为包含 M0 行为。因此 GT 是生成路径这一隐变量，而不是可从 (M0, L') 唯一辨识的量。论文自己的 RI^e_in(1) 案例已暴露这一点：三法都把"ring 记错"作为解释，而 GT 是"order depot 记错"[PDF p.24-25]——在只看标签的输入下，两种解释可能代价相同，"none resolve correctly"实际上是不可辨识问题，论文却按"方法失败"解读，且未讨论最优对齐的非唯一性（p.9 定义 gt^CC 为 "the optimal alignment"，冠词 the 默认唯一）。

**(2) 覆盖度与真实噪声**。模式库 7 RI + 11 BI [PDF p.10]，论文承认"inherently incomplete" [PDF p.28]；Table 1 的 imprecise / irrelevant 两类完全未实现 [PDF p.6, p.10]。"realistic"是标题级主张，但全篇没有一次把合成日志的统计量与真实日志（如 p.2 提到的 Omron 数据）比对；"resembles real-life behavior by design" [PDF p.16] 是设计论断而非检验。DS3 标题为 "Real-life assembly process" [PDF p.22]，实际只用了规范模型，日志全部合成，无真实事件参与 [PDF p.23]。

**(3) 对齐方法选择**。三法中 γ、γ̃ 为作者自研，γ° 为教科书基线 [PDF p.24]；"interpretability"由作者在 Table 3 最右列以文字判定 [PDF p.26]，无独立度量、无第三方对齐方法（如 Gianola et al. 2024 的 object-centric alignments 只在 p.16 作形式并列，未进入实验）。这使"evaluating the interpretability"（节标题 p.23）更接近示范而非评估。

**(4) 规模**。动机是"large-scale evaluation and validation practically impossible"用真实数据 [PDF p.2]，但实验为 12 份日志、每份 2 个包裹、单次运行 [PDF p.19, p.24]；Fig. 12 无重复实验与误差棒 [图读数不清]；DS2/DS3 只生成、不评估 [PDF p.21-23]。框架中的 k 组仿真参数在三个数据集里都取 k=1 [PDF p.19, p.21, p.23]，"impact of the simulation parameters"（p.3 自述贡献）只停留在 p.15-16 的概念讨论。

**(5) 方法的隐含假设**。偏差必须能用与基模型相同形式表达 [PDF p.28]；映射 h 的角色约束由用户负责 [PDF p.14]；仿真频率决定"真实感" [PDF p.28]——三者都由作者列为限制，但没有任何一项被量化。

## 2. 逻辑审视

**主张—证据缺口**：
- 摘要："provides detailed insights ... both quantitatively and qualitatively" [PDF p.1]；结论："we focused on the qualitative aspect of the evaluation" [PDF p.28] [⚠️矛盾 p.1 vs p.28]。计算时长是唯一数值，且未与任何 GT 距离 d 挂钩。
- gt^CC 定义在 move 粒度（同步/日志/模型移动）[PDF p.9]，实验比较却降到"对象集"粒度（Table 3）[PDF p.24, p.26]；§"Usage in assessments" 与实验之间粒度不一致，"how well ... reflect the ground truth explanations"（AQ2）没有被按定义回答。
- RQ 要求"complete assessment" [PDF p.8]，"complete"按 p.1 含 validation、评估、reliability、robustness、performance/scalability、usability 六项；论文只交付定性 validation + 时长，其余以"trivially extends" [PDF p.28] 带过，"trivially"无支撑。
- p.3 与 p.28 均称数据集特征"cannot be established / are not supported by existing ... methods"，但 DS1 段明说"it is actually not inherently infeasible to generate the same (or similar) event logs ... using the existing ... methods" [PDF p.19]；DS2/DS3 的"不可复现"只是论证（重复标签 p.22、模式互相影响 p.23），未用 PTALG/PURPLE 实际尝试 [⚠️矛盾-弱 p.19 vs p.3/p.28]。
- "exponential increase"（p.25, p.28）建立在三个离散方法的柱高之上，不是随输入规模的增长曲线；三点不能支撑"指数"。
- p.22 "the base model is not discoverable by ... Alpha Miner ... or the Inductive Miner, even for simulated event logs without any deviations"——无实验 [需验证]。
- p.13 "multiple deviation patterns do not interfere with each other" 与 p.23 "The patterns ... are all behaviorally influencing each other"——前者指变换结构、后者指仿真行为 [推断]，但同一术语两用未做说明。

**内部一致性（编号、术语、数据声明）**：
- [⚠️矛盾] p.10 正文 "Skipping an activity ... (BI1)" vs p.10 Table 2 BI1 = Switching correlation、BI3 = Skipping activity；p.18 亦用 BI3 = skipping。
- [⚠️矛盾] p.14 同页：先写 "changing correlation (BI1)"、"switching roles BI7"，两句后写 "the pattern BI2 for changing correlation"、"The pattern BI6 for switching roles"；对照 Table 2 [PDF p.10] BI2 = multitasking、BI6 = capacity。
- [⚠️矛盾] p.12 批量记录模式："⟨t1⟩batch log takes as long as processing the whole batch and ⟨t1⟩batch log takes a negligible amount of time"——两处同为 t1，Fig. 3 [PDF p.11] 显示应有 ⟨t2⟩batch log；该句因此不可读。
- [⚠️矛盾] p.14 BI5 映射 {⟨pq1⟩ ↦ p̄q2, ⟨pq2⟩ ↦ p̄q3} 用了通配符 ⟨pq2⟩，而 p.12 对 BI5 的定义只有 ⟨pq1⟩、⟨pqw⟩。
- [⚠️矛盾] p.5 "load it into a van (yellow)" vs p.6 Fig. 2 图注 "FIFO queue (yellow) ... delivery vans (orange)"。
- [⚠️矛盾] p.18 "All models and corresponding generated logs ... are available at gitlab.com/dominiquesommers/mira/..." 与 p.1 "create datasets of synthetic process data for three processes" vs p.28 Data availability "No datasets were generated or analysed during the current study"。
- [⚠️矛盾] p.24 "For recording errors, each deviation was detected by each method" vs 同页 "The last recording error (RI^p_mi) is not considered a deviation"——应为 5/6。
- [需验证] p.13 "four more examples of the patterns RI^e_mi, RI^e_in, BI3, BI2, and BI1"——列了五项。
- 术语漂移：PUPRLE（p.2, p.4）vs PURPLE（p.21）；systemic（p.24）vs systematic（Table 3 题 p.26）；switching correlation（Table 2）vs changing correlation（p.12, p.14）；M^S/M^L 与 M_S/M_L 在 p.8 同段混用；Fig. 9 图注 "for the energy contract process from, with" 残句 [PDF p.20]。
- DS2 第三条 RI 标为 RI^o_in（incorrect object），内容却是"accompanied with the data label of false" [PDF p.21]，按 Table 1 更像 E_attribute 类 RI^ea_in [推断]。

## 3. 贡献审视（p.3 自述五项逐条对照）

| 自述贡献 [PDF p.3] | 证据 | 判断 |
|---|---|---|
| 一般化为"从每个模式子集与仿真参数子集生成一组日志" | Fig. 6 概念（n·m·k）[PDF p.17]；DS1 仅单模式子集 + k=1 [PDF p.19-20]；DS2/DS3 各一模型一日志 [PDF p.21, p.23] | 概念成立，实证最小化；"every subset"未演示任何多模式组合下的 GT 可用性 |
| 三个数据集，特征"cannot be established using existing ... methods" | DS1 作者自认可由现有方法做出 [PDF p.19]；DS2/DS3 靠论证 [PDF p.22-23] | 部分成立；措辞在 p.28 被放大 |
| 工具支持现状描述 | 两个 GitLab 路径、支持的四种网类 [PDF p.16-17] | 成立，但无版本/提交号、无许可证、且与 p.28 数据声明冲突 |
| 通过示例展开模式与变换 | Fig. 3-5、式 (1) [PDF p.11-14] | 成立，是全文最扎实的部分；被编号错误与 t1/t1 笔误削弱 |
| 讨论仿真参数对日志的影响 | p.15-16 权重/延时/条件变量概念 | 仅概念；无敏感性实验，三数据集 k=1 |

未在 p.3 列出但实际承担分量的"贡献"是 p.23-27 的对齐评估；其结论（γ̃ 兼得检测与责任对象、BI7/BI5/BI10 上可解释性不以时间为代价 [PDF p.27]）建立在 12×2 包裹、单次运行之上，且 Fig. 12 中 γ̃ 在若干模式上达 10^3–10^4 s 量级 [图读数不清·近似]，对 2 个包裹的日志而言是明显的可扩展性信号，正文未讨论。

## 4. 可复现性

- **代码**：Trident 在 gitlab.com/vignesh_dv/mira/-/tree/paper/mira/pattern（他人账号、paper 分支），高级版在 gitlab.com/dominiquesommers/mira/-/tree/main/mira/simulation [PDF p.16]；无提交哈希、无版本号、无许可证说明；两处均为分支路径而非固定发布。
- **数据**：p.18 称模型与日志在高级版同一路径；p.28 Data availability 称"No datasets were generated or analysed"[⚠️矛盾]。若以 p.28 为准，评估数据不可得；若以 p.18 为准，声明失实。二者只能有一真 [PDF p.18 vs p.28]。
- **参数**：DS1 "a single set of simulation parameters that ensure that the patterns are invoked"[PDF p.19]、DS2 "frequencies ... low" + "large number"[PDF p.21]、DS3 "standard simulation parameters"[PDF p.23]——三者均无数值；无随机种子；无日志规模统计（事件数、轨迹数）。
- **实现细节**：对齐的代价函数、搜索算法、超时设置未给，全部外包给 Sommers 2022/2024 [PDF p.24]；"projection of the simulated logs with some types of deviating events (like skipped steps or missing events) removed"[PDF p.24]——具体移除规则未列举；Fig. 12 无硬件/环境说明 [PDF p.27]。
- **可核对项**：Table 2 的 18 个模式名、DS1 的 12 个模型组合、Fig. 8 的树结构可从正文完整重建；模式的 t-PNID 蓝图只给了 7 个（Fig. 3）[PDF p.11]，其余 11 个引向会议版或代码。
- **利益声明**：受邀扩展稿，第三作者为期刊共同主编，声明其未参与决策 [PDF p.28]；审稿周期约 10 周 [PDF p.28]。本身不构成缺陷，但与上述数据声明矛盾并置时，编辑核查显得薄弱 [推断]。

## 5. 总评（审稿人视角）

**一句话定位**：一篇把"记录错误 + 行为偏差"以模式—变换方式植入模型、再用仿真产出带可回链 ground truth 的合成数据框架论文；概念层清晰且有工具，评估层只做到"用自家对齐方法演示一次"。

**审稿判断 [推断]**（论文已发表，此为假想投稿态判断）：应为**大修**（major revision）。必须项：(i) 消除 BI 编号与 t1/t1 等使方法段不可读的错误 [PDF p.10, p.12, p.14]；(ii) 统一 p.18 与 p.28 的数据可得性声明；(iii) 摘要"quantitatively"与结论"qualitative"二选一 [PDF p.1, p.28]；(iv) 给出仿真参数与日志统计；(v) 讨论最优对齐非唯一性对"correct explanation"判定的影响 [PDF p.9, p.24-25]；(vi) 为两条 Sommers 2024 加 a/b。可选项：至少一个非自研对齐方法、至少一次 d 的数值化、k>1 的参数敏感性。

**独立视角补充**：论文最有价值的资产不是评估结果，而是 Table 2 的 counterpart 结构（同一日志现象由记录错误或行为偏差两种成因产生）[PDF p.10] 与"GT = 四元组 + 回链"的定义 [PDF p.8]；两者都独立于 t-PNID 与对齐方法，可迁移。最薄弱处是"realistic"从未被检验。

**与事件日志采样 / EdgeIM 的关系**：全文未提及 EdgeIM。与"日志缩减"最接近的原文仅一句："Käppel et al. (2021) developed an evaluation framework that reduces event logs and generates small event logs by removing traces either randomly or along the time dimension, producing training and test logs. Removal of traces can lead to side effects related to the workload of resources, case interactions, etc., making the log less realistic." [PDF p.4]。按本任务约束，不作进一步引申。

---
[FINAL · 两部分全节完成 · 每页 PDF 各读 1 次，未触发第二次判读]
