# CrossEdgeIM Build Receipt

**构建回执状态（生成时）**：BUILT-WITH-SOURCE-OPEN / QA-PENDING
**后续状态边界（2026-09-20 路由订正）**：历史 controller 汇总表记录为 QA-PASS；当前 zancun 快照未包含 sealed 正文，未在本仓重放该 QA，rubric 仍 NOT-FROZEN。

- actual module files：`PRETEST.md`、`README.md`、`RUBRIC.md`、`TRAINING_FIXTURE.md`、`BUILD_RECEIPT.md`
- actual sealed files：`_sealed/holdouts/crossedgeim-P0-P3.md`、`_sealed/references/crossedgeim-P0-P3.md`、`_sealed/retests/crossedgeim-P0-P3.md`
- full coverage：pp.1-6、Fig.1、Table I、Figs.2-3、Eq.1-2、limitations/conclusion
- 训练覆盖：三层 I/S/delta/O、timestamp、delivery stress、evidence、genealogy/residual
- authorship boundary：已在 public、rubric、sealed reference 中重复设置 hard gate
- SOURCE-OPEN：proof/final identity、generator、implementation params、transport/clock/lifecycle、network/privacy/scaling、global semantics
- sealed holdout/reference/retest 已配套
- 未把 CrossEdgeIM 归为鲁法明署名成果；未改变用户能力状态
- 合同边界：课程 `QA-PASS` 不改变用户的 `PASS / RETAINED / OWNED`；本模块不写 `learning/training/LEDGER.md`。
