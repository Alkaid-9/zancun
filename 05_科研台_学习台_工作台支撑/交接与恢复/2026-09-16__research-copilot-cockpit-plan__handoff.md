# 科研项目驾驶舱方案：复核后恢复入口

日期：2026-09-16。任务：`TASK-20260916-008`。会话：`01a0aa0a-203a-7290-b7c8-be62c8f1f896`。

状态：`RECOVERABLE / DOC-ACCEPTED / DESIGN-RECONCILED / IMPLEMENTATION-NOT-AUTHORIZED / USER-DECISIONS-OPEN`。

## §0 TL;DR

驾驶舱详细方案及A-E复核对账已写盘；任务身份由作废草稿号004迁到已登记008。当前仍是设计，不授权G0、P1a／P1b、P2-P7、应用、数据、Skill、WP0、部署或push。

## §1 权威链

1. [当前方案](../decisions/two-desks-delta-20260914/RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md)：范围、G0-P7、阶段合同、测试和验收标准。
2. [主控复核对账](../decisions/two-desks-delta-20260914/_review/20260916_cockpit-review-controller-reconciliation.md)：A-E采纳、修正和证据坐标。
3. [原独立评论](../decisions/two-desks-delta-20260914/_review/20260916_fable5-independent-review.md)：保留自我更正与原始评论，不作决策正本。
4. [本任务日志](../task_logs/2026/09/2026-09-16__research__research-copilot-reference-integration-plan.md)：实际发生、检查与开放门。
5. [统一参考清单](../decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md)：R01-R11与I01身份、来源和证据上限。
6. [09-15两台总交接](2026-09-15__desks-window-current__handoff.md)：A/B、N3、用户试用、WP0和历史采收的上游现态。

## §2 已完成

- 会话恢复绑定已解析；`TASK-20260916-008`按发号器不可达兜底协议登记，INDEX保持原生CRLF。
- 方案已覆盖权威边界、八阶段、五门、G0-P7、检查／评审／验收、测试、回滚和完成标准。
- C04-C07真实定义及五个已点名Skills已复核；此前两项“0命中”误判保留撤回记录。
- A-E已回到实际B合同、实现、WP-S设计与CURRENT生成链核验；方案改为P1a静态验证、P1b条件升级。
- 原独立评论未被覆盖；主控另建对账层。
- 文档收口复验通过：8份设计链文档严格UTF-8，82个本地链接目标／锚点有效，空白／围栏／限定diff检查通过；task INDEX保持纯CRLF并以CAS只替换008行。

## §3 未完成与用户门

- R11仍为`IDENTITY-OPEN / SCREENSHOT-ONLY`。
- `research-desk`不是注册slug；是否立卡需用户决定，注册后不可改名。
- 实际B合同文件未跟踪，A/B独立复核与用户试用仍开放。
- G0、P1a／P1b、P2-P7均未启动；P5 kind／关系合同未冻结；有效Skill运行回执源未定义。
- WP0异构审、用户接受、精确采收、8899加载与push仍走原治理线。
- 本批尚未commit或push；生成视图未刷新，可能暂时仍显示旧004诊断，禁止手改生成物。

## §4 新窗口第一动作

1. 依次读本页§0-§5、当前方案§10和主控复核对账§2。
2. 在`/mnt/d/MyResearch/MAS_Safety_Project`重核HEAD、index/worktree及上述文件跟踪状态；不得按外层cwd或聊天摘要猜任务。
3. 先问用户两项：R11是否继续只按截图；是否要注册`research-desk`永久slug。
4. 若用户只批准设计续作，另领任务做G0，不修改应用；若批准P1a，也须等G0和现有DEMO短试用后再建静态验证件。

## §5 边界与完成标准

- 不把Skill目录、EVENTS引用、运行回执、技术通过、研究判断、独立评审和用户接受合并。
- 不新建第四套正本；静态页只能读现有正本并显示来源、版本、新鲜度和未知。
- 不手改`PROJECTS.md`等生成视图；共享INDEX只用`ledger_edit.py`＋CAS。
- 当前任务完成只需：身份一致、A-E对账落文、文档链接／格式／状态检查通过、恢复入口齐全。产品完成仍需后续实现和相应各门证据。
- 上述当前任务完成标准已经满足，任务状态为`completed_with_open_gates`；开放门不因文档任务收口而关闭。
- 撤回只审本任务hunk，不reset、stash、clean或覆盖其他窗口改动。

## §6 Git与运行边界

开工前快照：MAS `master@306cc2b3172c3504c23be913a97f518a707ea217`，index为空，相对本地`origin/master`为`+21/-0`（未fetch）；共享工作树有大量他窗改动。本任务未启动服务、未读写真实数据库、未运行应用测试、未部署、未push。
