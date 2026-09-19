---
id: TASK-20260915-013
title: 科研台A/B收口与工作台接续推进（进组线另窗）
date: 2026-09-15
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 当前托管会话未给出可核实的有效effort
  launch: 用户交互式分包实施
type: implementation
status: completed_with_open_gates
area: research-desk / workbench-v2
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/NEXT_EXECUTION_PLAN.md
  - progress/handoff/2026-09-15__lu-onboarding-and-desks-window__handoff.md
---

# 目标与授权

用户在存档b1e2f1a后明确“你这边继续做工作台、科研台，我去另一个窗口继续进组计划的完成”，随后把本窗并发改为2。采用N0/N2/N3/N5推进；N1及进组计划/课程内容由另一窗口处理，本窗不修改。已有及时commit许可生效；不push、不迁移真库、不代签用户试用或WP0外部门。

# 计划、写域与基线

1. N2：核既有A/B代码归属，在新的合成根复跑B/A/C03与后端；修实际阻断后限定应用commit，用户/独立验收分别保留。
2. N3：核WP0实际合同/隔离实现/外部门，确定可落地的任务接续切片；不得用两个GET推造写接口，不绕过异构审/采收/加载门。
3. 更新本任务、两台入口/回执和本任务INDEX行，按小包提交；不改进组计划、jinzu/lu-side路由卡、学习答案、sealed、ownership-v3及他窗状态冲突。

应用 `main@d53d188faff8e64ae9d22d92dd1eeab1b8309b84`；6处既有文件变更与A/B新增代码/测试/回执是前序本窗产物，未提交。MAS开工 `master@b1e2f1adbbb27e2dd25deca8436eca8b6d9acfd9`，暂存为空。solver预检通过，TASK-013由中央allocator签发。

N2新验收根：`/mnt/d/MyResearch/research-desk/acceptance/n2-TASK-20260915-013/`，独立content及B/A/C03数据/导出/runtime/logs；端口候选8878，测试依次运行。复用原脚本，只在启动脚本的进程内显式指定允许的验收根，不改旧断言或旧现场。

# 验收与证据

- N2新隔离根实际后端28/28（2.459s）、B浏览器27/27、A38/38、C0322/22全部通过；JS语法/diff空白/B patch reverse check通过。主线程目视本轮B窄屏与返回桌面；无产品返修。应用限定20路径commit=`b54ea71`，源码/测试及本次配置、3报告、2截图；未采收旧验收全目录/合成原件/数据库，未push。
- N2回执：`/mnt/d/MyResearch/research-desk/acceptance/n2-TASK-20260915-013/RECEIPT.md`。历史A/B用户门和独立代码复核仍OPEN；本轮通过数来自新run，不复用旧数。
- 唯一只读子代理workbench_link_readonly有效终态complete；主线程抽查共享http.py及隔离Task字段/writer/events。详情见`progress/decisions/two-desks-delta-20260914/WORKBENCH_LINK_REVIEW.md`，仅属接口边界独立核验，不是WP0异构审或A/B独立验收。
- N3按已有普通note＋同源身份链接实现人工交接面板，不改服务/Task schema。实际范围先落于应用`acceptance/n3-TASK-20260915-013/CONTRACT.md`，M1–M7验证在新合成根执行中；不声称自动派发。

# 当前状态

N0/N2/N3人工切片/N5本批实现与归档收口。N2应用commit=b54ea71；N3应用commit=c86f6d13efc8a93542bc7577cbe5ef01cc722419（24个限定路径）。专项最终20/20，后端28/28（2.102s）、B27/27、A38/38、C0322/22，语法/空白与窄屏目视通过；独立静态三发现修复闭环。状态为MANUAL-ONLY / USER-OPEN / AUTO-BRIDGE-OPEN，不等于三台全完工。未push、未部署、未研究实验。

恢复顺序：本节→应用[N3回执](/mnt/d/MyResearch/research-desk/acceptance/n3-TASK-20260915-013/RECEIPT.md)及[复验命令](/mnt/d/MyResearch/research-desk/acceptance/n3-TASK-20260915-013/RUN_CHECKS.md)→[接口/审查回执](../../../decisions/two-desks-delta-20260914/WORKBENCH_LINK_REVIEW.md)→[下一批计划](../../../decisions/two-desks-delta-20260914/NEXT_EXECUTION_PLAN.md)。先核两仓HEAD/暂存/工作树，不从外层cwd、旧存档或自动摘要推断任务；进组、课程仍归另窗。

N3复核过程：初始16/16后发现旧revision与旧继续点；RED 2/3复现前者，修后18/18。再审发现面板打开后改正文可复制，第二RED 6/7复现；集中检查脏稿并阻断copy/save后20/20。最后只读终态complete确认三项收敛，不冒称代理亲自实跑、WP0异构审或A/B全审。旧失败/中间报告都保留。

最终合成实例：workspace=obj_6badd58292f0456fafff0ac8c81058c0，view=view_a72cfbfc5b7148bea70e35b93c820abe，question=obj_600658d35b7f4a02b047f65fd99aa076，note=obj_eb69f33ce02f43279169616c91bd6131。对应config.final-v2.json与[返回身份](http://127.0.0.1:8878/?desk_workspace=obj_6badd58292f0456fafff0ac8c81058c0&desk_view=view_a72cfbfc5b7148bea70e35b93c820abe&desk_record=obj_600658d35b7f4a02b047f65fd99aa076)。原问题→note中的真实TASK/N2路径→本节原身份是人工闭环，不是自动执行；旧初始实例在下节保留。

## N3人工回链实例（合成问题，不是本人研究证据）

本次N3合成原问题ID=`obj_ce612d1fad134edb9c5f2f6a576296ad`，workspace=`obj_a798ba50dacb47d297ef5bad4190fd6c`，view=`view_f6ec0401bf394a67800cded8d592f85c`。经界面保存的普通note=`obj_88c8c78b13d1416a95dc415a8de6acf3`，正文包含本任务真实路径与N2真实回执路径。这里人工保存返回引用，形成“合成原问题→真实TASK/产物路径→本日志返回原身份”的验证实例，不称自动写回。

启动N3自己的DEMO配置后可访问[原身份链接](http://127.0.0.1:8878/?desk_workspace=obj_a798ba50dacb47d297ef5bad4190fd6c&desk_view=view_f6ec0401bf394a67800cded8d592f85c&desk_record=obj_ce612d1fad134edb9c5f2f6a576296ad)。服务不常驻，该URL不保证目前在线；配错数据根会明确缺失，不能换同名对象。观察版本/重启验证见应用`acceptance/n3-TASK-20260915-013/run-01/manual-workbench-report.json`。

# 尚未完成与下一步

下一动作：在新隔离现场做一次真实用户短试用（N4），依反馈修实际使用障碍。没有用户参与就保持USER-OPEN，不自行追加学习证据。A/B全包独立代码审、C03 AC03-12仍开放；WP0异构审/接受/精确采收/受控加载未闭，自动桥不能继续越过这些门。精确摘录EXR、C04–C07与完整多层网不由本次人工切片关闭。课程掌握和进组新计划由另一窗口继续。

# 风险与回滚

共享INDEX仅本任务行CAS更新；不git add -A、reset、stash、clean或归一化他窗行尾。应用A/B差分先按B_SCOPED.patch及A历史patch核归属；N2无schema迁移。新根不覆盖旧报告，失败现场保留。WP0复合树不整树采收，M4仍warn；实际服务加载须按原门。

# 文件和产物

应用N2回执与N3合同/回执/命令/选定配置/报告/截图随两次应用commit保存；合成content、对象数据库、导出与运行日志只保留本地，未删除、未全量采收，所以Git不是完整现场备份。MAS本批限定本任务、接口审查、两台README/下一步计划、架构/使用/维护手册及INDEX本任务一行；不改进组或生成视图。文档checkpoint准确ID以本文件的git log最近提交为准，避免自引用提交号。

## Amendment

- 本轮先前1并发指令已被用户最新2并发替代；本窗最多主线程＋一个只读核验位，不把另窗进组施工当作本窗子任务。
- 恢复时外层cwd引发wrong_repo；读取实际binding并对MAS显式cwd验证后恢复TASK-012正本，再由其授权链重开TASK-013。收口把本会话恢复入口更新到本任务“当前状态”，不改全局hook配置。solver初次因未激活失败，激活solver后预检通过；未安装/改包。
- 最终回归批次最初只生成B报告：原main成功时抛SystemExit导致循环停止。不是A/C03失败或已经通过；随后分别新根实跑并核三份报告，才记录27/38/22全部通过。自有8878测试进程已退出，末次ss无监听；不据此断言8899状态。
- 归档检查：7份文档UTF-8、84条本地链接通过；INDEX仍纯CRLF，CAS更新后仅本任务行进入暂存；8路径限定文档checkpoint，未采收其他窗口行。恢复binding已在显式MAS cwd验证为TASK-013 / VERIFIED。记录本批checkpoint可用git log -1 --本文件路径查询，不将旧b1e2f1a冒作收尾HEAD。
