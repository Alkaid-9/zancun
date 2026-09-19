Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# 12 · Sommers（Process Science 2025）第一性原理全拆（上：§0–§4）—— 桥线 T1 必要辅助篇

> 主输入：原 PDF `research/papers_lu/Sommers-2025-ProcessScience.pdf`（30 页，印刷页码 = PDF 物理页，页眉 "Page N of 30"），判定以 `Read` PDF 为准；`_launch/pdftxt/SOMMERS.txt`（实际位于 `teardown-bridge-20260904/_launch/pdftxt/`）只用于定位。本篇与 EdgeIM 无作者关系，全文未提及 EdgeIM。
> 体量说明：期刊长文（正文约 27 页 + 2 页参考文献），本篇只做上半 §0–§4；§5 以后由下半篇承接。

---

## 0. 身份卡

- **题录**：Dominique Sommers*, Natalia Sidorova, Boudewijn van Dongen. "A ground truth approach for assessing process mining techniques". *Process Science* (2025) 2:1, 栏目 RESEARCH, Open Access, DOI 10.1007/s44311-025-00006-8 [PDF p.1]。
- **作者单位**：三人同属 Mathematics and Computer Science, Eindhoven University of Technology（TU/e），通讯 d.sommers@tue.nl [PDF p.1]。
- **venue**：Process Science（Springer）。卷号 "2:1" 说明 2025 年为第 2 卷，即创刊于 2024 年 [推断，依据 PDF p.1 卷期号]；期刊等级 `[需验证]`。van Dongen 为该刊 co-Editor in Chief [PDF p.28]。
- **前身与扩展**："This paper is an extension of work originally presented in ICPM (Sommers et al. 2024)"，扩展点：由单日志推广为"从所选模式与仿真参数的每个子集生成一组日志"；给出三个数据集实例；补充工具支持现状；用例子展开模式与模型变换；讨论仿真参数影响 [PDF p.3]。
- **OA 许可**：CC BY 4.0（"Creative Commons Attribution 4.0 International License"，首页页脚，非末页）[PDF p.1]；末页只有 Publisher's Note [PDF p.30]。
- **时间线**：Received 11 December 2024；Accepted 18 February 2025 [PDF p.28]。
- **基金**：NWO 项目 "Certification of production process quality through Artificial Intelligence (CERTIF-AI)"，项目号 17998 [PDF p.28]。
- **数据可得性声明**："No datasets were generated or analysed during the current study." [PDF p.28] —— 与 p.18 "All models and corresponding generated logs with the applied patterns are available at gitlab.com/dominiquesommers/mira/-/tree/main/mira/simulation" `[⚠️矛盾]`（疑似出版社模板句未改，[推断]）。
- **利益冲突声明（原样抄）**[PDF p.28]："The authors of this manuscript were invited by the program chairs of the International Conference on Process Mining 2024 to submit an extended version of their conference paper to be considered for publication in the Process Science journal. The submitted manuscript went through a regular review process. Since Boudewijn van Dongen is co-Editor in Chief for Process Science, he was not involved in the decision to invite this paper, nor in the journal's review process, nor did he have any influence on the decisions related to this manuscript." 首页边栏预告："Competing interests for Boudewijn van Dongen are declared at the end of the manuscript." [PDF p.1]
- **作者贡献**："All authors contributed equally to writing and reviewing the manuscript." [PDF p.28]
- **sha256**：`59cf748494a4f5f9393c0e9082a7cbb368e24148a5de6708ba9aa4e305db6603`（任务书给定，本篇未重算）；来源 `[需核实]`。
- **PDF 页 ↔ 章节映射（核对后修正版）**：Abstract + Introduction p.1–3；Related work p.3–5（"Assessment using real-life logs with unknown model" p.3–4；"Assessment with synthetic data" p.4–5；Fig. 1 p.5）；**"Requirements to synthetic process data" p.5–8**（Fig. 2 + Table 1 p.6；"Characteristics of real-life processes and their data" p.6–7；"The need for ground truth" p.7；RQ p.8）；"Generating process data with ground truth" p.8–15（Framework design p.8–9；Usage in assessments p.9；Deviation patterns p.10–13，Table 2 p.10、Fig. 3 p.11；Model transformations p.13–14，式(1) p.13、Fig. 4 p.13、Fig. 5 p.14）；Simulation p.15–16（式(2) p.15）；Tool support p.16–17；"Putting the framework into practice" p.17–23（Fig. 6 p.17；Package delivery p.18–19，Fig. 7 p.18、Fig. 8 p.20；Energy contract p.19–22，Fig. 9 p.20；Real-life assembly p.22–23，Fig. 10 p.22）；"Evaluating the interpretability of (Relaxed) multi-object alignments" p.23–27（Experimental setup p.24；Results and discussion p.24–27）；Conclusion p.27–28；声明 p.28；References p.29–30。
  - 对任务书定位表的修正：任务书写 "Related work p.3–8"，实际 Related work 止于 p.5，p.5–8 是独立一节 "Requirements to synthetic process data"（Fig. 2/Table 1 属于这一节）；"Deviation patterns p.10–15" 实为 p.10–13，p.13–14 是 "Model transformations"；"Simulation p.15–24" 实为 p.15–16，其后 p.16–17 Tool support、p.17–23 实践三例。Fig. 11/Table 3/Fig. 12 的页码（p.25/26/27）本篇未逐页核对 `[需验证]`。

## 1. Task：解决什么问题？形式化

**非形式陈述**：用真实数据评估过程挖掘技术时，缺少 ground truth、系统行为里有非本质离群点、日志里有记录错误，评估被"妥协"[PDF p.1 摘要]。作者在 NWO CERTIF-AI 项目里对合作公司 Omron 的制造过程做对齐（alignment）时，发现每一处偏差都可以有多种解释（记录时序问题、操作员多任务、临时换岗），验证需要干系人大量人工检查，规模化验证"practically impossible" [PDF p.2]。真正需要的是一个"omniscient stakeholder / oracle"，能说出某偏差是否为真偏差、解释是否正确 [PDF p.2]。

**研究问题（原文 RQ）**："How can we set up an experiment with realistically noisy process data where the ground truth is known to allow for a complete assessment?" [PDF p.8]

**三分法的精确定义（桥线核心）**：
- **系统行为 vs 记录行为**：Fig. 1 标题把对象记为"underlying process S"、模型 M、日志 L [PDF p.5]；摘要区分 "non-essential outliers in system behavior" 与 "recording errors in event logs" [PDF p.1]。
- **记录错误（recording error）**："records misrepresenting the actually executed behavior of the process" [PDF p.6]。按 Bose et al. (2013) 分四类：(1) missing, (2) incorrect, (3) imprecise, (4) irrelevant；每类可作用于日志的不同元素（事件、事件属性、属性与事件的关系、事件之间的关系），Table 1 逐格给出 RI 记号（行 = Missing/Incorrect/Imprecise/Irrelevant data，列 = Case / Event / Belongs to / C_attribute / Position / Activity name / Timestamp / Resource / E_attribute）[PDF p.6]。来源："faulty logging mechanisms, either automatic or manual, with unsynchronized clocks, too coarse timestamps, data corruption, and filtering and aggregation methods" [PDF p.6]。本文例子聚焦 missing 与 incorrect 两类 [PDF p.6]。
- **行为离群/行为偏差（behavioral outlier / deviation）**："behavior that deviates from the main behavior of the process"；"main behavior" 的解释依赖挖掘任务：expected behavior、"happy flow"、或 frequent behavior [PDF p.7]。原因举例：人不遵守指南、遇到模型未考虑的罕见情形 [PDF p.7]。行为偏差同样被当作 pattern；落入日志后"boil down to similar issues as the recording errors" [PDF p.7]。
- **ground truth**：由 M0、M^S、M^L、L′ 以及它们之间的链接共同构成，"including behavioral characteristics of the process and recording characteristics of the event log as well as its completeness with respect to the process (M^S) and the model (M0)" [PDF p.8]。其中：M0 = base model，表示过程的 expected behavior；M^S = 过程的 true model，捕获行为偏差；M^L = 在 M^S 上再模仿 faulty logging mechanisms 的模型 [PDF p.8]。仿真 M0 得 "exemplary" 日志；仿真 M^S 得 "clean" 日志（"real" behavior）；仿真 M^L 得 L′（真实行为 + 真实感记录错误）——**L′ 是框架的目标产物** [PDF p.8]。
- **信息分层**：交给被评估技术的只有事件的部分信息（如 transition labels）；其余信息构成 ground truth，用于算指标与做定性洞察 [PDF p.9]。

**输入 / 输出 / 目标（形式化重构，符号按原文）**：
- 输入：base model M0；偏差模式集 Π = Π^S ∪ Π^L（Π^S 行为偏差模式，Π^L 记录错误模式）；每个模式的映射函数 h（把模式中的元素映到 M 的元素，指明偏差发生位置）[PDF p.8]。
- 变换：模型变换函数 Ψ(M, π, h)，序列应用：M0 → Ψ(M0, π1, h1) → … → M^S；再从 M^S 应用 Π^L 得 M^L [PDF p.8–9]。
- 输出：仿真 M^L 得 L′，"encoding the complete information about the transitions that generated events"；事件可回链到 M^L 的 transition firing，再回链到 M^S 与 M0 的变迁，或被标为对应偏差 [PDF p.8–9]。
- 评估通式：评估者为其 PM 问题定义 ground truth 函数 gt 与距离函数 d，质量 = d( f(M0, L′), gt^f(M0, L′, M^S, M^L) ) [PDF p.9]（无编号公式）。
- 两个实例化：过程发现 PD 的目标模型 = M0 加上子集 Π^{S′} ⊆ Π^S 的行为偏差（"频繁的保留、不频繁的与全部记录错误忽略"），相似度可用 Dijkman et al. 2011 的模型相似度 [PDF p.9]；一致性检查 CC 的 ground truth = 最优对齐：M0 原始变迁的触发对应同步移动，属于偏差模式的变迁对应 log move / model move，相似度用序列或图编辑距离 [PDF p.9]。
- 需求边界：合成数据需 (1) 不同特征的模型、(2) 执行与记录两层的偏差变化且与真实偏差模式一致、(3) ground truth 作为目标函数；**本文只处理 (2)(3)**，假定模型已由 PTALG 等工具或人工给出 [PDF p.5]。

**立足点（未被原文明说，[推断]）**：把"噪声"从日志层搬到模型层的收益是——每一个偏差都对应一个具名的模型元素（created transition/place），因此"哪个事件是偏差、属于哪类"不需要事后标注，而是仿真的副产品。整篇论文 = 这一个搬家动作的形式化与工程化。

## 2. Challenge

原文对两条现有路线各自的指控 [PDF p.3–5, p.7]：

1. **真实日志评估**：需要数据所有者深度参与（UWV 案例 Dees et al. 2017 为例）；专有数据不能共享，可重复性/再现性"out of reach" [PDF p.3]。BPIC 2011–2020 与 CCC 2019/2020 虽公开且"realistically noisy"，但底层过程的 ground truth 缺失，只有靠人工分析与专家咨询得到的有限信息 [PDF p.3–4]；即便有规范模型（Munoz-Gama et al. 2019），也无法判定偏差是否被正确暴露和解释，因为偏差既可能是行为偏差也可能是记录错误，算法识别的正确性无法核验 [PDF p.4]。Käppel et al. 2021 的删迹法会带来资源负载、案例交互等副作用，"less realistic"，已经在向合成数据靠拢 [PDF p.4]。
2. **现有合成日志工具（直接往日志注噪）**：PTALG 在仿真后直接对 trace 注入 Günther (2009) 定义的噪声——missing head / missing body (episode) / missing tail / order perturbation / additional activities [PDF p.4]；PURPLE 也限于同样的简单日志操作、只在仿真后注入，且其输入模型代表"actual behavior"（离群行为已混入模型，不可区分）[PDF p.4]；AIR-BAGEL 用概率机制注入带根因的伪真实异常并打标签，面向日志清洗评估 [PDF p.4–5]。Fig. 1a 抽象：M0 仿真出 clean 日志 L，再由日志操作函数 ε_L 注噪 [PDF p.5]。两点不足：(1) 没给出"real system"的模型——base model 要么不含行为偏差，要么含了但与正常行为不可区分；(2) 日志操作与过程行为无关，**模型与日志之间的链接丢失** [PDF p.7]。
3. **为什么必须有 ground truth**：用一致性指标评估发现算法假定日志无记录错误，但记录错误与行为离群的原因有歧义、可能无法区分；理想上记录错误应被完全过滤，而（部分）行为离群应进入发现的模型——验证需要能做这个区分 [PDF p.7]。作者称决策挖掘、模型/日志修复、瓶颈检测、预测/规范性监控同样受困 [PDF p.7]。

**真/套话判断 [推断]**：挑战 1 是真挑战（Omron 案例是第一手经历 [PDF p.2]）；挑战 2 中"链接丢失"是真痛点，但 p.19 作者自己承认"用现有方法构造相同或相似日志并非本质上不可行"（"not inherently infeasible"），本框架的优势被降格为"methodological and structured approach" [PDF p.19]——即挑战 2 对包裹投递数据集而言部分是套话；真正现有方法做不到的是重复标签活动上的定向注噪（能源合同过程，p.22）与模式间行为互相影响（装配过程，p.23）。

## 3. Insight & Novelty

### 3.1 Inspiration 来源
- **I-A（问题源）**：Rozinat et al. 2008 的评估框架需求——用户应能影响过程/日志特征、生成"forbidden"场景 [PDF p.1–2]；NWO CERTIF-AI + Omron 的对齐验证困境 [PDF p.2]。
- **I-B（分类学）**：Bose et al. 2013 的日志质量问题四分类（Table 1）[PDF p.6]；Russell et al. 2006 的工作流建模模式（行为偏差 = 模式的违反）[PDF p.6, p.10]；Basmer et al. 2024 把质量问题扩展到对象中心数据，"essence is the same" [PDF p.6]。
- **I-C（形式底座）**：t-PNID（van der Werf et al. 2022），多对象交互建模 [PDF p.10–11]；Petri 网变换（Ehrig and Padberg 2003）作为 Ψ 的定义来源 [PDF p.13]；SPN（Leemans et al. 2021）与 TPN（Razouk & Phelps 1983; Zuberek 1980）供仿真扩展 [PDF p.15]；RC ν-nets、OPIDs、OC nets、Synchronizing proclets 作为可扩展形式 [PDF p.16]。
- **I-D（标签思想）**：AIR-BAGEL 的"带异常类型标签的日志" [PDF p.5]——本文把标签前移到变迁与事件记录上 [PDF p.2]。

### 3.2 Insight 逐条
- **Insight 1（对应 I-A/I-D）**：噪声应建模在仿真模型里而不是注入日志——"realistic noise is incorporated into a simulation model with the help of model transformations"，变迁与事件记录都带偏差类型 tag，于是 oracle 可实现 [PDF p.2]。方面：链接保持。
- **Insight 2（对应 I-B）**：两段式变换 M0 → M^S → M^L 把"期望行为 / 真实行为 / 记录行为"三层分离，三个模型 + 日志 + 链接 = ground truth [PDF p.8]。方面：三分法可操作化。
- **Insight 3（对应 I-B）**：记录错误与行为偏差落进日志后表现相同，只是原因不同（RI^e_mi 缺失事件 vs 跳过活动），所以用同一套分类对齐两列并画出 counterpart 链接 [PDF p.7, p.10]。方面：分类学统一。
- **Insight 4（对应 I-C）**：所有模式设计为行为"additive"——只加不减 base model 的行为，因此多个模式互不干扰、created 元素名字互异，这是能为不同 PM 任务自由定义 gt 函数的"necessary property" [PDF p.13]。方面：可组合性。
- **Insight 5（对应 I-C）**：有些偏差（批量记录 RI^p_in、长时长 BI11）不改变工作流视角的行为，只改时序/随机性——可直接建模在权重与时长的采样分布及其条件变量（时间、标识）上 [PDF p.15–16]。方面：随机层偏差。

### 3.3 Novelty 清单
- N1（框架）：Fig. 1b 的 M0/M^S/M^L/L′ 四件套 + 链接式 ground truth [PDF p.5, p.8]。
- N2（模式库）：Table 2 的 7 个记录错误模式 + 11 个行为偏差模式，附 t-PNID 蓝图（Fig. 3）[PDF p.10–13]。
- N3（变换）：Ψ(M, π, h) = M ∪ h(π)（式 1）[PDF p.13]。
- N4（仿真）：加权变迁的分类分布采样（式 2）+ 变迁/弧上的时长 + 以标识、时间为条件的参数 [PDF p.15]。
- N5（扩展，相对 ICPM 2024 新增）：一个 M0 → n·m·k 份日志（Fig. 6）[PDF p.3, p.17]。
- N6（实例）：三个数据集（包裹投递、能源合同、Omron 装配）[PDF p.17–23]；N7（工具）：Trident GUI 版 + mira 脚本版 [PDF p.16–17]。

### 3.4 Novelty 严格三段式
- **N1 框架**：解决 §2 挑战 2 的"链接丢失"与挑战 3 的"无法区分"；受 Insight 1+2 启发；设计 = 两段式模型变换后再仿真，事件回链到变迁 [PDF p.8–9]。
- **N2 模式库**：解决"注噪只覆盖 Günther 五种简单操作"（§2 挑战 2）；受 Insight 3 启发；设计 = 每个模式是带通配符 ⟨∗⟩ 的抽象模型 M̄，蓝图给出 matched（蓝）与 created（绿）元素 [PDF p.10–11]。
- **N3 变换 Ψ**：解决"模式如何落到任意 base model"；受 I-C（Ehrig & Padberg）启发；设计 = 单射映射 h 把通配符映到 M 的元素，Ψ 取并 [PDF p.13]。
- **N4/N5 仿真与扩展**：解决"偏差频率与随机层偏差的可控性"与"单一日志代表性不足"（§0 前身扩展点 [PDF p.3]）；受 Insight 5 启发；设计 = 式 2 的权重采样、时长规格、条件变量，以及模式子集 × 仿真参数组合 [PDF p.15–17]。

## 4. 方法全恢复

### 4.0 数据流总图（文字版）
- **Fig. 1a（现有路线）**：M0 —仿真→ clean 日志 L —ε_L 日志操作→ 带噪日志 [PDF p.5]。
- **Fig. 1b（本文）**：M0 —Ψ(·, π ∈ Π^S, h) 序列→ M^S —Ψ(·, π ∈ Π^L, h) 序列→ M^L —离散事件仿真→ L′；M0/M^S/M^L/L′ 之间的链接保留 [PDF p.5, p.8–9]。
- **Fig. 6（扩展）**：一个 M0 → 行为偏差模式的任意组合得 n 个 M^S → 每个 M^S 上记录错误模式的组合得 n·m 个 M^L → k 组仿真参数得 n·m·k 份日志，各自在行为偏差、记录错误、随机性上特征不同 [PDF p.17]。

### 4.1 "Generating process data with ground truth" 的形式化
原文**没有编号的 Definition**，只有式 (1)(2) 与一个无编号评估通式；下面按原文文字重构并自编编号 D1–D6（非原文编号）。
- D1（模型三元）：M0 base model（expected behavior）；M^S true model（含行为偏差）；M^L（M^S + 模仿错误记录机制）[PDF p.8]。M0 可以是现有过程、人工设计的假想过程、或模型生成工具的产物；"merely serves as a base process that does not represent the 'real' process execution"，可作 CC 评估的规范模型或 PD 评估的"typical flow"模型 [PDF p.8]。
- D2（模式集）：Π = Π^S ∪ Π^L；偏差建模为模板 [PDF p.8]。
- D3（偏差模式）：一个模式 = 行为描述 + 抽象过程模型片段；形式上是抽象过程模型 M̄，"describing deviating behavior in relation to some process behavior"，其中某些元素是通配符 ⟨∗⟩ [PDF p.10]。
- D4（变换）：Ψ 取 (M, π, h)，h 把 π 的元素映到 M 的元素以指明偏差位置；序列应用得 M^S、M^L [PDF p.8–9]；具体式见 4.5 式 (1)。
- D5（日志）：L′ = M^L 的仿真，编码"生成事件的变迁的完整信息" [PDF p.9]；被评估技术只拿到部分信息 [PDF p.9]。
- D6（评估）：gt^f 与 d 由评估者定义，质量 = d(f(M0, L′), gt^f(M0, L′, M^S, M^L)) [PDF p.9]。
- 附：ground truth 的四项内容——过程的行为特征、日志的记录特征、日志相对 M^S 的完备性、相对 M0 的完备性 [PDF p.8]。

### 4.2 Deviation patterns
**Table 2 逐格抄录**[PDF p.10]（两列之间有彩色连线表示 counterpart，连线具体对应关系图上不可逐条辨读 `[需验证]`；原文文字给出的对应：RI^o_in ↔ switching correlation、multitasking 等 [PDF p.10]；RI^e_mi ↔ 跳过活动 [PDF p.10]）：

| 记录错误模式（左列，7 个） | 记号 | 行为偏差模式（右列，11 个） | 记号 |
|---|---|---|---|
| Missing event | RI^e_mi | Switching correlation | BI1 |
| Incorrect event | RI^e_in | Multitasking | BI2 |
| Missing object | RI^o_mi | Skipping activity | BI3 |
| Incorrect object | RI^o_in | Neglecting object(s) | BI4 |
| Missing position | RI^p_mi | Overtaking in queue | BI5 |
| Incorrect position | RI^p_in | In/decreasing capacity | BI6 |
| Incorrect activity name | RI^a_in | Switching roles | BI7 |
| | | Same resource on 4-eyes principle | BI8 |
| | | Different resource on resource memory | BI9 |
| | | Ignoring batching | BI10 |
| | | Long duration | BI11 |

记号约定：RI 上标 = 元素（e 事件、o 对象、p 位置、a 活动名），下标 = 问题类别（mi 缺失、in 错误）[PDF p.6, p.10]。左列来自 Table 1 中为记录错误特化的子集，右列来自 Russell et al. 2006 建模模式的违反 [PDF p.10]。
- `[⚠️矛盾]` p.10 正文写"Skipping an activity during the execution of a process (BI1)"，而 Table 2 中跳过活动是 BI3、BI1 是 switching correlation [PDF p.10]。
- 建模形式：t-PNID——变迁（矩形）、带类型库所（彩色圆）、带标签弧；token 携带（多个）标识符表示对象名；变迁触发 = 一个事件，涉及对象 = 消耗/产生 token 所代表的对象 [PDF p.10–11]。方法"conceptually defined, independent of the modeling formalism"，只要模式与 base model 同形式 [PDF p.13]。

**Fig. 3 蓝图文字复原**（蓝 = matched，绿 = created）[PDF p.11–13]：
- **RI^o_mi 缺失对象（左上）**：匹配变迁 t 及其前集 •⟨t⟩、后集 ⟨t⟩•；假定库所类型与待缺失对象集 O 的类型一致，新建变迁 t_missing O，活动名同 t 但不涉及 O；另建两个静默变迁 τ_•⟨t⟩-⟨O⟩ 与 τ_⟨t⟩•-⟨O⟩，把 O 对应库所的 token 从 •⟨t⟩ 旁路到 ⟨t⟩•↾⟨O⟩ 再到 ⟨t⟩•；其它库所（•⟨t⟩↾⟨O⟩^C、⟨t⟩•↾⟨O⟩^C，O^C 为补集）的 token 交给 t_missing O [PDF p.11]。
- **RI^p_in 错误位置（左中，批量记录）**：作用于 base model 的批处理结构——t1 启动一批对象的处理，t2 逐个处理；新建 t1_batch log、t2_batch log，活动名同 t1、t2，行为相同，但时序规格不同：仿真中 t1_batch log 耗时等于处理整批，t2_batch log 耗时可忽略（原文此处两次写 "t1 batch log" `[⚠️存疑]`，按语义第二个应为 t2 [推断]），从而同一活动被记录在错误位置；对 t1 后集与 t2 前集的交集与差集分别处理以正确传 token [PDF p.11–12]。
- **RI^a_in 错误活动名（左下）**：为匹配变迁 t 建复制变迁 ⟨t′⟩_incorrect a-⟨t⟩，继承前后集，活动名改为 ⟨t′⟩ [PDF p.12]。
- **BI1 改变关联（右上）**：匹配库所 p（双类型，其一为资源类型，与 p_r 同型）与 p_r；新建静默变迁 τ_change correlation-p-p_r，通过弧标签从 p 消耗关联 token、从 p_r 消耗资源 token，把关联改到新资源；ICPM 2024 版本是交换两个已有关联 token 的资源 [PDF p.12]。
- **BI5 FIFO 队列插队（右中上）**：静默变迁 τ_overtake 交换匹配库所 p_q1、p_qw 中两个对象与其队列位置对象的关联；新建库所 p_q1 overtake 防止仿真中无限互相插队 [PDF p.12]。
- **BI6 容量增减（右中下）**：τ_⟨p_c⟩− 从匹配库所 p_c 减一个容量并把信息存入新建库所 ⟨p_c⟩−，可由 τ_⟨p_c⟩− undo 撤销；τ_⟨p_c⟩+ 复制 p_c 中一个 token，τ_⟨p_c⟩+ undo 消耗复制品 [PDF p.12]。
- **BI7 换岗（右下）**：匹配两个角色库所 p_r1、p_r2；τ_switch role-r1-r2 把资源 token 从角色 r1 移到 r2，信息存入 p_r1-r2，由 τ_switch role back r1-r2 撤销；弧标签中的 ν 变量合成新标识符引用原对象，保证不同类型对象不重叠 [PDF p.12–13]。
- 另四个模式（RI^e_mi、RI^e_in、BI3、BI2 与交换式 BI1）见 ICPM 2024 版 [PDF p.13]。

### 4.3 模型变换（M → M′ → 变换结果）
- **式 (1)**：Ψ(M, π, h) = M ∪ h(π)，h 是从抽象片段 π 到 M 空间中具体片段的 morphism（单射，matched 元素指向 M 中元素），Ψ(M, π, h) 额外含 π 的 created 组件 [PDF p.13]。
- **Fig. 4**：Fig. 2 稍作修改后的 t-PNID 实现 M′ 的片段；初始状态用加粗轮廓库所里的对象名多重集表示（[(we1),(we2)] 于 p_we 仓库员工，[(c1),(c2)] 于 p_c 快递员）；为套用缺失对象模式，新增"重件到家投递"活动，需两名快递员 [PDF p.13–14]。
- **Fig. 5 四步变换**[PDF p.14]：(i) BI5 插队，映射 {⟨p_q1⟩ ↦ p̄_q2, ⟨p_q2⟩ ↦ p̄_q3}，建静默变迁交换两个对象与队列位置的关联（`[⚠️存疑]` 蓝图用 p_q1/p_qw，此处用 p_q1/p_q2）；(ii) 改变关联，映射 {⟨p⟩ ↦ p2, ⟨p_r⟩ ↦ p_we}，可把装车员工改为与拣货不同的员工——原文此处标为 "BI2"，按 Table 2 应为 BI1 `[⚠️矛盾]`；(iii) 换岗，映射 {⟨p_r1⟩ ↦ p_we, ⟨p_r2⟩ ↦ p_c}，仓库员工临时充当快递员——原文标 "BI6"，按 Table 2 应为 BI7 `[⚠️矛盾]`；(iv) RI^o_mi 应用于重件投递：两名快递员都被占用，但创建的重件投递变迁"不知道"第二名快递员，其经新建库所 p_c′ 旁路 [PDF p.14]。
- **映射约束**：通配符映射有角色限制（库所/变迁在网中的角色须与模式要求匹配），可在变换里检查或由用户遵守；例：多任务模式要求 p1、p2 分别映到某资源角色的 busy 库所与 idle 库所 [PDF p.14]。RC ν-nets 因建模限制严格，约束"can be easily checked" [PDF p.16]。

### 4.4 Simulation 框架与 Fig. 6 参数
- **定位**：L′ 由 M^L 的离散事件仿真得到；仿真模块可替换——最简为 play out（变迁被使能或按到达/预定计划触发）[PDF p.15]。
- **概率**：权重 w: T → R≥0，使能触发集 T^e_μ 上按分类分布采样，式 (2) 见 4.5 [PDF p.15]。
- **时长**：token 产生延迟，规格挂在变迁或（更细）出弧上；延迟期间变迁不消耗 token；规格可为常数/函数/分布，采样值非负；例：拣货到装车 +N(15, 6)（均值 15、方差 6 分钟，挂在 'pick package' → p2 的弧上）[PDF p.15]。
- **条件参数**：权重与时长可加条件变量——当前标识、当前仿真时间 η ∈ T、其它数据属性（Holliday & Vernon 1987）；w: T × T → R≥0 可临时禁用变迁，用于控制偏差行为的概率与频率 [PDF p.15]。
- **随机层偏差**：RI^p_in 批量记录与 BI11 长时长——工作流不变，只有时序刻画偏差 [PDF p.16]。
- **Trident 简单仿真器参数**：从初始到终止标识 play out；可设变迁触发次数上限（应对无限行为）；概率 = 使能后采样等待时间，到点不再使能则取消；不考虑采样时间以外的依赖 [PDF p.17]。
- **高级实现参数**：变迁触发采样 + token 产生时长采样；自发对象的到达、计划对象的启停计划由采样分布定义；条件变量"当前仿真时间"可让偏差概率随时间变化 [PDF p.17]。
- **Fig. 6 的三个乘子**：n = 行为偏差模式组合数（→ n 个 M^S）；m = 记录错误模式组合数（→ n·m 个 M^L）；k = 仿真参数组数（→ n·m·k 份日志）[PDF p.17]。
- **三个实例的取值**[PDF p.19, p.21, p.23]：包裹投递——模式隔离，6 个单偏差 M^S + 1 个无偏差 M^S_∅，6 个记录错误只加在 M^S_∅ 上，共 12 个 M^L，单一组仿真参数、每份日志两个包裹（n·m·k 口径为 12×1）；能源合同——5 个行为 + 4 个记录模式全部合进单一 M^L，参数使问题频率低、BI11 时长分布偏离正常，大量申请靠大数定律逼近期望频率，并提示 PURPLE 式引导仿真可补充频率控制；装配——3 个行为 + 2 个记录模式，"standard simulation parameters"，建议用当前状态提高换岗概率、用历史数据校准随机信息。

### 4.5 公式/定义全量（编号对齐原文）
- **式 (1)** [PDF p.13]：Ψ(M, π, h) = M ∪ h(π)。
- **式 (2)** [PDF p.15]：p(t^s_μ = t_μ | w) = w(t) / Σ_{t′_μ ∈ T^e_μ} w(t′)，其中 T^e_μ 为使能的变迁触发集（含 binding/mode），w: T → R≥0。
- **评估通式（无编号）** [PDF p.9]：d( f(M0, L′), gt^f(M0, L′, M^S, M^L) )。
- **变换序列（无编号）** [PDF p.9]：M0 → Ψ(M0, π1, h1) → … → M^S；M^S → … → M^L。
- **PD 目标（无编号）** [PDF p.9]：由 M0 与 Π^{S′} ⊆ Π^S 定义；相似度 sim(PD(L′), gt^PD(M0, M^S, M^L, L′))。
- **CC 目标（无编号）** [PDF p.9]：sim(CC(M0, L′), gt^CC(M0, M^S, M^L, L′))，gt^CC = 最优对齐。
- **时长规格示例** [PDF p.15]：+N(15, 6)。
- **偏差模式定义（文字定义，无编号）** [PDF p.10]：抽象过程模型 M̄ + 通配符 ⟨∗⟩。
- 证明：原文无定理/证明；additivity 只有文字论证（"modeled in a way that the model transformation is additive in behavior"）[PDF p.13] `[篇幅限制]`。
