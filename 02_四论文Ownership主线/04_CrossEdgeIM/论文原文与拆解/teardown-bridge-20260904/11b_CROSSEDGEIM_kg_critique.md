Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# CrossEdgeIM 知识图谱提取与批判性分析（B2 独立视角）

**题录**：Xuan Su, Cong Liu (corresponding author), Qingtian Zeng, Jinglin Zhang, Long Cheng. "CrossEdgeIM: An Edge-Based Approach for Interactive Robotic Behavior Model Discovery". IEEE Internet of Things Magazine, Jan. 2026, pp. 55–60（卷/期号页面未印 [需验证]）。DOI 10.1109/MIOT.2025.3625047；Date of Publication 3 Dec 2025；Current Version 22 Jan 2026；专栏 "Edge AI for Internet of Robotic Things" [PDF p.1]。
**体裁**：杂志文，6 页，15 篇参考文献，无定义块/定理/伪代码。主窗标签"作者校样"；但页脚带 IEEE Xplore 下载水印与印刷页码 55–60，更像 Xplore 终版 [PDF p.1 页脚][需验证]。
**作者注**：Faming Lu 不在本文 5 位作者之列 [PDF p.1]，是参考文献 [8][11] 的合著者 [PDF p.6]。
**页码约定**：[PDF p.N]，N=1..6 对应印刷页 55–60。
**层级**：EVIDENCE。只读原件（逐页 Read）+ pdftotext 定位；未读 10_/11_/12_ 拆解；不含 EdgeIM 机制复原。

---

# 第一部分：知识图谱提取

## 1. 核心概念及其关系

| # | 概念 | 论文定义/角色 | 出处 |
|---|---|---|---|
| C1 | CrossEdgeIM | 三层架构 活动节点→组织节点→中心节点；"robotic activities act as the smallest computational units" | [PDF p.1] |
| C2 | Activity Node | 部署在机器人/本地控制器的边缘设备，"responsible for monitoring a specific robotic task"；在线维护 DFR、StartSet、EndSet；时间戳相同触发 "concurrency-marking" 双向计数 | [PDF p.2] |
| C3 | 增量包 ΔDFR/ΔStartSet/ΔEndSet | 异步发送；内容 "activity pairs with count changes, the updated start and end activity sets, the case identifier, and the event timestamp range"；大小 e+\|ΔStart\|+\|ΔEnd\| | [PDF p.3][PDF p.4] |
| C4 | Organization Node | III.A "runs on a fog-level server"，III.C "deployed at the edge-computing layer"（fog/edge 混用 [⚠️矛盾-轻]）；三步聚合：同活动对计数累加；起始集合并后删去 "appears as a target" 者；结束集合并后删去 "appears as a source" 者 | [PDF p.2][PDF p.3] |
| C5 | Org-DFG | 组织级三元组构造的 DFG，馈入 IM | [PDF p.3] |
| C6 | Inductive Miner [3] | 双重角色：Stage 2 内部构件 + 实验唯一基线（集中式） | [PDF p.2][PDF p.3][PDF p.5] |
| C7 | Central Node | 云层；只收 PNML；合并两步：source→τ_split、τ_join→sink；各组织网 start place 接 τ_split、end place 接 τ_join，"ensuring that all organization models are executed in parallel" | [PDF p.4][PDF p.5] |
| C8 | 复杂度断言 | 聚合 O(e)；"IM on a sparse DFG is O(m log m)"；合并 ≈O(K) | [PDF p.4][PDF p.5] |
| C9 | F-measure [14] | 式(1) fitness/precision 调和平均 | [PDF p.5] |
| C10 | Complexity [15] | 式(2) ECaM/ECyM 调和平均，"measuring the interpretability" | [PDF p.5] |
| C11 | 四个实验日志 | "event logs generated from simulated robotic interaction scenarios"；脚注 1 github.com/Lihuiling12/TASE.git；Table I 列 #Dep. 正文解释为 "number of departments" | [PDF p.4][PDF p.5] |
| C12 | EdgeMiner [6][7] / EdgeIM [8] | 原句："EdgeMiner [6], [7] and EdgeIM [8] construct local features at edge nodes and aggregate them centrally to produce a global process model, thereby reducing computation and communication overhead. However, such approaches mainly target single-organization IoT environments and lack technical designs for interactive robotic behavior discovery." [8] 全文仅此一处 | [PDF p.1] |

关系（论文明示，箭头=类型）：
- C1 part-of C2/C4/C7 = Stage 1/2/3 [PDF p.2]；Fig. 1 却标 Phase 1/2/3 并称活动节点为 "Edge Node" [PDF p.3][⚠️矛盾-轻]
- C2 produces C3；C4 consumes C3 → produces C5；C6 uses C5 → 组织级 Petri 网 [PDF p.3]
- C7 consumes 组织级 Petri 网（"only once"）→ "raw merged model" [PDF p.2][PDF p.5]
- C1 evaluated-by C9、C10；compared-with 仅 C6 [PDF p.5]
- C12 motivates C1（"single-organization" 局限），但不 compared-with [PDF p.1]
- C11 与文献 [9]（IEEE TASE 跨科室医疗）共享 department 术语与仓库名 [推断][PDF p.5][PDF p.6]

## 2. 理论框架图（文字描述，含推断）

数据流（Fig. 1 + III.B–D）：
1. 事件源→活动节点。假设 "event log remain locally distributed across edge nodes during system operation" [PDF p.2]；实验中 "each node processes only the events corresponding to its specific robotic action" [PDF p.5]。[推断] 活动节点 = 单一活动类型的计数器。
2. 节点内：新事件与 "the preceding event in the same case" 比时间戳，晚则 (prev,cur)+1，同则双向 +1；首事件入 StartSet、末事件入 EndSet；"online without waiting for case completion" [PDF p.2][PDF p.3]。[推断] 前一事件属于别的活动即别的节点，其活动名/时间戳如何到达本节点，文中无说明；不等 case 完成如何判定"末事件"也无说明。
3. 活动节点→组织节点：异步增量包，携带 case id 与时间戳范围 [PDF p.3]。
4. 组织节点：三步聚合→Org-DFG→IM→组织级 Petri 网 [PDF p.3]。
5. 组织节点→中心节点：PNML，"only once" [PDF p.5]。
6. 中心节点：source→τ_split→{各组织网}→τ_join→sink [PDF p.4]。[推断] 全局模型 = 各组织模型的纯 AND 组合，不含组织间顺序/消息约束；"cross-organization robotic collaboration" [PDF p.2] 在模型中只体现为"并行"。

框架里没有的东西 [推断]：无中心/组织→活动节点的回流；无重挖/重合并触发条件；同一 case 相邻两事件分属两组织时该 DFR 边归谁，无说明 [PDF p.3]。

## 3. 关键数据表（逐数值解释）

**Table I** [PDF p.4]（#Dep. = "number of departments" [PDF p.5]），末列为本文计算：

| 日志 | #Case | #Event | #Task | #Dep. | Event/Case |
|---|---|---|---|---|---|
| EM_Log | 18909 | 605088 | 32 | 6 | 32.000（整除，=#Task） |
| ID_Log | 50427 | 1277247 | 30 | 6 | 25.329 |
| FP_Log | 37816 | 945400 | 27 | 4 | 25.000（整除） |
| SD_Log | 48320 | 1111360 | 23 | 4 | 23.000（整除，=#Task） |

解读：EM/SD 每 case 事件数恰等于任务数、FP 恰为整数，与"每条迹固定执行各活动一次"的生成方式一致 [推断]；此类日志缺少 XOR 跳过/循环带来的长度变化，而 Intro 把 "parallel, choice, and loop" 列为第三挑战 [PDF p.1]。ID_Log 是唯一非整除者。

**Fig. 2（IM）/ Fig. 3（CrossEdgeIM）图内数字** [图读数]，八个子图均可辨认 [PDF p.4][PDF p.5]：

| 日志 | 方法 | Fitness | Precision | F-measure | ECaM | ECyM | Complexity |
|---|---|---|---|---|---|---|---|
| EM | IM | 1 | 0.1322 | 0.2335 | 55 | 10004 | 109.3985 |
| EM | CrossEdgeIM | 0.9697 | 0.2289 | 0.3704 | 45 | 10001 | 89.5969 |
| FP | IM | 1 | 0.233 | 0.3779 | 41 | 10008 | 81.6654 |
| FP | CrossEdgeIM | 0.9434 | 0.3916 | 0.5535 | 36 | 10002 | 71.7418 |
| ID | IM | 1 | 0.247 | 0.3962 | 44 | 10006 | 87.6147 |
| ID | CrossEdgeIM | 1 | 0.3986 | 0.5700 | 37 | 10005 | 73.7273 |
| SD | IM | 1 | 0.3207 | 0.4857 | 36 | 10009 | 71.7420 |
| SD | CrossEdgeIM | 0.9787 | 0.4603 | 0.6261 | 32 | 10001 | 63.7959 |

复算：8 组 F-measure 与 Complexity 均可由式(1)(2)从图内 fitness/precision、ECaM/ECyM 复现到小数第 4 位（逐组代入核过），图内自洽。

正文数字逐条对照：
- "most notable improvement in SD_Log (0.6261 vs 0.4857)" [PDF p.5]：SD 只是绝对值最高。绝对增量 EM +0.137、FP +0.176、ID +0.174、SD +0.140；相对增幅 EM +58.6%、FP +46.5%、ID +43.9%、SD +28.9%，SD 增幅最小 [⚠️矛盾]。
- "complexity scores 12-17% lower than IM" [PDF p.6]：本文算得 EM −18.1%、FP −12.2%、ID −15.9%、SD −11.1%，两端都落在 12–17% 之外 [⚠️矛盾]。
- "Fitness values are slightly lower than IM's perfect score of 1" [PDF p.6]：ID_Log 上 CrossEdgeIM fitness 亦为 1（Fig. 3c）[图读数]，该句对 3/4 成立。
- "an average of 8.2 nodes per organization, compared to Inductive Miner's denser average of 11.7 nodes" [PDF p.6]：图内无此统计；IM 输出不按组织划分，"per organization" 对 IM 如何定义未说明 [需验证]。
- ECyM 八值全在 10001–10009 [图读数]：远大于 ECaM（32–55），调和平均退化为 ≈2×ECaM（2×55=110≈109.40；2×32=64≈63.80）。[推断] ECyM 疑似被 ≈10000 的上限截断 [需验证]；Complexity 实际只由 ECaM 决定，"EcaM and EcyM metrics further confirm ... consistently lower values" [PDF p.6] 中 ECyM 那半句无信息量。
- O(e)、O(m log m)、O(K) [PDF p.4][PDF p.5]：无推导、无引用、无实测；O(m log m) 与 IM 常见复杂度分析不一致 [需验证]。
- 图形形态 [图读数]：Fig. 2 四图皆为一个起点扇出 20–30 条近乎单活动的并行分支再汇合；Fig. 3 四图为 τ 分叉后 4–6 条各含 4–8 活动的顺序分支。节点标签细字未逐一辨认 [图读数不清]。

## 4. 引用网络（TOP 5 + 引用方式）

15 篇文献，[8]–[13] 六篇含本文作者 Cong Liu / Qingtian Zeng（40% 自引）[PDF p.6]。

| 序 | 文献 | 被引位置 | 方式 | 判断 |
|---|---|---|---|---|
| 1 | [3] Leemans IM 2013 | p.1 Intro、p.2 Related Work；III.C "the IM algorithm"、IV "Inductive Miner" 处未再标号 | 背景+方法沿用+唯一基线 | 同一算法既是零件又是唯一对手 [PDF p.1][PDF p.3][PDF p.5] |
| 2 | [6][7] EdgeMiner/EdgeAlpha | p.1、p.2 | 背景+借口（"single-organization"） | 最接近的分布式竞品，实验未对比 [PDF p.1][PDF p.2][PDF p.5] |
| 3 | [8] EdgeIM（本组前作） | 仅 p.1 一处（原句见 C12） | 自引+借口 | 与本文 Stage 1/2 的机制差异全文未陈述；见 EdgeIM 原文 §IV.B，用户自读 [PDF p.1] |
| 4 | [9] Liu TASE 2023 跨科室 | p.2 | 背景 | 脚注仓库名 "TASE" + "#Dep."/"departments" 指向其数据谱系 [推断][需验证][PDF p.5][PDF p.6]；作为跨组织发现方法本应入基线 |
| 5 | [14] F-measure / [15] 复杂度 | p.5 | 方法沿用（指标） | 出处清楚；ECyM 退化见 §3 [PDF p.5] |

[4][5] 在 p.1 以 "As indicated in [4], [5]" 为三大挑战背书，在 p.2 又分别被批 "trade-offs"/"accuracy loss"——借口型引用 [PDF p.1][PDF p.2]。[10]–[13] 各只在 Related Work 出现一次，均为背景 [PDF p.2]。

---

# 第二部分：批判性分析

## 1. 方法论审视

(a) 单基线的含义。唯一对手是完整日志上的集中式 IM [PDF p.5]，而 CrossEdgeIM 额外拿到基线没有的输入——按组织/活动的划分（"partitioned into robotic organizational nodes and further into activity nodes" [PDF p.5]）。F-measure 提升可以完全来自"按组织切分、分别挖掘、AND 组合"的信息优势，与边缘架构无关 [推断]。缺的公平基线：(i) 单机跑"按组织投影+IM+并联"；(ii) 被引的 [6][7][9]。二者皆无 [PDF p.5]。

(b) 模拟数据。称 "generated from simulated robotic interaction scenarios" [PDF p.5]，生成器、场景、活动语义一概未述；"#Dep." 被正文解释为 departments [PDF p.5]、仓库名 TASE.git [PDF p.5]、文献 [9] 刊于 IEEE TASE [PDF p.6]，三者吻合 [推断]。若属实，"机器人"是对既有跨部门日志的重新命名 [需验证，无网络未能打开仓库]。另 §一.3 显示 EM/SD 每 case 事件数恰等任务数 [PDF p.4]，日志本身缺 choice/loop 变化，与 Intro 第三挑战 [PDF p.1] 脱节。

(c) 无通信量/时延实测。摘要、III.C、III.D 反复主张 "reduces communication overhead"、"scalability" [PDF p.1][PDF p.3][PDF p.5]，证据只有三个未推导的复杂度记号和 "substantially smaller" 的定性句 [PDF p.4]；实验只测 F-measure 与 Complexity [PDF p.5]，无字节数、包数、延迟、随 K 增长曲线、硬件/网络配置。"scalability" 未被任何实验触及。

(d) τ_split/τ_join 的结构含义。合并规则是把每个组织网的 start/end place 接到一对不可见变迁 [PDF p.4]，全局模型 = 各组织模型的纯 AND 组合。后果：任何跨组织顺序都无法表达，跨组织交错"全部放行"；Threats 自认 "interactions between organizations are represented in an implicit form" [PDF p.6]，按规则更准确的说法是"未表示"；这一步的技术含量是常数时间图拼接（自述 O(K) [PDF p.5]），却是标题 "Cross" 的全部落点。

(e) 起始/结束集剪枝的正确性。"any activity that appears as a target in the aggregated directly-follows relations is removed" [PDF p.3]。反例：迹 ⟨A,B⟩ 与 ⟨B,A⟩ 并存时 A、B 既是起始又是 target，StartSet 被清空；回环到首活动的流程同理。规则把"真起始"定义为"从不作后继"，与循环/多起始结构不相容 [推断，纯逻辑]。

(f) 活动节点的 DFR 来源。III.B 要求比较新事件与 "the preceding event in the same case" [PDF p.2]，但每节点只处理自己那一种活动 [PDF p.5]；前一事件的活动名与时间戳如何到达本节点，全文未交代 [PDF p.2][PDF p.3]。"末事件入 EndSet" 与 "online without waiting for case completion" [PDF p.3] 互相牵制。

## 2. 逻辑审视

(a) 主张—证据缺口：
- "improves the accuracy of behavior discovery" [PDF p.1]：证据是 precision 升、fitness 降 [图读数]；"accuracy" 未定义。
- "substantial gains in ... scalability" [PDF p.1]：无规模实验 [PDF p.5]。
- "most notable improvement in SD_Log" [PDF p.5]、"12-17% lower" [PDF p.6]：与自家图内数字不符 [⚠️矛盾，见 §一.3]。
- "rapid detection of local process changes ... improving the responsiveness" [PDF p.3] 对 "transmits its Petri net model only once" [PDF p.5]：增量到组织节点后何时重挖、何时重合并无机制；"只发一次"意味着全局模型不随流更新，"responsiveness" 落空 [⚠️矛盾]。
- Fitness<1 归因 "minor uncaptured cross-organization traces" [PDF p.6]：AND 组合允许全部交错，理论上不应比按组织投影的模型少覆盖；未捕获的是什么，无分析 [需验证]。

(b) "privacy preservation" 靠什么支撑：两句架构性陈述——活动节点只发三元组 "instead of raw event logs, thereby ... preserving local data privacy" [PDF p.3]；"no raw event log leaves the organizational boundaries, only abstracted process models" [PDF p.5]。无威胁模型、无攻击者假设、无度量，也未与被引的差分隐私 [5]、SMPC [11]、区块链 [13] 作对照 [PDF p.2]。增量包却携带 "the case identifier, and the event timestamp range" [PDF p.3]，组织内 case 级信息并未抽象。隐私主张是"数据少传"的同义反复 [推断]。

(c) 基线呈现。Fig. 2 中 IM 四图皆近乎全并行扇形 [图读数][PDF p.4]；IM 参数（噪声阈值、变体）、同时间戳事件在集中式日志中的处理均未说明 [PDF p.5]。基线是否被合理配置无法判断 [需验证]。

## 3. 贡献审视

原文自述（摘要+结论 [PDF p.1][PDF p.6]）逐条对证据：

| 自述贡献 | 证据状况 |
|---|---|
| 三层边缘架构 | 有描述 [PDF p.2–p.5]；相对 [6][7][8] 的增量是"组织层"+AND 合并；与 [8] 的差异未自述 [PDF p.1]，见 EdgeIM 原文 §IV.B，用户自读 |
| "structured model merging" | K 个网并联，O(K) [PDF p.4][PDF p.5]，无跨组织约束 |
| 降低通信成本 | 只有记号 [PDF p.4]，无测量 |
| 增强隐私 | 只有架构性断言 [PDF p.3][PDF p.5] |
| 提高准确性/可解释性 | 有数 [图读数]；但基线单一且输入不对等（§二.1a），Complexity 退化为 ECaM（§一.3） |
| 可扩展性 | 无实验 |
| "interactive robotic behavior" | 方法与数据里无任何机器人特有成分（无传感器/动作/多机交互建模）；Threats 自认 "does not yet explicitly capture the collaborative relations among multiple robots" [PDF p.6] |

判断：能站住的贡献是"把组织维度显式引入边缘式过程发现并给出一个最简合并"；其余主张停留在陈述层。标题 "Interactive Robotic" 与正文内容的距离是最大的贡献层面问题 [推断]。

## 4. 可复现性

- 代码：无 CrossEdgeIM 代码链接；只说 "implemented ... in the open-source process mining tool PM4Py and deployed it in Docker containers" [PDF p.5]。
- 数据：脚注 1 github.com/Lihuiling12/TASE.git [PDF p.5]，唯一可追溯材料；内容未核 [需验证]。
- 参数：IM 变体/噪声阈值、每组织活动节点数、活动→组织划分表、增量发送周期、PNML 合并的 place 命名，全缺 [PDF p.3–p.5]。
- 指标实现：ECaM/ECyM 计算工具与 ≈10000 上限来源未说明 [PDF p.5][需验证]。
- 硬件/网络：无。形式化：无定义、伪代码、定理；Fig. 1 与正文术语不一致 [PDF p.2][PDF p.3]。
- 结论：按文中信息无法重跑；方法侧至少四处未定义行为需自行补全（§二.1 e、f；重挖触发；跨组织边归属）。

## 5. 总评（审稿人视角）

一句话定位：把"按组织切分 + 各自 IM + 不可见变迁并联"包装为"面向交互机器人的边缘式跨组织行为发现"的杂志短文；三层数据流描述可读，但每一项非精度主张（通信、隐私、可扩展、机器人相关性）无实验证据，精度主张建立在单一且输入不对等的基线上，且两处正文数字与自家图不符（§一.3）。

判断 [推断]：按研究论文标准属"大修"偏"拒"——需补公平基线（单机投影+并联、[6]/[9]）、通信与时延实测、隐私威胁模型，并修正 SD_Log 与 12–17% 两处陈述；按杂志专栏"概念介绍"体裁看可接受，但应删去未验证的强主张。对本项目的可用价值：III.B–D 的合并规则可作"跨组织合并最简基线"引用；Fig. 2/3 的 16 组数字可直接复用于后续对比。

[全部章节在时间盒内完成]
