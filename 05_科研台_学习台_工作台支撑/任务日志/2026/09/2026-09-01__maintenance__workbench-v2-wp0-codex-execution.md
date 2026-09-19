---
id: TASK-20260901-007
task_id: TASK-20260901-007
title: 工作台 v2 WP0 数据底座与 M4 写门 Codex 隔离施工
date: 2026-09-01
type: maintenance
status: completed_with_open_gates
state: review
area: dashboard/workbench-v2
project: dashboard-v3
acceptance: WP0 A-E 按 FINAL-v1.0 完成，存量测试与 golden 零回归，并保留异构审、用户验收和采收门。
sessions: [{"id":"01a058f4-780c-7ae1-ac89-4194f16ac836","primary":true}]
gates: [{"gate":"外部依赖","waiting_on":"Claude异构审"},{"gate":"授权","waiting_on":"用户accepted与采收/重启"},{"gate":"commit","waiting_on":"用户"},{"gate":"push","waiting_on":"用户"}]
next_action: 由 Claude 主控执行异构审 A，再由用户裁定 accepted 与采收门。
todo_ids:
  - WB-1
owners:
  - user
  - codex
related:
  - progress/handoff/2026-09-01__workbench-v2-wp0-codex-execution__handoff.md
  - progress/handoff/2026-09-01__workbench-v2-design-window__handoff.md
  - progress/decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md
  - progress/decisions/2026-08-31__maintenance__task-unified-contract-v0-proposal.md
  - tools/dashboard/_briefs/CODEX_BRIEF_WP0.md
---

# CURRENT

as_of: 2026-09-01T09:53:28+08:00
- 现状：WP0 A-E 已通过 Codex controller 技术验收，S 档可恢复交接已落盘。
- 下一行动：Claude 异构审 A，然后由用户裁定 accepted 与采收门。
- 开放门：异构审、用户 accepted、commit/merge、8899 live 复验、push。
- 权威入口：WP0 交接档、本记录、`tools/dashboard/_briefs/CODEX_BRIEF_WP0.md` 与 `_codex_wp0/` 回执/复核。

# EVENTS

- 2026-09-01T03:45:16+08:00 | state_changed | review
- 2026-09-01T03:45:16+08:00 | artifact_linked | tools/dashboard/_briefs/_codex_wp0/
- 2026-09-01T03:45:16+08:00 | note | TECH-PASS / CONTROLLER-PASS；外部门保持开放
- 2026-09-01T09:53:28+08:00 | artifact_linked | progress/handoff/2026-09-01__workbench-v2-wp0-codex-execution__handoff.md

# 目标

按用户 2026-09-01 “找一下相关的文件并且执行”口令，在隔离 worktree 执行工作台 v2 WP0 Lot A-E，并按最新口令把总并发限制为 2（主窗口加至多一个子 agent）；子 agent 固定为 `gpt-5.6-sol`。本任务不改权威计划的 WP1+ 排期，不触发 commit、push 或真实 8899 重启。

# 最终结果

WP0 A-E 已在 `/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901` 完成代码、测试、逐 Lot 回执和 Codex 控制器复核，终态为 `TECH-PASS / CONTROLLER-PASS / HETERO-REVIEW-OPEN / USER-ACCEPTANCE-OPEN`。实现仍停在分支 `codex/wb2-wp0-20260901-root` 的未提交复合工作树；HEAD 锚点保持 `02da69bfd54f5a2fdfb70b6ae085c1178bfea43e`，未合并到共享 `master`。

# 修改内容

- Lot A：新增 task log 宽容读取器和字节保形写入器，覆盖契约十字段、LF/CRLF/混杂行尾与真实日志只读解析。
- Lot B：新增 O5 五动词事件写入器，固定“先追加 EVENTS、再执行动作”的事件先行顺序与 append-only 公共面。
- Lot C：新增由 task log 文本可重建的 SQLite 派生索引、确定性查询面和 rebuild CLI；重复 task id 按来源行保留。
- Lot D：新增 INDEX 镜像只读校验器与真实报告；共享语料现有 94 项漂移被如实报告，未自动修复。
- Lot E：新增纯函数 M4 写门、`off/warn/enforce` 三态、项目/output/decided_by 闭集校验，以及 `GET /api/tasks.json`、`GET /api/task/<id>.json` 两个只读端点。
- Lot E 集成中把 `taskstore/rebuild.py` 的 paths 导入改为包内相对导入，使 `dashboard` 与 `tools.dashboard` 两种既有包上下文都可用。
- 每个 Lot 均有 receipt 和 Codex controller review；没有冒充施工方案要求的 Claude 异构审。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 会话与权威输入 | 绑定指定 session、读附件、重开交接/施工/契约/作业书 | 通过 | session `01a058f4-780c-7ae1-ac89-4194f16ac836`；`CODEX_BRIEF_WP0.md` FINAL-v1.0 |
| 并发与模型 | 总 agent 数不超过 2；子 agent 为 5.6-sol | 通过 | 全程主窗口加唯一 `wp0_baseline_audit`；spawn 记录 `model=gpt-5.6-sol` |
| Lot A | 读写、保形、真实日志解析 | 通过 | focused 40；dashboard 时点 392；golden 9/9 |
| Lot B | 五动词、事件先行、append-only | 通过 | focused 12；dashboard 时点 404；golden 9/9 |
| Lot C | 重建幂等、确定性查询、真实语料 | 通过 | focused 7；真实 2026 task logs 232/232；dashboard 时点 411 |
| Lot D | 五类镜像漂移、真实报告只读 | 通过 | focused 12；真实 94 findings；报告 SHA-256 `8c5885355da19f25a01e1d2ef5903d4adeec0629b54a9a36cc59333da5ef0ac4` |
| Lot E TDD | 先 RED 后 GREEN，覆盖全部写门和端点判据 | 通过 | RED 66 failed/1 passed；focused GREEN 67 passed |
| WP0 聚合 | A-E taskstore 测试全绿 | 通过 | 主窗口独立复测 138 passed |
| 旧基线 | passed/skipped/collected 不回归 | 通过 | 49 passed / 1 skipped / 50 collected，另 2 subtests passed |
| dashboard 全量 | 新模块测试全绿 | 通过 | 主窗口独立复测 490 passed / 0 skipped / 490 collected |
| golden | 9 case 全绿且产物字节一致 | 通过 | 9/9；117/117 artifacts byte-identical |
| 写域与产物 | diff clean、无 progress 越界、无 SQLite 残留 | 通过 | `git diff --check`；隔离 worktree 的 `progress/**` 无 diff；仓内 DB 扫描为空 |
| 运行态边界 | 不启动/重启真实 8899 | 通过 | 端点仅以临时回环 server 验证；live 8899 未触碰 |
| 新契约自举 | 007 自身十字段完整、可过 M4 enforce、不给镜像新增漂移 | 通过 | loader missing=0/lints=0；write gate issues=0；共享 239/239 logs 可重建；007 mirror findings=0 |
| 登记面保形 | INDEX 纯 CRLF、TODO 纯 LF，CAS 哈希稳定 | 通过 | INDEX `0e4125770b6969fdb05fe5af562ea9313b98558c7ba0b3473786bbdff5b9a8f6`；TODO `f95c26784e675dd1e7a1dad244d89f73e26dc7a542034fc833e47eacfa9e8e04` |

# 当前状态

- 代码只在隔离 worktree 的复合 dashboard 基线上，不能声称是 clean `02da69b` checkout 上的单一补丁。
- M4 默认 `warn`，本任务没有启用全局 `enforce`，也没有新增环境变量或配置文件。
- 两个任务 GET 端点已通过真实 task log 临时重建后的 200/schema 测试；重复 task id 仍返回列表，缺项 404，缺 DB 503，GET 不重建 DB。
- 共享主仓当前仅登记任务事实；WP0 实现尚未 commit、merge 或 push，运行中的 8899 也未加载这批代码。

# 尚未完成

- Claude 跨模型异构审 A 未运行；当前只有 Codex 施工者自测和主窗口独立 Codex controller review。
- 用户尚未把 WP0 Task 标为 accepted；施工方案全局门 7 仍开。
- commit、采收/合并、push、真实 8899 受控重启与 live 端点复验均未获本任务授权。
- Lot D 报告的共享 INDEX/task-log 94 项存量漂移未修复；本 Lot 的职责是检测，不是治理语料。
- `waiting_user(typed)` 的独立编码、session type 强制策略和 `current.as_of` 年龄阈值仍未冻结，本实现没有发明它们。

# 下一步

1. 由 Claude 主控按施工方案 §7.3 对 diff 与五份回执做异构审 A。
2. 用户审阅 WP0 自检结果并决定 accepted、commit/采收、运行态重启和 push 各门。
3. 外部门关闭后再按权威施工方案推进 WP1/WP2；本次一次性提前执行不改其长期排期。

# 可拓展方向

- 在 D6 冻结完整 EVENTS/session/waiting_user schema 后，补强当前明确留白的 typed waiting 与 session type enforce。
- 另立镜像治理任务处理 Lot D 的 94 项存量漂移，避免把校验器变成隐式修复器。

# 风险与回滚

- 风险：隔离 worktree 含 WP0 前既有复合 dashboard 改动，采收时必须按文件归属和回执逐项挑选，禁止整树 bulk stage。
- 回滚：本任务未 commit、未部署；在采收前可按 WP0 文件清单逐项放弃本任务差异，但不得 reset/clean 覆盖复合基线中的他人改动。

# 文件和产物

- `tools/dashboard/taskstore/`
- `tools/dashboard/tests/test_taskstore_lot_a.py`
- `tools/dashboard/tests/test_taskstore_lot_b.py`
- `tools/dashboard/tests/test_taskstore_lot_c.py`
- `tools/dashboard/tests/test_taskstore_lot_d.py`
- `tools/dashboard/tests/test_taskstore_lot_e.py`
- `tools/dashboard/service/http.py`
- `tools/dashboard/_briefs/_codex_wp0/`

## Amendment

后续异构审、用户验收、采收、commit、push 或运行态复验只在此处追加，不回写本次历史证据。

### 2026-09-01 09:53 +08:00 · 可恢复交接落盘

- 新增 S 档恢复入口：`progress/handoff/2026-09-01__workbench-v2-wp0-codex-execution__handoff.md`；
- 交接按当前双 worktree 盘面区分 TECH-PASS、异构审、用户 accepted、采收/commit、live 与 push；
- Task 状态保持 `review / completed_with_open_gates`，开放门和下一行动不变；
- 本次只追加交接事实与反向引用，不触碰 WP0 实现、8899、commit、merge 或 push。
- handoff INDEX 经 `ledger_edit.py` + CAS 精确挂链，终态纯 LF，SHA-256=`12f3f088a81540ad743a3882d74d42b28535fa6b62b699923444d6863a3dea65`；交接 12/12 自审通过。
