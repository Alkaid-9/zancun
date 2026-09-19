Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# 12 · Sommers（Process Science 2025）第一性原理全拆（下：§5–§9）—— 桥线 T1 必要辅助篇

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
