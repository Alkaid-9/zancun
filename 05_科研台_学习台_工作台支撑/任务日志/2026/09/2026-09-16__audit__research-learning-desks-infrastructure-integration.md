---
id: TASK-20260916-007
title: 科研方法论基建与科研台、学习台实际接入审计
date: 2026-09-16
runtime:
  model: GPT-5
  effort: xhigh
  effort_source: 当前 Codex 托管会话系统运行档；子代理由环境固定为 gpt-5.6-sol/xhigh
  launch: Codex API 协作会话（SESSION_ID 01a0aa94-9235-7db3-ba4a-f1e39c322b1a）
type: audit
status: done
area: research
project: lu-side
todo_ids: []
owners:
  - codex-controller
related:
  - progress/audits/2026/09/2026-09-16__research-learning-desks-infrastructure-integration/INTEGRATION_AUDIT.md
  - progress/runbooks/lu-onboarding-and-desks-architecture.md
  - progress/handoff/2026-09-15__desks-window-current__handoff.md
  - progress/decisions/rd2-construction-v0.3/TRACEABILITY.md
  - research/map/surveys/SURVEY_LEDGER.md
---

# 目标

回答用户点名的知识图谱、菌丝网、科研地图、团队脉络、领域全景、横纵展开、跨领域方法、成果追踪、开源／论文／OpenReview、失败／错题和工业界追踪，究竟是已有静态资产、已经接入当前科研台／学习台、仅有设计，还是已经陈旧／未运行。先形成可恢复存档，再重试此前因 HTTP 429 失败的三路只读独立核验。

# 最终结果

审计已完成。主控结论为 `SUBSTANTIAL-CONTENT / PARTIAL-DESK-INTEGRATION / CONTINUOUS-LOOPS-OPEN`：内容底盘真实存在，A/B/N3 有有限产品链路，但完整多层网络、菌丝画布、C04-C07、自动工作台桥和持续跟踪均不能宣称完成。存档后重试的三路只读独立核验均返回 `complete`，主控已抽查关键出处并修订终版。

# 修改内容

- 新建接入审计，按四层状态逐项覆盖用户列出的能力。
- 恢复并重读三台架构、当前交接、RD-2 追踪矩阵、驾驶舱计划、地图总纲、调研台账和九月补缺计划。
- 用 solver 环境重跑 `map_to_yaml.py --check`，替换此前错误继承环境下的预备数字。
- 明确 TASK-006 是资产／方案盘点，本任务新增实际接入与持续机制判定轴。
- 重试并合并网络／地图、研究追踪、学习／工业三路独立核验；纠正“错题机制持续运作中”，并补入 TraceBridge 一次性工业普查资产。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 恢复绑定 | 不按外层 cwd 或摘要猜任务，重开当前权威文件 | PASS | 当前交接、架构、TRACEABILITY、cockpit plan 均已重读；MAS 根实核 |
| 仓库身份 | 记录根、分支、HEAD、index/worktree 和远端差异 | PASS | `/mnt/d/MyResearch/MAS_Safety_Project`，`master@306cc2b3172c3504c23be913a97f518a707ea217`，共享脏树，`origin/master...HEAD = 0 behind / 21 ahead` |
| 环境门 | solver 预检通过 | PASS | `Environment OK: solver (/home/alkaid/miniconda3/envs/solver/bin/python)` |
| 地图结构检查 | 指定 solver Python，退出码 0 | PASS | 41 表、25 解析、16 跳过；40 school、33 team、170 paper、19 review_case、5 topic |
| 状态分层 | 内容、接入、设计、陈旧／未运行分开 | PASS | 接入审计 §2-§5 |
| 独立核验 | 三路均返回准确 `file:line` 与未查面 | PASS | `audit_network_maps`、`audit_research_tracking`、`audit_learning_industry` 均为 `complete`；主控抽查关键出处 |
| 变更边界 | 不改产品、课程、TODO/PENDING、生成视图或服务 | PASS | 本阶段仅新增审计／任务日志，随后单行登记 INDEX |

# 当前状态

- TASK-007 已由中央计数器发出：`progress/task_logs/.id_counter.json` 的 `20260916` 值为 7；落盘前 INDEX 尚无该号。
- 当前没有产品实现、扫描发射、外部联系、实验、部署、commit 或 push。
- 三路独立核验已完成；总并发保持为 4（主线程 + 3 子代理），代理全程只读，无文件修改或派生代理。

# 尚未完成

- 这是审计而非产品施工；C04-C07、完整知识网络、菌丝画布、持续扫描、自动工作台桥和用户学习／使用验收仍按各自正本保持 OPEN。
- 未联网刷新外部世界，未实跑 research-desk 浏览器／数据库／服务；因此不裁定 8 月后外部变化或真实使用体验。

# 下一步

1. 由用户基于终版矩阵决定先补“工作台接入”还是先恢复“持续追踪”；任何实施另领任务号和授权。
2. 若选择持续追踪，复用已写好的九月 IND-1/RS-A/RS-B 发射包，不再重写计划。
3. 若选择工作台接入，按 C04-C07 分包推进，不把完整知识网、学习闭环和自动桥一次打包。

# 可拓展方向

- 本审计确认缺口后，可另行由用户选择是否授权 C04-C07、九月补缺波或轻量持续追踪；本任务不自动启动。

# 风险与回滚

- 共享工作树含大量他窗改动；只新增本任务两文件，并用 CAS 工具改单行 INDEX。
- 回滚只删除本任务新增文件和 INDEX 本任务行；不 reset、stash、clean 或改他窗文件。
- 结构化地图检查跳过 16 张综合／矩阵表，数字不能升级为全量语义覆盖。

# 文件和产物

- `progress/audits/2026/09/2026-09-16__research-learning-desks-infrastructure-integration/INTEGRATION_AUDIT.md`
- `progress/task_logs/2026/09/2026-09-16__audit__research-learning-desks-infrastructure-integration.md`

## Amendment

- 2026-09-16：按用户“先存档，再继续 429 失败项”的顺序创建第一版检查点。
- 2026-09-16：三路 429 任务重试均成功；主控抽查后收口为 `done`。新增两项关键订正：EdgeIM 错题机制并未持续运行；工业侧有 8 月底 bounded census，但九月续跑未发射。
