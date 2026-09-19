---
title: 分支 · 重构进组计划
source: https://chatgpt.com/c/6a9f6203-9990-83e9-aa72-d631a466a6f4
---

# 分支 · 重构进组计划

#### You:
<time datetime="2026-09-06T23:23:10.772Z" title="2026/9/7 上午7:23:10">07:23</time>

对了。。。那个，我们的进组计划，不是要重构吗，我今天三节课来着，准备挂着电脑自己先跑点东西？我们计划要怎么改？还是说不着急，今天啃论文，等上完课人到电脑前了再进行？感觉人到电脑前再说，甚至今天可能可以不开电脑？

#### ChatGPT:
<time datetime="2026-09-06T23:26:11.228Z" title="2026/9/7 上午7:26:11">07:26</time>

<details>
<summary>Thought for 46 seconds</summary>

- 正在搜索网页
- 梳理进组计划与科研学习安排

梳理研究方向并优化边缘计算学习实验计划

规划了文献核查方案

我正在先确认 EdgeIM 与 PM4Py 的公开资料，再结合已提供的文档安排后续实验。当前重点是厘清算法、数据集和运行环境要求，避免把尚未执行的结果误写成既定结论。

已搜索 4 个网站

梳理进组计划并筛选沙箱文件路径

</details>

我先把你 9.5 / 9.6 两次“进组计划改版”里的硬约束对齐一下，再按你今天“三节课、白天不在电脑前”的实际可执行性压成今天版本。重点不是把电脑挂起来制造进度，而是判断**哪些任务必须有人盯、哪些适合离线跑、哪些今天干脆不该开电脑**。

我会改，而且我现在更倾向于：**今天白天不要为了“不能浪费电脑”而硬挂实验。你甚至完全可以不开电脑。**

因为我们昨天把进组计划重构以后，**当前瓶颈已经从“缺不缺更多实验结果”迁移到了“EdgeIM 全文 ownership 到底扎没扎实 + 新实验到底该服务哪个 claim”**。新版最低线已经不是“跑出一个 pilot”了，而是：

> EdgeIM 全文可重建 → 核心算法可手推 → 最小实现可重建 → claim 可审计 → assumption 可攻击 → 一个小研究问题跑完整闭环 → 脱稿连续追问。

而且我们明确保留了原来的 `T2 replication-plus`--基础 → 有界 clean-room 重实现 → synthetic ground-truth experiment → real-log stress check → cold replay--只是给它加了一个更高层约束：

> **实践 scope 可以窄；认知 scope 不能窄。**

所以今天如果拿旧 harness、旧实验合同、旧采样问题继续挂几个小时，最大的风险不是“跑错代码”，而是：

> **我们正在重定义研究问题，却让旧 experiment contract 继续生产结果。**

这些结果很可能不是错，而是**回答了一个已经不再优先的问题**。那才是浪费。

### 我会把进组路线临时冻结成这样

```text
Phase 0  现状重测
        ↓
EdgeIM Whole-Paper Diagnostic
        ↓
找出真正掉包的位置

Phase 1  EdgeIM Mastery
        ↓
全文 pipeline ownership
representation / algorithm / evidence / attack
        ↓
Mastery Gate

Phase 2  bounded clean-room implementation
        ↓
不是抄论文代码
而是自己重建最小链条

Phase 3  一个窄研究问题
        ↓
synthetic GT
→ controlled experiment
→ real-log stress check

Phase 4  冷启动重放 + 面试压缩
        ↓
30 秒 / 2 分钟 / 10 分钟 / 连续追问

──────────── 进组最低线 ────────────

外围菌丝：
sigRank / Ground Truth / CrossEdgeIM
program analysis / conformance
MAS representation / assurance
按需要接入，不抢主干
```

也就是说，我们昨天长出来的 **Agent behavior → explicit model → assurance**、object-centric / causal MAS representation，仍然是 North Star；EdgeIM 也仍然是非常好的第一块培养基。但它现在首先承担的是“behavior → structure + research training”的教材作用，而不是让我们继续无限优化 EdgeIM sampling 本身。

EdgeIM 本身也确实就是“预处理/feature-preserving sampling → edge-side structural feature extraction → central aggregation/model discovery”这三阶段，且作者在 PM4Py 上实现并用九个公开日志实验；所以后面要跑东西并不缺现成的计算入口。([Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/edgeim-an-efficient-edge-based-process-model-discovery-technique/?utm_source=chatgpt.com), [Process Intelligence Solutions](https://processintelligence.solutions/app/static/api/2.7.17/api/pm4py.discovery.html?utm_source=chatgpt.com)) **我们缺的是先决定下一次计算要回答什么。**

## 所以今天怎么过

我建议今天直接做成一个**低设备依赖的论文日**。

你三节课之间，手机/iPad 就够了。今天不要追求“啃多少页”，而做第一次**整篇收束**：

> 我现在能不能不看论文，画出 EdgeIM 整条 pipeline？\
> 每个箭头为什么存在？\
> 每个 representation 保存什么、丢什么？\
> 哪块我其实只是“看着熟”？\
> 哪个 claim 我还不知道证据来自哪？

这正是昨天说的“双线程”：局部继续吃，但每吃一个节点，都必须重新接回整篇，禁止形成知识孤岛。

你今天可以随手留一份特别短的东西，甚至不用正式笔记：

```text
EdgeIM 今日冷启动

1. 一句话问题：
2. 三阶段：
3. 我能讲清的：
4. 一追问就可能掉包的：
5. 我最不信的一个 claim：
6. 今天新长出的一个问题：
7. PARK：
```

**这个比电脑挂六小时更值。**

### 等你晚上真正坐到电脑前，再决定要不要跑

顺序也不要是“开机 → Agent 干活”。

而是：

```text
先做 Whole-Paper Diagnostic
        ↓
发现主要还是认知洞
        → 今天继续学，不跑

如果主链已经比较稳
        ↓
冻结下一阶段 experiment contract
        ↓
才允许开 runner
```

而且第一轮计算应该小到能人在旁边验收：smoke test、最小 baseline、一个 synthetic case。**不要一上来扔长任务让它自己跑。**

以后“挂着电脑上课时自己跑”当然会很有用，但适合的是这种任务：

> 输入冻结；代码冻结；metric 冻结；不会覆盖文件；append-only 输出；失败可见；跑完无需 Agent 自己解释和改方案。

也就是**机械 execution 已经低熵化**以后，再让机器吃你的无人值守时间。

现在这一刻还没到那里。

所以今天我甚至会明确给你一个许可：

> **可以不开电脑。**

三节课的日子，拿来做一次论文全局 consolidation，晚上还有精力再碰电脑；没精力，今天纯论文也完全不算落后。新版计划里，**认知 ownership 本来就是实验之前的硬门，不是“没空跑代码时的替代任务”。**

至于原来的进组日历，我不会现在继续在旧计划上打补丁。我们等这次 Whole-Paper Diagnostic 做完，按你真实的 `OWNED / OPEN / SEEN` 分布，重新排一次 9 月剩余路线；这样重构才是真的重构，不是计划文件又长了一层。（）

**来源:**

- [Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/edgeim-an-efficient-edge-based-process-model-discovery-technique/?utm_source=chatgpt.com)


#### You:
<time datetime="2026-09-06T23:31:10.463Z" title="2026/9/7 上午7:31:10">07:31</time>

重点参考这个文件和我们提到过的菌丝网，我说的我们自己做一个创新之类的而且得新，我们重构一下。edgeim保留是吗，那其他的呢？我们应该怎么走？

#### ChatGPT:
<time datetime="2026-09-06T23:31:11.506Z" title="2026/9/7 上午7:31:11">07:31</time>

<details>
<summary>Thought for 96 seconds</summary>

- 正在搜索网页

重构菌丝网研究方案并检索创新点

已搜索 12 个网站

重构项目方向

我会保留 EdgeIM 作为基础与归属锚点，把 Ground Truth、CrossEdgeIM 提升为核心方法线，暂时降低 sigRank 的优先级。创新重点收窄为面向安全属性的多智能体执行轨迹表示精化，并用可区分性与最小关系类型评估。

整理文档并建立多智能体安全交互主题索引

已搜索 8 个网站

规划领域制图与技术资产升级研究计划

筛选创新路线

我会把“表示是否充分”发展为主线：测试不同轨迹表示能否保留安全判定，并构造成对场景基准。该方向仍需系统查重；同时保留采样失真研究作为更快的备选成果。

构建充分性基准并调整阅读优先级

我会固定 EdgeIM 为主线，提升 Ground Truth、CrossEdgeIM 与对象中心一致性分析的优先级；将 sigRank 改为条件性阅读，并用因果、形式验证和多智能体轨迹研究检查创新边界。核心问题聚焦安全分析中的表示充分性，但新颖性仍需系统查重。

我会定义表示冲突：同一表示对应的两条轨迹，却得到不同安全判定。随后比较活动序列、代理标注、流程图、层级树、对象日志与因果图，并设计伪造、竞态、重试、委派等反例族。

已搜索 14 个网站

</details>

这次我不把它当“EdgeIM 学习计划微调”，而是直接按你说的目标重构：\*\*进组前要长出一个新的、能被你自己做出来的小创新；EdgeIM 只是培养基之一，不再是终点。\*\*我先从完整会话里把“菌丝网、鲁×孙交集、representation refinement、创新/技术资产、进组最低线”几条线重新扣起来。我已经抓到这次重构最关键的一刀了：**四论文十字架还保留，但它从“课程结构”降级成“基础培养基”；真正的主线改成“Novelty-seeking research loop”。**不过既然你明确要求“得新”，我还要把昨天我们看中的 MAS representation 方向做一次当前 prior-art 压测--不然拿昨天觉得新鲜的东西直接立项，可能已经撞车。现在有一个重要校准：昨天那个“直接把 OCEL / 因果关系搬到 Multi-Agent trace 上”已经**不能当创新本身**了。最近几个月已经出现 CTEG、Causal Past Logic、TraceCompiler、Agentproof，甚至已经有人在做 OCEL 2.0 的 multi-agent trace 生成/分析工具；所以我们真正该押的不能是“多加几个字段、画一张因果图”，而得再往下一层问：**什么信息对某类 safety claim 是必要且足够的，以及怎样用反例驱动地把 representation 长到刚刚够。**

对，这次要**真重构**。不是“EdgeIM 学完以后再顺手做点创新”，而是把整个进组计划改成：

> **以 EdgeIM 建底座，用科研菌丝网不断找 residual；最终必须长出一个经过 prior-art 审计、能亲手验证、确实有新东西的小研究成果。**

而且我刚刚又按 2026 年 9 月 7 日的最新工作扫了一遍，昨天那版路线还需要再往前推一层。

## 1. EdgeIM 保留，但它的角色变了

**保留，而且仍然深学。**

但它不再是：

> 我们最终要做的研究题。

它现在是三个东西：

**① 研究 ownership 训练器。**\
它短、完整、有可攻击的设计选择，可以一路做到 Algorithm 1、DFG、IM、Petri net、实验和 claim audit。文件里原本就把它定位成能从“看懂论文”做到“research object ownership”的主教材。

**② 你的第一块菌丝培养基。**\
EdgeIM 最值得继承的不是某个 sampling trick，而是那个母问题：

> 原始 execution 很复杂，downstream 真正需要什么 information？

文件里已经把它抽象成：

> behavioral observation → structural identification → model reconstruction，\
> 以及 coverage witness / sufficient summary / coreset 这些更一般的方法族。

**③ 鲁侧的直接锚点。**\
它能把你带进 process mining / Petri / distributed behavioral modeling，又能自然接 CrossEdgeIM、object-centric conformance、agent behavior modeling。

所以：

> **EdgeIM 不砍。**
>
> 但从“项目主角”降成“基础主干 + 问题发生器”。

---

# 2. 原来的四篇十字架，也不废，但重新排级

原来是：

```text
                 CrossEdgeIM
                      ↑
sigRank ←────── EdgeIM
                      ↓
               Ground Truth
```

这套本身很好：EdgeIM 学方法，sigRank 做横向攻击，Ground Truth 学证据，CrossEdgeIM 看后继 residual。

但现在既然目标变成**必须长一个新东西**，权重应该变成：

| 材料                                    | 新角色                                                     |    权重 |
| ------------------------------------- | ------------------------------------------------------- | ----: |
| **EdgeIM**                            | 基础主干 / ownership / representation 起点                    | ★★★★★ |
| **Ground Truth**                      | **提升为硬核心**：你的创新凭什么成立                                    | ★★★★★ |
| **CrossEdgeIM**                       | **提升**：直接提供 bottleneck migration 和 interaction residual | ★★★★☆ |
| **sigRank**                           | 降为条件分支：只有 sampling/selection 菌丝继续旺才深读                   |   ★★☆ |
| **Object-centric conformance**        | **新增硬桥梁**：multi-object interaction → conformance        | ★★★★☆ |
| **Agent trace / formal-assurance 前沿** | **新增 novelty guard**                                    | ★★★★★ |

为什么 CrossEdgeIM 现在反而比 sigRank 重要？

因为它已经把 genealogy 推到了：

```text
EdgeIM
single-org / feature aggregation
       ↓
CrossEdgeIM
cross-org hierarchical models
       ↓
剩余问题：
真正 cross-organization interaction
仍然没有显式建模
```

这正是文件里已经抓出来的 residual。

而我们昨天最后真正感兴趣的也是：

> **raw Agent behavior → ??? → safety-relevant formal model → verification**。

这两条已经接起来了。

---

# 3. 但是昨天的“创新方向”不能原样做了

这里有个非常重要的新发现。

昨天我们说，可以从：

> flat DFG 不够\
> → agent\_id\
> → message/artifact identity\
> → causal relation\
> → happens-before

一路 representation refinement。

这个**研究动作仍然对**。

但是：

### “给 Agent trace 加 causality / object-centric structure”已经不够新。

2026 年前沿现在已经非常挤：

- **TriCEGAR** 已经在做 agent trace → 自动 state abstraction → counterexample-guided refinement → probabilistic model checking；所以“把 CEGAR 搬到 agent trace abstraction”已经撞车。([arXiv](https://arxiv.org/abs/2601.22997?utm_source=chatgpt.com))
- **TraceCompiler** 已经证明 adjacency / directly-follows 对 Agent dependency 不够，并从 trace 中恢复 producer-consumer 数据依赖。([arXiv](https://arxiv.org/abs/2608.02680?utm_source=chatgpt.com))
- **Causal Past Logic** 已经明确处理 distributed agent 中“时间先后 ≠ causally visible”，并用 vector clock 在线验证。([arXiv](https://arxiv.org/abs/2605.20923?utm_source=chatgpt.com))
- **CTEG** 已经提出 Agent execution 的 causal-temporal graph formalism。([arXiv](https://arxiv.org/abs/2604.17557?utm_source=chatgpt.com))
- **Agentproof** 已经自动从 Agent frameworks 抽 workflow graph，再做静态/运行时 temporal safety verification。([arXiv](https://arxiv.org/abs/2603.20356?utm_source=chatgpt.com))
- 连 **OCEL 2.0 multi-agent traces** 都已经有人开始做生成/分析工具了。

所以不能写：

> “我们提出一种给 multi-agent trace 加 object / causal edge 的新方法。”

这个 novelty ceiling 已经塌了。

这其实正好证明了为什么我们需要**菌丝网 + Field Cartography + 持续 prior-art 搜索**，而不能坐屋里憋“创新”。

---

# 4. 那我们真正值得押的母问题，应该再抬一层

我现在会把 North Star 改成：

> ## **什么样的 execution representation，才“足以”支持某一类 Agent / Multi-Agent safety reasoning？**

注意这个问题和：

> “怎么表示 Agent trace？”

不一样。

现在大家已经有很多表示：

```text
flat sequence
workflow graph
DFG
OpenTelemetry span tree
OCEL
producer-consumer graph
causal graph
vector-clock partial order
MDP state abstraction
CTEG
...
```

新的问题是：

> **你为什么需要这些信息？**

> **少一个字段到底会让哪类 safety judgment 变得不可判？**

> **多出来的信息到底有价值，还是纯 observation overhead？**

> **对不同 safety property，所需 representation 是否不同？**

这一下重新扣回了 EdgeIM 最核心的研究问题：

> **downstream 需要什么 information？**

EdgeIM 用的是：

```text
downstream = process discovery
summary = S / E / DFR
```

我们现在把它升级成：

```text
downstream = safety property family P
summary = ?
```

这就不是生硬地：

> EdgeIM + Agent Safety。

而是把 EdgeIM 教给我们的**研究操作符**迁过去：

> **representation relative to downstream objective。**

这才是菌丝真正接上了。

---

# 5. 我现在最看好的“小创新第一候选”

先叫它一个工作名，不急着起论文名：

## **Safety-sensitive trace representation audit**

最核心的 formal question 可以极简写成：

有一个真实 execution：

$
x
$

有一个抽象表示：

$
R(x)
$

还有一条 safety property：

$
P(x)\in{safe,unsafe}
$

如果存在两个 execution：

$
x\_1,x\_2
$

满足：

$
R(x\_1)=R(x\_2)
$

但是：

$
P(x\_1)\neq P(x\_2)
$

那就说明：

> **R 对这条 safety property 不够。**

这个东西我们暂时可以叫 **safety collision**。

例如昨天那个：

```text
Run A
produce Plan_1
review Plan_1
execute Plan_1
```

和：

```text
Run B
produce Plan_1
review Plan_OLD
execute Plan_1
```

如果 representation 只有：

```text
produce → review → execute
```

两者完全相同。

但：

> execute 的 artifact 必须就是被 review 的 artifact

这个 property 对二者 verdict 不同。

所以 flat trace 不够。

---

然后我们就不凭感觉说：

> “OCEL 比 DFG 高级。”

而是实验性地比较：

```text
R0 activity sequence
↓
R1 + agent identity
↓
R2 workflow / DFG
↓
R3 parent-span execution tree
↓
R4 + message / artifact identity
↓
R5 object-centric relationships
↓
R6 causal / data dependency
↓
R7 partial-order / causal visibility
```

对于不同 failure family：

```text
review bypass
stale artifact review
wrong-message consumption
causal invisibility
parallel race
retry/replay confusion
delegation recursion
stale shared state
wrong tool-result dependency
```

问：

> **哪个 representation 第一次能够区分两个 safety-relevantly different worlds？**

---

# 6. 这比“直接提出一个新 schema”更聪明

因为现在我们还不知道最后的新贡献长什么样。

可能实验以后发现：

### 情况 A

OCEL 就全解决了。

那我们不能发明一个更复杂 schema。

但我们可能得到：

> 某些 MAS safety properties 用 object identity 已经足够，不需要完整 causal instrumentation。

这是一个**negative / sufficiency result**。

---

### 情况 B

OCEL 仍然会 collision，但 OCEL + producer-consumer dependency 能解决。

那我们有：

> **最小 augmentation**。

---

### 情况 C

即使 dependency 有了，distributed causal visibility 还区分不了。

那我们才有理由往：

> vector clocks / partial order / causal view

走。

---

### 情况 D

不同 property family 需要完全不同的 abstraction。

那可能长出：

> **property-conditioned instrumentation / representation selection**。

这甚至比“一刀切新 schema”更有研究味。

也就是说：

> **我们不预先规定创新是什么。**
>
> 我们建立一个能把创新逼出来的实验系统。

这和你文件里那套：

> `R0 → 反例 → R1 → 反例 → R2...`

其实一致；只是现在经过 prior-art 搜索以后，我们知道\*\*“counterexample-guided refinement”本身也不能声称新\*\*，因为 TriCEGAR 已经很接近。([arXiv](https://arxiv.org/abs/2601.22997?utm_source=chatgpt.com))

我们真正可能新的，是：

> **以 safety-property distinguishability 为标准，系统比较 trace representation 的 information sufficiency，并建立 paired-counterexample benchmark / adequacy criterion。**

我目前没有在这轮搜索里发现一篇正面完成这个 formulation 的论文；但这**还只是候选 novelty**，不是“查五个关键词没搜到，所以宣布全球首创”。后面必须做系统 prior-art audit。

---

# 7. 所以新进组计划不再是一条线，而是三层菌丝

我会正式改成：

```text
────────────────────────────────
LAYER A：ROOT / 根系
       必须会的基础
────────────────────────────────

EdgeIM ownership
│
├─ event / trace / log
├─ S/E/R
├─ DFG
├─ IM
├─ Petri net
├─ sampling / abstraction
└─ claim-evidence

        ↓

────────────────────────────────
LAYER B：BRIDGE / 桥接菌丝
       为 North Star 服务
────────────────────────────────

CrossEdgeIM
│
└─ cross-org interaction residual

Object-centric process
│
└─ object / relation / conformance

Formal assurance
│
├─ safety property
├─ conformance
├─ runtime verification
└─ abstraction

Causality / distributed execution
│
├─ data dependency
├─ happens-before
├─ vector clock
└─ causal visibility

        ↓

────────────────────────────────
LAYER C：FRONTIER / 创新菌丝
────────────────────────────────

Agent execution trace
       ↓
representation R
       ↓
safety property P
       ↓
是否发生 safety collision？
       ↓
YES → representation 不够
       ↓
最小 refinement
       ↓
再验证
       ↓
最终长出 contribution
```

这就是我们的新菌丝主网。

---

# 8. 原来“sampling 实验”怎么办？

**不删。降级成备用研究支。**

而且我刚查了一下，这一条其实也比我们之前想象得拥挤。

2024/2025 已经有专门保证 DFR equivalence 的 sampling framework，也有 RemainderPlus / AllBehavior 同时考虑 DFR coverage 和 frequency representativeness。([Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.8077?utm_source=chatgpt.com), [Springer](https://link.springer.com/chapter/10.1007/978-3-031-82225-4_4?utm_source=chatgpt.com))

所以：

> “EdgeIM 只保 support，我来保 frequency。”

单凭这句话，大概率也不够新。

因此原来的：

```text
EdgeIM filtering
vs fixed-K
vs significance
vs random
```

现在主要承担两个角色：

1. **科研训练 sandbox**；
2. 如果主项目卡住时的 fallback experiment。

不再默认它就是我们最后的 contribution。

这也是为什么 **sigRank 降级**。

---

# 9. Ground Truth 反而必须升权

这个现在尤其不能砍。

因为我们的新问题需要自己造很多：

> “表示看起来相同，真实 safety verdict 不同”

的世界。

那就必须知道 ground truth 是什么。

文件里原先对 Ground Truth 的定位就是：

> initial GT → controlled deviation → recording error → imperfect log，

目的是知道你看到的差异到底来自真实行为还是记录错误，而不是拿未知真实流程的数据自己解释自己。

以后我们自己的 synthetic MAS world 也应该这样：

```text
真实 interaction graph
+
真实 artifact/message dependency
+
已知 safety property
        ↓
execution traces
        ↓
人为改变 logging representation
        ↓
测试哪些 safety distinctions 消失
```

这就是它直接为创新服务的地方。

---

# 10. 我会把未来三周拆成这样

不是按“每天读几页”。

## 9/7-9/9：Root consolidation

目标：

> EdgeIM 从“我在学”变成“我能拿它思考”。

完成：

- 整篇 pipeline 能脱稿画；
- Stage 1-3 能手推；
- DFG / Petri / IM 接口清楚；
- 写出：
  - preservation object；
  - information loss；
  - downstream assumption；
  - paper claim ceiling。

同时只**浅读** CrossEdgeIM，锁死那个：

> cross-org interaction implicit

的 residual。

今天有三节课，就干这个。**完全可以不开电脑。**

---

## 9/10-9/13：Bridge sprint

只补会改变项目判断的基础：

- object-centric event log；
- object relation；
- conformance checking；
- safety property；
- causal dependency；
- happens-before / vector clock。

同时拆四篇 frontier guard：

> TriCEGAR\
> TraceCompiler\
> Causal Past Logic\
> CTEG / Agentproof 二选一深一点

不是逐页精读。

每篇只回答：

```text
它表示什么？
它要支持什么 downstream task？
它保什么？
它丢什么？
它解决了我们候选 novelty 的哪一块？
它还剩什么？
```

---

## 9/14-9/17：Counterexample laboratory

这是第一次真正“做自己的”。

不要 LLM API，不要大工程。

手造大约 10-20 组 paired worlds：

```text
same R
different safety verdict
```

逐级攻击：

```text
sequence
DFG
agent-labelled trace
span tree
object-centric log
dependency graph
causal partial order
```

到这里应该第一次得到一张：

### Representation × Property collision matrix

这张表如果做出来，已经开始不是“学习笔记”了。

---

## 9/18-9/22：Novelty Gate

这个阶段**禁止急着写新方法**。

我们拿前面的 bad cases 去反搜 related work。

每一个“我发现”都要问：

> 有没有人在某个别的术语下已经解决了？

这就是 Field Cartography 真正进入研究流程，而不是当百科全书收藏。文件里当时定义它，本来就不是“找几个大 lab”，而是追踪 Problem / Genealogy / Method / Pressure / Frontier-Residual。

只有同时满足：

```text
现有表示确实失败
+
这个 failure 对 safety claim 真有影响
+
现有工作没有正面解决
+
我们能做出最小实现
```

才能 PROMOTE 成 project。

否则砍。

---

## 9/23-月底：长第一朵“蘑菇”

根据 evidence 决定到底长什么。

可能是：

> 新的 adequacy criterion；

也可能是：

> paired-trace benchmark；

也可能是：

> minimal representation augmentation；

也可能是：

> property-conditioned trace instrumentation；

也可能实验最后证明：

> 某种复杂 representation 根本没必要。

然后做：

```text
formal definition
+
counterexample suite
+
small implementation
+
controlled synthetic experiment
+
一个真实 Agent harness sanity check
+
technical report
+
repo
```

这才算我们这轮真正结算。

---

# 11. 菌丝网也要升级一个规则

以前是：

> 一个节点向前置、后继、横向、实验长菌丝。

现在要再加一个 **Novelty pressure**：

```text
每一个研究节点
│
├─ WHAT：它是什么？
├─ WHY：为什么需要？
├─ GENEALOGY：从哪来？
├─ ALTERNATIVES：别人怎么做？
├─ FAILURE：在哪里坏？
├─ TEST：能造什么反例？
├─ PRIOR ART：谁已经解决？
└─ RESIDUAL：还剩什么是真的没人解决？
```

最后一条才允许继续吃资源。

菌丝可以乱长。

**项目不能乱长。**

Project branch 必须通过：

> `failure → evidence → prior-art gap → executable contribution`

四门。

---

# 12. 最终我们进组前希望手里是什么

不再只是：

> “我读懂 EdgeIM 了。”

也不只是：

> “我复现了一个 paper。”

而是最好形成这一套：

```text
① EdgeIM：
我能完整讲、手推、攻击。

② Research map：
我知道它在更大的 trace→structure→assurance 谱系里在哪。

③ 一个明确 residual：
我不是凭感觉说“这里可以创新”。

④ Counterexample suite：
我亲手证明旧 representation 为什么不够。

⑤ Prior-art matrix：
我知道 TraceCompiler / TriCEGAR / CPL / Agentproof 等已经做了什么。

⑥ 一个 surviving contribution：
小，但确实经过新颖性压测。

⑦ 一个 artifact：
代码 + synthetic worlds + benchmark/evaluation + report。
```

这时候面试叙事会完全变。

不是：

> “我学了老师的 EdgeIM。”

而可以是：

> “我从 EdgeIM 里开始关注一个问题：下游模型真正需要保留什么信息。沿着 CrossEdgeIM 和 object-centric process 的后继工作，我发现这个问题到了 Multi-Agent assurance 会变成 trace representation 是否足以支持 safety reasoning。后来我又查了 TraceCompiler、TriCEGAR、Causal Past Logic 等工作，发现简单的 dependency/causal abstraction 已经有人做，所以我没有直接造新 schema，而是从 safety-property distinguishability 出发构造了一组反例，系统测试不同 representations 在什么条件下发生 information collision……”

哪怕最后你只做出其中 **60%**，这个研究味也已经和：

> “我跑了一下 EdgeIM reproduction”

不是一个东西了。

**所以最终结论：EdgeIM 保留；四论文结构保留但重新分工；sampling 不再是默认创新主线；主研究方向升级为“Agent trace representation 对 safety reasoning 的信息充分性”，先做反例和 novelty audit，再让方法从 failure 里长出来。**

而今天三节课这一天，反而正适合先做 **EdgeIM Root + CrossEdgeIM residual**，不用挂电脑跑旧实验。晚上如果还有脑子，我们第一件“自己的工作”也不是开 runner--而是亲手写出 **3 组 `same representation / different safety verdict` 的 paired worlds**。这就是新版计划真正的起点。

**来源:**

- [arXiv](https://arxiv.org/abs/2601.22997?utm_source=chatgpt.com)
- [Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.8077?utm_source=chatgpt.com)


#### You:
<time datetime="2026-09-06T23:35:06.738Z" title="2026/9/7 上午7:35:06">07:35</time>

这几个文件你都读过了吗？你搜索了鲁老师和孙老师目前的最新成果的具体情况吗？我们现在重心放鲁老师这边，按照之前的划分，我们重点看哪些？怎么看？怎么学？

#### ChatGPT:
<time datetime="2026-09-06T23:35:08.975Z" title="2026/9/7 上午7:35:08">07:35</time>

<details>
<summary>Thought for 70 seconds</summary>

- 核查四份文件及最新成果
- 正在搜索网页

梳理鲁法明研究方向及EdgeIM学习进组计划

核查四份文件及最新成果

完善EdgeIM论文掌握体系并梳理研究脉络

已搜索 7 个网站

梳理文件并建立研究面试与智能体干预框架

梳理了重点方向

我会把重心放在鲁老师的主线：先掌握Petri网与过程挖掘基础，再深入EdgeIM、过程符合性和程序并发分析；贝叶斯因果与LLM工业应用作为第二梯队，持续跟踪但暂不平均用力。

已搜索 1 个网站

</details>

我这次会把两件事分开核：一是**你上传的这几份文件里到底已经定过什么路线**，二是**截至现在鲁老师/孙老师公开最新成果到底长到哪一步**。然后只按“鲁老师优先”的目标重新筛主次，不再把两边平均摊开。

对，我刚才重新核了一遍，先把“我到底读到什么程度”说清楚：

你这次提到的几份核心文件，我现在都已经定位并打开了：`更改EdgeIM学习计划和进组计划！！！.md`、`紫占盘用途和科研菌丝网构想...md`、`杂谈，有可以参考的.txt`、`只拆论文-完整会话整理.md`。其中《只拆论文-完整会话整理》我已经按完整导出结构核过；另外三份我重点读了和**进组计划、EdgeIM Mastery Gate、菌丝网、科研训练与创新路径**直接相关的部分，而不是把其中所有闲聊逐字线性重读。

而且我刚刚又**重新联网核了截至 2026-09-07 的公开最新情况**，不是只复用昨天的搜索结果。这里有一个很重要的结论：

> **如果现在重心明确放鲁老师，我们不能继续把“鲁老师 = EdgeIM / process mining”当完整地图。**
>
> EdgeIM 仍然是最适合你当前切入和训练 ownership 的主教材，但鲁老师当前真正活跃的技术面至少有四根值得认真看的枝。

---

# 一、先冻结鲁老师现在的真实地图

昨天文件里那次校准是对的，而且今天重新查官网后更确定了。

鲁老师当前官网直接写的是：

> 应急决策支持、人工智能、知识图谱与大模型、Petri 网理论与应用，并长期做 BPM；同时把成果落在矿山、化工、公共安全、海洋安全等场景。([山东科技大学计算机学院](https://cise.sdust.edu.cn/home/Page/teacher_detail/catId/30/id/509.html?utm_source=chatgpt.com))

而近两年的产出不是一条线，而是明显**多枝同时活着**。

我现在给它压成五层：

```text
鲁侧
│
├── A. Petri / 并发程序分析 / 软件验证
│
├── B. Process Mining / BPM
│      ├─ discovery
│      ├─ distributed / edge
│      ├─ richer semantics
│      └─ conformance / object-centric
│
├── C. Bayesian / causal Petri / RCA
│
├── D. ML / 时序 / 多模态 / LLM
│
└── E. 矿山安全 / 应急 / 工业系统
       ← 长期应用与真实问题来源
```

这个结构和我们文件里重新拉的鲁侧谱系一致：**Petri/程序分析、process mining、概率因果结构、现代 AI、工业安全不是替代关系，而是并行生长。**

---

# 二、如果目标是“进鲁组 + 以后还能往可信 AI / formal / agent 长”，优先级我会这样排

注意，这已经不是“按论文新不新”排序，而是综合：

- 鲁老师本人当前真实活跃度；
- 你现在的基础；
- 进组面试直接价值；
- 能不能形成自己的小创新；
- 未来迁移价值。

## 第一优先级：Process Mining → Conformance / Object-centric

### ★★★★★

这是我现在最想**提高权重**的一支。

过去我们一直把：

> EdgeIM / process discovery

当主轴。

但最新信号告诉我们，鲁侧已经不只是：

> “从 log 发现 model。”

2025 已经有一个很明确的 **object-centric conformance checking** 专利：从对象中心日志构造对象图和 process execution，处理对象间依赖，再映射到 multi-object Petri net 做 token replay，最后量化 fitness 并定位 deviation。([Google Patents](https://patents.google.com/patent/CN119477231B/zh?utm_source=chatgpt.com))

这个方向为什么特别值得你学？

因为它把一条链补完整了：

```text
execution
↓
representation
↓
process model
↓
model ↔ execution
↓
deviation / conformance
```

而你以后想碰可信系统、runtime assurance、agent behavior，这条链几乎天然能继续长：

```text
actual behavior
vs
desired / allowed behavior
```

这比“只会 discovery”更接近 assurance。

### 这一枝怎么学？

不是马上啃 OCEL 全家桶。

先按：

```text
EdgeIM
↓
普通 case-centric process discovery
↓
为什么 flat case 不够？
↓
object-centric log 到底多了什么？
↓
multi-object Petri net 表达了什么？
↓
token replay / conformance 在检查什么？
↓
什么 deviation 能被定位？
```

也就是说，**从你已有的 DFG/Petri 认知往外长，而不是另起炉灶。**

---

# 三、第二优先级：Petri → 并发程序分析 / MHP / deadlock

### ★★★★★

这一支我们之前严重低估了。

鲁老师 2025 有 **Segment-Based May-Happen-in-Parallel Analysis for C Programs**，核心不是泛泛“形式化验证”，而是：

> 构造 segment-level thread-sensitive CFG，显式编码 Pthreads 的 lock / fork / inter-procedural synchronization，推导 happens-before / conflict，再判断哪些 statements 可能并发。([Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70203?utm_source=chatgpt.com))

而 2026 官网最新又列出了：

> **Deadlock Detection and Replay of Multi-Thread Programs Based on Refined Segmentation and Lock Graphs**。([山东科技大学计算机学院](https://cise.sdust.edu.cn/home/Page/teacher_detail/catId/30/id/509.html?utm_source=chatgpt.com))

这说明：

> **并发程序分析不是鲁老师以前做过、现在停掉的老枝，而是现在仍然活跃。**

这里的研究味其实和 EdgeIM 很像：

```text
原始程序状态太大
↓
选一个 representation
↓
segment / lock graph / happens-before
↓
保住与下游 property 有关的信息
↓
检测 race / MHP / deadlock
```

你看，菌丝又接上了：

> **“representation 必须保留 downstream reasoning 所需的信息。”**

这不是硬类比，是同一个研究操作符。

### 怎么学？

这一枝不要先学 LLVM。

先按：

1. 什么叫 concurrency？
2. interleaving 为什么爆炸？
3. happens-before 是什么？
4. MHP 到底问什么 property？
5. 为什么 statement-level 太贵？
6. segment abstraction 保留了什么？
7. lock / fork / join 怎么改变可能并发关系？
8. abstraction 错了会漏什么 / 多报什么？
9. 再看实现怎么落到 LLVM。

这才符合你的菌丝法。

---

# 四、第三优先级：Bayesian / causal Petri → RCA

### ★★★★☆

这是鲁侧现在**非常值得看的增长线**，而且比“直接追大模型”更有技术内核。

2026 最新一篇很明确：

> **A New Knowledge Mining and Root Cause Analysis Methodology for Multivariate Time Series**。

它把 Petri net 和 Bayesian network 结合成 synergy-incorporated Bayesian time Petri net，显式处理：

- 时序依赖；
- AND / OR cause structure；
- causal variables；
- 非因果变量的 synergy effect；
- probabilistic evidence reasoning；

并用于太阳能板质量异常和 Tennessee-Eastman 工业过程 RCA。([IEEE JAS](https://www.ieee-jas.com/en/article/doi/10.1109/JAS.2026.125837?utm_source=chatgpt.com), [IEEE JAS](https://www.ieee-jas.com/article/doi/10.1109/JAS.2026.125837?pageType=en\&utm_source=chatgpt.com))

这条 genealogy 很漂亮：

```text
Petri
并发 / AND-OR / temporal structure
        +
Bayesian
uncertainty / evidence reasoning
        ↓
Bayesian Petri
        ↓
Bayesian Time Petri
        ↓
knowledge mining / RCA
```

它会训练你另一个非常重要的东西：

> **显式结构如何和概率、不确定性、因果推理结合。**

这个对可信 AI 的长期迁移价值非常高。

但它前置比 EdgeIM 多，所以不是今天马上开。

---

# 五、第四优先级：EdgeIM 本身

### ★★★★☆，但作为**学习主干仍是五星**

这里要区分两个评分：

**作为“鲁老师最新 frontier”**：它只是 2025 process-mining 分支的一篇，不应统治全图。

**作为“你现在第一篇主教材”**：仍然几乎最优。

因为它能用 7 页串起：

```text
event
→ trace
→ event log
→ sampling
→ representation
→ DFR / DFG
→ distributed aggregation
→ Inductive Miner
→ Petri net
→ evaluation
```

而且它自己还有足够多可攻击点。你完整会话里已经挖到了：

- support vs weight；
- timestamp conflict；
- Stage 1 物理执行位置；
- logical edge computing vs real edge deployment；
- static hash ≠ load balancing；
- low redundancy regime；
- scalability evidence 是否真的充分。

所以：

> **EdgeIM 继续深学，不是因为它代表鲁老师全部方向，而因为它是你目前最好的研究训练培养基。**

这点不要改。

---

# 六、第五优先级：LLM / 多模态 / 工业 AI

### ★★☆ 现在浅看，长期追踪

这一块确实已经不是“偶尔蹭 AI”。

官方主页已经把“人工智能、知识图谱与大模型”写成当前方向。([山东科技大学计算机学院](https://cise.sdust.edu.cn/home/Page/teacher_detail/catId/30/id/509.html?utm_source=chatgpt.com))

2026 也确实有很新的成果：

- **LLM-driven multimodal clean-coal ash prediction**：LLM + domain knowledge → structured text embedding，同时把时序转成多通道图像，再做 multimodal fusion，并加入 physical-constraint loss。([ArocMag](https://www.arocmag.cn/abs/2026.02.0048?utm_source=chatgpt.com))
- **SiamWT-CRNet**：wavelet + Siamese + cross-domain feature fusion，用于动态煤岩识别。([山东科技大学计算机学院](https://cise.sdust.edu.cn/home/page/details/catId/30/id/509.html?utm_source=chatgpt.com))
- 2026 年学校与全国重点实验室对接时，鲁老师本人展示的是矿山安全态势感知、预警、应急联动算法与平台。([山东科技大学新闻网](https://news.sdust.edu.cn/info/1160/109042.htm?utm_source=chatgpt.com))

但这里有一个非常重要的边界：

> **目前公开材料支持“鲁侧正在明显吸收 LLM / multimodal / modern ML”。**
>
> **不支持“鲁老师当前已经在做 LLM Agent Safety / Agent formal verification”。**

这条昨天文件里已经明确提醒过，今天搜索没有改变。

所以现在不应该：

> 为了我们的长期兴趣，反过来把鲁老师所有论文都解释成 Agent Safety。

这会把现实地图画歪。

---

# 七、于是我们真正应该重点读的不是“四篇”，而是“四个锚点组”

这是这次最大的结构升级。

以前：

> EdgeIM + sigRank + Ground Truth + CrossEdgeIM。

现在那四篇仍然保留，但属于 **EdgeIM 学习培养皿**。

鲁侧整体应该再加三组锚点。

| 锚点组                                      | 具体材料                                | 学到什么                                                               |    当前深度 |
| ---------------------------------------- | ----------------------------------- | ------------------------------------------------------------------ | ------: |
| **I. Discovery / representation**        | EdgeIM + duplicate-task discovery   | trace→structure、summary、DFG、IM、representation failure              |   ★★★★★ |
| **II. Conformance / object-centric**     | 2025 object-centric conformance     | multi-object interaction、execution vs model、token replay、deviation |   ★★★★☆ |
| **III. Concurrency / verification**      | 2025 MHP + 2026 deadlock replay     | happens-before、abstraction、concurrency、property reasoning          |   ★★★★☆ |
| **IV. Probabilistic / causal structure** | 2024 Bayesian PN + 2026 Time-PN RCA | AND/OR、uncertainty、causal reasoning、diagnosis                      |   ★★★☆☆ |
| **V. Modern AI / industrial**            | LLM multimodal coal + SiamWT 等      | 看鲁侧新技术往哪里汇合                                                        | ★★，持续扫描 |

其中 2025 同届 ICWS 的 duplicate-task discovery 很值得放在 EdgeIM 旁边，因为它攻击的是完全不同的 assumption：

> **相同 activity label 不一定代表相同任务。**

它最后依然是 DFG → Inductive Miner → Petri net，但首先修正日志语义。([Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/enhancing-healthcare-process-model-discovery-through-duplicate-ta/?utm_source=chatgpt.com))

所以它特别适合和 EdgeIM 并排：

```text
EdgeIM：
数据太多 / distributed
→ 怎么压缩处理

Duplicate-task：
label 语义不可靠
→ representation 怎么修正
```

这就是非常好的菌丝横向比较。

---

# 八、那“怎么看论文”也必须变

不是：

> 一篇看完 → 下一篇。

而是每篇永远按同一套 **Research Mycelium Card** 去拆。

你们文件里已经形成了菌丝原则：只有“必要前置、改变当前判断、反复出现、能形成实验”的枝才继续长，其他 PARK。

我现在把每个 paper node 固定成八问：

1. **Pressure**：旧方案到底卡在哪里？
2. **Representation**：作者把真实世界压成了什么对象？
3. **Downstream target**：这个表示最终服务哪个判断？
4. **Preserve / Lose**：它保存了什么，丢了什么？
5. **Mechanism**：作者到底做了哪一刀？
6. **Evidence**：实验真正支持哪一级 claim？
7. **Failure / residual**：什么世界里会坏？
8. **Genealogy**：这个 residual 后来长出了什么？

然后再多一张：

> **我的动作**

不是“我的感想”。

而是：

```text
我能否：
手算？
造反例？
最小实现？
改 assumption？
做对照实验？
连接另一枝？
```

这才算学进去了。

---

# 九、学习顺序我建议重构成这样

不是五条一起学。

### Phase 1：EdgeIM ownership

先把 EdgeIM 做完我们已经约定的 Mastery Gate：

> 全文可重建 + 核心算法可手推 + formal objects 真懂 + claim 可审 + assumption 可攻击 + 四档面试压缩。

注意：

> **完整实现不是硬门；完整认知 ownership 是硬门。**

---

### Phase 2：马上打开两根“鲁侧第二主枝”

不是继续在 sampling 上无限打转。

同时开：

**A. duplicate-task / object-centric conformance**

和

**B. MHP / concurrency**

每根先用**最小概念 + 一篇代表工作**。

目标不是马上学会整个领域，而是回答：

> 鲁老师另一根枝到底如何选择 representation？

如果你发现：

```text
EdgeIM：
S/E/DFR

Object-centric：
objects + relations + execution

MHP：
segments + HB + conflict
```

你会突然真正看到：

> **同一个导师组在三个不同问题上，反复做“压缩真实行为 → 留下足以支持 downstream reasoning 的结构”。**

这比我们凭空给他总结“研究风格”有证据得多。

---

### Phase 3：再开 Bayesian / causal Petri

这时候你已经懂：

> Petri 并不只是 process discovery 最终画出来的模型。

再学它如何被用于：

> uncertainty + causal reasoning + RCA。

这样不会把 Bayesian Petri 学成另一个孤岛。

---

### Phase 4：最后回看现代 AI / LLM 枝

再问：

> 鲁侧现在把现代 neural / LLM 技术吸进来了以后，原来的 structure / reasoning tradition 还剩多少？

这个问题非常值得长期观察。

例如精煤 ash 那篇用了：

> LLM + domain knowledge + multimodal fusion + physical constraint。([ArocMag](https://www.arocmag.cn/abs/2026.02.0048?utm_source=chatgpt.com))

那我们就可以问：

> 这是纯 prediction pipeline？
> 还是以后可能继续和 explicit causal / process structure 汇合？

目前不能替作者回答。

但可以放到 Field Cartography 的 `FRONTIER / WATCH`。

---

# 十、我们暂时不重点学哪些

这也是路线必须明确的一部分。

**Predictive Process Monitoring**：了解鲁侧做过，但当前不是最强新增长点，不深挖。

**纯 CV / autonomous perception**：比如自动驾驶 collaborative perception，可以知道鲁老师现代 AI 面并不窄，但不作为当前主课。

**所有矿山具体业务知识**：现在不用学矿业教材。它是应用 pressure source，不是你当前形式技术前置。

**Agent Safety 最新论文海洋**：继续扫描，但不让它抢鲁侧主线。

**sigRank**：仍然是 EdgeIM sampling 的 sparring partner，不再单独占一条主路线。

---

# 十一、所以这轮路线和我上一条还有一个微妙但重要的变化

上一条我把我们的创新候选很快推到了：

> Agent trace representation → safety sufficiency。

这个可以保留为**长期 North Star / 独立创新菌丝**。

但是如果你现在明确说：

> **“进组重心先放鲁老师。”**

那么进组前主路线应该更贴鲁侧实际生态：

```text
                 EdgeIM
                   │
      ┌────────────┼────────────┐
      ↓            ↓            ↓
 richer        object-       concurrency
 discovery     centric       / program
      │        conformance    analysis
      │            │            │
      └──────┬─────┴──────┬─────┘
             ↓            ↓
       representation   verification/
       sufficiency      diagnosis
             │            │
             └──────┬─────┘
                    ↓
          自己的小 research question
```

Agent 可以以后接进来。

**但我们的小创新不必一开始就写“Agent”。**

甚至如果你从鲁侧三根枝里先挖出一个真正有意思的：

> representation / abstraction / conformance / concurrency residual

反而更稳。

以后往 Agent 一接：

> 那叫迁移。

不是强行贴标签。

---

## 最后，把我们现在的重点压成一句非常实用的话

**当前 60%：EdgeIM + Process Mining / Conformance。**

**25%：并发程序分析 / Petri verification。**

**10%：Bayesian / causal Petri / RCA。**

**5%：LLM / multimodal / 矿山 AI frontier watch。**

不是永远这个比例。

是**你现在这个进组准备阶段**。

而学习动作统一成：

> **吃透一个节点 → 横向比较 → 找表示 → 找 preservation target → 造反例 → 看证据 → 找 residual → 才决定菌丝是否继续长。**

这跟《更改EdgeIM学习计划》里最后形成的要求完全一致：EdgeIM 是锚点，但“全文吃透只是底座，不是终点”；每个核心设计都必须横着打开方法空间，再回流成技术动作。

我现在不会急着再造一个庞大的日历。\*\*今天真正应该继续做的，就是按这个新地图把 EdgeIM 吃到 Whole-Paper ownership，同时开始给 `Object-centric Conformance` 和 `Concurrency/MHP` 建两个非常浅的菌丝入口。\*\*这样我们的鲁侧地图才开始从“一篇论文”变成“一个研究生态”。

**来源:**

- [山东科技大学计算机学院](https://cise.sdust.edu.cn/home/Page/teacher_detail/catId/30/id/509.html?utm_source=chatgpt.com)
- [Google Patents](https://patents.google.com/patent/CN119477231B/zh?utm_source=chatgpt.com)
- [Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70203?utm_source=chatgpt.com)
- [IEEE JAS](https://www.ieee-jas.com/en/article/doi/10.1109/JAS.2026.125837?utm_source=chatgpt.com)
- [ArocMag](https://www.arocmag.cn/abs/2026.02.0048?utm_source=chatgpt.com)
- [山东科技大学新闻网](https://news.sdust.edu.cn/info/1160/109042.htm?utm_source=chatgpt.com)
- [Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/enhancing-healthcare-process-model-discovery-through-duplicate-ta/?utm_source=chatgpt.com)


#### You:
<time datetime="2026-09-06T23:38:26.365Z" title="2026/9/7 上午7:38:26">07:38</time>

下载地址给我一下，或者doi

#### ChatGPT:
<time datetime="2026-09-06T23:38:47.487Z" title="2026/9/7 上午7:38:47">07:38</time>

<details>
<summary>Thought for 24 seconds</summary>

- 正在搜索网页

核对了论文链接

我正在核对上一轮列出的论文，优先整理 DOI、出版社页面和可直接下载的开放版本。专利类文献通常没有 DOI，我会单独标注公开编号或检索入口，避免把不同版本混在一起。

已搜索 7 个网站

</details>

有。我把刚才那几篇你现在最该拿到手的先按优先级列出来。

- **EdgeIM: An Efficient Edge-Based Process Model Discovery Technique**\
  DOI：`10.1109/ICWS67624.2025.00057`。这是 ICWS 2025 那篇，404-410 页。([Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/edgeim-an-efficient-edge-based-process-model-discovery-technique/?utm_source=chatgpt.com))\
  (DOI / IEEE入口)\
  这篇你其实已经有 PDF 了。

- **Enhancing Healthcare Process Model Discovery Through Duplicate Task Identification**\
  DOI：`10.1109/ICWS67624.2025.00067`。同样是 ICWS 2025，477-483 页。([Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/enhancing-healthcare-process-model-discovery-through-duplicate-ta/?utm_source=chatgpt.com))\
  (DOI入口)\
  (NOVA论文记录页)\
  NOVA 那边目前 AAM 标的是 embargo 到 **2027-09-30**，所以未必能直接公开下全文。([Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/enhancing-healthcare-process-model-discovery-through-duplicate-ta/?utm_source=chatgpt.com))

- **Segment-Based May-Happen-in-Parallel Analysis for C Programs**\
  DOI：`10.1002/cpe.70203`。这个是我们并发程序分析支线的第一篇重点。([Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70203?utm_source=chatgpt.com))\
  (论文主页)\
  (Wiley PDF入口)

- **Deadlock Detection and Replay of Multi-Thread Programs Based on Refined Segmentation and Lock Graphs**\
  DOI：`10.26599/TST.2025.9010085`。这是 **2026-06-17** 正式 online 的新成果，而且是 Open Access。([科学开放](https://www.sciopen.com/article/10.26599/TST.2025.9010085?issn=1007-0214))\
  (SciOpen全文/PDF页)\
  (DOI入口)\
  **这篇建议直接下。**

- **A New Knowledge Mining and Root Cause Analysis Methodology for Multivariate Time Series**\
  DOI：`10.1109/JAS.2026.125837`，IEEE/CAA Journal of Automatica Sinica，2026 年 5 月，13(5):1054-1067。([IEEE JAS](https://www.ieee-jas.com/en/article/doi/10.1109/JAS.2026.125837?utm_source=chatgpt.com))\
  (期刊全文页)\
  (DOI入口)

- **对象中心合规检查：基于托肯重演的对象为中心业务流程违规检查方法及系统**\
  这个不是论文，所以**没有 DOI**。授权公告号是 **CN119477231B**，申请号 **CN202510067395.5**，2025-05-27 授权；Google Patents 页面直接有 `Download PDF`。([Google Patents](https://patents.google.com/patent/CN119477231B/zh?utm_source=chatgpt.com))\
  (专利全文 + PDF下载)\
  **这个其实很值得马上存下来，因为免费、全文、而且正好接我们 object-centric / conformance 菌丝。**

另外，昨天一直提到的 **CrossEdgeIM**：

- **CrossEdgeIM: An Edge-Based Approach for Interactive Robotic Behavior Model Discovery**\
  DOI：`10.1109/MIOT.2025.3625047`，IEEE Internet of Things Magazine 9(1):55-60，2026 年 1 月正式发表。([Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/crossedgeim-an-edge-based-approach-for-interactive-robotic-behavi/))\
  (DOI入口)\
  NOVA 的 accepted manuscript 目前 embargo 到 **2027-12-03**。([Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/crossedgeim-an-edge-based-approach-for-interactive-robotic-behavi/))

**你现在真要下的话，优先顺序我建议：**

> `Deadlock 2026` → `MHP 2025` → `对象中心 conformance 专利` → `Duplicate Task` → `RCA 2026` → `CrossEdgeIM`

EdgeIM 已经在手里，不重复折腾。

其中前三个特别好，因为分别给我们三种不同的 **representation → downstream reasoning** 实例：\
**segment/HB → MHP，refined segment/lock graph → deadlock，object/execution → conformance。** 这正好能拿来和 EdgeIM 的 `S/E/DFR → process discovery` 横着拆。

**来源:**

- [Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/edgeim-an-efficient-edge-based-process-model-discovery-technique/?utm_source=chatgpt.com)
- [Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70203?utm_source=chatgpt.com)
- [科学开放](https://www.sciopen.com/article/10.26599/TST.2025.9010085?issn=1007-0214)
- [IEEE JAS](https://www.ieee-jas.com/en/article/doi/10.1109/JAS.2026.125837?utm_source=chatgpt.com)
- [Google Patents](https://patents.google.com/patent/CN119477231B/zh?utm_source=chatgpt.com)


#### You:
<time datetime="2026-09-07T00:22:31.104Z" title="2026/9/7 上午8:22:31">08:22</time>

然后呢？我们怎么处理它们？

#### ChatGPT:
<time datetime="2026-09-07T00:27:27.822Z" title="2026/9/7 上午8:27:27">08:27</time>

<details>
<summary>Thought for 27 seconds</summary>

制定了阅读路线

我不会让“相关论文集”变成逐篇精读清单，而是分层处理：先吃透 EdgeIM，再用 Duplicate Task、MHP 和 RCA 做对照，最后把 Deadlock 作为前沿延伸。

**安排产出**

每篇只提取问题定义、核心机制、实验指标、可复用组件和局限。随后建立术语表、方法对照表与研究空白，最终转化为可执行的复现和选题计划。

制定论文学习阅读与科研积累回流路线

</details>

接下来不能把它们当“下载回来排队精读”的论文堆。我要把每一篇都**分配成一个研究功能**：有的负责打基础，有的负责提供反例，有的负责桥接，有的只负责监控前沿；最终都要回流到同一张菌丝网和一个可执行的小研究问题里。我把它们重新分了：\*\*不是 7 篇论文 = 7 个学习任务，而是 3 个“研究包” + 2 个横向训练器。\*\*每个包都要产出手算、反例、最小实现或比较，不允许最后只剩摘要笔记。

对，下一步不是“下载完 → 一篇篇从第一页读到最后一页”。那样两周以后大概率会变成七篇都眼熟、没有一篇真正长进你的脑子里。

我们按之前的**科研菌丝网**来处理：EdgeIM 是第一块主培养基，其他论文承担不同功能；每读一篇，都必须回到同一个母问题：

> **现实行为被压成什么 representation？为什么这样压？下游要判断什么？保存了什么、丢了什么？在哪里失败？失败以后下一篇怎么长出来？**

这其实正是我们之前重构鲁侧地图后得到的四个入口：`Process Discovery / EdgeIM`、`Object-centric Conformance`、`Program Analysis / MHP`、`Probabilistic-Causal Petri / RCA`。之前的问题不是 EdgeIM 选错了，而是我们把鲁侧地图画窄了。

## 我现在会这样处理这批材料

| 材料                                 |               深度 | 它在菌丝网里的任务                                          | 最终必须留下什么                                              |
| ---------------------------------- | ---------------: | -------------------------------------------------- | ----------------------------------------------------- |
| **EdgeIM**                         |      **100% 深拆** | 主培养基；建立 process mining / representation / Petri 主干 | 全文脱稿重建 + 手推 + 最小实现 + claim audit + 反例                 |
| **Duplicate Task**                 |       40-50% 定向拆 | 攻击“activity label 就是 task identity”这个默认假设          | 和 EdgeIM 的 representation 对照 + 2 个反例                  |
| **Object-centric conformance 专利**  |    **70-80% 深拆** | 从 discovery 跨到 `model ↔ execution deviation`       | 一个最小多对象例子 + 手工 token replay + failure taxonomy        |
| **CrossEdgeIM**                    |       30-40% 谱系读 | 学 predecessor → residual → redesign                | 一张 EdgeIM→CrossEdgeIM 瓶颈迁移图                           |
| **MHP 2025**                       |    **70-80% 深拆** | 打开鲁侧程序分析主枝；学 concurrency abstraction               | 2-thread 手算 + happens-before + segment abstraction 反例 |
| **Deadlock 2026**                  |       40-60% 对照读 | 看 MHP/segment 思路如何继续长到另一 property                  | MHP vs deadlock representation 对照                     |
| **Bayesian Time Petri / RCA 2026** | 20-30% 第一轮 scout | 打开概率/因果 Petri 枝                                    | 只做概念地图，暂时不深实现                                         |
| **sigRank**                        |             按需调用 | EdgeIM sampling 的横向 sparring partner               | 当我们碰 sampling objective 时再打开                          |
| **Ground Truth**                   |       **贯穿全部实验** | 教我们什么实验真的能支持 claim                                 | synthetic-world / evidence contract                   |

也就是说，**现在真正并行推进的只有三个东西**：

> **EdgeIM 主干 + Object-centric/Conformance 菌丝 + Program Analysis/MHP 菌丝。**

RCA 暂时只是埋一个孢子，不让它抢时间。

这也符合我们以前给四论文十字架的定位：EdgeIM 是学习对象，sigRank、Ground Truth、CrossEdgeIM 分别是横向比较、证据方法论和纵向谱系的观察镜。

---

# 第一阶段：先把 EdgeIM 做成“坐标原点”

现在不要暂停 EdgeIM 去开七篇。

EdgeIM 继续学，但目标从“懂 Algorithm 1”升级成：

```text
现实 event log
    ↓
trace / activity
    ↓
Stage 1：filter / sampling
    ↓
S / E / DFR
    ↓
local representation
    ↓
central aggregation
    ↓
global DFG
    ↓
IM cuts / recursive decomposition
    ↓
process tree / Petri net
    ↓
fitness / precision / F-measure
```

你最后得做到我随便从其中一个箭头下刀，你能回答：

> 为什么有这一步？\
> 输入输出是什么？\
> 信息损失是什么？\
> 下游为什么还够用？\
> 如果这个假设不成立呢？

EdgeIM 之所以还值得当主教材，就是它很短，却把 event→trace→sampling→representation→DFG→distributed aggregation→IM→Petri net→evaluation 整条知识链串起来，而且本身又有大量可以攻击的点。

### EdgeIM 每学完一个节点，就强制开三个口

例如我们学到 DFG：

**横向口：**

> Duplicate Task 会告诉你：\
> “等等，你连 activity identity 都可能认错，DFG 当然也会跟着错。”

**纵向口：**

> CrossEdgeIM 会告诉你：\
> “EdgeIM 的 batch/distributed architecture 到持续在线、跨组织环境以后还够吗？”

**研究口：**

> “DFG 这个 representation 到底对哪些 downstream queries sufficient？”

所以我们以后不是：

> EdgeIM → 学完 → 下一篇。

而是：

> **EdgeIM 节点 → 菌丝发射 → 回到 EdgeIM。**

之前文件里说的正是这个：一个节点不应该只是学完打勾，而应该成为向前置、横向方法、后继谱系和实验发射问题的接口。

---

# 第二阶段：EdgeIM 一过 DFG/Petri 基础，立刻插 Object-centric Conformance

这是我现在认为**第一根真正值得长粗的旁枝**。

因为它让你第一次看到：

### EdgeIM 在问

> 从 execution log 里**发现**什么 process structure？

而 conformance 在问：

> 已经有一个 process model，现在实际 execution **偏离它了吗？**

从：

```text
log → model
```

变成：

```text
log ↔ model
```

研究问题完全变了。

更重要的是 object-centric。

普通 event log 很容易默认：

```text
一个 case
里面一串 activity
```

但真实流程可能有：

```text
订单 O1
商品 I3
客户 C7
付款 P9
```

一个 event 同时牵涉多个 object。

所以我们第一轮根本不用学完 OCEL 标准。

我会给你造一个**两订单 + 两商品 + 一付款**的小世界。

亲手做三次：

```text
普通 flat trace
        ↓
你发现什么信息没了？

加 object identity
        ↓
能区分什么了？

再建立 multi-object execution
        ↓
token replay 能抓什么 deviation？
```

做完这个以后，你才正式去读专利。

否则第一页就是：

> binding / multi-object Petri / object execution……

你只会名词过脑。

这一枝真正要训练的是：

> **representation failure → richer representation → downstream analysis capability。**

---

# 第三阶段：同时打开 MHP，但它不是另一门毫不相关的课

这一点很重要。

MHP 看起来像：

> C 程序、Pthreads、CFG。

和 process mining 八竿子打不着。

但我们用菌丝眼睛看：

### EdgeIM

```text
raw event log 太大
↓
DFR / DFG abstraction
↓
保留 process discovery 所需结构
```

### MHP

```text
raw interleaving/state space 太大
↓
segment / HB / synchronization abstraction
↓
保留 concurrency reasoning 所需结构
```

于是共享母问题暴露了：

# **什么 abstraction 对 downstream property 足够？**

这个才是我们要学走的 research operator。

所以 MHP 也不从论文开读。

先做一个：

```text
Thread 1:
A
lock(m)
B
unlock(m)
C

Thread 2:
D
lock(m)
E
unlock(m)
F
```

我们亲自问：

> A 和 D 能不能同时？\
> B 和 E 呢？\
> C 和 E 呢？\
> fork/join 又会怎样？

然后自然长：

> program order\
> synchronization\
> happens-before\
> conflict\
> may-happen-in-parallel。

再去看作者为什么要造 segment。

这样你才能判断：

> segment 是聪明 abstraction，还是论文给了什么就背什么。

---

# 第四阶段：Deadlock 2026 不单独学，而是拿来“看下一篇怎么长出来”

这篇最适合和 MHP 连着用。

不要问：

> Deadlock 论文算法是什么？

先问：

> **同样面对 multithread behavior，MHP 和 deadlock detection 为什么不能直接共用完全相同的 representation？**

因为 downstream property 变了。

MHP 关心：

> 两段 execution 有没有可能同时发生？

Deadlock 关心：

> 是否可能形成循环等待，并且怎么重现这个错误？

于是 representation 所需 information 也会变化。

这里会第一次形成一个很漂亮的矩阵：

```text
真实系统         abstraction             downstream

Event log   →   DFR / DFG            → process discovery
Objects     →   object execution      → conformance
Threads     →   segment + HB          → MHP
Locks       →   segment + lock graph  → deadlock
```

**这张表非常重要。**

因为这已经开始脱离“我读了鲁老师四篇论文”。

你是在重建鲁侧反复出现的**方法模式**。

---

# 第五阶段：CrossEdgeIM 专门学“研究是怎么长下一篇的”

这篇不能像主论文一样精读。

我们只追一件事：

```text
EdgeIM 做完了什么？
        ↓
它还留下什么现实条件没解决？
        ↓
CrossEdgeIM 改了哪一层？
        ↓
旧 bottleneck 去哪了？
        ↓
新 bottleneck 又是什么？
```

已有文件已经帮我们抓到了一个特别好的例子：

```text
EdgeIM：
case filtering
→ edge feature
→ central global DFG
→ central discovery

CrossEdgeIM：
activity node 在线维护
→ ΔDFR / ΔS / ΔE
→ organization-level DFG
→ organization-level discovery
→ central model merging
```

然后自然出现下一问：

> **真正跨组织 interaction 怎么表示？**

这就是 residual。

CrossEdgeIM 的学习成果不应该是一页 summary。

应该是一张：

# `Predecessor → Pressure → Redesign → New Residual`

谱系卡。

---

# 第六阶段：RCA 先只开地图，不进深水

Bayesian Time Petri 那篇现在不要硬啃。

第一轮只让你明白：

> Petri 不是“画流程图的东西”。

它还能和：

```text
probability
causal dependence
time
evidence
```

结合以后，用于 diagnosis / root-cause reasoning。

我们只先补：

> Bayesian network 是什么；\
> conditional probability 是什么；\
> AND/OR causal structure 为什么 Petri 擅长；\
> uncertainty 又为什么单靠普通 Petri 不够。

然后论文只回答：

> 作者把哪两个 representation 拼起来？\
> 为什么？\
> 拼完新增了什么能力？

到这里 STOP。

如果以后菌丝发现：

> probabilistic assurance / causal diagnosis

真的开始与我们自己的问题连接，再升权。

---

# 最关键的是：每篇论文必须产出同样的“菌丝卡”

以后**禁止普通论文摘要**成为主要产物。

一篇论文处理结束，我只认这几个字段：

```text
PAPER NODE

1. Pressure
旧世界到底哪里坏了？

2. Task
作者形式上要解决什么？

3. Representation
真实世界被压成什么对象？

4. Preserve / Lose
保了什么？丢了什么？

5. Downstream
这个 representation 最终要支持什么判断？

6. Mechanism
作者利用了哪个结构 / invariant？

7. Evidence
实验到底支持到哪一级？

8. Failure
我能造出什么 bad case？

9. Genealogy
前身是谁？后继 / residual 是什么？

10. MY ACTION
我亲手做了什么？
- 手算
- 反例
- 小实现
- controlled comparison
```

前九项都漂亮，但第十项空着：

> **不算完成。**

因为我们之前已经明确过：每一圈阅读必须回流成自己的技术动作，而不是做完 comparison table 就结束。

---

# 最后才进入“创新寻找”

这里我想纠正一个很容易犯的错误：

不要这样：

> 读完七篇\
> ↓\
> “现在想一个创新。”

应该是：

```text
Paper A
↓
发现 assumption A
↓
造反例
↓
Paper B 恰好解决了一部分
↓
但引入 residual B
↓
Paper C 用另一种 representation
↓
做 controlled comparison
↓
发现一个稳定 failure
↓
查 prior art
↓
还没人正面解决？
↓
才 PROMOTE 成自己的研究问题
```

也就是说：

# **创新不是第八个学习任务。**

它是菌丝碰撞以后长出来的蘑菇。

这也符合我们之前整个进组计划真正想训练的东西：

> 看到已有设计 → 理解 → 横向比较 → 找 assumption → 最小实验 → 形成判断 → issue 才可能变 contribution。

---

所以你**今天**实际上不用打开七篇。

今天三节课，我甚至建议只做两件事：

> **主线：继续 EdgeIM，推进 Whole-Paper ownership。**

同时遇到 `representation / DFG / identity / interaction` 这种节点时，我会主动告诉你：

> **“这里该打开 Duplicate Task / Object-centric 那根菌丝了。”**

遇到：

> concurrency / parallel / synchronization

我再把 **MHP** 插进来。

换句话说，**你不用自己管理七篇论文的切换。**

我们以后按当前知识节点走；该调用哪篇镜子，我负责把它拉进来。这样菌丝会长，但不会又长成七个同时进行的坑。


#### You:
<time datetime="2026-09-07T00:49:12.874Z" title="2026/9/7 上午8:49:12">08:49</time>

@深度研究 深度看看这几篇论文的具体情况和横向的可以对比与深入的其他工作，按照我们自己的路线长一点点

#### ChatGPT:
<time datetime="2026-09-07T00:49:13.899Z" title="2026/9/7 上午8:49:13">08:49</time>

<details>
<summary>Thought for 256 seconds</summary>

- 正在搜索网页

深入研究EdgeIM及横向迁移研究脉络

已搜索 10 个网站

筛选了研究材料

我正在优先使用可访问的网页和论文内容，并检查关键文献是否需要进一步核对。若材料仅提供摘要，我会明确区分已验证结论与推测，避免把有限证据说得过满。

已搜索 2 个网站

拓展文献并收束研究路线，核对方法与采样并定位跨组织分支

我正在将对象中心合规检查与动态身份关系视为前沿参照，避免把“加入对象身份”当作新意；并把 MHP、死锁分析拆成并发抽象、同步语义与精度权衡来学习。

我正在把 Lu 老师相关路线定位为两条互补分支：一条修复任务语义后再发现模型，另一条在边缘分层聚合；跨组织协作已有显式建模谱系，不能误判为空白。

我正在补齐横向谱系：DFR 等价保证、分布代表性、行为覆盖和下游模型质量并不相同；同时将 EdgeAlpha、EdgeMiner 纳入分布式架构比较，避免把 EdgeIM 的贡献说得过满。

我正在把已确认的论文信息与项目中的阅读假设分开：EdgeIM 的集合覆盖不等于频率或模型等价，sigRank 则以活动与直接跟随关系的重要性给轨迹排序，再按比例采样。

我正在把文献阅读收束为一条可执行主线：运行痕迹、结构恢复、表示、检查、系统改变与反馈，并用替代方法、假设、失败例和最小实验逐篇验证。

我正在围绕既定路线补充横向对比：以 EdgeIM 为主线，连接跨组织协作、医疗场景与表示学习工作，重点寻找机制、假设和失败边界上的小创新。

控制研究范围并规划渐进路线

我正在把路线压缩成三层：丰富语义与精确性、资源约束下的轻量摘要、面向下游属性的验证。接下来按九个学习单元推进，每单元设明确停点，避免菌丝失控。

我会把采样分布式发现设为主线，对象中心语义作为外圈参照；暂不纳入 Agentproof、TraceCompiler、CPL，先验证表示是否满足下游属性，再讨论创新性。

组织了研究证据

我会明确区分文件已定、本轮核验与我们的推断/PARK，并围绕三条主线比较：EdgeIM 摘要压缩、对象中心语义、程序分析验证，避免新增过多分支。

已搜索 7 个网站

</details>

我会沿着我们已经定下的“**representation → downstream property → preserve/lose → residual → prior art → 可执行小实验**”这条菌丝主线来做，不会把它扩成大而全综述。先把文件里已经定过的路线、几篇论文各自的位置重新抽出来，再去查同方向最值得横向比较的最新工作。第一轮横向图已经有点形状了：sampling 这边出现了一个很关键的“前身-平行路线”--2024 的 **Sampling business process event logs with guarantees** 直接把 DFR equivalence 当保证，2025 的 **RemainderPlus / AllBehavior** 又把“频次代表性”和“行为覆盖”拆成两种 objective。这个正好能拿来压 EdgeIM 的 `support vs weight vs downstream model`，比只拿 sigRank 单挑更完整。有一个比“再多找几篇”更重要的修正冒出来了：\*\*CrossEdgeIM 的“跨组织 interaction 没显式表示”可以作为它自身的 residual，但不能写成“鲁/曾/刘这条谱系没人做过 interaction 表示”。\*\*他们更早在 cross-organization emergency / healthcare process mining 里就用过 **message/resource-aware Petri nets + collaboration patterns** 显式建跨组织交互。也就是说，我们得研究“为什么后来 Edge/CrossEdgeIM 又选择了更轻的 representation”，这比简单说“下一步加 interaction”有意思得多。

我这轮按我们已经定下的菌丝规则，重新把 **EdgeIM / sigRank / CrossEdgeIM / Duplicate Task / Object-centric conformance / MHP / Deadlock / RCA** 往前后左右都查了一圈。先给结论：

> **路线不用继续横向铺很多篇，而是出现了三条明显可以长粗的菌丝。**
>
> 其中有一条比我们昨天想的更有意思：\
> **“丰富的交互语义”与“边缘/分布式条件下的轻量表示”之间的张力。**
>
> 这可能比直接往 Agent trace 上套新 schema，更贴鲁侧谱系，也更容易从现有工作里长出一个自己的小研究问题。

而且有几个地方必须修正我们之前的理解。

文件里原本定的总原则仍然成立：EdgeIM 是学习对象，其他论文不是平均精读，而是横向方法、证据方法论和 genealogy 镜头；每一圈阅读必须回流到反例、实现或实验，新的 residual 在 prior-art audit 前只能 PARK。

---

# 一、第一条菌丝：EdgeIM 不能再单独看，它其实处在一个很完整的 sampling / distributed discovery 方法空间里

这是这次查完以后变化最大的地方之一。

我们原来看到：

```text
EdgeIM
│
├─ coverage
├─ S / E / DFR
├─ filtering
└─ distributed discovery
```

现在应该扩成：

```text
                 Event-log reduction / distributed discovery
                                │
        ┌───────────────────────┼─────────────────────────┐
        │                       │                         │
  保什么行为？              怎么选 trace？             计算放哪里？
        │                       │                         │
 DFR equivalence         significance / coverage      central
 support / frequency     distribution / budget       federated
        │                       │                      edge / stream
        ↓                       ↓                         ↓
Sampling w/ Guarantees     sigRank                  EdgeMiner
RemainderPlus              AllBehavior              Federated Alpha+
EdgeIM                     EdgeIM                   EdgeIM
                                                     CrossEdgeIM
```

这不是我为了画图硬拼的。现在相关工作真的把这几个 design axis 分别做出来了。

## 1.1 EdgeIM 之前，已经有“Sampling with Guarantees”

2024 的 **Sampling business process event logs with guarantees** 已经明确把 **DFR 作为基本行为单元**，目标是让原日志和 sampled log 保持 DFR equivalence，并给出了七种 sampling strategies。([Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.8077?utm_source=chatgpt.com), [Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpe.8077?utm_source=chatgpt.com))

这会直接改变我们怎么讲 EdgeIM 的 novelty。

以后不能笼统说：

> EdgeIM 的创新是想到“保存 DFR 而不是完整日志”。

至少不能这么讲。

更准确的问题应该是：

> 2024 那篇已经有 DFR-preserving sampling，那么 EdgeIM **在 edge/distributed process discovery 的具体 setting 下，为什么又采用 S/E/DFR witness-based filtering？架构、计算位置、采样过程和 downstream interface 到底发生了什么变化？**

这才是 genealogy。

而且它让我们之前一直追的：

> `support preserved ≠ weight preserved ≠ downstream model preserved`

变得更重要了。

你们案例册已经专门写了：EdgeIM 的保留规则利用集合覆盖的幂等性，能讨论 feature support 的 witness；但 Stage 2 的计数是加法，因此 support 相同不能推出 frequency 相同，更不能直接推出 downstream model 相同。

### 所以这篇不用全精读

我们只定向读三个东西：

> **Guarantee 到底形式化保证什么；sample size 怎么产生；这个 guarantee 与 downstream discovery quality 之间有什么边界。**

然后和 EdgeIM 做一张非常严格的：

```text
preservation object
guarantee
budget
downstream consumer
```

四格比较。

---

## 1.2 RemainderPlus / AllBehavior 把我们想问的问题直接拆开了

2025 的 **Representative Sampling in Process Mining** 非常值得作为第二面镜子。

因为它恰好造了两个不同 objective：

**RemainderPlus** 更强调原日志的 trace / behavior distribution 代表性；

**AllBehavior** 更强调 DFR/DFP coverage，而且覆盖完以后再用 RemainderPlus 填满固定 sample budget。([Springer](https://link.springer.com/chapter/10.1007/978-3-031-82225-4_4))

最有意思的不是算法本身，而是它的实验结果：

> sample-level representativeness 更好的方法，不一定在 process discovery / conformance 上更好；AllBehavior 在一些 downstream task 上反而更强。([Springer](https://link.springer.com/chapter/10.1007/978-3-031-82225-4_4?utm_source=chatgpt.com), [Springer](https://link.springer.com/chapter/10.1007/978-3-031-82225-4_4))

这正好打中我们之前一直强调的一件事：

> **不要把 surrogate objective 当最终 objective。**

文件里我们本来就已经把这个能力作为 sigRank 镜头的训练目标。

现在变成了一个真正的方法 landscape：

| 工作                     | 主要选择思想                          | 明显值得问的东西                                        | 我们怎么用          |
| ---------------------- | ------------------------------- | ----------------------------------------------- | -------------- |
| Sampling w/ Guarantees | 保 DFR equivalence               | guarantee 到底到哪一级                                | EdgeIM 的前身/平行线 |
| EdgeIM                 | 新 S/E/DFR witness 决定 trace 去留   | support→frequency→model 的接口                     | **主干**         |
| sigRank                | trace significance              | 高频 significance 是否牺牲 rare-but-critical behavior | 横向攻击           |
| RemainderPlus          | distribution representativeness | 表面代表性与 downstream 是否一致                          | objective 对照   |
| AllBehavior            | behavior coverage               | coverage 是否更适合 discovery                        | objective 对照   |
| random/fixed ratio     | budget first                    | 没有 structural awareness 会怎样                     | baseline       |

sigRank 2026 正式版也确实把 trace significance 作为核心，并在 12 个公开日志上评价 sample quality / process discovery。([Run UNL](https://run.unl.pt/server/api/core/bitstreams/4d685e7f-5077-4a1d-8b35-8eb41f27fda2/content?utm_source=chatgpt.com), [Run UNL](https://run.unl.pt/entities/publication/cfdff734-3844-41a6-952e-74e55e4d092e?utm_source=chatgpt.com))

### 这条菌丝最终不是让你学五套 sampling 算法

而是学会问：

$
\text{sample quality}
\neq
\text{structural coverage}
\neq
\text{distribution fidelity}
\neq
\text{model quality}
$

这四个量什么时候相关、什么时候翻脸。

---

# 二、distributed 那一半也出现了非常好的横向对照

EdgeIM 的另一个大设计变量不是 sampling，而是：

> **计算究竟在哪里发生？传输的究竟是什么？**

这里我现在建议只保留两个特别干净的对照。

### EdgeMiner：直接在数据源处理 streaming events

EdgeMiner 让 sensor node 自己跟踪事件及其 predecessor/successor，并局部聚合 direct successions，避免把 raw events 全送到中央；它处理的是实时 event stream，还专门分析 correctness 和 communication overhead。([arXiv](https://arxiv.org/abs/2405.03426?utm_source=chatgpt.com))

于是你可以问：

```text
EdgeIM：
trace → filter → local features → aggregate

EdgeMiner：
event stream → predecessor/successor inference
             → local direct-successions
             → aggregate
```

它们表面都叫 edge process mining，但 abstraction boundary 完全不一样。

一个 trace/case-oriented。

一个 event/stream-oriented。

这正好能帮我们把：

> batch / streaming / online / incremental

真正挂回知识图谱，而不是单独背概念。

---

### Federated Alpha+：另一端极端--我要 distributed，但尽量保中央算法的等价性

2025 的 Federated Alpha+ 不以“采样减少信息”为主，而是让数据留在各医疗机构，交换 aggregate information，并且论文专门给出了 distributed 与 centralized algorithm 的结果等价证明。([哈德斯菲尔德大学研究门户](https://pure.hud.ac.uk/en/publications/towards-distributed-process-discovery-inhealthcare-testing-andpro/?utm_source=chatgpt.com), [UPV销售门户](https://aplicat.upv.es/exploraupv/ficha-publicacion/publicacion/557974?utm_source=chatgpt.com))

于是一下出现两个不同哲学：

```text
EdgeIM
愿意做信息压缩 / selection
→ 换 efficiency

Federated Alpha+
尽量保持 centralized result equivalence
→ 数据不移动，但计算协议变
```

这个比较特别适合训练你以后做系统时最重要的一种 taste：

> **你是在做 approximation，还是 decomposition？**

两者经常都被写成：

> “distributed / efficient”。

但数学性质完全不是一回事。

---

# 三、第二条菌丝变得比昨天更有意思：不是“object-centric 很新”，而是“语义到底应该保多丰富”

先看 Duplicate Task。

鲁老师署名的 2025 **Enhancing Healthcare Process Model Discovery Through Duplicate Task Identification** 做的并不是换掉 DFG/IM。

它先攻击更前面的问题：

> **同一个 activity label，真的一定是同一种 task 吗？**

方法先根据 contextual relations 识别 duplicate task sequence，再利用从日志构造的 transition system 对任务重新标注，之后才构造 DFG、最后仍用 Inductive Miner 得到 Petri net。([Run UNL](https://run.unl.pt/handle/10362/191476?utm_source=chatgpt.com), [Universidade NOVA de Lisboa](https://novaresearch.unl.pt/en/publications/enhancing-healthcare-process-model-discovery-through-duplicate-ta/?utm_source=chatgpt.com))

这个特别漂亮。

EdgeIM 问：

> 日志这么大，什么能删？

Duplicate Task 问：

> 等等，你删之前，**event label 的语义本身对吗？**

所以我们知识图谱应该第一次正式增加：

```text
representation compression
↑
必须有一个前置节点：

semantic identity / observational equivalence
```

两个 event 名字一样，不代表它们对 downstream model 是 interchangeable。

这其实已经开始接近我们以后真正关心的：

> **什么时候两个 observation 可以安全地被视为同一个东西？**

---

# 四、然后进 Object-centric：这条菌丝值得长粗，但不能把“加 object identity”当创新

我们之前看到鲁侧 object-centric conformance 那条线，动机很明确：

> 把涉及多个对象的过程 flatten 成单 case trace，会损失对象之间 interaction，导致 deviation detection 和 source attribution 不准确。

相关方案从 object dependencies 建 object graph / process executions，再把 execution 映到 multi-object Petri net 上，通过 token replay 检查 deviation。

但现在查到 2026 前沿以后，要加一条非常强的 novelty guard：

**Object-centric process mining 已经继续长到了 dynamic identity relations。**

2026 的 **Noise-resistant discovery of identifier-sound object-centric process models with dynamic identity relations** 已经正式研究：

> 不只是“object 有 ID”，而是 object identity 之间的关系会在过程中动态变化，并要求发现出来的模型满足 identifier-soundness。([Springer](https://link.springer.com/article/10.1007/s44311-026-00052-w))

另一条 object-centric conformance 工作甚至已经把 synchronization / identity dependency 放进 alignment formalization。([arXiv](https://arxiv.org/abs/2312.08537))

所以：

> `flat trace → 加 object ID`

已经只能作为学习例子。

绝对不能拿来当我们自己的 novelty。

---

# 五、但是！这里挖出了这轮最有价值的新连接

我们之前从 CrossEdgeIM 看到一个 residual：

> 顶层合并 organization models，但 inter-organization interaction 没有被显式完整表示。

一开始很容易自然想到：

> 那我们把 message / resource / interaction 加回来不就好了？

**不能这么说了。**

因为沿着鲁/曾/刘这套更老的 cross-organization process mining 谱系往前找，早就有人干过。

2020 的 **Cross-Organization Emergency Response Process Mining** 明确：

- 给 Petri net 加 resource 和 message attributes，形成 RMPN；
- 分别发现各 organization 的内部模型；
- 显式定义三种 collaboration pattern：
  - message exchange；
  - resource sharing；
  - task synchronization；
- 最后把组织模型和 collaboration patterns 合并成全局 CERP model。([Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1155/2020/8836007))

甚至论文自己还回顾了更早的跨组织医疗/工作流研究，其中也已经存在 message/resource/task collaboration 类的显式建模。([Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1155/2020/8836007))

### 这反而让问题变得更漂亮了。

不是：

> “以前没人建 interaction，现在我们加 interaction。”

而是：

> **“这条研究谱系以前明明知道如何表示丰富的 cross-organization interaction，为什么到了 EdgeIM / CrossEdgeIM 这种 edge / distributed / robotic setting，却选择了明显更轻量、更局部的表示和模型合并？”**

这才是一个有味道的问题。

可能的 pressure 有很多：

```text
rich semantics
message
resource
sync
identity
        ↓
表达能力强

但是
        ↓

更高 logging requirement
更高 communication cost
更复杂 online maintenance
更难 privacy preservation
更复杂 composition
更重 discovery / conformance
```

而另一边：

```text
local DFR
local model
incremental delta
simple merge
        ↓
轻量、distributed-friendly

但是
        ↓
interaction fidelity 下降？
```

注意：后半句现在只是**我们的 hypothesis**，不是已经证明的事实。

但它构成了一个真正值得测试的 tension：

# **semantic richness ↔ distributed efficiency**

这条线我现在会正式升成菌丝网里的 **PARK-A，最高优先级研究候选**。

---

# 六、我们甚至已经可以造第一个非常小的反例世界了

不是立刻写论文，是研究问题发生器。

设有两个 organization：

```text
Org A:
a → b

Org B:
x → y
```

现在造两个世界。

World 1：

```text
b sends m1
x receives m1
```

World 2：

```text
b sends m2
x receives m1
```

如果你的 representation 只保存：

```text
local model A
+
local model B
```

两个世界可能看起来一样。

但如果 downstream query 是：

> “B 的 x 是否消费了 A 的 b 产生的正确 message？”

答案不同。

那么我们就问：

> **最小要增加什么 summary，才能区分这两个世界？**

完整 RMPN？

message ID？

message type？

send/receive pair？

dependency edge？

还是只需要一个非常小的 inter-org interaction sketch？

这一下，就把：

> EdgeIM\
> CrossEdgeIM\
> 老 cross-org RMPN\
> object-centric identity\
> conformance

五根菌丝接起来了。

而且仍然是鲁侧自己的问题生态，不需要强行跳去 Agent Safety。

未来如果迁去 Agent：

```text
organization → agent
message → tool/artifact/message
```

那是**后面的 transfer audit**。

现在先别贴标签。

---

# 七、第三条菌丝：MHP + Deadlock，其实是另一套特别干净的“representation sufficiency”教材

这边我查完以后，反而觉得应该比之前更认真学。

## MHP 2025

**Segment-Based May-Happen-in-Parallel Analysis for C Programs** 的 task 很明确：

> 判断两个 program statements 是否可能并行执行。

作者指出已有分析在 lock 与 thread creation coupling、inter-procedural locks 上可能损失精度，于是构造 **Segmented Thread-sensitive CFG (STCFG)**：

```text
statements
↓ group
segments
↓ add context
Pthreads fork/join/lock semantics
↓
HB relationship
+
conflict relationship
↓
statement-pair MHP
```

它不是单纯为了让图变小。

关键 assumption 是：

> **同一个 segment 内的 statements 可以共享需要用于 concurrency reasoning 的性质。**

这样才能用 segment relation 推 statement relation。([Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70203?utm_source=chatgpt.com), [Wiley Online Library](https://onlinelibrary.wiley.com/doi/pdf/10.1002/cpe.70203?utm_source=chatgpt.com))

这和 EdgeIM 的研究动作特别像：

```text
完整对象太复杂
↓
选 representation / grouping
↓
保 downstream property 必要 information
↓
在压缩表示上推理
```

但这里 downstream 已经不是 discovery。

而是：

> **property checking。**

这非常重要。

---

# 八、Deadlock 线甚至已经能看出清楚的 genealogy

鲁老师 2024 有一篇：

**Petri Net Unfolding-Based Detection and Replay of Program Deadlocks**

它从 runtime trace 构建 program Petri net，然后用 unfolding 检测潜在 dead marking，再生成 deterministic schedule replay；核心 motivation 是一般 lock graph 的 information loss 会制造 deadlock false positive。([ResearchGate](https://www.researchgate.net/publication/379546660_Petri_Net_Unfolding-based_Detection_and_Replay_of_Program_Deadlocks?utm_source=chatgpt.com), [开放获取期刊目录](https://doaj.org/article/5d971f31dd2447448367d44d6288abb0?utm_source=chatgpt.com))

到了 2026 的 **Deadlock Detection and Replay ... Based on Refined Segmentation and Lock Graphs**，路线又继续修改 representation，而不是简单重复 Petri unfolding。

所以这条 genealogy 大概可以重建成：

```text
lock graph
↓
信息不够 → false positives

2024
runtime trace
→ Petri net
→ unfolding
→ candidate deadlock
→ deterministic replay

          ↓ 又发现成本 / representation 问题？

2026
refined segment
+
extended lock information
+
deadlock detection / replay
```

这里特别值得我们以后精读 2024 → 2026 两篇，问：

> **作者为什么从“更 expressive 的 Petri unfolding”又转向 refined segment / lock graph？**

这跟上面的：

> rich cross-org semantics → lightweight Edge representation

居然又出现同一个味道。

我暂时不说这是鲁老师统一的“研究哲学”--证据还不够。

但是它至少是一个值得进一步验证的重复 pattern：

# **不是 representation 越强越好，而是寻找“对当前 property 足够、但计算上更便宜”的 representation。**

这个值得进我们的研究操作符案例册。

---

# 九、RCA 这根菌丝现在也终于找到真正的前身了

这次顺手把它 genealogy 补完整了。

2024：

**Synergy-incorporated Bayesian Petri Net**

已经把 Bayesian network 与 Petri net 结合，目标包括显式表示 AND relation 以及非因果变量对推理规则的 synergy effect。DOI 是 `10.1016/j.ins.2024.121019`。([新泽西工学院数字库](https://digitalcommons.njit.edu/fac_pubs/170/?utm_source=chatgpt.com), [科学直通车](https://www.sciencedirect.com/science/article/pii/S0020025524009332?utm_source=chatgpt.com))

2026：

**A New Knowledge Mining and Root Cause Analysis Methodology for Multivariate Time Series**

进一步变成 **synergy-incorporated Bayesian time Petri net**，加入 temporal dependencies，用于 multivariate time-series knowledge mining / RCA。([IEEE JAS](https://www.ieee-jas.com/en/article/doi/10.1109/JAS.2026.125837?utm_source=chatgpt.com), [IEEE JAS](https://www.ieee-jas.com/en/article/2026/5?utm_source=chatgpt.com))

所以这里是很清楚的：

```text
Bayesian Network
    │
    ├─ probabilistic reasoning
    │
    ×
    │
Petri Net
    ├─ AND/OR structure
    └─ process structure
         ↓
2024 Bayesian Petri
         ↓
time / multivariate series / RCA pressure
         ↓
2026 Bayesian Time Petri
```

### 但这一枝现在仍然只种孢子

不是现在开课。

因为一旦正式进去，你马上要补：

> conditional probability、BN、causal vs probabilistic dependency、temporal model、Petri semantics……

会抢主线。

目前只需要知道：

> 鲁侧另一个非常稳定的研究动作，是让 formal structure 获得 uncertainty / evidence reasoning 能力。

PARK。

---

# 十、所以现在我们的菌丝网，我会正式改成这样

```text
                         鲁侧：behavior → representation → reasoning
                                        │
              ┌─────────────────────────┼────────────────────────┐
              │                         │                        │
        PROCESS MINING            PROGRAM ANALYSIS         CAUSAL / RCA
              │                         │                        │
              │                         │                        │
   ┌──────────┴─────────┐        STCFG / segment          Bayesian Petri
   │                    │              │                        │
sampling             semantics          HB                    Time
   │                    │              │                        │
DFR guarantee       duplicate task     MHP                      RCA
coverage            object identity     │
significance        interaction         │
distribution            │            deadlock
   │                    │            / replay
   │                    │
EdgeIM             object-centric
   │                conformance
distributed              │
   │                     │
CrossEdgeIM        rich cross-org semantics
   │                     │
   └──────────────┬──────┘
                  │
       ★ PARK-A：轻量 distributed representation
              到底该保多少 interaction？
```

最底下这个 ★ 是**我们这轮真正新长出来的一点点**。

不是论文题目。

不是 novelty claim。

而是一个值得继续喂证据的 research question。

---

# 十一、这会改变我们接下来怎么读论文

我们不新增十篇必读。

下一阶段我建议这样执行：

### 当前主任务仍是 EdgeIM ownership

继续把：

```text
event log
→ sampling
→ S/E/DFR
→ local DFG
→ aggregation
→ IM
→ Petri
→ evaluation
```

整个打穿。

这是不能绕的。你们完整会话里定的目标本来就是从 paper comprehension 做到 research-object ownership。

### 遇到 Sampling 节点时，只开三面镜子

不是全读：

**Sampling with Guarantees**：看 guarantee。

**sigRank**：看 importance。

**RemainderPlus / AllBehavior**：看 distribution vs coverage。

读完我们就做一张：

```text
Objective × Representation × Budget × Guarantee × Downstream
```

表，然后关掉。

### 遇到 DFG / activity identity 节点

打开：

> **Duplicate Task**

只追：

> label 为什么不够？transition context 补了什么？

然后开始 Object-centric 前置。

### EdgeIM 全文比较稳以后

才开：

> **Object-centric conformance + CrossEdgeIM**

这个时候我们做那个两组织 message toy world。

### 再之后开 MHP

不直接读全文。

先亲手算一个两线程程序：

```text
fork
lock
unlock
join
```

学会：

> program order / HB / conflict / segment。

再对照 STCFG。

### Deadlock 要和 MHP/2024 unfolding 成组读

不单独学。

最终产出不是三篇摘要，而是一张：

```text
Property
↓
需要什么信息？
↓
选择什么 representation？
↓
representation 太粗时出现哪种 false result？
```

---

# 十二、我们自己的“小实验候选”现在也可以重新排序了

目前我会给三个候选，但**都先 PARK，不声明创新**。

**PARK-A：Minimal interaction summary under distributed process discovery** -- 我现在最看好。问：组织内模型相同、跨组织 interaction 不同时，CrossEdgeIM 类轻量表示什么时候无法区分？要增加多少 message/resource/object relation 才足够？代价是多少？

**PARK-B：Downstream-aware sampling adequacy** -- 继续我们原来的 EdgeIM pilot，但升级成严格比较 `DFR support / frequency / distribution / process-model quality`。Sampling with Guarantees、sigRank、AllBehavior 已经让 naive novelty 空间很窄，所以必须找到新的 downstream/property dimension 才可能继续。

**PARK-C：Property-conditioned representation adequacy** -- 用 MHP / deadlock 做小世界：同一个 coarse representation 对 MHP 够不够？对 deadlock 又够不够？这是非常好的研究训练题，但目前离一个“鲁组进组小创新”还稍远。

我现在会把 **A > B > C**。

因为 A 同时接：

> EdgeIM → CrossEdgeIM → 鲁侧早期 cross-org Petri → object-centric conformance，

而且存在一个非常真实的设计 tension：

> **丰富语义 vs distributed cost。**

这个比我们昨天那种“Multi-Agent 加个 causal relation 会不会新”要扎实得多。

---

还有一个我这轮**故意没有继续长**的区域：TraceCompiler、Causal Past Logic、Agentproof、TriCEGAR 等 Agent/MAS 最新工作。它们仍放在外圈 `TRANSFER / FRONTIER WATCH`，不进入这周主学习队列。因为我们目前已经从鲁侧本身挖出了足够深的 `representation → property → sufficiency → cost` 主线，再继续往 Agent 扩只会让菌丝又失控。

所以我觉得这轮“长一点点”的量正好：\*\*没有把论文清单翻倍，但我们已经从“EdgeIM 周围几篇论文”升级成了三个 method families，并且第一次挖出了一个真正有鲁侧谱系依据的候选张力：`interaction semantics × distributed efficiency`。\*\*这条值得我们接下来边学 EdgeIM，边慢慢给它喂反例。

**来源:**

- [Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.8077?utm_source=chatgpt.com)
- [Springer](https://link.springer.com/chapter/10.1007/978-3-031-82225-4_4)
- [Run UNL](https://run.unl.pt/server/api/core/bitstreams/4d685e7f-5077-4a1d-8b35-8eb41f27fda2/content?utm_source=chatgpt.com)
- [arXiv](https://arxiv.org/abs/2405.03426?utm_source=chatgpt.com)
- [哈德斯菲尔德大学研究门户](https://pure.hud.ac.uk/en/publications/towards-distributed-process-discovery-inhealthcare-testing-andpro/?utm_source=chatgpt.com)
- [ResearchGate](https://www.researchgate.net/publication/379546660_Petri_Net_Unfolding-based_Detection_and_Replay_of_Program_Deadlocks?utm_source=chatgpt.com)
- [新泽西工学院数字库](https://digitalcommons.njit.edu/fac_pubs/170/?utm_source=chatgpt.com)
- [IEEE JAS](https://www.ieee-jas.com/en/article/doi/10.1109/JAS.2026.125837?utm_source=chatgpt.com)


#### You:
<time datetime="2026-09-08T01:17:47.066Z" title="2026/9/8 上午9:17:47">09:17</time>

这个，参考一下，我们根据项目里另一个窗口的学习进度再进一步细化一下？只细化进组相关的任务和规划．

#### ChatGPT:
<time datetime="2026-09-08T01:17:53.873Z" title="2026/9/8 上午9:17:53">09:17</time>

<details>
<summary>Thought for 606 seconds</summary>

- 统计并检索项目文档状态
- 梳理Agent Formality Scan与进组任务进度
- 读取学习与科研体系文档
- 查看项目文档指定章节
- 正在搜索 14 个网站
- 查看项目源文件指定片段
- 正在搜索 https://www.padsweb.rwth-aachen.de/wvdaalst/publications/p825.pdf
- 正在搜索 10 个网站
- 正在搜索 2 个网站
- 应用代码补丁
- 检查 Markdown 文档结构与占位符
- 创建鲁组进组准备执行细化文档
- 应用文档库文件扩展属性

统计并检索项目文档状态

梳理Agent Formality Scan与进组任务进度

重新阅读选定的导出部分

**Rereading selected export sections**

读取学习科研体系并检索项目文档模式

查看项目与学习科研体系文档指定内容

已搜索 14 个网站

查看了项目源文件指定片段

整理了独立进组执行细化稿

**我正整理独立的进组执行细化稿。**

已搜索 10 个网站

定义语义层级

**Defining semantic tiers**

明确研究目标并整理阶段任务矩阵草案

**整理阶段任务矩阵草案**

**Defining precise research goals**

已搜索 2 个网站

检查了文档长度和格式

**我正在检查文档格式**

**Checking document length**

应用了代码补丁

检查 Markdown 文档结构与占位符

制定鲁组进组准备执行细则

应用文档库文件扩展属性

</details>

我先用 personal-context 技能核对另一个窗口的最新学习位置，再对照这三份文件，把进组部分细化成下一步任务、完成标准和分支开启条件。
《整合版(1)》正文已经是 v1.1，我会以它为当前基线。能确认的是：EX00 已完成，EX01 已有 DFG 手算；最近可见的学习问题落在 Stage 3、递归和 cut 判定。跨窗口检索没拿到此后的作答，所以这部分先保留为接续点，已有进展可直接跳过。

这次会把深研里的候选方向转换成明确的开启条件，同时把交流材料嵌进学习过程，避免准备一直停在读论文。
找到一个能直接推进下一课的原文入口：经典 IM 论文的 §6.2 给了四类 cut 的正式定义，§6.3 给了日志切分与递归例子，可以接着你上传的那篇学。

还需要补一个会影响实验判断的区别：经典 IM 切分日志，DFG 路线切分图。先核清 EdgeIM 对应的接口和权重使用方式，才能判断频次变化是否会影响最终模型。我也会用 Library 技能保存这份进组执行细化稿，方便两个窗口接续。
执行稿已写好：下一步从最近未完成的 cut／递归实例继续，再接 Petri 网执行语义、EdgeIM 接口核对和有限实现；交流说明随每一步补充。

候选方向也写了具体开启条件。跨组织交互仍然保留，但它是否值得先做，要看当前下游问题、已有方法和实际反馈。现在我检查一下任务依赖、完成状态和文件格式。

已经细化好了，单独整理成进组执行稿：

[](sandbox:/workspace/scratch/29f7bd6a83c0/)

**这次重点是把当前学习推进成可检查的个人工作，并同步准备与老师交流。** 每项任务都写了具体动作、产物、完成标准和后续条件。

目前能确认：EX00 已完成，EX01 已有 DFG 手算；最近可见问题落在 Stage 3、递归和 cut 判定。没有取得另一个窗口此后的实际作答，因此暂以这里接续；已经做完的部分直接跳过。

接下来这样走：

| 顺序             | 具体任务                                    | 留下的成果                   |
| -------------- | --------------------------------------- | ----------------------- |
| ① 接当前卡点        | 跟完一个嵌套例子的 cut、切分、递归和返回                  | 一张“本层输入-判定依据-子问题-返回结果”表 |
| ② 接执行语义        | 将同一例子的 process tree 接到 Petri 网，手推 token | 能解释一次有效执行和一次无法完成的执行     |
| ③ 核对 EdgeIM 接口 | 查清具体变体、权重用途、切分对象，再接回全文                  | 一份已知／未知接口表，加两分钟整体说明     |
| ④ 形成有限实践       | 优先复用已有练习，核对手算与代码；按真实疑问选一次比较             | 一项自己能解释、修改、重做的局部工作      |
| 同步推进           | 整理研究兴趣、本人工作和希望请教的问题                     | 一份简短交流说明，逐步补实           |

\*\*本轮有个直接影响下一课的新核查：\*\*经典 IM 原论文 §6.2 确实给出了四类 cut 的正式定义，§6.3 有切分与递归例子，可以直接接着读。[经典 IM 原文](https://dfahland.win.tue.nl/publications/LeemansFA_2013_blockstructured.pdf)

同时，经典 IM 的日志递归与 IMd 的图递归需要区分。这会影响我们怎样补全 EdgeIM 的接口，以及怎样判断“频次变了，最终模型会不会变”。所以先核对具体信息依赖，再安排实验。[IMd 原文](https://leemans.ch/publications/papers/bpmds2015leemans.pdf)

深研里的旁枝也保留了具体入口：对象中心分支在能执行小网、明确要检查什么偏差后开启；MHP 在并发问题或老师任务需要时开启；跨组织交互摘要继续作为候选。**候选方向的吸引力，与下一次最值得做的动作，分别判断。**

下一次学习就接最近未完成的那一次切分／递归；交流说明从这一步开始积累，不必等全部旁枝读完。


#### You:
<time datetime="2026-09-08T01:35:50.817Z" title="2026/9/8 上午9:35:50">09:35</time>

？你搜搜历史，我说过我们要做自己的东西的，除了论文本体的理解深挖，还有横向的另一个自己的东西啊

#### ChatGPT:
<time datetime="2026-09-08T01:36:25.372Z" title="2026/9/8 上午9:36:25">09:36</time>

<details>
<summary>Thought for 456 seconds</summary>

- 检索项目资料中的研究线索
- 检索并梳理两条并行研究线索
- 读取合并项目源文件内容
- 检索个人科研与创新内容
- 检索EdgeIM进组计划相关文档
- 查看项目文档指定片段
- 读取并分析库文件内容
- 读取执行细化文档指定段落
- 应用代码补丁
- 检查进组准备文档关键内容

检索项目资料中的研究线索

梳理了两条并行研究线索

检查项目规划对话

**Inspect project-planning turns**

读取项目文件并检索横向双线及科研创新内容

检索了EdgeIM进组计划相关文档

查看了项目文档指定片段

准备定向改写交付物相关章节

**我正准备定向改写交付物的相关章节。**

读取并分析了库文件内容

准备针对性修订

**Preparing targeted revisions**

更新了版本文件

**Updating the version file**

读取文档段落并应用代码补丁

检查了进组准备文档关键内容

</details>

我先用 personal-context 技能查回“做自己的东西”当时的约定，再核对这三份文件，确认横向那条线原本要做什么、推进到哪。刚才的细化稿把它压成了“论文练习＋候选方向”，这很可能漏掉了已经定下的任务。
查到了：历史检索返回了你说过的“我们自己做一个创新之类的而且得新”，以及“我们现在重心放鲁老师这边”；v1.0 也明确保留了这个目标。\*\*要做自己的研究已经定了，具体选题尚未定。\*\*我刚才把后者误写成了前者也可以一直暂存。

我正在回读更早的两份改计划记录，也会用 Library 技能修正刚才那份执行稿，把第二条线的任务和产物补回来。
更早的原文也找到了。我当时已经写过：“全文吃透只是底座，不能是终点”，以及“每一圈阅读都必须回流成自己的技术动作”。

执行稿已据此改回两条线：论文线继续 cut／递归；自主研究线同步做问题形成、前人核查、最小验证和自己的技术产物。具体实验只依赖它需要的局部知识，不能再被“先学完整篇”整体推迟。


#### You:
<time datetime="2026-09-08T06:11:02.047Z" title="2026/9/8 下午2:11:02">14:11</time>

继续

#### ChatGPT:
<time datetime="2026-09-08T06:11:10.845Z" title="2026/9/8 下午2:11:10">14:11</time>

<details>
<summary>Thought for 56 seconds</summary>

- 查找项目文档与说明文件
- 搜索鲁组进组准备执行细化文档
- 搜索项目文档中的关键词
- 恢复论文深入与自主研究双线 plan
- 应用文件版本元数据

查找了项目文档与说明文件

搜索并细化鲁组进组准备执行文档

搜索并查看入组准备执行细化文档内容

恢复论文深入与自主研究双线计划

应用文件版本元数据

</details>

我接着把这次修正落实完：核对执行稿是否已经保存，并把“论文理解”和“自己的研究”两条线各自下一步要做的事写清楚。修订稿已经恢复了两条独立队列。关键区别也写进去了：**论文练习、复现和比较表可以支持自己的研究，但不能自动算作已经做出了自己的东西。** 第二条线要留下我们自己的问题、设计和验证证据；它现在就推进，所需前置按具体实验补。

对，之前是我把你的目标缩小了。**“要做自己的研究”已经确定；尚未确定的是具体选题，不能因此把整条线推迟。**

修订已保存，正文更新为 v1.1：[](sandbox:/workspace/scratch/29f7bd6a83c0/)。

现在按两条线同步推进：

|       | 论文理解与深挖                    | 横向发展自己的研究             |
| ----- | -------------------------- | --------------------- |
| 目标    | 能重建、解释、实现和审查 EdgeIM        | 提出自己的问题，做出有实质新意的技术成果  |
| 当前入口  | 接另一窗口最近未完成的 cut／递归；已完成部分跳过 | 从已有横向材料形成一个可验证的问题     |
| 下一份产物 | 递归记录、执行解释与接口核对表            | 问题卡、最近方法对照、最小区分实例     |
| 后续产物  | 可解释、可修改的局部实现与全文说明          | 自己的方法或构造、对照验证、贡献与边界说明 |

**第二条线不能用“多读几篇＋做个比较表”交差。** 比较之后必须继续回答：我们发现了什么具体问题？准备改变哪个设计？什么证据能说明这个改变有用？已有工作是否已经解决？

研究线下一步先沿已有投入，核查“跨组织交互信息与分布式代价”这个候选的三个问题：

1. 目标方法实际保留了什么信息？
2. 我们希望支持哪一个具体判断，为什么需要它？
3. 现有的简单办法在哪个明确约束下不够用？

这只是先查哪个候选，尚未定题。核查成立就构造最小实例，再做自己的方案；不成立就据证据调整。**它不等待整篇 EdgeIM 学完。**

后续两个窗口的接续记录也会同时保留“论文线下一步”和“自主研究线下一步”，避免又只剩上课进度。


#### You:
<time datetime="2026-09-08T06:19:03.355Z" title="2026/9/8 下午2:19:03">14:19</time>

？你搜一下之前的呢？第二条线确实还没定，但是应该有大概的方向和相关文献（没有直接说是哪些，但往这边走了几步了的），然后我们讨论一下第二条线？？对了，EdgeIM是不是不是鲁老师主线来着？我们要不要往我们喜欢的之后要用的主线那边走走？我们当时聊了不过直接进入交叉方向了。但感觉现在初步阶段还是从他这边出发会好一点？

#### ChatGPT:
<time datetime="2026-09-08T06:19:05.264Z" title="2026/9/8 下午2:19:05">14:19</time>

<details>
<summary>Thought for 118 seconds</summary>

- 检索自主研究第二方向与进组规划
- 检索关键流程与因果属性
- 正在搜索 25 个网站
- 检索项目技术关键词引用
- 正在搜索 4 个网站
- 查看项目源码指定片段
- 正在搜索 arxiv.org
- 正在搜索 16 个网站
- 查看项目源文件指定片段
- 正在搜索 10 个网站
- 正在搜索 13 个网站

检索自主研究方向与进组规划

检索关键流程与因果属性

已搜索 25 个网站

检索项目技术关键词引用

已搜索 16 个网站

查看项目源文件指定内容及代码段

已搜索 4 个网站

查看了项目源码指定片段

已搜索 16 个网站

检查了主要论文

**Checking primary papers**

查看了项目源文件指定片段

已搜索 13 个网站

</details>

我会用 personal-context 查回当时已经往前走的方向和文献，再核对鲁老师的公开研究谱系。这次先讨论第二条线该从哪里长出来，尤其分清 EdgeIM 的学习入口、鲁老师持续做的问题，以及你以后想用的形式化与 AI 安全方向。找到了，旧讨论比我刚才恢复的更具体：第 16 轮已经走到“行为结构抽取 → 一致性检查／形式保障”，也比较过对象与交互表示、MHP、死锁等入口。

还有一个关键背景：当时把 MHP 降为训练副线，是在比较“哪条路线最快接到 Agent”时作的助手判断。现在你问的是“先从鲁老师已有工作出发，积累以后要用的能力”，这个排名不能直接照搬。我继续核对程序分析这条线的具体论文，看看哪个入口最贴合。

\*\*搜到了。第二条线确实已经有方向和文献积累，我刚才把它恢复得太浅，又被最新的 CrossEdgeIM 候选带偏了。\*\*这次我回读了《只拆论文》里鲁侧谱系、鲁×孙交集及后续取舍的原文，也重新查了相关公开来源。

我的判断是：**EdgeIM 继续作为已经在推进的学习锚点；自己的研究可以开始向鲁侧的“行为建模-性质分析-验证”靠近。具体入口值得优先讨论并发程序分析／死锁检测，同时保留对象与交互一致性这条已有积累。**

先把为什么这样判断讲清楚。

**之前到底走到了哪里？**

在[《只拆论文》原始记录](sandbox:/workspace/scratch/29f7bd6a83c0/project_sources/01-md)第 16 轮，我们已经讨论了：

> 从运行行为中恢复足以支持安全分析的显式结构，再用于一致性检查、形式验证与运行时保障。

这不是现在新起的方向。当时实际上已经形成了三层：

| 层次      | 已经讨论过的内容                                      | 当时的状态         |
| ------- | --------------------------------------------- | ------------- |
| 长期问题方向  | behavior → model → assurance，即行为怎样转成可信分析可用的模型 | 已有明确倾向，尚非具体课题 |
| 更具体的问题族 | 对象身份、消息／制品依赖、因果关系；这些信息怎样影响违规判断                | 已讨论表示差异和小例子   |
| 技术底座    | 并发、程序分析、Petri 网、形式验证、自动推理                     | 后续讨论明确强调其长期价值 |

对应文献也已经出现：鲁侧的 **MHP、死锁检测与 replay、对象中心违规检查**，外侧的 **Object-Centric Conformance Alignments with Synchronization、TraceCompiler、Causal Past Logic、Agentproof**。

这里必须区分：这些方向排序大多是当时的**助手建议**，不能全部算成你已定的路线；但也绝不能把已有探索抹成“只有三个空候选，重新挑一个”。

尤其是：当时把 MHP 降为副线，理由是它**直接迁移到 Agent 的距离较长**；后面的讨论又把并发／程序分析提升为硬技术底座。\*\*“不适合第一个 Agent 桥接课题”，并不推出“不适合第一个鲁侧自主研究”。\*\*我之前漏掉了这个判断条件。

**至于 EdgeIM 是不是鲁老师的主线，要稍微修正一下说法。**

EdgeIM 确实有鲁法明署名，属于边缘过程发现工作；它研究的是这一设置下的发现效率与模型表现。[EdgeIM 论文记录](https://run.unl.pt/entities/publication/91b982e7-dc5e-4ead-99d8-8ffa5236e043)

但“过程挖掘不是他的主线”也不准确。学院页面列出的博士论文、奖项和早期代表成果，长期包含**业务流程建模、验证与挖掘**；同时，Petri 网展开、死锁、数据竞争和 UAF 也有连续成果。因此，更稳妥的结论是：

> **过程挖掘是他长期研究的重要组成部分；EdgeIM 的边缘部署／采样优化只是其中一个具体分支，不能代表他的全部研究重心。**

公开成果能支持这一点，但不能确定他现在主要投入哪个内部项目、会给你什么任务。[学院官方页面](https://cise.sdust.edu.cn/home/page/details/catId/85/id/209.html)

所以我们选择入口，应该看**鲁侧已有积累与你想获得的能力在哪里重合**，不必争出一个唯一“主线”。

**从这个角度，我现在更想让我们认真看一眼“程序运行行为 → 并发模型 → 错误预测与验证”。**

这条路其实就在鲁侧内部，甚至有一个被我们忽略的直接入口：

**2021 年《基于程序运行轨迹 Petri 网模型挖掘的死锁检测方法》**，已经列在他的官方代表成果中。单看已核实的研究题目，就能发现它把“从运行轨迹建模”和“用模型判断程序问题”放在了一起。它的具体算法保证还需要读原文，不能凭题目补全。[官方成果目录](https://cise.sdust.edu.cn/home/page/details/catId/85/id/209.html)

围绕它，已有一组值得按问题联系起来的文献：

| 工作                                                                           | 我们重点追什么                         |
| ---------------------------------------------------------------------------- | ------------------------------- |
| **2021：基于锁增广分段图的多线程程序死锁检测**                                                  | 锁图／分段图漏了哪些信息，为什么会产生误报？          |
| **2024：Petri Net Unfolding-Based Detection and Replay of Program Deadlocks** | Petri 网展开怎样用于死锁检测，候选错误怎样通过重演检查？ |
| **2025：Segment-Based May-Happen-in-Parallel Analysis for C Programs**        | 怎样利用线程、锁和控制流信息，判断两条语句是否可能并发？    |
| **2026：Deadlock Detection and Replay…Refined Segmentation and Lock Graphs**  | 更细的分段与锁操作信息怎样改变检测结果，怎样生成重演调度？   |

来源分别是[《软件学报》原文页](https://ebook.xml-journal.net/rjxb/2021/06/files/basic-html/page109.html)、[IEEE 论文记录](https://ieeexplore.ieee.org/document/10489962)、[MHP 出版商页面](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70203)、[2026 死锁论文](https://www.sciopen.com/article/10.26599/TST.2025.9010085)。

这组文献是**相互关联的方法线索**，不能只按年份排列，就认定作者依次放弃上一种方法、转向下一种。

它对我们有吸引力，是因为能把你喜欢的问题落得很实：

- 模型为什么这样表示？
- 哪个依赖被忽略后，分析会误判？
- 检测出的错误是否真的可能发生？
- 怎样构造一次可执行的证据，而不仅是画出一个看起来有问题的图？

其中一个尤其值得补进知识图谱的节点是：**检查已经发生的执行，与预测其他可能执行中的错误，是不同任务。**

例如，一次运行没有死锁，不代表换一种合法调度也没有死锁。我们必须知道模型允许推断哪些未观察到的执行，以及凭什么允许。这比笼统的“日志 → 模型 → 验证”更深入了一层。

**但这不意味着之前的对象／交互方向应该丢掉。我们真正需要比较的是两个入口。**

|          | 并发程序分析／死锁               | 对象与交互一致性                |
| -------- | ----------------------- | ----------------------- |
| 核心问题     | 看起来可能发生的并发错误，实际是否可发生？   | 执行次序看起来正确时，对象或依赖是否仍然配错？ |
| 鲁侧依据     | 多年连续的程序分析与验证成果          | 已有对象中心违规检查专利等成果         |
| 对长期目标的帮助 | 并发语义、抽象、可达性、误报、反例与重演    | 对象身份、依赖关系、规范、一致性与偏差定位   |
| 当前主要负担   | 程序执行、线程／锁语义，后续可能涉及分析工具链 | 多对象模型与一致性语义，不能停在日志字段设计  |

鲁侧的对象中心专利确实包含鲁老师，并围绕对象中心日志、多对象 Petri 网和托肯重演展开；但单项专利不足以证明它是一个与程序分析同样成熟的持续研究分支。[专利原文](https://patents.google.com/patent/CN119477231B/zh)

另一方面，对象方向也完全可以深入到形式化：之前出现的 **Object-Centric Conformance Alignments with Synchronization** 已经结合对象身份、同步和 SMT 编码做一致性检查。因此，“对象中心只是应用，程序分析才有硬技术”同样不成立。[作者论文](https://arxiv.org/abs/2312.08537)

**我的当前建议，是先把“死锁检测／重演”作为第二条线优先短探的具体问题，MHP 作为相邻分析方法；对象／交互一致性作为真正的竞争入口。**

这里的“优先”有三个依据：

1. 鲁侧的连续研究证据更充分。
2. 能直接练到你以后想用的形式化与程序分析能力。
3. 与现有“运行行为 → 模型”的理解有连接，不需要立刻引入 Agent 框架、提示词或大模型行为的不确定性。

这仍是**入口建议，不是已经找到创新点**。例如“补充锁与 fork 的依赖以减少误报”，2025 MHP 和 2026 死锁工作已经明确处理过，不能再拿来当我们的新意。[MHP](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70203)、[死锁检测与重演](https://www.sciopen.com/article/10.26599/TST.2025.9010085)

下一步值得实际做的是：各拿一个原文中的失败实例，看看我们能否解释**旧方法为什么误判、新方法凭什么修正、还剩下什么限制**。自主研究从这个剩余问题继续形成，而不是学完三四篇之后再临时想创新。

EdgeIM 那边继续接当前 cut／递归进度。第二条线则开始判断上述入口；**不再默认沿着 EdgeIM 的采样与分布式效率往下长，也不要求新研究必须改 EdgeIM。**

至于以后接 AI：旧文献仍然有用。TraceCompiler 对应行为依赖恢复，Causal Past Logic 对应分布式因果可见性，Agentproof 对应工作流结构与策略验证；它们帮助我们观察技术将来怎样使用，现在无需把它们全部变成实现依赖。[TraceCompiler](https://arxiv.org/abs/2608.02680)、[Causal Past Logic](https://arxiv.org/abs/2605.20923)、[Agentproof](https://arxiv.org/abs/2603.20356)

我想和你先讨论一个更具体的兴趣差别：\*\*“这个并发错误到底能不能真实发生”，和“这次执行顺序都对，却操作了错误的对象／依赖”，哪个更让你想追着机制往下拆？\*\*这会帮助我们在两个有依据的入口之间作选择。


#### You:
<time datetime="2026-09-08T06:34:31.456Z" title="2026/9/8 下午2:34:31">14:34</time>

都落盘一下，我去试试？

#### ChatGPT:
<time datetime="2026-09-08T06:34:34.021Z" title="2026/9/8 下午2:34:34">14:34</time>

<details>
<summary>Thought for 273 seconds</summary>

- 查看执行细化文档开头内容
- 应用代码补丁
- 更新鲁组准备文档版本内容
- 上传并更新研究文档

编写了两个文件

**Writing two files**

查看文档并应用代码补丁

更新鲁组准备文档版本内容

上传并更新研究文档

</details>

我把这轮历史恢复、方向判断、文献入口和两个试探任务一起保存，再更新进组执行稿的接续位置。你换个窗口就能直接试，两个方向都保留，试过后再定。两个试探入口都写进去了：一个从“两线程拿锁，是否真能死锁”开始；另一个从“批准过方案，但执行了另一个版本”开始。都标明了是教学构造，并附上回到原文、继续寻找自己研究问题的下一步。现在保存两份文件。新文件可以直接带到另一个窗口开试；执行稿也同步更新，避免接续时又回到旧的候选排序。

都保存好了，你可以直接去试。

- [第二条研究线-方向恢复与双入口试探-2026-09-08.md](sandbox:/workspace/scratch/29f7bd6a83c0/第二条研究线-方向恢复与双入口试探-2026-09-08.md)：包含历史方向、文献链接、判断依据、两个试探例子和换窗口接续说明。
- [鲁组进组准备-执行细化-v1.0-2026-09-08.md](sandbox:/workspace/scratch/29f7bd6a83c0/鲁组进组准备-执行细化-v1.0-2026-09-08.md)：正文已更新至 **v1.2**，同步修正第二条线入口。

**先打开第一份，从 §5 死锁例子或 §6 对象例子任选一个。** 不用先读完文献，带着卡住的那一步回来就行；试过再判断往哪边深入。


#### You:
<time datetime="2026-09-08T06:48:19.889Z" title="2026/9/8 下午2:48:19">14:48</time>

如果让你重新审视一下我们的计划我目前的这些操作与规划，你觉得应该怎么改？就是如果跳出当前架构，让你基于目的重新设计当前的设计，你会采取什么不一样的做法吗？我们先做鲁老师孙老师的调研然后梳理，然后看交叉点，然后找工业界的所有的相关信息这样？然后现在是先争取进入鲁老师组，目前重点先放在鲁老师的领域与方向去好好学。🤔

#### ChatGPT:
<time datetime="2026-09-08T06:48:46.572Z" title="2026/9/8 下午2:48:46">14:48</time>

<details>
<summary>Thinking</summary>

查找官方来源并核对行业案例

**Checking industry examples**

**Locating official sources**

</details>

我会按“当前怎样获得真实研究参与、同时积累长期能力”重新审视这套安排，重点检查：哪些调研已经够用，哪些未知需要通过动手或导师反馈解决，以及我们有没有把论文理解、独立研究和进组条件混在一起。再用少量工业界的一手材料校准能力目标。目前最明显的缺口是：文献和方向地图已有不少依据，但老师实际能提供什么任务、谁会指导、你做这些任务的真实难点，还没有同样具体的证据。另外，工业界材料提醒我们，“用形式化方法做 Agent 安全”只是可能路径之一；需要积累的是建模、实现、验证和处理真实失败的能力，不能只靠研究标签的交集来选题。

\*\*会改，而且我会改“这些工作怎样推动决策”，而不只是换论文、调顺序。\*\*你说的“近期先争取进入鲁组，重点在鲁侧好好学”成立；但我不会把整个过程排成“调研两位老师 → 找交叉点 → 查完工业界 → 确定方向 → 开始准备”的长链条。

已有调研已经帮我们排除了不少随意选方向的可能。现在更需要让**实际学习、自己的研究和真实反馈，开始反过来修正地图**。

**先重新确定：我们究竟在争取什么。**

我会把当前目标写成：

> **获得一段有具体问题、有指导与反馈的研究参与机会，同时形成自己能承担的技术能力，并推进一项属于自己的研究。**

这里有三件事，不能相互替代：

- **进入鲁组**：需要知道参与方式、真实任务、谁指导、怎样反馈。
- **自己长本事、做出东西**：需要实际理解、构造、实现和验证，保留自主研究目标。
- **通向长期兴趣**：逐渐积累形式化、程序分析、可信系统等能力，并观察它们怎样用于 AI。

组的名字、读过的论文数量、与热门方向的交集，都是帮助判断的线索。最终要看这些安排能否产生上述结果。

我刚才又查了已有记录，仍没有取得鲁老师已明确给出的任务、交流日期或指导安排。**这表示我们的计划还缺这一类信息，不表示你实际上一定没联系过。**

**我会首先改变三类调研的职责。**

| 调研对象         | 现在主要回答什么                           | 什么时候已经够用             |
| ------------ | ---------------------------------- | -------------------- |
| 鲁老师及相关合作研究   | 有哪些持续问题？哪些有可读原文、材料、可尝试的入口？实际能怎样参与？ | 能带着具体工作与问题寻求反馈       |
| 孙老师及相关研究     | 长期目标需要哪些形式化能力？有哪些未来可接的问题？          | 能校准能力方向，不必立即满足两边课题交集 |
| 工业界          | 这些能力用于什么真实任务？结果怎样验收？什么条件下方法会失败？    | 能改变当前产物或能力训练的要求      |
| **你自己的实际尝试** | 哪些内容能掌握？哪里依赖提示？做什么时能持续产生问题？        | 能决定下一段投入，而非只凭抽象兴趣排名  |

\*\*鲁×孙交集可以提供好问题，但不应成为每个起步项目必须满足的条件。\*\*一个扎实的鲁侧并发分析问题，即使暂时没有 Agent，也可能积累很有用的能力；反过来，一个题目同时包含 Petri、Agent、Safety，也可能没有清楚的问题和可验证的贡献。

同样，“工业界所有相关信息”没有明确完成点。我会保留宽视野，但按需要深入：正在研究误报，就查误报代价和实际处理流程；正在研究重演，就查如何把失败变成稳定测试；正在考虑部署，再查性能和集成约束。

这不是缩小认知范围，而是让广泛观察与当前执行保持不同节奏。

**第二个改变：把“真实反馈”前移。**

目前计划里论文理解、反例和文献比较已经相当细，**具体参与条件却仍很模糊**。这是我认为最需要修正的不对称。

我会尽早用已有材料形成一次可以得到反馈的交流：

> 我已经围绕 EdgeIM 做了哪些手算，目前理解到哪里；最近在尝试并发分析／对象一致性中的哪一个具体问题；希望了解组内有没有适合继续做的入口，以及需要补什么。

这次交流的作用，是补齐我们无法从论文推断的信息：近期课题、指导资源、适合的任务范围、预期交付。

\*\*自主研究继续推进，也可以带着尚未完成的问题接受指导。\*\*我们追求自己的成果，不需要先独自在组外解决完所有选题困难，才允许获得研究反馈。

而且“有机会加入”和“这个机会能提供有效训练”也要分别看。能否得到技术反馈、承担什么工作，会直接影响这段经历的价值。

**第三个改变：保留双线，但让它们共享能力与产物。**

我不会撤回刚刚恢复的第二条线。它是你明确要做的事情。

不过，两条线可以这样连接：

- EdgeIM 深入产生对日志、关系、图、递归、模型语义与评价的理解。
- 自主研究使用其中适用的部分，并暴露需要补的新知识。
- 研究遇到的问题，再帮助我们理解论文的假设和边界。

它们各有目标，但不必维护两套完全分离的学习体系。比如 Petri 网执行语义，可以同时支持论文理解和死锁／一致性研究；不用每换一个入口再从零讲一遍。

同时，\*\*自主研究不需要先选一个研究标签。\*\*它可以从“这个模型为什么报告了一个实际上做不到的错误”这种明确问题开始，逐渐形成自己的设计和证据。

这里我也会修正上一条回复的最后那个问题：问你“两个例子更喜欢哪个”，只能获得初步兴趣信息。一个例子讲得更生动、刚好更容易，也会影响你的感受。实际选择还要看：

> 原文与材料是否可得、必要前置是否可承受、问题是否值得做、现有办法是否已经解决、能否得到反馈。

所以我目前仍支持先试死锁／重演，也保留对象／交互一致性；**这个短探顺序不需要在真正试过之前再次重排。**

**第四个改变：增加一条稳定的基础积累，减少“每篇论文现场补洞”。**

你要求从零基础教，是合理的；但如果所有基础都只在论文卡住时临时解释，也容易出现“这个例子听懂了，换个地方又认不出来”。

我会把反复使用的少量基础持续串起来，例如：

- 集合、关系、图、状态与不变量；
- 递归、基本数据结构、把规则写成程序；
- 从输入到输出的调试、测试与实验记录。

它们依然通过当前问题学，但会有独立的复用机会。例如学过“关系”后，在 DFR、线程先后关系、对象关联中分别认一次；学过递归后，自己改一个小输入，预测调用怎样变化。

\*\*不需要因此加一整套计算机本科课程作为进组前置。\*\*课程、考试和数学英语的既有安排也继续保留，研究计划按真实可用时间调整。

AI 的分工同样要据此改变：检索、材料整理、脚手架可以多交给我；关键模型、预测和判断逐步由你承担。我们需要观察的是你能否解释、修改和检验核心部分，而不是要求所有机械工作都手工完成。

**第五个改变：工业界调研要校准“工作能力”，不能只为当前方向寻找支持。**

这次查到的几个一手来源，恰好说明了这一点：

- AWS 的正式经验报告讨论用形式规格与模型检查处理关键分布式系统的设计问题。[AWS 经验报告](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods)
- 微软 Coyote 用系统化测试探索并发执行，同时明确说明它不提供一般正确性证明。[Coyote 官方说明](https://microsoft.github.io/coyote/)
- OpenAI 当前 Agent Safety 岗位强调把模糊安全问题变成威胁模型、可复现实验和实际缓解措施，并衡量漏检、误拦截与延迟。[岗位原文](https://openai.com/careers/researcher-agent-safety-oversight-and-system-mitigations-san-francisco/)

\*\*我的推断是：长期值得积累的是“选对问题、明确保证范围、做出实现、用证据判断效果”的能力。\*\*形式化方法是你很值得深入的一条技术路线，但未来具体任务可能同时需要测试、系统工程、安全分析或统计评价。

这也意味着工业调研要主动找反例：哪些问题用简单测试已经足够？哪些形式化方法因为建模、维护或集成成本而不好用？什么情况下表示更丰富反而没有实际收益？这些证据比继续证明“我们的方向很有前景”更能改善选题。

当前岗位只能说明现在的任务样貌，不能直接预测你以后一定会做什么。

**如果现在就执行这个重设计，我会这样安排下一段，而不重新开一轮全景调研：**

| 当前动作                              | 应该取得的证据                    |
| --------------------------------- | -------------------------- |
| 接着完成 EdgeIM 当前未完成的 cut／递归实例，并接回全文 | 哪些机制已经能由你解释，哪个接口仍不清楚       |
| 尝试已经保存的两个入口，随后给更有潜力的一边接一个原文实例     | 兴趣、实际前置、方法差异，以及一个值得继续追的未知  |
| 用已有工作形成简短交流材料，补齐实际参与条件            | 老师／组内对问题、任务范围和准备程度的具体反馈    |
| 将选中的未知推进成自己的最小验证                  | 我们提出了什么、亲手获得什么证据、下一步为什么值得做 |
| 遇到跨任务反复出现的基础，持续补并复用               | 提示依赖是否减少，能否在新例子中使用         |

因此，已经保存的文件和试探任务仍然有效。\*\*这次最实质的变化，是把计划的推进依据从“地图越来越完整”，转向“能力证据、自己的研究证据和外部反馈越来越具体”。\*\*地图继续长，但每次大改计划要有能改变判断的新证据。

要进一步决定哪些动作应当前移，我现在最需要补的一条事实是：**你和鲁老师本人，或能实际帮你接入组内的人，目前已经沟通到哪一步？**


#### You:
<time datetime="2026-09-08T06:53:56.586Z" title="2026/9/8 下午2:53:56">14:53</time>

对，其实是有说想要调研现在的这些交叉方向的具体情况，有哪些团队在做，横向对比是都在做什么，纵向看单个团队的脉络，工业界都是怎么做的，怎么处理的。是的，感觉基础知识这里需要单独拿出来做一条线比较好，在必备的基础上往外也拓展一点。
你说的这些有一些是我不确定为什么你没有记录的，不过现在揪出来说清了就可以了
目前还没沟通，感觉能力不够，中下旬再去

#### ChatGPT:
<time datetime="2026-09-08T06:54:23.903Z" title="2026/9/8 下午2:54:23">14:54</time>

<details>
<summary>Thinking</summary>

更新研究简报并完善四线执行计划

**我更新四线执行计划**

**Updating the research brief**

</details>

明白，交叉方向调研本身就是一项正式任务：既要比较不同团队，也要追单个团队的研究演变和工业界的实际做法。我会把这一点、独立的基础知识线，以及“尚未沟通，计划九月中下旬联系”写回现有计划，保留已经定下的论文深入和自主研究两条线。已把四项工作的目的分开写清楚：论文深入、自主研究、基础学习、交叉生态调研。基础线也补了从逻辑、关系、图、状态与编程起步的顺序。联系时间按你的九月中下旬意向准备，到时看具体成果和缺口，不要求等所有基础与调研都完成。

嗯，这次把它明确留下了。**你要的交叉调研本身就有认识领域、培养判断力的价值**，之前我把它收缩成“只为当前实验服务”，确实漏掉了你的目标。

现在四条线各有自己的进度：

| 工作线        | 做什么                                   |
| ---------- | ------------------------------------- |
| 论文深入       | 接着学 EdgeIM，保留全文理解、机制、实现与评价            |
| 自主研究       | 从已有方向继续形成自己的问题、设计和验证证据                |
| **独立基础**   | 系统学习必要基础，再向相邻知识适度拓展                   |
| **交叉生态调研** | 横向比较团队与方法，纵向追研究脉络，查工业界如何实现、验证、部署和处理失败 |

基础线会有自己的顺序：先从**逻辑、集合与关系、图、状态与不变量、基本编程与算法**串起来，再逐步接并发、自动机、概率与实验等。这个范围也参考了 [MIT 离散数学课程](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/)；具体速度根据你的实际学习调整。

联系状态也已更新为：\*\*目前尚未沟通，计划九月中下旬联系。\*\*这段时间就积累能展示的具体准备：一份能讲清的论文说明、一项自己能解释和修改的工作、一个带着尝试的问题。到时据这些判断还缺什么，不必等“完全有信心”才联系。

两份文件已同步保存：

- [鲁组进组准备-执行细化-v1.0-2026-09-08.md](sandbox:/workspace/scratch/29f7bd6a83c0/鲁组进组准备-执行细化-v1.0-2026-09-08.md)：正文 **v1.3**，新增基础线与调研任务书。
- [第二条研究线-方向恢复与双入口试探-2026-09-08.md](sandbox:/workspace/scratch/29f7bd6a83c0/第二条研究线-方向恢复与双入口试探-2026-09-08.md)：正文 **v1.1**，保留两个试探入口。

四条线不要求每天平均推进；接续与记录由我维护，你继续实际学习和尝试就好。


#### You:
<time datetime="2026-09-08T09:01:15.328Z" title="2026/9/8 下午5:01:15">17:01</time>

想知道自己的这个基础线这边，目前根据这些论文，应该怎么去规划，之后单独看课补吗？还是对着讲义和实际遇到的问题去逐个击破并拓展相关的脉络？我们提到的科研菌丝网络体系怎么去建设？盘点了一下现在电脑里的情况，你也看看？

#### ChatGPT:
<time datetime="2026-09-08T09:01:24.978Z" title="2026/9/8 下午5:01:24">17:01</time>

<details>
<summary>Thought for 303 seconds</summary>

- 读取学习科研体系构想文档
- 提取并清理科研任务详版内容
- 正在搜索 2 个网站
- 正在搜索 5 个网站
- 读取科研台进度文档前224行
- 正在搜索 3 个网站
- 查找项目中的 Markdown 文件
- 正在搜索 8 个网站

读取科研体系、科研台进度及任务盘点文档并统计结构

提取并清理科研任务详细内容

已搜索 5 个网站

准备DFR/HB概念说明

**Preparing DFR/HB concept notes**

读取科研台进度文档前224行

已搜索 3 个网站

查找项目中的 Markdown 文件

已搜索 8 个网站

</details>

我先读完你新传的三份盘点，核清已有课程、笔记、工具和项目能怎样复用，再把基础线细化到具体单元。我也会把“科研菌丝网络”落到一次学习如何留下概念、证据和下一步，看看现有科研台还缺什么。盘点里已经有地图、七个学习视角、操作符和不少论文材料，缺的是把它们接到你的实际作答、理解变化和后续复用上。基础线也已经被明确保留，接下来需要给它连续的学习单元和独立练习。

所以我倾向于用讲义建立知识顺序，用论文和小问题决定从哪里切入；课程视频在需要完整示范时补上。我正在把这个安排对应到现有资产，避免再添一套重复维护的笔记。
