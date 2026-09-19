# 两台与工作台窗口：最新存档及断电恢复入口

日期：2026-09-15。TASK-20260915-019。会话：`01a09aa5-24c1-7233-868b-7426b5d94476`。

## 当前状态

`RECOVERABLE / ARCHIVE-PARTIAL / USER-OPEN / INDEPENDENT-AB-REVIEW-OPEN`。
本次用户要求全面检查并落盘窗口总结、日志、设计、分工、计划、使用与维护手册，随后告知即将没电。优先保存可恢复状态并限定提交；旧证据全量采收留作未完成，不以紧急存档冒充整包验收。

此页替代[TASK-012旧总交接](2026-09-15__lu-onboarding-and-desks-window__handoff.md)作为当前入口；旧档保留其历史事实。工作日志见[TASK-019](../task_logs/2026/09/2026-09-15__archive__desks-window-current.md)。

## 1. 恢复顺序与唯一第一动作

1. 读本页，再读[下一步执行计划](../decisions/two-desks-delta-20260914/NEXT_EXECUTION_PLAN.md)、[TASK-017](../task_logs/2026/09/2026-09-15__implementation__desks-ab-review-and-user-trial.md)。
2. 显式在 `/mnt/d/MyResearch/MAS_Safety_Project` 核Git根、HEAD、暂存与工作树，再分别核research-desk、WP0隔离树；不可按外层cwd或聊天摘要猜任务。
3. 文档补档先核本任务实际commit与下述未采收项；产品继续时先按新试用README完成一次真实短试用，或在用户不在时做有界独立A/B复核。两者都不能由本主线程代签。
4. 旧会话binding曾因外层cwd触发wrong_repo；本次显式MAS cwd验证为VERIFIED并重开TASK-017正本。收尾绑定改到本页；未加载WP0、未重启服务。

## 2. 线路、分工与长期约束

| 线 | 已有职责/产物 | 谁接着做及边界 |
|---|---|---|
| research-desk 科研台/学习台 | 来源、问题、目标要求、尝试反馈、版本与补学返回 | 本窗口维护代码与手册；用户实际操作、判断与学习证据不代填 |
| workbench-v2 / dashboard-v3 | 人工交接引用、任务正本、产物与验收回链 | 本窗只交N3人工切片；WP0由其原治理线办理异构审/接受/采收/加载 |
| lu-side / jinzu-sprint | 鲁侧训练、课程补修与进组材料消费者 | 用户已分配另一个窗口，本窗仅引用观察，不接管ownership-v3或路由卡 |
| 多层知识/科研网络 | 内容、目标、认识、实践与执行分层 | 已有设计和有界容器，完整内容与跨层语义仍未建齐 |
| 参考吸收 | 统一11项清单、分类标准、静态比较、摘录提案 | 沿现有计划按需推进，不默认安装外部工具 |
| 一苇渡江 | 本窗已交采集交接 | 另窗下载；本轮未核完整下载结果 |

总并发≤2；主线程唯一写入/整合者，至多一个只读子代理，fork_turns=none，不派生。当前紧急收口不再派发代理。近期鲁老师→升学后希望孙老师实验室→两年后工业/OAI是阶段导向，不默认添加近期小模型课。考研数三、英一、统计学、数据结构；2027-12初试，用户要求2027-09中旬前结束自己的积累阶段；来源27届2026-12只作参考。经济学不加入当前建设范围，具体时间百分比未恢复不编造。

## 3. 已完成工作与证据时间线

| 任务/阶段 | 已完成 | 证据与提交 |
|---|---|---|
| 09-14 TASK-001/002 | 多层内容暂定、三档要求；两台增量设计、九场景、首批A/B方案 | [旧讨论交接](2026-09-14__lu-learning-multilayer-toy-discussion__pause-handoff.md)、[设计入口](../decisions/two-desks-delta-20260914/README.md)；部分基础文件仍未跟踪 |
| 09-15 TASK-002/004 | A来源全集选择检索/保存反馈；B目标要求、版本化尝试反馈、研究补学往返与选择导出 | [A日志](../task_logs/2026/09/2026-09-15__implementation__two-desks-a-source-save.md)、[B日志](../task_logs/2026/09/2026-09-15__implementation__two-desks-b-goals-return.md)；应用 `b54ea71`已采收代码 |
| TASK-008–011 | 三次参考集中为11项；六阶段融入方案、静态比较、原段摘录窄合同EXR-01–10 | [清单](../decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md)、[融入计划](../decisions/two-desks-delta-20260914/REFERENCE_INTEGRATION_PLAN.md)、[评估](../decisions/two-desks-delta-20260914/REFERENCE_EVALUATION.md)；MAS `ac87186`、`4a4c7a9` |
| TASK-012 | 原窗口总结、进组补充计划、下一步及三份手册 | MAS `b1e2f1a`；本次修正其中滞后入口，不改进组正本 |
| TASK-013 N2/N3 | 新隔离复验、限定A/B提交；人工交接、普通note保存、workspace/view/record身份返回 | 应用 `c86f6d1`；MAS `828db25`；[N3回执](/mnt/d/MyResearch/research-desk/acceptance/n3-TASK-20260915-013/RECEIPT.md) |
| TASK-017 | 两份合成来源、新隔离试用配置/登记/README；原API读取和首页检查 | 应用 `0b3a541`；MAS `18e4183`；[新试用入口](/mnt/d/MyResearch/research-desk/acceptance/user-trial-TASK-20260915-017/README.md) |
| TASK-019 本次 | 恢复核验、当前盘点、断电交接、手册/计划现态修正、限定存档 | 本任务日志及其git log；不新增产品功能或运行实验 |

历史技术结果：N3最终20/20，后端28/28，B27/27，A38/38，C0322/22，详见N3回执与各报告；本次文档收口未重跑，不能写成“本轮测试全部通过”。N3独立静态审三项发现已修复，保留两次RED与最终结果；完整A/B独立审因429无有效结果，仍OPEN，不等于没有缺陷。C03 AC03-12及真实用户试用仍开放。

## 4. 三仓与运行快照

2026-09-15本轮开工核验，恢复时需刷新：

| 仓库 | 分支/HEAD | 工作树/远程 |
|---|---|---|
| MAS_Safety_Project | master / `18e418302fea2df34abba08b4f2dc0dec2a4a11e` | index空，共享大量他窗改动；相对本地origin/master 0 behind/19 ahead，未fetch |
| research-desk | main / `0b3a54178e4ec58fb96eb8570101c44d94ac5687` | 已跟踪文件/index干净；历史acceptance有未跟踪文件；无remote |
| MAS_Safety_Project-wb2-wp0-20260901 | `02da69bfd54f5a2fdfb70b6ae085c1178bfea43e` | 先前本轮检查index空、33个已跟踪修改；复合隔离树未采收，本次不动 |

solver预检通过。本次8878无监听，未启动/停止常驻服务、未部署、未push。上述HEAD是归档前快照；本次文档提交号用 `git log -1 --format='%H' -- progress/handoff/2026-09-15__desks-window-current__handoff.md` 定位。

## 5. 未完成、触发条件与完成标准

| 项目 | 当前未完成 | 下一动作/通过标准 |
|---|---|---|
| 真实使用 | USER-OPEN，未代填观察 | 按TASK-017新DEMO用5–10分钟，记录卡点/版本/丢稿或错返；修复后相关回归，用户确认 |
| A/B独立QA | 429无有效审查结果 | 按实际合同分小范围只读复核，产出file:line、覆盖与未查面；发现逐项闭环 |
| WP0自动桥 | N3仅MANUAL-ONLY；AUTO-BRIDGE-OPEN | 原异构审、接受、精确采收及服务加载条件先闭；另列窄接口合同，不绕建第二任务库 |
| 完整多层网络 | 容器不等于内容/语义完成 | 用真实问题检验来源→知识→方法→产物→研究判断/个人证据，分层保留依据；不预填掌握 |
| 摘录/后续模块 | EXR未施工，C04–C07未整体交付 | 沿[SOURCE_EXCERPT_PROPOSAL](../decisions/two-desks-delta-20260914/SOURCE_EXCERPT_PROPOSAL.md)按授权启动，执行EXR-01–10；PDF/OCR/复杂嵌套另议 |
| 课程/进组 | 他窗进行，不是本窗完成 | 以其当前日志/验收为准；TASK-018已更正TASK-20260906-004状态为in_progress，解除该项前置冲突不等于跨论文接线已完成 |
| 归档完整采收 | 本次电量不足，未完成历史文件逐项采收 | 按§6核归属/内容/引用后分别限定提交；不改写历史回执为新验收 |

## 6. 尚未纳入本次Git的实体与恢复限制

以下已在本地，尚未整体采收；停电不会自动删这些文件，但Git克隆不能替代本机保留：

- 应用 `acceptance/a-TASK-20260915-002/RECEIPT.md`；`acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md`、`RECEIPT.md`、`RUN_CHECKS.md`、`FAILURES.md`及相关patch/before/历史报告，仍需核归属与敏感内容再提交。
- MAS 09-14两份 `multilayer-*` 基础决策、讨论交接/日志，09-15 A/B原任务日志，一苇渡江HANDOFF及采集交接日志仍有未跟踪实体。后续只采收本窗口确有归属文件，不采收整个resources或其他窗口课程/进组树。
- N2/N3合成content、对象库、导出、runtime/logs和用户试用data留本地。已有源码/报告提交不构成运行现场全备份；TASK-017两原件/登记/配置可从Git恢复，但后续用户数据不可。
- 禁止复制真实学习答案、密封材料、数据库、桌面完整对话或无关原件进入Git来凑“全部存档”；需要数据备份时先定范围，按SQLite一致快照/受控停写办理。

## 7. 设计、操作与维护正本

- [架构说明](../runbooks/lu-onboarding-and-desks-architecture.md)：三台分工、多层网络、权威对象/数据位置、当前与目标接口。
- [使用手册](../runbooks/lu-onboarding-and-desks-user-guide.md)：新隔离DEMO启动、最短学习科研往返、人工接续、停止与反馈。
- [维护手册](../runbooks/lu-onboarding-and-desks-maintenance.md)：环境、配置/数据根、复验、备份、分仓提交、故障与撤回。
- [执行计划](../decisions/two-desks-delta-20260914/NEXT_EXECUTION_PLAN.md)：N0–N5现态、下一批、写域/分工、标准与测试。

本次文档检查与提交在任务日志记录。无独立归档审查，不将主线程自查冒名为独立接受。共享INDEX只改本窗口行并保原生行尾；不手改生成视图、不清理脏树。撤回只审阅本任务文档hunk，不reset任何仓、不删除历史数据。
