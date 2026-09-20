# sigRank Build Receipt

**构建回执状态（生成时）**：BUILT-WITH-ERRATA / QA-PENDING
**后续状态边界（2026-09-20 路由订正）**：历史 controller 汇总表记录为 QA-PASS；当前 zancun 快照未包含 sealed 正文，未在本仓重放该 QA，rubric 仍 NOT-FROZEN。

- actual module files：`PRETEST.md`、`README.md`、`RUBRIC.md`、`TRAINING_FIXTURE.md`、`BUILD_RECEIPT.md`
- actual sealed files：`_sealed/holdouts/sigrank-P0-P3.md`、`_sealed/references/sigrank-P0-P3.md`、`_sealed/retests/sigrank-P0-P3.md`
- full coverage：pp.1-13、Definitions 1-6、Eq.1-8、Tables I-III、Figs.1-6、major claims/limits/conclusion
- 训练覆盖：multiset support、position average、rank、Phase 2、protocol、claim audit、fair comparison
- 已纠错：ETMC4200/LogRank、trainingLog1/hybrid/5%、trainingLog7/IMi/5%
- SOURCE-OPEN：plugin/code version、datasets/preprocess、baseline params、tie/rounding、10/12 counting、100x comparator
- sealed holdout/reference/retest 已配套
- 未把 BUILT 写成用户 sigRank ownership
- 合同边界：课程 `QA-PASS` 不改变用户的 `PASS / RETAINED / OWNED`；本模块不写 `learning/training/LEDGER.md`。
