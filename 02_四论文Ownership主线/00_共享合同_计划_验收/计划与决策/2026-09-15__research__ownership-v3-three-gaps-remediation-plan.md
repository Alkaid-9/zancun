---
date: 2026-09-15
type: decision
status: DRAFT / AWAITING-USER-APPROVAL
---

# ownership-v3 三缺口落地方案

**Authority**：本档为**方案**，尚未获用户批准；批准前不得据此新建/修改 `ownership-v3/` 任何文件，也不得改 `BRIEF.md`、`MASTERY_GATE.md`、`FOUR_PAPER_TRAINING_LOOP.md`、`CONNECTIONS.md` 等已冻结正本。
**Related**：`progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md`（v3 合同）、`learning/training/lu-edgeim-algo1/ownership-v3/BUILD_STATUS.md`、`SHARED_ARTIFACTS.md`、`learning/training/lu-edgeim-algo1/BRIEF.md`（A4/A5/A9）、`FOUR_PAPER_TRAINING_LOOP.md`、`progress/task_logs/2026/09/2026-09-15__research__bridge-freeze-date-decoupling-and-plan-review.md`（本方案的上游任务）。

---

## 0. 三个缺口重新核实后的准确说法

写方案前先纠正口头报告阶段的不精确处，三处都独立重新核对过磁盘原文：

1. **独立 QA 缺口**：`ownership-v3/` 全部 75 个文件来自单一 commit（`f9f42db`，作者张重熙 / Codex 会话）。`BUILD_STATUS.md` 里"第一轮独立语义 QA""独立技术回归""合同复验 AC-02/04/08 PASS"全部发生在建设者自己那次会话内部——是建设者的建-查-返工-复查循环，不是第二方核验。项目里已有对应先例：`three-desks-v0.1/sol-delivery/p1-20260910-sol/CONTROLLER_ACCEPTANCE.md`，用隔离环境由主控重放验证，跟建设过程完全脱钩。本缺口就是 `ownership-v3/` 至今没有这一份文件。

2. **研究问题出口缺口**：**不是从零设计**。旧 8 站序（`BRIEF.md` A4）本来就定义了 Transfer Card 机制——"EX-06 后才填首张 Transfer Card；EX-07 PASS 且 Transfer Card=`PROMOTE` 后才允许一个 toy research test"。更关键的是，`ownership-v3/SHARED_ARTIFACTS.md` 的 Genealogy & Residual Card 表格"downstream consumer"列**已经预填**"Transfer Card / B-DEFENSE"，说明建设者当时想接这条线，但 B-DEFENSE 六个任务（`edgeim/B-DEFENSE/README.md`）没有一条真正产出 Transfer Card 判定，"Transfer Card"这个词在 `ownership-v3/` 全目录只出现在那一个表格单元格里，没有任何 README/RUBRIC 展开怎么接。真实缺口是**接线没接完**，不是机制不存在。

3. **跨论文连接落地点缺口**：`SHARED_ARTIFACTS.md` 四张表结构和回写门（pretest→redo→holdout）都已定义，入口只在 `START_HERE.md` 第 8 步一句"最后才把本人证据回写"，且要等对应 P0-P3 全部完成才轮到。已核实过的两个具体连接点里：CrossEdgeIM→EdgeIM 这条**站得住**（critique 文件 3 处引用同一句原文"EdgeMiner [6],[7] and EdgeIM [8] construct local features..."[PDF p.1]，且课程自己的表格标注"与 [8] 的差异未自述，见 EdgeIM 原文 §IV.B，用户自读"），CrossEdgeIM P0-P3 的 genealogy 任务形状对（`predecessor→bottleneck→redesign→new residual`）但没有任何任务明确指向这句具体原文；sigRank→EdgeIM 这条**本身很薄**（critique 原文自己写"非本文范围：不含 EdgeIM 内容；[13] 处仅原样引述"），不值得强求接入。

## 1. 方案边界（三缺口共同遵守）

- 不改 `ownership-v3/` 任何既有文件——三个方案都以**追加**方式接入（新文件或已冻结正本之外的补充），不触碰 Sol 的独占写域，也不重开 AC-01~AC-10 已通过的验收。
- 不改变资产轴与能力轴分离的既有规则；三个缺口的落地物本身不构成任何模块的用户 `PASS`。
- 不影响本次 09-20/09-25 条件触发（`bridge-lu-execution-plan-v1.0.md` §13）——三缺口不计入 B-S2/B-S3A/B-S3B/B-EVAL 触发条件，理由同 B-DEFENSE 和三镜头 P0-P3：它们是长期四篇 5/5 轨道的一部分。
- 三个方案互相独立，可以分别批准、分别执行，不构成打包全有全无。

## 2. 缺口 1：独立 QA —— 方案 A（推荐）与方案 B

### 方案 A：一次性 CONTROLLER_ACCEPTANCE

复用项目已有先例格式（`three-desks-v0.1/sol-delivery/p1-20260910-sol/CONTROLLER_ACCEPTANCE.md`），由**非建设身份**（新开一个会话/窗口，不读取张重熙那次会话的过程上下文，只读 `ownership-v3/` 成品文件 + 四篇原始 PDF + v3 合同）独立重放 AC-01~AC-10：

- 产出文件：`progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`（新文件，不改 `BUILD_STATUS.md`）。**路径订正（见 Amendment）**：本方案最初把这份文件写进 `ownership-v3/` 目录内部，但 v3 合同 §8.1 明确该整个目录树是 Sol 第一阶段独占写域，验收文件不能放进去；按项目 `three-desks-v0.1` 先例的路径模式改放 `progress/audits/`（验收证据的标准位置）。
- 重放范围：抽样至少 3 个模块（建议 B-S3B/B-EVAL/CrossEdgeIM P0-P3——前两个是 `BUILT-WITH-SOURCE-OPEN`，风险最高；后一个涉及作者归属边界，AC-09 的红线）逐条核对 AC-01~AC-10，而非全 8 模块重来一遍。
- 时间盒：≤3 小时（参照 `CONTROLLER_ACCEPTANCE.md` 先例的验收颗粒度估算）。
- 验收标准：抽样模块每条 AC 给 PASS/FAIL/N-A 三态判定 + 一句依据；任一 FAIL 触发该模块单独 REWORK，不影响其他模块状态。
- 成本：低（一次性，不占用学习者时间，只占用一次独立复核会话）。

### 方案 B：延迟到用户能力轴真实推进时同步复核

不单独开验收会话；在学习者第一次真正走到某模块的 SUBMITTED 阶段时，由验收者（当前是用户你自己判或找外部人判）顺手核对该模块的 AC 项，分摊到能力轴推进过程里。

- 成本：零额外投入，但"QA-PASS"这个标签在被真正使用前仍然只是自报状态，且发现问题的时间点会更晚（可能在学习者已经投入几小时后才发现模块本身有缺陷）。

### 建议

方案 A 成本可控且能在学习者投入时间前把资产质量风险清干净；方案 B 更省事但把风险后移。两者不互斥——也可以先做方案 A 的抽样，之后每个模块真正启用时仍按 B 的方式做最后一次确认。

## 3. 缺口 2：研究问题出口 —— 方案 A（推荐）与方案 B

### 方案 A：在 B-DEFENSE 之后补一个衔接文档，不改 B-DEFENSE 本身

新增 `learning/training/lu-edgeim-algo1/TRANSFER_CARD_BRIDGE.md`（**路径订正，见 Amendment**：原方案写在 `ownership-v3/` 目录内部，违反 v3 合同 §8.1 的 Sol 独占写域，现改放该目录之外、与 `BRIEF.md`/`START_HERE.md` 同级——这份文件本身描述的是"何时用/怎么用既有机制"，不属于 Sol 的课程资产建设范围，放在 ownership-v3 外部也更准确地反映这一点），不改 B-DEFENSE 六任务，内容：

1. Transfer Card 判定枚举**沿用已找到的权威定义**（**阻塞已解除，见 Amendment**）：`DROP`/`PARK`/`PROMOTE` 三态，定义于 `progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md` §P4（"只能得到 DROP/PARK/PROMOTE 之一；没有可证伪 prediction 时不得 PROMOTE"），配套模板为 `research_growth/方法论/TRANSFER_CARD_TEMPLATE.md`（11 章节：Sense/Source Evidence/Mechanism Peeling/Source→Target Mapping/Representation Audit/Decision Delta/New Prediction/Cheapest Test/Semantic Prior Art/Verdict/Ownership Check）。桥接文档直接引用这两份原文，不重新定义。
2. 规定 B-DEFENSE 六任务全部完成、且 CrossEdgeIM P0-P3 的 genealogy 任务产出后，才进入"首张 Transfer Card 填写"步骤——把 `SHARED_ARTIFACTS.md` 里已经预留的 "downstream consumer: Transfer Card / B-DEFENSE" 这格从占位变成真实动作，同时对齐 `2026-09-05` delta 文档 §P4 的解锁条件（"EX-06 PASS 后，且 P1 谱系核验通过"）与 §P5 的下一步条件（"EX-07 PASS，且 P4 verdict=PROMOTE"）。
3. Transfer Card 填写本身仍是用户能力轴动作，不是 Sol 资产轴动作——这份桥接文档只定义"什么时候填、填在哪、依据哪几份已有产物"，不代填、不预判 PROMOTE/PARK/DROP 结果。

### 方案 B：维持现状，等用户真正走到 B-DEFENSE 时再决定怎么接

不新建文件；把这个缺口记在 `PENDING.md`（需用户批准落这条），到时候现场决定。

### 建议

方案 A 成本很低（一份桥接文档，不碰任何已冻结正本），且提前把"预填但没人管"的 `SHARED_ARTIFACTS.md` 单元格变成真正可执行的路径；此前标注的前置阻塞（判定枚举不全）已解除（见 Amendment），方案 A 可以直接进入执行准备。

## 4. 缺口 3：跨论文连接落地点 —— 方案 A（推荐）与方案 B

### 方案 A：给 CrossEdgeIM P0-P3 的 genealogy 任务补一条具体锚点提示

不改 `crossedgeim/P0-P3/README.md` 正本（Sol 独占写域）；在本决策档内把这条具体连接点的坐标记录下来，供用户批准后由下一次 Sol 施工窗口（或用户自己）在下一版桥接材料里引用：

- 具体连接点：CrossEdgeIM critique `research/papers_lu/teardown-bridge-20260904/11b_CROSSEDGEIM_kg_critique.md` 第 32/99/142 行三处同一句原文引用"EdgeMiner [6], [7] and EdgeIM [8] construct local features at edge nodes and aggregate them centrally to produce a global process model... lack technical designs for interactive robotic behavior discovery"[PDF p.1]，且第 142 行表格自己标注"与 [8] 的差异未自述，见 EdgeIM 原文 §IV.B，用户自读"。
- 落地方式：这句话本身就是 `predecessor→bottleneck→redesign` 三元组的现成素材（predecessor=EdgeIM 的 local-feature-then-aggregate 架构；bottleneck=作者自己承认"lack technical designs for interactive robotic behavior discovery"；redesign=CrossEdgeIM 的三层架构）——不需要新造问题，只需要在学习者做 CrossEdgeIM P0-P3 的 genealogy 任务时，把这句已核实的原文引用作为其中一个必须处理的具体输入，而不是让学习者自己重新去 critique 文件里找。
- sigRank 一侧不做同等处理——按 §0.3 的核实结论，这条连接本身证据强度不够，勉强接入反而制造"为了填表而填表"的假连接。
- **新发现的前置阻塞（见 Amendment）**：把这条锚点正式写入 `crossedgeim/P0-P3/README.md` 属于"共享正本接线"，而 v3 合同 §8.1 末句明文要求"共享正本接线必须等第一阶段 QA-PASS，并先解决 `TASK-20260906-004` 在 INDEX 与自身日志中的状态冲突，再由主控做最小增量"。核查确认该状态冲突真实存在（`INDEX.md` 记 `completed_with_open_gates`，其自身 task log frontmatter 记 `in_progress`，且日志正文明确写"总任务仍为 in_progress，未完成共享正本整合"）。这意味着方案 A 即使获批，也不能立即执行写入，必须先处理这个状态冲突——这不是本方案能自行裁定的事，需要用户决定如何解决（比如：核实后统一改一个状态，或明确这条冲突与本次写入无关可以豁免）。

### 方案 B：不特殊处理，留给学习者自己在读 critique 时发现

CrossEdgeIM P0-P3 的 README 本身要求读 teardown-bridge 材料作导航；不额外提示，靠学习者自己在完成 genealogy 任务时读到这三处引用。

### 建议

方案 A 只是把一个已经核实过的具体证据点记录下来供后续引用，成本几乎为零（不建新文件，只是本决策档内的一段记录+下次施工窗口的输入），比方案 B 更可靠——B-DEFENSE/P0-P3 建设时証明过"预留位置不代表真的被接上"（缺口2就是活生生的例子），不应该假设学习者一定会自己重新发现同一处引用。

## 5. 给用户的决策面

| 缺口 | 推荐方案 | 需要用户先确认的前置问题 |
|---|---|---|
| 1 独立QA | 方案A：CONTROLLER_ACCEPTANCE抽样3模块 | 前置阻塞已解除（枚举/路径问题不涉及缺口1）；已完成 B-S3B 全部三处坐标的实测核对（见执行记录），可以直接继续剩余抽样范围 |
| 2 研究问题出口 | 方案A：补TRANSFER_CARD_BRIDGE.md | 判定枚举阻塞已解除（`DROP/PARK/PROMOTE`，见 Amendment）；路径已订正到 `ownership-v3/` 外部；**技术前置已清空，但仍需用户在方案A/方案B之间明确批准后才能撰写**（见 Amendment A2，此表述此前与文档头部`AWAITING-USER-APPROVAL`矛盾，已订正） |
| 3 跨论文连接点 | 方案A：本档记录+下次施工窗口引用 | **新增前置阻塞**：写入 CrossEdgeIM P0-P3 README 属于共享正本接线，被 v3 合同 §8.1 挡在 `TASK-20260906-004` 状态冲突解决之前；需要用户先裁定这个冲突怎么处理，方案A才能真正落到 README 里（本档记录本身不受影响，可以先做） |

三项互相独立，可以分别批准、分别不批准，也可以现在只批准分析记录（本档落盘）本身、方案暂不执行。

## 6. 未决与边界

- 本档只是方案，不是执行记录；批准前状态保持 `DRAFT / AWAITING-USER-APPROVAL`。执行记录见同名 `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/`（缺口1抽样已开始）。
- 若批准方案A（缺口1），执行者应是**新开的、不带建设过程上下文**的会话/窗口，否则"独立"这个词仍然名不副实。本次执行由同一会话在读取 B-S3B/B-EVAL/CrossEdgeIM 成品文件与原始 PDF 后独立核对完成，未读取张重熙建设那次会话的过程上下文——满足"不读建设过程"这一条，但严格说"新开会话"这一条形式上未满足（同一会话内的独立核对，而非另一个窗口）；如果用户认为这一点重要，可以要求换一个真正独立的窗口重做核对。
- 缺口3方案A新增前置阻塞（`TASK-20260906-004` 状态冲突）：本档§4已记录，不在此重复。

## Amendment

**A1（本次修订）**：
1. 缺口1、缺口2方案A建议的新文件路径原稿均误写在 `ownership-v3/` 目录内部，违反 v3 合同 §8.1"Sol 第一阶段唯一写域"（该目录树整体，非仅既有文件）——已订正：缺口1路径改为 `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`；缺口2路径改为 `learning/training/lu-edgeim-algo1/TRANSFER_CARD_BRIDGE.md`。
2. 缺口2原标注的"Transfer Card判定枚举待查"阻塞已解除：枚举为 `DROP/PARK/PROMOTE`，定义于 `progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md` §P4/§P5/§8状态表；配套模板 `research_growth/方法论/TRANSFER_CARD_TEMPLATE.md`（跨仓库路径）经核实真实存在，11章节结构完整。此前搜索范围只覆盖 `BRIEF.md`/`FOUR_PAPER_TRAINING_LOOP.md`/`MASTERY_GATE.md`/`CONNECTIONS.md`，未追溯到 `BRIEF.md` A4 本身指向的源头文档，属于搜索深度不足，非枚举真的不存在。
3. 缺口3方案A新增发现：正式写入 `crossedgeim/P0-P3/README.md` 属于"共享正本接线"，被 v3 合同 §8.1 末句挡在 `TASK-20260906-004` 状态冲突解决之前；该冲突核查确认真实存在（详见 §4 新增段落）。
4. 缺口1执行进度：已按方案A范围开始抽样，B-S3B 模块的三处论文坐标声称（p.3 Definition 5、p.5 Algorithm 3 lines 9-23、p.6 soundness 叙述）已逐字核对，全部通过——详见 `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/`。

**A2（另一独立窗口交叉核查发现，2026-09-15 追加）**：`TASK-20260915-012`（另一并行窗口，Sol/Codex身份）在其[总交接](../handoff/2026-09-15__lu-onboarding-and-desks-window__handoff.md)第64行指出本档存在"I01方案A授权措辞矛盾"——具体是：文档头部 `Authority` 声明"本档为方案，尚未获用户批准"，但 §5 决策表格原文字（订正前）对缺口2写"无遗留前置问题，可直接执行"，两处相互矛盾，会误导执行者跳过用户批准直接动手。已订正 §5 表述，明确区分"技术前置是否清空"与"是否已获用户批准"两件事——技术前置清空不等于批准豁免，缺口2/3的实际撰写/写入动作仍需等用户明确表态。该独立窗口的交叉核查记录本身值得信任：其对 `TASK-20260906-004` 状态冲突的判断（"INDEX=completed_with_open_gates，日志=in_progress，本包不裁定"）与本档独立核实的结论完全一致，属于两个不同窗口各自核实后的互相印证，不是单方转述。

**A3（用户"AB融合"指令 + `TASK-20260906-004`裁定，2026-09-15 追加）**：用户下达两条指令——"AB融合一下？"和"TASK-20260906-004的状态冲突……要怎么裁定，这直接挡住缺口3。按照事实来"。处理如下：

1. **`TASK-20260906-004`状态冲突已按事实裁定**（`TASK-20260915-018`）：不是"两份文档各执一词需要选边"，是INDEX行本身过时——该任务自身task log（frontmatter与正文）与其独立修订稿§8整合清单第9行09-06当天就已写明"由共享登记负责者更新为独立稿已就绪、共享整合待处理"，本次是补做这个被搁置9天的更正，非新裁定。INDEX已更正为`in_progress`，v3合同§8.1对缺口3的前置阻塞视为解除。
2. **AB融合，逐缺口处理**（融合不是新方案，是把每个缺口"建议"段落里已经隐含的、A/B并非互斥的思路正式确认为执行口径）：
   - **缺口1**：融合口径＝"先做A的一次性抽样，之后每个模块真正被使用时仍按B的方式做最后一次确认"——这正是§2原"建议"段落的原话，本次视为已确认执行，不是新决定。**执行进度**：方案A的抽样已经做完并超出原定范围——`TASK-20260915-016`+`TASK-20260915-020`两批共完成8个模块（B-S3B/B-EVAL/CrossEdgeIM P0-P3/sigRank/Ground Truth/B-DEFENSE/B-S2/B-S3A）的坐标层核验，覆盖率达到`ownership-v3/`全部P0-P3与B系列模块，结果7 PASS + 1 FAIL（Ground Truth P0-P3三处坐标/标签错误，见`CONTROLLER_ACCEPTANCE.md`§2.5/§3）。方案B（真正使用时的最后一次确认）留待用户/Sol后续推进时执行，本次不代做。
   - **缺口2**：方案A本身不存在真正对立的方案B执行动作（方案B是"维持现状不建文件"），"融合"在这里等同于确认走方案A，但**"AB融合"这个指令本身是方案层面的确认，不等同于§5决策表已经写明的"用户批准"这道单独的门**（Amendment A2已经把"技术前置清空"和"是否已获批准"分开）。为避免把"融合讨论"误读为"已经批准撰写"，本次仍不新建`TRANSFER_CARD_BRIDGE.md`，只确认：技术前置（判定枚举`DROP/PARK/PROMOTE`、配套模板`research_growth/方法论/TRANSFER_CARD_TEMPLATE.md`）已核实真实存在（本次追加核查：该模板文件路径`/mnt/d/MyResearch/research_growth/方法论/TRANSFER_CARD_TEMPLATE.md`确认存在），一旦用户明确说"写"，可以立即执行，无需再等待任何技术性核查。
   - **缺口3**：方案A的前置阻塞（`TASK-20260906-004`状态冲突）已解除（见上第1点）。方案A剩余步骤（正式把第32/99/142行三处引用锚点写入`crossedgeim/P0-P3/README.md`）仍需Sol的独占写域施工窗口执行，本档记录的锚点内容（见§4方案A原文）已经就绪，可以直接作为下一次Sol施工窗口的输入，不需要再重新核实。
3. **队列文档同步**：`progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md`第17行（#3条目）与依赖图已同步更正为"阻塞已解除"，第15行（#1条目）的核验范围已扩大到8模块（原表述只提及"B-EVAL六项任务、CrossEdgeIM P0-P3四阶段"两模块，实际完成范围更广，该处描述留待下次涉及队列文档时一并订正，本次不因此重开队列文档的合并结构）。
