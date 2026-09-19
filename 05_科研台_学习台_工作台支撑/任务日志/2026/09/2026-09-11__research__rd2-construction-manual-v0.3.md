---
id: TASK-20260911-001
title: RD-2施工总审与Sol施工手册v0.3
date: 2026-09-11
runtime:
  model: Codex (GPT-6)
  effort: UNKNOWN
  effort_source: 当前运行环境未暴露可独立核验的effort字段
  launch: API coding agent
type: research
status: done
area: research-desk
project: none
todo_ids: []
owners:
  - user
  - codex
related:
  - progress/decisions/rd2-construction-v0.3/SOL_START_HERE.md
  - progress/decisions/rd2-construction-v0.3/MANUAL.md
  - progress/decisions/rd2-construction-v0.3/CONTRACTS.md
  - progress/decisions/rd2-construction-v0.3/ACCEPTANCE.md
  - progress/decisions/rd2-construction-v0.3/TRACEABILITY.md
---

# 目标

总审科研台、学习台、工作台相关施工地图与Sol任务书，修复编号混用、地图主线后置、自然入口缺失、验收只覆盖技术链和维护说明冲突等规划问题；交付可直接执行的分包手册，不在本窗口修改应用。

# 最终结果

已形成RD-2施工手册v0.3。第一波明确授权Sol连续执行C00–C03：维护和版本基线、自然资料入口、关系／提案、多尺度地图往返；完成后停止扩大范围并交用户体验。搜索／工业、指导、学习、成果继承细分为C04–C07，外部画布、3D、工作台、TaskQuay、版本化、桌面与部署列为独立专项。本窗口未改应用、未启停服务、未迁移数据、未commit/push/deploy。

# 修改内容

- 新增Sol直接入口、详细施工步骤、对象与接口合同、分层验收及R01–R27追踪。
- 把页面、施工包、验收与历史包改用不同命名空间，避免“P1完成”歧义。
- 将用户无需知道内部ID、同一真实主题贯穿全局／专题／工作区设为第一波硬验收。
- 将运行日志可清理与当前记录库位于runtime下的冲突列入C00，不在规划窗擅自移动现有数据。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 施工入口 | Sol能明确知道本轮做什么、做到哪停 | 通过 | `progress/decisions/rd2-construction-v0.3/SOL_START_HERE.md` |
| 分包完整 | C00–C07及专项有目标、步骤、产物、前置 | 通过 | `MANUAL.md` |
| 技术合同 | 来源、关系、提案、Topic、HTTP、兼容与备份有合同 | 通过 | `CONTRACTS.md` |
| 验收可判定 | 第一波逐动作验收，后续包有场景，用户门独立 | 通过 | `ACCEPTANCE.md` |
| 需求未缩水 | R01–R27逐项映射当前上限与后续入口 | 通过 | `TRACEABILITY.md` |
| 环境 | Python动作前solver门禁 | 通过 | `Environment OK: solver`；本轮未运行项目Python |

# 当前状态

手册READY-FOR-EXECUTION；P1既有技术结果保留、用户实际使用仍开放。应用目录仍无独立Git仓的既有状态没有改变。MAS工作树原有大量他窗改动，本轮没有清理或采收。

# 尚未完成

- C00–C03应用施工与Sol自验尚未发生。
- C04–C07只完成细分设计，未授权本次连续施工。
- 独立主控验收、用户体验、版本采收、commit/push及部署均未完成。

# 下一步

1. 用户将`SOL_START_HERE.md`交给Sol，Sol按第一波C00–C03施工并交回执。
2. 主控按AC00–AC03复核证据；用户走AC03-12后再决定修摩擦或启动C04。

# 可拓展方向

- C04搜索与工业；C05指导；C06学习；C07成果继承。
- X-CANVAS、X-3D、X-DISPATCH、X-TASKQUAY、X-REPO、X-DESKTOP、X-DEPLOY。

# 风险与回滚

- 关系／提案会扩大记录合同；通过独立演示根、expected_revision和原子事务控制，回退先导出新记录再撤源码。
- 应用未独立版本化；Sol必须保存改前文件与changes.patch，不以外层Git状态作为应用证据。
- 本任务只新增规划文档和任务记录；删除新增v0.3目录及本日志即可回退文档，但已领任务号不回收。

# 文件和产物

- `progress/decisions/rd2-construction-v0.3/SOL_START_HERE.md`
- `progress/decisions/rd2-construction-v0.3/MANUAL.md`
- `progress/decisions/rd2-construction-v0.3/CONTRACTS.md`
- `progress/decisions/rd2-construction-v0.3/ACCEPTANCE.md`
- `progress/decisions/rd2-construction-v0.3/TRACEABILITY.md`
