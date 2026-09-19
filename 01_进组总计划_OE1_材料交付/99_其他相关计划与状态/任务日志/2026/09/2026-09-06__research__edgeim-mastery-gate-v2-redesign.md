# EdgeIM Mastery Gate v2 重构（TASK-20260906-001）

**日期**：2026-09-06
**状态**：`done`（文件落盘；§8 四项 flag 待拍板）
**任务**：`TASK-20260906-001`

## 背景

09-05 晚一个窗口在模型问题下（两次 `/model` 切换回执均为"saved as default for new sessions"，疑似当前会话未热切换）写出了 EdgeIM Mastery Gate 重写稿，落盘于 `progress/decisions/2026-09-05__research__edgeim-mastery-gate-and-learning-restructure.md`，并留交接文档 `progress/handoff/2026-09-05__edgeim-mastery-gate-rewrite__wrong-model-handoff.md` 待新窗口用正确模型复核。

本窗口（确认为 Fable 5 max effort）接手后，核对发现该草稿与同日更早由 Codex 执行、用户已批准的 `TASK-20260905-001`/`TASK-20260905-002`（EX-00 v2 §6 唯一现行门 + 四论文十字训练闭环 `FOUR_PAPER_TRAINING_LOOP.md` 的分时镜头解锁）存在时间线冲突：草稿的 Week 1-4 计划未引用后者，且直接假定 sigRank/Ground Truth/CrossEdgeIM 可立即挑选，与后者的 L-S1…L-CX2 锁点冲突。

用户拍板：**B**——两案冲突不需要弥合考据，「实际执行已经过了 EX-3，直接做，重点是要重构整个方案」。

## 核对

- 磁盘现状：`_sealed/` 下 EX-00/01/02/03/05/05a 六份答案齐全（EX-02 答案 09-05 09:34 更新）；`EX-04/` 目录不存在；EX-06/07 只有题面无密封答案。
- BRIEF.md 台账字面仍写"当前唯一游标仍是 EX-00 v2 §6 脱稿"——与用户口径（已过 EX-3）不一致，判断为台账滞后未跟手速，不是执行倒退。本次未回改 BRIEF 原文，差异原样挂 flag 写入新文件，不悄悄抹平。

## 产出

- 新文件：`learning/training/lu-edgeim-algo1/MASTERY_GATE.md`（v2，取代旧决策文件的内容判断部分）
  - 六道门（Whole-paper reconstruction / Algorithm ownership / Formal-object mastery / Claim-evidence audit / Attack mode / Interview compression）
  - 双线程学习节奏（纵向深挖 + 横向接回整篇）
  - OWNED 判定七问，对已完成的 EX-00~EX-03 同样补做回测（不是只对新内容生效）
  - 现状诊断优先：Whole-Paper Diagnostic 15 题，先测掉包位置再决定后续深挖顺序，不机械重做旧站
  - 源框架五分枝 ↔ 现有 `FOUR_PAPER_TRAINING_LOOP.md` 十字结构映射表（不重造分枝体系，只叠加六道门检验标准）
  - 进组面试新最低线七条
  - 附录：formal-object 五层表、claim-evidence 审计表、attack mode 清单、四档话术模板、面试模拟题库
- 旧文件 `progress/decisions/2026-09-05__research__edgeim-mastery-gate-and-learning-restructure.md` 状态行改为 `SUPERSEDED`，指向新文件，原文保留不删。

## 未决（写入新文件 §8，不在本次处理）

1. `EX-04/` 目录缺口：补建站点 vs 内容并入诊断题库，待定。
2. BRIEF.md 游标字面 vs 用户口径差异：是否需要单独 BRIEF amendment，待定。
3. Whole-Paper Diagnostic 15 题执行时间，待用户口令。
4. 源框架 Week 1-4 冲刺日程（写的是 09-05~09-30）是否需按当前日期（09-06）重排，待定。

## 不受影响

- `TASK-20260904-004`（EdgeIM 学习包增量升级）仍是 PAUSED，本次未触碰。
- `FOUR_PAPER_TRAINING_LOOP.md` 原文未改，本次只在新文件里做映射引用。
- BRIEF.md 站序表（EX-00…EX-07）原文未改。

## 验收证据

- `learning/training/lu-edgeim-algo1/MASTERY_GATE.md`（新文件，本次落盘）
- `progress/decisions/2026-09-05__research__edgeim-mastery-gate-and-learning-restructure.md`（状态行已改 SUPERSEDED）

## 回滚

- 若需回滚，删除 `MASTERY_GATE.md` 并把旧决策文件状态行改回"执行中（v1.0 落地计划）"即可，无其他文件被本次改动触及。
