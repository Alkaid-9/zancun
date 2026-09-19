---
id: TASK-20260915-017
title: 两台A/B独立代码复核与隔离用户试用准备
date: 2026-09-15
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 托管会话未提供可核实有效effort；仅交互式有界工作
  launch: 用户交互续作
type: implementation
status: completed_with_open_gates
area: research-desk / workbench-v2
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/task_logs/2026/09/2026-09-15__implementation__desks-n2-closeout-and-workbench-link.md
---

# 目标与授权

用户在TASK-013收口后要求“继续？”。继续已授权两台质量收口与N4准备，不自动批准原段摘录新合同、部署、WP0接入或研究实验。总并发2：主线程唯一写入者，一个只读代理核已提交A/B。进组/课程由另一窗口负责。

# 计划、写域与基线

1. 只读复核d53d188→b54ea71的A/B代码，发现沿出处核验；修合同内缺陷才做相应回归。
2. 应用acceptance/user-trial-TASK-20260915-017建立独立DEMO配置、两份合成文本及登记，不引用旧验收数据库或真实资料。用原服务验证启动/读取；给最短用户路线，不代填用户反馈或能力证据。
3. 回执/任务/入口与本任务INDEX行限定提交。应用基线c86f6d1，MAS基线828db25，两仓暂存为空；solver预检通过，TASK-017由allocator签发。

# 当前状态

新试用准备完成，ENV-READY / USER-OPEN / INDEPENDENT-REVIEW-OPEN。2份合成原件和登记与旧验收/真库隔离；通过原服务读取两来源，工作区数0，无个人成绩或研究结论。首页Playwright检查无JS错误，主线程目视截图；临时服务25976已终止，末次8878无监听，未部署。来源revision_id为空，不伪造已扫描版本。

只读代理ab_acceptance_review最终因429 exceeded retry limit失败，没有有效审查结果；不能算独立核验通过，也不能报告“未发现缺陷”。主线程没有冒名代签或宣称本轮已全审A/B。不重试、不增加代理并发，不把失败扩大成新试用准备无法完成。

入口：[新试用README](/mnt/d/MyResearch/research-desk/acceptance/user-trial-TASK-20260915-017/README.md)，含显式启动/停止、5–10分钟路线、反馈方式及数据边界。本轮只准备容器和DEMO，没有新增产品功能、未复跑全套A/B。此前c86f6d1的技术回执继续有效，独立验收/用户门不变。

# 尚未完成与下一步

下一步用户按新README实际操作并反馈卡点；据真实反馈修缺陷、保留其记录版本。独立A/B代码复审仍待有效审查者，429不算证据；如后续恢复，优先分小范围，不重复派发整个A/B。未确认的摘录、自动桥、C04–C07不默认开工。进组/课程由另一窗口继续。

# 验收与归档

准备检查：显式solver预检通过；新配置指向本任务根；catalog=2，source读取=2，workspaces=0，页面errors=[]。只发生服务初始化的新DEMO数据库写入，没有POST创建学习/研究记录；不修改真实registry。应用12个限定路径（配置/2原件/小型登记/说明/截图）已提交0b3a54178e4ec58fb96eb8570101c44d94ac5687，data/exports/runtime/logs不采收不删除。文档checkpoint用本文件git log定位。JSON/UTF-8/暂存空白检查通过，不push。

# 风险与恢复

不改默认config.local.json、不读sealed/答案、不迁移真库、不push/部署；8878冲突时不杀未知进程。所有测试/试用数据留本任务新根，不清理旧根。shared INDEX用CAS保CRLF，只采收本任务行。
