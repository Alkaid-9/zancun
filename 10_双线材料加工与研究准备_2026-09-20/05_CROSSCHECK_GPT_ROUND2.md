# JINZU_MASTER_V2 · 05_CROSSCHECK_GPT_ROUND2

**版本**：初版
**日期**：2026-09-21
**状态**：SECONDARY-SOURCE CROSSCHECK / 非 v2.0 强制文件

---

## 这份文件是什么，不是什么

**不是**：v2.0 §27 推荐目录树里的文件——v2.0 只规定 00–04 五个核心文件。本文件是 00–04 定稿之后新增的第六份文件，用来处理一个 v2.0 没有预见的输入类型：**用户与另一个模型（ChatGPT）就同样三篇论文进行的独立讨论**。

**是什么**：对这段 GPT 讨论做一次 **P0（SOURCE）+ P2（FALSIFICATION）式的审查**——像对待第四篇"论文"一样对待它，而不是因为它出自一次对话就默认可信，也不因为它讲得流畅、成体系就默认正确。这直接对应 v2.0 §1.3 的纪律：**"模型互相同意不等于独立验证"**。GPT 和这份计划的作者（Fable）此前并未互相校对，两者独立地讨论同样三篇论文，这本身是一次有价值的交叉验证机会，但前提是真的去比对差异，而不是找相同点就归并、找不同点就沉默。

**结论先行**：GPT 的核心框架（三层 stack）在结构上与 00 文件已有的 Q1–Q6 映射**高度重合，不需要新增框架**；但 GPT 在两个具体问题上给出了与现有纪律**相冲突**的建议（PetriBench 定位、里程碑命名），已在下文明确标注为不采纳；另有若干**细化信息**（taxonomy、predicate 词表）值得吸收，但均标记为未独立核实的二手数据。

---

## 一、结构层面：GPT 的"三层 Formal Agent Stack" vs 已有的 Q1–Q6 映射

GPT 提出的分层：

```
Representation / Semantics   ← String Diagrams
        ↓
Reasoning / State-Space      ← PetriBench
        ↓
Specification / Control      ← ContrAgent
```

00_OBJECTIVES_AND_CLAIMS.md 已有的映射（本轮之前已写入，见该文件"统一研究坐标与六个问题"一节）：

| 论文 | 对应问题 |
|------|---------|
| String Diagrams | **Q2** Representation Preservation |
| ContrAgent | **Q1 + Q5** Observation Sufficiency + Intervention Semantics |
| PetriBench | **Q4 + Q6** Verifier Correctness + Evaluation Validity |

**比对结论**：
- String Diagrams ↔ Q2：**完全一致**。两边都把它定位成"表示保留什么信息"的问题。
- ContrAgent ↔ "Specification/Control"：**部分一致，但 GPT 的标签比 Q1+Q5 窄**。GPT 强调的是"约束/监督"（用合约管住 agent 的动作），这基本对应 Q5（Intervention Semantics）；但 JINZU 现有映射还包含 Q1（Observation Sufficiency）——即 ContrAgent 论文里"观测相同但真值不同"这个反例，这一半在 GPT 的三层框架里被并进了"Specification/Control"层，没有单独强调。**不算错误，但是一次信息损失**：GPT 的框架把"看得到什么"和"能不能管住"合成了一层，JINZU 现有框架坚持把它们分开审计（这正是 Q1 和 Q5 分成两个问题、而不是一个问题的原因——一个系统可以"看得到但管不住"，也可以"管得住但看不到"，两者是独立故障模式）。
- **PetriBench ↔ "Reasoning/State-Space"：这是唯一一处真正的分歧，见下节详述。**

**处理方式**：不修改 00 已有的 Q1–Q6 映射表（它更细、更符合"审计点独立"的原则）。本文件记录这次比对，作为该映射表的一次外部交叉验证：三层 stack 没有提供任何 Q1–Q6 框架无法覆盖的新结构，唯一的实质分歧在 PetriBench 的定位上。

---

## 二、实质分歧：PetriBench 是"推理测试工具"还是"待验证的 oracle"？

这是本次交叉核对中**最需要明确表态**的一点。

**GPT 的框架**：PetriBench 的核心价值被描述为"LLM reasoning microscope"——用 PCA 分析模型在 Easy/Hard 任务上的能力画像分化（第一主成分解释力从 91.7% 降到 78.9%），以及区分"visible CoT"和"internal reasoning effort"对分数的不同影响。整段论述把 PetriBench 当作**评价 LLM 推理能力**的工具在使用。

**现有 JINZU 计划的立场**（00/02/03/04 四处一致）：
- 00_OBJECTIVES_AND_CLAIMS.md："PetriBench...**接入方式**：不测 LLM leaderboard。先验证 oracle 自身可信，再决定是否拿去评 LLM。"
- 03_PAPER_TO_CAPABILITY_PIPELINE.md P5 说明："本轮明确'不测 LLM leaderboard'...nearest-neighbor 检索完全没开始。"
- v2.0 源文档 §14："首轮不做 LLM leaderboard。"
- v2.0 源文档 §21 Background B："暂时不测 LLM。先把可信 checker 做出来。"

**这不是措辞差异，是范围冲突**：GPT 的框架默认"用 PetriBench 测模型"是当前就该做、且是这篇论文最有价值的部分；JINZU 现有纪律明确把"测 LLM"列为**本轮不做**，理由是必须先把 oracle 自身的可信性建立起来（RP-C 的全部内容），再决定是否要拿它去评价任何模型——包括评价 Fable/Sol/Gemini 自己。

**判断**：**不采纳 GPT 关于"PetriBench 核心价值是 reasoning microscope"的定位。** 保留 JINZU 现有立场（PetriBench → RP-C → oracle 可信性优先）。GPT 提到的 PCA 发现、CoT 有效性发现，本质上都是"**别人已经拿这个 benchmark 测过 LLM 之后**得到的结果"——这些是有意思的背景知识，但采纳它们不等于现在就要重复这类测试。这类工作只有在通过 P0–P4（尤其是 oracle 已经 VERIFIED、且明确决定要不要评 LLM）之后，才进入 03 文件定义的 **P5 RESEARCH** 范围，而 P5 本轮不做。

**唯一可以低风险采纳的部分**：GPT 给出的 2×2 taxonomy（finite/infinite × local/global）是对"六个标准任务"的一种更精细切分方式，这个切分本身**不涉及测不测 LLM**，只是任务分类法，可以用来充实 03 文件 PetriBench 的 P1 Mechanism Sheet（见下节"细化：可采纳部分"）。切分法本身与"要不要拿去测模型"是两个独立问题。

---

## 三、命名冲突：F1/F2/F3/B1 不能直接采用

GPT 提议的里程碑：

- **F1** State-Space Competence（PetriBench）
- **F2** Temporal Specification Competence（ContrAgent）
- **F3** Representation Competence（String Diagrams）
- **B1** Formal Agent Bridge（三者组合 toy）

**冲突点**：

1. **F1–F8 已经是一个在用的命名空间**，含义完全不同。00_OBJECTIVES_AND_CLAIMS.md"与现有资产的关系"一节明确写着：

   > **F1–F8** | 内嵌到各 RP 中；不另建课程 | 按需 JIT

   这里的 F1–F8 指的是旧版（07/08 材料）里的具体学习模块编号，v2.0 把它们降级为"按需嵌入各 RP，不再单独成课"。如果现在再用 F1/F2/F3 表示三个全新的、含义完全不同的里程碑，任何人日后读到"F1"这个词都要先问"是哪个 F1"——这正是好的命名规范要避免的歧义。

2. **B1 已经是 04_BRIDGE_LU_SUN_OPENAI.md 里一个具体定义的桥**（Representation & Information Preservation：EdgeIM → String Diagrams → ReGA，接鲁侧）。GPT 提议的"B1 Formal Agent Bridge"（三篇论文组合 toy，指向 agent runtime 而非鲁侧表示学习）是完全不同的概念。复用"B1"这个编号会直接产生编号冲突。

**判断**：**不采纳 F1/F2/F3/B1 这套编号。** GPT 描述的三个"能力锚点"本身是合理的（分别验收 PetriBench/ContrAgent/String Diagrams 的独立掌握程度），但它们的验收标准已经被 01_CAPABILITY_EVIDENCE_MATRIX.tsv 的 E0–E5 等级 + 02_RESEARCH_PROBE_REGISTRY.md 各 RP 的交付物覆盖，不需要一套平行的新标签：

| GPT 的标签 | 对应到已有结构 |
|-----------|--------------|
| F1 State-Space Competence | RP-C（Petri Exact Oracle）的 E2/E3 证据 + 01 矩阵对应行 |
| F2 Temporal Specification Competence | RP-A + RP-D（ContrAgent 两段）的 E2/E3 证据 |
| F3 Representation Competence | RP-B（String Diagrams）的 E2/E3 证据 |
| B1 Formal Agent Bridge（三合一 toy） | **确实是个新概念**，04 现有 B1–B4 都不覆盖"三篇论文合成一个可运行 agent toy"这件事；见下节 |

**"三合一 toy" 是否值得单独立项，留给用户决定**——如果决定要做，编号应该是不与现有 B1–B4 冲突的新标识（例如 B5，或者干脆不进入"Bridge"这个类别，而是作为 RP-A/B/C 全部达到 P2 之后的一个"整合 milestone"，参照 04 文件里 B4 的写法："当 B1/B2/B3 各有初步结论时，B4 才能问……"）。本文件不代用户做这个决定，只排除"复用 B1"这一个选项。

---

## 四、优先级：GPT 建议的学习顺序 vs 已有的 P0/P1/P2 分组

GPT 建议：**PetriBench → ContrAgent → String Diagrams**（严格串行，理由是"学习收益/前置成本最高的先学，能给后面搭脚手架"）。

**核对结果——这条建议在粗粒度上已经被满足，不需要改动**：

02_RESEARCH_PROBE_REGISTRY.md 现有优先级：
```
P0（当前）：RP-A（ContrAgent 首件）+ RP-C（PetriBench oracle）
P1（EX-05 收口后）：RP-B（String Diagrams）+ RP-D（ContrAgent 后续）
P2：RP-E
```

String Diagrams（RP-B）本来就排在 P1，晚于 PetriBench 和 ContrAgent 的首件（都在 P0）——这与 GPT "String Diagrams 最后学"的建议**方向一致**，不需要调整。

**真正有新信息量的部分，是 P0 内部的顺序**：现有计划里 RP-A 和 RP-C 是**并行**的两个 WIP 槽位（v2.0 §20：Background 最多 1 个 active research probe + 1 个 oracle/infrastructure unit，当前分别是 RP-A 和 RP-C），并不要求分先后。GPT 建议"先啃 PetriBench"，其实是在问一个 JINZU 框架没有直接回答的问题：**如果同一时间只能真正投入注意力做一件事，先做哪个？** 这个问题成立，而且答案（先做 RP-C 的 oracle 基建）有合理依据：oracle 是纯粹的、不依赖其他探针结论的基础设施，而 RP-A 的反例构造某种程度上可以借用 PetriBench 练出来的"状态追踪"直觉。

**判断**：**采纳"注意力顺序"这一条**，但表述为"P0 内部建议先攻 RP-C 再深入 RP-A"，而不是重写整个优先级分组（因为分组本身已经对，动它反而会破坏"active probe / infrastructure"两槽并行的设计）。已在 02_RESEARCH_PROBE_REGISTRY.md 的优先级小节加一行注记，指回本文件。

---

## 五、细化：可采纳的二手信息（均未独立核实，标注后使用）

以下内容来自 GPT 的讨论，**本文档没有对照论文原文逐字核实**，采纳时一律视为"待核实的二手细化"，与 03 文件里 `identity_manifest`/`source_locator` 的"待填"占位符处于同一诚信等级——即：可以先记下来指导阅读重点，但不能当作已确认的论文事实来引用或对外表述。

### 5.1 PetriBench 的 2×2 任务分类法

| | Finite horizon | Infinite horizon |
|---|---|---|
| **Local** | Minimum Token Steps | L0 / L4 Liveness |
| **Global** | Reachable Markings | Deadlock / Boundedness |

**用途**：可以用来充实 03_PAPER_TO_CAPABILITY_PIPELINE.md 中 PetriBench 的 P1 Mechanism Sheet（Input 部分目前只写"A query: {type: reachability | liveness | deadlock | ...}"，比较扁平）。这个 2×2 结构如果核实无误，可以帮助区分"这道题需要的是深度搜索还是广度枚举，是有限步还是需要 invariant 推理"——这正好是 RO-2/RO-3 一直在强调的"不要把所有 fixture 当同一种能力"。

**核实要求**：使用前必须对照 PetriBench 论文原文确认——尤其是 "L0/L4 liveness 到底是不是 local"这一分类，以及是否真的只有这四类（论文摘要通常还会提到其他任务如 "livelock" 等）。**在核实之前，不要把这张表写入 00–04 任何一份文件的正文**，只作为 03 文件里的一条旁注参考。

### 5.2 ContrAgent 的 predicate 词表

GPT 提到 ContrAgent 把每个 event 转成 checkable predicates：`Call(tool) / ArgHas(...) / OutHas(...) / Match(...) / Flow(source,sink) / Perm(...) / Cnt(tool) / Tok / Depth / Num(...)`。

**这与 JINZU 现有的 event 分解不是同一层**：03/04 文件里 ContrAgent 的 event 分解是 `proposal/accepted_call/return/effect/END`——这回答的是 **Q1（能观测到什么事件类型）**；GPT 给出的 predicate 词表回答的是**用什么逻辑谓词描述规格**（Q3 Specification Adequacy 的下游），两者互补，不冲突。

**用途**：如果需要写具体的 A/G contract（比如 03 文件 ContrAgent 部分尚未展开的"教学 contract monitor subset"），这个谓词词表是一个有用的起点模板。

**核实要求**：同上，用之前对照论文原文确认这十个谓词的准确定义和是否有遗漏/合并。

### 5.3 String Diagrams 的单向声明（signature 相等 ⇒ trace 相等，非反之）

这一条**已经与现有文件一致**，不算新增信息：03_PAPER_TO_CAPABILITY_PIPELINE.md 的 Invariant 部分已经写着 "signature(x) = signature(y) ⇒ trace_language(x) = trace_language(y)"。GPT 的表述（$\Sigma_1=\Sigma_2 \Rightarrow L(\Sigma_1)=L(\Sigma_2)$，且强调不声称逆命题）与此完全吻合，可以当作对已有内容的独立确认，不需要改动文件，只在此记录"两个独立来源在这一点上互相印证"。

---

## 六、GPT 自己已经做对的一件事：没有抢跳到 novelty

GPT 讨论的结尾明确写道：

> 现在证据等级应该是：**SOURCE FACT**（三篇分别提出了上述方法）/ **RECONSTRUCTION**（三层框架是重构，不是作者本意）/ **HYPOTHESIS**（三层接口之间可能存在研究空间）。这个现在先不要升格成 idea。等下一步我们真正拆的时候，再去查 prior art、counterexample 和已经有人做过的 bridges。

这段自我约束**值得保留和强调**，理由是它与 v2.0 §29"当前明确不做"里的两条纪律直接对应：
- "把关键词相似当 bridge" → GPT 的三层 stack 目前只是**重构**（reconstruction），不是发现，用词上也没有强行宣称"这就是一个 bridge"。
- "为了保住 idea 移动评价指标" → GPT 没有在文中给这个三层框架编造一个"结果"来证明它成立。

**唯一的风险**：这段克制的表述夹在一段修辞感很强的论述中间（"隐约出现了一套 Formal Agent Systems 的完整纵向栈"），如果以后只记得后半句、忘了前面的 SOURCE/RECONSTRUCTION/HYPOTHESIS 分级，这段讨论就会在传播过程中被意外拔高成"结论"。本文件记录这一点，就是为了防止这种拔高在未来的引用中发生——**引用这次讨论时，只能引用到 HYPOTHESIS 这一级，不能引用成"我们已经发现了 Formal Agent Stack"**。

---

## 七、留给用户决定的点（已裁定）

1. **"三合一 toy"要不要单独立项？—— 已裁定：立项。** 2026-09-21 用户拍板，编号为 **B5**（不复用冲突的 B1），已写入 04_BRIDGE_LU_SUN_OPENAI.md，硬性前置条件是 B1/B2/B3 各自达到 P2 交付物；未满足前 B5 只是占位问题陈述，不能开始构造 toy。
2. **是否安排时间独立核对 PetriBench 的 2×2 taxonomy 和 PCA 数字（91.7%→78.9%）？—— 已裁定：安排，指派 Luna。** 见 06_HANDOFF_LUNA_VERIFICATION.md 第三节。核实结论回执后由主控写回本节，在此之前这两个数字仍不得进入 00–04 正文，限制不变。
3. **ContrAgent 的 predicate 词表是否要正式写入 03 文件的 P1 Mechanism Sheet？—— 已裁定：先核实，指派 Luna。** 见 06_HANDOFF_LUNA_VERIFICATION.md 第四节。核实前 03 文件维持现状。

**交接与执行状态**：核对任务已正式派发给 Luna（执行环境：codex），交接文档见 06_HANDOFF_LUNA_VERIFICATION.md。该文档同时代 03 文件顺带核实两篇论文 `identity_manifest` 中仍缺的 authors/page_count 字段。Luna 只读核验、不写本仓文件；回执由主控核对后手工写回本节与 03 文件。
