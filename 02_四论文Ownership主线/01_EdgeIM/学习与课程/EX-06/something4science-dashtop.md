我们刚才走到的是：**Algorithm 1 可能扭曲频次，而 IMf 会显式读频次，所以这个变化可能传导到下游。**

现在把四个层次彻底分开：

* **现象（phenomenon）**：你实际观察到了什么。
  例：`D` 和 `D′` 的边集合一样，但边频次变了。

* **风险（risk / concern）**：这个现象为什么值得担心。
  例：IMf 会用频次和阈值做过滤，所以频次变化可能影响后续处理。

* **研究问题（research question）**：把担心改写成一个能被系统检查的问题。
  例：
  **在什么条件下，feature-preserving sampling 引入的频次失真会改变 IMf 的过滤结果或最终模型？**

* **假设（hypothesis）**：你在实验前对这个研究问题给出的可证伪预测。
  例：
  **当采样使某条边相对其源节点最强 outgoing edge 的频次比例跨过 IMf 阈值时，D 与 D′ 的过滤结果会发生分岔。**

这里最关键的是：

```text
现象 ≠ 研究问题
风险 ≠ 研究问题
研究问题 ≠ 假设
```

很多刚开始做研究时最容易犯的错就是：

> “我发现频次变了，所以这是个问题。”

这还不够。

因为你还没说明：

> **谁会读取这个变化？**
> **什么条件下它真的产生 downstream consequence？**

而你现在已经开始补上这两层了。

---

再往前一步，我们把它形式化一点。

假设从活动 `a` 出发有两条边：

```text
a -> b
a -> c
```

原始日志 D 中：

```text
w_D(a,b) = 100
w_D(a,c) = 20
```

采样后 D′ 中：

```text
w_D'(a,b) = 10
w_D'(a,c) = 10
```

定义相对频次：

```text
r_D(a,c)
=
w_D(a,c) / max_y w_D(a,y)
```

那么原始 D 里：

```text
r_D(a,c) = 20/100 = 0.2
```

采样后：

```text
r_D'(a,c) = 10/10 = 1
```

如果 IMf threshold：

```text
t = 0.3
```

那么：

```text
D:   0.2 < 0.3  → 可能过滤
D′:  1.0 > 0.3  → 保留
```

看见了吗？

真正重要的不是：

> “weight 变了多少”

而是：

> **变化有没有跨过下游决策边界。**

这个思想非常通用。

以后你看任何论文，看到 representation compression / sampling / abstraction，都可以问：

> 上游 loss 是否跨过了 downstream decision boundary？

这比单纯问“信息有没有损失”强很多。

---

所以我们现在其实已经能把 T0 的核心对象说得很接近了：

> **研究 EdgeIM 的 feature-preserving sampling 是否在保留结构存在性的同时改变频次信息，以及这种频次失真在什么条件下会改变固定下游 IM/IMf 的行为。**

但还没正式拍板。

下一步该做的是 **attack**：

我们要问一个反方向的问题——

> 有没有可能频次被扭曲得非常厉害，但 IMf 最终模型完全不变？

如果答案是“有”，那我们就知道：
**频次失真本身不是充分条件。**

这一步很重要，因为它会逼我们从“相关现象”继续收缩到真正的机制条件。



继续。现在做 **attack：把“频次失真 → 最终模型变化”这条直觉拆掉**。

先看整条因果链：

```text
Algorithm 1
↓
weight / frequency 发生变化
↓
某些边是否跨过 IMf threshold
↓
过滤后的 DFG 是否变化
↓
cut 判定是否变化
↓
递归结构是否变化
↓
最终 process tree / model 是否变化
```

关键点是：**每一个箭头都可能断。**

所以“频次失真很大”本身远远不够。

### 反例 1：频次变得很厉害，但没跨 threshold

原始：

```text
A→B = 100
A→C = 80
```

采样后：

```text
A→B = 10
A→C = 8
```

绝对频次掉了 90%，看起来“失真巨大”。

但相对关系：

```text
80/100 = 0.8
8/10   = 0.8
```

完全没变。

如果 threshold = 0.3：

```text
0.8 > 0.3
```

前后都保留。

于是：

```text
weight 变化 ✅
threshold decision 不变 ✅
filtered DFG 不变
```

所以这里**频次变化根本没有 downstream consequence**。

---

### 反例 2：跨 threshold 了，但最终模型还是不变

假设：

```text
原始：
A→B = 100
A→C = 20

采样后：
A→B = 10
A→C = 10
```

threshold = 0.3。

于是：

```text
原始：20/100 = 0.2 → C 边过滤
采样：10/10 = 1.0 → C 边保留
```

这次 filtered DFG 确实不同了。

但还不能宣布：

> “最终模型一定变了。”

因为新保留下来的 `A→C` 可能**没有改变当前 cut 的判定**。

比如原来整个结构已经因为别的边非常明确地形成某个 sequence cut，那么多一条局部边未必足以推翻那个分组。

于是可能：

```text
threshold decision 变化 ✅
DFG 变化 ✅
cut 不变 ❌
最终模型不变
```

这特别重要。

---

### 所以我们第一次得到一个真正像研究结论的东西

不能问：

> “Algorithm 1 会不会扭曲 frequency？”

这个已经太浅。

甚至不能只问：

> “frequency distortion 会不会影响 IMf？”

还是太宽。

更好的问题是：

> **什么样的 frequency distortion 会跨过 IMf 的过滤边界，并进一步改变决定 cut 的结构证据？**

这句话里已经出现两个条件：

```text
条件 1：
跨 threshold

条件 2：
被改变的边对 cut decision 有结构意义
```

这就比“频次变了”深入了一层。

---

而这里还有一个很重要的科研 operator：

### 不要只测 effect size，要找 decision boundary

很多时候大家会自然问：

> 变化有多大？

比如：

```text
frequency error = 40%
```

但真正有研究价值的可能不是这个 40%，而是：

> **这个变化有没有跨过算法内部的决策边界？**

举个极端例子：

```text
0.90 → 0.50
```

变化很大，但 threshold = 0.3，两边都保留。

反过来：

```text
0.31 → 0.29
```

只变化 0.02，却刚好跨 threshold。

后者反而可能真正改变算法行为。

所以：

> **small perturbation can have large downstream effect；large perturbation can have zero downstream effect。**

这其实已经是很典型的 robustness / sensitivity 思维了。

---

现在把它映回 EX-06。

T0 真正值得裁定的，不是一个宏大题：

> “研究 EdgeIM 是否有问题。”

而是一个非常具体的对象：

```text
对象：
D → D′ 后的 DFG weight distortion

consumer：
IM / IMf

decision boundary：
IMf threshold + 后续 cut 条件

outcome：
过滤后 DFG / cut / process tree 是否分岔
```

这也正好符合 EX-06 对 T0 的要求：研究对象要建立在你前面自己的证据上，并且明确 claim ceiling，不能从一个局部现象直接跳成“EdgeIM 有缺陷”。

现在来一个很短的判断题：

```text
原始 D：
A→B = 100
A→C = 29

采样 D′：
A→B = 10
A→C = 4

threshold = 0.3
```

你先判断两件事：

1. `A→C` 在 D 和 D′ 里分别会不会被过滤？
2. 单凭这个结果，我们能不能断言最终 process tree 一定不同？

这两个答出来，我们就可以继续进 **“必要条件 / 充分条件”** 了。


————————————————————————————————————
这种方法论是什么的，控制论？
————————————————————————————————————
有一点像，但**不应该把我们现在这套叫“控制论方法论”**。你会联想到控制论很合理，因为我们确实一直在画这种东西：

`输入扰动 → 系统内部传播 → 决策边界 → 输出变化`

控制理论也研究系统对扰动、误差和参数变化的响应，并尤其关心 feedback、stability、robustness、sensitivity。MIT 的控制课程就是沿着反馈、稳定性、鲁棒性这些概念展开的。([MIT OpenCourseWare][1])

但我们刚才实际在做的，更准确地说是几种方法叠在一起：

1. **Sensitivity analysis / 敏感性分析**：改一点输入或参数，看输出怎么变。NIST 对 sensitivity analysis 的经典表述就是研究“改变输入所诱导的模型输出变化”，并用它寻找关键输入、关键假设和输出不变区域。([NIST 发布的技术系列出版物][2])
   我们这里就是：
   `DFG weight 改变 → IMf 输出是否改变？`

2. **Robustness analysis / 鲁棒性分析**：不是只问“变没变”，而是问：

   > 系统在多大的扰动范围内仍保持同样行为？

   比如：

   ```text
   weight 可以变很多
   但只要没跨 threshold
   → decision 不变
   ```

   这就是典型 robustness 思维。控制理论里 robustness 也非常核心，但这个概念早就跨到了算法、ML、软件系统等很多领域。([MIT Press][3])

3. **Decision-boundary analysis / 决策边界分析**：这是刚才最关键的那个 operator。不是问：

   > error 有多大？

   而问：

   > **error 有没有跨过使算法行为发生离散变化的边界？**

   所以 `0.31 → 0.29` 可能比 `0.9 → 0.5` 更重要。

4. **Mechanistic / causal decomposition，机制链拆解**：我们没有满足于相关性：

   ```text
   sampling → final model changed
   ```

   而是强行拆成：

   ```text
   sampling
   → weight distortion
   → threshold crossing
   → filtered DFG
   → cut
   → recursion
   → model
   ```

   然后逐箭头问：“这个传播真的发生吗？”
   这更接近机制分析 / causal reasoning，而不是经典控制论。

5. **Falsification / hypothesis testing**：我们故意找“频次变化很大但模型不变”的反例，是为了攻击自己的猜想，而不是搜支持材料。科学方法里这种从 hypothesis 推导可观察后果、再主动寻找反证的逻辑非常经典。([斯坦福哲学百科全书][4])

所以如果以后你想给我们这套研究动作一个名字，我反而建议记成：

> **机制驱动的敏感性 / 鲁棒性分析**
> `mechanism-guided sensitivity & robustness analysis`

或者更白话：

> **扰动 → 传播路径 → 决策边界 → 输出 → 反例**

这套东西和你以后想做的 **formal verification / AI safety** 其实连接得非常漂亮。比如 Agent：

```text
trajectory representation 丢了一点信息
        ↓
monitor / verifier 读取什么？
        ↓
这个 loss 有没有跨过判定边界？
        ↓
safe → unsafe judgment 会不会翻转？
```

你会发现这几乎就是我们现在 EdgeIM：

```text
sampling 丢了 frequency 信息
        ↓
IMf 读取什么？
        ↓
有没有跨 threshold？
        ↓
process model 会不会翻转？
```

所以你刚才突然想到“控制论？”其实抓到了一个**更高层的共同结构**。只是 taxonomy 上，我会把控制论放在它的一个重要邻居位置，而不是说“这就是控制论”。

而且还有个很有意思的连接：你之后学到 **necessary/sufficient condition、invariant、stability region、counterexample** 时，这几条会进一步汇合。到那个时候，你现在这套 EdgeIM 小实验会突然看起来很像一个缩小版的 verification / robustness 问题。

[1]: https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-10-feedback-and-control/?utm_source=chatgpt.com "Lecture 10: Feedback and Control | Signals and Systems | Electrical Engineering and Computer Science | MIT OpenCourseWare"
[2]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication616.pdf?utm_source=chatgpt.com "Validation and assessment of energy models"
[3]: https://mitpress.mit.edu/9780262693042/stability-and-robustness-of-multivariable-feedback-systems/?utm_source=chatgpt.com "Stability and Robustness of Multivariable Feedback Systems"
[4]: https://plato.stanford.edu/entries/scientific-method/?utm_source=chatgpt.com "Scientific Method (Stanford Encyclopedia of Philosophy)"


————————————————————————————————————————————————
这个知识坐标下都有什么东西啊？如果我想建立这种知识图谱应该以什么作为坐标轴，怎么去拓宽啊？
————————————————————————————————————————————————
对，而且我觉得你现在已经摸到一个**非常适合你长期科研训练的“母坐标系”**了。

关键不是建一张“控制论知识图谱”，而是建一张更高层的：

> **System Reasoning / Mechanism–Perturbation–Guarantee Map**
>
> 系统在扰动、信息损失、不确定性和环境变化下，为什么保持/改变行为，以及我们如何知道。

控制、形式化验证、鲁棒性、因果、软件测试、UQ、system identification……都可以挂在这张图上。

## 一、不要拿“学科”当主坐标轴

如果你这样画：

```text
控制论
├─ 鲁棒控制
├─ 自适应控制
└─ 最优控制

形式化方法
├─ model checking
├─ theorem proving
└─ abstract interpretation

软件测试
├─ fuzzing
└─ metamorphic testing
```

当然没错，但最后容易重新变成“背领域目录”。

你真正需要的是：

> **同一个 research operator 在不同领域里怎么出现。**

所以我建议你的主图用 **4 个正交坐标轴**。

---

# 轴 1：WHAT CHANGED？

## 扰动发生在哪一层？

这是最重要的一轴。

```text
World / Environment
        ↓
Observation / Data
        ↓
Representation
        ↓
Model / State
        ↓
Decision rule
        ↓
Action / Execution
        ↓
Outcome
        ↓
Feedback
```

分别可以问：

| 层              | 扰动例子                                      |
| -------------- | ----------------------------------------- |
| Environment    | distribution shift、环境变化                   |
| Observation    | noise、missing event、timestamp error       |
| Data           | sampling、subsampling、corruption           |
| Representation | abstraction、compression、feature loss      |
| Model          | parameter perturbation、approximation      |
| Decision       | threshold、policy、ranking                  |
| Execution      | concurrency、delay、tool failure            |
| Feedback       | closed-loop interaction、adaptive behavior |

你现在的 EdgeIM 正好落在：

```text
event log
   ↓ sampling
representation / statistics altered
   ↓
IMf decision threshold
   ↓
model structure
```

这也是为什么它可以自然迁移到 Agent Safety：

```text
agent trajectory
   ↓ compression / logging / abstraction
representation altered
   ↓
monitor / verifier
   ↓
safe / unsafe judgement
```

---

# 轴 2：WHAT QUESTION ARE WE ASKING？

## 研究动作是什么？

这一轴才是你真正应该积累的 **research operators**。

我会先放 9 个。

| Operator                | 核心问题                    |
| ----------------------- | ----------------------- |
| **Identify**            | 这个系统实际上是什么机制？           |
| **Perturb**             | 改一点输入，会发生什么？            |
| **Sensitivity**         | 哪些变量最影响输出？              |
| **Robustness**          | 多大扰动以内行为仍不变？            |
| **Boundary finding**    | 在哪里发生 qualitative flip？ |
| **Causal intervention** | 真正导致变化的是谁？              |
| **Verification**        | 某性质是否对所有允许行为成立？         |
| **Falsification**       | 最小反例是什么？                |
| **Diagnosis**           | 已经失败了，错误从哪里传播来的？        |

例如刚才 EdgeIM，我们已经偷偷做了：

```text
Perturb
D → D'

Sensitivity
frequency change 对 output 敏感吗？

Boundary
什么时候跨 IMf threshold？

Robustness
什么变化范围内 process tree 不变？

Falsification
frequency 变很大但 model 不变的反例

Diagnosis
如果最终模型变了，沿哪条路径传导？
```

NIST 对 sensitivity analysis 的定义就非常接近这个视角：研究输入不确定性如何影响模型输出，以及哪些变量重要、在哪些输入范围内模型有效。([NIST 发布的技术系列出版物][1])

---

# 轴 3：WHAT MUST REMAIN TRUE？

## 你到底关心什么性质？

这是 **property axis**。

它会把你的 formal verification 线直接接进来。

最常见的一组：

```text
Correctness
Safety
Liveness
Invariant
Stability
Robustness
Consistency
Conformance
Soundness
Completeness
Fairness
Efficiency
Privacy
Identifiability
Recoverability
```

这几个不能混。

例如：

```text
“模型输出一样”
```

和

```text
“模型仍然 sound”
```

不是一回事。

同样：

```text
“Agent 完成任务”
```

和

```text
“Agent 整个 trajectory 都满足 safety policy”
```

也不是一回事。

所以以后一个研究问题可以直接表示成：

> **Perturbation × Property**

例如：

```text
timestamp noise × conformance
sampling × model invariance
network delay × liveness
representation loss × safety judgement
parameter perturbation × stability
```

一下就能长出很多研究问题。

---

# 轴 4：HOW STRONG IS THE EVIDENCE？

## 你凭什么敢这么说？

这一轴就是 EX-06 的 `claim ceiling`。

可以从弱到强粗略排：

```text
intuition
↓
toy example
↓
counterexample
↓
finite experiment
↓
statistical evidence
↓
mechanistic explanation
↓
mathematical bound
↓
formal proof
```

注意这里不是严格总排序，因为它们解决的问题不同。

例如一个 counterexample 对推翻：

> “对所有输入都成立”

已经是决定性的。

但它不能证明：

> “大多数现实输入都不成立。”

反过来，大规模 empirical benchmark 很强，但通常不能证明 universal property。

这正是 formal verification 为什么存在：model checking 的核心就是检查一个抽象模型是否满足形式化 specification。([数字对象标识符][2])

---

# 二、把四个轴合起来，你得到的不是“树”，而是一个坐标

一项研究可以写成：

```text
Object
×
Perturbation
×
Property
×
Evidence / Guarantee
```

例如我们现在 EdgeIM：

```text
Object:
DFG / IMf pipeline

Perturbation:
feature-preserving sampling 导致 weight distortion

Property:
downstream model invariance

Decision boundary:
IMf filtering threshold / cut

Evidence:
toy → synthetic experiment → counterexample
```

这比：

> “我在学 process mining。”

信息量大得多。

---

# 三、这张地图周围有哪些大领域？

这时候再挂“学科”，它们就变成 **overlay**，而不是坐标轴。

### ① Sensitivity Analysis / Uncertainty Quantification

核心：

> **输入/参数有点不确定，输出会变多少？**

典型东西：

```text
local sensitivity
global sensitivity
parameter perturbation
uncertainty propagation
Sobol-style variance decomposition
adjoint sensitivity
```

NIST 把 sensitivity 直接定义为输入不确定性对模型输出的影响；现代 adjoint methods 则是在高维系统里高效算“哪个输入最影响哪个输出”。([NIST 发布的技术系列出版物][1])

你刚才的：

```text
edge frequency
↓ perturb
process tree
```

就是一个离散算法版 sensitivity problem。

---

### ② Robustness / Control

这里继续问：

> **变化多少以后系统才失效？**

控制里典型的是：

```text
state
dynamics
feedback
disturbance
stability
gain
margin
robustness
```

MIT 的控制课程明确把 modeling error、nonlinearity、delay 和 robustness 放在核心位置；robust control 则进一步研究 bounded uncertainty 下能否保持稳定等性质。([MIT OpenCourseWare][3])

你的 EdgeIM threshold 可以类比成一种离散 decision boundary。

但注意：

> 类比成立 ≠ EdgeIM 是控制系统。

这是 **research operator transfer**。

---

### ③ System Identification

这个领域跟你的胃口应该也挺合。

问题反过来了：

> **我只看到系统的 input/output，能不能推回它的模型？**

比如：

```text
input u(t)
   ↓
 unknown system
   ↓
output y(t)

→ infer model
```

它里面会碰到：

```text
identifiability
parameter estimation
model structure
noise
persistent excitation
model validation
```

MIT 的 System Identification 课程基本就是围绕“从观测行为构建数学系统模型”、identifiability、prediction error、model structure validation 等展开。([MIT OpenCourseWare][4])

这个对 process mining 本身就有很强的概念邻接。

因为 process discovery 本质上也带一点：

> behavior observations → model

的味道。

---

### ④ Formal Verification

这里不满足于：

> “我试了 10000 次好像没问题。”

而问：

> **允许状态空间里的所有行为，都满足 property 吗？**

重要家族：

```text
model checking
theorem proving
temporal logic
invariant checking
reachability
symbolic execution
SAT/SMT
runtime verification
```

model checking 的经典定义就是：

```text
model M
+
formal specification φ
→
M satisfies φ ?
```

并且失败时往往给 counterexample。([数字对象标识符][2])

所以你现在练的：

> 找最小反例、明确 property、区分 empirical 和 universal claim

会直接迁移过去。

---

### ⑤ Abstract Interpretation

这个可能尤其值得你记一个红星。

核心问题：

> **我不保留完整系统，而构造一个 abstraction；这个 abstraction 保留什么性质？**

例如：

```text
actual integer
↓ abstraction
positive / negative / zero
```

Cousot & Cousot 的经典 abstract interpretation 就是用抽象域中的计算去获得关于实际 computation 的可靠信息。([恩斯迪][5])

你发现没有：

EdgeIM 的：

```text
完整 event log
↓
S / E / R
```

在**思维结构**上和这个非常近：

> 丢掉很多信息，只保留足以服务 downstream reasoning 的摘要。

于是一个非常自然的问题就是：

> **这个 abstraction 对 downstream property 是否 sufficient？**

这条对你以后：

```text
Agent trajectory
→ abstract state / events / relations
→ safety verification
```

尤其重要。

---

### ⑥ Software Testing

这里的核心不是证明所有情况，而是：

> **怎么高效找到 failure？**

旁边会长出：

```text
property-based testing
fuzzing
mutation testing
differential testing
metamorphic testing
fault injection
```

尤其 **metamorphic testing** 很值得你收。

当没有明确 GT / test oracle 时，不问：

> 这次输出正确答案到底是什么？

而问：

> 我对输入作某种应该保持语义的 transformation 后，输出之间应该满足什么关系？

这正是 metamorphic testing 用来缓解 oracle problem 的核心思路。([白玫瑰研究网][6])

例如：

```text
input permutation
↓
如果语义不应改变
↓
output 应满足 invariant relation
```

你之前搞正序/逆序 Algorithm 1，其实就已经非常接近这种 research taste。

---

### ⑦ Causal / Intervention Thinking

这里的问题变成：

> **相关变化里，哪个变量是真正的机制节点？**

不是：

```text
sampling 和 model change 同时出现
```

而是：

```text
sampling
→ frequency distortion
→ threshold crossing
→ DFG change
→ cut change
→ tree change
```

然后 intervention：

```text
只固定 frequency
其余不变
```

看看结果还能不能出现。

这和传统的：

```text
correlation
vs
intervention
```

区别是一回事。

---

### ⑧ Reliability / Fault Tolerance / Safety Engineering

它关心：

```text
component failure
sensor fault
delay
message loss
crash
Byzantine behavior
```

如何传播：

```text
fault
→ error
→ failure
```

以及：

```text
detect
isolate
contain
recover
```

这跟你未来 Multi-Agent / distributed system 特别容易接起来。

---

# 四、所以你的知识图谱我建议长这样

不要造：

```text
控制论知识图谱
```

而是造：

```text
MECHANISM / ROBUSTNESS / VERIFICATION MAP
```

中心不是某个学科，而是：

```text
                    What property?
                         │
                         │
What changed? ── SYSTEM ── What mechanism?
                         │
                         │
               How do we know?
```

然后再加外围：

```text
                         FORMAL METHODS
                     proof / model checking
                            ↑
                            │
 UQ / sensitivity ←── SYSTEM ──→ causal inference
                            │
                            ↓
                  testing / falsification
                            │
                     fault injection
                            ↓
                  reliability / safety

         control                 system ID
     robustness/stability   inference/identifiability
```

---

# 五、真正建议你用的“节点 schema”

以后每碰到一个新方法，不要只记：

> XX 方法：定义……

而是固定回答 **9 个槽**：

```text
1. OBJECT
   它研究什么系统/表示？

2. PERTURBATION
   什么东西允许发生变化？

3. OBSERVABLE
   能看到什么？

4. PROPERTY
   希望保持什么？

5. MECHANISM
   变化通过哪条路径传播？

6. DECISION BOUNDARY
   哪里会发生 qualitative flip？

7. ORACLE / GT
   怎么知道结果正确？

8. GUARANTEE / EVIDENCE
   empirical / statistical / bound / formal？

9. FAILURE MODE
   什么条件下这个方法失效？
```

**这一张卡就是一个知识图节点。**

例如 IMf：

```text
OBJECT
DFG

PERTURBATION
edge frequency

OBSERVABLE
weighted DFG

PROPERTY
noise-filtered discovery quality

MECHANISM
frequency → filtering → cut → recursion

DECISION BOUNDARY
noise threshold

ORACLE
GT / reference log / evaluation metric

GUARANTEE
目前按具体论文与实验确定

FAILURE MODE
frequency distortion 跨过 threshold；
错误过滤结构证据；等等
```

这样 IMf 就不再只是“一个 process mining 算法”。

---

# 六、怎么向外拓宽：不要按论文数量拓宽

这是我觉得最重要的一点。

不要：

```text
EdgeIM
↓
读 20 篇 process mining
↓
读 50 篇 formal verification
```

会炸。

应该使用 **一格一格横移**。

比如我们现在有：

```text
sampling
→ representation distortion
→ decision boundary
→ output
```

第一圈只找：

**同问题，不同方法**

```text
sensitivity analysis
robustness analysis
```

第二圈：

**同 operator，不同领域**

```text
IMf threshold
→ classifier decision boundary
→ control stability margin
→ verification abstraction boundary
```

第三圈：

**同 object，不同 question**

```text
DFG
├─ information preservation?
├─ robustness?
├─ identifiability?
├─ verification?
└─ causal sufficiency?
```

第四圈：

**找反例领域**

> 有没有一个领域告诉我：
> “你现在这个 framing 根本不对？”

第五圈：

**追 genealogy**

```text
这个方法解决什么旧问题？
↓
上一代怎么做？
↓
它修了什么？
↓
又制造了什么 residual？
↓
后人怎么修？
```

这才是真正的“菌丝式扩图”。

---

# 七、而且我会给你设置一个停止规则

否则按照你的习惯，这张图能一路长到数学哲学（）。

一个节点只有满足下面至少一条才展开：

> **A. 会改变当前研究问题；**
> **B. 会改变实验设计；**
> **C. 会改变 claim ceiling；**
> **D. 提供一个可迁移 research operator；**
> **E. 是当前方法的 strongest counterexample / competing approach。**

否则：

```text
PARK
```

不是“不重要”，而是：

> **当前 marginal information value 不够。**

---

## 最后给你一个更高层的坐标

如果让我从零给你建，我甚至会把这整个地图压成三个大问题：

### I. Representation

> **我们保存的信息够不够？**

这里长：

```text
abstraction
compression
sufficient statistics
information loss
observability
identifiability
state representation
```

### II. Perturbation

> **世界发生变化以后，我们的结论还成立吗？**

这里长：

```text
sensitivity
robustness
stability
distribution shift
fault injection
adversarial perturbation
uncertainty
```

### III. Guarantee

> **我们凭什么相信结论？**

这里长：

```text
ground truth
experiment design
statistics
testing
falsification
invariants
formal verification
model checking
proof
```

然后第四个横穿三者：

### IV. Mechanism

> **为什么？变化是怎么传过去的？**

```text
causal chain
data flow
state transition
feedback
dependency
failure propagation
```

这四根轴，其实比“控制论 / 软件工程 / AI safety / process mining”更适合你。

因为你的长期问题很可能会不断换领域，但这四个问题**不会换**：

> **我保留了什么？**
>
> **什么变化会让它坏？**
>
> **坏是怎么传过去的？**
>
> **我凭什么知道？**

你现在 EdgeIM 的 EX-06，其实第一次在非常小的玩具世界里，把这四件事同时碰齐了。这个节点值得保留下来，不只是“学完 EdgeIM 第六节”。

[1]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1030.pdf?utm_source=chatgpt.com "5 Sensitivity of the Model"
[2]: https://doi.org/10.1145/1592761.1592781?utm_source=chatgpt.com "Model checking: algorithmic verification and debugging: Communications of the ACM: Vol 52, No 11"
[3]: https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/?utm_source=chatgpt.com "Feedback Control Systems | Aeronautics and Astronautics | MIT OpenCourseWare"
[4]: https://ocw.mit.edu/courses/6-435-system-identification-spring-2005/?utm_source=chatgpt.com "System Identification | Electrical Engineering and Computer Science | MIT OpenCourseWare"
[5]: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml?utm_source=chatgpt.com "P. Cousot & R. Cousot, Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints"
[6]: https://eprints.whiterose.ac.uk/id/eprint/110335/?utm_source=chatgpt.com "A Survey on Metamorphic Testing - White Rose Research Online"

继续。我们把刚才那张“大地图”收回到 **EX-06 当前这一小步**，不继续横向扩了。

你刚才其实已经准备好进入一个很关键的东西：

> **必要条件 / 充分条件**

这正好用来把“frequency distortion 会不会导致最终模型变化”说清楚。

先定义：

* **必要条件**：没有它，这件事一定不会发生。
* **充分条件**：只要它发生，这件事一定会发生。

放进我们当前链条里：

```text
frequency distortion
→ threshold crossing
→ filtered DFG change
→ cut change
→ process tree change
```

这里，**frequency distortion 不是 process tree change 的充分条件**。因为频次可以变很多，但没跨 threshold，最终什么都不变。

同样，**threshold crossing 也不一定是最终 process tree change 的充分条件**。它可能让某条边的过滤状态变化，但这条边不影响 cut，最后树还是一样。

所以更准确地说：

```text
frequency distortion
    ↓
可能导致 threshold crossing

threshold crossing
    ↓
可能导致 filtered DFG change

filtered DFG change
    ↓
可能导致 cut change

cut change
    ↓
才比较直接地导致递归结构变化
```

这就是为什么研究问题不能写成：

> “频次改变是否会改变最终模型？”

太粗。

更好的问题是：

> **在什么条件下，sampling 引起的频次失真会跨过 IMf 的过滤边界，并进一步改变决定 process-tree cut 的结构信息？**

这个版本已经开始有“机制条件”了。

然后 EX-06 的 T0 就要你做一件事：

> **从所有可能研究的问题里，选一个现在证据最扎实、最能被实验打脸、范围又不失控的对象。**

你可以把它想成：

```text
很多观察
↓
很多可能问题
↓
删掉宏大/模糊/不可测的
↓
留下一个最小可研究对象
```

我们现在这个候选其实已经很清楚了：

```text
对象：
EdgeIM Stage 1 sampling 后的 DFG weight distortion

下游 consumer：
IM / IMf

关键边界：
IMf threshold + cut condition

结果：
filtered DFG / cut / process tree 是否分岔
```

接下来最自然的一步，就是把它写成三个版本：

1. **Observation**
2. **Research Question**
3. **Hypothesis**

比如：

```text
Observation:
D 和 D' 可以保持相同的 edge set，
但 edge weights 不同。

Research Question:
这种 weight distortion 在什么条件下
会改变 IMf 的过滤结果及最终 process tree？

Hypothesis:
当 weight distortion 使关键边的相对频次
跨过 IMf threshold，
且该边参与决定某个 cut 时，
D 与 D' 的最终 process tree 可能分岔。
```

注意 hypothesis 里我特意加了：

> **且该边参与决定某个 cut**

因为只跨 threshold 还不够。

现在你来试一下，只写 **Research Question** 那一句。

不用漂亮，不用论文腔。你就按自己的话，把我们现在真正想问的问题写出来。
