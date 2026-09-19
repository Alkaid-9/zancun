---
id: TASK-20260912-004
title: EdgeIM EX-03 app learning progress checkpoint
date: 2026-09-12
runtime:
  model: Codex
  effort: n/a
  effort_source: current managed session; exact reasoning setting unavailable
  launch: Codex app
type: archive
status: completed_with_open_gates
area: learning
project: lu-side
todo_ids: []
owners:
  - user
related:
  - learning/training/lu-edgeim-algo1/MASTERY_GATE.md
  - learning/training/lu-edgeim-algo1/BRIEF.md
---

# 目标

在共享脏工作树中，只归档用户通过 app 学到 EX-03 时留下的原始作答和可复跑代码；不把该快照升级为站点 PASS、OWNED 或 RETAINED，也不夹带学习包改写和其他窗口改动。

# 最终结果

完成一个窄范围 WIP checkpoint。当前口径仍是 `EX-03 USER-REPORTED / NOT PASS`；正式恢复入口是 `MASTERY_GATE.md` 第 4.2 节 Whole-Paper Diagnostic，而不是从 EX-00 机械重学。

# 修改内容

- 保存 EX-02、EX-03 的原始学习记录。
- 保存 EX-02 的 PM4Py 对照脚本，以及它实际导入的 EX-05a Algorithm 1 实现。
- 保存 EX-05a 的独立正逆序复测脚本。
- 未修改或提交题面 README、sealed answers、LEDGER、MISTAKE_LOG、后续站空骨架、共享生成视图及其他研究窗口文件。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| EX-02 脚本可运行 | solver Python 退出码 0 | PASS | `python learning/training/lu-edgeim-algo1/EX-02/answer.py`；D/D' 首次在 `t=0.3` 分岔 |
| EX-05a 复测可运行 | solver Python 退出码 0 | PASS | `python learning/training/lu-edgeim-algo1/EX-05a/retest.py`；正序 1/2/3/6、逆序 6/5/4、`S/E/R` 相同 |
| 提交边界 | 只暂存白名单路径 | PASS | 提交前后检查 `git diff --cached --name-status` |
| 学习能力判定 | 有无整篇诊断与延迟冷复测 | OPEN | 15 题诊断尚未执行；本快照不得作为 PASS/OWNED 证据 |

# 当前状态

仓库为 `master@bf9f45c` 起始基线，相对 `origin/master` 原先 ahead 11。工作树另有大量其他窗口改动，本任务全部保留且不暂存。学习文件中的 AI 解释、纠正和答案暴露如实保留为原始过程，因此最多证明 `SEEN` 和一次可复跑记录。

# 尚未完成

- 未执行 Whole-Paper Diagnostic 15 题，无法确定实际需要回补的 2-4 个缺口。
- 未对 EX-00 至 EX-03 做七项 OWNED 回测和延迟 cold retest。
- 未独立确认 EX-03 PASS；不写 `learning/training/LEDGER.md`。
- `EX-02/answer.py` 导入 `EX-05a/algo1.py` 时会执行该文件的顶层示例并打印额外输出；本次按原始学习状态归档，不作代码清理。

# 下一步

1. 在 60-90 分钟内闭卷完成 `MASTERY_GATE.md` 第 4.2 节 15 题诊断，逐题标 `OWNED / SEEN / OPEN / UNKNOWN`。
2. 只选 2-4 个最高价值缺口，按冻结依赖回到对应站补手算、预测、本人最小实现和反例。
3. 完成至少一次关闭旧答案与聊天后的延迟复测，再决定是否继续 EX-05。

# 可拓展方向

- EX-01 已解锁的 sigRank L-S1 横向镜头可在诊断后按缺口安排，但不能替代 EdgeIM 主干证据。
- EX-06 后再接 Ground Truth 和 CrossEdgeIM；JINZU 材料只消费已验证的本人证据。

# 风险与回滚

- 风险：原始记录混有 AI 解释，容易被误读为用户独立作答。所有状态保持 `USER-REPORTED / NOT PASS`。
- 风险：共享工作树同时含其他任务改动。提交使用逐文件白名单和仅索引单行的 staged patch。
- 回滚：该 checkpoint 为独立提交；需要撤销时只反向该提交，不触碰其余未暂存改动。

# 文件和产物

- `learning/training/lu-edgeim-algo1/EX-02/ans.md`
- `learning/training/lu-edgeim-algo1/EX-02/answer.py`
- `learning/training/lu-edgeim-algo1/EX-03/answ-ex03.md`
- `learning/training/lu-edgeim-algo1/EX-05a/algo1.py`
- `learning/training/lu-edgeim-algo1/EX-05a/retest.py`
- `progress/task_logs/2026/09/2026-09-12__learning__edgeim-ex03-app-progress-checkpoint.md`

## Amendment

无。
