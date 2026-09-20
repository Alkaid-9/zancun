# B-S3A Build Receipt

**构建回执状态（生成时）**：BUILT / QA-PENDING
**后续状态边界（2026-09-20 路由订正）**：历史 controller 汇总表记录为 QA-PASS；当前 zancun 快照未包含 sealed 正文，未在本仓重放该 QA，rubric 仍 NOT-FROZEN。

- actual module files：`PRETEST.md`、`README.md`、`RUBRIC.md`、`TRAINING_FIXTURE.md`、`BUILD_RECEIPT.md`
- actual sealed files：`_sealed/holdouts/B-S3A.md`、`_sealed/references/B-S3A.md`、`_sealed/retests/B-S3A.md`
- primary coverage：EdgeIM section IV.D、Algorithm 3 lines 1-8
- 训练覆盖：set union、weight sum、排列不变性、信息损失
- sealed：holdout/reference/retest 均已配套
- SOURCE-OPEN：singleton/zero-edge node、transport/duplicate delivery、weight 是否参与 cut
- 未修改既有站点、用户证据或 Ledger
- 本回执不改变用户能力状态
- 合同边界：课程 `QA-PASS` 不改变用户的 `PASS / RETAINED / OWNED`；本模块不写 `learning/training/LEDGER.md`。
