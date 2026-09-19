---
id: TASK-20260901-001
title: 工作台 v2 契约冻结批量执行（§8/O1-O7/§13 拍板落账＋施工四件套＋蓝图更新＋九档入库）
date: 2026-09-01
type: maintenance
status: completed_with_open_gates
area: progress/decisions
project: dashboard-v3
todo_ids: []                 # TODO 行=topic:workbench-v2（WB-1 主行 + Git_UI_Pro 子项，本窗新挂）
owners:
  - user
related:
  - progress/decisions/2026-08-31__maintenance__task-unified-contract-v0-proposal.md
  - progress/decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md
  - progress/decisions/2026-08-31__maintenance__workbench-v2-blueprint.html
  - progress/decisions/2026-08-31__maintenance__workbench-product-model-alignment-checkpoint.md
  - progress/decisions/2026-08-31__maintenance__user-statement-archive-4.md
---

# 目标

执行用户 2026-08-31 深夜「先做吧」批量拍板（原文逐字=archive-4）：把工作台 v2 蓝图页"待拍板"清单中的纸面+入库类一次落账——契约 v0→v1 冻结（§8 八项 + O1–O7 全采纳 + §13 科研侧四挂载确认，其中 §8-6/§8-8 两处选择题按提案默认执行、用户可否决）；产出施工四件套（施工方案 / Agent 分工 / 验收标准 / 预期产物）+ UI 规范（简约 + "● Teammate" 同款身份色生成逻辑）；蓝图 html 同步为冻结态；相关九档 pathspec 隔离入库挂路由。本窗跨午夜（08-31 深夜 → 09-01 凌晨），task id 按领号日期 09-01。

# 最终结果

契约 v1 已冻结并记录于提案档 §14（判定表 + 批量边界 + 随附执行清单）；施工四件套落 `workbench-v2-construction-plan.md`（WP0–WP6 切分 / R1–R5 子代理分工全 sonnet 档 / 7 条全局验收门 + 分项要点 / 预期产物表 / UI 身份色规范含双主题色板与 `identity_color()` 代码 / 排期与门）；蓝图 html 更新为 CONTRACT-v1-FROZEN 态（图签、状态带、门梯 1/2 已过、§九改拍板结果、新增 §十 UI 规范色板）；TODO 主行 WB-1 + Git_UI_Pro 子项（铁律 8）与 INDEX 行均以 ledger_edit.py CAS 保形写入并钉哈希。开放门：门 4 开工令（09-10 进组后）、四仓复核 R07 豁免、C-P0 §-2 四项、push、两处默认选择的否决权、TODO/INDEX 行的入库（随下次登记面清算 commit）。

# 修改内容

- 提案档：Status 头改 `CONTRACT-v1-FROZEN`（保留历史行）；追加 §14 拍板记录（逐项判定 + 本批不含 + 随附执行）。
- 新建 `2026-08-31__maintenance__workbench-v2-construction-plan.md`（施工四件套 + UI 规范 §5 + 排期 §6；修复一处 CJK 写入乱码"决策"）。
- 新建 `2026-08-31__maintenance__user-statement-archive-4.md`（「先做吧」+ UI 偏好原文逐字 + 执行口径）。
- 蓝图 html 冻结态改版：状态带红→绿、图签批准行、门 1/门 2 卡置 done、§二 §8-6 已定注记、§四 secref、§九 重排（已批/全采纳/剩余门）、新增 §十 UI 规范（8 色身份色板 + 分配规则）、页脚事实源补施工方案与 archive-4。
- TODO.md（纯 LF 保形）：`[topic:workbench-v2]` WB-1 主行 + Git_UI_Pro 试用子项，插于 DB-7 之后。
- task_logs/INDEX.md（CRLF 保形）：`TASK-20260901-001` 行插于 TASK-20260830-005 之后；同笔以 `--normalize` 修复第 23 行（TASK-20260830-004，Bridge 窗遗留）裸 LF 缺陷，文件恢复纯 CRLF。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 拍板记录 | §14 含逐项判定+边界+随附执行 | 通过 | 提案档 §14（判定表 10 行） |
| 施工四件套 | 四要素齐备且与已冻契约一致 | 通过 | construction-plan §1–§4；UI 规范 §5；排期 §6 |
| 蓝图冻结态 | 无残留 DRAFT/未批表述 | 通过 | 状态带/图签/门梯/§九/页脚全部更新 |
| TODO 写入 | CAS+保形+回读断言 | VERIFY-OK | 终态 sha256=12990a3735b665ddd7618e4e769e7c1a4176f4262e41bc7b7d37c3ef0f6c5acb（纯 LF 813 行） |
| INDEX 写入 | CAS+保形+回读断言 | VERIFY-OK | 终态 sha256=14b9e934d3e3ec0cf949743baea9db878d755e538dbf8aa7f51b46ebe72ec680（纯 CRLF 257/0，混杂已治） |
| task_id 领号 | 8899 中央发号 | 通过 | POST /api/next-task-id → TASK-20260901-001 |
| commit | 九档 pathspec 隔离入库，不含 CROSSWINDOW/他窗面 | 本窗随批执行 | 哈希见 `git log --oneline -1` 与收尾报告 |

# 当前状态

契约 v1 = M4 写门与工作台 P0 的共同输入，施工输入已齐（契约 + 施工方案 + 蓝图 + UI 规范）；施工未开工（门 4）。九个决策/task log 文件入库；TODO/INDEX 新行在盘、未随批 commit（两文件另有 EvoAgent 窗 EA-4、hub 窗 DB-6/DB-7、TASK-20260830-002~005 等他窗在途行，卷入即违反 08-24 事故纪律）。8899 视图由 watchdog 周期自愈刷新。

# 尚未完成

- 门 4 开工（09-10 进组后，WP0 与 M4 合建）——本批明确不提前。
- 四仓复核窗（Keelson/Wegent/NotEMD/LearnGraph）R07 显式豁免：需用户点名。
- C-P0 暂停档 §-2 四拍板点：多选项题，用户排序在工作台后。
- workbench checkpoint 侧的契约引用行（§8-8 默认=本档独立作准，引用行待 checkpoint 下次修订窗）。
- decisions/PENDING.md 中工作台相关旧卡的销账核对（该文件他窗在途，未动）。
- 回传 Bridge 窗三件：Git_UI_Pro 版本号 0.1.35→0.1.48 过时、Tier A vs TIER-B-PROPOSED 确认、Supervisor-Skills 逐 skill 许可证分裂（7×CC-BY / 4×CC-BY-NC-SA）。

# 下一步

1. 09-10 进组后由用户下门 4 开工令 → WP0（数据底座 + M4 合建）先行，按 construction-plan §6 序列推进。
2. 用户如需改选 §8-6（收件箱改一级导航）或 §8-8（改 checkpoint 引用制），任一句话即可翻案，改动仅涉 §14 与蓝图对应行。
3. 下次登记面清算 commit 时把 TODO/INDEX（含本窗两行）一并入库。

# 可拓展方向

- 身份色规范可回灌 8899 现有 hub 面板（会话/窗口列表着色）作为 P0 前的低风险试点——未授权，仅记录。
- INDEX 行尾防线：ledger_edit.py 已能拒改混杂文件，可考虑在 8899 采集器加"登记面 EOL 巡检"告警卡（O6 语义），属 WP0 候选。

# 风险与回滚

- 回滚：本批为单 commit 纯新增文件（九档），`git revert <hash>` 即可整批撤销；TODO/INDEX 两行可按上表哈希定位后用 ledger_edit.py `--replace` 移除。
- INDEX `--normalize` 触碰了他窗一行的行尾字节（TASK-20260830-004 行 LF→CRLF）：属止损性质（恢复登记面 EOL 不变量，工具正门操作），语义零改动；已在此留痕并将报告用户。
- 两处默认选择若被否决：影响面=收件箱导航位置（UI 层）与 checkpoint 引用行（文档层），均无代码耦合。

# 文件和产物

- `progress/decisions/2026-08-31__maintenance__task-unified-contract-v0-proposal.md`（契约 v1 + §14）
- `progress/decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md`（施工四件套 + UI 规范）
- `progress/decisions/2026-08-31__maintenance__workbench-v2-blueprint.html`（冻结态蓝图，浏览器直开）
- `progress/decisions/2026-08-31__maintenance__workbench-product-model-alignment-checkpoint.md`（随批入库）
- `progress/decisions/2026-08-31__maintenance__user-statement-archive-1/2/3/4.md`（原文逐字存档）
- `progress/task_logs/2026/09/2026-09-01__maintenance__workbench-v2-contract-freeze-batch.md`（本档）

## Amendment

历史记录原则上不重写。后续状态变化在这里追加日期和说明。
