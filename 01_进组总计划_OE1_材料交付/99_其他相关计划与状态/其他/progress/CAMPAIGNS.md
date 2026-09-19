# CAMPAIGNS

B+ 战役 registry overlay（人工手改真相源；采集器只读，自动生成视图不回写本文件）。
格式冻结：`progress/audits/2026/08/dashboard-task-module-design/04_UNIFIED_BPLUS_DESIGN.md` §3.1 固定五 section；
契约：`progress/decisions/2026-08-18__maintenance__dashboard-task-module-bplus-contract.md`。

规则速记：

- 实体 ID 必须显式登记（CMP-*）；禁止从标题、窗口名、分支名或路径推断战役归属。
- lifecycle 只允许 planned / active / closed / archived；stale、zombie、conflict 是诊断风险标记，不是状态值。
- 空单元格留空即解析为 null；歧义活动宁可不登记（登记不了就进 bplus.unlinked_activity 诊断）。

## Campaigns
id | name | objective | line | branch | lifecycle | next_action | next_actor | progress_note | updated_at | resume_route_id
|---|---|---|---|---|---|---|---|---|---|---|
| CMP-BPLUS-IMPLEMENTATION | 看板 B+ 任务模块实施 | 按 I00-I90 计划逐 issue 只读增强看板 | infra | master | active | 实施 I20 并逐 issue 推进至 I90 | ai | 四块执行窗 TASK-20260821-001 块③；I00=c29dafc I10=d878a82 | 2026-08-22 | |
| CMP-LU-FINISHING-WAVE | 鲁线补齐波 | 产出五缺件并 T-B 收口 | research | master | active | T-B 收尾+§6 五门验收 | ai | 五件 00:21-00:46 全落盘；HANDOFF-20260816 手册 | 2026-08-22 | |
| CMP-OE1-EMAIL | OE1 九月致鲁老师邮件定稿 | v4 定稿零占位符并备投递检查单 | outreach | master | active | 等用户提供占位符真实信息后定稿 | user | 死线 2026-08-25；素材三句已备(EDGEIM_T2_bridge §5)（08-26 用户核实死线滑线，改期待定） | 2026-08-26 | |
| CMP-JINZU | 鲁线进组冲刺 | 2026 年 9 月底进组前消费 EdgeIM 学习主干与研究邻域证据，收口材料（精确日期待定） | research | master | active | 下一学习窗口先做 Whole-Paper Diagnostic 15 题；研究邻域按解锁门推进，材料只消费已核验证据 | mixed | 09-06 用户报告 EdgeIM 已过 EX-03；新入口为 MASTERY_GATE v2.1，月底为软边界；进组是应用出口，不定义学习主干；成员名单仍只从项目卡 campaigns 标签扫出（TASK-20260906-004） | 2026-09-06 | |

## Gate supplements
id | campaign_id | unlocks | est_minutes | estimate_source | estimate_confidence | blocking_scope | completion_authority
|---|---|---|---|---|---|---|---|

## Presence registry
id | title | campaign_id | state | unlocks | est_minutes | estimate_source | estimate_confidence | blocking_scope | completion_authority | done_count | total_count | root_id | path | anchor
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Milestones
id | campaign_id | title | kind | state | hardness | start_at | due_at | end_at | time_precision | timezone | rrule | trigger_ref | related_task_id | completed_at
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MS-JINZU-ENTRY | CMP-JINZU | 鲁法明实验室进组日（预计 2026 年 9 月底，精确日期待定） | trigger | open | hard | | | | unknown | | | {"kind":"external","id":"jinzu-entry-date-confirmed","state":"open"} | | |
| MS-OE1-DEADLINE | CMP-OE1-EMAIL | OE1 定稿节点（旧 2026-08-25 已滑线，新日期待定） | trigger | open | hard | | | | unknown | | | {"kind":"external","id":"oe1-deadline-confirmed","state":"open"} | | |

## Routes
id | campaign_id | kind | root_id | path | anchor | as_of
|---|---|---|---|---|---|---|
