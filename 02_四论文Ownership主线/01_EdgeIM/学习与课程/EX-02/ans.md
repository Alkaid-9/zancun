节点记录：`已有证据（EX-01 的 DFG） -> 当前节点（sequence cut） -> 前置依赖（节点、方向、分组） -> 后继概念（choice，再 parallel，再 loop） -> 暂时封存（Petri net；soundness，健全性；复杂 IMf，即带低频过滤的归纳式发现变体）`。这些封存项本轮不要求定义、计算或使用。

**站**: 第 2 站（BRIEF §2 + A1：5–6h，拆 2a / 2b）
**前置**: EX-01 任务 1–4 的三张 DFG 表（原始 D、D′正序、D′逆序）；EX-05a 的 `algo1.py`
**产出**: `EX-02/` 下你的手切过程树（纸/照片）+ `EX-02/run.py` 与输出
**PASS 条件**（冻结）: 在 EX-00 日志的 DFG 上手切出过程树；用 pm4py 跑出模型并指出与手切的异同；用一句话说清 `noise_threshold` 按什么砍边、为什么第 1 站的频次塌平会让它失效

a→b
a→c
b→d
c→d

a
b c
d

是choice，二选一，
    ×(P,Q)

parallel（前后可以交换）
    ∧(P,Q)

loop（body redo body）
    ↺(body,redo)


| 符号        | 读法  | 意思                   | 例：允许的 trace             |
| --------- | --- | -------------------- | ----------------------- |
| `→(a, b)` | 顺序  | 先 a 后 b              | `a b`                   |
| `×(a, b)` | 二选一 | a 或 b，只做一个           | `a` 或 `b`               |
| `∧(a, b)` | 并行  | a、b 都做，顺序随意          | `a b` 或 `b a`           |
| `↺(a, b)` | 循环  | 做 a；之后可以"b 再 a"重复任意次 | `a`、`a b a`、`a b a b a` |


`τ`（tau）表示"什么都不做"。`×(τ, b)` 就是"b 可做可不做"。

树可以套：`→(a, ×(τ, b), c)` 允许 `a c` 和 `a b c`。

→(X,x(τ, Y), Z )

只允许了两个trace
——————
**基本情形**：一组里只剩一个活动 a → 树就是 `a`。拆出的子日志里如果有空 trace（这一段什么都没做）→ 包一层 `×(τ, …)`。

**找不到切**：叫 fall-through，pm4py 有兜底规则，本站不学；碰到就写"找不到切"，记下来。

这里是什么？

---

→(
    A, x(B, C),x(τ，C), D, x(↺(E,D), F)
)

`∧(a, b)`这里还是不太明白

**任务 6**：对 D′正序（{1,2,3,6}）重做任务 1–4。树一样吗？**先预测再做**：写下"一样 / 不一样，因为……"。

一样的
————————————————

**任务 8**：`tree` 打印出来的树，跟你任务 4 手切的树对。pm4py 的写法：`->` 是 →，`X` 是 ×，`+` 是 ∧，`*` 是 ↺，`tau` 是 τ。一样吗？不一样的地方，谁对？（提示：可能是运算符嵌套顺序不同但等价，也可能真不一样——用任务 5 的办法各走一遍六条 trace 判。）

```
    empty_traces = EmptyTracesUVCL.apply(obj, parameters)
    if empty_traces is not None and empty_traces[1]:
        number_original_traces = sum(
            y for y in obj.data_structure.values()
        )
        number_filtered_traces = sum(
            y for y in empty_traces[1][1].data_structure.values()
        )

        if (
            number_original_traces - number_filtered_traces
            > noise_threshold * number_original_traces
        ):
            return self._recurse(
                empty_traces[0], empty_traces[1], parameters
            )
        else:
            obj = empty_traces[1][1]
```



### 6. 任务

**任务 7**：跑上面的代码。`dfg` 打印出来的 8 条边和次数，跟你 EX-01 任务 1 的表**逐条对**。对不上的先怀疑自己的表，再怀疑代码。

**任务 8**：`tree` 打印出来的树，跟你任务 4 手切的树对。pm4py 的写法：`->` 是 →，`X` 是 ×，`+` 是 ∧，`*` 是 ↺，`tau` 是 τ。一样吗？不一样的地方，谁对？（提示：可能是运算符嵌套顺序不同但等价，也可能真不一样——用任务 5 的办法各走一遍六条 trace 判。）

**任务 9**：用 `algo1`（EX-05a）过滤出 D′ 正序，做成 `df2`，再跑一次 `discover_process_tree_inductive`。跟任务 6 的预测对。

**任务 10 ·** `noise_threshold`：

`discover_process_tree_inductive(df, noise_threshold=t)`，t 从 0.0 到 0.5，每 0.1 一档，**D 和 D′ 各跑一遍**，12 棵树列一张表：

```
t | D 的树 | D′ 的树 | 一样吗
```

**公开核心数量口径只有一个**：`D` 六个阈值 + **正序** `D′={1,2,3,6}` 六个阈值，共 12 棵树、表中 12 个树单元。这里的 `D′` 均指正序 D′。

- 在哪个 t，D 和 D′ 的树第一次不一样？哪一部分变了？
- 那个 t 之下，D 的树自己有没有变？D′ 的树呢？

**EXTEND（可选，不影响 PASS）**：再对逆序 `D′={6,5,4}` 跑同样六个阈值，另列 6 棵树，用来观察遍历顺序改变保留集后，下游何时出现可见差异。这 6 棵不计入公开核心 12 棵，不做也不影响 PASS。

**任务 11 · 它按什么砍**：打开本机文件
`/home/alkaid/miniconda3/envs/solver/lib/python3.10/site-packages/pm4py/algo/discovery/inductive/variants/imf.py`
只看两处：第 64–81 行（关于空 trace）和第 103–127 行（`__filter_dfg_noise`）。每处用一句话写出"什么东西 和 什么东西 比，小于就砍"。不用看懂其余部分。

**任务 12 · 回到第 1 站**：用任务 11 的两句话解释任务 10 里 D 和 D′ 分岔的那个 t：过滤把哪个数字改了，改到了阈值的哪一边？用 D 和 D′ 的具体次数算给我看。

对，那我们顺着这个点把 EX-02 任务 2–4 的手切主干接起来。

现在原始 DFG 是：

A→B   A→C
B→C   B→D
C→D
D→E   E→D
D→F

第一刀：sequence cut

我们可以把活动分成：

{A} → {B} → {C} → {D,E} → {F}

为什么这个分组成立？

因为所有跨组边都只往右：

A→B
A→C
B→C
B→D
C→D
D→F

没有一条从后面的组倒着回到前面的组。

而 D→E、E→D 都留在 {D,E} 组内，所以不会破坏外层 sequence cut。这个正是 README 里 sequence cut 的基本判据。

---

然后就是任务 3：把每条 trace 按这些组投影/拆段。

例如：

case1 = A B D F

按

{A} | {B} | {C} | {D,E} | {F}

拆就是：

A | B | ∅ | D | F

这里这个 ∅ 很重要——它意味着在 {C} 这一段，case1 什么都没做。

六条全拆开：

case	A组	B组	C组	{D,E}组	F组

1 ABDF	A	B	∅	D	F
2 ACDF	A	∅	C	D	F
3 ABDEDF	A	B	∅	DED	F
4 ABDF	A	B	∅	D	F
5 ACDEDF	A	∅	C	DED	F
6 ABCDF	A	B	C	D	F

现在你就能看到为什么 PM4Py 那棵树是：

→(
  A,
  ×(τ,B),
  ×(τ,C),
  ↺(D,E),
  F
)

因为：

{A}：永远是 A → A

{B}：有的 trace 有 B，有的为空 → ×(τ,B)

{C}：有的 trace 有 C，有的为空 → ×(τ,C)

{D,E}：只有 D 或 DED → ↺(D,E)

{F}：永远是 F → F

所以你手切出来的完整树，应该跟 PM4Py 语义上完全一致。

---

这里有一个很关键的新连接：

> optional 不是因为 DFG 上“看起来像可选”，而是因为 sequence cut 之后，投影到某个子组时出现了 empty trace。

也就是：

sequence cut
    ↓
project / split traces
    ↓
某个子日志出现空 trace
    ↓
×(τ, subtree)

这个比单背“×(τ,B) = B 可选”更重要，因为现在你知道它是怎么从日志里长出来的。

你现在可以自己做一个很小的检查：

> 为什么 {B} 和 {C} 都是 optional，
> 但 {D,E} 不是 optional？

————————————————

可以先只看成“给每个源节点找一个参照频次，然后判断它的弱出边要不要当噪声删掉”。

源码先做的事是：对每个 activity，看它所有 outgoing DFG 边里谁出现得最多，把这个最大次数记成 outgoing_max_occ。

如果这个 activity 本身还可能作为 end activity，它的结束次数也会参与这个最大值的计算。然后每条边 (u,v) 都拿自己的次数去和
t\times \text{maxoutgoing}(u)

比较；只有严格大于才留下。

拿你的原始 D 举例，DFG 是：

A→B  4     A→C  2
B→D  3     B→C  1
C→D  3
D→F  6     D→E  2
E→D  2

所以每个源节点的“最强出边”是：

A: 4
B: 3
C: 3
D: 6
E: 2

例如 B→C 只有 1 次。若 t=0.3，它比较的是：


1 > 0.3\times3=0.9


成立，所以保留。

若 t=0.4：


1 > 0.4\times3=1.2


不成立，所以这条边会被当噪声过滤。

因此 Task 11 第二句话可以写成：

> 一条 DFG 边的频次，和 noise_threshold × 该源节点最强 outgoing 频次 比；如果不超过这个值，就砍掉。

这里同样要记住“等于也砍”，因为源码的保留条件是严格 >。

---

现在 Task 11 两句话完整了：

> Empty trace： empty trace 数和 t × 当前子日志总 trace 数 比；不超过就把 empty trace 当噪声删掉。

> DFG edge： 边频次和 t × 该源节点最大 outgoing 频次 比；不超过就把边当噪声删掉。

这两句其实属于同一个 pattern：


\text{局部弱信号}
\quad\text{vs}\quad
t\times\text{局部参照量}


区别只是“局部弱信号”一个是 empty trace 数，一个是 edge count。

---

Task 12 现在重新自己走一遍

第一次分岔：

t = 0.3

D :  X(tau, B)
D':  B

因此先追 tau，对应 empty trace rule。

原始 D 中：

6 条 trace
4 条含 B
2 条不含 B

投影到 {B} 后就是：

**<> <>**

所以：


empty(D)=2,\qquad total(D)=6


阈值侧：


0.3\times6=1.8


比较：


2>1.8


所以 empty trace 太多，不算噪声，不能删。





因此“B 可以缺席”这个证据还存在：

X(tau, B)

而正序 D′ 只有：

case1
case2
case3
case6

其中只有 case2 没有 B：


empty(D')=1,\qquad total(D')=4


于是：


0.3\times4=1.2


比较：


1>1.2


不成立，也就是：


1\le1.2


所以这一条 empty trace 被当噪声删掉。

删完以后投影只剩：



PM4Py 再也看不到“B 可以不出现”的证据，于是：

X(tau, B) → B

所以 Task 12 可以写成：

> Algorithm 1 把“不含 B 的 trace”从 2/6 = 33.3% 改成 1/4 = 25%。在 t=0.3 时，D 的 33.3% 高于阈值，因此 empty traces 保留；D′ 的 25% 不超过阈值，因此被过滤，于是 X(tau,B) 变成 B。

注意这里真正被 Algorithm 1 改掉的不只是“2 变 1”，而是：


\boxed{2/6\to1/4}


也就是次数和分母一起变，最终改变了比例。

这正好回答你脱稿最后那句将要问的：

> 为什么 Algorithm 1 后的 D′ 会让 noise filtering 不一样？

因为 Algorithm 1 保证的是某些结构关系至少出现过，它并不保持原始 trace 的频次分布；一旦下游算法按“次数 / 比例阈值”做决定，过滤后的日志就可能跨到阈值另一边。

现在 Task 11、12 都已经接上了。下一步其实就是这一站最后那个 10 分钟脱稿：四种 cut + noise threshold + Algorithm 1 为什么影响它。那一步我应该先不替你答，我们可以直接开始验收。