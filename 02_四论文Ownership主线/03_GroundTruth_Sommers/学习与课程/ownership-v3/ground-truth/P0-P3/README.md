# Ground Truth Approach P0-P3 Full-Paper Package

**资产状态**：BUILT-WITH-SOURCE-OPEN；学习状态继承 L-GT
**论文**：Sommers PDF physical pp.1-30

## P0 全文地图

闭卷重建 RQ、三项 requirements、related-work gap、核心世界、DS1-DS3、AQ1-3、results、limitations 和 conclusion；再完成 [Coverage Matrix](../COVERAGE_MATRIX.md)。

## P1 机制 ownership

1. 重建 `M0 -> M^S -> M^L -> L'`，每一步写 generator、consumer、visible/hidden。
2. 重建 `Psi(M,pi,h)=M union h(pi)`、mapping 约束和 simulation Eq.2。
3. 完成 [训练微例](TRAINING_FIXTURE.md)：把 BI、RI、simulation randomness、projection、sampling 分开。
4. 不把 Fig.4 的 illustrative `M'` 叫 `M^L` 或 log `L'`。
5. 对未见 world 先预测 observable symptom，再看 oracle。

## P2 evidence ownership

重建 DS1/DS2/DS3 和完整 AQ1-3 protocol；所有 major claims 写 evidence/ceiling。Table 3 与 Fig.12 只能支持实际规模；缺 seed、参数、环境、重复和 raw values 时保留 OPEN。

## P3 attack + defense

1. 改一个 pattern、projection 或 simulation parameter，先预测。
2. 明确“可迁移到 EdgeIM”和“不能迁移”各至少一项。
3. 消费 EdgeIM Mechanism/Sampling/EX-06 measurement contract，回写 World & Evidence Contract。
4. sampler 只能看到 `D_obs`，不能看到 transition provenance/deviation tag。
5. 完成三档表达和 D+2/D+7。

Sommers 没有测试 EdgeIM；不得把本篇方法框架写成 EdgeIM 实验结果。
