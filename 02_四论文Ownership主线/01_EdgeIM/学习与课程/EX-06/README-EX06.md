# EX-06 · 规划：T0 裁定 → T2′ / T3′ / T4′

**站**: 第 6 站（BRIEF §2：由 v1.1 定；A1 后顺序里排在第 5 站之后、第 7 站之前）

**前置**: EX-01 的 G0 note 已落盘；EX-02、03、05 PASS

**产出**: `_scratch/seg0/T0_object_verdict.md`（你拍板，我只记录）；然后 v1.1 §3 的 T2′ / T3′ / T4′（主窗口起草，你批）

**PASS 条件**: 由 v1.1 判——T0 verdict 有"消费的 flag"栏且每条 flag 有处置；T2′ 五单位各有数学定义 + toy + 边界 + 代码字段 + 作废条件；T3′ 每节点标 CORE/ADJACENT；T4′ 从可用小时倒排到降级触发线

这一站没有密封答案。规划没有标准答案，只有"依据够不够"。

这一站也**不教新东西**——BRIEF §0 说了，规划本来是做得最好的部分，坏的是对象层。前面五站把对象层补上了，这里只是回到规划，把前面的产出接上去。

## 0. 零基础词汇与归属桥（先读；不影响 PASS）

本段先把 T0/T2′ 会用到的缩写和责任主体说清楚，再要求你裁定。微例与 EdgeIM 无关：一张配送表记录 `仓库 -> 卡车 -> 客户`，另一个程序按总里程选择路线。


| 词 | 白话定义 | 配送微例 | 在本站的用法 |
|---|---|---|---|
| DFG（directly-follows graph，直接跟随图） | 把活动当节点、相邻活动当有向边的图；边可带出现次数 | `仓库→卡车`、`卡车→客户` 是两条边 | 记录 Stage 2/3 交接的对象，不自动等于完整日志 |
| IM（Inductive Miner，归纳式过程发现算法） | 按结构切分输入并递归构造过程模型的一类算法 | 按路线段落分组再递归组合 | EX-07 的固定下游消费者之一 |
| IMf（Inductive Miner-infrequent，带低频过滤的 IM 变体） | 在发现前按阈值处理低频行为的 IM 变体 | 忽略只出现一次的临时绕路 | 需要单独写阈值和分岔，不能与 IM 混称 |
| GT（ground truth，真值/真流程） | 由生成规则或独立规范给出的参照对象；不是“程序跑出的答案” | 预先规定的允许路线集合 | 只在来源和构造规则写清时使用，未知就写 `UNKNOWN` |
| surrogate（代理指标） | 间接反映目标的可观测量，不等于目标本身 | 用里程代理油耗，但没有油耗计 | 不能用运行时间代理通信、隐私或质量 |
| claim ceiling（主张上限） | 当前证据最多允许写到的范围、条件和强度 | 20 次配送只支持这 20 次的时长比较 | 每个 T0/T2′ 对象都必须写，不能把架构推论写成测量事实 |


四类责任主体分开记账：

1. **论文作者**：对论文正文、算法、表格中明确写出的主张负责；引用 `PAPER-TEXT` 只证明“作者这样写”。
2. **现有研究仓**：对仓库代码、测试和运行输出的可复查事实负责；仓库不是论文作者，也不是独立真值来源。
3. **AI/工具**：只能提供导航、摘要、脚手架或 API 协助；其解释属于 `AGENT-SUMMARY`，必须回到原文/代码核验。
4. **学习者**：对自己的预测、数学定义、运行、推理和裁定负责；没有自己可定位产物时不能把“看过”写成能力证据。

**亲手动作**：任选 T2′ 的一个对象，分别写“对象是什么、四类主体各自能提供哪一种证据、尚缺什么”；再写一句为什么 `GT` 或 surrogate 不能直接填进 claim。此动作只建立归属边界，不改变 PASS。



---

## 1. T0 · 研究对象裁定（你做，30–60 分钟）

v1.1 §2 列了四个选项。你在 09-03 口头同意过审稿人的"B 为地板、C 为唯一研究问题"，但正式裁定要等 G0 note——现在有了。


按这个模板写 `T0_object_verdict.md`：

```
裁定：A / B / C / D（可以组合，写清楚）
一句话表述研究对象：
  （审稿人的版本作参考，不照抄：「EdgeIM feature-preserving filter 的有边界复现：
   证明它保什么（边集），量它扭什么（频次），测这是否改变固定下游 IM/IMf 的输出」）



依据（每条指到你自己的产出，不指到 AI 的文件）：
  - G0 note 第 3 问答案 + 页码 →
  - EX-02 任务 12 的算式 →
  - EX-03 任务 3 上界 / 任务 2 "看不见的非法" →
  - EX-05 不变量表 →



消费的 flag（v1.1 A1 第 1 条：这一栏必填）：
  上游文档里每一个"未验证 / 待确认 / 不授权 / UNKNOWN"，逐条写怎么处理。至少要过一遍：
  - 你 G0 note 里所有 UNKNOWN
  - 独立审稿 §0 F2（Stage 3 是否用权重）、§0 末尾的并发边疑点、§6 三件不确定
  - v1.1 §9 B3 primary 必换
  - A4 课表未补
  每条三选一：已解决（写依据）/ 带进 T2′ 作边界 / 不影响本对象、搁置



不选其他选项的理由：各一句

claim ceiling（这项研究最多能说什么、不能说什么）：
  例：只能说「feature-preserving 过滤与频次型噪声过滤的兼容性」，
  不能说「EdgeIM 有缺陷」——EdgeIM 自己的 Stage 3 用不用频次是 UNKNOWN（F2）
```



写完发我。我只做一件事：核对每条依据是否真的指到你的产出、每个 flag 是否都有处置。**不替你裁。**



## 2. T2′ · Measurement Contract（主窗口起草，你批，2h）

T0 定了之后才开始。从零写，不从 `_withdrawn/T2` 改（v1.1 §3）。

五个单位大多已经被算法钉死，写起来比第一轮短得多：


| 单位 | 现在的答案来源 |
|---|---|
| 采样/过滤单位 | trace（Algorithm 1 逐 case） |
| 预算 | 无，内生（EX-03 上界） |
| 主对照 | **D 本身**（v1.1 A1 第 4 条；原文 zero loss 就是相对 D） |
| 次级对照 | 随机等量抽 \|D′\| 条（只作控制，不作主张） |
| 指标 | 第 7 站定：IM 树是否恒等；IMf 在哪些阈值分岔；分岔的活动 |


每个单位五栏：数学定义 / toy（≤10 条 trace，可直接用 EX-00 或论文十条）/ 边界 / 代码字段（对应你 EX-05 的变量名）/ 作废条件。


## 3. T3′ · CORE / ADJACENT（1h）

`_withdrawn/T3` 的 §1 决策规则和 §4 ADJACENT 表可以搬。节点清单按 T0 重列：Algorithm 1、DFG、IM 四种切、IMf 阈值规则各标 CORE；Petri 网、alignment、Stage 2 边缘节点合并、sigRank / CrossEdgeIM / Sommers 标 ADJACENT，各附一句理由。


## 4. T4′ · 时间倒排（1h）

沿用 `T4_reverse_schedule.md` 的容量模型和 T4-A~D 四门。改三处：
- 分项工时按 T0 重排（第 7 站为主）
- 修"14 天 vs 17 天"自相矛盾
- §5 的 random-vs-coverage "不可降级"改为 D-vs-D′ 不可降级，随机等量可降级（A1 第 4 条）


09-20 core freeze、09-25 打包不动（C-069 草稿）。A4 课表还没补——补了才能倒排，这是这一站唯一的外部输入。


完成核心 T0/T2′ 并留下自己的产物后，才可[打开受控连接卡 C06](../_sealed/connections/C06.md)。卡内 `CONNECT` 与 `EXTEND` 都不影响本站冻结 PASS。


## 5. 记账

- T0 verdict 落盘后，C-069 草稿（`_scratch/2026-09-03__C-069-draft__scratch.md`）里的"(c) T0 四选项待第 1 站后裁"可以关；C-069 本身仍等你说"C-069 写"
- 这一站不进 LEDGER 的"铸/磨卡"，它不是能力训练；但 T0 verdict 是 hard output（OS §17），日志记一行 `T0 verdict 落盘`

## 6. Claim–evidence 交叉题（CONNECT；不影响 PASS）

完成核心 T0/T2′ 后，回看 [PAPER_MAP 的 Claim–evidence 工作表](../PAPER_MAP.md#6-claim-evidence-工作表)，对四个对象各填一行。这里只给列，不代填结论：

| 对象 | claim（主张） | direct measure（直接测量） | indirect support / surrogate（间接支持/代理） | missing evidence（缺口） | ceiling（上限） |
|---|---|---|---|---|---|
| 质量 | ________ | ________ | ________ | ________ | ________ |
| 时间 | ________ | ________ | ________ | ________ | ________ |
| 通信 | ________ | ________ | ________ | ________ | ________ |
| 隐私 | ________ | ________ | ________ | ________ | ________ |

质量的候选来源是 Table II（印刷 p.409）的 fitness、precision、F-measure；时间的候选来源是 Table III（印刷 p.410）的时间列。通信和隐私请逐项查 §V 与 Tables I–III；找不到直接量就写 `NONE`，不得用时间、过滤条数或架构图代填。每一行都要标明来源是 `PAPER-TEXT`、`CODE-EVIDENCE`、`USER-INFERENCE`、`AGENT-SUMMARY` 或 `UNKNOWN`，并区分论文作者、研究仓、AI、学习者的 credit。

**八步探索闭环（仅 CONNECT）**：`Observe` 记录表格或代码中实际看到的字段；`Analogize` 可提出配送等类比；`Abstract` 写成“目标量—观测量—接口”；`Hypothesize` 写一条可证伪的 claim；`Attack` 给出最小反例或混淆代理；`Experiment` 设计只改一个因素的检查；`Verify` 回指原始记录；`Update` 根据结果收窄或改写 ceiling。大胆 analogy 可以保留，但 hypothesis 之后必须有可检查文字；全程不改变 PASS。

## 7. 系统阅读与证明义务（CONNECT/EXTEND；不影响 PASS）

对 T2′ 的每个对象各留一条最小记录：在 [Research Note 的 System reading](../RESEARCH_NOTE_TEMPLATE.md#system-reading) 写 `input/output → data flow → state before/update/after → algorithm step → exact code anchor → observed behavior`；在 [Evidence audit](../RESEARCH_NOTE_TEMPLATE.md#evidence-audit) 标出直接来源与验证动作；若有“这个指标是否真测到目标”的疑问，在 [Evidence closure](../RESEARCH_NOTE_TEMPLATE.md#evidence-closure) 保持 `OPEN / UNKNOWN` 直到出现区分证据。

再在 [Research hooks](../RESEARCH_NOTE_TEMPLATE.md#research-hooks) 写 proof obligation，并给每条标层次：

> 为允许主张“该对象的测量足以支撑 ________”，必须以 ________ 证明/反驳 ________；层次：`implementation` / `model` / `abstraction`。

例如，检查 Table III 是否真的记录通信字节数属于 `implementation`/measurement contract；把 DFG 摘要推广到下游模型性质属于 `abstraction`。这些只是待检义务，不是预填裁定。

本站只打开与当前决定自然相关的地图：[Map 1：Knowledge](../KNOWLEDGE_MAP.md)、[Map 5：Researcher Competency](../RESEARCHER_COMPETENCY_MAP.md)、[Map 7：Research Trajectory](../RESEARCH_TRAJECTORY_MAP.md)；不要求一次填完七张地图。
