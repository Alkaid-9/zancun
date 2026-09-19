# EX-07 · 实验：pre-prediction → 合成日志 → IM / IMf on D vs D′ → verdict



**站**: 第 7 站（BRIEF A1 新增；OS §10 ③"小而完整的实验"的落点）
**前置**: T0 裁定 + T2′ 冻结（EX-06）；EX-05 的 `algo1` + `test_invariants.py`；EX-02 的 pm4py 跑法
**产出**: `EX-07/PREDICTION.md`（先写，冻结后不改）→ `EX-07/gen.py`（你的日志生成器）→ `EX-07/run.py` + `results/`（原始输出）→ `EX-07/VERDICT.md`
**PASS 条件**: 预测在跑之前落盘且有 falsifier；主对照是 D 本身；每个结果能回指到原始输出文件；verdict 三级裁定（成立 / 不成立 / 无法判定）之一，且写明 claim ceiling
**时间盒**: 由 T4′ 定；审稿人估 W2 一周（09-11→09-17），可降级项见 §6

这一站没有密封答案——实验的答案就是结果，谁也不该提前有。EX-02 那个玩具上的分岔（t=0.3 / 0.4）**不算**这一站的结果，它只是让你知道现象存在。

作答写别的文件。

---

## 1. 教学：一个实验最少要有的四样东西

1. **问题**：一句话，能被"是 / 否"回答。这一站的问题由 T0 定，审稿人版本作参考：

   > 用 Algorithm 1 过滤后的 D′ 喂给固定的下游算法（IM、IMf），输出跟直接喂 D 一样吗？如果不一样，差在哪、由什么决定？

2. **预测**：跑之前写下"我认为会怎样"，**并写下什么结果会让我承认自己错了**（falsifier）。没有 falsifier 的预测不是预测，是愿望。
3. **对照**：跟谁比。这里主对照是 **D 本身**——论文说 zero loss 是相对 D 说的，所以比的就是 D′ 和 D。"随机抽同样多条"只是次级控制，用来回答"是过滤造成的，还是单纯变少造成的"。
4. **裁定规则**：跑之前定好"什么算成立、什么算不成立、什么算判不了"。跑完不许改。

## 2. 任务 1 · PREDICTION.md（1h，写完不改）

按 EX-01 停靠点 / EX-02 任务 12 / EX-03 任务 3 / EX-05 表，你手里已经有足够的东西写出**实验前就能推出的预测**。至少写三条，每条带 falsifier：

```
P1（IM）：在任何 D 上，IM(D) 与 IM(D′) ______。
   依据：
   falsifier：出现一个 D 使两棵树不等价（用六条 trace 走一遍的办法判等价，不用字符串相等）
   如果被证伪，先怀疑：（提示：审稿人 §6 第 1 条——pm4py 的 IM 是纯 DFG 级还是会看日志属性）

P2（IMf）：存在阈值 t，使 IMf_t(D) ≠ IMf_t(D′)；分岔发生在 ______ 那种结构上，方向是 ______。
   依据：EX-02 任务 12 的比例算式
   falsifier：扫遍 t ∈ [0, 0.5] 所有 D 上两棵树都相同

P3（随机对照）：随机抽 |D′| 条得到的 D_r，IMf 分岔的阈值与 D′ 相比 ______。
   依据：
   falsifier：

P4（可选，噪声）：加入不造新边的扰动（EX-03 任务 2 那类）后，D′ ______。
```

写完把文件哈希记到 `VERDICT.md` 顶部（`sha256sum PREDICTION.md`），之后不改。要改就另起 `PREDICTION_v2.md` 并写明为什么。

> **量词提醒（保留上面的 P1 原题）**：P1 中的“在任何 D 上”是一个全称理论猜想，必须把输入范围、实现版本和参数前提写出来；一个满足前提的反例即可证伪。即使所有已列日志和 seed 都成功，也只能写“在已测范围内尚未被证伪”，不能写成对所有 D 的证明。

## 3. 任务 2 · 日志生成器（2–3h）

研究仓的 `build_universe` 每个只有 6 条 trace，太小。你按 OS §11 接管它的思路（拓扑 + 变体 + 裁判 + 扰动），自己写一个 `gen.py`：

- 输入：拓扑名、trace 条数 n（100–1000）、每种变体的比例、扰动比例、seed
- 输出：`(case_id, trace, label)` 列表 + 真流程（`ModelSpec` 那四样）
- 至少四种拓扑（沿用 chain / branch_merge / shortcut / loop），加一种**能让 IMf 的 `__filter_dfg_noise` 启用**的（EX-02 追问 3：找不到切的结构——比如两个活动互相跟随又各自能到终点）
- 变体比例要不均匀（比如 70/25/5）——比例均匀的话频次塌平没东西可塌
- 扰动分两类分开生成：造新边的 / 不造新边的（EX-03 任务 2）

自检：每种拓扑生成一份，先跑 `test_invariants.py` 的不变量断言，再打印 |D′| 与 EX-03 上界对照。

## 4. 任务 3 · 跑（1–2h）

对每份 D：
1. `algo1` 得 D′；随机抽 |D′| 条得 D_r（固定 seed，多抽几次取分布）
2. IM：三份各跑 `discover_process_tree_inductive(noise_threshold=0)`，判等价（用生成器的变体走树，或 pm4py 的 `fitness`——先查 API，走不通就用走 trace 的办法）
3. IMf：t = 0.0 到 0.5 每 0.05，三份各跑，记第一次分岔的 t 和分岔的活动
4. 每次跑的树字符串、t、|D′|、seed 全部写进 `results/*.json`，不手抄

## 5. 任务 4 · VERDICT.md（1h）

```
预测哈希：
结果表：拓扑 | n | |D′| | IM 等价? | IMf 首次分岔 t (D vs D′) | IMf 首次分岔 t (D vs D_r) | 分岔活动
P1 裁定：成立 / 不成立 / 无法判定 —— 依据 results/xxx.json
P2 裁定：
P3 裁定：
意外：跑之前没预测到的现象，逐条
claim ceiling：这些结果最多能说什么（例：「在合成日志上、pm4py 2.7.23.6 的 IMf 实现下」）、不能说什么（例：不能说 EdgeIM 的 Stage 3 会受影响——F2 UNKNOWN）
下一步如果只做一件事：
```

三级裁定（计划 v1.0 §6.6）：**成立** = 预测方向对且 falsifier 没触发；**不成立** = falsifier 触发；**无法判定** = 结果有但依赖某个没控制的变量（写出是哪个）。

## 6. 降级序（T4′ 判 NOT FEASIBLE 时按这个砍）

按审稿人 §5：Sepsis 加分项 → IMf 阈值扫描宽度（0.1 步长）→ 拓扑种类（砍到 2 种）→ 包装。**不砍**：PREDICTION 先于结果、D vs D′ 主对照、D+2 复测。

Sepsis（真实日志）是可选加分，走计划 v1.0 的"有限资料取得"门——下载前要你的口令；`teardown-joint/repro/EDGEIM_plan.md:87-93` 有链接和旧 MD5，v1.0 改 SHA-256 须重算。

## 6a. 观察层检查、语言等价与外部效度（CONNECT / EXTEND；不影响 PASS）

### 观察层与模型语言必须分开

trace replay 或给定日志上的 fitness，只是**观察层日志一致性检查**：它说明模型能否重放这批已观察 trace，不能单独证明两个模型的允许语言相同。模型语言等价要求覆盖两个模型**所有可生成的 trace**，或给出形式化等价判定；有限日志、有限 seed 和字符串相同都不足以替代该证明义务。precision 也只约束当前观察范围内的额外行为，不能自动外推到未测 trace。

### 外部效度 EXTEND（可选；不影响 PASS）

在 `VERDICT.md` 后另开一节，明确结果适用范围的五个维度：

| 维度 | 本轮实际范围 | 需要怎样收窄或扩展 |
|---|---|---|
| 拓扑 | ________ | 换一种拓扑会不会改变 cut/分岔 |
| 规模 | n、case 数、trace 长度 ________ | 增大或减小到何处仍可观察 |
| 噪声类型 | 造新边 / 不造新边 ________ | 未覆盖的扰动是什么 |
| 顺序 | 正序 / 逆序 / 随机 seed ________ | 改遍历顺序是否改变结果 |
| 实现版本 | pm4py 与本仓 commit/version ________ | 升级版本或换实现的风险 |

然后设计两个最小后续产物：

1. **最小反例**：只改变一个维度，给出会让当前 P1/P2/P3 预测失效的最小 D 或 trace，并写预先承诺的判定规则。
2. **后续实验**：固定其余维度，改变该维度并保存原始 JSON；写清结果若 A/B 分别怎样更新 claim ceiling。

这是一项可选研究延伸，不改变 PASS，也不把尚未运行的反例或实验写成观察事实。

### 系统阅读、异常闭环与 proof obligation

每个“疑似 bug”、异常分岔或 `无法判定` 都必须在 [Research Note 的 Evidence closure](../RESEARCH_NOTE_TEMPLATE.md#evidence-closure) 建 `EC-__`：列竞争解释、区分证据、最低成本检查、观察和 `OPEN / SUPPORTED / REFUTED / BLOCKED`。trace replay 成功本身不能关闭“语言等价”疑问。

在 [System reading](../RESEARCH_NOTE_TEMPLATE.md#system-reading) 至少记录一行：生成器/过滤器的 input-output、状态更新、算法步骤、精确代码锚点、实际观察与 mismatch；在 [Research hooks](../RESEARCH_NOTE_TEMPLATE.md#research-hooks) 写 proof obligation：**为允许主张“D′ 与 D 的下游输出在声明范围内相同”，必须以 ________ 证明/反驳 ________**，并标明它属于 `implementation`、`model` 或 `abstraction` 层。缺证据时保留 `UNKNOWN`。

完成核心题并留下自己的预测、原始输出和 verdict 后，才可[打开受控连接卡 C07](../_sealed/connections/C07.md)。卡内 `CONNECT` 与 `EXTEND` 均不影响本站冻结 PASS。本站只打开自然相关的 [Map 1：Knowledge](../KNOWLEDGE_MAP.md)、[Map 5：Researcher Competency](../RESEARCHER_COMPETENCY_MAP.md)、[Map 7：Research Trajectory](../RESEARCH_TRAJECTORY_MAP.md)，不要求一次填完七图。

## 7. 这站不做的

- 不在跑之前看任何已有结果（包括研究仓 `results/`、REUSE 表第 14 项 Sepsis 数字）
- 不把 D_r 写成主对照
- 不在 VERDICT 里写"EdgeIM 有问题"这类超出 ceiling 的句子
- 不因为结果漂亮就跳过 D+2：09-16 前后空白纸重讲实验设计（OS §5）


