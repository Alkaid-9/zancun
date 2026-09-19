# 交接档 · 工作台 v2 WP0 数据底座与 M4 写门（2026-09-01）

**Date**: 2026-09-01 09:53 +08:00
**Task**: `TASK-20260901-007`
**Type**: handoff（S 档单文件；WP0 隔离施工恢复入口）
**Line/Project**: maintenance / `dashboard-v3` / `[topic:workbench-v2]`
**Session**: `01a058f4-780c-7ae1-ac89-4194f16ac836`
**Status**: `TECH-PASS / CONTROLLER-PASS / HETERO-REVIEW-OPEN / USER-ACCEPTANCE-OPEN`

## §0 · TL;DR

WP0 A-E 技术验收全绿；实现仍在隔离复合工作树，等待异构审、用户验收与采收门。

## 权威链声明

本档是后续窗口的恢复路由，不取代任务事实、冻结契约或 Git 当前状态。冲突时按下列顺序回到对应事实面：

1. 当前执行事实与验收回执：`progress/task_logs/2026/09/2026-09-01__maintenance__workbench-v2-wp0-codex-execution.md`；
2. Task 字段与状态机语义：`progress/decisions/2026-08-31__maintenance__task-unified-contract-v0-proposal.md` §4/§5；
3. WP0 范围、全局门和异构审协议：`progress/decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md` §1/§3/§7；
4. 本次施工判据：隔离 worktree 内 `tools/dashboard/_briefs/CODEX_BRIEF_WP0.md`（FINAL-v1.0）；
5. Lot 级证据：隔离 worktree 内 `tools/dashboard/_briefs/_codex_wp0/` 的 receipt、controller review 和真实镜像报告；
6. commit、index、worktree 与运行态：新窗口重新读取 Git 和 8899，任何快照均不得当作永久事实。

前序 `2026-09-01__workbench-v2-design-window__handoff.md` 仍是架构与排期入口；其中“WP0 尚待门 4”的动态描述已被用户本次执行口令和 TASK-007 的盘面事实取代。本档只 supersede 该动态开工状态，不修改契约、施工方案或 WP1+ 排期。

## §1 · 当前状态快照

快照时刻：2026-09-01 09:53 +08:00。新窗口必须重读，不得照抄为当前事实。

| 面 | 当前读数 | 判定 |
|---|---|---|
| 共享主仓 | `/mnt/d/MyResearch/MAS_Safety_Project` · `master` | 任务登记面与本交接落点 |
| 共享 HEAD | `3779b81075ba91bfc80d188c410166dde8359f07` | 本地 master；不是 WP0 实现 commit |
| 共享 index | staged 路径 0 | 未授权 commit |
| 共享 worktree | 70 个 unstaged、56 个 untracked 条目 | 多窗口复合脏树，默认不归 WP0 |
| 施工 worktree | `/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901` | WP0 实现与证据所在地 |
| 施工分支/HEAD | `codex/wb2-wp0-20260901-root` · `02da69bfd54f5a2fdfb70b6ae085c1178bfea43e` | HEAD 是开工锚点，不是实现 commit |
| 施工 index | staged 路径 0 | WP0 未提交 |
| 施工 worktree | 33 个 unstaged、17 个 untracked 条目 | 含 WP0 前既有 dashboard 复合改动 |
| Task 状态 | `review / completed_with_open_gates` | 技术通过，未到 user accepted |
| M4 模式 | 默认 `warn`；未新增全局配置 | 未启用全局 enforce |
| 8899 | 未因本次施工重启 | 运行进程尚未加载 WP0 |
| 并发/模型 | 总并发上限 2；唯一子 agent=`gpt-5.6-sol` | 符合用户最新覆盖口令 |

## §2 · 已完成与证据

### 2.1 Lot A-E

| Lot | 已完成 | 关键边界 |
|---|---|---|
| A | task log 宽容读取、十字段对象、字节保形字段写回 | 历史缺字段只 lint；LF/CRLF/混合行尾不被归一 |
| B | O5 五动词事件写入器；固定事件先行顺序 | 第二步失败时 EVENTS 残影保留；完整事件 schema 仍等 D6 |
| C | SQLite 派生索引、确定性查询和 rebuild CLI | task log 是唯一事实源；重复 task ID 按来源路径保留 |
| D | INDEX/task log 五类镜像漂移检查器 | 只报告不修复；真实共享语料当前有 94 项存量漂移 |
| E | M4 纯函数写门、三态 rollout、两个 Task GET 端点 | 默认 warn；GET 不重建 DB；无写端点、无全局激活 |

Lot E 另修复 `taskstore/rebuild.py` 的一行包内相对导入，使 `dashboard` 与 `tools.dashboard` 两种既有导入上下文均可工作。两个只读端点为：

- `GET /api/tasks.json`：返回派生任务列表；合法空库为 200；
- `GET /api/task/<id>.json`：保留重复 ID 列表；缺项 404；DB 缺失或不可用为 503；
- 两端点只读既有派生 DB，不在 GET 时隐式重建或改写文件。

### 2.2 新鲜验收结果

| 验收面 | 结果 | 范围说明 |
|---|---|---|
| Lot A focused | `40 passed` | loader/writer 与真实日志只读兼容 |
| Lot B focused | `12 passed` | 五动词、事件先行、append-only |
| Lot C focused | `7 passed` | 重建幂等、确定性查询、真实语料 |
| Lot D focused | `12 passed` | 五类漂移和真实报告 |
| Lot E TDD | RED=`66 failed, 1 passed`；GREEN=`67 passed` | 写门和只读端点先红后绿 |
| A-E 聚合 | `138 passed` | taskstore 全部 Lot |
| dashboard 全量 | `490 passed` | 隔离复合基线上的全量套件 |
| legacy | `49 passed, 1 skipped, 50 collected`，另 2 subtests | 存量入口零回归 |
| golden replay | `9/9`；`117/117` artifacts byte-identical | expected 基线未由 Lot E 改动 |
| TASK-007 自举 | 十字段 `10/10`、lint=0、M4 enforce issues=0 | 新契约可读取和校验自身任务 |
| 账本保形 | task INDEX 纯 CRLF；TODO 纯 LF；ledger hygiene `3 passed` | TASK-007 镜像新增漂移 0 |

Lot C 施工时重建了当时的 2026 task logs `232/232`；TASK-007 登记完成后的共享语料自举重建为 `239/239`。两者是不同时间点，不应混报为同一次运行。

Lot D 当前 94 项存量漂移分布：`frontmatter_missing=71`、`status_mismatch=10`、`missing_index_row=9`、`dead_link=2`、`type_mismatch=2`。它们不是本次引入，也没有在本任务中自动修复。

## §3 · 未完成、恢复条件与第一安全动作

| 开放项 | 当前状态 | 恢复条件 | 第一安全动作 | Owner |
|---|---|---|---|---|
| Claude 异构审 A | 未运行；Codex controller review 不能冒充跨模型审查 | Claude 主控可读施工 worktree、作业书和五份回执 | 逐 Lot 比对 diff/新文件、receipt 和 FINAL-v1.0 判据；任一 FAIL 回 Codex 修复 | Claude 主控 |
| 用户 accepted | 未发生；Task 仍为 `review` | 异构审结果送达用户 | 用户明确接受指定 WP0 scope，或点明需修项 | 用户 |
| 精确采收/commit | 未做；实现没有 commit | 异构审 PASS、用户 accepted、用户放行 commit | 重读双 worktree 状态，按文件与 hunk 建所有权清单；禁止整树 stage | 主控 |
| 8899 live 复验 | 未做；真实服务未加载 WP0 | 采收结果明确且用户授权受控重启 | 记录旧 PID/版本，受控重启后查两个新端点及既有端点 | 主控/用户 |
| push | 未做 | commit 与 live 门关闭后，用户另行授权 | 列出精确待推 commits 与远端，再非交互 push | 用户/主控 |
| 94 项镜像漂移治理 | 不在 WP0 范围 | 另立任务、归属与修复政策 | 先分类 71 个 frontmatter 缺失是否为 legacy 兼容对象 | 后续任务 |
| 未冻结 schema | 未实现 typed waiting、session type enforce、as_of 年龄阈值 | D6 或对应决策明确冻结 | 先写决策，不在当前实现中猜测补齐 | 架构决策窗 |
| WP1/WP2 | 未开始且不由本档授权 | WP0 外部门按施工方案关闭 | 重新 FINAL 化对应作业书与写域，再开独立任务 | 后续施工窗 |

## §4 · 状态上界

当前可以声称：WP0 A-E 代码、测试、回执和 Codex controller 复核在指定隔离 worktree 达到 `TECH-PASS / CONTROLLER-PASS`。

当前不能声称：

- Claude 跨模型异构审已经完成；
- 用户已经 accepted；
- WP0 是 clean `02da69b` checkout 上的单一补丁；
- 实现已经 commit、merge、部署、push 或被 8899 加载；
- 94 项历史镜像漂移已经修复；
- 工作台 v2、P0 全阶段或 WB-1 总体完成。

## §5 · 文件归属与采收边界

### 5.1 WP0 明确产物

- `tools/dashboard/taskstore/`：8 个模块；
- `tools/dashboard/tests/test_taskstore_lot_a.py` 至 `test_taskstore_lot_e.py`；
- `tools/dashboard/_briefs/_codex_wp0/`：5 份 receipt、5 份 controller review、1 份 Lot D 真实报告；
- `tools/dashboard/_briefs/CODEX_BRIEF_WP0.md`：由 DRAFT 升为 FINAL-v1.0 的施工输入。

### 5.2 必须按 hunk 复核的共享文件

- `tools/dashboard/service/http.py`：Lot E 只拥有两个 GET 路由、DB 路径 seam 等 34 行增量；文件另含 WP0 前既有改动；
- `tools/dashboard/taskstore/__init__.py`：Lot E 仅拥有 4 行导出；
- `tools/dashboard/taskstore/rebuild.py`：Lot E 仅拥有 1 行相对导入修复；
- `.gitignore`：SQLite 落点忽略规则由主控预置，采收时单独核归属；
- 其余 dashboard、golden expected、tools/scripts 改动默认属于复合基线，不得因同处施工 worktree 而归给 WP0。

### 5.3 共享主仓本次交接所有权

本次交接只拥有：本档、`progress/handoff/INDEX.md` 的一条路由增量，以及 TASK-007 的 CURRENT/EVENTS/Amendment 反向引用。共享树其余 126 个脏条目保留原所有权，不 clean、stash、reset、checkout、整文件覆盖或批量暂存。

## §6 · 新窗口必读与第一动作

读取顺序：

1. `progress/handoff/INDEX.md` 顶部本条路由；
2. 本档 §0、权威链、§1、§3、§5、§7；
3. TASK-007 task log 的 CURRENT、验收表、尚未完成与 Amendment；
4. 隔离 worktree 的 `CODEX_BRIEF_WP0.md` §零至§五；
5. 契约 §4/§5、施工方案 §1/§3/§7；
6. `_codex_wp0/lot_{a..e}_receipt.md` 与对应 controller review；
7. 重读双仓 branch、HEAD、staged/unstaged/untracked，再决定是否进入异构审。

新窗口第一安全动作是只读复核，不是采收：

```bash
cd /mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901
git branch --show-current
git rev-parse HEAD
git diff --cached --name-status
git status --short
```

若这些读数与 §1 漂移，先更新事实判断，不以本档快照覆盖磁盘。确认施工证据仍在后，才按施工方案 §7.3 开始 Claude 异构审 A。

可重跑验收命令：

```bash
bash tools/scripts/require_solver_env.sh
/home/alkaid/miniconda3/envs/solver/bin/python -m pytest tools/dashboard/tests/ -q
/home/alkaid/miniconda3/envs/solver/bin/python -m pytest tools/dashboard/tests/test_taskstore_lot_a.py tools/dashboard/tests/test_taskstore_lot_b.py tools/dashboard/tests/test_taskstore_lot_c.py tools/dashboard/tests/test_taskstore_lot_d.py tools/dashboard/tests/test_taskstore_lot_e.py -q
```

legacy 与 golden 分别从施工 worktree 的 `tools/scripts/` 和仓根按 FINAL-v1.0 §一.6 运行。测试通过只证明对应技术面，不自动关闭异构审、用户验收、commit、live 或 push 门。

## §7 · 禁止越界

- 不把本档或 controller review 写成 Claude 异构审证据；
- 不把 `TECH-PASS` 写成 user accepted、clean HEAD、merged、deployed、pushed 或项目总体完成；
- 未获用户授权不 commit；push 必须另获授权；
- 不使用 `git add -A`、`git commit -a`、reset、clean、stash 或整树 cherry-pick；
- 不整体采收 `service/http.py` 或复合基线中的 golden、hub、projects、tools/scripts 改动；
- 不为追求“0 findings”自动修复 94 项历史镜像漂移；
- 不启用全局 M4 enforce，不新增环境变量或配置开关；
- 不猜测 `waiting_user(typed)`、session type enforce 或 `as_of` 年龄阈值；
- 不因本次提前执行 WP0 而自动推进 WP1/WP2 或改写 09-10 后长期排期；
- 不手改 NOW、STATUS、PROJECT_HOME、WEEK、DAILY 或 dashboard 生成视图。

## §8 · 完成判据

### 本次 WP0 技术施工

已满足：Lot A-E 判据、A-E 聚合、legacy、dashboard 全量、golden、TASK-007 自举、行尾保形和 controller review 全部通过；对应上界是 `TECH-PASS / CONTROLLER-PASS`。

### WP0 用户验收与持久化

尚未满足：Claude 异构审 A PASS；用户对明确 scope 表示 accepted；精确所有权清单与 scoped commit；若要求运行生效，还需 8899 受控重启和 live 端点复验；若要求远端恢复，还需独立 push 授权与远端验证。

### 工作台 v2 后续阶段

不在本交接完成判据内：WP1/WP2/WP3、P0 用户整体验收、WP4、WP5/WP-S、WP6 和 94 项历史漂移治理。

## §9 · 主控默认问句

用户未指定后续动作时，只问：

> 是否先由 Claude 按施工方案 §7.3 对 WP0 diff 与五份回执执行异构审 A，保持 commit、8899 和 push 不动？

## §10 · 证据地图

| 结论 | 证据入口 |
|---|---|
| TASK-007 当前事实与总验收 | `progress/task_logs/2026/09/2026-09-01__maintenance__workbench-v2-wp0-codex-execution.md` |
| Task 十字段与状态机 | `progress/decisions/2026-08-31__maintenance__task-unified-contract-v0-proposal.md` §4/§5 |
| WP0 范围与异构审流程 | `progress/decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md` §1/§3/§7 |
| FINAL 施工判据 | 施工 worktree `tools/dashboard/_briefs/CODEX_BRIEF_WP0.md` |
| Lot A-E 回执与控制器复核 | 施工 worktree `tools/dashboard/_briefs/_codex_wp0/` |
| 94 项镜像漂移原始报告 | `_codex_wp0/lot_d_real_index_report.md` |
| 当前交接路由 | `progress/handoff/INDEX.md` |
| 工作台长期运维 | `progress/runbooks/dashboard-system.md`、`progress/runbooks/dashboard-maintenance.md` |

## §-1 · 复核记录

| 维度 | 结果 | 备注 |
|---|---|---|
| L0-1 零临时路径 | PASS | 机械扫描禁用临时目录命中 0 |
| L1-1 本档存在且 >50 行 | PASS | 落档后实测 239 行 |
| L1-2 关联决策档 | PASS | 沿用冻结契约和施工方案，无新决策 |
| L1-3 task log 存在 | PASS | TASK-007 正本已读 |
| L2-1 开放项有触发条件 | PASS | §3 每项含恢复条件 |
| L2-2 无语义重叠 | PASS | 异构审、accepted、commit、live、push 分层 |
| L2-3 完成项有总结 | PASS | §2 与 §8 范围化总结 |
| L3-1 新护栏落 memory | N/A | 本次不建立新全局护栏 |
| L3-2 不重复立护栏 | PASS | 引用既有共享树、交接和验收纪律 |
| L4-1 引用格式 | PASS | 仓内路径使用反引号；无新增 memory 链接 |
| L4-2 交叉引用 | PASS | handoff INDEX 一条路由；TASK-007 已反向挂链 |
| L4-3 TL;DR ≤80 字符 | PASS | §0 单句低于上限 |

**主控自审结果**：12/12（11 PASS + 1 N/A）。另验：10 个必需章节齐全，TASK-007 十字段 `10/10`、lint=0、M4 enforce issues=0；handoff INDEX 保持纯 LF且该 tracked diff 通过 `git diff --check`；两份新文档尾随空白命中 0；ledger hygiene `3 passed`；生成器 dry-run exit 0 且未写文件。

## 反向引用

- task log：`../task_logs/2026/09/2026-09-01__maintenance__workbench-v2-wp0-codex-execution.md`；
- 前序设计交接：`2026-09-01__workbench-v2-design-window__handoff.md`；
- 交接规范：`../runbooks/handoff-checklist.md`、`../runbooks/window-archive-package.md`；
- 上下文恢复局部实例：`../runbooks/context-preservation-and-compaction.md`。

---

*本档只建立可恢复游标，不授权异构审之外的后续施工，也不改变任何开放门。*
