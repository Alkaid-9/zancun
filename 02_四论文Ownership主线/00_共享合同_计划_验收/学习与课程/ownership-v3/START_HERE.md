# 四论文全文 Ownership v3

本目录是课程公共入口，不是学习完成证明。它依据
[v3 施工合同](../../计划与决策/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md)
独立建设，不替换现有 EX-00 至 EX-07，也不改变任何既有 PASS、Ledger 或用户作答。

> **zancun 快照边界（2026-09-20）**：目录重组后，八个公开模块分布在四个论文目录；本入口已改为实际路径。受保护的 sealed/holdout/reference/retest 正文不在本包，历史构建回执中的 sealed 路径不能在这里直接复验。当前学习先走[证据对账路由](../../../../01_进组总计划_OE1_材料交付/CURRENT_LEARNING_ROUTE.md)，不要从本页批量开模块。

## 先分清两条状态轴

- 资产轴：`DESIGN -> FROZEN -> BUILT -> QA-PASS`。
- 能力轴：`LOCKED -> RELEASED -> SUBMITTED -> PASS -> RETAINED -> OWNED`。
- 公开文件存在只证明公开快照可读；历史源仓曾记录 `BUILT / QA-PASS`，本包没有 sealed 正文，不能独立重放该 QA。只有学习者本人完成冻结题、未见题和延迟复测，能力轴才会移动。

## 当前用户路线不变

用户继续完成前半程漏项和 EX-05/EX-06。本目录可以先建，但按下列依赖释放：

1. `B-S2 -> B-S3A -> B-S3B`：在 EX-07 最终实验 verdict 和 D1 前完成。
2. `B-EVAL`：消费 EX-06 的 measurement contract，并在 EX-07 最终裁定前完成。
3. `B-DEFENSE`：EX-07 与三个镜头的必要产物完成后释放。
4. sigRank `P0-P3`：继承 L-S1/L-S2 解锁条件。
5. Ground Truth `P0-P3`：EX-06 后释放，且其 world contract 是 EX-07 的方法门。
6. CrossEdgeIM `P0-P3`：EX-06 且能解释 EdgeIM 下游链后释放。

完整十五题不是课程施工门；D0 只复核已经学过的范围，D1/D2 在相应教学和延迟复测完成后执行。

## 使用顺序

1. 验收者只释放当前模块的 `PRETEST.md`；学习者在未读 README、rubric、coverage、source register 和 sealed 的条件下完成 H0。
2. H0 落盘后，再读 [来源登记](SOURCE_REGISTER.md)、对应 `COVERAGE_MATRIX.md`、模块 `README.md` 与 `RUBRIC.md`，并在正式训练前冻结 rubric。
3. 复制 [证据记录模板](EVIDENCE_RECORD_TEMPLATE.md) 到自己的作答文件，记录 H0 与后续 exposure。
4. 完成公开训练题；需要提示时记录 H1-H4。
5. 关闭材料独立重做，再由验收者释放未见 holdout。
6. 先预测，再检查；记录差异、错误更新和 claim ceiling。
7. 当前 PASS 后仍不等于 `RETAINED`；按期完成 D+2/D+7。
8. 最后才把本人证据回写到 [共享产物](SHARED_ARTIFACTS.md)；课程作者不得代填。

## 公共与密封边界

- H0：每个模块独立的 `PRETEST.md`，只给问题，不给术语桥、结论或 source map。
- 公共训练：模块目标、零基础词汇、任务、提交格式、rubric、训练题；只能在 H0 落盘后打开。
- 密封：训练题参考、未见题、评分键、D+2/D+7。
- `_sealed/` 由验收者按阶段释放。若提前看到完整参考或 holdout，该题当次最多记 `SEEN`，必须换题并延迟复测。
- teardown 只作导航；事实以登记的原始 PDF 为权威。找不到依据时写 `SOURCE-OPEN / UNKNOWN`。

## 目录

| 包 | 模块 | 目标 |
|---|---|---|
| EdgeIM | [B-S2](../../../01_EdgeIM/学习与课程/ownership-v3/edgeim/B-S2/README.md) | hash 分派与局部 `S_i/E_i/R_i` |
| EdgeIM | [B-S3A](../../../01_EdgeIM/学习与课程/ownership-v3/edgeim/B-S3A/README.md) | 中心 union/sum 与全局 weighted DFG |
| EdgeIM | [B-S3B](../../../01_EdgeIM/学习与课程/ownership-v3/edgeim/B-S3B/README.md) | 论文递归编排、经典 IM 补充层、Petri net/soundness 边界 |
| EdgeIM | [B-EVAL](../../../01_EdgeIM/学习与课程/ownership-v3/edgeim/B-EVAL/README.md) | 实验合同、表格复算、全部 major claim |
| EdgeIM | [B-DEFENSE](../../../01_EdgeIM/学习与课程/ownership-v3/edgeim/B-DEFENSE/README.md) | related work、限制、四档表达与 D1 |
| sigRank | [P0-P3](../../../02_sigRank/学习与课程/ownership-v3/sigrank/P0-P3/README.md) | 全文地图、两阶段机制、evidence、attack/defense |
| Ground Truth | [P0-P3](../../../03_GroundTruth_Sommers/学习与课程/ownership-v3/ground-truth/P0-P3/README.md) | 世界生成、oracle 分离、实验与迁移 |
| CrossEdgeIM | [P0-P3](../../../04_CrossEdgeIM/学习与课程/ownership-v3/crossedgeim/P0-P3/README.md) | 三层增量架构、证据、谱系与 residual |

资产施工状态见 [BUILD_STATUS.md](BUILD_STATUS.md)。本目录不直接写
`learning/training/LEDGER.md` 或 `MISTAKE_LOG.md`。
