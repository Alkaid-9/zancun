# Execution -> Structure -> Intervention：从运行痕迹恢复潜在结构

**记录日期**：2026-09-05

**来源类型**：用户研究思考的保真整理

**证据状态**：概念框架已记录；文中论文名称、年份、方法细节和实验数字均来自本次用户输入，尚未逐项回到原论文核验

**用途**：保存跨领域联想的完整推理链，并作为迁移审计协议的首个案例

**不得据此声称**：相关工作清单已穷尽、论文细节已核真、研究空白或 novelty 已成立

## 1. 真正要挖的不是领域标签，而是研究动作

问题不是“有没有一篇叫 Process Mining for LLM Multi-Agent 的论文”，而是：

> 从运行痕迹里抽结构，把结构显式化，再拿结构去压缩、验证、监控或改造系统，这种研究动作能否跨领域复用？它已经在哪些领域被复用？

暂时把母结构写成：

\[
\boxed{\text{Execution} \rightarrow \text{Structure} \rightarrow \text{Intervention}}
\]

更完整的闭环是：

```text
真实运行 / traces / logs
        -> 识别稳定结构、依赖、冗余或因果关系
        -> 显式 representation / model / IR
        -> 验证 representation 是否捕捉到目标结构
        -> 把稳定部分固化、编译、监控或用于控制
        -> 用新的运行反馈继续修正模型
```

它与控制论或系统辨识共享一种一般动作：

\[
\text{observations}
\rightarrow
\text{identify model}
\rightarrow
\text{reason/control with model}
\rightarrow
\text{observe again}
\]

但不同领域中的状态和模型不必是连续变量或微分方程，也可能是 DFG、Petri net、DAG、TLA+ specification、MDP 或 dataflow graph。

## 2. 同一母结构在 Agent 领域的候选实例

以下内容是本次思考中提出的 related-work 候选，不是已经完成的文献审计。

### 2.1 TraceCompiler：从 trace 恢复数据依赖并编译 workflow

候选动作：

\[
\text{trace}
\rightarrow
\text{dependency discovery}
\rightarrow
\text{workflow compilation}
\]

用户输入中的关键判断是：它不只把 adjacency 或 directly-follows 当依赖，而是追问 producer-consumer data dependency，即“谁真正消费了谁产生的值”。

这与 EdgeIM 的：

\[
\text{event log}
\rightarrow
\text{DFG}
\rightarrow
\text{process model}
\]

具有家族相似性，但也暴露了迁移时必须更换 representation：Agent 系统中的关键关系可能不是“经常相邻”，而是 artifact/value 的生产与消费。

### 2.2 Agent Workflow Optimization：把重复工具序列编译为 meta-tool

候选动作：

\[
\text{trace}
\rightarrow
\text{recurring pattern}
\rightarrow
\text{compile into reusable primitive}
\]

用户输入将其描述为分析 agent workflow traces 中反复出现的工具调用序列，并把它们编译成 deterministic meta-tools，以减少中间 LLM reasoning 和 tool calls。输入中记录的候选结果数字是：两个 benchmark 上最多约减少 11.9% LLM calls，成功率最多增加约 4.2 个百分点。数字在原论文核验前不得引用为已确认事实。

它对应一个更一般的工程/研究动作：

> 把 repeated reasoning 编译成 callable capability。

### 2.3 Artic：从隐式自然语言语义到显式 artifact IR

候选动作：

\[
\text{implicit semantics}
\rightarrow
\text{explicit IR}
\rightarrow
\text{local verification}
\]

用户输入中的核心描述是：每一步显式声明读取和写入的 artifact、constraint 以及 control transfer，再通过局部 obligations 和 scenario dry-runs 检查编译结果是否忠于原 workflow。

由此得到的 meta-principle 是：

> Plugin 可以隐藏 mechanics，但 epistemically important semantics 必须显式保存。

### 2.4 Agentproof：抽取统一 workflow graph 并执行静态验证

候选动作：

\[
\text{agent framework}
\rightarrow
\text{extract workflow graph}
\rightarrow
\text{static verification}
\]

用户输入将其描述为从 LangGraph、CrewAI、AutoGen 和 Google ADK 抽取统一 abstract graph，检查 unreachable/dead-end 等结构问题，将 temporal safety policy 编译成 DFA，再通过 graph x DFA product 做静态验证，并可检查 runtime traces。

这里出现一个重要 operator：

\[
\boxed{\text{Make structure explicit} \Rightarrow \text{new analysis becomes possible}}
\]

结构的价值不只在“理解系统”，而在于显式结构使静态分析、模型检查或运行时检查成为可能。

### 2.5 Causal Past Logic：从全局时间顺序细化到因果可见性

用户输入指出，分布式 Agent workflow 不能简单压成一条全局线性日志，因为某个 Agent 做决定时只能知道因果上已经到达它的信息。候选 representation 包括消息关系、局部顺序和 vector clocks，并用 temporal logic guard 在线影响控制流。

它对 DFG 式表示提出了关键修正：

```text
DFG：A 先发生，B 后发生，可能被理解为 A -> B

分布式 Agent：A 在全局时间先发生，
但 B 当时可能根本不知道 A 发生了
```

因此：

\[
\text{temporal order} \neq \text{causal visibility}
\]

迁移不是把老算法原封不动搬过去，而是保留研究动作，重新寻找目标域中 downstream-sufficient representation。

### 2.6 AgentGuard：在线辨识行为模型并检查风险

候选动作：

\[
\boxed{
\text{observe}
\rightarrow
\text{identify behavioral model}
\rightarrow
\text{verify online}
}
\]

用户输入将其描述为：观察 Agent raw I/O，抽取 formal events，在线学习 MDP 行为模型，再用 probabilistic model checking 实时检查风险。

这与控制/系统辨识的相似性更直接：控制中可能识别 dynamics，process mining 中识别 workflow，agent mining 中识别 dependency/protocol，formal assurance 中拿模型检查 property，compiler/system optimization 中拿模型改变 execution。

## 3. Semantic prior-art search：按研究动作搜索

只搜索 `process mining + LLM multi-agent` 会漏掉概念上相关但不自称 process mining 的工作。搜索单位应从领域标签改成“动作 + 对象 + 结果”。

### 3.1 概念族

- `trace -> workflow`：trajectory mining、workflow induction、program synthesis from traces、trace compilation；
- `trace -> dependency`：dataflow inference、def-use mining、causal dependency discovery、interaction mining；
- `workflow -> formal model`：workflow compilation、protocol IR、Petri net extraction、automata extraction；
- `formal model -> assurance`：static verification、runtime verification、model checking、conformance checking；
- `trace -> optimization`：workflow optimization、meta-tool compilation、skill induction、procedure extraction；
- `execution -> diagnosis -> repair`：failure localization、trace attribution、workflow repair、protocol repair。

### 3.2 查询候选

```text
agent trace dependency inference
workflow induction from execution traces
program synthesis from traces
agent trajectory compilation
protocol inference from logs
causal dependency discovery agent workflow
runtime monitor learned from traces
workflow repair from execution feedback
```

核心原则：

> Search by mechanism, not by tribe.

Related work search 不只追踪“和我使用同一领域标签的人”，还要寻找“与我共享同一研究动作的人”。

## 4. 把母结构继续上抽

```text
                         从经验中抽结构
                               |
          +--------------------+--------------------+
          |                    |                    |
     Process Mining        System ID       Program/Trace Mining
          |                    |                    |
     event -> process     obs -> dynamics      trace -> program
          +--------------------+--------------------+
                               |
                       explicit model / IR
                               |
            +------------------+------------------+
            |                  |                  |
         predict             verify            optimize
            |                  |                  |
         control             monitor            compile
```

可复用 operator 的候选名称：

> Recover latent structure from behavior.

触发条件：系统本身复杂、规则未被完全显式写出，但留下了大量 execution traces。

触发后连续追问：

1. traces 中是否存在稳定结构？
2. 哪一种 representation 能保留目标任务需要的信息？
3. 得到结构后，能做什么原先做不了的预测、验证、监控、编译、控制或修复？

## 5. 从联想到研究问题的更新

初始问题可能只是：

> CrossEdgeIM 的感觉能否迁移到 Multi-Agent？

第一轮 prior art 可能告诉我们：旧 MAS 已经有人做 process mining。这并不自动意味着 idea 终止。

进一步抽象后，真正迁移的可能不是 EdgeIM，而是：

> behavior -> structure 这一研究动作。

于是 frontier 问题更新为：

> 到底应该从 Agent trace 中恢复什么结构，以及这个结构应被拿来做什么？

这个问题比“有没有 process mining + agent 的论文”更宽，也更接近研究方向如何实际演化。

## 6. Transfer Judgment：迁移判别力

真正困难的不是产生“这两个东西好像很像”的 sense，而是判断是否存在可迁移的研究结构。

### 6.1 相似性层级

| 层级 | 看到的相似性 | 研究价值 |
|---|---|---|
| L0 词汇相似 | 都叫 graph / agent / feedback | 几乎没有价值 |
| L1 现象相似 | 都有重复、瓶颈、并行 | 可作为灵感 |
| L2 结构相似 | 对象、关系、约束存在对应 | 值得继续剥皮 |
| L3 机制相似 | 源方法有效所依赖的机制也存在于目标域 | 真正可能迁移 |
| L4 干预相似 | 可用相近干预改变目标系统 | 有较高研究价值 |
| L5 可验证迁移 | 可设计低成本实验区分成立与不成立 | 可进入研究队列 |

大多数 sense 会停在 L1/L2。只有经受住 L3-L5 的审计，才值得持续投入。

## 7. 机制剥皮：源方法为什么有效

跨域迁移的中心问题不是“源方法用了什么实现”，而是：

> 源方法到底依赖什么机制才有效？

通用表达：

\[
\text{source phenomenon}
\rightarrow
\boxed{\text{why does it work?}}
\rightarrow
\text{abstract mechanism}
\]

### 7.1 示例

- Mapping Networks：高维参数空间很大 -> 好解可能只占低维有效自由度 -> 压缩搜索自由度。
- IndexShare：每层重新计算 selection -> 相邻层 selection 高度冗余 -> 共享重复计算。
- DSpark：全串行慢、全并行丢依赖 -> 真正必须串行的只是少量依赖 -> dependency-critical 部分串行，昂贵且独立的工作并行。
- Process mining：大量 execution traces 复杂 -> 行为中可能存在重复和稳定结构 -> 恢复潜在行为结构。

应迁移的是中间机制，不是两端的表面实现。

### 7.2 EdgeIM -> Agent 的关键改写

浅层联想是“两边都有 traces，所以都能画 DFG”。更深的问题是：

> EdgeIM 有效是否依赖某种局部事件关系足以表示 downstream 需要的结构？

迁移到 Agent 后，对应 observable relation 可能不是：

\[
A\text{ 后发生 }B
\]

而是：

\[
B\text{ 消费了 }A\text{ 产生的 artifact}
\]

或者：

\[
A\text{ 的 message causally enabled }B
\]

因此：

> 具体方法可能不能搬，但研究 operator 可以搬。

## 8. 目标域检查

抽出机制后，不能只问“像不像”，而要依次审计以下问题。

### 8.1 结构存在吗

目标域中是否真的有稳定 latent structure？如果 Agent 策略每次完全不同、没有稳定组织规律，就没有值得 mining 的结构。

### 8.2 结构可观察吗

真实 dependency 可能存在，但日志可能只记录：

```text
Agent A called tool
Agent B called tool
```

如果没有 message ID、artifact provenance、sender/receiver 或 causal link，则：

\[
\text{存在} \neq \text{可识别}
\]

### 8.3 结构可行动吗

识别出的结构必须改变至少一种决策，例如 verification、orchestration、failure diagnosis、compilation、monitoring 或 resource allocation。否则它可能只是 visualization。

### 8.4 如何证明不是幻觉

必须设计 discriminating test。例如：

- 交换两个 independent actions 的顺序，representation 应认为结构不变；
- 替换 producer artifact 后，consumer 应失效或结构应改变；
- 构造 adjacency 相同但 causal dependency 不同的 workflows，representation 应区分二者。

只有这样，才能从“图看起来合理”升级成“representation 捕捉到了 operational dependency”。

## 9. 迁移价值判断

启发式公式可以写成：

\[
\text{Transfer Value}
\approx
\frac{
\text{mechanism overlap}
\times
\text{observability}
\times
\text{actionability}
\times
\text{testability}
}{
\text{translation cost}
}
\]

各项含义：

- `mechanism overlap`：源方法成功依赖的条件在目标域是否存在；
- `observability`：是否能得到识别该机制所需的信号；
- `actionability`：识别结果能否改变系统决策；
- `testability`：是否存在低成本证伪实验；
- `translation cost`：是否需要先新造 logging、benchmark、formal semantics 或 runtime。

但正式协议不把它当可加权补偿的总分。`observability`、`decision delta` 或 `falsifiability` 缺失时，应触发硬门，而不是让其他高分抵消。

## 10. 假相似与 analogy boundary

“control、RL、human learning、Agent 都有 feedback”只停留在词汇或现象层。

进一步可以比较：

\[
\text{state}
\rightarrow
\text{controller}
\rightarrow
\text{action}
\rightarrow
\text{environment}
\rightarrow
\text{new state}
\]

和：

\[
\text{belief}
\rightarrow
\text{experiment}
\rightarrow
\text{evidence}
\rightarrow
\text{belief update}
\]

共同结构可能是“闭环系统通过外部响应修正内部状态”。但还必须检查 stability、observability、delay、noise 等概念是否在目标域有可操作对应。没有对应时必须明确写：

> Analogy stops here.

敢于写清类比的终点，也是研究素养。

## 11. 真迁移必须产生新预测

如果两个领域共享机制，迁移不能只产生新解释，还应产生原本没有的预测。

### 11.1 DSpark 式预测

源观察：长 dependency chain 的可靠性可能累积衰减。

迁移到 Agent workflow 后的预测：

> verification checkpoint 不应平均插入，而应优先放在高风险 dependency boundary。

### 11.2 Process-mining 式预测

源观察：行为中存在可恢复的稳定结构。

迁移到 Agent 后的预测：

> successful traces 与 failure traces 在 dependency topology 上应存在系统性差异。

如果类比只能生成“这让我想到某领域”，却不能生成“因此在条件 C 下应观察到 Y”，则仍只是 inspiration。

## 12. 从 sense 到研究队列的闭环

```text
1. 闻到相似
2. 去表面化：两边真正共享的结构是什么？
3. 机制剥皮：源方法为什么成立？
4. 目标域检查：机制在那里也存在吗？
5. Representation check：能观察、识别和充分表示吗？
6. Intervention check：知道它以后会改变什么决策？
7. 生成新预测与竞争解释
8. 按机制做 prior-art search
9. 做最小实验或构造反例
10. 决定 DROP / PARK / PROMOTE
```

Prior-art search 不必总在第一步。先独立抽象几分钟，有助于避免被窄关键词锁死；但任何 novelty 判断仍必须在系统检索之后。

## 13. 二次抽象与反向具体化

一次较浅的抽象可能是：

> EdgeIM 是日志压缩。

继续抽象：

> EdgeIM 是 coverage preservation。

再抽象：

> 在保留 downstream-relevant invariant 的前提下删除冗余实例。

这时可以连接 test-suite reduction、coreset、graph sparsification、abstraction 和 sufficient statistics。

但科研上最关键的是反向具体化：

> 迁移到目标域后，那个 invariant 到底是什么？

完整能力因此是：

\[
\boxed{
\text{具体}
\rightarrow
\text{抽象}
\rightarrow
\text{迁移}
\rightarrow
\text{重新具体化}
}
\]

缺少最后一步，就容易滑向“万物皆 coreset、万物皆控制论、万物皆信息压缩”。

## 14. 晋级标准

一个 sense 从 `PARKED` 升为 `PROMISING`，至少应产生以下三项之一：

1. 一个新的 representation；
2. 一个新的可证伪 prediction；
3. 一个新的 intervention。

满足一项：值得继续剥皮。

满足两项：值得做低成本实验。

三项都满足：开始认真审计 novelty、prior art 和 feasibility。

最终训练目标是：

> 大胆地产生 analogies，苛刻地审判 mechanisms，快速杀掉假迁移，把验证资源留给真正能产生新预测的结构同构。

## 15. 本案例当前边界

- `Execution -> Structure -> Intervention` 是待检验的母结构，不是自然定律。
- TraceCompiler、AWO、Artic、Agentproof、Causal Past Logic、AgentGuard 是候选案例；未完成逐篇身份、版本、原文和数字核验。
- EdgeIM 的具体论文算法、当前本地 surrogate 和 Agent dependency inference 不得混称为同一方法。
- 下一步若进入研究执行，应先实例化 Transfer Card，再做 semantic prior-art audit，最后才决定是否设计 toy experiment。

## 16. 关联谱系案例

`2026-09-05_鲁法明研究谱系与稳定Research-Grammar.md` 把本 operator 放回鲁法明本人及曾庆田—刘聪—苏轩—程龙公开合作谱系中，区分本人署名、合作网络、公开证据和推断，并具体展示 `representation -> structure -> downstream reasoning` 如何跨越流程挖掘、并发程序、RCA 与工业 AI。
