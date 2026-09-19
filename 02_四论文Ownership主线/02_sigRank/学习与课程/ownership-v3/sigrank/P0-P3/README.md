# sigRank P0-P3 Full-Paper Package

**资产状态**：BUILT-WITH-ERRATA；学习状态继承 L-S1/L-S2
**论文**：sigRank PDF physical pp.1-13
**硬边界**：工作证据无 2500 字上限；最终闭卷摘要可另交且不替代 coverage

## P0 全文地图

H0 重建 problem、constraints、两阶段方法、实验主线、limitations、related work 和 conclusion；再逐行完成
[Coverage Matrix](../COVERAGE_MATRIX.md)。所有 Abstract/Introduction/Results/Conclusion major claims 必须入表。

## P1 机制 ownership

1. 重建 Definitions 1-6、Eq.1-8 和 prose Step 1-4。
2. 完成 [训练微例](TRAINING_FIXTURE.md)，逐 trace 计算 activity/DFR significance、Eq.4-6、rank 和 sample。
3. 分清 trace multiset、trace-position average 与“support numerator 每 trace 只计一次”。
4. rounding、boundary tie、duplicate variant、singleton 除零只可声明 policy 或 SOURCE-OPEN。
5. 关闭材料重做，再完成未见 log/budget 变体。

## P2 evidence ownership

1. 重建 12 logs、9 methods、ratio/IMi 映射、固定 miner、metrics、五次运行和时间口径。
2. 复核代表性 Table I/II/III/Fig.6 单元，并把 [Source Register](../../SOURCE_REGISTER.md) 的三条 errata 纳入 discrepancy ledger。
3. 审计全部 major claims；`10/12`、`100x`、complexity 和 guarantee 不能沿用作者句子后直接通过。
4. 区分 F-measure、Eq.8 quality ratio、per-ratio 结果和六 ratio aggregate。

## P3 attack + defense

1. 改一个 budget/objective/frequency 假设，先预测 rare-critical、tie 或 consumer mismatch 会怎样。
2. 与 EdgeIM 比较时只用 matched interface、matched retained count 或 matched total cost；选择一种并说明另一种没回答的问题。
3. 消费 Shared Artifacts 里的 EdgeIM Sampling/Selection 行，回写 sigRank delta。
4. 完成 30 秒/2 分钟/10 分钟表达和 D+2/D+7。

## 提交

Coverage、Evidence Record、手算/最小实现、protocol、all-major-claim table、attack、fair-comparison contract、共享矩阵 delta 和全文回接句。
