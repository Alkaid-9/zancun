# EX-02 · Inductive Miner 直觉；pm4py 首装首跑；`noise_threshold` 是什么

## 先读：只开第一种“顺序切”的六步入口

下面六步走完之前，不打开 choice、parallel、loop，也不需要先懂 Petri net（佩特里网，后续的一种模型表示；本轮只记名字，正式定义封存）。

**1. 它解决什么问题。** DFG（directly-follows graph，直接跟随图）只记录哪些活动曾经相邻，以及可选的边权；“沿边描一遍”得到的仍是一张图，不会自动说明活动应怎样分组，也没有明确的顺序、选择、并行或循环语义。要得到可递归理解的流程模型，当前只补第一种分组动作：sequence cut（顺序切）。

**2. 与正式题不同的四活动微例。** 某个玩具物流图只有四个活动 `收件、分拣、装车、签收`，边为 `收件->分拣`、`分拣->装车`、`装车->签收`。不要套用 L1；在纸上画这四个点和三条边。

**3. 正式定义与符号。** 设 DFG 为 `G=(V,E)`：`V` 装活动节点，`E` 装有方向的直接跟随边。把 `V` 分成互不重叠且合起来仍是 `V` 的非空组 `P1,...,Pk`。若观察到的跨组边只从较早的 `Pi` 指向较晚的 `Pj`（`i<j`），没有从较晚组回到较早组的边，就得到 sequence cut 的基本直觉：这些组按 `P1 -> ... -> Pk` 排列。这里是四节点手切所需判据，不是完整 IM 实现的形式化规范。

**4. 亲手切一次。** 在微例图上画三条竖线，把四个单节点分成四组；逐条检查每条跨组边的方向。然后只反转 `装车->签收` 为 `签收->装车`，写出原分组的哪条检查不再成立。先留下纸面分组和理由，再继续阅读。

**5. 接回 EdgeIM。** 上游是 Stage 2/中心合并得到的 DFG；当前动作读节点与边方向，输出一个“这些活动组按顺序组合”的候选结构，供递归继续处理并最终形成 process tree（过程树，用运算符分层表达行为的树状模型）。weight（边权）在具体实现的哪一步被读取，要用源码或原文核查，不能从这张微例图猜。

**6. 研究追问与边界。** 若只增加一条反向边，原切分一定失败，还是可能换一组分法继续成立？把答案先写成可被图反例推翻的 hypothesis（假设）。一张微例只证明你会执行这次分组检查，不能证明完整 IM 对所有日志正确，也不能证明生成模型与原日志语言等价。

节点记录：`已有证据（EX-01 的 DFG） -> 当前节点（sequence cut） -> 前置依赖（节点、方向、分组） -> 后继概念（choice，再 parallel，再 loop） -> 暂时封存（Petri net；soundness，健全性；复杂 IMf，即带低频过滤的归纳式发现变体）`。这些封存项本轮不要求定义、计算或使用。



**站**: 第 2 站（BRIEF §2 + A1：5–6h，拆 2a / 2b）
**前置**: EX-01 任务 1–4 的三张 DFG 表（原始 D、D′正序、D′逆序）；EX-05a 的 `algo1.py`
**产出**: `EX-02/` 下你的手切过程树（纸/照片）+ `EX-02/run.py` 与输出
**PASS 条件**（冻结）: 在 EX-00 日志的 DFG 上手切出过程树；用 pm4py 跑出模型并指出与手切的异同；用一句话说清 `noise_threshold` 按什么砍边、为什么第 1 站的频次塌平会让它失效

作答写别的文件，不追加进本 README。

---

## 2a · 手切（约 2.5h）

### 1. 教学：过程树是什么

DFG 是"谁后面跟谁"的图。过程树是把这张图**读成一句话**：先做什么、再做什么、二选一、并行、重复。你已经完成顺序切；下面才依次打开 choice、parallel、loop 三个新节点。

#### 1.1 Choice cut（二选一切）

1. **问题**：若几组行为互为替代，一次只走其中一组，需要明确表达“二选一”，不能把两条分支误读为都要执行。
2. **微例**：只有两个活动 `短信`、`邮件`，日志分别是一条 `短信` 和一条 `邮件`。
3. **定义**：把节点分成非空组 `P,Q`；若 `P` 与 `Q` 之间两个方向都没有直接跟随边，就得到 choice cut 的基本直觉，过程树写 `×(P,Q)`。
4. **亲手动作**：画两个点，检查组间边为零，再写 `×(短信,邮件)`；若增加 `短信->邮件`，写哪项检查改变。
5. **接回 EdgeIM**：输入仍是 DFG 的节点与边，输出是候选选择分组，递归再处理各组。
6. **研究追问**：图上没有跨组边，可能是业务互斥，也可能只是日志没有观察到；写一个能区分这两种解释的新增证据。微例不能证明真实业务必然互斥。

#### 1.2 Parallel cut（并行切）

1. **问题**：若几组都要发生，但先后可交换，需要把“可换序”与“二选一”分开。
2. **微例**：两条 trace 是 `拍照 签字` 与 `签字 拍照`。
3. **定义**：把节点分成非空组 `P,Q`；在这个最小判据里，`P` 中每个活动与 `Q` 中每个活动之间两个方向都有边，并且两组各自能贡献起点与终点，才是 parallel cut 的候选，写 `∧(P,Q)`。
4. **亲手动作**：画双向边，标出两条 trace 的起点和终点，再写 `∧(拍照,签字)`；删去一个方向后重做检查。
5. **接回 EdgeIM**：上游提供 DFG 及起止信息，输出是候选并行分组；具体实现读取哪些字段仍要核源码。
6. **研究追问**：双向相邻是并发造成，还是不同案例恰好给出相反顺序？写一个竞争解释和最低成本检查。微例只支持候选切分，不证明一般并发语义。

#### 1.3 Loop cut（循环切）

1. **问题**：若一个主体做完后可经“回头路”再进入主体，单纯顺序无法表达重复次数。
2. **微例**：允许 `填写`，也允许 `填写 复核 填写`；活动只有 `填写、复核`。
3. **定义**：把活动分为 body（主体）和 redo（回头路）；观察到主体终点通向 redo、redo 再通向主体起点时，得到 loop cut 的基本直觉，写 `↺(body,redo)`，例中为 `↺(填写,复核)`。
4. **亲手动作**：画两方向边，分别在两条 trace 上标起点、终点和回到主体的位置；再写它允许的下一条更长 trace。
5. **接回 EdgeIM**：输入是 DFG 与起止活动，输出是候选循环分组；递归继续处理主体和回头路。
6. **研究追问**：同一张双向图为何也可能被解释成 parallel 候选？列出还需核对的起止信息和实现判据。这里不教学完整 loop 边界条件。

三座桥各留一行 `问题 -> 微例图 -> 分组理由 -> 能支持什么 / 不能支持什么`。完成后再看四个运算符的汇总表：

| 符号 | 读法 | 意思 | 例：允许的 trace |
|---|---|---|---|
| `→(a, b)` | 顺序 | 先 a 后 b | `a b` |
| `×(a, b)` | 二选一 | a 或 b，只做一个 | `a` 或 `b` |
| `∧(a, b)` | 并行 | a、b 都做，顺序随意 | `a b` 或 `b a` |
| `↺(a, b)` | 循环 | 做 a；之后可以"b 再 a"重复任意次 | `a`、`a b a`、`a b a b a` |

`τ`（tau）表示"什么都不做"。`×(τ, b)` 就是"b 可做可不做"。

树可以套：`→(a, ×(τ, b), c)` 允许 `a c` 和 `a b c`。

**微例子**（跟练习不同）：日志 `X Y Z`、`X Y Z`、`X Z`。过程树 `→(X, ×(τ, Y), Z)`。检查：三条 trace 都能被它"走出来"吗？还允许了别的 trace 吗？（这里没有：它恰好只允许这两种。）

### 2. 教学：Inductive Miner 在干什么

一句话：**在 DFG 上找一条"切线"，把活动分成几组，判断组和组之间是四种关系里的哪一种，然后把日志按组拆开，对每一组重复这件事，直到一组里只剩一个活动。**

四种切在 DFG 上长什么样（把活动分成两组 P、Q 来看）：

- **顺序切 →**：所有跨组的边都从 P 指向 Q，没有从 Q 回 P 的边
- **二选一切 ×**：P 和 Q 之间一条边都没有
- **并行切 ∧**：P 的每个活动和 Q 的每个活动之间**双向**都有边，而且两组各自都有起点活动和终点活动
- **循环切 ↺**：一组是"主体"，一组是"回头路"；从主体的终点出去到回头路，再从回头路回到主体的起点；起点和终点活动都在主体里

找切的顺序固定：先试 ×，再 →，再 ∧，最后 ↺。找到就切，切完拆日志、递归。

**基本情形**：一组里只剩一个活动 a → 树就是 `a`。拆出的子日志里如果有空 trace（这一段什么都没做）→ 包一层 `×(τ, …)`。

**找不到切**：叫 fall-through，pm4py 有兜底规则，本站不学；碰到就写"找不到切"，记下来。

### 3. 任务

**任务 1**：把 EX-01 任务 1 的 DFG（8 条边，S={A}，E={F}）画在纸上，只画边，先不管数字。

**任务 2 · 第一刀**：试四种切。哪一种成立？把活动分成几组？写出切完的第一层树，形如 `→(?, ?, ?, ?)` 或别的运算符。

**任务 3 · 拆日志**：按第一刀的分组，把六条 trace 各自拆成几段。比如 case1 `A B D F` 拆成 `A | B | D | F`。列一张 6 行的表。注意有的 case 在某一段是**空**的。

**任务 4 · 递归**：对每一组继续切，直到只剩单个活动。有空 trace 的那段包 `×(τ, …)`。写出完整的树。

**任务 5 · 验证**：用你的树把六条 trace 各走一遍（每条能不能"走出来"）。再问：你的树允许了日志里**没有**的 trace 吗？举一条。




**任务 6**：对 D′正序（{1,2,3,6}）重做任务 1–4。树一样吗？**先预测再做**：写下"一样 / 不一样，因为……"。

一样。


---

## 2b · pm4py 首装首跑（约 2.5h）

### 4. 环境

本机已装：`python3` = `/home/alkaid/miniconda3/envs/solver/bin/python3`（3.10），`pm4py 2.7.23.6`（2026-09-04 核实；PyPI 现行 2.7.23.8，不升级）。第一次 import 会打一段 AGPL 许可横幅，不是报错。

装不上 / import 报错 → 发我，环境问题归我（BRIEF §3）。

### 5. 把日志喂给 pm4py（这段代码直接用，API 层不算作弊）

pm4py 要的输入是一张三列表：case 编号、活动名、时间戳。列名有默认约定。

```python
import datetime
import pandas as pd
import pm4py

LOG = {
    "case1": "ABDF", "case2": "ACDF", "case3": "ABDEDF",
    "case4": "ABDF", "case5": "ACDEDF", "case6": "ABCDF",
}

def to_df(log):
    rows = []
    for case, acts in log.items():
        for i, a in enumerate(acts):
            rows.append({"case:concept:name": case,
                         "concept:name": a,
                         "time:timestamp": datetime.datetime(2026, 1, 1, 0, i)})
    return pm4py.format_dataframe(pd.DataFrame(rows))

df = to_df(LOG)
dfg, start, end = pm4py.discover_dfg(df)
print(dfg, start, end)
tree = pm4py.discover_process_tree_inductive(df)
print(tree)
```

时间戳是编出来的：同一 case 内第 i 个事件给第 i 分钟，只为保证顺序。

{('A', 'B'): 4, ('A', 'C'): 2, ('B', 'C'): 1, ('B', 'D'): 3, ('C', 'D'): 3, ('D', 'E'): 2, ('D', 'F'): 6, ('E', 'D'): 2} {'A': 6} {'F': 6}
->( 'A', X( tau, 'B' ), X( tau, 'C' ), *( 'D', 'E' ), 'F' )



### 6. 任务

**任务 7**：跑上面的代码。`dfg` 打印出来的 8 条边和次数，跟你 EX-01 任务 1 的表**逐条对**。对不上的先怀疑自己的表，再怀疑代码。

对的上

**任务 8**：`tree` 打印出来的树，跟你任务 4 手切的树对。pm4py 的写法：`->` 是 →，`X` 是 ×，`+` 是 ∧，`*` 是 ↺，`tau` 是 τ。一样吗？不一样的地方，谁对？（提示：可能是运算符嵌套顺序不同但等价，也可能真不一样——用任务 5 的办法各走一遍六条 trace 判。）


**任务 9**：用 `algo1`（EX-05a）过滤出 D′ 正序，做成 `df2`，再跑一次 `discover_process_tree_inductive`。跟任务 6 的预测对。



**任务 10 · `noise_threshold`**：

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




        empty_traces = EmptyTracesUVCL.apply(obj, parameters)

<!-- 检查当前子日志里，有没有空的trace，并给我一个“保留空trace”和“删掉空trace”之后的候选结果 -->

        if empty_traces is not None and empty_traces[1]:
<!-- 如果发现empty-trace 这种情况，且有可处理的结果，那就继续 -->

            number_original_traces = sum(
                y for y in obj.data_structure.values()
            )
<!-- 当前子日志总共有多少trace -->

            number_filtered_traces = sum(
                y for y in empty_traces[1][1].data_structure.values()
            )

<!-- empty_traces[1][1]是把empty trace删掉之后剩下的日志 -->
<!-- number_filtered_traces是删掉空trace后，还剩多少条非空trace -->


            if (
                number_original_traces - number_filtered_traces
                > noise_threshold * number_original_traces
            ):

<!--空 trace 数量 > noise_threshold × 总 trace 数量 -->
<!-- 空/总 ＞ 噪声阈值-->

                return self._recurse(
                    empty_traces[0], empty_traces[1], parameters
                )
            else:

                obj = empty_traces[1][1]
<!-- 如果 empty trace 比例很小：
“它出现得够少，可以当噪声处理。”
于是：
obj = empty_traces[1][1]
直接把当前对象换成：
删掉 empty traces 后的日志。
所以整段代码你最后只需要记成这一句：
先算 empty trace 占当前子日志的比例；如果这个比例不超过 noise_threshold，就把 empty traces 当噪声删掉。 -->




其实也就是说：小于、相等都会被砍

if empty_count > threshold * total:
    # 保留 empty trace 结构
else:
    # 过滤 empty traces

__filter_dfg_noise 的核心是：
某条 DFG 边的频次 和 noise_threshold × 该边源节点所有 outgoing 边中的最大频次 比；如果该边频次 ≤ 这个阈值，就把边过滤掉。
源码保留条件是严格的 >，所以同样是 ≤ 就砍。


总结：

1. 看当前子日志里有没有 empty trace
2. 记下当前总 trace 数 = N
3. 删除 empty trace 后，剩余 trace 数 = M
4. empty trace 数 = N - M
5. 比较 (N - M) 和 noise_threshold × N
6. 如果 empty trace 比例不超过阈值，就把 empty trace 当噪声删掉

===================

一条 DFG 边的频次，和 noise_threshold × 该源节点最强 outgoing 频次 比；如果不超过这个值，就砍掉。
现在 Task 11 两句话完整了：

Empty trace： empty trace 数和 t × 当前子日志总 trace 数 比；不超过就把 empty trace 当噪声删掉。

DFG edge： 边频次和 t × 该源节点最大 outgoing 频次 比；不超过就把边当噪声删掉。

这两句其实属于同一个 pattern：

\text{局部弱信号}
\quad\text{vs}\quad
t\times\text{局部参照量}

区别只是“局部弱信号”一个是 empty trace 数，一个是 edge count。

**任务 12 · 回到第 1 站**：用任务 11 的两句话解释任务 10 里 D 和 D′ 分岔的那个 t：过滤把哪个数字改了，改到了阈值的哪一边？用 D 和 D′ 的具体次数算给我看。

Algorithm 1 把“不含 B 的 trace”从 2/6 = 33.3% 改成 1/4 = 25%。在 t=0.3 时，D 的 33.3% 高于阈值，因此 empty traces 保留；D′ 的 25% 不超过阈值，因此被过滤，于是 X(tau,B) 变成 B。



---

## 7. 脱稿（10 分钟，决定 PASS）

合上所有东西：

- 四种切各一句话（在 DFG 上看什么）
sequence 有向边，严格从左到右
choice 二选一
parallel 两个都要走，顺序可以互换
loop 严格按照body redo 的顺序走的



- `noise_threshold` 按什么砍边，一句话
按照边出现的频次比例严格＞噪声才留下

- 为什么 Algorithm 1 过滤后的 D′ 会让这种砍法结果不同，一句话——要说到"次数"和"比例"

Algo不保留频次权重，只保留是否出现过


发我。通过 → LEDGER 加一行。密封 `_sealed/EX-02_answer.md` 有手切树、12 棵树的表、任务 12 的算式；做完再开。


## 7A. 核心题完成后的研究连接（不改变 PASS）


完成任务 1–12 和脱稿后，才打开[受控连接卡 C02](../_sealed/connections/C02.md)。卡中 `CONNECT` / `EXTEND` 不影响 PASS；逆序六树仍是 EXTEND。

这一站只挂[知识图的当前小视窗](../KNOWLEDGE_MAP.md#当前小视窗)、[研究地图的八步探索闭环](../RESEARCH_MAPS.md#八步探索闭环)和[能力证据图的 EX-02 行](../RESEARCHER_COMPETENCY_MAP.md#八站能力与证据映射)。观察的能力是 `abstraction`（抽象）：可检查产物是四节点微例分组、正式题手切树、投影表、运行前预测和逐 trace 核对；只贴 pm4py 输出只算见过结果。

消费者接口与源码阅读只填写 [System reading 空白行](../RESEARCH_NOTE_TEMPLATE.md#sr-blank-01)：从 `D / D′ -> to_df -> discover_dfg / discover_process_tree_inductive -> tree` 写清 data flow、调用前后状态、算法步骤到代码位置、消费者实际读取字段与 observed behavior。大量逐行注释不是证据；图与日志管线不一致时先记录 mismatch，未闭环前不直接叫 bug。

## 8. 这站不做的

- 不学 Petri 网转换（`discover_petri_net_inductive` 先别碰），不学 alignment / fitness 指标
- 不碰 Sepsis 或任何真实日志
- 不碰 `pilot.py`
- 跑出来的"D 与 D′ 在某个 t 分岔"**只是玩具上的现象**，不是第 7 站的实验结果；第 7 站要先写预测再在合成日志上做
