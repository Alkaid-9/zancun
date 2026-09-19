# Progress Records

本目录是 MAS Safety Project 的任务状态、历史记录和可重复操作入口。

## 🏠 首选入口

| 想干什么 | 用哪个 |
|---|---|
| **看 + 点着改**（推荐） | 双击仓库根 `看板.bat`，或 `python tools/scripts/app.py` → http://localhost:8899 |
| **只想快速扫一眼** | `PROJECT_HOME.md`（自动生成的单页总览） |
| **新窗口接手** | `NOW.md`（自动生成：七线现状、下一步、红线、待拍板） |
| **离线/手机只读**（无服务） | `dashboard/static.html`（与服务版同模板） |

- 手改数据只改四处：`TODO.md`（七线任务）· `lines/`（7 条业务线）· `decisions/PENDING.md`（待拍板）· `task_logs/`（日志）
- 手改后跑 `python tools/scripts/generate.py` 刷新；看板上的写回会自动触发
- 会话结束钩子（`session_postflight.sh`）会自动重生成
- `STATUS.md` / `NOW.md` / `PROJECT_HOME.md` / `dashboard/data.json` / 两份 HTML 均为生成物，禁止手改
- 使用手册：`runbooks/dashboard-system.md`

## 快速入口

| 文件或目录          | 职责                                        | 更新方式                               |
| -------------- | ----------------------------------------- | ---------------------------------- |
| `PROJECT_HOME.md` | **单页总览**（自动生成 · 人工查看首选）            | 由 `generate.py` 生成，不改手 |
| `NOW.md` | **新窗口入口**（七线现状/下一步/红线/待拍板） | 由 `generate.py` 生成，勿手改 |
| `STATUS.md` | **当前状态快照** | 由 `generate.py` 生成，勿手改 |
| `dashboard/` | **看板产物**（`template.html` 唯一模板 / `ui.html` 可操作 / `static.html` 离线 / `data.json` 数据） | 模板可维护，其余由 `generate.py` + `app.py` 维护 |
| `lines/` | **业务线定义**（7 条：evoagent/research/outreach/exam/casual/infra/pending） | 业务线变化时手改 |
| `decisions/PENDING.md` | **待拍板队列** | 待用户决定事项新增或拍板时手改 |
| `TODO.md`      | 七线任务真相                                   | 行动项新增、完成或取消时更新                     |
| `CHANGELOG.md` | 重要里程碑摘要                                   | 只记录有持续影响的变化                        |
| `task_logs/`   | 每个重要任务实际做了什么                              | 任务结束时写入，原则上不重写历史                   |
| `runbooks/`    | 当前正确的重复操作方法                               | 工具、命令或流程变化时持续维护                    |
| `audits/`      | 验收证据、安全和依赖审计                              | 高风险或需证明的任务单独记录                     |
| `decisions/`   | 长期有效的架构与流程决策                              | 决策变化时追加新记录，不覆盖旧理由                  |
| `incidents/`   | 故障、near-miss 和恢复过程                        | 发生后记录影响、根因和预防措施                    |
| `templates/`   | 记录模板                                      | 记录制度变化时维护                          |
| `.obsidian/`   | Obsidian vault 配置根（含 Dataview 插件 v0.5.68） | 路径由 spec §13 锁死，本目录由 Obsidian 自动管理 |

> **Obsidian vault 根 = `progress/`**（不是项目根）。vault 端看到的全部路径以 `progress/` 为锚点。Dataview 块 FROM 路径相对 vault 根，例如 `FROM "cards/by-id"` = `progress/cards/by-id/`。完整调试指南见 `cards/_dataview-realtime-fix.md`。

任务总索引：[`task_logs/INDEX.md`](task_logs/INDEX.md)

## 记录类型

| 类型 | 用途 |
|---|---|
| `setup` | 环境、依赖、工具和服务接入 |
| `research` | 论文阅读、调研和方案分析 |
| `experiment` | 实验执行、数据和结果分析 |
| `audit` | 安全、质量、依赖和复现审查 |
| `maintenance` | 升级、清理、迁移和文档治理 |
| `incident` | 故障、误操作和恢复 |

## 状态定义

| 状态 | 含义 |
|---|---|
| `planned` | 已定义但尚未开始 |
| `in_progress` | 正在执行 |
| `partial` | 部分目标完成，仍有明确未验收项 |
| `done` | 目标和验收标准均完成 |
| `blocked` | 需要用户、凭据或外部状态变化才能继续 |
| `abandoned` | 经记录后主动停止 |

## 强制收尾流程

每个有实质产出的任务结束前：

1. 使用 `templates/TASK_LOG_TEMPLATE.md` 创建或更新任务记录。
2. 在 `task_logs/INDEX.md` 登记日期、类型、状态和下一步。
3. 明确列出已完成、未完成、验收证据、风险和可拓展方向。
4. 只有形成里程碑时才追加 `CHANGELOG.md`。
5. 行动、业务线或待拍板变化时更新 `TODO.md`、`lines/` 或
   `decisions/PENDING.md`；随后运行生成器，禁止手改 `STATUS.md` / `NOW.md`。
6. 重复操作另写或更新 `runbooks/`，不要让历史任务日志承担活文档职责。
7. 原始运行输出放在 `outputs/<task-id>/`，任务日志只保留结论和链接。

## 命名规则

任务记录：

```text
progress/task_logs/YYYY/MM/YYYY-MM-DD__type__short-name.md
```

审计、决策和 incident 使用相同的年月分层和日期前缀。

## 并行写入

- 同一个 task log 只允许一个写者。
- 代理写入前先检查 `task_logs/INDEX.md` 和目标路径；发现 ID 已占用时使用下一序号。
- 并行代理各写自己的 task log，由主控统一合并 INDEX、TODO、lines、PENDING 和
  CHANGELOG，再生成 STATUS/NOW。
- 不覆盖另一代理刚生成的记录；发生同主题重复时先比对，再保留信息完整且已被索引的版本。

## 安全规则

- 不记录真实 API Key、访问令牌、Cookie 或完整凭据。
- 不把大量原始命令输出直接粘贴进任务日志。
- 关键结论必须区分“已验证”“推断”“未验证”。
- 历史记录只做勘误；状态变化通过追加 amendment 或新任务记录表达。
