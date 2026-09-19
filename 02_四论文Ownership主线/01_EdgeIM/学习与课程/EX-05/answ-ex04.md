
representation: 整数列表[2, 1, 2]
fixture:固定的测试材料，固定顺序和输入参数等属性
seed：随机种子，结果可复现
oeacle:独立裁判，只负责一个法则的确认
invariant: 不变量，在声明的输入变化范围内，理论上应该保持不变的性质
traceback: 只定义一次失败路径，定位出错位置


————————————————————————————
【再写一句：若 10 个 seed 都通过，当前证据仍不能覆盖哪些输入】

如果 10 个 seed 都过了，你能说什么、不能说什么：

能说：这 10 个特定的 universe（4 种拓扑 × 10 个 seed）上，不管 6 条 trace 怎么顺序排，Algorithm 1 都保持 (S,E,R)。

不能说：
- 其他任意日志上是否也保持（你只测了玩具日志）
- 真实日志（随机活动、任意噪声分布）会怎样
- 更大的日志（|D|>6）保不保持
- 真正的 random.shuffle() 打乱后会不会 pass（只测了两种固定顺序）

这就是为什么 README §7 最后说"10 个 6 条 trace 的玩具，只够证伪，不够立论"。
————————————————————————————————————————



【**产出**: `EX-05/test_invariants.py`（你写）+ 运行输出；`EX-05/takeover.md`（你写，OS §11 八条的作答）
**PASS 条件**（冻结，A1 改后）: 自写实现在 D 与 D′ 上断言 S/E/R 相等（10 个 universe，两种顺序）；对 `build_universe` / `classify_trace` 各答出 representation、改一个条件的影响；`1.000` 塌不塌只作 30 min 附录，能预测并说出理由
】


————————————————————————————————————————————————

**不变量**指"不管输入怎么变，某个性质永远成立"。Algorithm 1 的核心承诺（论文叫 zero loss）翻成不变量就是：

> 对任何日志 D，任何 case 顺序，`(S, E, R)(D′) == (S, E, R)(D)`。

其中右边的 (S,E,R)(D) 是**直接在全日志上算**的三个集合——不经过过滤，把每条 trace 的特征全并起来。左边是过滤后剩下的 D′ 算出来的。

——————————————————————

IM 那边：
sequence / choice / parallel / loop
= “我怎么切这个过程模型”

pilot 那边：
chain / branch_merge / shortcut / loop
= “测试数据背后的流程长什么样”

不是同一个抽象层。






[(i, c.trace) for i, c in enumerate(U.candidates)]

oracle_map = {c.trace: c.oracle_lable for c in U.candidates}

===============================

重开：
**任务 1**：写 `full_features(log)`：不过滤，把每条 trace 的 Si、Ei、Ri 全并起来，返回 (S,E,R)。三行。


**任务 2**：写 `test_invariants.py`。对 seed 0–9 每个 universe：

- 取 6 条 trace，按 `candidate_index` 顺序作为正序，倒过来作为逆序
- 正序、逆序各跑一次你的 `algo1`
- 断言：正序 D′ 的 (S,E,R) == `full_features` 的 (S,E,R)；逆序同样
- 记录：|D′| 正序、|D′| 逆序、正序 D′ 里 `ILLEGAL` 的条数

打印一张 10 行的表：`seed | 拓扑 | |D′|正 | |D′|逆 | 正序 D′ 里非法条数 / |D′| | 不变量`。



————————————————————————————
笔记：
对，这下 representation 就从“我们实际用过的几个字段”扩成了完整结构。

你不需要现在把所有字段死记下来，先按“它在实验里承担什么角色”分组会更好。

`Candidate` 大致可以这样读：

```text
Candidate
│
├─ 身份 / 来源
│  ├─ candidate_index
│  ├─ source_case_id
│  └─ derived_trace_id
│
├─ 修改前后
│  ├─ clean_trace
│  └─ trace
│
├─ 合法性 / 污染状态
│  ├─ noise_contaminated
│  └─ oracle_label
│
├─ 做了什么扰动
│  ├─ operation_id
│  ├─ affected_event_positions
│  ├─ variant_id
│  ├─ injected_noise_event
│  ├─ perturbation_type
│  └─ perturbation_label
│
└─ 扰动对结构造成了什么
   └─ induced_edges
```

所以 README 特别让你找的两个现在已经非常明确：

```python
candidate.oracle_label
```

是**裁判标签**；

```python
candidate.induced_edges
```

是**这次扰动诱导出来的边**，也就是类似：

```text
(('a', 'x'), ('x', 'b'))
```

这种“因为插入/修改而新造出来的直接跟随关系”。

而 `Universe` 是更上一层的容器：

```text
Universe
├─ universe_seed
├─ topology
├─ model
├─ candidates
├─ seed_map
├─ target_source_case_ids
└─ clean_dfg_edges
```

你刚才闭卷记得：

```text
topology
candidates
```

现在开卷以后补出来了另外 5 个。

这里有一组特别值得现在接通：

```text
clean_trace       ← 单条 candidate 被污染前是什么
trace             ← 污染/扰动后真正送进实验的是什么

clean_dfg_edges   ← 整个 clean model 原本有哪些边
induced_edges     ← 当前 candidate 的扰动额外诱导出了哪些边
```

这其实和你刚刚看到“非法 trace 为什么容易被 Algorithm 1 留下”直接连上了。

比如原来：

```text
clean_trace = ('a','b','d')
```

如果扰动后：

```text
trace = ('a','x','b','d')
```

那么可能有：

```text
induced_edges = (
    ('a','x'),
    ('x','b')
)
```

而这些边不在 `clean_dfg_edges` 里。

于是 Algorithm 1 一看：

> 哎，新 `R`。

它不知道这是“非法噪声造成的新边”，只知道这是此前没见过的 feature，所以可能把它留下。

这就把刚才我们的实验观察和生成器 representation 接起来了：

```text
perturbation
    ↓
induced_edges
    ↓
新的 R feature
    ↓
Algorithm 1 判为 novel
    ↓
ILLEGAL trace 可能被留下
```
————————————————————————————————————





