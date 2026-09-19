# EX-05 · 不变量测试；接管生成器层；`1.000` 附录

## 0. 零基础词汇桥：先知道测试在检查什么

没有这些词，会把“测试输入是什么”“谁给正确答案”“随机性怎样复跑”和“什么性质应保持”混成一件事。先用一个与正式实验无关的三张号码卡微例：输入 `x = [2, 1, 2]`，小程序按给定随机起点打乱三张卡，再检查号码的多重集合仍是 `{1, 2, 2}`。


| 词 | 白话定义 | 三张卡微例 | 本站位置 |
|---|---|---|---|
| representation（表示） | 对象在内存里用什么结构和字段装着；换表示不应偷偷换研究对象 | 三张卡表示为整数列表 `[2, 1, 2]` | 解释 `Universe`、`Candidate`、trace 和标签各放在哪里 |
| fixture（固定测试材料） | 每次测试开始前准备好的输入、对象和环境 | 固定三张卡及其初始列表 | 固定一个 universe、顺序和参数，避免每轮暗中换输入 |
| seed（随机种子） | 随机过程的初始值；同一实现、参数和 seed 应能复现同一随机选择 | seed `7` 决定这次怎样打乱三张卡 | 生成 universe 或随机打乱时记录 seed |
| oracle（外部裁判） | 独立于待测程序、用来判定期望结果或合法性的规则 | 裁判只检查打乱前后号码及次数是否相同 | `oracle_label` 和 `classify_trace` 提供合法性判定，不能与 Algorithm 1 的选择规则混写 |
| invariant（不变量） | 在声明的输入变化范围内，理论上应保持不变的性质 | 无论怎样打乱，三张卡的号码及各自次数不变 | 比较过滤前后以及不同 case 顺序下的 `(S, E, R)` |
| traceback（报错调用链） | 程序失败时列出的调用路径、文件和行号，用来定位错误发生在哪里 | 若程序收到缺失的一张卡后报错，traceback 指向读取卡片的位置 | 改生成器条件后若报错，记录最先暴露假设的代码位置和原因 |

形式化地，fixture 给出输入 `x`，seed 固定随机选择，程序得到输出 `T_seed(x)`；oracle 判断输出是否合格；invariant 是要求某个性质 `P(T_seed(x))` 在声明范围内保持为真。traceback 只定位一次失败路径，不自动解释根因。

**亲手动作**：在纸上写出三张卡例子的 representation、fixture、seed、oracle 和 invariant；再写一句：若 10 个 seed 都通过，当前证据仍不能覆盖哪些输入。这个动作只检查词义，不影响本站 PASS。

**站**: 第 5 站（BRIEF §2 + A1，4–6h）
**前置**: EX-05a 的 `algo1.py` 过了三条断言；EX-03 的上界推导
**产出**: `EX-05/test_invariants.py`（你写）+ 运行输出；`EX-05/takeover.md`（你写，OS §11 八条的作答）
**PASS 条件**（冻结，A1 改后）: 自写实现在 D 与 D′ 上断言 S/E/R 相等（10 个 universe，两种顺序）；对 `build_universe` / `classify_trace` 各答出 representation、改一个条件的影响；`1.000` 塌不塌只作 30 min 附录，能预测并说出理由

这一站第一次碰研究仓 `research/edgeim_sampling_audit/`。那里的数字全部不可引（`STATUS.md`）；代码可以读、可以跑，但你要把它当成"别人写的、有一处根本错误的代码"来读——错在把 Algorithm 1 当成了 fixed-K 采样器（`src/pilot.py:335` `sample_coverage`）。你的任务不是修它，是**在它旁边放一份对的**，然后接管它的生成器层。

作答写别的文件。

---

## 1. 教学：什么叫不变量测试

EX-05a 的第三条断言是"正序和逆序跑完，(S,E,R) 相同"。这只是一个日志、两种顺序。

**不变量**指"不管输入怎么变，某个性质永远成立"。Algorithm 1 的核心承诺（论文叫 zero loss）翻成不变量就是：

> 对任何日志 D，任何 case 顺序，`(S, E, R)(D′) == (S, E, R)(D)`。

其中右边的 (S,E,R)(D) 是**直接在全日志上算**的三个集合——不经过过滤，把每条 trace 的特征全并起来。左边是过滤后剩下的 D′ 算出来的。

测试的写法：造很多不同的 D，每个 D 跑几种顺序，每次都断言这条等式。任何一次失败，要么你的实现错了，要么这条承诺本身不成立——两种都是发现。

跟 EX-05a 的区别：那里只比"正序 vs 逆序"，这里比"过滤后 vs 不过滤"，而且要跨很多日志。

## 2. 日志从哪来：研究仓的生成器

`research/edgeim_sampling_audit/src/pilot.py` 里有一个 `build_universe(seed)`，给一个整数，吐出一个 6 条 trace 的小日志（叫 universe），其中 3 条合法、3 条被插入了一个非法事件，每条都带 oracle 标签（`LEGAL` / `ILLEGAL`）。seed 0–9 共 10 个，四种拓扑轮换（chain / branch_merge / shortcut / loop）。

这就是第 3 站说的"合成日志 + 裁判"。生成器层本身没错（错的是采样器层），所以可以用；但按 OS §11，用之前你要先接管它——第 4 部分。

读入方式（API 层，直接用）：

```python

import sys
sys.path.insert(0, "/mnt/d/MyResearch/MAS_Safety_Project/research/edgeim_sampling_audit/src")
import pilot

U = pilot.build_universe(0)
for c in U.candidates:
    print(c.candidate_index, c.trace, c.oracle_label)
```

`c.trace` 是活动元组，`c.candidate_index` 是它在 universe 里的位置（0–5），`c.oracle_label` 是裁判标签。

## 3. 任务 A · 不变量测试（约 2h）

**任务 1**：写 `full_features(log)`：不过滤，把每条 trace 的 Si、Ei、Ri 全并起来，返回 (S,E,R)。三行。


**任务 2**：写 `test_invariants.py`。对 seed 0–9 每个 universe：

- 取 6 条 trace，按 `candidate_index` 顺序作为正序，倒过来作为逆序
- 正序、逆序各跑一次你的 `algo1`
- 断言：正序 D′ 的 (S,E,R) == `full_features` 的 (S,E,R)；逆序同样
- 记录：|D′| 正序、|D′| 逆序、正序 D′ 里 `ILLEGAL` 的条数

打印一张 10 行的表：`seed | 拓扑 | |D′|正 | |D′|逆 | 正序 D′ 里非法条数 / |D′| | 不变量`。




**任务 3 · 先预测再跑**：跑之前写下三条预测，写进 `test_invariants.py` 顶部注释：

- (p1) 10 个 universe 的不变量全过吗？

全过

- (p2) |D′| 会落在什么范围？（用 EX-03 的上界想：这些 universe 活动只有 3–4 个）


- (p3) 正序 D′ 里非法 trace 的占比，比全日志的 3/6 高还是低？为什么？（EX-03 追问 1 的思路）



跑完逐条打 ✓ / ✗，错的写一句为什么。

**任务 4**：再加一种顺序——随机打乱（固定 `random.seed(0)`），不变量还过吗？|D′| 变不变？



===============
D′₁ ≠ D′₂ ≠ D′₃

但

φ(D′₁) = φ(D′₂) = φ(D′₃) = φ(D)

其中 φ(D) = (S,E,R)
====================

## 4. 任务 B · 接管生成器层（约 2h，`takeover.md`）

OS §11 说：用了别人的代码，要能答出这八条才算你的。这一站只要求其中三条，对两个函数各答一次。

对 `pilot.build_universe`（`src/pilot.py:175-298`）：

1. **Representation**：一个 universe 在内存里是什么？（不看代码，先凭读过的印象写；再翻代码对，把差的地方记下来）——`Universe` 有哪几个字段？`Candidate` 有哪几个？哪个字段是裁判标签，哪个字段记录"插入造出了哪些新边"？
——————————————————————————
@dataclass(frozen=True)
class Universe:
    universe_seed: int
    topology: str
    model: ModelSpec
    candidates: tuple[Candidate, ...]
    seed_map: Mapping[str, int]
    target_source_case_ids: tuple[str, ...]
    clean_dfg_edges: tuple[tuple[str, str], ...]



@dataclass(frozen=True)
class Candidate:
    candidate_index: int
    source_case_id: str
    clean_trace: tuple[str, ...]
    trace: tuple[str, ...]
    derived_trace_id: str
    noise_contaminated: bool
    oracle_label: str
    operation_id: str | None
    affected_event_positions: tuple[int, ...]
    variant_id: str = "variant-0"
    injected_noise_event: bool = False
    perturbation_type: str = "none"
    perturbation_label: str | None = None
    induced_edges: tuple[tuple[str, str], ...] = ()
——————————————————————————————





2. **改一个条件**：把 `_CONTAMINATED_COUNT` 从 3 改成 1（`src/pilot.py:23`）。**先预测**：10 个 universe 的 |D′| 会怎么变？正序 D′ 里非法占比怎么变？然后真改、真跑、对预测。跑出来什么就记什么——**如果有 universe 报错，报错也是结果**：读 traceback，找到是哪一行、为什么，写一句"这个生成器隐含假设了什么"。
再改成 2 跑一次。**改完改回去**——那个仓是取证用的，不能留改动。（用 `git -C research/edgeim_sampling_audit diff` 确认干净。）






3. **来源披露**：这份生成器是谁写的、什么时候、错在哪一层、哪一层没错。一段话，写到 `takeover.md` 顶部。

对 `pilot.classify_trace`（`src/pilot.py:151-162`）：

1. **Representation**："真正的流程"在这个函数眼里是什么？（提示：`ModelSpec` 的哪几个字段被读了）它判"合法"的条件有几条？


2. **改一个条件**：把第 162 行的"每条相邻对都在 transitions 里"去掉，只保留起点、终点、字母表三条。**先预测**：universe 0–9 里有哪些原本 `ILLEGAL` 的 trace 会变成 `LEGAL`？（EX-03 任务 2 的"看不见的非法"在这里会现形。）然后跑、对、改回去。


3. 一句话：这个裁判和 Algorithm 1 的判据，看的东西有多少重合？



## 5. 任务 C · `1.000` 附录（30 分钟，只做这么多）

`results/REVALIDATION_COMPARISON.md:21` 里那个 `1.000`，是 fixed-K 替代品在 K=2 时选出的 2 条里非法占比 = 100%。它审的是死数字。你只回答：

- 用真 Algorithm 1（没有 K），"K=2"这个格子还存在吗？
- 你任务 2 表里 |D′| = 2 的 universe，非法占比是多少？|D′| > 2 的呢？
- 一句话：`1.000` 塌不塌，为什么这个问题本身问错了

## 6. 脱稿（10 分钟，决定 PASS）

合上一切：

- 不变量是什么，一句话；它跟论文 "zero loss" 的关系，一句话
- `build_universe` 吐出来的东西的 representation，一句话
- 把 `_CONTAMINATED_COUNT` 改成 1 之后 |D′| 怎么变，一句话（凭记忆）

发我。通过 → LEDGER 加一行。密封 `_sealed/EX-05_answer.md` 有 10 行表和两处改条件的真实结果，做完再开。

## 6a. A4 增量 · 四类证据与系统阅读

先分清四类证据：**定理/证明**是在写明前提后，对整个量词范围作演绎推导；**反例**是满足前提却违反结论的一个实例，可证伪全称命题；**有限测试**只运行列出的有限输入；**实现验证**检查固定版本的代码是否符合给定规格，不能替规格本身证明正确。

**CONNECT（不影响 PASS）**：完成上面的核心题后，从本站挑四项证据，填写下表。每格必须写证据对象与最远可说到哪里；没有某类证据就写 `NONE`，不得把全绿改写成“证明了所有输入”。

| 证据项 | 类型：定理 / 反例 / 有限测试 / 实现验证 | 它直接检查什么 | 当前证据上限 | 不能据此声称什么 |
|---|---|---|---|---|
| `(S,E,R)(D') == (S,E,R)(D)` 的运行结果 | ________ | ________ | ________ | ________ |
| 正序、逆序与固定 seed 打乱 | ________ | ________ | ________ | ________ |
| `build_universe` 改条件后的结果或报错 | ________ | ________ | ________ | ________ |
| `classify_trace` 改判据后的结果 | ________ | ________ | ________ | ________ |

系统阅读只做一个最小映射：在 [Research Note 的 System reading](../RESEARCH_NOTE_TEMPLATE.md#system-reading) 填一行，把一个函数的 `input/output -> data flow -> state before/update/after -> algorithm step -> exact code anchor -> observed behavior/mismatch -> claim ceiling` 连起来。可检查产物是一个 `SR-__` 行锚点和对应的运行输出；源码注释行数、阅读时长或“跑通过一次”都不衡量理解。

本站只打开三张自然相关的地图，不预判学习者等级：[Map 1：Knowledge](../KNOWLEDGE_MAP.md) 用来定位不变量连接的输入/状态/输出，[Map 5：Researcher Competency](../RESEARCHER_COMPETENCY_MAP.md) 用 `test_invariants.py`、预测对照和 `takeover.md` 观察 rigor（严谨）与 ownership（独立接管），[Map 7：Research Trajectory](../RESEARCH_TRAJECTORY_MAP.md) 只在后续同类任务出现时记录 feedback（反馈）后的变化。

核心题完成并留下自己的答案后，才可[打开受控连接卡 C05](../_sealed/connections/C05.md)。卡内 `CONNECT` 与 `EXTEND` 都不改变本站冻结 PASS。

### 6b. 最小 evidence closure 与 proof obligation（不影响 PASS）

如果改条件后出现异常、报错或“似乎违反不变量”，不要直接写成 bug。按 [Research Note 的 Evidence closure](../RESEARCH_NOTE_TEMPLATE.md#evidence-closure) 建一行 `EC-__`：写目标解释、竞争解释、能区分它们的证据、最低成本检查、预先承诺的裁定规则、观察和 `OPEN / SUPPORTED / REFUTED / BLOCKED` 状态。没有足够证据时保留 `OPEN` 或 `UNKNOWN`，并记录 traceback 只是定位路径，不是根因证明。

再在 [Research Note 的 Research hooks](../RESEARCH_NOTE_TEMPLATE.md#research-hooks) 建一行 `RH-__`，至少写一个 proof obligation（证明义务）：**为允许主张“在声明的输入范围内过滤保持 `(S,E,R)`”，必须以 ________ 证明/反驳 ________**。把义务标成 `implementation`（固定代码和运行行为）、`model`（算法性质）或 `abstraction`（从完整日志到摘要的映射）中最直接的一层；不要把一次有限运行升级成定理。此记录是 CONNECT/EXTEND 产物，不改变核心 PASS。

## 7. 这站不做的

- 不修 `sample_coverage`，不给它加 Algorithm 1 模式，不往研究仓里提交任何文件
- 不重跑 `clean_pilot.py` / `recompute_pilot.py`，它们测的对象已作废
- 不把任务 2 的非法占比当成研究结论——10 个 6 条 trace 的玩具，只够证伪，不够立论。第 7 站才做实验
