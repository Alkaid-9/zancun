# Bridge → 鲁组 R1 Pilot：跨窗口交接

**Date**: 2026-09-03 Asia/Taipei  
**Status**: `PAUSED / RECOVERABLE / PILOT-FINDING-SAVED / NO-EXECUTION-AUTHORITY`  
**Authority**: 用户 controller 已批准 R1；当前 pilot 已主动收口，未授权继续扩展。  
**Task**: `TASK-20260830-004`

## 1. 当前结论

已完成一个窄的、真实运行过的 R1 pilot slice。当前核心观察是：在局部 DFG-edge legality 的 recording-perturbation setting 下，低预算 greedy DFG-coverage sampling 可能优先保留 contaminated traces，因为非法扰动产生的 forbidden/new edges 与 novelty objective 对齐。

这不是 EdgeIM 的 faithful reproduction，也不是 coverage 普遍不鲁棒的结论。

## 2. 关键权威文件

1. `progress/decisions/2026-09-03__research__bridge-lu-execution-plan-v1.0.md`：总体计划与 09-20/09-25 目标。
2. `progress/decisions/2026-09-03__research__bridge-segment0-execution-brief.md`：Segment 0 作业书。
3. `research/tracebridge_full_spectrum_20260830/00_control/BRIDGE_LU_PLANNING_LOG.md`：C-040–C-068 决策与游标。
4. `research/edgeim_sampling_audit/results/CURRENT_FINDING_NOTE.md`：当前 pilot finding 与 claim ceiling。
5. `research/edgeim_sampling_audit/results/genuine_multi_universe.json`：10-universe 原始输出。
6. `research/edgeim_sampling_audit/scripts/genuine_multi_universe.py`：pilot 生成/比较脚本。
7. `research/edgeim_sampling_audit/src/harness.py`、`tests/test_harness.py`：最小 sampler/harness 与测试；当前测试 `19 passed`。

## 2a. 最早的计划/方向档

用户指定的最早学习/科研 OS 文件为：

`learning/2026-09-03__learning-research-os-v0.1.md`

该文件已根据用户提供的完整正文重新落盘并核验存在；当前状态为 `FROZEN / USER-PROVIDED-CONTENT-RESTORED`。新窗口恢复时应先读取该文件，不得在周复盘之外自行修改或升级其状态。

本链最早的正式落盘入口是：

`progress/task_logs/2026/08/2026-08-30__research__bridge-lu-two-week-masterplan-alignment.md`

随后收缩与重设计的关键历史档是：

`progress/decisions/2026-09-02__research__bridge-requirements-realignment-and-edgeim-slice-proposal.md`

这些文件保留作历史来源，不覆盖当前 C-068 finding；恢复时先以本 handoff、当前规划日志和 `CURRENT_FINDING_NOTE.md` 为现状依据，需要追溯方向来源时再读上述历史档。

## 3. 已完成

- Segment 0 四表：论文核对、Measurement Contract、CORE/ADJACENT、时间倒排。
- W2：`FROZEN / PASS`。
- W3 第一 harness Gate：`PASS WITH KNOWN LIMITATIONS`。
- random baseline 与 deterministic greedy coverage sampler。
- fixed-K matched comparison。
- 10-universe generator/provenance smoke + 修复：独立 RNG、真实 illegal insertion、candidate indices、shuffle identity、no-candidate generation error。
- C-057 fixed-universe permutation diagnostic：已关闭，不作为 evidence。
- C-064 generator/provenance audit：PASS。
- C-068 finding note：已落盘。

## 4. 当前 pilot 数字（探索性）

| K | Coverage noise proportion | Random mean |
|---:|---:|---:|
| 2 | 0.950 | 0.630 |
| 4 | 0.600 | 0.505 |

这些数字仅适用于当前 synthetic setting，不应外推。

## 5. 未完成的原计划项目

- 用户本人完整核心论文深读与 paper note ownership 验收；
- CORE foundation 的独立 hard evidence；
- D+2 / D+7 ownership 复测；
- README、一页 brief、贡献账本、公开仓库、冷邮件；
- 09-20 核心冻结和 09-25 包检尚未满足。

## 6. 下一步（若恢复）

先不写代码。由用户决定是否继续 R1。若继续，优先从论文/定义 ownership 开始；如扩展实验，首选 K interaction 或 edge-preserving-but-globally-illegal anomaly，但必须另行确认，不得自动执行。

## 7. 禁止越界

- 不继续扩 harness 或新增 Gate；
- 不修改冻结 W2 Measurement Contract；
- 不把当前 pilot 写成 faithful EdgeIM reproduction；
- 不把结果写成 coverage 一般不鲁棒；
- 不自动扩大 universe、seed、扰动类型或实验矩阵；
- 不公开仓库、发邮件、commit/push，除非用户重新授权。

## 8. 恢复第一动作

读取本 handoff → 读取 `BRIDGE_LU_PLANNING_LOG.md` C-068 → 读取 `CURRENT_FINDING_NOTE.md` → 先向用户确认是否继续 R1，不直接运行代码。


