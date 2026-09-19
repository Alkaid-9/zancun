# WINDOW-ARCHIVE-MANIFEST-20260915

> 生成时间：2026-09-15（用户设备电量告急触发的应急存档）｜校验文件：`WINDOW-ARCHIVE-MANIFEST-20260915.sha256`
> 规则：`.sha256`不列自身；后续追加新建日期化manifest，不覆盖本件

## A. 本次新增归档文件

1. `WINDOW-ARCHIVE-20260915.md` — 窗口工作总归档（身份/状态/证据口径/已完成/未完成/进度/决策约束/文档地图/恢复点/自审）
2. `WINDOW-WORKLOG-20260915.md` — 窗口工作日志（开窗原因/12阶段事件顺序日志/Agent分工历史/修改边界/5条异常闭环/停点）
3. `WINDOW-ARCHITECTURE-AND-PLAN-20260915.md` — 架构与后续执行计划（目标架构图/文档组件职责/4条后续工作流/推荐顺序/Agent分工/风险机制/完成定义）
4. `WINDOW-HANDOFF-20260915.md` — 交接单（先读顺序/一句话现状/4入口/恢复检查单/不可变状态/脏工作区/交接完成条件）
5. `WINDOW-USER-MANUAL-20260915.md` — 使用手册（快速看懂状态/选择下一步/操作验收方法/档案完整性检查/进度报告格式）
6. `WINDOW-MAINTENANCE-MANUAL-20260915.md` — 维护手册（权威层级/追加式规则/状态词典/登记模板/哈希维护/多Agent纪律/一致性检查/关闭重开条件）

## B. 既有关键依赖文件（本包引用，未随本包复制正文）

- `progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md`（含Amendment A1-A3，A3本窗口新增）
- `progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md`（#3行本窗口更正）
- `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`（§2.4-2.8/§3/§4/§5本窗口更新）
- `progress/task_logs/2026/09/2026-09-15__research__task004-status-correction.md`（`TASK-20260915-018`）
- `progress/task_logs/2026/09/2026-09-15__research__ownership-v3-controller-acceptance-batch2-parallel.md`（`TASK-20260915-020`）
- `progress/task_logs/2026/09/2026-09-15__research__ownership-v3-controller-acceptance-batch1.md`（`TASK-20260915-016`，此前完成）
- `progress/task_logs/2026/09/2026-09-15__research__lu-side-jinzu-sprint-routing-cards-v3-sync.md`（`TASK-20260915-014`，此前完成）
- `progress/task_logs/2026/09/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md`（`TASK-20260915-015`，此前完成）
- `progress/decisions/2026-09-06__research__edgeim-jinzu-reconstruction-TASK-004.md`（§8整合清单，TASK-004裁定的关键证据）
- `progress/task_logs/2026/09/2026-09-06__research__edgeim-plan-rewrite-draft-and-input-review.md`（`TASK-20260906-004`自身task log）
- `progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md`（v3合同）
- `progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md`（Transfer Card判定枚举来源）
- `/mnt/d/MyResearch/research_growth/方法论/TRANSFER_CARD_TEMPLATE.md`（跨仓库，本窗口核实存在）

## C. 外部冻结和进度依赖

- `progress/task_logs/INDEX.md`（共享登记面，本包生成时刻sha256=`8a061edb8b73ce8dc64fdd2c02cfe189cf4352e0651d1cc410a675a3fcb21a7a`，314行；**此哈希会随其他并发窗口追加而变化，仅作历史快照，不作当前基线**）
- `learning/training/lu-edgeim-algo1/ownership-v3/BUILD_STATUS.md`（Sol写域内，本包未修改，标注可能与本次QA结果矛盾）
- `learning/training/lu-edgeim-algo1/ownership-v3/`全目录树（Sol第一阶段独占写域，本包全程未写入）
- `research/papers_lu/`下的PDF源文件（EdgeIM-2025-ICWS.pdf、sigRank-2026-TSC.pdf、Sommers-2025-ProcessScience.pdf、CrossEdgeIM-2026-IoTMag.pdf，坐标层核验的最终证据来源，变化时旧核验结论只保留历史意义）

## D. 校验规则

- hash变化先判断是否授权追加（本包6件文件属于"追加式维护"，生成后不应再被编辑；若发现hash变化且无对应的、说明性的新增package，视为异常）。
- 不复制敏感正文——本manifest和校验和文件均不包含用户凭据、Cookie或其他敏感信息，只做文件清单与完整性校验。
- 校验命令：`sha256sum -c WINDOW-ARCHIVE-MANIFEST-20260915.sha256`，全部`OK`视为完整未篡改。
