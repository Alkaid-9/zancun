# 进组包拓展 W0 执行回执

日期：2026-09-17  
任务：`TASK-20260917-001`  
状态：`W0-CONTROLLER-COMPLETE / USER-ACTION-OPEN / W1-READY`

## 1. 授权与恢复

本轮已重新读取接入审计、RD-2 MANUAL／ACCEPTANCE、科研驾驶舱方案、下一执行计划、并发 TASK-009 日志、OE-1 最新交接和 TASK-017 试用入口。未从聊天摘要推断正式边界；恢复状态已由上述正本重新绑定。

## 2. 当前事实

| 对象 | 2026-09-17 观察 | 结论 |
|---|---|---|
| MAS | `/mnt/d/MyResearch/MAS_Safety_Project`，`master`，HEAD `306cc2b3172c3504c23be913a97f518a707ea217`，相对 `origin/master` 为 0 behind / 21 ahead | 工作树高度 dirty；已有 staged 内容，禁止整树采收 |
| research-desk | `/mnt/d/MyResearch/research-desk`，`main`，HEAD `0b3a54178e4ec58fb96eb8570101c44d94ac5687` | tracked index/worktree 无修改；多组历史 acceptance 运行产物未跟踪 |
| WP0 隔离树 | `/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901`，分支 `codex/wb2-wp0-20260901-root`，HEAD `02da69bfd54f5a2fdfb70b6ae085c1178bfea43e` | 只读记录；本任务不修改、不采收 |
| TASK-017 服务 | `127.0.0.1:8878`，PID `8705`，命令使用 `acceptance/user-trial-TASK-20260915-017/config.demo.json`，HTTP `/` 返回 200 | 服务存活；本轮未重启、未启动第二实例 |
| TASK-017 数据 | SQLite 只读计数：objects=0、views=0、object_revisions=0、view_revisions=0 | 试用环境就绪，但没有用户试用证据 |

## 3. 并发与写域冻结

`TASK-20260916-009` 当前 `in_progress`，拥有科研驾驶舱 G0 既有文件；其 staged 集合包含方案、参考、复核、交接、TASK-008 日志和共享 INDEX。本任务不修改这些路径，不改变暂存状态。

W0 仅新增：

- `progress/decisions/2026-09-17__research__jinzu-extension-master-execution-contract.md`
- `progress/decisions/2026-09-17__research__jinzu-extension-wave0-receipt.md`
- `progress/task_logs/2026/09/2026-09-17__research__jinzu-extension-master-contract-and-wave0.md`
- `progress/task_logs/INDEX.md` 中 TASK-001 的唯一新增行

未修改 PENDING 中关于 BR-1 的陈旧文本；最新事实以 2026-09-17 OE-1/BR-1 交接为准，当前只记录冲突，不跨写域修订。

## 4. W0 验收

| ID | 状态 | 证据／观察 |
|---|---|---|
| AC-W0-01 | passed | 三仓身份和 HEAD 当次重读；WP0 通过 `git worktree list --porcelain` 定位 |
| AC-W0-02 | passed | MAS staged 与 dirty 列表已核；TASK-009写域明确；未改暂存集合 |
| AC-W0-03 | passed | `ss`、`ps`、HTTP 三路一致指向 PID 8705／8878／TASK-017 配置 |
| AC-W0-04 | passed | SQLite 使用只读 URI 查询四表均为 0；结论保持 USER-OPEN |
| AC-W0-05 | passed | 总合同 R01-R10 已列正本、消费者、产物与完成判据 |
| AC-W0-06 | passed | 总合同 W0-W7 已列依赖、输出、验收和停止条件 |
| AC-W0-07 | passed | 总合同单列工作树、验收、复核、用户、commit、采收、加载、部署、push |
| AC-W0-08 | passed | 任务日志已建立；INDEX 以旧 SHA `8adce807...` 作 CAS 写入并得到 `VERIFY-OK`，写后 SHA `82f81258...`；纯 CRLF 保持 |

## 5. 开放门与下一步

- `USER-ACTION-OPEN`：用户尚未按 TASK-017 README 完成 5-10 分钟真实路径并提交观察。该门阻止 C04 及其下游，不得由AI代填。
- `W1-READY`：可以按总合同启动公开来源的有界九月刷新；实际联网前必须冻结查询清单、时间范围、来源政策和写域。
- `W2-W5-GATED`：分别服从 C03/C04/C05/C06 的硬依赖。
- `W6-W7-GATED`：驾驶舱交互升级、专项包、WP0桥和端到端试点没有被本轮自动授权。

本轮没有 commit、采收、加载、部署、push、外部发送或用户接受。
