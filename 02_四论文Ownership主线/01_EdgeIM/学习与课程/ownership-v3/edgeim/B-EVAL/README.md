# B-EVAL - Experiment and Claim Audit

**资产状态**：BUILT-WITH-SOURCE-OPEN；学习状态默认 LOCKED
**论文坐标**：EdgeIM PDF pp.5-7，section V、Eq.4、Tables I-III
**前置**：EX-06 measurement contract；EX-07 最终 verdict 前

## 目标

能重建“数据、预处理、miner、参数、环境、重复、输出、指标、差异规则”。每条 major claim 同时填写
[Source Register](../../SOURCE_REGISTER.md) 的 source label 与 claim verdict，不能把两套分类混成一栏。

## 任务

1. 闭卷写论文实验合同，再逐项回 PDF；缺项只写 `REPRO-CONTRACT-OPEN`。
2. 完成 [训练微例](TRAINING_FIXTURE.md)：复算 F-measure、相对变化和总时间，反驳过宽 claim。
3. 为 EdgeIM Abstract/Introduction/section V/Conclusion 的主要 claim 建全表，不只挑两条。
4. 至少处理三类冲突：正文与表格、proxy 与 target、作者解释与直接观察。
5. communication、privacy、scalability、timestamp causality、soundness 若无直接量，不得用 runtime/fitness 代填。
6. 写 reproduction ceiling：一个可复算单元为什么不是整篇复现。

提交 Evidence Record、实验合同、复算、major-claim table、OPEN register、全文回接句。
