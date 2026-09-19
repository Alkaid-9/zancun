# 四论文全文 Ownership v3：Sol 施工合同

**任务**：`TASK-20260913-001`  
**日期**：2026-09-13（任务号由中央 allocator 签发；当前会话当地日期仍为 2026-09-12）  
**状态**：`DESIGN-v3 / READY-FOR-SOL-HANDOFF / NO-CANONICAL-WRITES`  
**作用**：把四篇论文全文 ownership 的课程资产建设、学习执行和能力验收拆开，给 Sol 一份可施工、可复核、不会替用户学习的合同。  
**前版**：[Fable 四论文扩容设计](2026-09-12__research__four-paper-full-ownership-design-for-sol.md)保留为历史输入；本稿不覆盖它。Sol 接单时以本稿为施工入口，前版只用于追溯缺口来源。  
**用户当前安排**：用户继续按原路线补前半程联动并推进 EX-05/EX-06；课程建设可以并行，用户只在满足解锁条件后进入新教学资产。

---

## 0. 本次裁定

旧设计的方向正确：EdgeIM 的 Stage 2、Stage 3、evaluation、related work 和全文压力测试需要补，另外三篇也不能停在浅层镜头。

但旧设计不能直接施工，原因不是“还少几道题”，而是它混合了三件不同的事：

1. Sol 是否已经把课程资产建好；
2. 用户是否已经完成一次当前学习任务；
3. 用户是否在陌生题和延迟复测中证明能力仍然存在。

v3 的最小原则如下：

- **课程可以先建，学习按依赖解锁**。未做完整十五题不阻止 Sol 建题面、rubric、fixture 和密封材料。
- **施工完成不改变用户能力状态**。Sol 的 `QA-PASS` 不能推出用户的 `PASS / RETAINED / OWNED`。
- **全文必须有全文覆盖表**。不能用几个选定章节、一份 2500 字文档或 teardown 复述代替整篇。
- **primary source 是事实权威**。teardown 是导航和核对辅助，不是用户 ownership 证据。
- **训练必须经历独立作答、反馈后重做、未见变体和延迟冷测**。
- **四篇形成一个回路**。三篇镜头必须消费 EdgeIM 产物并回写比较、评测或谱系判断，不能成为三座孤立课程。

---

## 1. 当前学习位置与前半程恢复线

### 1.1 当前位置

- 用户当前正在 `learning/training/lu-edgeim-algo1/EX-05/README-EX04.md`。
- 文件名中的 `README-EX04` 是历史命名，正文第 1 行和第 21 行均将它定义为 **EX-05 / 第 5 站**；后续一律按语义站点和冻结顺序识别，不用文件名猜站号。
- 冻结路线仍是 `EX-00 -> EX-01 -> EX-05a -> EX-02 -> EX-03 -> EX-05 -> EX-06 -> EX-07`。
- 用户计划先补漏，再继续 EX-05，并争取当日推进到 EX-06。这是学习执行线，不是 Sol 的课程建设线。

### 1.2 已核实的漏项

| 漏项 | 当前磁盘证据 | 性质 | 负责人 | 对 Sol 线的影响 |
|---|---|---|---|---|
| EX-01 `G0_user_paper_note.md` | 仓内未找到；EX-01 README §5 明确要求五问少一问不算过 | 原核心 PASS 的必补证据 | 用户 | 不阻止建设；未验收前不把 EX-01 写成正式 PASS |
| C00/C01/C05a/C02 CONNECT | 公共索引和密封卡存在；既有用户作答文件中未见提交记录 | 站后联动，不改变原 PASS | 用户 | 不阻止建设；集中补交即可 |
| sigRank L-S1 | `FOUR_PAPER_TRAINING_LOOP.md` 有题面要求，未见一页对照产物 | EX-01 PASS 后的第一横向镜头 | 用户 | Sol 可先建后续全文包；用户解锁仍看实际 PASS |
| EX-02 System Reading | 模板只有空白 `SR-__` 行；既有作答未见已填记录 | 系统阅读证据 | 用户 | 作为旧证据迁移缺口，不阻止建设 |
| EX-03 Evidence Closure | 模板只有空白 `EC-__` 行；既有作答未见已填记录 | 对“论文计数似乎有误”的证据闭环 | 用户 | 作为旧证据迁移缺口，不阻止建设 |
| 每站全文回接句 | `MASTERY_GATE.md` 有统一要求；既有作答未见集中记录 | 横向线程记录 | 用户 | 后续模块强制预留字段；旧站只补最小句，不重写答案 |
| EdgeIM Ledger / 冷复测 | `learning/training/LEDGER.md` 实际存在，但未见当前 EdgeIM 正式 PASS 行 | 能力证据闭环 | 用户 + 验收者 | 禁止倒填；复核通过后追加 |

### 1.3 用户恢复包

用户当前恢复包固定为：

1. 亲自完成 EX-01 G0 五问 note；
2. 集中补 C00、C01、C05a、C02 的 CONNECT；
3. 补一张 L-S1 对照；
4. 在统一 Research Note 中各补一条 EX-02 `SR-__` 和 EX-03 `EC-__`；
5. 每个已学站补一句“它怎样改变我对整篇 EdgeIM 的理解”；
6. 后续按冻结 rubric 复核，只有真实 PASS/冷测结果才能进入 Ledger。

这条恢复线不要求填写七张地图，不要求做 EXTEND，也不授权 AI 代写上述内容。

---

## 2. 两条状态轴

课程资产状态与学习能力状态必须分别记录，禁止自动转换。

### 2.1 课程资产轴

```text
DESIGN -> READY_FOR_FREEZE -> FROZEN -> BUILT -> QA-PASS
                                      -> REWORK
```

- `DESIGN`：任务、输入、输出和 rubric 尚可讨论。
- `READY_FOR_FREEZE`：结构齐全，等用户确认范围与 PASS 条件。
- `FROZEN`：开始学习前已确认 rubric；之后只允许追加 Amendment，不赛后降标。
- `BUILT`：Sol 已交 public、fixture、rubric、sealed 和构建回执。
- `QA-PASS`：主控按冻结合同独立复核通过。
- `REWORK`：课程资产有缺项、答案泄漏、来源错误或不可执行条件。

### 2.2 用户能力轴

```text
LOCKED -> RELEASED -> SUBMITTED -> PASS -> RETAINED -> OWNED
                         |          |          |
                         +------> RE-OPEN <----+
```

- `RELEASED` 只表示前置满足、材料可打开。
- `SUBMITTED` 只表示用户留下可定位作答。
- `PASS` 表示本次冻结 rubric 逐项通过。
- `RETAINED` 表示 D+2/D+7 或题面规定的延迟冷测通过。
- `OWNED` 表示 `RETAINED` 之上，全文覆盖和六道门均有本人证据。
- Sol 的 `QA-PASS` 不得写入用户 Ledger，也不得把能力轴推进一步。

---

## 3. 分阶段诊断，不再用十五题阻塞施工

### D0：当前范围复核

- 只核对已经学过的 EX-00、EX-01、EX-05a、EX-02、EX-03 和当前 EX-05 内容。
- 作用是验证旧作答能否迁移到当前 rubric，并定位需要重做的最小动作。
- 不考尚未系统教学的 Stage 2、完整 Stage 3、论文 evaluation、EdgeAlpha、Ground Truth 或 CrossEdgeIM。
- §1.3 的恢复包就是当前 D0，不额外再开一套六十至九十分钟整篇卷。

### D1：EdgeIM 全管线诊断

- 在 Stage 2/3 桥接模块、evaluation 模块和 EX-07 均完成后执行。
- 覆盖 `event log -> Stage 1 -> Stage 2 -> central aggregation -> IM recursion -> process tree/Petri net -> evaluation/claims`。
- 使用未见日志，不复用 EX-00、论文例子或已公开训练 fixture。

### D2：四论文全文 ownership 冷诊断

- 在四篇各自的全文包完成且至少一次延迟复测到期后执行。
- 旧 `MASTERY_GATE.md` 十五题可作为题库输入，但必须补齐三篇论文各自的全文问题，并替换已经暴露的题。
- D2 是最终验收，不是 Sol 开工门，也不是用户当前继续 EX-05/EX-06 的前置。

---

## 4. 四篇共享的全文 Ownership 合同

### 4.1 全文覆盖矩阵

每篇必须有 `COVERAGE_MATRIX.md`，至少包含：

| 章节/对象 | 原文坐标 | 最低学习动作 | 验收动作 | 当前状态 | 未覆盖理由 |
|---|---|---|---|---|---|
| problem / motivation | 页码或章节 | 闭卷重述问题与约束 | 改一个约束后重述问题 |  |  |
| challenge / prior limitation | 页码或章节 | 说明旧方法为什么不够 | 与一个替代方案比较 |  |  |
| method / mechanism | 页码、公式、算法 | 手推或重建 | 未见例子 |  |  |
| formal objects / assumptions | 定义或公式 | 定义、例子、信息损失 | 表示碰撞或边界题 |  |  |
| experiment protocol | 数据、baseline、参数 | 重建实验合同 | 改一个控制变量 |  |  |
| results / major claims | 表、图、正文 | claim-evidence 表 | 证据上限追问 |  |  |
| limitations / threats | 原文或明确未讨论 | 列出适用边界 | attack mode |  |  |
| related work / genealogy | 原文坐标 | 区分论文自述与独立核验 | 横向或纵向回接 |  |  |
| conclusion | 原文坐标 | 检查是否超出证据 | 压缩表达 |  |  |

摘要、introduction 的 contribution 列表、conclusion 的主要结论，以及实验部分被这些结论引用的主要 claim 必须全部入表。不能用“各挑两条”代替主要 claim 覆盖。

### 4.2 来源顺序

- Sol 建课时必须同时核对原始 PDF 与已有 teardown。
- 用户学习时以原始 PDF 为事实权威；teardown 用于定位、对照和暴露后的纠错。
- teardown、AI 总结和 sealed answer 都不能作为用户的独立能力证据。
- 找不到 primary source 支撑的内容标 `SOURCE-OPEN / UNKNOWN`，不得由 Sol 补成确定答案。
- 本合同不新增 checksum 工作流；来源以明确路径、版本/commit、页码和责任标签管理。

### 4.3 每个核心任务的训练闭环

```text
H0 独立预答
-> 针对性教学或来源核对
-> 关闭材料独立重做
-> 未见 holdout：先预测后检查
-> 写错误更新和 claim ceiling
-> 当前 PASS
-> D+2 / D+7 冷测
```

每项至少留下：

- `pretest`：第一次独立答案和时间；
- `exposure`：看过哪些提示、原文、输出或答案；
- `redo`：关闭材料后的重做；
- `holdout`：未见变体的预测、检查和差异解释；
- `feedback_update`：原信念、击穿证据、正确模型、下次识别信号；
- `claim_ceiling`：当前证据最远支持到哪里；
- `retest_due / retest_result`：延迟复测时间和结果。

### 4.4 提示等级

| 等级 | 允许内容 | 当次能力上限 |
|---|---|---|
| H0 | 只给题面 | 可进入 PASS 评审 |
| H1 | 重述题意、澄清术语，不给步骤 | 可进入 PASS 评审，但必须记录 |
| H2 | 给对象、步骤框架或关键定位 | 最多 `SUBMITTED/SEEN`，需新变体重做 |
| H3 | 给局部推导、关键反例或代码骨架 | `RE-OPEN`，不能据此 PASS |
| H4 | 打开 sealed 或给完整答案 | 该题仅 `SEEN`；必须换题并延迟复测 |

### 4.5 工作稿与最终摘要分开

- 工作证据不设 2500 字上限；手算、代码、claim 表、错误记录和运行输出按任务需要保留。
- 每篇可另交一份不超过 2500 字的最终闭卷重建稿，用于压缩表达。
- 最终摘要是输出之一，不是全文 coverage 或 ownership 的替代品。

---

## 5. EdgeIM 桥接模块与迁移规则

新内容不再简单编号为“EX-08 到 EX-11 并全部接在 EX-07 后”。使用桥接模块表达概念位置，同时不静默改写既有站号。

### 5.1 概念依赖

```text
EX-05a
  -> B-S2   Stage 2：边缘端分派、局部 S_i/E_i/R_i、weight
  -> B-S3A  Stage 3 输入：中心端聚合和全局 DFG
  -> EX-02  IM cuts 的已有训练
  -> B-S3B  完整 IM recursion、process tree、Petri net、soundness

EX-03 -> EX-05 -> EX-06
  -> L-GT / B-EVAL  评测世界、复现合同、claim audit
  -> EX-07           prediction -> check -> verdict
  -> B-DEFENSE       related work、全文重建、连续追问、D1
```

### 5.2 当前学习者迁移规则

用户已经到 EX-05，不要求今天机械回滚重走 EX-02。迁移按以下方式处理：

1. 用户完成 §1.3 恢复包并继续当前 EX-05/EX-06；
2. Sol 在独立写域建设 B-S2/B-S3A/B-S3B/B-EVAL/B-DEFENSE；
3. 新桥接包 QA-PASS 后，用户在进入 EX-07 的最终实验 verdict 和 D1 前补完 B-S2/B-S3A/B-S3B/B-EVAL；
4. B-DEFENSE 只在 EX-07 和三个镜头的必要产物均完成后释放；
5. 旧作答可引用，但未见题、预测、重做和冷测必须产生新证据。

### 5.3 EdgeIM 各模块最小内容

| 模块 | 必须教 | 必须验 | 固定边界 |
|---|---|---|---|
| B-S2 | 分派对象、局部日志、Algorithm 2、support/weight、同时间戳 | 未见局部 trace 手算 + 本人最小实现/修改 + hash/顺序变体 | 不把 Stage 1 的集合 R 当成 Stage 2 权重 |
| B-S3A | 多节点局部产物如何被中心消费、union/aggregation、全局 DFG | 固定 fixture 完整聚合；指出保留/丢失信息 | 不提前把 DFG 等同于模型语言 |
| B-S3B | IM 递归、process tree、Petri net、soundness | 未见 DFG 完整递归 + 一个不 sound 反例 + 形式对象五层 | 不要求补造论文未公开的实现细节 |
| B-EVAL | 九日志设置、baseline、指标、环境/参数、通信/隐私/复杂度 claim | 至少一个可复算单元 + 全部 major claim 表 + 差异解释 | 不能把有限复算写成整篇复现 |
| B-DEFENSE | EdgeAlpha 来源边界、全文三阶段、限制与谱系、四档表达 | 30 秒/2 分钟/10 分钟 + 30 分钟追问 + D1 | 15 分钟只能是中测，不关闭门 6 |

B-EVAL 的 rubric 必须固定数据版本/来源、预处理、具体 miner 变体、参数、模型产物、指标实现和允许差异。缺一项时只能标 `REPRO-CONTRACT-OPEN`。

---

## 6. 三篇论文的全文包

三篇不再各交“一份 2 至 2.5 小时、2500 字重建稿”就结案。每篇可以是一个目录，但必须分多个学习窗口完成以下四阶段。

### 6.1 统一四阶段

| 阶段 | 内容 | 必须产物 |
|---|---|---|
| P0 全文地图 | 填完整 coverage matrix；闭卷说问题、约束、方法和 evaluation 主线 | 全文地图 + OPEN/UNKNOWN |
| P1 机制 ownership | 重建核心算法/方法/架构；完成未见变体 | 手推/模型/最小实现或结构追踪 |
| P2 evidence ownership | 重建实验协议；审计全部 major claims 与 limitations | claim-evidence 表 + claim ceiling |
| P3 attack + defense | 改 assumption、跨论文回写、四档表达、延迟复测 | 冲突卡 + shared artifact 更新 + retest receipt |

### 6.2 sigRank 适配器

- P0：Task、Challenge、Insight、两阶段方法、实验、limitations、related work、conclusion 全覆盖。
- P1：Phase 1 Step 1-4、式 (2)-(6)、Phase 2；Fig. 3 只作训练例，另配未见日志和预算变体。
- P2：重建数据、sampling ratios、baselines、模型质量指标和主要结果；所有主要 claim 入表。
- P3：在 matched interface 或 matched cost 下与 EdgeIM 比较；改 budget/objective 假设并先预测后检查。
- 回写：`Sampling/Selection Matrix`。

### 6.3 Ground Truth Approach 适配器

- P0：问题、ground-truth 需求、方法、simulation、实验、limitations 和 conclusion 全覆盖。
- P1：重建 `initial model -> deviation -> deviating model -> recording error -> imperfect log`，并为未见 world 指定谁生成、谁消费。
- P2：重建 deviation patterns、simulation 参数、指标和主要 claim；区分 behavioral deviation、recording error 与 sampling intervention。
- P3：选择一个具体 deviation 或参数，判断它能否迁移到 EdgeIM；必须写能套、不能套及原因。
- 回写：`World & Evidence Contract`。

### 6.4 CrossEdgeIM 适配器

- P0：问题、residual bottleneck、三层架构、实验、limitations、genealogy 和 conclusion 全覆盖。
- P1：重建 activity node、organization node、central node 的输入、状态、delta 和输出；完成一个未见增量更新例。
- P2：重建实验协议、各图表主要 claim 和证据边界。
- P3：写清 predecessor、redesign、新 residual；攻击一个架构假设并完成口头 defense。
- 回写：`Genealogy & Residual Card`。
- 归属硬边界：CrossEdgeIM 不是鲁法明署名论文，不得把其方法或结果归为导师本人产出。

---

## 7. 四篇之间的钩子

### 7.1 四个共享产物

1. `Mechanism Map`：对象、输入、状态 before/update/after、输出、下游消费者、信息损失；
2. `Sampling/Selection Matrix`：coverage/importance、内生样本量/fixed ratio、接口、成本、consumer；
3. `World & Evidence Contract`：ground truth、deviation、recording error、sampling intervention、指标、claim ceiling；
4. `Genealogy & Residual Card`：predecessor、bottleneck、redesign、new residual、迁移边界。

### 7.2 每篇必须完成的回路

```text
consume 一个已有问题或共享产物
-> 独立重建本篇机制
-> 指出至少一个真实冲突
-> 用未见例子检查
-> 回写一个共享产物
-> 说明这次怎样改变对 EdgeIM 整篇的理解
```

固定冲突至少包括：

- EdgeIM coverage vs sigRank importance；
- endogenous sample size vs fixed ratio；
- DFG structural preservation vs downstream model quality；
- behavioral deviation vs recording error；
- EdgeIM central discovery vs CrossEdgeIM multi-level architecture。

“F-measure 不可直接并表”继续有效；这只禁止错误数值比较，不禁止比较问题、接口、假设和证据结构。

---

## 8. Sol 的明确写域与交付树

### 8.1 第一阶段唯一写域

Sol 第一阶段只写：

```text
learning/training/lu-edgeim-algo1/ownership-v3/
```

建议结构：

```text
ownership-v3/
├── START_HERE.md
├── BUILD_STATUS.md
├── SHARED_ARTIFACTS.md
├── edgeim/
│   ├── COVERAGE_MATRIX.md
│   ├── B-S2/
│   ├── B-S3A/
│   ├── B-S3B/
│   ├── B-EVAL/
│   └── B-DEFENSE/
├── sigrank/
│   ├── COVERAGE_MATRIX.md
│   └── P0-P3/
├── ground-truth/
│   ├── COVERAGE_MATRIX.md
│   └── P0-P3/
├── crossedgeim/
│   ├── COVERAGE_MATRIX.md
│   └── P0-P3/
└── _sealed/
    ├── rubrics/
    ├── training-fixtures/
    └── holdouts/
```

Sol 不得在第一阶段修改：

- `BRIEF.md`、`MASTERY_GATE.md`、`FOUR_PAPER_TRAINING_LOOP.md`、`START_HERE.md`、`CONNECTIONS.md`；
- 现有 `EX-00` 至 `EX-07` 题面、用户答案和 `_sealed`；
- `learning/training/LEDGER.md`、`MISTAKE_LOG.md`、用户 G0/CONNECT/SR/EC/L-S1 产物；
- Fable 的前版设计和 task log。

共享正本接线必须等第一阶段 QA-PASS，并先解决 `TASK-20260906-004` 在 INDEX 与自身日志中的状态冲突，再由主控做最小增量。

### 8.2 每个模块必须交付

- public README：目标、零基础词汇桥、前置、允许输入、核心题、提交格式；
- `RUBRIC.md`：逐项可判定条件、提示等级、失败和重开规则；
- training fixture：与正式题不同的教学微例；
- sealed holdout：未在 public、teardown 摘要或训练例中出现；
- sealed reference：步骤、来源坐标、允许差异和 claim ceiling；
- `BUILD_RECEIPT.md`：实际文件、覆盖章节、已核来源、未解决项、未触碰路径；
- 冷测题：D+2/D+7 题面和评分条件。

### 8.3 来源输入

Sol 可使用：

- `research/papers_lu/EdgeIM-2025-ICWS.pdf`；
- `research/papers_lu/sigRank-2026-TSC.pdf`；
- `research/papers_lu/Sommers-2025-ProcessScience.pdf`；
- `research/papers_lu/CrossEdgeIM-2026-IoTMag.pdf`；
- `research/papers_lu/teardown-bridge-20260904/` 对应拆解件和 critique；
- 当前公开学习包及本合同。

当前 `research/papers_lu/` 未见 EdgeAlpha 原始 PDF。B-DEFENSE 的独立 EdgeAlpha 比较不得只靠 EdgeIM 对自己的 framing 得出最终 verdict；Sol 应标 `SOURCE-OPEN`，等待单独来源补充或把结论限定为 `EDGEIM-AUTHOR-FRAMING`。

---

## 9. Sol 施工顺序

1. 只读核对本合同、四篇 PDF、teardown 标题结构和现有课程接口；
2. 在 `ownership-v3/` 建空结构、状态轴和 coverage matrix；
3. 先完成 EdgeIM B-S2/B-S3A/B-S3B，再完成 B-EVAL/B-DEFENSE；
4. 建三篇 P0-P3 和四个共享产物的 consume/writeback 接口；
5. 分离 public、training fixture、holdout、rubric 和 reference；
6. 自查 public 中是否泄露 holdout 或标准答案；
7. 提交 `BUILD_RECEIPT.md`，状态停在 `BUILT`；
8. 主控独立复核后才能标课程资产 `QA-PASS`；
9. 用户确认每个模块 rubric 后标 `FROZEN` 并按依赖逐步释放；
10. 最后才提案把入口链接增量接入共享正本。

Sol 不判用户 PASS，不改 Ledger，不替用户做任何 recovery artifact。

---

## 10. 主控验收 Sol 的标准

| AC | 可判定标准 |
|---|---|
| AC-01 | 第一阶段改动全部位于 `ownership-v3/` 与 Sol 自己的 task log；现有学习题面、答案和正本零修改 |
| AC-02 | 四篇各有全文 coverage matrix，所有 major claims 有原文坐标或 `SOURCE-OPEN` |
| AC-03 | 每个模块都有 public、rubric、training fixture、holdout/reference、冷测题和 build receipt |
| AC-04 | public 不含 holdout 答案；training example 与 holdout 不是同题换数字 |
| AC-05 | 每个核心能力都有 pretest、redo、unseen transfer、claim ceiling 和 retest 字段 |
| AC-06 | 提示等级和答案暴露后的能力上限写入 rubric，不能由批改者临场决定 |
| AC-07 | 四个共享产物都有明确 consumer 和 writeback；三篇不是孤立摘要任务 |
| AC-08 | B-EVAL 明确数据、预处理、miner、参数、指标和差异处理；未知处不伪造 |
| AC-09 | CrossEdgeIM 作者归属边界和四篇数值不可直接并表边界保留 |
| AC-10 | BUILD_RECEIPT 明确“课程 QA-PASS 不改变用户能力状态”，且未写 Ledger |

任一 AC 不满足，状态为 `REWORK`；不能用“文件很多”“写得很详细”或 Sol 自己的总结替代。

---

## 11. 时间线

### 09-20 核心闭环

09-20 只用于冻结短期 EdgeIM 核心闭环：本人 paper note、foundation 证据、自有 Algorithm 1、当前实验/测量合同、初步 verdict/claim ceiling 和已到期冷测。它不等于四篇全文 `OWNED`。

### 长期四篇 5/5

四篇 5/5 必须完成：全文覆盖、论文类型适配器、未见题、反馈重做、跨论文回写、D+2/D+7 和 D2。时间预算应分别记“初学/初测、反馈重做、holdout、延迟复测”，不再压成每篇 2 至 2.5 小时。

在冷测到期前只能写 `MATERIAL-COMPLETE / CAPABILITY-PENDING`，不能为了日期降 rubric。

---

## 12. 前版需要订正但本稿不代改的事实

1. `learning/training/LEDGER.md` 实际存在；前版 §3.5 和其 task log 的“不存在”判断错误。后续只能追加真实验收行，不能新建或覆盖。
2. 前版 task log 第 18 行保留“e71384d 不存在”的旧结论，第 51 行又订正为存在；交接时不能引用第 18 行。
3. `TASK-20260906-004` 在共享 INDEX 中为 `completed_with_open_gates`，其自身 task log 仍为 `in_progress`；共享正本接线前必须先统一状态和写域。
4. 前版把完整十五题设成 Sol 建课前置。v3 只取消它作为**课程施工门**；用户学习、PASS、冷测和对外能力证明的证据边界不放宽。

---

## 13. 交给 Sol 的一句话

> 先在独立 `ownership-v3/` 写域内把四篇课程资产建到 `BUILT`，以 primary source、全文 coverage、未见变体、反馈重做、跨论文回写和延迟冷测为合同；不要改现有站点、不要替用户作答、不要写 Ledger，也不要把你的构建完成报告成用户 ownership。

