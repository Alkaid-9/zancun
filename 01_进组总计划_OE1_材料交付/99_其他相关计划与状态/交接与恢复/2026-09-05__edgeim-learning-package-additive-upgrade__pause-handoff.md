# EdgeIM 学习包增量升级：暂停交接

- 日期：2026-09-05 09:59 +0800
- 任务：`TASK-20260904-004`
- 状态：`PAUSED / RECOVERABLE / NO-EXECUTION-AUTHORITY`
- 工作区：`/mnt/d/MyResearch/MAS_Safety_Project`
- 分支：`master`
- 暂停原因：用户明确要求“停一下，做一下交接文档”。

## §0 · TL;DR

地图和前半增量已落盘，后半未验收，等待恢复口令。

## §1 · 本次暂停的边界

1. 本档是可恢复的事实交接，不是任务完成报告，也不是新的执行授权。
2. 用户要求暂停后，未继续修改学习包、未运行实验、未运行 PM4Py、未提交、未推送。
3. 两个子 Agent 已被中断：`/root/front_stations_reviewer`、`/root/back_stations_writer_retry`。落档时没有运行中的子 Agent；它们的修改不能因为曾由 Agent 产生就视为已验收。
4. 暂停期间不再派发 Agent。恢复后总并发仍以 3 为上限，子 Agent 必须显式使用 `gpt-5.6-sol`。
5. 当前工作树在本任务开始前已经含有其他窗口的修改；本档不把全树 dirty 状态归因给本任务。

## §2 · 权威链与阅读顺序

新窗口先读本档，再按下列顺序恢复事实；不要从聊天摘要或 Agent 自述推断完成度。

1. [`progress/handoff/INDEX.md`](INDEX.md)：跨窗口路由和最新档入口。
2. [`SDD progress`](../../.superpowers/sdd/2026-09-04-edgeim-learning-package-additive-upgrade/progress.md)：任务状态和执行裁定。
3. [`review-contract.md`](../../.superpowers/sdd/2026-09-04-edgeim-learning-package-additive-upgrade/review-contract.md)：严重度、逐任务验收和整包验收。
4. [`approved plan`](../../docs/superpowers/plans/2026-09-04-edgeim-learning-package-additive-upgrade.md)：写域、任务顺序和最终门。
5. [`approved spec`](../../docs/superpowers/specs/2026-09-04-edgeim-learning-package-additive-upgrade-design.md)：用户范围、解锁边界和七图追加。
6. [`BRIEF.md`](../../learning/training/lu-edgeim-algo1/BRIEF.md) 最新 A4/A5/A6：唯一站序、四论文镜头和当前教学合同。
7. [`START_HERE.md`](../../learning/training/lu-edgeim-algo1/START_HERE.md)、[`PAPER_MAP.md`](../../learning/training/lu-edgeim-algo1/PAPER_MAP.md) 和七图入口：当前学习表面和证据边界。
8. [`CrossEdgeIM 主来源审计`](../../.superpowers/sdd/2026-09-04-edgeim-learning-package-additive-upgrade/crossedgeim-source-audit.md)：停放枝能安全写到的上限。
9. [`handoff-checklist`](../runbooks/handoff-checklist.md) 与 [`no-tmp-archive`](../runbooks/no-tmp-archive.md)：本档自审和持久化护栏。

## §3 · 已完成且有独立复审的部分

以下状态只按对应 receipt / rereview 记录，不代表学习者已经掌握，也不代表整包完成。

### 3.1 Task 0：规格与计划

- 已有批准的 spec、plan、review contract 和 SDD progress。
- 起始锚点记录为 `HEAD=da66308fb34abb8f93c40be07de119231914c7e2`；当时工作树已 dirty。
- 计划明确：保留 `0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7`，只增量，不改学习者答案、Ledger、Mistake Log，不提交或推送。

### 3.2 Task 1：全局入口与论文地图

- 产物：[`START_HERE.md`](../../learning/training/lu-edgeim-algo1/START_HERE.md)、[`PAPER_MAP.md`](../../learning/training/lu-edgeim-algo1/PAPER_MAP.md)。
- `task-1-rereview.md` 判定 `CLOSED`。
- 已固定唯一站序、`SEEN / SUBMITTED / PASS / RETAINED` 的分离、整站集中反馈、旧证据复用规则和密封边界。
- 论文地图把作者原文、学习者推论和未知分开；充分信息、切日志到切图、precision 张力和通信/隐私证据仍作为问题或裁定表，不提前替学习者回答。

### 3.3 Task 2：连接索引、受控卡与阅读导航

- 公开索引：[`CONNECTIONS.md`](../../learning/training/lu-edgeim-algo1/CONNECTIONS.md)。
- 八张受控卡在 `learning/training/lu-edgeim-algo1/_sealed/connections/`；两份旧阅读材料的结论段迁入对应受控路径。
- 三个 EX-01 阅读导航文件已恢复，且公开部分只负责定位和方法导航。
- `task-2-rereview.md` 判定 `CLOSED_TASK_2`；其中 EX-01 三处可解析链接保留为 `OPEN_CROSS_TASK_TASK3`，不是 Task 2 的漏项，而是后续 Task 3 接线项。

### 3.4 Task 2b：七张地图、研究树和停放枝

- 产物：[`KNOWLEDGE_MAP.md`](../../learning/training/lu-edgeim-algo1/KNOWLEDGE_MAP.md)、[`RESEARCH_MAPS.md`](../../learning/training/lu-edgeim-algo1/RESEARCH_MAPS.md)、[`RESEARCHER_COMPETENCY_MAP.md`](../../learning/training/lu-edgeim-algo1/RESEARCHER_COMPETENCY_MAP.md)、[`RESEARCH_IDENTITY_MAP.md`](../../learning/training/lu-edgeim-algo1/RESEARCH_IDENTITY_MAP.md)、[`RESEARCH_TRAJECTORY_MAP.md`](../../learning/training/lu-edgeim-algo1/RESEARCH_TRAJECTORY_MAP.md)。
- `task-2b-rereview.md` 判定 `CLOSED_TASK_2B`；上一轮 I1–I5 均有关闭证据。
- 当前对象主干仍是 `EdgeIM -> Stage 1 -> DFG support/weight -> Stage 3 IM -> process tree -> Petri net`；当前小视窗只开 `weighted DFG -> 为什么描边不够 -> cut -> sequence cut`。
- 七图不是七门新课。旁枝状态 `SEEN / OPEN / PARKED / OWNED / TRANSFERRED` 与站点验收状态正交；只能由 Dependency、Repeated recurrence 或 Research leverage 升级。
- CrossEdgeIM、DES、形式化验证、runtime assurance 和 MAS safety 已按来源审计登记为 `PARKED`，不进入当前站题面。

### 3.5 Task 2c：系统阅读与 evidence closure 接口

- 产物：[`RESEARCH_NOTE_TEMPLATE.md`](../../learning/training/lu-edgeim-algo1/RESEARCH_NOTE_TEMPLATE.md)。
- `task-2c-rereview.md` 判定 `CLOSED_TASK_2C`。
- 模板固定四个入口：`System reading`、`Evidence audit`、`Evidence closure`、`Research hooks`；要求数据流、状态前/更新/后、算法步骤到代码锚点、来源归属和主张上限。
- “像 bug / 假设怪”不能停在直觉；缺少区分证据时保持 `OPEN / UNKNOWN`。逐行注释、阅读时长、一次绿灯都不计作 Level 2 证据。

### 3.6 CrossEdgeIM 主来源审计

- [`crossedgeim-source-audit.md`](../../.superpowers/sdd/2026-09-04-edgeim-learning-package-additive-upgrade/crossedgeim-source-audit.md) 已完成主来源核验。
- 可安全写作：作者、四位共同作者、三层数据流、organization-level IM/Petri net 和中心结构化合并，以及作者明写的“未显式捕获多机器人协作关系、组织间 interaction 为 implicit”。
- “CrossEdgeIM 是 EdgeIM 的正式直接后继”、DES/formal verification/runtime verification/MAS safety 均不能升级为论文贡献；相应内容保持 `USER-RECONSTRUCTION / UNKNOWN`。

## §4 · 当前已落盘但尚未验收的前半站增量

下面是磁盘事实，不是 PASS 结论。恢复时必须先读 diff，再由独立 reviewer 逐项审。

### 4.1 已出现修改的站点文件

- `EX-00/README.md`：增加核心题后的 C00 研究连接和地图/证据入口。
- `EX-01/README.md`：增加三层计数桥、集中提交点，并把三个阅读导航与后续受控材料改成可解析路径。
- `EX-05a/README.md`：增加 Python 函数、参数、返回值、set、tuple、遍历顺序、assert 的最短零基础桥。
- `EX-02/README.md`：增加 sequence-cut-first 六步入口；补 choice/parallel/loop 的分段桥；明确公开核心是 `D + 正序 D′` 六档共 12 棵，逆序为非门槛 `EXTEND`；增加 C02 连接入口。
- `EX-03/README.md`：明确 EX-02 完整原始 `D` 的手切树为前置；增加合法性 × 新颖性 2×2 桥和 evidence-closure 入口。
- `_sealed/EX-02_answer.md`：仅有任务 10 判分口径的局部文字修改，意图是澄清 12 棵公开核心与逆序延伸；树、阈值、算式和答案值不得被改动，尚未完成独立 byte-level 复核。

### 4.2 这些修改的当前状态

- 它们来自已中断的前半站 Agent 写入和主控已有增量，当前都应标为 `UNREVIEWED / NOT-PASS`。
- Task 3 报告尚不存在；Task 3 的独立审查、链接复核、原题/PASS 保留核对和密封局部复核尚未做。
- `EX-01` 的三处链接修正是 Task 2 rereview 明确留下的跨任务门；恢复时优先核对目标存在和相对路径。

## §5 · 当前已出现但尚未形成 Task 4 的后半状态

- `EX-05/README.md` 磁盘上已有一段测试词汇/证据边界增量，包含 oracle、fixture、seed、traceback、representation、invariant、四类证据和最小 System reading 要求；它是部分写入，不能视为 Task 4 完成。
- `EX-06/README.md` 与 `EX-07/README.md` 当前仍是基线版本，尚未加入计划中的缩写/归属桥、claim-evidence 矩阵、量词/外部效度修正。
- `C05/C06/C07` 当前没有经 Task 4 独立复审的后半卡增量；先读当前文件，不要假设它们已符合 Task 4 brief。
- Task 4 报告尚不存在，后半三个站和受控卡均未验收。

## §6 · 尚未开始的任务与开放门

### 6.1 Task 3

触发 = 用户明确恢复后，先由主控审当前前半 diff，再分配一个只读/审查写域的 `gpt-5.6-sol` Agent；不得把中断 Agent 的自述当 receipt。

必须完成：

- 逐站审 EX-01、EX-05a、EX-02、EX-03 及允许局部修改的 EX-02 sealed 文件。
- 证明三层计数桥先于任务提问，且没有把 L1 答案写进题面。
- 证明 sequence-cut-first 先于首次正式 cut 任务，且没有要求先懂 Petri net。
- 证明公开核心 12 棵与逆序 `EXTEND` 的数量口径唯一，原 PASS 没有降低。
- 逐项检查原任务标题、原题和 PASS 文本仍在；对 `_sealed/EX-02_answer.md` 做答案值不变的局部比较。
- 写 `task-3-report.md` 和独立 `task-3-review.md` / rereview，状态未关闭前不得写 PASS。

### 6.2 Task 4

触发 = Task 3 的接口和共享地图链接先被主控核对，且用户仍授权继续。

必须完成：

- 审/补 EX-05 的最小测试桥和四类证据边界。
- 补 EX-06 的 DFG、IM、IMf、GT、surrogate、claim ceiling 首次展开和四方归属；补不预填裁定的 claim-evidence 表。
- 补 EX-07 的全称猜想、有限证据上限、trace replay/fitness 与语言等价区分、外部效度延伸。
- 更新并审 C05/C06/C07；每个 CONNECT/EXTEND 都明确不影响 PASS。
- 写 `task-4-report.md` 和独立复审；当前 EX-05 部分内容不可自动继承为已验收。

### 6.3 Task 5 与 Task 6

触发 = Task 3、Task 4 各自有独立关闭证据。

- Task 5：只由主控做 `BRIEF.md`、站点链接、站序、四论文镜头和受控解锁的最终整合；当前 A6 已出现，但整合任务仍未正式关闭。
- Task 6：只由主控写实际 task log / 必要索引，并执行整包验收；不得在暂停期间预写“完成”。

## §7 · 保护对象与当前哈希异常

以下四个路径是不可修改的学习者证据/账本。恢复前必须重新计算；不得为了让哈希变绿而覆盖文件。

| 路径 | 计划基线 | 暂停时当前 | 结论 |
|---|---|---|---|
| `learning/training/lu-edgeim-algo1/EX-00/answer.md` | `e8276348…` | `e8276348…` | 一致 |
| `learning/training/lu-edgeim-algo1/EX-01/answer_EX_01.md` | `252eeec9…` | `0fdeca9f…` | **不一致，来源待核；不得编辑** |
| `learning/training/LEDGER.md` | `eac75c03…` | `eac75c03…` | 一致 |
| `learning/training/lu-edgeim-algo1/MISTAKE_LOG.md` | `ff3db0ee…` | `ff3db0ee…` | 一致 |

说明：`EX-01/answer_EX_01.md` 当前为 untracked 文件，且与 SDD 保存的计划基线不同；这个事实在暂停时才被明确核对。不能据此推断是谁改的，也不能在恢复前自行替换或删除。第一动作是只读查明当前文件的来源/版本关系，再把结果交给用户或主控裁定。

## §8 · 共享工作树与未归属改动

当前 `git status` 显示许多不属于本任务的文件，包括 `progress/` 看板、其他研究线、`task_logs/INDEX.md`、方法论文件和其他窗口的 handoff/decision 产物。本任务的计划明确：

- 不用 `git add -A`、`commit -a`、reset、clean、stash 或整文件覆盖。
- 不要把整棵树的 `git diff --check` 失败归给 EdgeIM；已知共享 `task_logs/INDEX.md` 存在其他窗口的换行/空白门，未经所有权和 CAS 授权不要修它。
- 不要修改 `LEDGER.md`、`MISTAKE_LOG.md`、四个保护答案或任何未列入当前任务写域的文件。
- 不要重写原题、删掉历史 Amendment、移除密封内容或提前打开其他 sealed answer。

## §9 · 新窗口第一动作表

用户没有明确恢复前，第一动作只是读档和核对，不执行剩余任务。

1. 读本档 §0、§2、§6、§7、§10 和 `INDEX.md` 的本路由行。
2. `agents.list_agents` 确认没有运行中的子 Agent；若仍有运行态，先中断/收口，不继续写入。
3. 只读记录仓库 identity、`HEAD`、branch、staged paths 和当前 status；保留其他窗口改动。
4. 重新计算四个保护哈希，优先调查 EX-01 answer 的不一致；调查前不审改题面。
5. 阅读 SDD progress、review contract、Task 3/4 brief、当前五个前半 README 和 EX-05/06/07 当前版本。
6. 对所有 Agent 写入先做路径级 diff 和目标存在性检查；没有 reviewer receipt 就标 `UNREVIEWED`。
7. 只有用户明确说继续后，才按“Task 3 审查 -> Task 4 审查 -> 主控整合 -> Task 6 验收”顺序恢复；同时保持总并发不超过 3、子 Agent 为 sol。

## §10 · 恢复后的推荐分工与边界

若用户明确恢复，默认只启两个子 Agent，主控保留最终整合权：

| 角色 | 允许写入 | 不允许写入 | 交付 |
|---|---|---|---|
| 前半审查 Agent | Task 3 brief 列出的前半 README 与对应 review receipt | 答案、Ledger、Mistake Log、BRIEF、共享索引 | 独立 finding 表、路径/行锚、结论上限 |
| 后半审查 Agent | EX-05/06/07 与 C05/C06/C07 的 Task 4 写域及 review receipt | 前半文件、答案、Ledger、Mistake Log、BRIEF、共享索引 | 独立 finding 表、路径/行锚、结论上限 |
| 主控 | progress、Task 5/6、最终链接/哈希/差分验收和本档更新 | 未经确认的他人写域、保护对象 | 合并裁定、最终 task log、用户可读回报 |

任何 Agent 报告都必须区分：文件事实、作者原文、学习者证据、Agent 推论和 UNKNOWN；发现疑似问题时必须给 Evidence closure，不得只写“像 bug”。

## §11 · 完成标准（当前尚未满足）

只有同时满足以下条件，才能把本任务标为完成；本档当前明确不满足。

- Task 3 和 Task 4 各有独立 review 与 narrow rereview，Critical/Important 为零或有用户明确处置。
- Task 5 的 BRIEF、START_HERE、连接卡、站点题面和四论文镜头经过主控路径/术语整合；路线仍是 `0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7`。
- Task 6 完成原题/PASS/密封边界、内部链接、答案泄露哨兵、七图入口、`CONNECT/EXTEND` 非门槛、有限证据 claim ceiling 和全包可读性检查。
- 四个保护路径哈希在授权范围内与已解释的基线一致；EX-01 answer 的当前不一致已由其所有者裁定，不得被静默覆盖。
- solver 环境预检、允许的 Algorithm 1 参考脚本检查、路径级 `git diff --check` 和本地 Markdown 链接检查均有新鲜回执；共享换行门不被偷修。
- 必要的 task log / handoff INDEX 路由已由主控按登记规则写入；没有 stage、commit、push 的隐含结论。
- 用户读档并明确接受最终状态；否则仍是 `RECOVERABLE / USER-PENDING`。

## §12 · 默认恢复问句

用户若说“继续”，默认解释为：先只读审计当前 Task 3/4 部分写入，核对保护哈希和所有权，再按 §10 分工；不把中断 Agent 的结果直接标 PASS。若用户只说“读一下/看看”，保持暂停，不启动写入或实验。

## §13 · 反向引用与可恢复性

- 本档应由 [`progress/handoff/INDEX.md`](INDEX.md) 的最新 EdgeIM 路由行指向。
- SDD 状态由 [`progress.md`](../../.superpowers/sdd/2026-09-04-edgeim-learning-package-additive-upgrade/progress.md) 的暂停条目反向指向本档。
- 任务规则由 [`review-contract.md`](../../.superpowers/sdd/2026-09-04-edgeim-learning-package-additive-upgrade/review-contract.md) 和 [`handoff-checklist`](../runbooks/handoff-checklist.md) 约束。
- 恢复所需的学习包入口、七图、受控卡和来源审计均在 §2、§3、§4 的路径中；不存在依赖聊天上下文才能解释的隐含文件。

## §-2 · 用户拍板点

- [x] 用户明确要求暂停并要求交接。
- [ ] 用户已读本档。
- [ ] 用户明确恢复剩余任务。
- [ ] 用户确认 EX-01 answer 当前哈希不一致的归属/处理方式。
- [ ] 用户确认最终整包状态。

## §-1 · 主控落档自审记录（2026-09-05 10:00）

| 维度 | 结果 | 备注 |
|---|---|---|
| L0 路径合规 | ✅ 0 命中 | 新档没有临时目录路径字符串 |
| L1 文件存在性 | ✅ 230 行 | 本档超过 50 行；关联 spec/plan/report 路径均已列且存在 |
| L2 任务颗粒度 | ✅ 初审通过 | 每个未完任务均写触发条件；Task 3/4/5/6 分工不重叠 |
| L3 记忆/护栏 | ✅ 已核对 | 使用 file-first、零假设、证据闭环和暂停交接约束；不新增记忆写入 |
| L4 文档引用 | ✅ 通过 | INDEX 与 SDD progress 均已反向指向本档；本档相对链接无断链 |
| 保护对象 | 已核对异常 | 三个保护哈希一致；EX-01 answer 不一致，已升级为恢复门 |
| Agent 状态 | 已核对 | 两个子 Agent interrupted；未继续派发 |

**自审结论**：本档已通过写后机械检查；它仍是 `PAUSED / RECOVERABLE / USER-PENDING`，不等于任务完成或恢复授权。
