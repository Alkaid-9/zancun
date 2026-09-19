# 窗口总交接：鲁侧进组补充计划与工作台／科研台／学习台

> 历史快照：当前恢复请读[TASK-019最新总交接](2026-09-15__desks-window-current__handoff.md)。下文“N0前/A/B未提交”为TASK-012时点，不是现态。

日期：2026-09-15。任务：`TASK-20260915-012`。会话：`01a09aa5-24c1-7233-868b-7426b5d94476`。

状态：`ARCHIVE-READY / IMPLEMENTATION-OPEN / USER-TRIAL-OPEN`。本页是窗口盘点与恢复入口，不是两台或课程全部验收通过的声明。文档检查、独立核验及最终commit见[本次任务日志](../task_logs/2026/09/2026-09-15__archive__lu-onboarding-and-desks-window.md)。

## 0. 用户要求、当前停点与恢复

最新指令要求先存档：进组新补充计划、工作台与科研台交接、工作总结/日志、已完成/未完成、进度与线路、架构/分工、下一步plan、使用/维护手册。本次先完成这些文档，不延续上一条讨论直接施工。

用户此前明确“继续推进，记得及时commit存档，不用总等我”：本次自有文档检查通过后限定commit，不自动push、不整树采收。对应用A/B的既有实施授权继续有效，但本存档不代签其用户试用；WP0异构审/接受/加载门不被通用commit许可取消。

新窗口顺序：本页 → [进组补充计划](../decisions/2026-09-15__research__lu-onboarding-supplement-next-plan.md) → [下一批执行方案](../decisions/two-desks-delta-20260914/NEXT_EXECUTION_PLAN.md) → 对应实现任务/实际合同/回执 → 仓库和服务实况。不要从外层cwd、聊天摘要、旧“未授权”标题或最近一个commit推断任务。

第一安全动作：核MAS、research-desk、WP0隔离树的Git根/HEAD/index/worktree，确认接着做哪一条已授权包；只读现有材料，不打开sealed、不启动实验、不重启8899。现在停在N0开工核对前，晚间4–5h只是建议工作预算，用户实际截止时间未知。

## 1. 本批归档清单

| 文件 | 内容/权威范围 |
|---|---|
| 本页 | 窗口总结、所属线、来源账、当前状态、未完项与分线交接 |
| [进组补充计划](../decisions/2026-09-15__research__lu-onboarding-supplement-next-plan.md) | 新讨论的增量、学习/研究/进组材料三层接续、具体下一步、验收与待裁定项；尚未实施 |
| [下一批执行方案](../decisions/two-desks-delta-20260914/NEXT_EXECUTION_PLAN.md) | N0–N5依赖、步骤、分工/写域、测试、评审、工期风险和缩减策略 |
| [架构说明](../runbooks/lu-onboarding-and-desks-architecture.md) | 现有与目标架构、三台职责、多层关系、数据/仓库权威、已实现接口与设计差异 |
| [使用手册](../runbooks/lu-onboarding-and-desks-user-guide.md) | 现有A/B安全试用路线、进组入口、工作台当前限制及故障辨别 |
| [维护手册](../runbooks/lu-onboarding-and-desks-maintenance.md) | 环境、启动/停止、复验、数据备份边界、分仓提交、恢复/撤回与日志维护 |
| [本次任务日志](../task_logs/2026/09/2026-09-15__archive__lu-onboarding-and-desks-window.md) | 本次操作与检查、错误/修正、实际提交结果；不充当活的操作手册 |

另更新两台设计README、handoff INDEX和task INDEX的本次路由。其余设计与原始资料只引用，不复制成第二正本。本包是文档存档，不是含应用、原始材料、数据库和所有历史回执的可独立运行镜像。

## 2. 属于哪条线，谁负责

| 工作 | 归属 | 当前事实的主要落点 | 边界 |
|---|---|---|---|
| 进组材料与表达 | outreach / `jinzu-sprint` | [进组路由卡](../projects/jinzu-sprint.md)及其技术材料消费者 | 只消费已有真实证据，不用材料压力反推本人已掌握 |
| 鲁侧论文、基础、研究邻域、toy | research / `lu-side` | [鲁侧卡](../projects/lu-side.md)、学习合同、研究产物 | 近期主轴；孙侧与毕业后工业/OAI仅中长期导向 |
| 科研台、学习台、多层网入口 | `research-desk` | [两台入口](../decisions/two-desks-delta-20260914/README.md)、应用A/B任务 | 工具支持不等于正式知识内容或学习效果完成 |
| 任务协调与执行接续 | maintenance / `dashboard-v3`，topic `workbench-v2` | [WP0交接](2026-09-01__workbench-v2-wp0-codex-execution__handoff.md) | 不替代研究判断与个人能力评价；仍有独立接入门 |
| ownership-v3课程补修 | learning / `lu-side` | [三缺口交接](2026-09-15__ownership-v3-three-gaps-remediation__handoff.md) | 课程写域、QA与用户能力分开，不由参考工具评估关闭 |
| 一苇渡江参考采集 | 学习资料支线；另窗执行 | [集中交接](../../learning/resources/yiwei-dujiang-2027-reference-20260915/HANDOFF.md) | 本人28届/2027-12；来源27届/2026-12，不照搬年份 |

主线程负责整合、文档/获准代码修改、限定提交与最终复核。最多一个只读子代理用于定向检索或独立核验，不派生、不写文件。用户负责真实学习、关键取舍和用户验收；他窗任务/课程写域不由本窗接管。WP0要求的Claude异构复审与普通同模型只读核验不同。

## 3. 工作总结与可追溯时间线

| 阶段/任务 | 已发生的工作 | 原记录与限制 |
|---|---|---|
| 09-14 / TASK-001 | App讨论、鲁→孙→工业/OAI阶段导向、多层网、四科、目标三档、toy边界暂定归档 | [原交接](2026-09-14__lu-learning-multilayer-toy-discussion__pause-handoff.md)；不新增本人PASS |
| 09-14 / TASK-002 | 两台增量设计、九项场景对照、A/B方案与B接口提案 | [设计入口](../decisions/two-desks-delta-20260914/README.md)；旧“未授权”仅指交付当时 |
| 09-15 / TASK-002 | 用户“施工A”后，来源全集检索、保存中/成功/不确定状态、重复点击与草稿保留 | [A任务](../task_logs/2026/09/2026-09-15__implementation__two-desks-a-source-save.md)、[A回执](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/RECEIPT.md) |
| 09-15 / TASK-004 | 用户“B启动”后，目标三档、版本化尝试反馈、一次研究补学往返、独立判断与选择导出 | [B任务](../task_logs/2026/09/2026-09-15__implementation__two-desks-b-goals-return.md)、[B回执](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/RECEIPT.md) |
| 09-15 / TASK-008/009 | 三次用户参考输入及I01集中为11项，写六阶段融入计划与标准 | [唯一清单](../decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md)、[融入计划](../decisions/two-desks-delta-20260914/REFERENCE_INTEGRATION_PLAN.md) |
| 09-15 / TASK-010/011 | 同场景比较ThoughtDAG/两个TreeTalk、PlanWeave/工程方法；限定发送/定位链续核；原段摘录窄合同 | [评估](../decisions/two-desks-delta-20260914/REFERENCE_EVALUATION.md)、[TASK-011](../task_logs/2026/09/2026-09-15__research__reference-followup-and-scoped-archive.md)；均非软件实测/安装 |
| 09-15 / 本次 | 总体状态核对、晚间建议、完整窗口归档与手册 | 最新用户要求先存档，后续施工尚未进行 |

他窗09-15 TASK-003已将09-20/09-25冻结日改为条件触发；TASK-005/007留下课程三缺口方案及部分核验。本包承接这些事实，不把它们记成本窗口实现。WP0是09-01隔离施工，亦非本次新完成功能。

## 4. 当前进度与证据上限

| 面 | 已完成 | 未完成/不能声称 |
|---|---|---|
| 进组计划 | 路线、能力门、四论文全文长期目标、冻结日条件化有文档 | 路由卡尚未接新状态；个人证据需定向核对，不能沿09-06旧游标断言今天仍未学习 |
| A | 完整可选来源集合检索和首次保存反馈 | 非全文件全文语义搜索；真实用户复验开放 |
| B | 同知识按目标分最低/正常/长期要求，版本化尝试/反馈，一次分支返回，两类评价，v2选择导出 | 非四科内容填齐、完整C06、多层网络或复杂嵌套全部实现 |
| RD-2 C00–C03 | 历史主控回执/现有A/B回归承接其底座 | C03 AC03-12用户门仍开放；C04/C05/C07尚未交付，C06仅B有界部分 |
| WP0 | 历史A–E技术/主控通过，代码及证据仍在隔离树 | 异构审、用户接受、精确采收、服务加载未确认关闭；不代表整个工作台v2完成 |
| 多层网络 | 内容版图、三台分工及局部记录能力有设计/实现 | 跨层依据、影响复核、复杂过程继承及正式内容仍需建设；不是单层加筛选 |
| 课程 | ownership-v3资产在f9f42db，目录相对HEAD无差分；I01有部分抽样 | 总表QA-PASS与8模块QA-PENDING未对齐；rubric NOT-FROZEN；无正式controller验收新文件 |
| 参考融入 | 11项有处置、关键机制静态核对和摘录窄合同 | EXR-01–10未运行；未安装工具、模型接入、同步或真实样本采用 |
| 一苇渡江 | 集中目录当前仅核见HANDOFF.md | 未确认另窗下载结果，不可报告完整本地复刻 |

### 测试如何读

[B回执§3](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/RECEIPT.md:33)记录浏览器27/27、后端28/28、A回归38/38、C03回归22/22；均为历史合成DEMO实跑，本存档没有重跑。C03同库二跑失败后换新隔离根的过程保留在FAILURES，不把新通过覆盖掉旧失败。

[WP0交接§2](2026-09-01__workbench-v2-wp0-codex-execution__handoff.md:64)记录taskstore138、dashboard490等历史结果；本轮未复跑，不可声称今天套件全绿。既往代理429/连接失败没有有效独立结果，不给它们签名。存档文档检查另记，不和上述数目加总。

## 5. Git、运行和数据快照

核对日期2026-09-15；恢复时重读，不能当永久状态。

| 仓库 | 分支/开工HEAD | 当前需保留的内容 |
|---|---|---|
| `/mnt/d/MyResearch/MAS_Safety_Project` | master / `4a4c7a97336c2b8fb880d1fc9759a707b453109a` | 共享脏树；本批只采收自己的七文档与三个路由增量 |
| `/mnt/d/MyResearch/research-desk` | main / `d53d188faff8e64ae9d22d92dd1eeab1b8309b84` | A/B六处已跟踪修改，新增b.js/测试/acceptance；未commit |
| `/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901` | `codex/wb2-wp0-20260901-root` / `02da69bfd54f5a2fdfb70b6ae085c1178bfea43e` | 复合工作树；taskstore和回执未跟踪，其他旧改动不能一并采收 |

前序文档commit：`ac87186`（14路径设计/参考checkpoint）、`4a4c7a9`（8路径摘录合同与续评）。开工相对本地origin/master为0 behind/16 ahead，未fetch、未push。本批最终commit见任务Git记录；不要把这里的开工HEAD当收尾HEAD。

本次ss在8873/8877/8878/8883/8899未见监听，同时allocator HTTP成功签发TASK-012；观察不一致详见任务日志，服务持续状态未确定。没有启动/停止服务、加载WP0或改真实数据库。不要靠端口/目录名判断已部署或数据可删。

## 6. 分线未完成项与下一动作

| 线/交付 | 下一步与完成标准 | 前置/阻塞 |
|---|---|---|
| 进组执行版 | 按补充计划把“证据→下一动作→验收→材料消费者”落到现有入口，路由一致 | 先核本人最新证据；不得强制重做旧已完成站点 |
| 课程独立QA | 完成B-EVAL/CrossEdgeIM可执行性检查，产出AC-01–10逐项详细回执 | 已有抽样非全包通过；新复核读sealed仍须遵守原写域/暴露规则 |
| 研究出口 | 建立Transfer Card桥接与实际consumer检查，保留DROP/PARK/PROMOTE | 原交接“方案A已选定/等待批准”矛盾需先核授权；不代填结论 |
| 跨论文接线 | 核原文锚点后按原合同接入 | TASK-20260906-004 INDEX=`completed_with_open_gates`，日志=`in_progress`，本包不裁定 |
| 早期教学缺口 | 完整IM/过程树/Petri net/soundness链、四篇各30分钟连续追问、跨四篇D2、EX-05卡点及App/CLI交接 | I01三缺口不能自动覆盖这些；暂无新的关闭证据 |
| A/B收口 | 差分归属→新隔离回归→修阻断→应用限定commit→一次用户试用 | 用户试用与独立审查分别保持状态；不接真实库 |
| 工作台接续 | 先核WP0外部门及接口；有条件时做一条request→产物→验收→原问题的真实接续 | 若硬门未闭，只交人工接续，标明自动接驳未完成；不改M4默认warn |
| 参考新功能 | 原段摘录窄合同明确后按EXR-01–10施工 | 仅设计完成；PDF/OCR/复杂分支不顺带扩大 |
| 享做/OpenScience | 补设备/版本/真实导出样本；两OpenScience唯一地址 | 只阻塞对应候选，不阻塞A/B收口 |

`CONTROLLER_ACCEPTANCE.md`预定路径（ownership-v3-controller-acceptance）和`TRANSFER_CARD_BRIDGE.md`本轮未核见实体，不写成已交。四篇全部数字尚未逐项重算。

## 7. 恢复完成、停止与撤回

存档验收：七份文档齐全、来源可追、状态不越界、使用命令有真实来源、登记可定位、Git限定提交。产品验收另走各合同，用户实际学习/试用与异构审不能被文档检查替代。

恢复遇到共享写域或权限冲突时，只停依赖该冲突的包，列准确文件/条款，不扩大为整个任务都无法推进。未经允许不清理历史验收根、不覆写原件、不推送、不替用户联系导师；新选题/novelty/个人能力结论不代签。

撤回本次仅限新文档及三条路由增量；先核后续变化，再审阅式撤回指定hunk。本包未改应用/课程/WP0，不能为了撤回文档去reset任何工作树。
