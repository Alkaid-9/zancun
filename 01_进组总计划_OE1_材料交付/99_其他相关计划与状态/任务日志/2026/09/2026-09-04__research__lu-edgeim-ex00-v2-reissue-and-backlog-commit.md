---
id: TASK-20260904-002
title: lu-edgeim-algo1 站 0(EX-00)从头换版为 v2 ＋ 09-01→09-04 四日存量统一入库
date: 2026-09-04
runtime:
  model: "Opus 5 (claude-opus-5[1M])"
  effort: max
  effort_source: "本会话 /model 输出确认「saved as your default for new sessions with max effort」"
  launch: "Claude Code CLI (WSL)"
type: research
status: completed_with_open_gates
area: learning/training · progress governance
project: lu-side
todo_ids: []
owners:
  - user
  - claude
related:
  - learning/training/lu-edgeim-algo1/BRIEF.md
  - learning/training/lu-edgeim-algo1/EX-00/README.md
  - learning/training/lu-edgeim-algo1/EX-01/README.md
  - learning/training/lu-edgeim-algo1/MISTAKE_LOG.md
  - progress/task_logs/2026/09/2026-09-04__research__research-system-overnight.md
  - progress/handoff/2026-09-04__research-system__window-handoff-snapshot.md
---

# 目标

两件独立但同窗完成的工作：

1. 按用户口令「不用管 sol 出的题啊，那个我觉得不太好用，所以是想让你从头再出（原来的 00 和 alg1 我写完了，直接贴在那个对应的 readme 上了）」，把 `lu-edgeim-algo1` 训练包站 0（EX-00）从 Sol 版（v0）整体换成本窗从头出的新题（v2），v0 不删除、原样归档；
2. 按用户口令「全部」，把 2026-09-01 至 09-04 累计四天、跨 8 条以上独立线的未提交改动一次性 commit 入库，同时排查并处理其中的 git 风险点。

两件工作边界独立：EX-00 换版不涉及 git 操作；四日存量 commit 覆盖的是本窗与此前多个会话留下的存量改动，多数文件内容并非本窗新写。

# 最终结果

**EX-00 换版**：v0 三件（`EX-00/README.md`、`EX-00/GRADING.md`、`_sealed/EX-00_answer.md`）原样搬到 `_v0_sol/` 子目录，搬移前后 sha256 前 12 位不变（`bde310271e55` / `a37c4285e6c9` / `80534f28667b`，已重新核实）。新写 v2 题面（新日志 L0，六条 trace c1–c6）、v2 密封答案、09-05 D+2 冷复测题（日志 K），修正 EX-01 两处指向 v0 的旧指针，并在 `BRIEF.md` 追加 Amendment 记录换版事实与依据。**站 0 仍未 PASS**——用户尚未提交 v2 的 Task 1-8 与 §6 脱稿作答，站 1 及以后维持锁定。

**四日存量入库**：`git commit da66308`，980 个文件（907 新增 + 73 修改）。commit 前发现并处理两个真实 git 风险：23 个第三方 vendored 仓库克隆（各带独立 `.git`，87K–279M）会在 `git add -A` 下产生失效 gitlink；一个扩展名为 `.html` 但 magic bytes 实为 PDF 的下载件违反既有 PDF 不入库政策。两者均已加入 `.gitignore` 排除，磁盘原样保留、未删除。未 push——push 仍是另一道独立口令。

# 修改内容

## EX-00 换版

- `EX-00/_v0_sol/README.md`、`EX-00/_v0_sol/GRADING.md`：v0 原文件原样迁移（用户已贴出的作答 + 175f2aa3 窗批改）
- `_sealed/_v0_sol/EX-00_answer.md`：v0 密封答案原样迁移
- `EX-00/README.md`（176 行）：v2 新题面——新日志 L0（六条 trace c1–c6，五活动 a-e）、§1-3 教学 + Algorithm 1 逐字抄录、Task 1-8（含"改一个条件""为什么没有 K"两组关键任务）、§5 桥接 L1、§6 脱稿
- `_sealed/EX-00_answer.md`（115 行）：v2 密封答案，含每题判分点、常见错误预判、追问库 Q1-Q5
- `_sealed/EX-00_retest_D2.md`（43 行）：09-05 D+2 冷复测题，日志 K（k1-k5，五活动 u-y），已密封
- `EX-01/README.md`（221 行）：§0 进门票不再指向 v0 GRADING.md 的追问 A-E（已作废），改指 v2；§4.4"一个诚实的说明"改指 `_v0_sol/README.md:445-453`（路径挪动后同步）
- `BRIEF.md`：文末 Amendment A2，记录换版事实、口令来源、OS §7 依据、PASS 条件不变、冷复测日期不变
- 所有数字来源：`_sealed/EX-05a_algo1_ref.py` 实跑 + 独立枚举脚本 `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__ex00-v2-verify.py`（L0 720 种顺序全枚举、K 120 种全枚举），非手推

## 四日存量入库

- `.gitignore` 新增两条排除：`research/tracebridge_full_spectrum_20260830/08_materials/oss_datasets_standards/repos/`（23 个 vendored git clone）、`.../academic_openreview/files/W1A-S034.html`（伪装 PDF）
- `git add -A` 后 `git commit da66308`：980 文件，覆盖训练包换版、科研体系通宵窗（TASK-20260904-001）产出、EvoAgent EA-4、jiang 归档收口、Kaggle KG-1、工作台 v2 契约与追加批、M0-M3 收尾勘误、edgeim_sampling_audit 冻结取证、shuorenhua skill 接入说明、08-30 全局上下文治理审计与 C-P0 收尾等跨线内容（详见 commit message 全文）

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| v0 三件哈希不变 | 搬移前后 sha256 前 12 位一致 | PASS | `bde310271e55` / `a37c4285e6c9` / `80534f28667b`，本次 commit 前重新核实 |
| v2 数字非手推 | 每个 D′/(S,E,R) 结果有可复跑脚本支撑 | PASS | `_sealed/EX-05a_algo1_ref.py` 实跑 + `2026-09-04__ex00-v2-verify.py` 全枚举 |
| G0 答案未泄漏 | v2 题面文件不含 §6 脱稿的密封答案内容 | PASS | 密封答案单独存于 `_sealed/`，题面文件（EX-00/README.md）与 EX-01 均未夹带答案 |
| EX-01 指针修正 | 两处引用 v0 路径的地方已改指 v2/新路径 | PASS | `EX-01/README.md` §0、§4.4 已读取确认 |
| commit 前无失效 gitlink | vendored repos 不以 gitlink 形式进入 HEAD | PASS | commit 后 `git diff --cached --name-only \| grep -c "oss_datasets_standards/repos/\|W1A-S034.html"` = 0 |
| commit 前无凭据 | 全量 diff 扫描常见密钥前缀（AWS/OpenAI/GitHub/Slack/PEM） | PASS | 扫描零命中 |
| commit 前 HEAD 未被并发窗口移动 | 分阶段核对 `git rev-parse HEAD` 恒等于 `3779b81` | PASS | 三次核对（investigate 时、`.gitignore` 改动前、`git add -A` 前）均为 `3779b81075ba91bfc80d188c410166dde8359f07` |
| commit 后仓库无失控膨胀 | `.git` 目录大小与 insertion 数字有正当解释 | PASS | `.git` 528M；1.5M insertion 主因是 6 个 ~4.5MB 的 `teardown-joint-20260813` 实验 `metrics.json`（F1 propagation 08-24/08-25/08-27 三轮跑），非误入内容 |
| 站 0 PASS 判定 | 用户交 v2 §6 脱稿作答并通过密封答案判分 | 未开始 | 待用户交作答 |

# 当前状态

- EX-00 站在"v2 题面已出，等用户作答"节点；EX-01 及以后全部锁定不可看
- `MISTAKE_LOG.md` #1 仍 OPEN，等 09-05 冷复测过了用户亲手改 CLOSED
- 四日存量已进入本仓 git 历史（`da66308`），工作树与 HEAD 一致，无残留未提交的相关改动；两个 vendored/伪装 PDF 路径已被 `.gitignore` 排除但磁盘原样保留
- 未 push；仓库当前领先 `origin` 若干个 commit（含本次），push 需另外口令

# 尚未完成

- 用户尚未提交 EX-00 v2 的 Task 1-8 与 §6 脱稿作答——这是本任务链条上唯一的实质阻塞项，且阻塞方是用户，不是 AI
- 09-05 D+2 冷复测（日志 K）尚未进行，需等 v2 首次判分通过后按计划触发
- `progress/TODO.md` 目前只有 TR-1 泛用阅读计划行提及 EdgeIM，没有专门指向 `lu-edgeim-algo1` 训练包本体（BRIEF/EX-00 v2/站序）的独立 TODO 行；是否需要补一行未与用户确认
- push 未授权，仍是独立开放门

# 下一步

1. 用户完成 EX-00 v2 §6 脱稿作答后提交
2. 按 `_sealed/EX-00_answer.md` 判分点批改，若通过则等 09-05 用 `_sealed/EX-00_retest_D2.md` §A 做冷复测
3. 冷复测通过后用户亲手将 `MISTAKE_LOG.md` #1 改为 CLOSED，站 0 关闭，站 1（EX-01）解锁

# 可拓展方向

- 可评估是否需要在 `progress/TODO.md` 挂一条专属训练包行（当前只有泛用 TR-1 行覆盖）
- 四日存量 commit 的内容分散在 8+ 条线，事后如需单独追溯某条线的独立历史，可考虑用 `git log --follow` 配合路径过滤，而非依赖这一笔大 commit 的 message

# 风险与回滚

- 风险：`da66308` 是一笔跨越 8+ 条独立工作线的大 commit，日后若某条线需要单独 revert，只能用路径级 `git checkout <commit>^ -- <path>` 手动还原，不能整体 revert 而不影响其他线；这是用户明确选择"全部一次提交"（而非分线多笔）后的已知代价，已在响应中向用户说明
- 风险：`.gitignore` 新增的两条排除规则依赖当前磁盘路径不变；若 vendored repos 目录改名或那个伪装 PDF 文件改名，需要同步更新 `.gitignore`，否则会重新被 `git add -A` 纳入
- 回滚：EX-00 换版可通过 `git show 3779b81:learning/training/lu-edgeim-algo1/...`（换版前状态在本次大 commit 之前不存在于 git 历史，因为训练包本身是本次一并入库的新内容）——实际回滚路径是磁盘上 `_v0_sol/` 与 `_sealed/_v0_sol/` 的原样归档，不依赖 git；四日存量 commit 若需整体撤销，`git reset --soft da66308^` 可回退到提交前状态（工作树不受影响，因为改动本就来自工作树）

# 文件和产物

- `learning/training/lu-edgeim-algo1/BRIEF.md`
- `learning/training/lu-edgeim-algo1/EX-00/README.md`
- `learning/training/lu-edgeim-algo1/EX-00/_v0_sol/README.md`
- `learning/training/lu-edgeim-algo1/EX-00/_v0_sol/GRADING.md`
- `learning/training/lu-edgeim-algo1/EX-01/README.md`
- `learning/training/lu-edgeim-algo1/_sealed/EX-00_answer.md`
- `learning/training/lu-edgeim-algo1/_sealed/EX-00_retest_D2.md`
- `learning/training/lu-edgeim-algo1/_sealed/_v0_sol/EX-00_answer.md`
- `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__ex00-v2-verify.py`
- `.gitignore`
- commit `da66308fb34abb8f93c40be07de119231914c7e2`

## Amendment

历史记录不重写。后续状态变化在此追加。
