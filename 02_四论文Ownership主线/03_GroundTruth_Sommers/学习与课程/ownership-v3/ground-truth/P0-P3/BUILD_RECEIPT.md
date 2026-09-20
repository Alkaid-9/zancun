# Ground Truth Build Receipt

**构建回执状态（生成时）**：BUILT-WITH-SOURCE-OPEN / QA-PENDING
**后续状态边界（2026-09-20 路由订正）**：历史 controller 汇总表记录为 QA-PASS；当前 zancun 快照未包含 sealed 正文，未在本仓重放该 QA，rubric 仍 NOT-FROZEN。

- actual module files：`PRETEST.md`、`README.md`、`RUBRIC.md`、`TRAINING_FIXTURE.md`、`BUILD_RECEIPT.md`
- actual sealed files：`_sealed/holdouts/ground-truth-P0-P3.md`、`_sealed/references/ground-truth-P0-P3.md`、`_sealed/retests/ground-truth-P0-P3.md`
- full coverage：pp.1-30、requirements、world chain、transform/simulation、DS1-3、AQ1-3、Table 3/Fig.12、limits
- 训练覆盖：BI/RI/oracle/projection/sampling 分离、generator/consumer、referent、EdgeIM transfer
- SOURCE-OPEN：ICPM predecessor、code/data revision、exact params/seeds、DS2/DS3 scale、projection、alignment settings、raw timing
- sealed holdout/reference/retest 已配套
- 未声称 Sommers 测试 EdgeIM；未代写 World Contract
- 合同边界：课程 `QA-PASS` 不改变用户的 `PASS / RETAINED / OWNED`；本模块不写 `learning/training/LEDGER.md`。
