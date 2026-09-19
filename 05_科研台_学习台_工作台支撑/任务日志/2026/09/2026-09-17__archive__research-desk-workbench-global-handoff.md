---
id: TASK-20260917-002
title: 科研台、学习台、工作台与驾驶舱全局总交接
date: 2026-09-17
type: archive
status: completed_with_open_gates
area: research-desk / workbench-v2 / research-copilot
project: research-desk
owners:
  - Codex controller
related:
  - progress/handoff/2026-09-17__research-desk-workbench-global__handoff.md
  - progress/handoff/2026-09-17__research-copilot-user-trial-save-failure__handoff.md
---

# 目标与授权

用户纠正此前交接范围：要求保存整个科研台与工作台的全局状态，而不是只保存单次用户试用故障。任务号由8899中央发号器领取。本任务只做全局事实整合、恢复路由和限定提交，不修改应用、数据库、WP0隔离实现、课程、Skills、sealed或生成视图，不部署、不push。

# 完成结果

- 新建[全局总交接](../../../handoff/2026-09-17__research-desk-workbench-global__handoff.md)，统一覆盖科研台／学习台、工作台／WP0、科研驾驶舱、Skills和参考层。
- 明确已完成、部分完成、未完成、当前RED、三仓与服务、未跟踪恢复载体、下一步严格顺序和全局验收标准。
- 将“保存未发生”降为科研台用户试用的一项RED，不作为全局任务身份或总状态。
- 全局结论保持`PARTIAL-PRODUCT`：G0完成不等于产品完成；WP0技术通过不等于加载；历史测试不等于本轮或用户通过。

# 检查与边界

依据09-15两台总交接、WP0原交接、G0交接、保存故障交接、下一执行计划及两台README对账。提交前检查UTF-8、相对链接、diff空白、共享INDEX行尾和限定暂存路径。回滚只撤本任务文档与两条INDEX路由，不动应用、运行数据或他窗修改。

# 下一动作

从8878保存路径精确复现开始；修复并获用户重试确认前，不启动P1a。A/B独立审、历史采收和WP0治理线随后分别推进。
