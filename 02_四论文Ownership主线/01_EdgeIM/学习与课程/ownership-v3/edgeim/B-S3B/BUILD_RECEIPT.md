# B-S3B Build Receipt

**构建回执状态（生成时）**：BUILT-WITH-SOURCE-OPEN / QA-PENDING
**后续状态边界（2026-09-20 路由订正）**：历史 controller 汇总表记录为 QA-PASS；当前 zancun 快照未包含 sealed 正文，未在本仓重放该 QA，rubric 仍 NOT-FROZEN。

- actual module files：`PRETEST.md`、`README.md`、`RUBRIC.md`、`TRAINING_FIXTURE.md`、`BUILD_RECEIPT.md`
- actual sealed files：`_sealed/holdouts/B-S3B.md`、`_sealed/references/B-S3B.md`、`_sealed/retests/B-S3B.md`
- primary coverage：Definition 5、Algorithm 3 lines 9-23、section V.B soundness claim
- implementation context：PM4Py `2.7.23.6`，仅作 implementation evidence
- 已分层：paper orchestration 与 complete IM/process-tree/PN/soundness 教学
- SOURCE-OPEN：cut predicates、priority、partition、fall-through、PN merge、invisible transition placement、soundness proof/check
- sealed holdout/reference/retest 已配套
- 未把课程补充内容归为 EdgeIM 作者贡献；未改变用户状态
- 合同边界：课程 `QA-PASS` 不改变用户的 `PASS / RETAINED / OWNED`；本模块不写 `learning/training/LEDGER.md`。
