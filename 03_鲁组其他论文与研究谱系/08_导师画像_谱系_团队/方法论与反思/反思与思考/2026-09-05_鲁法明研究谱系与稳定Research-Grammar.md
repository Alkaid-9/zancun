# 鲁法明研究谱系与稳定 Research Grammar

**记录日期**：2026-09-05

**来源类型**：用户对鲁法明本人近年产出、山东科技大学 Petri 网/流程挖掘谱系，以及曾庆田—刘聪—苏轩—程龙公开合作网络的综合研究笔记

**当前状态**：`SYNTHESIS-PENDING-CITATION-AUDIT`

**用途**：保存完整研究判断、谱系结构、稳定研究动作、公开证据与推断边界，并服务 EdgeIM 学习、鲁组理解、研究选题和面试准备

**证据边界**：本文忠实整理本次用户输入。论文作者、日期、指标、职务、项目资助、官网表述及原话，尚未在本文中逐条绑定一手 URL、页面位置或 PDF 页码；引用或对外使用前，必须回到 `MAS_Safety_Project` 的现有 teardown/画像/原文资产或官方网站重新核验。

## 0. 一句话总判断

> 鲁法明老师并没有从 Petri 网/形式化方法“转行”去做 AI。更像是一直守着一个稳定内核：复杂系统的“结构化建模 -> 行为/知识发现 -> 分析验证 -> 决策/优化”，然后不断把新技术和新的真实系统接入这个内核。

因此，Petri 网、流程挖掘、并发程序、因果/根因分析、EdgeIM、矿山 AI、时序大模型和多模态并不是必然割裂的项目集合。更有解释力的观察单位是它们共享的研究动作。

用户输入还记录了鲁老师过去的一项公开表态：Petri 网相对小众，但科研方向需要保持相对稳定；可以借鉴“时髦的科技”，让传统方向获得新的用武之地，而不是抛弃过去。该表述是理解下述路径的重要候选证据，但原始出处和逐字引文仍须核验。

## 1. 首先分开“鲁法明本人”和“公开合作网络”

这一区分是所有判断的前提。不能把长期合作者、同门谱系或共同作者的全部产出都称为“鲁老师自己的组正在做”。

### 1.1 鲁法明本人

用户输入记录的当前公开身份包括：山东科技大学计算机学院教授、博士生导师、公共安全与应急管理研究院副院长。官方当前方向被概括为应急决策支持、人工智能、知识图谱与大模型、Petri 网理论与应用，成果介绍还包括 BPM。

这些身份和方向属于可核验的公开事实候选；本文尚未附官网 URL 与抓取日期。

### 1.2 长期公开合作谱系

更准确的图是：

\[
\text{曾庆田}
\leftrightarrow
\text{鲁法明}
\leftrightarrow
\text{刘聪}
\leftrightarrow
\text{苏轩}
\leftrightarrow
\text{程龙}
\]

它表示长期公开合作谱系或研究网络，而不是一张实验室组织架构图。

### 1.3 署名边界

本次用户输入给出的区分如下，需在引用前逐篇核验作者表：

| 工作 | 鲁法明署名状态 | 本文中的归属方式 |
|---|---|---|
| EdgeIM | 有鲁法明 | 鲁本人产出 + 合作网络节点 |
| 2025 healthcare duplicate-task discovery | 有鲁法明 | 鲁本人产出 + 合作网络节点 |
| CrossEdgeIM | 无鲁法明 | 同一公开合作谱系，不称鲁本人论文 |
| 2026 sigRank event-log sampling | 无鲁法明 | 合作网络发展，不称鲁本人论文 |
| 2026 IM imprecise-subprocess optimization | 无鲁法明 | 合作网络发展，不称鲁本人论文 |
| 2026 causal process anomaly RCA | 无鲁法明 | 合作网络发展，不称鲁本人论文 |

用户输入还给出作者关系示例：EdgeIM 作者包含苏轩、刘聪、鲁法明、程龙、曾庆田等；CrossEdgeIM 作者为苏轩、刘聪、曾庆田、张景林、程龙。这里的姓名和次序仍须以论文原文为准。

## 2. 截至 2026-09 的四条可见轨道

| 轨道 | 2025-2026 代表工作候选 | 真正处理的问题 |
|---|---|---|
| A. Petri 网 / 因果知识 / RCA | 2026 JAS 多元时序知识挖掘与根因分析 | 从时间序列恢复 AND/OR、协同效应、因果与时间结构 |
| B. 并发程序分析 / 形式化 | MHP、UAF、deadlock detection and replay | 更准确地表示并发因果关系并验证真实 bug |
| C. Process Mining / BPM | EdgeIM、医疗 duplicate-task discovery | 从大规模、复杂或脏事件日志中恢复高质量流程模型 |
| D. AI / 大模型 / 多模态工业智能 | 不规则时序 + LLM、精煤灰分 LLM、多模态、煤岩识别、跨语言情感 | 把新 representation 引入真实工业和安全数据 |

四条轨道不是一个项目，但共享一组很稳定的认知动作。

## 3. 轨道 A：Petri 网从行为结构走向知识、因果与根因

### 3.1 候选演化链

用户输入整理出的论文演化是：

1. 2022：synergy-effect-incorporated fuzzy Petri net；
2. 2024：Synergy-incorporated Bayesian Petri Net；
3. 2026：`A New Knowledge Mining and Root Cause Analysis Methodology for Multivariate Time Series`。

2024 工作的候选增量是把 Petri 网与概率推理结合，显式处理 AND/OR relation 和 synergy effect。用户输入称鲁老师官方主页把 2022 和 2024 两篇都列为代表成果。

2026 工作的候选作者是 Xiaoliang Wang、Faming Lu、MengChu Zhou、Qingtian Zeng，鲁法明和孟初周为通讯作者。其方法被概括为融合 Petri net 与 Bayesian network 的 synergy-incorporated Bayesian time Petri net，从多元时序中挖掘 temporal causal structure、AND/OR relations 和 synergy effect，再执行 root-cause analysis。

用户输入记录的实验场景是太阳能板质量异常与 Tennessee-Eastman process；前一场景据称比对比 RCA 方法高出超过 11% 准确率。该数字在查到表格、指标定义和对比设置前不得对外引用。

### 3.2 研究动作的变化

```text
Petri Net
“行为结构是什么？”
        -> Fuzzy PN
“关系有不确定性怎么办？”
        -> Bayesian PN
“能不能进行概率推理？”
        -> Bayesian Time PN
“能否从时序数据挖知识、解释异常并找到根因？”
```

这条线更适合被理解为向 `structured causal knowledge representation + reasoning` 发展，而不只是“继续使用 Petri 网发论文”。

### 3.3 与自动化/控制的连接

用户输入指出，2026 工作发表在 IEEE/CAA Journal of Automatica Sinica；共同作者 MengChu Zhou 的公开研究背景又连接 Petri nets、automation、robotics、IoT/edge computing。这个连接可以解释为什么该路线具有自动化与控制的气质，但不能仅凭 venue 或合作者背景推导论文机制。

## 4. 轨道 B：并发程序形式化分析持续发展

AI 论文增加并不等于 formal methods 被放弃。用户输入列出了三项候选工作。

### 4.1 Segment-Based May-Happen-in-Parallel Analysis for C Programs（2025）

候选方法不是用粗粒度标签断言两个语句“可能并发”，而是构造 Segmented Thread-sensitive Control Flow Graph（STCFG），把语句划分为 segment，将 fork/join、锁等上下文显式编码，再判断 Happens-Before 和 conflict relations，目标是同时改善 precision 与 efficiency。

### 4.2 Improved Petri Net + Value Flow Graph 的 UAF 检测（2025）

候选结构是：

\[
\text{程序}
\rightarrow
\text{segmented Petri net}
+
\text{value-flow graph}
\]

Petri 网承担控制流与并发因果约束，value-flow graph 承担值传播和 UAF 触发条件，再检查约束兼容性。

这说明 representation 不是越统一越好；不同图可以分别保留控制与数据依赖，再在验证时组合。

### 4.3 Deadlock Detection and Replay（2026-06）

候选工作名称是 `Deadlock Detection and Replay of Multi-Thread Programs Based on Refined Segmentation and Lock Graphs`。用户输入将其概括为：从运行轨迹提取更细的 causal dependence 和 lock information，以降低 false positive；发现潜在死锁后，再生成 deterministic scheduling 执行 replay，确认死锁是否真实可触发。

### 4.4 这条线的元动作

```text
Petri-net theory
-> reachability / unfolding
-> deadlock analysis
-> program running traces
-> data race / UAF / MHP / deadlock
-> detect
-> replay / reproduce
```

它把 `representation -> verification` 推进到 externally checkable evidence。

与 EdgeIM 并排看时：

- EdgeIM 问：execution log 中哪些结构信息值得保留？
- 并发程序线问：execution trace 中哪些 causal/locking structure 必须显式表达，否则会误判？

二者领域不同，但都可以被看作 `recover the right structure from behavior`。

## 5. 轨道 C：Process Mining 处理复杂、分布式、大规模和脏日志

### 5.1 早期主线

用户输入列出的代表性早期成果候选包括：

- 2014：`Hierarchy Modeling and Formal Verification of Emergency Treatment Processes`；
- 2015：跨部门 collaborative process Petri-net modeling/verification；
- 2015：并行 heuristic process mining；
- 2015：case cluster + synchronization core process discovery；
- 2016：synchronization-core-based process discovery；
- 2016：BPMN model fusion。

用户输入称这些工作目前仍在鲁老师官方主页代表成果中。需要在正式引用时保存当前页面快照与访问日期。

### 5.2 学术 genealogy

鲁法明博士论文候选题目为：

> 《业务流程的分层建模验证与挖掘方法研究》

用户输入记录：导师曾庆田，2015 年获山东省优秀博士论文。曾庆田官方页面也记录了导师关系，并记录刘聪硕士论文为《跨组织业务流程挖掘及其隐私保护方法研究》。这些信息构成以下 genealogy 的候选公开证据：

```text
曾庆田：Petri Net / workflow / process mining
          |
          +-- 鲁法明：分层建模、验证、挖掘
          |
          +-- 刘聪：跨组织 process mining、privacy、discovery
```

后续多条线又通过合著重新交叉。

### 5.3 2024：Sampling Business Process Event Logs with Guarantees

用户输入将这项苏轩、刘聪、曾庆田等人的工作概括为：把 DFR equivalence 当作 sampling quality 的结构保证，并提出 7 种 sampling strategies。

应核验的关键点包括：DFR equivalence 的正式定义、七种策略的分类、保证成立的前提，以及它保存的是 support、frequency 还是其他统计量。

### 5.4 2025：EdgeIM

候选流程是：

```text
feature-preserving sampling
-> edge local feature extraction
-> central global DFG
-> Inductive Miner
```

它把 structural feature preservation 搬到 distributed edge / IoT process discovery。这里必须继续保持一个已知边界：论文 Algorithm 1 不是 fixed-K sampler；本地 fixed-K greedy DFG coverage 是 surrogate，不能混称论文算法。

### 5.5 2025：Healthcare duplicate-task discovery

用户输入中的题名是 `Enhancing Healthcare Process Model Discovery Through Duplicate Task Identification`。候选问题是医疗日志中的 duplicate tasks 会干扰流程发现，因此先识别或 relabel duplicate task，再构造 DFG，并用 IM 生成 Petri net。

### 5.6 稳定的问题形式

这一组工作不像是在反复发明“新的 miner”，更像持续追问：

\[
\boxed{
\text{真实日志具有什么特殊结构，导致标准 process discovery 失效？}
}
\]

然后分别处理：

- 大日志 -> sampling；
- distributed data -> EdgeIM；
- duplicate tasks -> preprocessing/relabeling；
- IM 局部 overgeneralization -> subprocess optimization。

## 6. 轨道 D：AI、LLM 与多模态工业智能明显加速

### 6.1 Irregularly Sampled Time Series + Language Models（2026-03）

候选题名为 `Irregularly Sampled Time Series Classification via Fusing Language Models and Multi-Channel Image Representations`。

用户输入概括的 representation pipeline 是：

\[
\text{time series}
\rightarrow
\text{text prompt}
\rightarrow
\text{LLM embedding}
\]

同时使用 message passing 补缺失数据，把时序转换成 multi-channel image，最后进行 text/image multimodal alignment。用户输入称鲁法明为通讯作者。

### 6.2 大语言模型驱动的多模态精煤灰分预测（2026-07）

这项工作把上述思路带进真实煤炭生产：

\[
\text{选煤工艺时序}
\rightarrow
\text{LLM + domain-knowledge structured text}
\]

候选方法还包括 message passing、multi-channel line images、multi-head attention multimodal fusion 和 physical-constraint loss。

用户输入记录：真实重介质选煤数据上，RMSE 比次优方法低 3.1%；工作由新一代人工智能国家科技重大专项和国家自然科学基金支持。指标与资助信息在逐项核验前只作为候选事实保存。

候选演化是：

```text
2026-03：LLM 能否帮助表示 irregular time series？
        ->
2026-07：进入真实选煤系统，并加入 domain knowledge + physical constraint
```

这表现为从 `LLM as feature extractor` 向 `domain-informed industrial AI` 发展。

### 6.3 同期其他 AI 支线

用户输入列出：

- 2026 SiamWT-CRNet：真实放顶煤场景的动态煤岩识别，多种 wavelet representation + Siamese/cross-domain feature fusion；
- 2026-08 advance online 的 cross-lingual speech emotion recognition：multi-wavelet augmentation + language-invariant emotion feature disentanglement；
- 2025 autonomous-vehicle collaborative perception；
- 2025 Dynamic Global Query Fusion：cross-layer persistent global context 增强 CNN。

这些条目的作者、正式题名、出版状态及鲁法明署名位置均需逐条核验。

## 7. 公开合作网络的研究簇，而不是组织架构

用户输入指出，山东科技大学“计算机模型与算法研究所”长期公开列出三类方向：Petri 网理论及应用、软件建模与分析、信息资源整合与共享；鲁法明是公开成员之一。

从近两年公开合著与产出，可以形成以下**分析图**：

```text
                         曾庆田
                 Petri Net / Process Mining
                            |
          +-----------------+-----------------+
          |                 |                 |
       鲁法明              刘聪             其他成员
          |              NOVA / BPM
          |                 |
   +------+------+          +-----------+
   |      |      |          |           |
程序分析 AI/工业 BPM      苏轩/采样    程龙/Edge
   |      |      |          |           |
 MHP    LLM   EdgeIM      sigRank      distributed
 UAF    时序   医疗PM     CrossEdgeIM  systems
deadlock 煤矿                 |
   |      |              causal PM / IM优化
包云霞  林泽东/李子辰
原桂远  刘毅……
```

该图只表示公开论文 coauthorship 抽出的研究簇，不表示学生归属、行政关系或实验室内部组织。

## 8. 2026 年合作网络的三个明显节点

### 8.1 sigRank：从 feature occurrence 到 significance + ratio

用户输入将 sigRank 与 EdgeIM 区分为：

- EdgeIM：顺序扫描，出现新结构特征时保留；
- sigRank：为 trace 计算 significance，显式输入 sampling ratio，选择高价值 traces，在效率和 sample-log quality 之间权衡。

用户输入记录其使用 12 个真实日志并提供 ProM 实现。

候选谱系是：

```text
LogRank / ranking sampling
        |
        +-- 2024 DFR-equivalence sampling
        |
        +-- EdgeIM 2025
        |      one-pass feature preservation
        |
        +-- sigRank 2026
               significance + sampling ratio
```

这个谱系也解释了 fixed-K 误解为何不是完全随机：EdgeIM 本身没有 fixed K，但整个合作网络确实存在预算/比例型 sampling formulation。二者必须区分，而后可以横向比较。

### 8.2 Enhancing Process Discovery by Optimizing Imprecise Sub-processes（2026）

候选方法不是推翻整个 IM，而是定位 overgeneralization 导致低 precision 的局部 subprocess/sublog，仅在局部执行 frequency filtering 和重新 discovery，再选择 fitness/precision 最好的 candidate。

用户输入记录：相对 IMi 的平均 F-measure 绝对提升为 0.173。该数字必须回到表格与统计口径核验。

它体现一个可迁移 operator：

> 不推翻整个系统，只修 residual bad region。

### 8.3 Causal inference for process-performance anomaly RCA（2026）

候选题名为 `Detecting Root Causes for Process Performance Anomalies Using Causal Inference`。

用户输入概括的动作是：

```text
event log
-> contextual factors
-> causal hypotheses
-> traceability
-> meta-learning causal inference
-> root cause
```

这与鲁法明本人 `Bayesian Time Petri Net -> multivariate time-series RCA` 的路线在 causal/root-cause 层面从不同方向靠近。

## 9. 二十年脉络的压缩树

```text
                         Petri Net
                    离散行为结构
                           |
             +-------------+-------------+
             |                           |
      Business Process                 Program
             |                       Concurrency
             |                           |
      建模 / 验证 / 挖掘          reachability / unfolding
             |                           |
   hierarchy / cross-org         race / deadlock / UAF
             |                           |
             |                         replay
             |
        Process Mining
             |
     +-------+----------------+
     |       |                |
  sampling complex logs    distributed
     |       |                |
     |   duplicate task     EdgeIM
     |   IM precision         |
     |                        v
     |                    CrossEdgeIM*
     |
     +----------------+
                      |
              knowledge / reasoning
                      |
                fuzzy Petri net
                      v
               Bayesian Petri net
                      v
          temporal knowledge + RCA
                      |
              +-------+-------+
              |               |
        industrial AI        LLM
              |               |
         mine/safety     text embedding
         perception      multimodal TS
              |               |
              +---- domain/physics ---- ?

* CrossEdgeIM 属于同一公开合作谱系，但不是鲁法明署名论文。
```

## 10. 真正稳定的内核不是“Petri 网”三个字

如果只按技术名分类，会看到 Petri net、CNN、LLM、wavelet、process mining 等多个方向。上抽一层后，稳定结构更清楚：

\[
\boxed{
\text{复杂系统产生数据}
\rightarrow
\text{选择合适 representation}
\rightarrow
\text{恢复结构/关系}
\rightarrow
\text{分析、验证或预测}
\rightarrow
\text{服务真实决策}
}
\]

### 10.1 各领域的重新具体化

**应急流程**

```text
事件/业务行为
-> Petri net
-> formal verification
```

**并发程序**

```text
running trace / code
-> segmented graph / Petri net
-> causality
-> bug detection / replay
```

**Process mining**

```text
event log
-> DFR / DFG
-> process model
-> discovery / conformance
```

**Root-cause analysis**

```text
multivariate time series
-> Bayesian time Petri net
-> causal structure
-> root causes
```

**近期工业 AI**

```text
irregular industrial time series
-> LLM text embedding + image representation
-> multimodal prediction
-> physical/domain constraint
```

共同动作可以写成：

> representation -> structure -> downstream reasoning。

它与 `Execution -> Structure -> Intervention` Research Operator 直接吻合，但每个领域中的 observables、结构关系、sufficient representation 和 intervention 都必须重新审计。

## 11. 为什么会形成这条路径

必须区分公开证据和我们的解释。

### 11.1 公开证据候选一：有意保留学术惯性

用户输入所述鲁老师公开表态支持以下判断：坚持相对固定方向，新技术应让传统方向获得新用途，而不是因流行而抛弃旧方向。

因此，“Petri nets、program verification、process mining 持续存在，同时 AI/LLM 进入”与这项公开 strategy 相容。

边界：相容不等于该表态逐项解释了所有论文选择。

### 11.2 公开证据候选二：BPM / Petri-net / workflow 学术出身

博士论文、导师关系及同一曾庆田谱系中的跨组织流程挖掘工作，使 EdgeIM 更像十余年研究线上的现代节点，而不是 2025 年的临时转向。

### 11.3 公开证据候选三：真实应用持续产生 pull

用户输入记录的官方应用场景包括矿山、化工、公共安全和海洋安全。

用户输入还记录：2026-04，鲁法明参与山东科技大学计算机学院赴“露天煤矿灾害防治与生态保护全国重点实验室”的 AI 赋能矿山安全技术对接团队。

这可以解释近年煤岩识别、矿工语音情绪、精煤灰分预测、多模态工业数据和 physical constraints 的聚集，但活动身份、日期与报道原文仍须核验。

### 11.4 我们的进一步推断：三股压力同时发生

以下是分析性推断，不是老师公开路线图：

```text
traditional formal / process core
            |
            +-- 现实系统越来越大
            |       -> sampling / edge / distributed
            |
            +-- 数据越来越复杂
            |       -> causal / probabilistic / multimodal
            |
            +-- AI 能力快速上升
                    -> LLM / representation learning
```

因此，可见现象不是单线转向，而是稳定内核向规模、数据复杂性和 AI representation 三个方向扩张。

## 12. INFERENCE：公开成果中尚未真正合流的节点

本节全部是根据公开论文结构与 residual 推导出的 plausible next step：不代表鲁老师或合作者已经在做，也不代表他们计划做。

### 12.1 Formal Methods x LLM/Agent 尚未真正接合

当前可见 LLM 侧候选结构：

```text
LLM
-> embedding / domain knowledge
-> time-series / multimodal prediction
```

另一侧：

```text
Petri Net
-> formal model
-> deadlock / causal reasoning / verification
```

尚未在公开成果中明确合成：

```text
LLM / Agent execution
-> formal behavior model
-> verification / runtime assurance
```

因此，较准确的 residual 是：AI 已进入 prediction/representation 侧，但 formal core 尚未大规模进入 foundation-model/agent assurance。这个 residual 仍需经过 semantic prior-art audit，不能直接称为 novelty gap。

### 12.2 Process Mining x LLM Multi-Agent 的 interaction semantics

合作网络已从 EdgeIM 延伸到 CrossEdgeIM 的 distributed robotic behavior discovery，但真正跨组织/多智能体 interaction 可能还需要更细的表示：

- message flow；
- data dependency；
- causal visibility；
- agent-to-agent protocol；
- interaction property。

问题不只是把局部 Petri nets 合并，而是选择足以表达 interaction semantics 的 representation。

### 12.3 从 offline discovery 到 online runtime assurance

公开成果中可见的候选零件包括：

- CrossEdgeIM：streaming/incremental features；
- 程序分析：runtime trace + detection + replay；
- process mining：conformance/discovery；
- Petri net：verification。

尚未看到它们被明确组装为：

\[
\boxed{
\text{stream}
\rightarrow
\text{online discovered model}
\rightarrow
\text{runtime property checking}
\rightarrow
\text{intervention}
}
\]

这是自然的未合流节点，但不能据此假设技术兼容性或低 translation cost。

### 12.4 从相关结构到因果结构

两条候选路线正在靠近：

- 鲁法明侧：Petri + Bayesian -> root cause；
- 合作网络侧：process logs + causal inference -> performance anomaly root cause。

自然问题是 process control-flow structure 与 causal intervention structure 能否统一。必须坚持：

\[
A \rightarrow B \text{ as directly-follows}
\not\Rightarrow
A \text{ causes } B
\]

这与 `adjacency != causality` 是同一个 representation audit。

### 12.5 AI 中的 constraint 可能进一步 formalize

精煤灰分候选工作已经加入 physical-constraint loss，说明纯 data fitting 之外需要 domain constraint。沿传统形式化路径继续推，可以提出：

\[
\text{physical constraints}
\rightarrow
\text{process constraints}
\rightarrow
\text{formal constraints}
\]

例如模型预测不仅数值准确，还必须满足流程、物理或安全 invariant。该路径目前只是我们的 prediction，不是已公布计划。

## 13. 最需要近身跟踪的 sampling 谱系

\[
\boxed{
\text{DFR-equivalence sampling}
\rightarrow
\text{EdgeIM}
\rightarrow
\text{sigRank}
}
\]

### 13.1 问题演化

```text
第一问：怎么抽样？
    ->
第二问：怎么保证 sample 仍保留关键 behavior？
    ->
第三问：如何把结构保存用于 edge discovery？
    ->
第四问：有限 budget 下，如何优先保留“重要”的 trace？
    ->
我们的下一问：这些 surrogate 与 downstream model fidelity
到底有多强的 alignment？
```

最后一问是我们的 research question，不是现有工作的已知结论。

### 13.2 与当前学习的关系

这条谱系使 support、frequency、ratio 和 downstream sensitivity 成为真实接口，而不是无关的细节争论。

但学习顺序仍需保持：先准确理解 EdgeIM Algorithm 1 的输入、输出、停止规则和 feature semantics，再横向比较 ratio/budget formulations；不能用 sigRank 的问题设定反向改写 EdgeIM。

## 14. 更有信息量的鲁法明研究描述

相较“研究 Petri 网、人工智能、大模型”，更有证据结构的描述是：

> 他从 Petri 网/流程模型出发，长期研究复杂离散系统中“行为结构如何表示、如何从数据恢复、如何验证和分析”；之后分别向并发程序验证、跨组织/大规模流程挖掘、概率与因果知识推理扩展。最近又把 AI、LLM、多模态表示学习引入工业时序和安全场景，但传统的形式化/程序分析线仍持续产出。

该描述仍是综合解释，不应伪装成老师本人的自我表述。

如果把公开合作网络一起纳入，候选 trajectory 是：

\[
\boxed{
\begin{array}{c}
\text{Formal structure}\\
\downarrow\\
\text{Process discovery}\\
\downarrow\\
\text{large / distributed / cross-org process}\\
\downarrow\\
\text{causal / probabilistic reasoning}\\
\downarrow\\
\text{edge / robotics / industrial AI}\\
\downarrow\\
\text{? agents / runtime assurance / trustworthy AI}
\end{array}
}
\]

问号必须保留：前五层是待逐项核验的公开成果综合，最后一层是根据 residual 与外部 frontier 推出的可能连接。

## 15. 为什么这条 genealogy 与纯 AI lab 不同

某些 AI lab 的发展叙事可能是：

```text
Transformer -> LLM -> Agent -> Agent RL
```

这里更可能是：

```text
Petri net
-> workflow / process
-> formal analysis
-> mining
-> complex systems
-> data / AI
```

因此，当 LLM 进入时，自然问题未必首先是如何训练、对齐或扩展能力，而可能是：

- LLM/Agent 进入复杂系统后，行为如何表示？
- 知识如何组织？
- 过程如何发现？
- 约束如何表达？
- 结果如何验证？
- 如何服务真实决策？

这是基于过去公开轨迹的解释性 prediction，不是对未来选题的保证。

## 16. 对 EdgeIM 学习与鲁组交流的含义

准备不应停在“会讲 EdgeIM 一个算法”。更重要的是逐渐识别并能独立运用整条 research grammar：

\[
\text{真实问题}
\rightarrow
\text{representation}
\rightarrow
\text{structural assumption}
\rightarrow
\text{method}
\rightarrow
\text{property / evidence}
\rightarrow
\text{failure boundary}
\]

这条链可以用于阅读论文、比较方法、生成问题和面试表达，但不能只背成话术。真正的掌握要求能够：

1. 用具体论文解释 representation 为什么这样选；
2. 指出 structural assumption 在什么情况下失效；
3. 区分 observed relation、causal relation 和 formal constraint；
4. 说明结果支撑了什么 property，没支撑什么；
5. 构造一个 failure case 或 competing explanation；
6. 把同一 operator 在另一个领域重新具体化。

## 17. 与迁移审计协议的对接

这份谱系档案提供的是 source-domain map 和 residual 候选，不直接给出 `PROMOTE` verdict。

任何候选接驳点都必须另开 Transfer Card，至少审计：

- **Source Evidence**：源方法是否真的依赖所说机制；
- **Target Preconditions**：Agent/LLM 域是否存在对应对象、关系与约束；
- **Representation**：temporal order、DFR、data dependency、causal visibility 或 formal state，哪个才足够；
- **Decision Delta**：结构显式化后改变 monitor、verify、compile、repair 中哪个决策；
- **Competing Explanation**：结果是否只是 adjacency、frequency、logging artifact 或规模效应；
- **Cheap Falsification**：最小反例能否先杀死 idea；
- **Translation Cost**：是否需要先造 logging、benchmark、semantics 和 runtime。

推荐优先实例化的卡，不代表优先开实验：

1. `DFR-equivalence sampling -> EdgeIM -> sigRank -> downstream model fidelity`；
2. `program runtime trace + replay -> Agent runtime assurance`；
3. `Bayesian time PN RCA + causal process mining -> causal Agent workflow diagnosis`；
4. `physical constraints -> process/formal safety invariants for industrial AI`。

## 18. 现有证据域与后续核验入口

当前工作区已有以下相关资产，应优先复用，不重新制造平行证据库：

- `MAS_Safety_Project/learning/training/ra2716-survey/EX-01/EX-01_鲁法明画像v0.md`；
- `MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/09_FAMILY_SYNTHESIS_V2.md`；
- `MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/bridge/EDGEIM_T2_bridge.md`；
- `MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/bridge/MHP_T1T3_bridge.md`；
- `MAS_Safety_Project/research/papers_lu/teardown-bridge-20260904/_launch/pdftxt/SIGRANK.txt`；
- `MAS_Safety_Project/research/_archive/desktop-survey-snapshot-2026-08-13/调研中/鲁法明_SDUST_2024-2026_学术产出审计_矩阵版.md`。

这些文件本身也具有不同时间、状态和 claim ceiling。后续正式核验时，应重新检查当前路径、论文原文、官网状态与作者身份，不能因为“本地已有文件”就自动视为一手事实已闭环。

## 19. 当前结论边界

### 可以说

- 本次用户研究形成了一个连贯、可检验的鲁法明研究谱系解释；
- 该解释的稳定内核是 representation、structure recovery、analysis/verification 和 decision，而不只是 Petri 网技术名；
- 鲁本人署名与合作网络产出已在叙事层明确分开；
- 五个 plausible next steps 已被明确标为 inference；
- sampling 近身谱系和四个 Transfer Card 候选已形成。

### 还不能说

- 本文所有论文信息与数字已经逐条核验；
- 公开合作图等于真实团队组织结构；
- 鲁老师已经规划 Agent/runtime assurance；
- `Formal Methods x LLM/Agent` 是无人做的 novelty gap；
- 任一候选接驳点已达到 `PROMOTE`；
- 用户已能脱离本文独立解释、修改、证伪和防守整条 research grammar。

## 20. 关联训练设计

`2026-09-05_EdgeIM四论文十字训练闭环.md` 把本谱系中的四篇近身材料落实为一主干三镜头：EdgeIM 建立 ownership，sigRank 横向攻击 sampling objective，Ground Truth Approach 约束实验与 claim，CrossEdgeIM 用于重建 predecessor、residual、redesign 和 new residual。
