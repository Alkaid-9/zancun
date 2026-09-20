# Maps 2-4（地图 2-4）：方法、思想谱系与迁移

- **用途**：把“还可以联想到什么”改写成能比较、能追源、能证伪的研究动作。
- **读者**：已经沿 [START_HERE.md](./START_HERE.md) 做当前站、但还不熟悉研究方法的学习者。
- **第一步**：不要先填结论。先在 Map 2 选一行方法，按统一比较轴补完一格“我的证据”；只有当前站授权后，才把 EdgeIM 的具体判断写入站内卡。
- **当前入口**：带权 DFG（带边频次的直接跟随图）是当前可比较对象；从它推到 cut（切分，把活动分组并判断组间关系）、模型或实验结论的关系仍需逐站验证。
- **暂时封存**：会直接回答后站的 EdgeIM 充分性、异常偏好、模型等价和证据充分性结论。公开地图只给框架、来源位置、异领域例子和空白记录。

Map 1 见 [KNOWLEDGE_MAP.md](./KNOWLEDGE_MAP.md)，Map 5 见 [RESEARCHER_COMPETENCY_MAP.md](./RESEARCHER_COMPETENCY_MAP.md)，Map 6 见 [RESEARCH_IDENTITY_MAP.md](./RESEARCH_IDENTITY_MAP.md)，Map 7 见 [RESEARCH_TRAJECTORY_MAP.md](./RESEARCH_TRAJECTORY_MAP.md)，论文导航见 [PAPER_MAP.md](./PAPER_MAP.md)。

统一记录接口：[RESEARCH_NOTE_TEMPLATE.md](./RESEARCH_NOTE_TEMPLATE.md)。后续系统阅读或算法怀疑必须链接该模板，按适用性填写 Evidence audit（证据审计）与 Research hooks（研究钩子）；不适用时写理由，本图不复制模板。

## 两条硬约束

- `Epistemic Integrity`（认知诚信）：用 `UNKNOWN` 标记当前无法裁定的项；保留 negative evidence（负面证据，包括失败、未观察到和反例）；记录 credit（谁完成了什么）与 provenance（主张到原始来源的链）。
- `Research Economy`（研究经济性）：在扩展一个问题前，写 value of information（信息价值，它可能改变哪个决定）、cost（时间、数据、计算和协作成本）与 decision impact（决策影响，不同结果分别触发什么动作）。

这两项必须进入方法记录、谱系记录、迁移验证和探索环，但不扩成七图全打卡。

## Map 2：Method Landscape（方法版图）

Method Landscape 指把解决同一类问题的方法放到统一坐标中比较。sampling（采样）指从原数据选出部分对象；summary（摘要）指不一定保留原对象，而是保留某种统计或结构信息。`K` 指运行前给定的保留数量预算。trace（轨迹）是一个案例内按时间排列的活动序列；variant（变体）指活动序列相同的一类 trace。

| 方法族 | 基本操作 | 主要想保什么 | 可能丢什么 | 需要的先验信息 | `K` | 顺序影响 | 是否直接保频次 | 保证应怎样写 | 我的证据或待查动作 |
|---|---|---|---|---|---|---|---|---|---|
| 随机采样 | 按随机规则抽 trace | 总体的随机切片 | 稀有结构可能未被抽到 | 随机机制、样本框 | 常见为需要 | 设计正确时不应由遍历顺序决定，但受随机种子影响 | 只近似，需误差分析 | 概率保证必须带样本量和假设 | ________ |
| 分层或变体采样 | 先按标签、层或变体分组，再从各组抽取 | 预先指定的组别覆盖或比例 | 未进入分层规则的差异 | 分层变量或变体定义 | 通常需要 | 取决于组内选择规则 | 可按设计近似 | 只能保证被定义的分层目标 | ________ |
| 频率代表 | 优先保留常见对象或按频率配额选取 | 主体分布或高频模式 | 低频但结构关键的对象 | 全局或近似频数 | 通常需要 | 排名并列时要声明 | 目标通常与频次直接相关 | 需写清距离、误差或配额 | ________ |
| coverage witness（覆盖见证） | 选能让目标特征集合继续扩大的对象 | 指定特征是否出现 | 原始出现次数、共同出现结构或其他未指定信息 | 特征定义和已覆盖状态 | 可以没有固定 `K` | 若逐个贪心处理，常可能受顺序影响 | 不自动保留 | 只对明确列出的特征谈保证 | ________ |
| 统计摘要 | 保存计数、均值、分布参数等，而非原对象 | 预先选定的统计量 | 个体身份、次序或高阶依赖 | 要回答的查询或模型假设 | 不一定适用 | 批量聚合通常可设计成无关 | 可以保指定频次 | 只对指定查询或统计量充分 | ________ |
| sketch（流式压缩摘要） | 用固定小内存近似记录大数据流 | 高频项、频数或基数等指定查询 | 精确明细和低于误差范围的差别 | 流模型、内存预算、误差目标 | 不是 trace 数预算 | 更新顺序的影响取决于算法 | 通常近似 | 必须同时写误差与失败概率 | ________ |
| 分布式计算 | 把数据或计算放到多个节点，再聚合中间结果 | 可扩展处理和局部计算结果 | 若中间接口过窄，可能丢下游所需信息 | 分区、通信和聚合规则 | 不一定适用 | 取决于合并算子是否满足交换、结合等条件 | 取决于局部输出 | 系统性质和信息保证要分开验证 | ________ |

这张表只比较接口，不裁定 EdgeIM 属于哪一行、保留的信息是否足够，或哪一种方法更好。到站后应先写消费者实际读取什么，再填结论。

### 方法比较记录

```markdown
- 当前问题：________
- 候选方法：________ 与 ________
- 共同输入单位：________
- 比较轴：保留 / 丢失 / 先验 / K / 顺序 / 频次 / 保证
- 我的运行前判断：________
- 可推翻判断的结果：________
- 最小检查：输入 ________；只改 ________；观察 ________
- 原始证据：路径 + 标题 / 输出文件
- UNKNOWN / 负面证据：________
- credit / provenance：谁做了什么 ________；原始来源 ________
- 信息价值 / 成本 / 决策影响：________ / ________ / ________
- 结论上限：________
```

## Map 3：Idea Genealogy（思想谱系）

Idea Genealogy 指追踪一个方法公开可考证的来源、相邻方向和问题继承关系。`CITATION-BACKED` 表示论文正文或引文明确支持的历史关系；`USER-RECONSTRUCTION` 表示学习者依据机制重建“一个想法可能怎样产生”，不能写成作者真实动机或历史事实。

### 可考证链

| 类型 | 可考证位置 | 只允许记录的关系 | 仍需学习者核查 |
|---|---|---|---|
| `CITATION-BACKED` | EdgeIM §II，p.405；[PAPER_MAP §2](./PAPER_MAP.md#2-相关工作分成哪四类) | 论文把集中式、分布式或边缘式、流式、隐私保护工作放在相关工作中 | 每条具体文献解决了什么、作者如何评价，回 PDF 查引文上下文 |
| `CITATION-BACKED` | EdgeIM §I，pp.404-405；[PAPER_MAP §2](./PAPER_MAP.md#2-相关工作分成哪四类) | 论文将 EdgeMiner 和 EdgeAlpha 放在直接问题背景中 | 哪个限制由作者陈述、哪个由实验测量，分开记录 |
| `CITATION-BACKED` | EdgeIM 摘要与 §I，p.404；[PAPER_MAP §1](./PAPER_MAP.md#1-论文在研究什么) | 作者明说 EdgeIM 受 Inductive Miner 启发 | “受启发”具体对应哪些机制，不能仅凭这句话补写 |
| `CITATION-BACKED` | EdgeIM §IV，pp.406-408；[PAPER_MAP §3](./PAPER_MAP.md#3-三阶段数据流) | 论文明确给出预处理、边缘节点局部特征、中心聚合与发现三阶段 | 各阶段接口是否足以复现、实现是否读取所有字段，需逐项核查 |

原文入口：[EdgeIM PDF（portable document format，便携式文档格式文件）](../../../03_鲁组其他论文与研究谱系/99_其他论文与盘点/论文原文与拆解/EdgeIM-2025-ICWS.pdf)。本表的页码是导航，不替代阅读引文所在句和参考文献条目。流式与隐私保护方向在 §II 出现，只能先记为相邻研究背景，不能自动画成 EdgeIM 的直接祖先。

### 机制重建区

| `USER-RECONSTRUCTION` 问题 | 我观察到的机制 | 候选来源或类比 | 竞争解释 | 去哪里找作者证据 | 当前标签 |
|---|---|---|---|---|---|
| 为什么先缩减输入，再构造局部特征？ | ________ | ________ | ________ | 摘要、§I、§IV 和被引方法原文 | `USER-RECONSTRUCTION` |
| 为什么把局部结果交给中心聚合？ | ________ | ________ | ________ | §IV 的输入输出和相关工作 | `USER-RECONSTRUCTION` |
| 为什么选这一组结构特征，而不是别的摘要？ | ________ | ________ | ________ | Definitions、Algorithms 1-3、下游函数读取项 | `USER-RECONSTRUCTION` |

把一条重建升级为历史陈述前，至少补：原句、页码、引用对象、关系类型。找不到时保留 `USER-RECONSTRUCTION`，不要改成“作者为了……”。

谱系记录还要保留检索失败和互相冲突的来源。查不到不是“证明不存在”，只是一条带检索范围的负面证据；继续查之前先问新来源是否会改变当前归属或实验决定。

<a id="parked-crossedgeim"></a>
### `PARKED` 谱系枝：CrossEdgeIM

这条枝只登记，不进入当前练习。它在概念上绑定主干的 `Stage 3 IM -> Petri net`；实际阅读仍服从 BRIEF A5，最早在 EX-06 后解锁。到时还要有一个会改变研究判断的跨组织建模问题，才评估升级门。

| 层次 | 可核事实或重建 | 来源与边界 |
|---|---|---|
| `PAPER-TEXT` | EdgeIM 在边缘节点提取局部特征，中心节点聚合全局 DFG 并发现模型 | [EdgeIM](../../../03_鲁组其他论文与研究谱系/99_其他论文与盘点/论文原文与拆解/EdgeIM-2025-ICWS.pdf)，pp.404-408 |
| `PAPER-TEXT` | CrossEdgeIM 的数据流是 activity node 在线维护并上报增量 DFR/Start/End -> organization node 构造 Org-DFG、运行 IM 得到组织级 Petri net -> central node 结构化合并各组织 Petri net | [CrossEdgeIM](../../04_CrossEdgeIM/论文原文与拆解/CrossEdgeIM-2026-IoTMag.pdf)，pp.55-58；[DOI](https://doi.org/10.1109/MIOT.2025.3625047) |
| `PAPER-TEXT` | CrossEdgeIM 引用并对照 EdgeMiner/EdgeIM 这组既有方法；作者把这组方法概括为主要面向 single-organization IoT。CrossEdgeIM 与 EdgeIM 有四位共同作者，但 Faming Lu 不在 CrossEdgeIM 作者表中 | CrossEdgeIM p.55；EdgeIM p.404。原组句不能改写成“EdgeIM 单篇证明自己只适用于单组织” |
| `PAPER-TEXT` | CrossEdgeIM 明写：尚未显式捕获多机器人协作关系，组织间 interaction 仍是 implicit | CrossEdgeIM p.60, Threats to Validity |
| `USER-RECONSTRUCTION` | 把两篇组织成 `predecessor -> residual -> computation placement change -> new residual` | 这是依据引用、共同作者、问题残差和架构变化作出的读者重建，不是作者明说的直接继承关系 |
| `UNKNOWN` | 作者是否有意把 CrossEdgeIM 定义为 EdgeIM 的正式直接后继；中心合并后保留了多少跨组织交互语义 | 当前两篇原文不足以裁定 |

枝条状态：`PARKED`。重开条件：先到 EX-06 后，再满足 Dependency（当前任务确实需要组织级 Petri net 或模型合并）或 Research leverage（显式 interaction 的缺失形成可证伪且会改变决定的问题）。当前只保留一个识别线索：看后继工作时，分别追踪“上一代移走的瓶颈”和“新架构暴露的新瓶颈”。

### idea 芽链

idea 芽链把一个观察推进到可检查更新：observation（原始观察）-> idea（待检想法）-> mechanism（候选机制）-> prediction（可被推翻的预测）-> attack（主动找反例）-> minimal test（最小区分测试）-> evidence（带来源的证据）-> update（按证据更新）。它是一条工作记录，不是成果等级。

| 芽链位置 | 必填记录 |
|---|---|
| observation | 我实际看见了什么，原始位置 ________ |
| idea | 一个待检问题或关系 ________ |
| mechanism | 若关系成立，可能通过什么机制 ________ |
| prediction | 在条件 ________ 下应观察到 ________ |
| attack | 最小反例或竞争解释 ________ |
| minimal test | 只改 ________；比较 ________；成本 ________ |
| evidence | 原始输出 / 原文 ________；负面证据 ________；credit ________ |
| update | 保留 ________；改写 ________；仍为 `UNKNOWN` ________；改变的决定 ________ |

芽链只有在原始观察、攻击和证据齐全后，才可能成为一条有边界的研究判断；未完成时仍称“芽”，不得写成发现、贡献或成果。一次错误也可成为 observation，但要继续抽象出可迁移识别线索，再到新任务验证，不能把“我错过一次”直接升级成方法论。

## Map 4：Transfer Map（迁移地图）

`common abstraction` 指两个问题共享的抽象骨架；`same` 指可逐项对应的结构；`different` 指不能对应的机制或目标；`new question` 指类比产生的新问题；`verification action` 指能执行的核查动作；`analogy ceiling` 指类比最多能支持到哪里。每次迁移固定使用这六项，不增减字段。

### 公开异领域例子：消防演练场景选择

消防部门要从许多演练场景中选少数几个，使灭火、疏散、通信、急救四类技能都至少演练一次。set cover（集合覆盖）指用尽量少的集合覆盖全部目标；maximum coverage（最大覆盖）指预算固定时覆盖尽量多的目标。

| common abstraction | same | different | new question | verification action | analogy ceiling |
|---|---|---|---|---|---|
| 从候选对象中选子集，使指定特征被见证 | 每个演练场景对应一组技能；选中场景会扩展已覆盖技能集合 | 演练还关心人员熟练度、重复频次和风险，单次“覆盖过”不能代替这些量 | 同样覆盖四类技能的两个方案，训练强度和风险暴露会不会不同？ | 为每个方案列“技能是否出现、练了几次、由谁完成”，再比较差异 | 只能提示“覆盖集合不等于保留所有信息”，不能证明任何过程挖掘算法的性质 |

### 学习者迁移单

| common abstraction | same | different | new question | verification action | analogy ceiling |
|---|---|---|---|---|---|
| ________ | ________ | ________ | ________ | 写成可执行的输入、改动和观察：________ | ________ |

EdgeIM 专属且会导出后站结论的迁移，只写入当前站授权的卡片；公开表不得预填。

填写 `verification action` 时同时写预计成本和结果会改变的决定；填写 `analogy ceiling` 时注明来源、贡献归属和仍为 `UNKNOWN` 的部分。六字段本身不增加。

### `PARKED` 迁移枝：DES、形式化验证与 Multi-Agent Systems

CrossEdgeIM 原文处理多机器人、跨组织的过程发现，并明确生成、合并 Petri net；它没有把方法写成 discrete-event systems（DES，离散事件系统）、formal verification（形式化验证）、runtime verification（运行时验证）或 Multi-Agent Systems safety（多智能体系统安全）方法。下面三行是待检迁移，不是论文贡献：

| common abstraction | same | different | new question | verification action | analogy ceiling |
|---|---|---|---|---|---|
| 离散事件、并发与同步的显式行为模型 | 两篇论文都从事件记录得到 DFG，并生成或处理 Petri net | DES 控制还需要 plant、specification、controllability、observability 和控制接口；两篇没有给出这些合同 | 当前 Petri net 能否被解释成某个明确 DES 模型？缺哪些状态和可观测事件？ | 到 Petri net 节点后，选一个 2-4 事件系统，逐项写状态、事件、可观测性、允许控制的动作，再检查映射 | 只能提出 DES 映射问题，不能称论文已经完成控制器设计或 supervisory control |
| `behavior data -> discovered model -> candidate property check` | 过程发现输出显式模型，Petri net 可作为后续验证的候选输入 | 发现出的描述性模型不是规范；论文没有给 safety/liveness property、初始 marking、model checker 或证明 | 哪个性质要验证？日志到模型的 abstraction 是否保留该性质？ | 先固定 property 和反例，再检查模型语义、初始状态、抽象保持义务和验证器输出 | “可作为验证输入”不等于“已经形式化验证”；process conformance 也不自动等于 safety |
| 多个自治实体产生事件，局部行为汇成全局行为 | CrossEdgeIM 原文对象包含多机器人、跨组织协作场景 | 一般 MAS 还可能依赖 message identity、sender/receiver、artifact、authority、resource 与 hidden state；普通活动边未必表达这些语义 | Multi-Agent event 和 case 应怎样定义？跨 Agent causality 应记录 control/message/data/authority/resource/epistemic flow 中哪些项？ | 为同一次交互分别建立普通 `(activity)` 与带 actor/artifact 的 `(agent, action, object)` 日志；预先选一个协议查询，比较两种表示能否回答 | 只能登记 behavior discovery/runtime-assurance 研究方向；不能写 EdgeIM 或 CrossEdgeIM 已解决 MAS safety |

枝条状态均为 `PARKED`。DES/形式化枝到 Petri net 正式节点后才评估 Dependency；MAS 枝只有在一个具体 property、event/case 定义和可区分实验出现后，才评估 Research leverage。CrossEdgeIM 的在线增量特征维护是 `PAPER-TEXT`；把它升级成 runtime monitor、violation verdict 或干预机制仍是 `USER-RECONSTRUCTION`，有效性保持 `UNKNOWN`。

## 八步探索闭环

主张（claim）是希望别人接受、且需要证据支撑的判断；证伪条件（falsifier）是出现后会迫使该判断被改写或放弃的结果；证据上限说明当前材料不能支持什么。

| 步 | 固定英文名与首见定义 | 必须产出 | 进入下一步前检查 |
|---|---|---|---|
| 1 | `Observe`（观察）：只记录看见的对象、数字或行为 | 来源、对象、原始记录 | 是否混入了解释？ |
| 2 | `Analogize`（类比）：寻找结构相似的已知问题 | 一张六字段 Transfer Map | 是否写了不同处和类比上限？ |
| 3 | `Abstract`（抽象）：去掉领域名，留下变量、关系和目标 | 输入、状态、输出、优化目标 | 每个符号装什么？ |
| 4 | `Hypothesize`（提出假设）：写可被结果推翻的判断 | 条件、预测、证伪条件 | 哪个结果会迫使我认错？ |
| 5 | `Attack`（攻击假设）：主动找边界、反例和竞争解释 | 最小反例候选、失效条件 | 是否只挑了支持自己的例子？ |
| 6 | `Experiment`（实验）：设计最小区分测试 | 对照、只改变的变量、指标、预注册裁定、成本 | 能否区分至少两个解释，并改变一个决定？ |
| 7 | `Verify`（核验）：核查实现、来源和结果可追溯性 | 原始输出、复跑命令、来源位置 | 观察、机制解释和外推是否分开？ |
| 8 | `Update`（更新）：按证据改写判断和下一步 | 新判断、证据上限、下一实验 | 是否保留失败和意外？ |

固定顺序必须写成：`Observe -> Analogize -> Abstract -> Hypothesize -> Attack -> Experiment -> Verify -> Update`

### 一轮记录模板

本轮的 `Attack / Verify / Update` 另链接 [Evidence audit、Evidence closure 与 Research hooks](./RESEARCH_NOTE_TEMPLATE.md)，不能只填下方摘要。

| 步 | 我的记录 |
|---|---|
| `Observe` | 对象：________；原始位置：________；只观察到：________ |
| `Analogize` | Transfer Map 行号：________；类比上限：________ |
| `Abstract` | 输入：________；状态：________；输出：________；目标：________ |
| `Hypothesize` | 在条件 ________ 下，我预测 ________；证伪条件：________ |
| `Attack` | 最小反例：________；竞争解释：________ |
| `Experiment` | 对照：________；只改：________；测量：________；裁定规则：________；成本：________ |
| `Verify` | 原始输出：________；复跑：________；来源：________；credit：________；异常与负面证据：________ |
| `Update` | 保留：________；改写：________；仍为 UNKNOWN：________；不能外推：________；被改变的决定：________；下一步：________ |

联想可以发散；一旦写成主张，就必须补证伪条件、最小区分实验和证据上限。AI（artificial intelligence，人工智能）可以帮助列候选类比或检查格式，但这些输出不证明学习者能独立迁移、设计实验或更新判断。
