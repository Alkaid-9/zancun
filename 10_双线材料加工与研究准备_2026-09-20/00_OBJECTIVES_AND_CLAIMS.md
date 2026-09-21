# JINZU_MASTER_V2 · 00_OBJECTIVES_AND_CLAIMS

**版本**：v2.0 正式版  
**日期**：2026-09-21  
**状态**：MASTER PLAN / 执行基准

---

## 核心研究母题

**英文**：What information is sufficient to verify or monitor a target property under a given access and intervention model?

**中文**：在给定可观测信息与干预能力下，什么表示足以可靠判断、验证或约束目标性质？

这是一个**共同研究坐标**，不是"已发现的 novelty"。

JINZU 中与 rigorous behavior 或 formal agent bridge 直接相关的研究工作向这个坐标投影；课程、通用能力、比赛和其他项目不受它统一解释。即使在这一研究范围内，也不要求把 EdgeIM、String Diagrams、ContrAgent、PetriBench、Agent Safety 强行拼成一个系统。

---

## 统一研究坐标与六个问题

这一范围内的论文、实验、toy 和 bridge 尽量投影到这条链：

```
World / History
      ↓
Observation α
      ↓
Representation R
      ↓
Specification φ
      ↓
Verifier / Monitor V
      ↓
Intervention I
      ↓
Environment Outcome
      ↓
Evaluation E
```

每个研究对象优先检查六类问题——这六问不是并列的检查清单，而是同一条链上的六个审计点。下表是概览，**主要对应探针**列中标 ⚠ 的是本文档自己做的归类推断（v2.0 原文未明说），其余四个是直接沿用 v2.0 给两者取的同名：

| 问题 | 核心追问 | 主要对应探针 |
|------|---------|------------|
| **Q1 Observation Sufficiency** | 系统到底能看到什么？是否存在两个 monitor 看起来完全一样、但真实安全真值不同的世界？ | RP-A（同名对应） |
| **Q2 Representation Preservation** | 从原对象映射到 representation 后丢了什么？对目标性质 φ，哪个 representation 保留了足够的信息？（不能问"哪个表示更高级"） | RP-B（同名对应） |
| **Q3 Specification Adequacy** | 当前 formal property 是否真的是 objective，还是一个容易形式化的 proxy？（"调用过 approve" ≠ "当前版本的同一对象已成功获得有效批准"） | RP-E ⚠（Q3 问"规格是否测中目标"，RP-E 问"规格改变后维护成本"——两者相关但不同问题，此处是最勉强的一组映射） |
| **Q4 Verifier Correctness** | checker 自己是否可信？必须分开审查：specification 正确、checker 对 specification 的实现正确、event extraction 正确、state update 正确、oracle 正确——这五者互不能替代证明。 | RP-C（部分对应，见下） |
| **Q5 Intervention Semantics** | 如果 monitor 阻止了某个动作，副作用真的没发生吗？"request rejected" 不能默认等于 "nothing happened"，除非执行语义明确保证如此。 | RP-D（同名对应） |
| **Q6 Evaluation Validity** | 最后 benchmark 测到的究竟是什么？oracle 独立性、information fairness、train/test leakage、baseline、parsing failure、隐藏特权信息、outcome/process/trajectory 指标差异都要查。 | RP-C ⚠（部分对应：RP-C 只覆盖 oracle 独立性这一项，不覆盖 leakage/parsing failure 等其余六项） |

**逐条展开（原样对齐 v2.0 §2，不再压缩枚举）**：

- **Q1** 的"看到什么"具体包括：event、object identity、version、arguments、successful return、failed return、timestamp、history、current state、communication、hidden state。
- **Q2** 的丢失检查沿一条具体变换链问：event log → DFG → process model → trace language → partial order → context/signature，每一步都要问"丢了什么"。
- **Q5** 的"副作用"具体检查四项：counter 增了吗？resource 被占了吗？retry 会重复执行吗？audit log 与 business state 是否分离？

三篇论文分别在这条链上撬动不同的审计点，这才是选它们的真正理由（不是关键词匹配）：

| 论文 | 攻击的维度 | 对应问题 | 核心研究操作 | 本轮目标 |
|------|----------|---------|-----------|--------|
| **String Diagrams** | Representation<br/>（什么结构必须保留） | **Q2** | RO-2：给定两个表示，定义 sameness，审计 information preservation | RP-B 初件产物 |
| **ContrAgent** | Observation + Intervention<br/>（看见什么 + 能做什么） | **Q1 + Q5** | RO-1 + RO-4：构造可观测冲突、检查干预一致性 | RP-A 初件产物 |
| **PetriBench** | Evaluation + Oracle<br/>（怎样建立可信真值） | **Q4 + Q6** | RO-3：独立 oracle、claim ceiling、mutation test | RP-C 初件产物 |

---

## 为什么选这三篇新论文

**不是什么**：
- 不是"学三个工具"。
- 不是"三篇论文分别覆盖 T2/T3-lite/evaluation"。
- 不是为了让你"掌握 category theory/ALTLf/Petri nets"。

**是什么**：
- 三个具体的研究操作示范。
- 三个可迁移的能力（不是知识）。
- 对母题的三个不同维度的论证。

---

## 进组可消费证据的等级定义

当前目标：**G2 级别**（可复现）。

| 级别 | 定义 | 证据 |
|------|------|------|
| **G0** | Exposure | 读过，不算掌握 |
| **G1** | Explainable | 未见例能脱稿 2 分钟解释问题/机制/假设/失败 |
| **G2** | Reproducible | ✓ 能独立跑 toy；改条件后能修改；能说 claim ceiling |
| **G3** | Research-ready | 有 nearest-neighbor / strong baseline / counterexample |
| **G4** | Owned | 自己的方法、实验、论文、artifact |

**G2 的三个形式**：
1. 一个本人手算的反例（RP-A/B/C 各一个）。
2. 一份本人修改后的运行结果（mutation 显示了什么变化）。
3. 一次独立的口头讲解（不读稿、能答问、能指出边界）。

---

## 与现有资产的关系

| 现有资产 | 新版中的角色 | 何时接入 |
|---------|-----------|--------|
| **EX-05** | Foreground 主线 | 现在就继续；增加 transfer hook |
| **F1–F8** | 内嵌到各 RP 中；不另建课程 | 按需 JIT |
| **01_两天执行合同** | 调度、工程验收、isolation | 保留；不当"进度指标" |
| **06_近期学习优先** | 当前 cursor 的 view | 保留；EX-05 收口后过期 |

---

## 三篇论文真正进入 JINZU 的路径

### String Diagrams

**当前阶段**：MECHANISM

**最小产物**（P0–P2）：
- `claim_ledger.md` — 论文主张、来源、条件。
- `mechanism_sheet.md` — 去掉论文语言后的 Input/State/Transition/Output/Assumption/Invariant/Failure Mode。
- `semantic_discrimination_matrix.md` — 表格化 representation 与目标性质的关系。

**第一个反例**：
```
a ; (b || c) ; d
vs
choice(a;b;c;d, a;c;b;d)
```
相同完整 trace (`abcd`, `acbd`)，但一个并发、一个互斥。

**接入方式**：不改 EdgeIM 发现算法，补一个"发现结果的事后审计"——比较 signature 相等 vs trace 相等的含义。

### ContrAgent

**当前阶段**：MECHANISM

**最小产物**（P0–P2）：
- `claim_ledger.md` — 论文主张、工具链、artifacts。
- `event_semantics.md` — proposal/accepted_call/return/effect/END 的明确分解。
- `observation_conflict_witness.json` — 两条可实现历史，观测相同但真值不同。

**第一个 baseline**：
```python
explicit_fsm_monitor.py  # object-aware FSM，跑通基本判定
```

**接入方式**：不实现任意 ALTLf 或 NL→logic，只上教学规范子集。若 FSM 在相同信息下完全解决，DROP "必须用更强形式体系" 这一主张。

### PetriBench

**当前阶段**：EXECUTABLE

**最小产物**（P0–P3）：
- `claim_ledger.md` — 六个任务、metrics、oracle 定义。
- `pn_oracle_min/` — 实现 enabled/fire/canonical_marking/bounded_bfs。
- `3_independent_goldens.json` — 在实现前冻结的真值。
- `8_adversarial_fixtures.md` — multi-input / self-loop / weight / initial-satisfied / path-merge / deadlock / growth / normal-end。

**接入方式**：不测 LLM leaderboard。先验证 oracle 自身可信，再决定是否拿去评 LLM。

---

## 鲁侧、孙侧、OpenAI 的接点

（见 04_BRIDGE_LU_SUN_OPENAI.md）

每个 bridge 由**统一问题** Q 驱动，不是关键词相似。

---

## 模型角色必须与模型名字解耦

研究架构里只允许出现**角色**，不允许把具体模型名字写进流程定义：

- Extractor（提取者）
- Mechanism Reconstructor（机制重建者）
- Implementer（实现者）
- Adversarial Reviewer（对抗审查者）
- Independent Oracle（独立真值源）
- Integrator（整合者）
- Learner（学习者——通常是用户本人）

某一轮具体分配哪个模型担任哪个角色，是**runtime config**，不是研究架构的一部分：

```
extractor: Gemini
mechanism_reconstructor: Fable
implementer: Sol
adversarial_reviewer: Fable
integrator: Sol
learner: USER
```

**关键约束**：以后模型换掉，研究流程不应该跟着变。

因此旧版 07/08 材料中大量"Sol 做什么、Fable 做什么、Gemini 做什么"的固定岗位描述，降级为 runtime config，不再属于 master research architecture 的一部分。

---

## Novelty Gate

一个探针（RP）必须**同时满足以下 12 个条件**，才允许被称为 **research candidate**（原样对齐 v2.0 §24）：

1. target problem 明确；
2. target property 明确；
3. access model 明确；
4. representation 明确；
5. information sufficiency 已审；
6. strong baseline 已跑；
7. independent oracle 已有；
8. nearest neighbor 已查；
9. open-source prior art 已查；
10. contradictory evidence 已查；
11. negative results 已接受；
12. toy 有预注册停止条件。

**否则只能标记为以下四种状态之一，不能自称"research candidate"或 novelty**：

- `TRAINING`
- `MECHANISM_ASSET`
- `RESEARCH_PROBE`
- `NOVELTY_UNESTABLISHED`

**与 01_CAPABILITY_EVIDENCE_MATRIX.tsv 的接口**：这四个标签是 `Research_Status` 列描述 RP-A~E 时应使用的词表。当前矩阵里出现的 `INFRASTRUCTURE`/`MACHINERY`/`ACTIVE_FOREGROUND`/`RESEARCH`/`FUTURE` 描述的是非 RP 对象（machinery、bridge、EX-05 foreground 等）——Novelty Gate 本身只约束"probe → research candidate"这一次跃迁，不对这些对象生效，两套词表尚未统一，留待下一轮决定是否合并。

**⚠ 已知的源文档内部张力**：v2.0 §19（统一状态矩阵）给"Research validity"轴列出的是另一组词表（`TRAINING`/`PROBE`/`FALSIFIED`/`SURVIVES`/`NOVELTY_UNESTABLISHED`），与本节（§24）的四词表不完全相同（仅 `TRAINING`、`NOVELTY_UNESTABLISHED` 重合）。本文档暂以本节为准（因为它直接服务于 gate 判定，定义更具体）；§19 的版本留作参考，不强行调和。

---

## 当前明确不做

本轮禁止：
- 搭新平台。
- 造"大一统 Formal Agent Safety Framework"。
- 完整复现三篇论文的作者实现。
- 把类别论当 String Diagrams 前置。
- 为了 T4 强加概率模型。
- 同时开多个 active research toy。
- 把模型并发当科研吞吐。
- 把阅读完成当本人掌握。
- 把 toy 正结果当 novelty。
- 把关键词相似当 bridge。
- 为了保住 idea 移动评价指标。
- 因为新论文出现重开已经闭合的旧局部结果。

---

## 进度定义的反转

**不再衡量**：
- 文件数、论文数、卡片数。
- token、分钟、worker 数。
- READY、DONE 标签。

**真正进度只看**：
1. 能不能独立**解释**机制？
2. 能不能独立**执行** toy？
3. 条件变化后能不能**修改**？
4. 换场景后能不能**迁移**？
5. 能不能**构造反例**并根据证据更新判断？

---

## 下一循环的大 Milestone

**EX-05 收口后**，给本人一个未见 workflow（不说来自哪篇论文），回答：

1. 系统 state 是什么？
2. observable events 是什么？
3. monitor 看不到什么？
4. target property 是什么？
5. specification 怎么写？
6. 是否存在 indistinguishable histories？
7. 若存在，缺哪个 observation 字段？
8. object-aware FSM 能不能解决？
9. checker 的 gold truth 怎么生成？
10. 若 specification 改变，哪些结论失效？
11. 当前实验最多能支持什么 claim？

**通过条件**：独立 formulation + counterexample + baseline + claim ceiling。

达到后，从"我在学 Formal Methods"进入"我能 formulation 一个 formal monitoring/verification problem"。
