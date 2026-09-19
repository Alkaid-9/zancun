# sigRank Build Receipt

**状态**：BUILT-WITH-ERRATA / QA-PENDING

- actual module files：`PRETEST.md`、`README.md`、`RUBRIC.md`、`TRAINING_FIXTURE.md`、`BUILD_RECEIPT.md`
- actual sealed files：`_sealed/holdouts/sigrank-P0-P3.md`、`_sealed/references/sigrank-P0-P3.md`、`_sealed/retests/sigrank-P0-P3.md`
- full coverage：pp.1-13、Definitions 1-6、Eq.1-8、Tables I-III、Figs.1-6、major claims/limits/conclusion
- 训练覆盖：multiset support、position average、rank、Phase 2、protocol、claim audit、fair comparison
- 已纠错：ETMC4200/LogRank、trainingLog1/hybrid/5%、trainingLog7/IMi/5%
- SOURCE-OPEN：plugin/code version、datasets/preprocess、baseline params、tie/rounding、10/12 counting、100x comparator
- sealed holdout/reference/retest 已配套
- 未把 BUILT 写成用户 sigRank ownership
- 合同边界：课程 `QA-PASS` 不改变用户的 `PASS / RETAINED / OWNED`；本模块不写 `learning/training/LEDGER.md`。
