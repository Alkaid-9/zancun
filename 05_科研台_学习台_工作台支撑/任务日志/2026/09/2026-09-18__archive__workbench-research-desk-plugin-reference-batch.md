---
id: TASK-20260918-002
title: 工作台/科研台/考研插件参考批存档（R13/R14）
date: 2026-09-18
runtime:
  model: Opus 4.6[1M]
  effort: max
  effort_source: ~/.claude/settings.json effortLevel=xhigh + CLAUDE_CODE_EFFORT_LEVEL=max
  launch: Claude Code 交互会话
type: archive
status: done
area: research-desk / workbench
project: research-desk
todo_ids: []
owners:
  - user
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
  - progress/decisions/2026-09-17__research__two-desks-purpose-redefinition-proposal.md
  - progress/task_logs/2026/09/2026-09-17__engineering__two-desks-base-trial.md
---

# 目标

用户压缩前贴出一批 Obsidian 插件/仓库社媒帖内容（无原始链接，按名称核身份），随后压缩后又分三类（考研/工作台/科研）贴出确切 GitHub 链接批，并明确要求"存一下是工作台参考和科研台参考"。本任务把两批链接统一登记进项目现有唯一参考正本，不新开平行清单（吸取 `external-tool-reference-lists-fragmentation-20260917` 记忆的教训）。

同时，本任务作为本会话（压缩恢复后）第一个实质产出，先处理 SessionStart:compact 钩子报告的 `CONTEXT_RECOVERY_STATUS=UNVERIFIED / REASON=missing_binding`：核实该钩子机制（`tools/scripts/context_recovery.py`）后确认——本会话未曾对本仓 `.git` 顶层写过 `agent-context-recovery` 显式 binding（历史 binding 均属 codex 平台的其他 session_id，或更早的 claude session_id，与本 session_id 不匹配属预期，非异常）；已按压缩摘要逐项核对磁盘真相（见下）而非直接采信摘要断言，符合 `compaction-ground-truth-disk` 记忆的要求。

# 最终结果

已把用户两批链接（社媒帖转述 11 项 + 用户自选确切链接 14 项，两批合计经去重后新增 R13、R14 两个编号）追加进 `progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md`（§0 编号更新为 R01-R14 共 15 项 + I01；新增 §7.8.1/§7.8.2 两个子节）。R13 全部按名称 WebSearch 核实身份（10/11 找到高置信匹配仓库；"Lazy-Kaoyan-Library" 当时未找到）；R14 用户随后自己给出该项目确切链接，解决了 R13 的缺口，同时确认 R14 的 Research OS 链接与 R13 猜测的是同一个仓库（`kivvng726/obsidian-research-os`），身份置信度从"按名称搜到的候选"提升为"用户确认的目标仓库"。

# 修改内容

- `REFERENCE_NOTES_20260915.md` §0：编号统计从 13 项更新为 15 项，登记 R13/R14 两行摘要。
- 同文件 R01-R12 表格：追加 R13、R14 两行。
- 同文件新增 §7.8.1（R13 详表，11 个名称的 WebSearch 核实结果 + 帖子原始描述要点）、§7.8.2（R14 详表，按用户原始三分类"考研/工作台/科研"整理，含去重说明）。
- 本 task log 与 INDEX.md 对应行（见下）。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 不新开平行清单 | 追加进已有 R01-R12 正本而非新建文件 | 通过 | 本次仅 Edit 了 `REFERENCE_NOTES_20260915.md`，未 Write 新文件 |
| 身份核实而非直接采信帖子转述 | R13 每项跑 WebSearch，记录找到/未找到及同名歧义 | 通过 | §7.8.1 表格逐项标注核实仓库 URL 及"未核实项"说明段 |
| 用户分类原样保留 | 不擅自把用户的"工作台/科研台"归类改判 | 通过 | §7.8.2 按用户原始三分类（考研/工作台/科研）呈现，仅在表后加"仅观察非选型结论"的初步定位，不改分类本身 |
| 共享登记面用 ledger_edit.py 保形写入 | TODO.md/INDEX.md 不整文件重写 | 通过 | 见下方命令与哈希 |
| 铁律8：用户单发内容必列 TODO | 批量插件/工具在 TODO.md 单独一行挂项 | 通过 | 见下方 TODO.md 新增行 |

# 当前状态

`REFERENCE_NOTES_20260915.md` 现含 R01-R14 + I01 共 15 项外部参考登记，仍是 `ARCHIVED / REFERENCE-ONLY / NO-ADOPTION-OR-RUN-AUTHORIZATION`——本次只登记、核身份、按用户分类整理，未安装任何插件、未选型、未修改 NotEMD/LearnGraph 试用范围。

另：本次顺带核实了 `two-desks-trial-20260917` 服务当前状态——18880/18881/8878 三个端口均不可达（用户确认"昨晚试了下"与"就这样"，与只跑过一次、之后停止的事实一致），`materials/` 独立仓已推送到 `Alkaid-9/Research-Garden`（本地 HEAD 与远端一致）。此为核实记录，不属于本任务的写域变更。

# 尚未完成

- R13/R14 中多个同名/相邻仓（Research OS 系、obsidian_math 衍生仓、Apex Dashboard 双仓、Editing Toolbar 双仓、Claudian 多个镜像���未核实彼此的 fork/血缘关系，也未确认用户帖子里的截图/描述具体对应哪一个。
- 全部 R13/R14 项目均未安装、未 clone、未做与 NotEMD/LearnGraph 试用架构的接口比较。
- 是否真正采纳其中任何一项作为工作台或科研台底座，未决，等用户后续拍板。
- `two-desks-purpose-redefinition-proposal.md` §7/§8（此前 Codex 会话续写）与本会话对用户"两轮生长/工业权重/主线"表述的理解已核对一致，未发现冲突，故本次不重复改写该提案文档；如后续需要正式回应 industry-weight 具体机制或"个人主线"是否需要独立 schema 字段，仍需用户在 §7.5 基础上进一步拍板。

# 下一步

1. 用户后续若要对 R13/R14 中某几项做真实试用或深评，参照 §7.5（TASK-010 深评格式）逐项固定版本号、只读源码核对，不批量安装。
2. 若确认某工作台候选与已批的 NotEMD/LearnGraph 试用产生角色重叠（如 Custom Frames/Claudian 都可能承载"AI 嵌入 vault"这一角色），需先回到 `two-desks-purpose-redefinition-proposal.md` §3 的槽位表判断归属，不重复选型。
3. `research/map/*RESTRUCTURING_20260917*`（disconnected 的第二套知识图谱设计）与既有 v0.2/v0.3 菌丝网设计的调和，仍是本会话之前发现但未处理的独立缺口，本任务不代为处理。

# 可拓展方向

- 若未来 R13/R14 项目数量持续增长，可考虑把"社媒帖转述批"与"用户确切链接批"的两段式记录方式固化为该清单的标准追加格式（本次已在 §7.8.1/§7.8.2 首次示范）。

# 风险与回滚

仅追加内容到既有 decisions 文档 + 新增一份 task log + 两条共享登记面行；未删除任何既有内容。回滚：`git diff` 定位本次追加的 §7.8.1/§7.8.2 与 §0 编号变更，可整体 revert 该文件的本次 diff hunk；INDEX.md/TODO.md 新增行可用 `ledger_edit.py --replace` 单行撤回。

# 文件和产物

- `progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md`（本次编辑）
- 本文件
- `progress/task_logs/INDEX.md`（新增一行，见 Amendment）
- `progress/TODO.md`（新增一行，见 Amendment）

## Amendment

### 2026-09-18 — 收尾回执

- `progress/task_logs/INDEX.md`：`ledger_edit.py --insert-after` 在 `TASK-20260917-007` 行后插入本任务行，CAS 前置哈希 `7c3e1a4f68b0980d33eaa0e3db1c1392934786bee61661daa7618ae7888ccada`，写入回读 VERIFY-OK，落盘后 `--check` 复验哈希 `3e1996f0041a945cabb35306dc275f9b2b91f553bbe449a3933b7984e28b9a7f`，纯 CRLF 329 行尾（较写入前 328 行 +1，符合预期）。
- `progress/TODO.md`：`ledger_edit.py --insert-before` 在 `RD-1` 行前插入新条目 `RD-3`，CAS 前置哈希 `c68b733ea394d2d97ffa19de0151077328a346f9225ca472cec9afce33524b93`，写入回读 VERIFY-OK，落盘后 `--check` 复验哈希 `75a1d1facfd3fdc3d8f27ca2c767a829e3b5a7b326891b9eb585002d8f5f01b8`，纯 LF 834 行（较写入前 833 行 +1，符合预期）。
- 两次写入均未触发行尾混杂拒绝，未使用 `--normalize`，说明未与其他窗口的并发写产生冲突。
- `git status --short` 在写入前确认 `progress/TODO.md`、`progress/task_logs/INDEX.md` 均已是 `M`（他窗口此前已有未提交改动）；本次追加内容前未 reset 或覆盖既有改动，只在原有基础上单行插入。本次未 commit、未 push，遗留的多窗口未提交积压问题不在本任务处理范围。
