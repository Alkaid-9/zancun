---
id: TASK-20260913-001
title: 四论文全文 Ownership v3 Sol 施工合同
date: 2026-09-13
runtime:
  model: Codex
  effort: n/a
  effort_source: current managed Codex session; exact reasoning setting unavailable
  launch: Codex app
type: research
status: completed_with_open_gates
area: learning
project: lu-side
todo_ids: []
owners:
  - user
  - Codex
related:
  - progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md
  - progress/decisions/2026-09-12__research__four-paper-full-ownership-design-for-sol.md
  - learning/training/lu-edgeim-algo1/START_HERE.md
  - learning/training/lu-edgeim-algo1/MASTERY_GATE.md
  - learning/training/lu-edgeim-algo1/FOUR_PAPER_TRAINING_LOOP.md
---

# 目标

在不触碰用户当前 EX-05 作答、不替用户补前半程联动、不修改共享学习正本的前提下，把四篇论文全文 ownership 方案重构为可交 Sol 施工的 v3 合同。核心是分离课程建设、学习执行、PASS、RETAINED 和 OWNED，并允许课程资产建设与用户当前补漏/推进并行。

# 最终结果

已新增独立 v3 施工合同。它不覆盖 Fable 前版，而是把前版作为历史输入；明确 Sol 第一阶段只写 `learning/training/lu-edgeim-algo1/ownership-v3/`，不得修改现有站点、用户答案、Ledger 或共享正本。合同补齐分阶段诊断、全文覆盖矩阵、primary-source 规则、提示等级、反馈后重做、未见 holdout、延迟冷测、四篇共享产物、EdgeIM 桥接顺序、三篇论文适配器、Sol 交付树和十项主控验收标准。

# 修改内容

- 新建 `progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md`。
- 记录用户当前位于 EX-05 语义站点，以及前半程 G0/CONNECT/L-S1/SR/EC/全文回接/Ledger 冷测漏项的责任边界。
- 将完整十五题从“Sol 施工前置”改为最终 D2；当前 D0 只做已学范围恢复，D1 在 EdgeIM 全管线教学后执行。
- 将 `EX-08~EX-11` 后置编号改为 B-S2/B-S3A/B-S3B/B-EVAL/B-DEFENSE 概念桥接模块，并提供当前学习者迁移规则。
- 将三篇 2500 字单稿改为 P0 全文地图、P1 机制、P2 evidence、P3 attack/defense 四阶段。
- 加入两条独立状态轴和 Sol 第一阶段独立写域，禁止施工状态自动升级用户能力状态。
- 未修改 Fable 前版、现有学习正本、EX 题面、用户作答、sealed、Ledger 或 Mistake Log。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 当前站识别 | 不由历史文件名误判站点 | PASS | `EX-05/README-EX04.md` 第 1、21 行均定义为 EX-05/第 5 站 |
| G0 缺口 | 确认题面要求且产物未见 | PASS | `EX-01/README.md` §5；仓内 glob 未找到 `G0_user_paper_note.md` |
| 联动提交 | 区分卡存在与用户提交存在 | PASS | `CONNECTIONS.md` 有 C00/C01/C05a/C02；既有非 sealed 作答 grep 未见 CONNECT/SR/EC/L-S1 记录 |
| Ledger 事实 | 不沿用前版“不存在”错误 | PASS | `learning/training/LEDGER.md` 当前存在且含历史行 |
| 写域隔离 | 不碰用户活跃学习文件与 Fable 文件 | PASS | 本任务只新增 v3 decision、task log，并登记自身 INDEX 行 |
| 合同完整性 | 覆盖施工、学习、验收、复测和跨论文回写 | PASS | v3 §2-§10 |
| 用户能力边界 | 不代写、不倒填 PASS/OWNED | PASS | v3 §1.3、§2、§8-§10 |

# 当前状态

- 中央 allocator 在当前会话签发 `TASK-20260913-001`；任务号日期采用 allocator 结果，虽然 America/Los_Angeles 当前仍为 2026-09-12。
- 用户学习文件正在被其他窗口/用户修改，本任务全部保留且未触碰。
- v3 已达到 `READY-FOR-SOL-HANDOFF`；尚未下发 Sol、尚未建设 `ownership-v3/`、尚未修改共享入口。
- Fable 前版仍保留，不在本任务中回写或修错。

# 尚未完成

- Sol 尚未按合同建设任何课程资产。
- 用户尚未逐项冻结各模块最终 rubric。
- `TASK-20260906-004` 的 INDEX 与自身 task log 状态冲突尚未统一。
- EdgeAlpha primary source 当前未见于 `research/papers_lu/`；对应独立比较保持 `SOURCE-OPEN`。
- 用户自己的 G0/CONNECT/L-S1/SR/EC/全文回接/冷测仍由用户完成，本任务不验收其内容。

# 下一步

1. 将 v3 作为 Sol 唯一施工入口下发，第一阶段只允许写 `ownership-v3/` 和 Sol 自己的 task log。
2. Sol 先交 coverage matrices、模块目录、rubrics、fixtures/holdouts 和 BUILD_RECEIPT，状态停在 `BUILT`。
3. 主控按 v3 AC-01 至 AC-10 独立复核；通过后再处理共享入口接线。
4. 用户继续当前恢复线和 EX-05/EX-06；新模块 QA-PASS 后按迁移规则补学。

# 可拓展方向

- D2 的最终冷诊断题库应在课程完成后单独密封生成，避免复用已暴露十五题。
- EdgeAlpha primary source 的取得和核验可以单独立项，不夹进 Sol 第一阶段施工。

# 风险与回滚

- 风险：共享工作树存在大量其他窗口未提交改动；本任务通过新增独立文件、限制未来 Sol 写域规避覆盖。
- 风险：详细课程资产可能再次被误报为用户能力；v3 用双状态轴和 Ledger 禁写规则隔离。
- 回滚：删除本任务新增的 decision、task log 和对应 INDEX 行即可；现有学习包不受影响。

# 文件和产物

- `progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md`
- `progress/task_logs/2026/09/2026-09-13__research__four-paper-full-ownership-v3-sol-contract.md`

