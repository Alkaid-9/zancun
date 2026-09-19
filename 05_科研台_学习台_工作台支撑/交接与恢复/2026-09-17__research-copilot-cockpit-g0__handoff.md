# 科研驾驶舱 G0 收口交接

日期：2026-09-17。任务：`TASK-20260916-009`。状态：`RECOVERABLE / G0-COMPLETE-WITH-OPEN-GATES / NO-PRODUCT-BUILD`。

## 0. 当前结论

TASK-008设计基线及TASK-009 G0事实／语义冻结已按阶段提交。G0只完成三仓事实、实际B合同依赖、需求／权威矩阵、跨仓内容身份与非原子读取规则、失败语义和开放项裁决；没有制作P1a页面或启动P1b、P2-P7。

## 1. 权威链

1. [G0冻结件](../decisions/two-desks-delta-20260914/RESEARCH_COPILOT_G0_FREEZE.md)：G0-A至G0-E事实、矩阵、语义和验收。
2. [驾驶舱方案](../decisions/two-desks-delta-20260914/RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md)：G0-P7及产品完成标准。
3. [独立复核](../decisions/two-desks-delta-20260914/_review/20260917_cockpit-g0-independent-review.md)：四轮发现、处置与最终SCOPED-READONLY PASS。
4. [TASK-009日志](../task_logs/2026/09/2026-09-16__research__research-copilot-cockpit-g0-freeze.md)：授权、阶段提交、测试和回滚。
5. [统一参考清单](../decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md)：R01-R12与I01；R12只作方法参考。

## 2. 已完成

- S0设计基线`c85bba4`；G0-A`7b545c6`；G0-B`695e0e3`；G0-C`2d7815e`；G0-D`e21c7e6`。G0-E限定commit由本交接所在提交固定。
- research-desk当前应用观察为`0b3a541`；B核心单测本轮6/6通过。旧B patch不再与当前整文件完全可逆，只作历史hunk归属证据。
- 新鲜度使用内容身份A/C/B比较和`NO-DRIFT-OBSERVED`，不宣称跨仓原子事务。
- 四轮同谱系只读复核最终`SCOPED-READONLY PASS`；未冒充异构或外部审。

## 3. 仍开放

- R11仍为`IDENTITY-OPEN / SCREENSHOT-ONLY`；未注册永久`research-desk` slug。
- A/B独立复核、真实用户试用、B合同采收、历史证据采收、EXR和C04-C07开放。
- WP0异构审、用户接受、精确采收、8899 loaded revision、部署和push开放。
- P1a/P1b与P2-P7均未启动；有效Skill运行回执源仍为MISSING，不能显示0。

## 4. 恢复第一动作与边界

先读本页和G0冻结件§5，再核MAS、research-desk、WP0的HEAD/index/worktree及8878/8899服务。不得从生成视图或聊天摘要推断当前状态，不得把service-up当loaded revision。

下一候选动作是用户在现有隔离DEMO完成一次5-10分钟真实路径观察。没有新的明确授权，不开始P1a；不修改应用、真实数据库、WP0、Skills、课程、sealed、答案或生成视图，不部署、不push。

## 5. 完成标准

G0已经完成但产品没有完成。后续只有在相应包另领task_id、合同冻结、测试／独立审／用户门按范围关闭并限定提交后，才能更新对应状态；本交接不代签任何后续门。

## 6. 试用后续更新

2026-09-17首次短试用收到用户反馈“没有保存”。8878日志只见GET、未见POST／PUT，当前标记`USER-TRIAL-RED / SAVE-NOT-REQUESTED / ROOT-CAUSE-OPEN`；不启动P1a。最新恢复入口改为[保存未发生交接](2026-09-17__research-copilot-user-trial-save-failure__handoff.md)。
