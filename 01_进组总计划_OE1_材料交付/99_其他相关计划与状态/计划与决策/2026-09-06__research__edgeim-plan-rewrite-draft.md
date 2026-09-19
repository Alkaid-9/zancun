# EdgeIM 学习主干与进组计划重构初稿

**状态**：`DRAFT / NOT-AUTHORITY / INPUT-FOR-REVIEW`

**作者窗口**：Codex `/root`，session `01a0765b-7d21-7690-a8b8-f7e7f69622d0`

**日期**：2026-09-06

**任务**：`TASK-20260906-004`（初稿落盘；尚未改写现行计划）

> **2026-09-06 恢复勘误**：上句与下文“尚未改写”保留为初稿时点的记录，不代表当前磁盘状态。本窗口随后确实写过共享学习入口和项目卡，且一度误用邻窗已占用的 `TASK-20260906-003`；后改为中央分配的 `TASK-20260906-004`。用户指出越界后，本窗口停止这些共享写入。本次继续仅完善 TASK-004 的独立稿与回执。§6 是历史提案，不是当前写入授权；§9 的“初步采纳”和 `CLAIMS / GOVERNANCE` 是助手判断，没有用户正式采纳回执。具体归属和剩余工作见[本窗口任务回执](../task_logs/2026/09/2026-09-06__research__edgeim-plan-rewrite-draft-and-input-review.md)。

## 0. 初稿用途

这份文件先保存当前窗口在阅读新增桌面材料之前形成的设计假设。它不是学习计划正本、不是用户能力记录，也不是对论文事实的核验结果。后续读取新增材料后，任何被推翻、收窄或改名的部分都在本文件追加修订记录，不覆盖本版初稿。

## 1. 当前输入与边界

- 完整会话归档：`research/papers_lu/session-archive-20260906/ONLY_PAPER_FULL_SESSION_20260906.md`。
- 会话 provenance：同目录 `README.md`；原文件与副本 SHA-256 为 `c204d276ec97187e04226c1772c132b63eadfc7a43bc6afb09f89f7f1301c381`。
- EdgeIM 框架输入：`D:\Alkaid\Desktop\更改EdgeIM学习计划和进组计划！！！.md`。
- 当前学习入口：`learning/training/lu-edgeim-algo1/MASTERY_GATE.md`、`BRIEF.md`、`FOUR_PAPER_TRAINING_LOOP.md`。
- 当前路由卡：`progress/projects/jinzu-sprint.md`、`progress/projects/lu-side.md`。

会话归档同时包含 EdgeIM、鲁/孙组方向、工业研究、开源、设备和其他讨论；它只能提供用户目标与待核验的建议输入，不能直接充当论文事实源、团队事实源或本人能力证据。

## 2. 从会话抽出的用户目标（待材料复核）

1. EdgeIM 学习不能被压缩成进组面试准备；学习主干和研究邻域是主体，进组表达是下游出口。
2. EdgeIM 需要整篇 ownership：问题、三阶段、表示、下游 IM/Petri net、实验与 claim 边界都能重建。
3. 学习采用“纵向深挖 + 横向回接整篇”的双线程；每个核心节点都要回答输入、输出、丢失信息和整篇位置。
4. 以 EdgeIM 为树干，受控打开 sampling/selection、representation/loss、model discovery、evaluation/evidence、genealogy 等枝；sigRank、Ground Truth Approach、CrossEdgeIM 是不同观察镜头，不平均精读。
5. 研究动作要形成 `prediction -> check -> verdict -> claim ceiling` 闭环；没有本人证据的内容只能标为输入、用户报告、假设或未知。
6. 实践 scope 可以窄，认知 scope 不能窄；研究邻域应小而真实，不能变成无边界百科全书。
7. 长期工业研究、开源飞轮和更宽领域地图作为方向约束与远期出口，暂不抢占 EdgeIM 站序。

## 3. 拟采用的分层结构

### A. EdgeIM 学习主干（现行正本）

保持站序 `0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7`、原题面、PASS 条件、答案密封和冷启动规则。主脊柱为：

```text
event log -> sampling/filtering -> local S/E/R -> global DFG
-> Inductive Miner -> process tree/Petri net -> evaluation
```

六道 Mastery Gate 作为跨站能力要求：整篇重建、算法手推、形式对象、claim-evidence、attack mode、四档压缩。Whole-Paper Diagnostic 用来定位真实缺口，不把密封答案或 AI 讲解升级为本人 PASS。

### B. 受控研究邻域（学习主干的上层）

- `sigRank`：selection objective、coverage/significance、预算与公平比较。
- `Ground Truth Approach`：ground-truth world、记录误差、指标和证据闭合。
- `CrossEdgeIM`：前序瓶颈、架构变化、残余问题和跨组织表示边界。
- `representation / loss`：DFR、权重、DFG 与下游发现之间的充分性和丢失信息。

每个枝只在依赖、反复出现或改变研究判断时升级；先标 `SEEN / OPEN / PARKED`，再由本人预测、检查和解释推动状态变化。

### C. 进组应用层（单独的消费面）

`jinzu-sprint` 只管理 pitch、简历、T5、OE1 和可对外表达的证据。它消费 A/B 层已经核验的材料，不重新定义学习目标，也不把研究假设包装成已完成成果。对外表达显式区分 `PAPER-TEXT`、`USER-REPORTED`、`USER-INFERENCE`、`UNKNOWN`。

### D. 长期方向背景（不进入当前站序）

工业研究能力、开源技术资产、Agent/process/formal 邻接方向、团队生态地图和设备工作流只作为选择标准、远期研究出口或另行任务。除非形成具体依赖，不写进当前 EdgeIM 站点 PASS。

## 4. 每个学习节点的共同回路

```text
paper object/design
-> smallest hand example
-> alternative design or neighboring method
-> changed assumption / counterexample
-> prediction
-> check
-> verdict and claim ceiling
-> reconnect to the whole EdgeIM pipeline
```

这条回路是研究训练接口，不改变原站题面，也不允许 AI 代写用户答案或 Ledger。

## 5. 三个可选设计分支

### 分支 A（推荐）：主正本 + 研究邻域 + 应用层

继续使用 `MASTERY_GATE.md` 作为 EdgeIM 学习总入口，在其中明确三层关系；`FOUR_PAPER_TRAINING_LOOP.md` 负责三篇镜头的解锁；`jinzu-sprint.md` 只保留应用门。优点是改动集中、与现有冻结 OS 兼容、能直接回应“不是只做进组相关”。风险是总入口会承载较多边界说明，需要控制长度。

### 分支 B（扩展）：另建独立研究邻域正本

把研究邻域和长期工业能力另立 `research/map/` 下的路线正本，`MASTERY_GATE.md` 只保留学习门。优点是学习与研究地图更清楚；风险是增加第二套导航和同步成本，可能提前把地图做大，暂不作为本轮首选。

### 分支 C（最小）：只改入口指针

不重写计划结构，只在现有文件补一段“EdgeIM 主干 / 研究镜头 / 进组出口”的说明，保留当前 P0-P5 与 W0-W4。优点是风险最低；风险是无法充分吸收完整会话里对研究邻域和长期能力的要求，容易再次退回“面试门控”。

## 6. 暂定落盘范围

在新增桌面材料复核后，若没有相反证据，优先采用分支 A：

1. 更新 `MASTERY_GATE.md` 的目标层级、来源标签、研究回路和进组应用边界。
2. 更新 `BRIEF.md` 的入口说明与 Amendment，保留冻结站序和 PASS。
3. 更新 `FOUR_PAPER_TRAINING_LOOP.md` 的当前游标，避免旧 EX-00 游标与现行诊断冲突。
4. 更新 `jinzu-sprint.md` 与 `lu-side.md` 的镜像描述，明确进组是应用层，鲁线仍承载研究邻域。
5. 仅在镜像确有漂移时更新 `progress/CAMPAIGNS.md`、`progress/TODO.md`；不触碰暂停任务、答案、Ledger、实验代码或外部平台。
6. 用独立 task log 记录本窗口作者、来源文件、路径级改动和验证结果；不自动 commit/push。

## 7. 待新增材料回答的问题

- “紫占盘用途和科研菌丝网构想”里哪些是用户明确决策，哪些只是象征性/探索性设想？
- “杂谈”中哪些内容改变学习优先级、研究邻域边界或工业能力约束，哪些只保留为背景？
- 三份文件是否提出了新的主干、分枝、进组门或时间约束？若有，是否与冻结 OS、现有四论文解锁点冲突？
- 是否需要把“科研菌丝网”落成受控分枝状态模型，还是只作为研究地图的隐喻？
- 是否有任何新材料要求改变当前“月底、精确日期待定”的进组时间口径？

## 8. 初稿状态

本文件只完成初始设计记录。下一动作是保存三份桌面源文件的 provenance 并逐份阅读；读取结果追加到本文件的“修订记录”，再决定是否修改现行正本。

## 9. 新增设计分支：科研菌丝网的五层架构

用户提出的结构作为本初稿的 `DESIGN-BRANCH-MYCELIUM-01` 保存：

```text
WORLD / FIELD
        ↓
RESEARCH MAPS
        ↓
ACTIVE TRACKS
        ↓
EVIDENCE / PRACTICE
        ↓
ARTIFACTS

所有层都反向链接 SOURCES：论文、原始会话、网页、仓库、数据、原始证据。
```

初步判断：可以采用。它比固定树形目录更适合“从一个节点向外长、再重新连接”的学习方式，也能把 EdgeIM 学习主干放在 `ACTIVE TRACKS` 中，把四论文研究邻域放在 `RESEARCH MAPS` 与 `EVIDENCE / PRACTICE` 的连接处。

需要补上的两个横切约束：

1. `CLAIMS / GOVERNANCE` 横切所有层。每个节点都要有来源坐标、责任主体、状态（例如 `PAPER-TEXT`、`USER-REPORTED`、`USER-INFERENCE`、`UNKNOWN`、`OWNED`、`PARKED`）和更新时间；会话或地图不能直接升级成论文事实或本人能力。
2. `EVIDENCE / PRACTICE` 与 `ARTIFACTS` 必须能反向更新 `RESEARCH MAPS` 和 `ACTIVE TRACKS`。反例、失败实验、导师反馈或新来源可以让分支降级、改写 residual 或关闭一条路径；单向“地图指导行动”会失去科研反馈回路。

在 EdgeIM 计划中的暂定映射：

| 菌丝网层 | 当前对应物 | 本轮处理 |
|---|---|---|
| `WORLD / FIELD` | process discovery、formal methods、agent systems、工业研究生态 | 只作背景地图，不塞进站点 PASS |
| `RESEARCH MAPS` | `KNOWLEDGE_MAP`、`RESEARCH_MAPS`、四论文谱系和方法对照 | 受控开枝，按依赖/重复/研究杠杆升级 |
| `ACTIVE TRACKS` | EdgeIM 主干、sigRank/Ground Truth/CrossEdgeIM 解锁轨 | 保持当前站序和解锁门 |
| `EVIDENCE / PRACTICE` | 手算、最小实现、预测—检查—裁定、冷启动复测 | 只计本人新证据，不把 AI 输出计入 Ledger |
| `ARTIFACTS` | 研究笔记、比较卡、实验回执、可复用代码、进组材料 | 先过 claim ceiling，再决定是否公开或对外表达 |
| `SOURCES` | 论文原文、归档会话、网页、仓库、数据和原始输出 | 所有事实与判断必须可回溯 |

这条分支目前是研究系统设计输入，不自动取代现行 `MASTERY_GATE.md`、`BRIEF.md` 或项目卡。

## 修订记录

### 2026-09-06 · `REV-0.1`

- 用户新增五层 `WORLD / FIELD -> RESEARCH MAPS -> ACTIVE TRACKS -> EVIDENCE / PRACTICE -> ARTIFACTS` 结构，并要求所有层回链 `SOURCES`。
- 初步采纳；补充 `CLAIMS / GOVERNANCE` 横切层和证据/资产反哺地图的反向回路。
- 尚未据此改写现行正本，等待三份新增桌面材料的逐份复核。

### 2026-09-06 · REV-0.2 独立修订与历史勘误

- 新材料复核后的方案已单独落为 [TASK-004 独立修订稿](2026-09-06__research__edgeim-jinzu-reconstruction-TASK-004.md)。本文件初稿正文与 A/B/C 分支保留，不能把其中“暂定落盘范围”当当前授权。
- 更正历史：本窗口后来确实写入了共享学习入口和两张项目卡，部分新增记录最初误用 TASK-003，之后改为中央分配的 TASK-004。此前“尚未改写正本”只适用于早期时点。
- 用户五层图是设计征询；`CLAIMS / GOVERNANCE` 和证据反向更新是助手补充，未得到独立正式采纳。新稿保留五层，并把来源、安排与本人能力分开记录。
- 新稿补全英语训练、四论文与研究候选的依赖、进组材料证据要求和进组后反馈；六门跨全篇覆盖，不扩成每节点重复六套考试；一次诊断不直接标 OWNED。
- 论文先例、团队信息和 novelty 均保留待核验。S2 的学习/研究邻域内容已提炼，未因文件标题含命理而全盘忽略。
- 本次继续只修改本窗口五份独立文件；此前写入的共享增量没有自动撤回，邻窗产物没有被覆盖。详见任务回执。
