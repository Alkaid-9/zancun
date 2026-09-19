---
id: TASK-20260915-009
title: 参考清单融入两台详细计划与划分标准
date: 2026-09-15
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 托管会话未提供可确认的有效effort；交互式有界文档设计，不启动长任务或无人值守执行
  launch: 当前交互式会话
type: research
status: completed_with_open_gates
area: research-desk
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_INTEGRATION_PLAN.md
  - progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
---

# 目标

用户要求“现在先构造详细计划方案，划分标准”。针对已归档11项参考，制定评估与融入学习台／科研台的时机、深度、处置、证据／授权标准，以及执行阶段、检查、评审、测试与退出方案。只授权本次设计、存档和范围内检查，不安装、不试点、不改应用、真实库或课程。

# 最终结果

计划已写入REFERENCE_INTEGRATION_PLAN.md并完成主线程文档／语义自查：四类划分轴、11项行动分配、六阶段、八个相关场景、评审／严重度／退出标准，以及PLAN-01–08方案验收条件齐全。来源清单继续唯一；新计划只增加行动和标准，不复制来源事实、不批准任何候选采用。独立评审未完成，未来评估／试点／接入尚未执行。

# 修改内容

- 新增详细计划与本任务记录。
- 在统一清单、FIRST_BUILD_PLAN和README增加新方案指针，保留前序授权和历史记录。
- 共享INDEX仅登记本任务行，不改TASK-008或课程TASK-004／005／007状态。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 需求覆盖 | 11项时机／深度／行动，四种划分标准分开 | 主线程自查通过 | 计划§2–3；R01–R10/I01程序覆盖核对 |
| 可执行性 | 阶段、输入产出、依赖、完成条件、评审与测试 | 方案层自查通过，未实跑 | 计划§5–7、§9；6阶段与8条PLAN标准存在性检查 |
| 边界 | 仅设计；不混淆多层网络、能力、执行和课程验收 | 主线程自查通过 | 计划§1、§4、§8–10；原教学缺口／TASK-004／考试阶段保留 |
| 入口与文档 | 本地链接／锚点、覆盖、空白／乱码和状态一致 | 5文件、57个本地链接目标、计划2个锚点通过 | Node一次性只读文档检查；未新增测试文件／平台 |
| 共享登记 | allocator签号、CAS单行更新、原行尾保留 | VERIFY-OK，纯CRLF，其他行字节保留 | 8899签发TASK-20260915-009；solver预检及ledger_edit --check通过 |
| 独立评审 | 与主线程自查分开，无有效回执不算通过 | 未完成：连接失败，无有效证据 | 仅一次派发，不重试；不标独立通过 |

# 当前状态

设计交付完成，未来执行与独立评审保持开放。MAS仓库`master@f9f42db39be4286e6275ffbeb636ffae53e1f23e`；现有共享脏树与应用A/B改动保留。本轮未运行应用、重跑课程QA、安装外部工具或变更真实数据；未commit/push。

# 尚未完成

- 按本方案执行11项深评、真实小样、隔离试用与正式接入均未开始，需相应后续授权。
- OpenScience项目地址、享做设备与实际导出、用户样本及成本预算待补。
- 课程补修／独立验收、TASK-20260906-004冲突、A/B用户验收不由本任务关闭。

# 下一步

交付用户审阅分类与阶段；获得继续评估的授权后，从需求对账与结构比较组开始，工具安装和数据接入另批。

# 可拓展方向

有实际评估结果时集中建立一份REFERENCE_EVALUATION.md；当前不创建空结果文件，不为每个候选建立新平台或表单体系。

# 风险与回滚

计划状态不等于执行授权；方法借鉴不等于软件采用。撤回只处理本任务新文件／新增路由及索引行，不重置共享树、不删除原清单或他窗回执。

# 文件和产物

- progress/decisions/two-desks-delta-20260914/REFERENCE_INTEGRATION_PLAN.md
- progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md（路由增量）
- progress/decisions/two-desks-delta-20260914/FIRST_BUILD_PLAN.md（后续方案指针）
- progress/decisions/two-desks-delta-20260914/README.md（当前设计入口）
- 本任务记录及progress/task_logs/INDEX.md本任务行

## Amendment

### 2026-09-15：方案自查与评审边界

- PLAN-01–08逐项主线程检查：所有参考均分配行动、四轴分离、阶段依赖明确、正常／关键失败场景齐备、I01与旧缺口保留、多层语义和阶段目标未改、评审失败处置明确、入口与未来文件口径一致；均为设计层结论，不是工具实测或学习效果验证。
- 只读代理`/root/reference_plan_review`在连接阶段失败（request ID `554e9dcb-fc58-43be-90f7-b476c0a840b5`），未产出问题清单或审查结果。最高并发2，派发后等待，未重试或派生。
- 实际修改域为新方案／新任务、统一清单和两个方案入口的路由增量、共享INDEX本任务行；无应用／课程／真实库／默认配置改动，不改他窗状态冲突行。后续第一动作是用户审阅本方案；批准评估范围后才启动对应阶段。
- INDEX以CAS只新增TASK-009一行；移除新增行后与写前内容逐字节一致，写后`VERIFY-OK`，CRLF=304、bare-LF=0，收尾SHA=`d6e5311f51a95510361e1bc966994e90b04fcc8c6e464825ae1ef161d0d29634`。SHA仅沿用共享登记并发核对，不新设hash质量门。
