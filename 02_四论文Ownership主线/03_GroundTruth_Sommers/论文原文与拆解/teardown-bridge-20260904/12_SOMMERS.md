Author: Fable 5 main window (merge of two subagent parts; TASK-20260904-001)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# 12 · Sommers（Process Science 2025）第一性原理全拆 —— 桥线 T1 必要辅助篇（合并件）

> 本文件 = `12_SOMMERS_p1.md`（§0–§4，子代理 A3p1，03:12）+ `12_SOMMERS_p2.md`（§5–§9，子代理 A3p2 尝试 3，05:08）原样拼接；两份 part 文件保留不动，判定以 part 文件与 PDF 原件为准。
> 主窗交叉核对块插在 §4 与 §5 之间：记录 p2 对 p1 三条 open 的兼核结论，以及独立视角 `12b_SOMMERS_kg_critique.md` 与本篇一致/不一致之处。

---

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

---

## 主窗交叉核对块（A3p1 ↔ A3p2 ↔ 12b，2026-09-04 05:1x）

| # | p1 留下的 open | p2 §9 兼核结论 | 12b 独立视角 | 主窗判定 |
|---|---|---|---|---|
| 1 | BI 编号在正文 / Table 2 / 图之间漂移 [PDF p.10] `[⚠️矛盾]` | 局部陈旧标签：p.10 一处 + p.14 两处；p.18/21/23/25/27、Table 3、Fig. 11 全部与 Table 2 一致 → 非系统性错位 [推断：ICPM 2024 版编号残留，需验证] | 独立发现同一处（p.10 BI1 vs BI3）并另指 p.14 两处互斥编号；建议以 Table 2 为权威 | 两视角一致。引用本篇 BI 编号时**以 Table 2 [PDF p.10] 为准**，正文编号不可直接引用 |
| 2 | Table 2 连线不可辨 | 按任务书未再试 | 未涉及 | 保持 open；需人工看图 |
| 3 | p.28 "No datasets were generated or analysed" vs p.18 gitlab 链接 `[⚠️矛盾]` | Declarations 段无其他说法；同页结论段自证"creating datasets" → 矛盾成立 | 独立发现同一矛盾；无网络未核仓库现状 | 矛盾成立（三处页码互证）。仓库是否可达待有网时核 `[需验证]` |
| 4 | — | — | 新增：摘要 "both quantitatively and qualitatively" [PDF p.1] vs 结论 "we focused on the qualitative aspect" [PDF p.28] `[⚠️矛盾]` | p2 §5.5 亦指出"无数值型质量分（d 未实例化）"[PDF p.9, p.19]，两视角从不同入口指向同一缺口：框架定义的距离函数 d 在实验里没有实例化 |
| 5 | — | Table 3 为单次判读 `[表读数·单次判读·需验证]`；Fig. 12 横轴标签不可辨，按 Table 3 行序假定 [PDF p.26–27] | Fig. 12 第 6 个横轴标签疑与 Table 3 第 6 行不同 [PDF p.27] `[图读数不清]` | 两视角都只做了单次判读且互有出入 → Table 3 / Fig. 12 的格内数字**一律不得引用**，只引结构与正文数字 |


> 承接 `12_SOMMERS_p1.md`（§0–§4），本篇只写 §5 起。主输入：`research/papers_lu/Sommers-2025-ProcessScience.pdf`（页眉 "Page N of 30"，印刷页 = PDF 物理页）；`_launch/pdftxt/SOMMERS.txt` 只作定位。
> 读页记录：PDF p.25–27 各 `Read` 一次（Fig. 11 / Table 3 / Fig. 12）；p.18–19、p.23–24、p.28–30 以文本层为准（纯正文，文本层完整）；Table 3 所在 p.26 文本层只剩图题（表体为矢量图，抽不出格），按"读页纪律"记结构 + 单次视觉判读，未做第二次读页。
> 实验节位置：p.23 末 "Evaluating the interpretability of (Relaxed) multi-object alignments" → p.24 "Experimental setup" + "Results and discussion" 起 → p.25 Fig. 11 → p.26 Table 3（横排整页）→ p.27 Fig. 12 + AQ 总结 → p.27–28 Conclusion → p.28 声明 → p.29–30 参考文献。

---

## 5. 实验协议与结果批判

### 5.1 协议

- **定位**：实验不是"评估本框架"，而是"用本框架的 ground truth 去评估三种对齐技术"，作者称之为 "Usage in assessments" 一节（p.9）的具体化 [PDF p.23]。因此原文没有针对框架本身的指标；框架的"效果"只能从"能否产出可判读的评估表"间接看。
- **评估问题（AQ）**三条 [PDF p.24]：AQ1 行为离群与记录错误是否被正确检出；AQ2 生成的对齐多大程度反映 ground truth 解释；AQ3 两类偏差如何影响对齐方法的计算时间。
- **数据集**：只用三个实例中的第一个——包裹投递合成过程（p.18–19）。6 个行为偏差模式（BI5 插队、BI7 换岗、BI10 忽略批处理、BI3 跳过按铃、BI9 投到不同 depot、BI2 快递员多任务）各自单独作用于 M0 得 6 个 M^S；6 个记录错误模式（RI^e_in(1) 家投登记成 depot 投递、RI^e_in(2) 反向、RI^e_mi 装车事件缺失、RI^o_mi 装车时 van 对象缺失、RI^o_in 按铃时快递员对象错误、RI^p_mi depot 投递/取件位置缺失）只作用于无行为偏差的 M^S_∅；共 12 个 M^L、12 份日志，**每份日志只含一个问题**、只处理两个包裹、同一辆 van [PDF p.18–19, p.24]。仿真参数：单一组，选到"保证模式在两个包裹的仿真中被触发" [PDF p.19]。
- **ground truth 生成方式**："The ground truth oracle provides explanations by knowledge of which transitions have fired in the simulation to produce the events in the logs" [PDF p.24]——即 §4 的事件→变迁回链；偏差在模型中的位置见 Fig. 7（p.18，本篇未读图）[PDF p.24]。
- **被评估对象**：三种对齐方法，输入均为 M0 + 日志 [PDF p.24]：(1) per-object γ°，逐对象孤立对齐、忽略对象交互（Carmona et al. 2018）；(2) systemic γ，整份日志对整模型对齐、考虑违规（Sommers et al. 2022）；(3) relaxed systemic γ̃，允许放松日志与模型两侧的对象交互（Sommers et al. 2024）。三者中两种是作者自己的方法，第三种引自 van Dongen 合著教材 [PDF p.24, p.29–30]——**自评自家技术**，这是读结果时必须带的前提。
- **输入预处理**：每种方法吃"偏序集形式的日志 + 规范模型"；送入对齐的日志是仿真日志的**投影**，"with some types of deviating events (like skipped steps or missing events) removed from it" [PDF p.24]——与 p.9 "技术只拿部分信息"一致；即 M^L 里 created 变迁产生的事件在投影时被抹掉，日志才像真日志。
- **输出与"指标"**：对齐由同步移动/日志移动/模型移动构成 [PDF p.24]。AQ1/AQ2 的"指标" = 每种方法暴露的"负责对象集合"与"受影响对象集合（下标）"对照 GT（Table 3）+ 人工解释栏 [PDF p.24, p.26]；AQ3 = 计算时长（Fig. 12，纵轴 Duration (s)，对数刻度）[PDF p.27]。**p.9 定义的距离函数 d 在实验中从未实例化**——没有任何数值型质量分数 [PDF p.9 vs p.24–27]。
- **实现/硬件**：全文未报告 CPU/内存/运行环境/重复次数/方差（文本层 grep "GHz/RAM/CPU/Intel/repeated/average/variance" 在实验节零命中；"Python" 只出现在 p.16 工具节）[PDF p.16, p.24–27] `[需验证：仅凭文本层缺失推断]`。对齐工具实现未指名。

### 5.2 Table 3 结构 + 可读数字

- **图题**（文本层可抽）："Experiment results showing the objects responsible for the deviation and those affected by it (in subscript) for each pattern, for the ground truth (GT) and detected by alignment methods: per-object (γ°), systemic (γ), and relaxed systematic (γ̃)" [PDF p.26]。注意图题写 "relaxed **systematic**"，正文一律 "relaxed **systemic**" [PDF p.24, p.26] `[⚠️矛盾·用词]`。
- **结构**：整页横排。列 = Dev. | "Deviating object(s)" 分组下四列 GT / γ° / γ / γ̃ | Interpretation of the results。行 = 12 个模式，顺序：RI^e_in(1)、RI^e_in(2)、RI^e_mi、RI^o_mi、RI^o_in、RI^p_mi、BI5、BI7、BI10、BI3、BI9、BI2（与 p.18–19 的列举顺序一致）[PDF p.26]。格内 = 对象集合，下标括号 = 受影响对象 [PDF p.24]。对象缩写 p/c/v/d/q = package/courier/van/depot/queue（位置）`[推断，依据 p.18–19 描述]`。
- **正文引用本表给出的事实** [PDF p.24–25]：(a) 记录错误 6 个"each deviation was detected by each method"，但对象层偏差（RI^o_*）三法暴露的对象集不同：γ° 只给负责对象，γ 给该活动涉及的全部对象，γ̃ 二者兼有并"correctly separating responsible objects from affected objects"；(b) RI^p_mi "not considered a deviation in the context of alignments"（三法与 GT 全空）；(c) RI^e_in(1) "none of the methods resolve the deviation correctly"——都判"ring 事件记错"而非"order depot 记错"；(d) BI7、BI3 属孤立活动/对象层，检出方式同记录错误；其余行为偏差 γ° 检不出（对象交互不在其视野），例外 BI9（两个 depot 对象的行为按模型都不完整，故 γ° 可见）；(e) γ 暴露全部偏差但不区分负责/受影响；γ̃ 对 BI7、BI3 能区分，"for the remaining deviations, the involved objects are detected without log and (labeled) model moves"。
- **单次视觉判读**（一次读页，未复核，整体标 `[表读数·单次判读·需验证]`）：

| Dev. | GT | γ° | γ | γ̃ | 解释栏（缩写） |
|---|---|---|---|---|---|
| RI^e_in(1) | {p} | {p} | {p,c} | {p}_(c) | 负责对象各法均暴露；γ/γ̃ 误把快递员加为负责/受影响 `[格内措辞不清]` |
| RI^e_in(2) | {p} | {p} | {p,q} | {p} | γ 把偏差错误级联到队列 |
| RI^e_mi | {p,v,c} | {p,v,c} | {p,v,c} | {p,v,c} | 各法均暴露 |
| RI^o_mi | {v}_(p,c) | {v} | {p,v,c} | {v}_(p,c) | γ̃ 正确定位受影响对象；γ° 不给；γ 当成负责 |
| RI^o_in | {c}_(p) | {c} | {p,c} | {c}_(p) | 同 RI^o_mi |
| RI^p_mi | ∅ | ∅ | ∅ | ∅ | 对齐语境下不是偏差 |
| BI5 | {q}_(p) | ∅ | {p,q,d} | ∅_(p,q) | γ/γ̃ 暴露受影响对象但无正确上下文；γ° 不暴露 |
| BI7 | {c}_(p,v) | {c} | {p,c,v} | {c}_(p,v) | 同 RI^o_mi |
| BI10 | {v}_(p,c) | ∅ | {p,c,v,d} | ∅_(v,p,c) | 同 BI5 |
| BI3 | {p,c} | {p,c} | {p,c} | {p,c} | 同 RI^e_mi |
| BI9 | {d}_(p,c) | {d} | {d,p} | {d}_(p,c) | 类 RI^o_mi，γ 漏掉受影响的快递员 |
| BI2 | ∅_(c,p,v,d) | ∅ | {p,c,v,d} | ∅_(c,p,v,d) | γ̃ 正确暴露受影响对象，γ 当成负责；γ° 不暴露 |

- **判断**：表的信息含量是"集合包含关系"，没有一个数。12 行里 γ̃ 与 GT 主集合一致 12/12、下标一致约 10/12（BI5、BI10 主集合为 ∅ 与 GT 的 {q}/{v} 不同）`[基于单次判读的计数，需验证]`；γ 在 9 行多报对象；γ° 在 3 行（BI5、BI10、BI2）全空。这就是 AQ1/AQ2 的全部定量证据——样本 = 12 份两包裹日志。

### 5.3 Fig. 11 / Fig. 12 逐图

- **Fig. 11** [PDF p.25]：图题 "Ground truth (GT) and computed (γ°, γ, and γ̃) sub-alignment results for recording error pattern RI^e_in and behavioral deviation pattern BI2. Log, model, and synchronous moves are colored yellow, purple, and green respectively. For clarity, truck and depot objects are omitted"。两个面板，各四行（GT / γ° / γ / γ̃），节点 = 活动框 + 上方对象多重集（[p1]、[p1,c1]、[p2,c1]）。
  - 左 "RI^e_in: log as depot order"：GT 行 = order depot（黄，日志移动）→ order home（紫，模型移动）→ ring、deliver depot（绿）；γ° / γ / γ̃ 三行的黄框都落在 **ring** 上，order depot 为绿 `[图读数·颜色单次判读]`——与正文 "all conclude that the ring event is incorrectly logged instead of the order depot event" 一致 [PDF p.24]。γ° 行把 p1 与 c1 拆成两条子对齐；γ̃ 行出现 ring⌈p、ring⌈c 投影记号与 τ_destroy / τ_create 静默模型移动。
  - 右 "BI2: multitasking"：GT 行含 τ_early-release、τ_late-claim 两个紫色静默移动，其余绿；γ° 行全绿（"show no deviations" [PDF p.25]）；γ 行 = 第一个 ring 黄 + 后插一个 ring 紫——即"用一条日志移动 + 一条模型移动"解释多任务，"its explanation differs from the deviation pattern used to generate the log" [PDF p.25]；γ̃ 行 = deliver depot 按对象拆成 ⌈c、⌈p 两个（放松同步移动）+ τ_destroy×2、τ_create [PDF p.25]。
  - 定性结论：图证实 γ̃ 的解释"结构上最接近 GT"，但正文自己承认"these alignments still allow for variance in their interpretation"（deliver depot 被拆、静默模型移动不匹配）[PDF p.25]——GT 与 γ̃ 之间的"距离"没有被定义，只靠肉眼。
- **Fig. 12** [PDF p.27]：图题 "Computation times of each method for every pattern of recording errors and behavioral deviations"。上排 "All methods"：分组柱状图，x = 12 个模式（标签极小，顺序疑为 Table 3 行序 `[图读数不清·x 轴标签]`），每组三柱 object（蓝）/ systemic（绿）/ relaxed（紫），y = Duration (s)，对数刻度 10^0–10^4。下排三小图 "Object" / "Systemic" / "Relaxed" 各自纵轴：Object 约 3×10^-1 到 10^0 量级；Systemic 10^0–10^2；Relaxed 10^1–10^4 `[图读数·刻度单次判读]`。
  - 能读出的定性：object 柱几乎全在 1 s 以下、彼此相近，BI7 一根明显高 [PDF p.27 正文同]；systemic 呈"两簇"——约 1 s 或约 10^2 s [PDF p.27]；relaxed 最高两根接近 10^4 s（疑为 RI^o_in 与 BI9 `[图读数·粗估·需验证]`），即对**两个包裹**的日志做放松对齐要数小时量级。
  - 正文归纳的三种时间"pattern" [PDF p.25]：(1) 除 BI5、BI10、BI7 外三法逐级"exponential increase"；(2) BI5、BI10 从 γ° 到 γ 增加、γ 到 γ̃ 无显著增加；(3) BI7 三法无显著差异。下排解读 [PDF p.27]：relaxed 相对 systemic "reasonably constant increase"，除 BI5/BI7/BI10。

### 5.4 支撑住的结论

1. **框架能产出按模式 × 方法的可判读评估表**（Table 3 的存在本身）——这是本文对"RQ：带 GT 的真实感噪声实验如何搭"的最直接回答 [PDF p.8, p.26]。成立，但只在"单问题、两包裹"的极小规模上。
2. **γ° 看不见对象交互层偏差**：BI5/BI10/BI2 行 γ° = ∅，Fig. 11 右 γ° 全绿 [PDF p.25–26]——有表有图，成立。
3. **γ 暴露全部偏差但把受影响对象一并算作负责**：Table 3 γ 列 9 行超集 + 正文 [PDF p.25–26]——成立。
4. **γ̃ 能分离负责/受影响，但解释不总正确**：RI^e_in(1)、BI2 两例 [PDF p.24–25]——成立，且这是全文最诚实的一段。
5. **计算时间随方法表达力上升、且上升幅度依模式而异**（BI5/BI7/BI10 例外）[PDF p.25, p.27]——柱状图定性支持"依模式而异"；"exponential" 见 5.5。

### 5.5 没撑住的 claim（逐条）

1. **"exponential increase"** [PDF p.25]，结论再抬为 "an exponential increase in computation time is expected across the different alignment techniques" [PDF p.28]：三种方法 = 三个点，无法区分指数与任何单调增长；无复杂度分析、无输入规模轴（所有日志都是两个包裹）。这是对数坐标下柱高的修辞，不是结论。
2. **"Systemic alignments are robust in detecting the deviations"** [PDF p.27]：Table 3 显示 γ 在 RI^e_in(2) 把偏差"级联到队列"、在 BI5 加入 depot 对象 "without adding correct context" [PDF p.26 单次判读]——"检出了某处不对"与"检出了偏差"被混用；robust 一词的样本量是 12。
3. **AQ2 无度量**：p.9 把评估形式化为 d(f(M0,L′), gt^f(·))，实验里 d 从未定义，"how well ... reflect" 只靠解释栏文字 [PDF p.9, p.24–27]。框架的形式化外壳与演示之间断链。
4. **"Having the ground truth knowledge provided by our framework was indispensable"** [PDF p.27]：对两包裹、单问题的日志，GT 可以手工标注；且作者在 p.19 自认这个数据集"not inherently infeasible"用现有方法生成 [PDF p.19]。"indispensable" 的是 GT 知识，不是本框架——演示恰好选了框架优势最弱的数据集，两个体现独特价值的数据集（能源合同的重复标签定向注噪、Omron 的模式互相影响 [PDF p.22–23]）没有进入任何评估 [PDF p.23, p.28]。
5. **时间数据无环境、无重复、无方差**（§5.1 末）：Fig. 12 每模式每法一根柱，10^4 s 量级的柱子有无重跑不可知 [PDF p.27]。
6. **"This approach trivially extends to the quantitative aspect"** [PDF p.28] 与同页 "limited ... by the dependency on the simulation method and parameters regarding the frequencies of the incorporated deviations" [PDF p.28] 并列 `[⚠️矛盾·同页]`：量化评估恰恰要求频率可控，而频率控制被承认是局限；p.21 已说频率只能靠大数定律逼近 [PDF p.21]。
7. **"记录错误 vs 行为离群可区分"是全文动机（p.7），实验没有测它**：三种方法都没有被要求把偏差归类为 RI 或 BI；Table 3 只比对象集合 [PDF p.7 vs p.24–27]。Oracle 的核心承诺（区分两类原因）在演示里未被行使。

## 6. Potential flaw

### 6.1 情境局限与延伸架构

- **同形式化假设**："limited by the assumption that the deviations can be modeled using the same formalism as the initial model" [PDF p.28]。11 个 BI 里 8 个（BI1/2/4/5/6/7/8/9）涉及资源、对象关联、队列或容量，蓝图全建在 t-PNID 上 [PDF p.10–13]；单案例 workflow net 场景用不上库的一半 [推断]。
- **全手工的两个环节**：映射 h 由用户选、角色约束靠用户遵守或变换里检查 [PDF p.14]；仿真参数手工设定且本实验只一组、模式彼此隔离（k = 1）[PDF p.19]。模式互相影响的数据集（Omron，"behaviorally influencing each other"）只被生成、未被评估 [PDF p.23]。
- **真实感未校准**：三个实例中两个源自课程合成过程（包裹投递、能源合同）[PDF p.18–19]，一个是 Omron 真实过程但只在"half of the process"加模式 [PDF p.23]；全文没有任何与真实日志的统计对照 `[推断，依据缺失]`。"designed in a way such that it could indicate a real-life process" [PDF p.18] 是设计意图，不是验证。
- **延伸架构**（原文自列）：量化维度——更宽的数据集 + 变化的偏差频率 + 统计 [PDF p.28]；随机/时间维度进模式或仿真模块 [PDF p.28]；用当前状态提高换岗概率、用历史数据校准随机信息 [PDF p.23]；PURPLE 式引导仿真补频率控制 [PDF p.21]；其他形式化 RC ν-nets / OPIDs / OC nets / proclets [PDF p.16]。本篇补一条原文没列的：把 p.9 的 d 实例化（对齐编辑距离 / 对象集合相似度）——没有它，"量化维度"无从谈起。

### 6.2 坏数据性质下的困难

ground truth 生成本身依赖五个假设，逐条看它们在真实坏数据面前站不站得住：

- **假设 A：噪声 = 模式库**。作者承认库 "inherently incomplete" [PDF p.28]；每个模式都需要位置映射 h [PDF p.13]，因此**非定位的全局噪声**（时间戳整体抖动、属性随机损坏、重试造成的重复事件）要么被拆成逐位置模式，要么塞进仿真分布 [PDF p.15–16]。p.6 列出的记录错误来源里 "filtering and aggregation methods" 在 Table 2 没有对应模式 [PDF p.6, p.10] [推断]。模式注入覆盖的是"有结构的噪声"，不覆盖"无结构的噪声"。
- **假设 B：GT 解释唯一**。Fig. 11 BI2 的 GT 含框架自造的 τ_early-release / τ_late-claim；γ 给出的"一条日志移动 + 一条模型移动"在标准代价函数下可能同代价甚至更低；RI^e_in(1) 三法一致选"ring 记错" [PDF p.24–25]。对齐方法优化的是**代价**，oracle 记录的是**发生了什么**，两者目标不同——"错"与"另一个同代价的合法解释"没有被区分 [推断]。原文自己承认 "these alignments still allow for variance in their interpretation" [PDF p.25]。**对一致性检查而言 ground truth 不是一个对象而是一个等价类**，这是 GT 方法学最深的坑，全文未触及。
- **假设 C：偏差 = 可加变换**。"additive in behavior" 保证 M0 行为不丢 [PDF p.13, p.19]，同时意味着永不建模"行为被移除"型偏差（分支废弃、活动合并）——真实日志里常见的概念漂移落在框架之外 [推断]。
- **假设 D：频率可控**。p.21 承认依赖大数定律逼近期望频率 [PDF p.21]；PD 的 GT 需要"frequent / infrequent"切分 [PDF p.9]，阈值由评估者定，于是 PD 的 GT 是参数不是真理 [推断]。
- **假设 E：RI 与 BI 落日志后"boil down to similar issues"** [PDF p.7]。这正是可识别性问题：RI^e_mi（装车事件缺失）与 BI3（跳过按铃）在日志上都是"少一个事件" [PDF p.18–19]；框架能分别生成两者，却没有问"只看日志 + M0 的方法能否区分它们"。

### 6.3 哪个困难值得写 paper

- **首选：偏差可识别性研究**（假设 E + B）。用本框架生成"同貌不同因"的模式对（RI^e_mi vs BI3、RI^o_in vs BI7、RI^p_in vs BI10），度量任何只用日志与 M0 的方法能否分辨原因，给出可识别/不可识别边界。这直接检验 p.7 的动机，产出是"评估框架的评估"；问题定义干净、baseline 明确（三种对齐 + 任一噪声过滤器）、数据由框架自产、GT 天然存在。
- **次选：等价类 GT 与 d 的实例化**（假设 B）。把 p.9 的 d 做成对齐间编辑距离或对象集合度量，让 Table 3 从解释栏变成数字，顺带终结 "exponential" 之类的修辞。
- **不值得**：把 10^4 s 压下去——那是 Sommers 2024 放松对齐自身的问题，不是 GT 方法学的问题。

## 7. Motivation 还原（问句形式）

1. 在 Omron 数据上，为什么每处偏差都验不了？——每处偏差有多种解释，没有全知者说哪种对 [PDF p.2]。
2. 全知者需要知道什么？——每个事件由哪个变迁产生、该变迁是基线元素还是偏差元素 [PDF p.8–9]。
3. 这份知识哪里能免费拿到？——仿真器；只要偏差是模型元素而不是日志后处理 [PDF p.2, p.8]。（→ Insight 1、N1）
4. 偏差从哪来、怎么不互相干扰？——文献分类学 + 可加变换 [PDF p.6–7, p.13]。（→ N2、N3）
5. 一份日志够代表吗？——不够，所以 n·m·k [PDF p.17]。（→ N5）
6. 怎么证明这套东西有用？——拿自家三种对齐方法做一次定性评估 [PDF p.23–27]。
7. （原文未问）oracle 的解释是唯一正解吗？——p.25 自己说 "still allow for variance" [PDF p.25]。
8. （原文未问）动机里的"区分 RI 与 BI"测了吗？——没有 [PDF p.7 vs p.24–27]。

## 8. 张力结构分析

**改变谁的想法**：
- 用 BPIC 真实日志做评估的主流：没有 GT 的"realistic"评估不是 assessment，是 case study——"the correctness of the identification of the algorithm cannot be verified" [PDF p.4]。
- PTALG / PURPLE / AIR-BAGEL 的作者：注噪应在模型层而非日志层，否则"模型与日志之间的链接丢失" [PDF p.4–5, p.7]。
- 一致性检查社区：可解释性与时间的折衷是模式相关的，不是一刀切——BI5/BI7/BI10 上"more interpretability can be achieved without significantly giving in on the computation times" [PDF p.27]。

**But 在哪里**：领域默认"真实感与 ground truth 二选一"（真实日志有真实感无 GT；合成日志有 GT 无真实感）。本文的 But：真实感可以被**建模**——模式来自真实数据文献 [PDF p.6–7, p.19]——所以两者兼得。**残余张力一**（原文部分承认）：真实感现在只等于"模式库 + 仿真参数"的真实感，前者 "inherently incomplete"、后者 "potentially affecting the realism" [PDF p.28]。**残余张力二**（原文未承认）：对一致性检查，GT 不是唯一对象（§6.2 假设 B）；oracle 说"发生了 X"，方法说"最便宜的解释是 Y"，两者不同不等于方法错。

**综述的张力结构**：数据来源（真实 / 合成）× GT 形态（无 / 有标签 / 有模型链接）。真实日志：无 GT [PDF p.3–4]；现有合成：无标签（PTALG、PURPLE）或有标签无链接（AIR-BAGEL）[PDF p.4–5]；本文占"有链接"格 [PDF p.5 Fig. 1b, p.8]。实验只支撑"链接 → 对象级归因可判"这一格的功能（Table 3 的下标列是链接的直接产物），不支撑"真实感"那一维——没有与任何真实日志的对照。

## 9. 桥线定位注记

本篇在桥线是**必要辅助**（ground-truth 评估方法学）。只写它提供什么 / 以什么为前提 / 不提供什么。

**提供**：
- P1 GT 构造配方：M0 → M^S → M^L → L′，事件回链变迁；每个事件可标"基线 / 哪个 RI / 哪个 BI"，并给出负责对象与受影响对象 [PDF p.8–9, p.24]。
- P2 分类学：7 RI + 11 BI，两类偏差在**生成时**就分开、各有具名模型元素 [PDF p.10]。
- P3 评估通式与两个实例化：质量 = d(f(M0, L′), gt^f(M0, L′, M^S, M^L))；PD 目标模型 = M0 + 频繁 BI 子集、忽略不频繁 BI 与全部 RI；CC 目标 = 最优对齐 [PDF p.9]。**PD 实例化只有定义，全文没有跑过任何发现算法** [PDF p.9, p.23–27]。
- P4 数据集乘子 n·m·k 与三个实例；模型与日志声明在 gitlab [PDF p.17–23, p.18]。
- P5 评估表形态：模式 × 方法 → 对象集合对照 + 解释栏（Table 3）[PDF p.26]，可直接复用作定性评估模板。
- P6 工具：Trident（GUI）/ mira（Python 脚本）[PDF p.16–17]。

**前提**：base model 为 Petri 网族形式化，对象级模式需 t-PNID [PDF p.10–13, p.28]；h 与仿真参数手工设定 [PDF p.14, p.19]；被评估技术能接受投影日志 [PDF p.24]；评估者自己定义 gt^f 与 d [PDF p.9]。

**不提供**：任何数值型质量分（d 未实例化）；频率受控的数据集（本实验 k = 1、模式隔离）[PDF p.19]；与真实日志的真实感校准；PD 评估的任何实证；对"日志层采样 / 过滤"的任何讨论——全文 "sampling" 只指从分布采样变迁触发与时长 [PDF p.15, p.17]，"filter" 只出现在 p.6（记录错误来源 "filtering and aggregation methods"）与 p.7（"recording errors should ideally be filtered out completely"）[PDF p.6–7]；全文无 EdgeIM 相关内容。

**对 p1 三条 open 的兼核**：
1. **BI 编号漂移**：在 §5/§6 范围再核——p.18 列表（BI5/7/10/3/9/2）、p.21（BI7/9/10/2/11）、p.23（BI6/7/2）、Table 3 行标、Fig. 11 图题 BI2 = multitasking、p.25/p.27 正文 BI7 = switching roles，**全部与 Table 2 一致** [PDF p.18, p.21, p.23, p.25–27]。全文错位点只有 p.10 "Skipping an activity (BI1)" 与 p.14 两处（"the pattern BI2 for changing correlation"、"The pattern BI6 for switching roles"），而 p.14 同页前一行 "changing correlation (BI1), switching roles BI7" 是对的 [PDF p.14]。**结论：非全文系统性错位；是模式定义节（p.10、p.14）残留的旧编号，应用节与实验节全部用 Table 2 新编号** [推断]。旧编号疑为 ICPM 2024 版本序（skipping = BI1、correlation = BI2、roles = BI6）`[需验证：需比对 ICPM 2024 原文，本次无网]`。
2. **Table 2 连线**：按任务书未再试。
3. **数据可得性**：p.28 Declarations 只有 Ethics（"Not applicable"）与 Competing interests，无其他数据说法 [PDF p.28]；同页结论段 "We described the usage of the framework for creating datasets consisting of multiple event logs" [PDF p.28] 与 p.18 gitlab 链接一起，两处自证生成了数据集。**"No datasets were generated or analysed during the current study" 与正文矛盾成立** `[⚠️矛盾]`，出版社模板句未改是最简解释 [推断]；gitlab 链接可达性 `[需验证：无网]`。
