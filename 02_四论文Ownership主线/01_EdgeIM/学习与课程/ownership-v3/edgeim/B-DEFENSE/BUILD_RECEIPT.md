# B-DEFENSE Build Receipt

**构建回执状态（生成时）**：BUILT-WITH-SOURCE-OPEN / QA-PENDING
**后续状态边界（2026-09-20 路由订正）**：历史 controller 汇总表记录为 QA-PASS；当前 zancun 快照未包含 sealed 正文，未在本仓重放该 QA，rubric 仍 NOT-FROZEN。

- actual module files：`PRETEST.md`、`README.md`、`RUBRIC.md`、`TRAINING_FIXTURE.md`、`BUILD_RECEIPT.md`
- actual sealed files：`_sealed/holdouts/B-DEFENSE.md`、`_sealed/references/B-DEFENSE.md`、`_sealed/retests/B-DEFENSE.md`
- full-paper coverage：problem、related work、三阶段、evaluation、conclusion/future work
- 训练覆盖：四档表达、来源归属、limitation taxonomy、adversarial response、D1
- SOURCE-OPEN：EdgeAlpha/EdgeMiner primary、独立 novelty、privacy/scalability/soundness
- sealed holdout/reference/retest 已配套
- 未把课程完成写成用户 defense 能力；未修改共享正本
- 合同边界：课程 `QA-PASS` 不改变用户的 `PASS / RETAINED / OWNED`；本模块不写 `learning/training/LEDGER.md`。
