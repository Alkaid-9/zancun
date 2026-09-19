# TASK-20260911-004：知识网络架构整合 v0.2

**日期**：2026-09-11
**关联**：RD-2、[v0.1讨论](../../decisions/2026-09-11__research__knowledge-network-architecture-v0.1.md)、[v0.2整合方案](../../decisions/2026-09-11__research__knowledge-network-architecture-v0.2.md)

## 背景

09-10晚讨论菌丝网/知识图谱设计，用户选定"思路B"（关系本身有多层信息），提出六维度（学术/工业/作者/时间/领域/问题）设想，末尾留"明天读现有设计文档再分析"的下一步。本任务是执行该下一步。

## 做了什么

1. 重新核实磁盘现状：三个仓的git log、working tree状态；确认v0.1文档本身尚未commit（未跟踪）。
2. 直接读取（非经Agent转述）以下现有设计文档全文：three-desks-v0.1/{README,WORKBENCH,LEARNING}.md、rd2-first-build-v0.2/{README,IMPLEMENTATION,DATA_CONTRACT}.md、rd2-construction-v0.3/{CONTRACTS,TRACEABILITY}.md、2026-09-08系列（Canvas/Graph需求v0.4、施工蓝图v0.1）、three-desks-v0.1/NEXT_STEP.md。
3. 全库定位"菌丝"关键词，发现9-6日更早的"菌丝网"原始出处（EdgeIM学习法讨论，非知识图谱语境），读取原始构想文件与对应阅读回执全文。
4. 与用户逐轮对齐：深度菌丝(个人学习) vs 广度追踪(工业/学术扫描)是否同一套生长规则→用户选"深度和广度都要"；六维度和"生长方式"的关系→用户点出"应该是多层网形式"（层与生长方式正交，非顶层并列）；最终用户下令"整合一下"。
5. 落盘整合方案v0.2：对齐三份从未对账的分层清单（Map八层/七图/指导库A-F六层）；确认工业维度是三重独立发现的真实缺口；提出`dimension_refs`（新字段，与指导库既有`layer`刻意区分避免命名碰撞）、`Relation.growth_mode`（depth_dig/breadth_scan/cross_pollination）、`Relation.maturity`（emerging/established）三个schema增量；重定性Competency/Identity&Fit/Trajectory为个人投影而非世界维度；列出4个未决的用户裁定点。

## 结果

- 新文件：`progress/decisions/2026-09-11__research__knowledge-network-architecture-v0.2.md`（DESIGN-ONLY）
- TODO.md RD-2行追加note，`ledger_edit.py` CAS写入，收尾哈希`0c128210...`，VERIFY-OK

## 未完成 / 下一步

- §10四个决策点未获用户裁定（时间是否单独维度、cross_pollination是否入relation_type白名单、maturity升级判据、团队维度是否纳工业界人物）。
- 本稿仅为设计契约文字，未改CONTRACTS.md/DATA_CONTRACT.md正文，未改C00-C03代码，未提交为正式amendment。
- 施工蓝图v0.1 §3的Map Estate/Mycelium并列表述与本稿§8的"同一网络两态"说法存在张力，本稿建议修正但未反馈回蓝图正文（需用户确认后再动）。
- CROSSWINDOW.md尚未登记本次整合（P1/C00-C03/repair round三笔此前已识别的欠登记，连同本次共四笔，仍待后续统一补登）。

## 验收证据

无代码变更，无测试运行；本任务为纯文档设计整合，验收标准是"三份分层清单是否被完整对照、缺口是否被具体指出"，非代码测试通过率。

## 回滚

如需撤销，删除新增决策文件并用`ledger_edit.py --replace`把TODO.md该note移除即可；不影响任何已跑通的C00-C03代码或测试。
