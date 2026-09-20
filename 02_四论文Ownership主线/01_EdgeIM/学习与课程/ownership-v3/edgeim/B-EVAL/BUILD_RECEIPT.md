# B-EVAL Build Receipt

**构建回执状态（生成时）**：BUILT-WITH-SOURCE-OPEN / QA-PENDING
**后续状态边界（2026-09-20 路由订正）**：历史 controller 汇总表记录为 QA-PASS；当前 zancun 快照未包含 sealed 正文，未在本仓重放该 QA，rubric 仍 NOT-FROZEN。

- actual module files：`PRETEST.md`、`README.md`、`RUBRIC.md`、`TRAINING_FIXTURE.md`、`BUILD_RECEIPT.md`
- actual sealed files：`_sealed/holdouts/B-EVAL.md`、`_sealed/references/B-EVAL.md`、`_sealed/retests/B-EVAL.md`
- primary coverage：EdgeIM Tables I-III、Eq.4、section V prose 和 conclusion claims
- 训练覆盖：protocol reconstruction、arithmetic、claim classification、contradiction、ceiling
- SOURCE-OPEN：dataset entity/version、code、miner/evaluator params、raw runs、communication/privacy/soundness/scaling measurements
- sealed holdout/reference/retest 已配套
- 未把复算写成 reproduction；未触碰用户 EX-07 或 Ledger
- 合同边界：课程 `QA-PASS` 不改变用户的 `PASS / RETAINED / OWNED`；本模块不写 `learning/training/LEDGER.md`。
