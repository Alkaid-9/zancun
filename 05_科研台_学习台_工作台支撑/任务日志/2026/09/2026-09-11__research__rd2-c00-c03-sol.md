---
id: TASK-20260911-002
title: RD-2 第一波 C00-C03 Sol实施
date: 2026-09-11
runtime:
  model: Sol
  effort: UNKNOWN
  effort_source: hosted session; no SKU evidence
  launch: Codex shared workspace
type: research
status: completed_with_open_gates
area: research-desk
project: research-desk
owners:
  - Sol
  - codex-controller
related:
  - progress/decisions/rd2-construction-v0.3/SOL_START_HERE.md
  - progress/decisions/rd2-construction-v0.3/sol-delivery/20260911-sol-c03-113925/RECEIPT.md
  - progress/decisions/rd2-construction-v0.3/sol-delivery/20260911-sol-c03-113925/CONTROLLER_REVIEW.md
---

# 目标

按 RD-2 手册连续实施 C00-C03，保留 P1，使用隔离验收数据，不改真实资料、默认配置或共享台账。

# 最终结果

C00-C03 的后端合同增量、GLOBAL/TOPIC/WORKSPACE 主路径与 C01/C02 UI 已实现；31 项技术验收通过，接收主控独立重跑单测、链接检查和 C03 浏览器路径后接受技术交付。AC03-12 保持 USER-OPEN。

# 修改内容

- `research-desk/app/research_service.py`：registered_asset、relation、proposal、decision、withdraw、graph。
- `research-desk/app/research_desk.py`：来源、map、graph、relation/proposal HTTP 路由。
- `research-desk/app/static/app.js`：无手填 ID 的来源选择与 Map 入口。
- `research-desk/README.md`、`MAINTENANCE.md`：数据根/运行态维护说明。
- 独立验收根与 Sol delivery 文档，详见回执。

# 验收与证据

| 验收项 | 结果 | 证据 |
|---|---|---|
| solver 门禁 | passed | `bash tools/scripts/require_solver_env.sh`（solver） |
| 后端/旧导航/P1/新路径测试 | passed | `21/21 OK` |
| API relation/proposal/map | passed | `research-desk/acceptance/c03-20260911-sol-c03-113925/runtime/` |
| 备份恢复 | passed | `runtime/backup.sqlite3`、`before/recovered-data/desk.sqlite3` |
| C03 浏览器完整路径 | passed | `runtime/c03-browser-report.json`，显式 8873，17/17，含新建/已有工作区、回流、重启与桌面/390px检查 |
| 接收主控复核 | passed | `CONTROLLER_REVIEW.md`；21/21、2432/0/0、17/17 均由主控重跑 |
| 干净用户沙箱烟测 | passed | `user-acceptance/runtime/user-acceptance-smoke.json`；知识图谱、Method正式/待确认边、唯一工作区和返回原专题通过，数据库哈希前后不变 |
| 用户实际使用 | USER-OPEN | `evidence.json` AC03-12 |

# 风险与回滚

服务只绑定127.0.0.1:8873；交付时使用`user-acceptance/config.user.json`运行，退出后可按`USAGE.md`重启。回滚仅撤销本轮源码差异并保留acceptance数据与证据；不删除真实资料或默认配置。
