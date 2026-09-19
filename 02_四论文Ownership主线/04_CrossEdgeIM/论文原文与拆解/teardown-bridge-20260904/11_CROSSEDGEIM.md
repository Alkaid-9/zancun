Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# 11 · CrossEdgeIM（IoT Magazine 2026）第一性原理全拆 —— 桥线 T1 背景篇

> 主输入：`research/papers_lu/CrossEdgeIM-2026-IoTMag.pdf`（6 页，印刷页 pp.55–60，**PDF 物理页 = 印刷页 − 54**；下文 `[PDF p.N]` 一律用物理页）。文本层 `_launch/pdftxt/CROSSEDGEIM.txt` 仅用于定位；判定以 `Read` PDF 为准。p.4 已视觉判读（Fig. 2 四格读数）；**p.5 Fig. 3 本次未完成视觉判读**，其格内数字标 `[图读数不清]`。
> 不变约束执行声明：本篇凡涉及 EdgeIM [8] 的句子只原样引英文并标 `[CrossEdgeIM 原文转述，非 EdgeIM 原文]`；不回答 G0 五问；不比较两者机制；不复原任何采样/过滤伪码。

---

## 0. 身份卡

- **题录**：Xuan Su (Graduate Student Member, IEEE), Cong Liu, Qingtian Zeng, Jinglin Zhang, Long Cheng (Senior Member, IEEE). "CrossEdgeIM: An Edge-Based Approach for Interactive Robotic Behavior Model Discovery". *IEEE Internet of Things Magazine*, January 2026, pp. 55–60, 栏目 "EDGE AI FOR INTERNET OF ROBOTIC THINGS"。DOI 10.1109/MIOT.2025.3625047；Date of Publication: 3 December 2025；Date of Current Version: 22 January 2026；ISSN 2576-3180 [PDF p.1 页眉/脚注]。
- **校样标记**：派单称"作者校样"，但页面带印刷页码 55–60、"Date of Current Version" 与期刊页眉，形态为 Xplore 正式版；页脚含 "Authorized licensed use limited to: Veer Narmad South Gujarat University. Downloaded on September 03,2026" 水印 [PDF p.1–6 页脚]。是否校样 `[需验证]`；来源 `[需核实]`。
- **sha256**：`ac7ec167a89cd726381ae451b96280e44d49951f55481049209414654f311803`（本次 `sha256sum` 复验一致）。
- **作者/单位** [PDF p.1 脚注]：Su、Zeng — 山东科技大学计算机学院；**Cong Liu（通讯作者）** — NOVA IMS（里斯本新大学）+ 山东理工大学计算机学院双署名；Jinglin Zhang — 山东大学控制科学与工程学院；Long Cheng — 华北电力大学控制与计算机工程学院。
- **基金** [PDF p.1 右栏]：NSFC 62472264、52574256；山东省杰青 ZR2025QA13；山东省重点基础研究 ZR2025ZD17；泰山学者 TSTP20250506；葡萄牙 FCT UID/04152/2025（MagIC/NOVA IMS）与 UID/PRR/04152/2025。
- **与 EdgeIM 作者栏交集（只陈述作者栏事实）**：本文引文 [8] 列 EdgeIM 作者为 "X. Su, C. Liu, F. Lu, L. Cheng, Q. Zeng, and S. Zhang" [PDF p.6 参考文献]。交集 = Su、Liu、Zeng、Cheng 四人；**Faming Lu 与 Shouli Zhang 不在本文作者栏**；Jinglin Zhang 为本文新增；通讯作者由 EdgeIM 的 Lu 换为本文的 Liu。NSFC 62472264 两篇共同出现（EdgeIM 侧依据见模板 07 §0 基金行）。
- **数据集脚注**：四份日志托管于 `https://github.com/Lihuiling12/TASE.git` [PDF p.5 脚注 1]。

## 1. Task：解决什么问题？形式化

**非形式陈述** [PDF p.1 摘要]：IoRT 中交互式机器人系统部署在分布式边缘环境；传统行为建模依赖集中式数据采集，带来延迟、通信开销与隐私风险。目标：在边缘架构下发现"交互式机器人行为模型"。

**场景假设** [PDF p.2 §III.B]："The proposed approach assumes that event log remain locally distributed across edge nodes during system operation, rather than being centrally stored in advance."

**三层实体**（按 §III.A 复原，[PDF p.2]）：
- 活动节点（Activity Node）：部署在机器人或其本地控制器所附边缘设备上，监控一个特定机器人任务，是"最小计算单元"。
- 组织节点（Organization Node）：fog 级服务器，管理一组功能相关的机器人。
- 中心节点（Central Node）：云或监督控制器。

**形式化（按原文对象重构，原文无编号定义）**：
- 输入：K 个组织，每个组织内若干活动节点；每个活动节点在线消费事件流 e = (case, activity, timestamp) [PDF p.2–3 §III.B]。
- 活动节点状态：DFR（活动对 → 计数）、StartSet、EndSet；上报增量 ΔDFR、ΔStartSet、ΔEndSet [PDF p.3]。
- 组织节点状态：组织级三元组 → Org-DFG → 组织级 Petri 网（IM 产出）[PDF p.3 §III.C]。
- 中心节点输出：全局 Petri 网 = K 个组织网的并行合并（source → τ_split → 各分支 → τ_join → sink）[PDF p.4 §III.D]。
- 目标函数（原文无显式优化目标，仅用评价指标）：F-measure（式 1）高、Complexity（式 2）低、通信量小、原始日志不出组织边界 [PDF p.5]。

**规模指标**（原文给出的量级）[PDF p.4]：设组织内活动数 m、ΔDFR 平均边数 e：三元组聚合 O(e)；在稀疏 DFG 上跑 IM O(m log m)；每包大小 e + |ΔStart| + |ΔEnd|。中心合并 O(K) [PDF p.5]。

## 2. Challenge

**原文声称的三条挑战** [PDF p.1 右栏，引 [4],[5]]：
1. 数据孤岛与隐私 → 拿不到完整全局日志，传统方法缺控制流信息。
2. 分布式计算与不稳定通信 → 边缘节点带宽有限，集中式传原始数据代价过高。
3. 机器人交互含并行/选择/循环 → 对发现算法精度与效率要求严格。

**对现有工作的定位** [PDF p.1–2]：
- 集中式（Alpha/Heuristic/Inductive Miner [1–3]）：假设集中存储或单机器人流程 [PDF p.1]；存储/计算瓶颈 + 隐私 [PDF p.2 §II]。
- 边缘式：原句 "EdgeMiner [6], [7] and EdgeIM [8] construct local features at edge nodes and aggregate them centrally to produce a global process model, thereby reducing computation and communication overhead. However, such approaches mainly target single-organization IoT environments and lack technical designs for interactive robotic behavior discovery." [PDF p.1] `[CrossEdgeIM 原文转述，非 EdgeIM 原文]`。§II 只再述 EdgeMiner："targets single-organization scenarios and does not address the specific needs of cross-organization collaborative modeling" [PDF p.2]。
- 流式 [4]、差分隐私 [5]、跨组织挖掘 [9–13]（含本组 TASE 2023 跨科室 [9]、DSS 2013 [10]、TSC 2019 [11]、MPE 2020 应急 [12]、ICWS 2024 区块链 [13]）：多数仍依赖集中或半集中聚合 [PDF p.2]。

**真/套话判定 `[推断]`**：挑战 1、2 是边缘过程挖掘的通用叙事（与 [6–8] 的动机同源），本文没有给出 IoRT 特有的新约束（如机器人实时性数值、带宽预算）。挑战 3（并行/选择/循环）由 IM 本身处理，不是本文新解决的难点。**本文真正区别于 [6–8] 的问题设定只有一条：多组织（K>1）且原始日志不出组织边界**——这一条在 §II 对跨组织文献的批评里成立，但在方法里被"并行合并"以最弱形式处理（见 §6）。

## 3. Insight & Novelty

### 3.1 Inspiration 来源
- I-A：边缘"本地统计 + 中心聚合"架构，原文归于 [6–8] [PDF p.1]（EdgeIM 相关句已在 §2 原样引述，不展开）。
- I-B：本组跨组织/跨科室建模线 [9][10][12]——"integrate intra-department models with inter-department collaboration patterns" [PDF p.2 §II]。
- I-C：IM 的 DFG 递归分解 [3]，原文描述为 "analyzes the global DFG to identify ... sequence, parallelism, exclusive choice, and loops ... recursively decomposes the activity set" [PDF p.3 §III.C]。

### 3.2 逐条 Insight
1. 计算单元下沉到"活动"粒度：一个活动节点只维护自己活动相关的 DFR/Start/End，上报增量而非全量 [PDF p.2–3]。
2. 组织级"真起止活动"清洗：合并各活动节点上报的 Start/End 集后，用聚合 DFR 的 target/source 关系剔除非全局起止 [PDF p.3 §III.C]。
3. 中心只收 PNML 模型不收关系：合并复杂度与组织数线性 [PDF p.5]。

### 3.3 Novelty 清单（原文自述）
- 三层架构（活动节点/组织节点/中心节点）[PDF p.1 摘要、p.6 结论]。
- 活动节点在线维护 DFR + 时间戳相同触发双向计数的"concurrency-marking mechanism" [PDF p.2 §III.B]。
- 组织节点三步聚合 + Org-DFG + IM [PDF p.3]。
- 中心节点结构化合并（全局 source/sink + τ_split/τ_join + 分支并联）[PDF p.4]。

### 3.4 严格三段式
- **前人做到**：单组织边缘式发现（[6–8]，原文口径）；集中式跨组织协同建模（[9–13]）。
- **前人没做到（原文口径）**：跨组织 + 全分布式 + 面向机器人交互 [PDF p.1–2]。
- **本文做到**：把组织当作独立分支并联进一张全局网；**没做到**：原文 §IV.C 自认 "does not yet explicitly capture the collaborative relations among multiple robots, and the interactions between organizations are represented in an implicit form" [PDF p.6]。`[推断]` 因此"跨组织协作模式"这一号称的 gap 在本文里并未被填。

## 4. 方法全恢复

### 4.0 数据流总图（对应 Fig. 1，[PDF p.3] 图题 "An approach overview"）
Fig. 1 本次未视觉判读 `[图读数不清]`，以下按 §III.A 文本 [PDF p.2] 复原：

```
事件流(机器人) → [活动节点 i,j] 维护 DFR/StartSet/EndSet，异步发 (ΔDFR, ΔStart, ΔEnd, caseID, 时间戳范围)
   → [组织节点 i] 聚合成组织级三元组 → Org-DFG → IM → 组织级 Petri 网 (PNML, 只发一次)
   → [中心节点] source→τ_split→{PN_1 ∥ … ∥ PN_K}→τ_join→sink → 输出 "raw merged model"
```

### 4.1 Stage 1：活动节点处理（本文自述，[PDF p.2–3 §III.B]）
- 维护对象：DFR、StartSet、EndSet，"in real time"。
- 更新规则（逐条原文语义）：
  (a) 新事件时间戳晚于同 case 前一事件 → 对应活动对顺序计数 +1；
  (b) 时间戳相同 → 触发 concurrency-marking，**两个方向计数各 +1**，表示并行；
  (c) 事件为 case 首事件 → 活动入 StartSet；为 case 末事件 → 入 EndSet；
  (d) 全部在线执行，"without waiting for case completion"。
- 上报：不周期性发全量；异步打包 ΔDFR、ΔStartSet、ΔEndSet，每包含"计数有变化的活动对、更新后的起止集、case 标识、事件时间戳范围" [PDF p.3]。
- 原文未说明：如何在流式下判定"末事件"（case 何时结束）`[需验证]`；活动节点如何知道"同 case 前一事件"若该事件属于另一活动节点 `[需验证]`；时间戳精度/时钟同步假设未给。
- **指针**：本文此节未标注是否沿用 [8]；是否与 EdgeIM 的对应步骤同构不在本篇判定范围，用户自读 EdgeIM 原文 §IV。本文全文**未出现任何采样/过滤/特征保持步骤**（文本层检索 "sampl"/"feature-preserving" 在正文无命中，仅 "event features"/"local features" 为泛称）。

### 4.2 Stage 2：组织节点建模（[PDF p.3 §III.C]）
聚合三步：
1. DFR 聚合：相同活动对计数累加。
2. Start 更新：合并各节点 StartSet，删除"在聚合 DFR 中作为 target 出现"的活动。
3. End 更新：合并各节点 EndSet，删除"在聚合 DFR 中作为 source 出现"的活动。
然后构建 Org-DFG → 喂 IM → "sound, behaviorally-complete organization-level Petri net"。
- 复杂度声明 [PDF p.4]：聚合 O(e)；IM O(m log m)（原文称"在稀疏 DFG 上"，无推导）；包大小 e + |ΔStart| + |ΔEnd|。
- `[推断]` 步骤 2/3 的删除规则在存在循环（活动既是 target 又是真起点）时会误删真起止活动；原文未讨论 `[需验证]`。

### 4.3 Stage 3：中心节点合并（[PDF p.4–5 §III.D]）
输入：K 个组织的 Petri 网（PNML，各发一次）。
1. 全局入口/出口：建全局 start place (source) → 单个不可见变迁 τ_split；另一不可见变迁 τ_join → 全局 end place (sink)。
2. 分支整合：每个组织网的 start place 接 τ_split，end place 接 τ_join，"ensuring that all organization models are executed in parallel within the global process model"。
输出："raw merged model" [PDF p.2]。复杂度 "approximately O(K)" [PDF p.5]。
- **无参数/阈值**：全文未出现任何可调参数、频次阈值、噪声过滤阈值；IM 变体未指明（IM/IMf/IMd）`[需验证]`。

### 4.4 公式全量
- 式 (1) F-measure = 2·fitness·precision / (fitness + precision) [PDF p.5]，引 [14]。
- 式 (2) Complexity = 2·ECaM·ECyM / (ECaM + ECyM) [PDF p.5]，引 [15]；ECaM = Extended Causal Metric（基于可达图的结构复杂度），ECyM = Extended Cyclomatic Metric（执行路径多样性）。
- 全文仅此两式；方法部分无公式、无算法框、无定义编号。

## 5. 实验协议与结果批判

### 5.1 协议逐项 [PDF p.5 §IV.A]
- 实现：PM4Py + Docker 容器。
- 数据：四份"simulated robotic interaction scenarios"日志；理由 "publicly available datasets are scarce"；托管 `github.com/Lihuiling12/TASE.git`（脚注 1）。
- 切分：日志按组织节点再按活动节点划分，每节点只处理其机器人动作对应事件。
- 基线：仅 Inductive Miner（集中式）。无 EdgeMiner/EdgeAlpha/EdgeIM 对照，无通信量/时延实测，无多次运行/方差。
- 指标：F-measure、Complexity（式 1、2）。

### 5.2 Table I 逐格 [PDF p.4]

| Dataset | #Case | #Event | #Task | #Dep. |
|---|---|---|---|---|
| EM_Log | 18909 | 605088 | 32 | 6 |
| ID_Log | 50427 | 1277247 | 30 | 6 |
| FP_Log | 37816 | 945400 | 27 | 4 |
| SD_Log | 48320 | 1111360 | 23 | 4 |

列名为 "#Dep."（department），正文却称 organization；`[推断]` 数据源自本组跨科室医疗线 [9]（TASE），"机器人交互"为改标签复用 `[需验证]`。

### 5.3 Fig. 2（IM 基线）逐格 `[图读数]` [PDF p.4]

| 子图 | Fitness | Precision | F-measure | EcaM | EcyM | Complexity |
|---|---|---|---|---|---|---|
| (a) EM_Log | 1 | 0.1322 | 0.2335 | 55 | 10004 | 109.3985 |
| (b) FP_Log | 1 | 0.233 | 0.3779 | 41 | 10008 | 81.6654 |
| (c) ID_Log | 1 | 0.247 | 0.3962 | 44 | 10006 | 87.6147 |
| (d) SD_Log | 1 | 0.3207 | 0.4857 | 36 | 10009 | 71.7420 |

自检：四行 F-measure 与式 (1)、Complexity 与式 (2) 重算一致（如 2·36·10009/10045 = 71.74）。结构描述：四张网均为"单入口 τ → 大扇出并行/选择分支 → 单出口 τ"的花状图，(d) 含 s1–s26 标号 `[图读数]`。

### 5.4 Fig. 3（CrossEdgeIM）逐格 [PDF p.5]
本次未完成 p.5 视觉判读，格内数字 `[图读数不清]`；正文可抄到的数字：SD_Log F-measure **0.6261**（vs IM 0.4857）[PDF p.5]；Fitness "slightly lower than IM's perfect score of 1"（未给数值）[PDF p.6]；Complexity "12-17% lower than IM" [PDF p.6]；平均每组织 8.2 节点 vs IM 11.7 [PDF p.6]；ECaM/ECyM "consistently lower" [PDF p.6]。

| 子图 | Fitness | Precision | F-measure | EcaM | EcyM | Complexity |
|---|---|---|---|---|---|---|
| EM_Log | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] |
| FP_Log | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] |
| ID_Log | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] | [图读数不清] |
| SD_Log | <1（文）| [图读数不清] | 0.6261（文）| [图读数不清] | [图读数不清] | [图读数不清] |

Petri 网结构（只描述）：按 §III.D，应为 source→τ_split→K 个组织子网并联→τ_join→sink；正文称 SD_log 图 "clearer organizational boundaries and more logical transition points (τ symbols) between parallel branches" [PDF p.6]。

### 5.5 撑住 / 没撑住的 claim
- 撑住（在其自设协议内）：SD_Log F-measure 高于 IM（0.6261 vs 0.4857，单点）；节点数更少（8.2 vs 11.7）。
- 没撑住：(i) "significantly higher F-measure across all datasets" [PDF p.5] 只给 SD 一个数，其余三份靠 Fig. 3 `[图读数不清]`；(ii) 通信开销、隐私、可扩展性、实时性均为叙述性主张，**零实测**；(iii) "improves the accuracy of behavior discovery" [PDF p.1] 与 fitness 下降并存，精度提升来自把组织切开后 precision 上升，属于评价口径效应 `[推断]`；(iv) IM 基线 ECyM 全部落在 10004–10009，`[推断]` 像实现层的饱和/上限值，Complexity 对比因此主要由 ECaM 驱动 `[需验证]`；(v) IM 基线 precision 0.13–0.32 极低，与"花状图"结构一致，说明日志本身高度并行/无序，基线未调参 `[推断]`。

## 6. Potential flaw

1. **体裁局限**：杂志 6 页、无定义/算法/证明、两式全为评价指标；方法只有叙述，不可精确复现（IM 变体、case 终止判定、时钟假设均缺）[PDF p.2–4]。
2. **"跨组织协作"名实不符**：中心合并把组织当独立并行分支，组织间交互 "implicit"（作者自认 [PDF p.6 §IV.C]）；`[推断]` 这等价于把跨组织 trace 切断，fitness 下降的根源正在此（原文归因 "minor uncaptured cross-organization traces" [PDF p.6]）。
3. **坏数据风险**：数据来自医疗跨科室仓库改称"模拟机器人交互"（§5.2 `[推断]`）；#Dep. 列与 organization 术语混用；无数据生成协议。
4. **基线单一且弱**：未与 [6–8] 任何边缘式方法对照；通信/时延主张无实验 [PDF p.5–6]。
5. **起止集清洗规则在循环下可能误删**（§4.2 `[推断]`）。
6. **值得写 paper 的困难 `[推断]`**：跨组织交互边（消息/共享资源）在"日志不出边界"约束下如何恢复——即用最少的跨界摘要（如边界活动的 DFR 片段）替代 τ_split/τ_join 的纯并联；这是 [9][10] 已在集中式下做过、本文在分布式下放弃的部分。

## 7. Motivation 还原（问句形式）

1. 若日志不能离开各组织，且中心只能收到"模型"，最少要传什么才能拼出全局网？（本文答：PNML 各一次 + 并联）[PDF p.4–5]
2. 活动节点粒度而非机器人/组织粒度上报，增量包能小到什么程度？（本文答：e + |ΔStart| + |ΔEnd|，未实测）[PDF p.4]
3. 分布式采集下同时间戳事件怎样进入 DFR 才不丢并发？（本文答：双向计数）[PDF p.2]
4. 组织级 IM 输出并联后，与集中式 IM 相比 precision/complexity 会怎样变化？（本文答：SD 上 F 升、复杂度降 12–17%，fitness 略降）[PDF p.5–6]
5. 机器人协作模式与多模态数据何时进入模型？（本文答：留作 future work）[PDF p.6]

## 8. 张力结构分析

- **隐私/通信 vs 保真**：只传模型 → 跨组织 trace 不可复放 → fitness < 1 [PDF p.6]；本文选择接受损失并称其 "reasonable trade-off"。
- **粒度 vs 一致性**：活动级上报使每个节点只看局部，case 级信息（首/末事件、跨节点前驱）依赖包内 caseID 与时间戳范围在组织层重建 [PDF p.3]；原文未说明重建规则 `[需验证]`。
- **评价口径 vs 主张**：F-measure 提升由 precision 驱动、fitness 下降；Complexity 由 ECaM 驱动、ECyM 疑似饱和（§5.5）；"更准"与"更简"两条主张都依赖口径 `[推断]`。
- **跨组织叙事 vs 并联实现**：§II 批评前人未建"协作模式"，§III.D 自身只做并联，§IV.C 承认隐式——三段自洽地暴露了张力 [PDF p.2, p.4, p.6]。

## 9. 桥线定位注记

- **本篇角色 = 背景篇**：确认 EdgeIM [8] 之后同一作者群（Su/Liu/Zeng/Cheng）在 2025-12 的邻近路线——从单组织边缘发现扩到多组织并联合并、换 IoRT 叙事、换通讯作者与主要基金。**不是 R1 的必要依赖**：本文无采样/过滤步骤、无算法框，对 G0 五问不提供任何输入（本篇亦按约束不作答）。
- **相对 EdgeIM 声称新增什么（只引原文自述句）**：
  - "EdgeMiner [6], [7] and EdgeIM [8] construct local features at edge nodes and aggregate them centrally to produce a global process model ... However, such approaches mainly target single-organization IoT environments and lack technical designs for interactive robotic behavior discovery." [PDF p.1] `[CrossEdgeIM 原文转述，非 EdgeIM 原文]`
  - "In this approach, robotic activities act as the smallest computational units." [PDF p.1]
  - "A central node then integrates the local models into a unified global behavior model through structured model merging." [PDF p.1 摘要]
  - 全文对 [8] 的实质引用仅上述一处（p.1），§II 相关工作段未再提 EdgeIM，仅提 EdgeMiner [PDF p.2]。
- **体裁与证据强度**：会议/期刊版（如 EdgeIM ICWS 7 页）通常有定义、算法框、多基线与表格；本杂志版只有叙述 + 两张图内嵌数字 + 单基线 + 无实测通信量。凡引用本文作为"EdgeIM 路线已扩展到跨组织"的依据时，证据等级应标为**作者自述级**，不作为方法学事实来源。
- **可追线索**（供用户自读，不作判定）：数据仓库 `Lihuiling12/TASE` 与 [9] 的关系；Fig. 3 四格数字；IM 变体与 PM4Py 版本。

[PARTIAL · 时间盒到 · 已完成到 §9；缺口 = Fig. 1/Fig. 3 视觉判读（§4.0、§5.4 格内 `[图读数不清]`）]
