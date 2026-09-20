# EdgeIM 论文地图：先定位，再裁定

这份地图服务于第一次通读和各站回查。它告诉你作者在哪里定义对象、怎样描述三阶段、在哪些表中报告指标；它不替你判断作者的证据够不够，也不回答后续的跨站推理题。

原文：[EdgeIM: An Efficient Edge-based Process Model Discovery Technique](../../../03_鲁组其他论文与研究谱系/99_其他论文与盘点/论文原文与拆解/EdgeIM-2025-ICWS.pdf)，Xuan Su、Cong Liu、Faming Lu、Long Cheng、Qingtian Zeng、Shouli Zhang，IEEE International Conference on Web Services（ICWS）2025，DOI（digital object identifier，数字对象标识符）`10.1109/ICWS67624.2025.00057`。文件共 7 页，PDF 第 1–7 页对应印刷页 404–410。

先认两种标签：

- `PAPER-TEXT`：下面这句话是对作者正文、图、算法或表格的保守转述，并附印刷页码。它表示“作者这样写”，不表示作者已经充分证明。
- `导航说明`：为了帮助阅读而写的位置提示、术语解释或待答问题，不冒充论文结论。

回到训练入口：[START_HERE.md](./START_HERE.md)。当前八站顺序及证据规则以入口页为准。

## 1. 论文在研究什么

`PAPER-TEXT`（摘要与 §I，p.404）：作者把对象放在物联网（Internet of Things，IoT）产生的大规模、分布式事件日志上，关注过程模型发现的可扩展性、效率和模型质量。过程模型发现是从事件日志中构造过程模型的任务。

`PAPER-TEXT`（§I，pp.404–405）：作者提出 EdgeIM，称它受 Inductive Miner（IM，归纳式过程发现算法）启发，先过滤冗余案例，再在边缘节点构造局部特征，最后由中心节点聚合并发现 Petri net（用库所、变迁和流关系表达过程行为的模型）。

`PAPER-TEXT`（摘要，p.404；§V，pp.408–410）：作者称 EdgeIM 已在 PM4Py（过程挖掘 Python 工具库）上实现，并用 9 个公开事件日志与 Alpha Miner、Inductive Miner、EdgeAlpha 进行质量或时间比较。比较对象和指标必须按具体表格分别读取，不能从摘要一句话外推。

## 2. 相关工作分成哪四类

论文 §II 位于 p.405。下面四类是对该节行文的导航归纳；每一行只转述作者如何摆放文献，不替作者补实验。

| 类别 | `PAPER-TEXT` 位置 | 作者讨论的核心问题 |
|---|---|---|
| 集中式过程模型发现 | §II，p.405 | 完整日志集中存储和处理；面对大规模分布式数据时出现传输、存储和计算瓶颈 |
| 分布式或边缘式过程挖掘 | §I–II，pp.404–405 | MapReduce（把计算拆分后再汇总的分布式处理框架）等并行化方法，以及边缘节点先构造局部关系或局部模型、中心再聚合的方法；作者同时指出频繁交换和部分集中聚合的负担 |
| 流式过程模型发现 | §II，p.405 | 用滑动窗口、近似计数和动态更新处理连续事件流；作者强调实时性与噪声处理、稳定性、准确性之间的取舍 |
| 隐私保护过程挖掘 | §II，p.405 | 以差分隐私等技术保护敏感信息；作者指出可能伴随模型准确率下降或额外计算成本 |

`导航说明`：§I 还单独回顾 EdgeMiner / EdgeAlpha，并列出作者认为它们在效率、同时间戳处理和复杂结构处理上的限制（p.404）。这段是 EdgeIM 的直接问题动机，不要与 §V 的实验结果混写。

## 3. 三阶段数据流

直接跟随关系指一条 trace 中相邻活动形成的有序对；DFG（directly-follows graph，直接跟随图）把活动作为节点、直接跟随关系作为有向边，并可在边上记录出现次数。`S`、`E`、`R` 分别表示起始活动集合、结束活动集合和直接跟随关系集合；带下标 `i` 时表示某个边缘节点的局部集合。

| 阶段 | `PAPER-TEXT` 名称与位置 | 输入 | 作者写出的处理 | 输出 |
|---|---|---|---|---|
| Stage 1 | Preprocessing and Feature-Preserving Sampling；§IV-A/B，pp.406–407；Algorithm 1，p.407 | cases set，也就是由多条 trace 组成的案例集合 | 按 `CaseID, Timestamp` 建立次序；逐条抽取起点、终点和直接跟随关系；只在当前 trace 扩展全局特征时保留它 | 过滤后的 `D'` 与全局特征 `(S, E, R)` |
| Stage 2 | Local Feature Construction of Edge Nodes；§IV-A/C，pp.406–407；Algorithm 2，p.407 | Algorithm 2 表头列出 `D'` 与全局特征 `(S, E, R)` | 以 hash function（哈希函数，把活动映射到节点编号的规则）分配活动；各边缘节点记录局部起止活动和带计数的直接跟随关系；同时间戳相邻事件加入双向关系 | 每个节点的局部特征 `Local_i = (S_i, E_i, R_i)` |
| Stage 3 | Central Node Merging and Model Discovery；§IV-A/D，pp.407–408；Algorithm 3，p.408 | 所有节点的 `Local_i = (S_i, E_i, R_i)` | 中心节点对局部起止集合做并集、对关系计数做累加，形成全局 DFG；再识别顺序、并行、选择、循环结构并递归分解 | Petri net `PN` |

`导航说明`：表中只恢复作者明确写出的输入、处理和输出。某阶段的摘要对下游算法是否“信息充分”、不同实现是否真的等价，仍是学习者问题，不在这里补结论。

## 4. 七页怎么找

| 印刷页 | 章节、图、算法或表 | 读这一页时找什么 |
|---|---|---|
| p.404 | 标题、摘要、§I Introduction | 研究对象、三阶段一句话版本、作者对 EdgeMiner / EdgeAlpha 的问题陈述 |
| p.405 | §II Related Work；§III Background Knowledge；Definitions 1–3 | 四类相关工作；事件日志、trace、activity（活动）、起止活动、直接跟随关系及其权重 |
| p.406 | Definitions 4–5；Figures 1–3；§IV-A | DFG、Petri net、整体架构图和三阶段名称；Stage 1、Stage 2 的概述从本页开始 |
| p.407 | §IV-A 续；§IV-B/C；Algorithms 1–2 | 三阶段概述收尾；特征保留过滤；边缘节点局部特征构造和同时间戳处理 |
| p.408 | §IV-D；Algorithm 3；§V 与 §V-A/B 开始 | 中心聚合与递归发现；实验环境；质量指标 fitness、precision、F-measure 的定义 |
| p.409 | Tables I–II；§V-B 续；§V-C；§VI 开始 | 9 个日志的规模；四种方法的质量结果；时间实验设计与作者解释；结论开头 |
| p.410 | Table III；References | EdgeAlpha 与 EdgeIM 的运行时间，以及 EdgeIM 的 sampling time 和 discovery time |

fitness（拟合度）衡量模型重放已观察行为的程度；precision（精确度）衡量模型是否避免允许日志中未观察到的额外行为；F-measure 是二者的调和平均。这里给定义是为了能读表，不提前判断某个模型比较意味着什么。

## 5. 三张表究竟放了什么

| 表 | 位置 | `PAPER-TEXT` 报告内容 | 不能从表名直接得到的结论 |
|---|---|---|---|
| Table I | p.409；实验设置在 §V-A p.408 | 9 个公开日志的 trace 数、event（单次活动记录）数、活动种类数，以及 trace 长度的最小、平均、最大值 | 数据规模不自动证明采样、通信或隐私性质 |
| Table II | p.409；指标定义和文字分析在 §V-B pp.408–409 | Alpha Miner、Inductive Miner、EdgeAlpha、EdgeIM 的 fitness、precision、F-measure | 一张结果表本身不自动给出因果机制或适用到所有日志的保证 |
| Table III | p.410；实验说明和文字分析在 §V-C p.409 | EdgeAlpha 的 time；EdgeIM 的 sum time、sampling time、discovery time；作者称每个数据集测 5 次后取平均 | 运行时间列与其他资源或系统属性不是同一个测量项 |

## 6. Claim–evidence 工作表

claim 是作者希望读者接受的主张；evidence 是用来支撑主张的可检查材料。下表只预填“去哪找”和论文实际命名的指标，不替你做“证据是否直接、是否足够”的裁定。最后一列必须由学习者在相应站点解锁后填写。

| 主题 | 作者在哪里说 | 实验在哪里测 | 学习者裁定 |
|---|---|---|---|
| 模型质量 | `PAPER-TEXT`：摘要 p.404；§V-B pp.408–409；§VI p.409。作者使用“maintaining high model quality”等表述，并在正文分别讨论 fitness、precision、F-measure | §V-B 定义三个质量指标；Table II p.409 报告四种方法在 9 个日志上的数值。请逐项写清某个 claim 对应哪一列、哪些数据集 | ________ |
| 时间与效率 | `PAPER-TEXT`：摘要与 §I p.404；§V-C p.409；§VI p.409。作者声称提高发现效率，并讨论大规模边缘场景 | §V-C p.409 说明比较和重复测量方式；Table III p.410 报告时间列。请标出比较基线、单位、分项与总体 | ________ |
| 通信 | `PAPER-TEXT`：§I pp.404–405 把通信开销列为问题；§V-C p.409 将过滤冗余案例与节点互访、通信开销联系起来 | 检查 §V 与 Tables I–III：记录作者实际报告的通信测量名称、单位、列或图；找不到时写 `NONE`，不要用运行时间代填 | ________ |
| 隐私 | `PAPER-TEXT`：§VI p.409 将 EdgeIM 描述为 privacy-preserving（隐私保护）；§I p.404 对隐私的较早表述是在介绍 EdgeMiner，归属不要混淆 | 检查 §V 与 Tables I–III：记录作者实际报告的隐私机制、攻击模型、预算、泄露量或其他测量位置；找不到时写 `NONE` | ________ |
| “zero loss” | `PAPER-TEXT`：§IV-B p.407 在 Algorithm 1 前，作者把集合包含检查描述为对关键过程结构特征的 zero loss（零损失） | 对照 Algorithm 1 的输出与 §V、Tables I–III：先写作者实际检查了哪一种对象或指标，再判断是否与该措辞同层 | ________ |

填写时把三件事分开：作者说了什么、实验实际测了什么、你允许结论走到哪里。`PAPER-TEXT` 只能用于前两件事的来源归属，不能替你完成第三件事。

## 7. 只在解锁后回答的问题

下面只给问题，不给结论。完成对应站核心题后，再到 [CONNECTIONS.md](./CONNECTIONS.md) 按要求作答。

### EX-01 后：一份摘要何时是充分信息

固定一个下游发现算法，先列出它实际读取的全部输入。只知道 `(S, E, R)` 或带权 DFG 时，什么条件下能够唯一确定该算法的输出？请尝试构造“摘要相同、原日志不同”的一对例子，并说明它是否会让下游输出不同。

### EX-02 后：什么时候能从切日志改成切图

论文 Stage 3 从全局 DFG 递归分解；经典 IM 的说明通常从日志上的切分进入。若把“切日志”替换为“切图”，需要补齐哪些信息、假设或 fall-through（基础切分失败后的后备处理）？递归中的哪一步仍可能需要原日志？

### EX-07 后：fitness、precision 与模型语言的张力

两个模型都能重放同一批已观察 trace 时，如果它们还允许不同数量或不同种类的未观察行为，fitness、precision 会怎样约束你的比较？哪些有限日志上的观测仍不足以断言两模型允许的全部行为相同？

这些问题的价值就在于由学习者自己建立“对象 -> 摘要 -> 算法读取 -> 可支持 claim”的链条。不要从密封答案、旧会话或 AI 补全中提前拿结论。
