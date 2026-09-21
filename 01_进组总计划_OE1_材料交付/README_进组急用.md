# 进组急用入口与修复验收

修订日期：2026-09-20。范围：鲁侧进组准备、研究路线表述和对外材料；不代表全仓审计完成。

> **ROUTER STATUS：`SUPERSEDED AS CURRENT ROUTER / EVIDENCE-RECOVERY-ONLY`。** 当前执行入口是 [10/两天双线执行入口](../10_双线材料加工与研究准备_2026-09-20/00_START_HERE.md)，当前状态只读其 [00_control/TASKS.tsv](../10_双线材料加工与研究准备_2026-09-20/00_control/TASKS.tsv)。本页及 `CURRENT_LEARNING_ROUTE.md` 只保留于证据恢复、材料索引和外联冻结历史，不再定义当前学习 cursor。

> **当前用户裁定：`OUTREACH-FROZEN / LEARNING-INCOMPLETE / DO-NOT-FINALIZE / DO-NOT-SEND`。** 本页保存的是事实止损结果和未来材料索引，不是当前邮件、面谈或简历任务。恢复外联必须由用户在学习与本人产物完成后重新明确授权。

## 1. 先用哪些文件

| 用途 | 入口 | 状态与使用上限 |
|---|---|---|
| 学习与进组任务分工 | [jinzu-sprint 项目卡](项目卡/jinzu-sprint.md) | 历史学习记录指向 EX-05；本轮不重新判定本人进度 |
| 09-20 历史证据路由 | [进组学习证据对账路由](CURRENT_LEARNING_ROUTE.md) | `SUPERSEDED AS CURRENT ROUTER`；仅用于恢复 R1–R6 库存和暴露边界，不代替 10/ 当前 cursor |
| 对账结果 | [R1–R6 本人证据库存](R1_R6_EVIDENCE_INVENTORY_2026-09-20.md) | 已与原 MAS 课程源对账；实质 WIP 存在，指定交付仍开放；R1 是下一缺口，不是从头重学 |
| 当前补漏与能力门 | [四论文 v3 合同](../02_四论文Ownership主线/00_共享合同_计划_验收/计划与决策/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md) §1.3、§3 | 六项恢复包；D2 是最终诊断，不是现在继续学习的前置 |
| 鲁侧面谈提纲 | [鲁版一页纸](进组交付材料/onepager_lu_variant.md) | `FROZEN DRAFT`；当前不填、不定稿、不外发 |
| 简历 | [中英简历](进组交付材料/resume_onepage.md) | `FROZEN DRAFT`；待学习与本人产物完成后再核贡献 |
| 本人字段与贡献 | [本人证据确认单](进组交付材料/PERSONAL_EVIDENCE_CHECKLIST.md) | `FUTURE GATE`；当前不是待办 |
| 历史邮件资产 | [OE1 正文](进组交付材料/OE1_lu_email_v4.md)、[发送检查单](进组交付材料/OE1_send_kit.md) | `QUARANTINED / DO NOT COMPLETE / DO NOT SEND` |
| 附件性质 | [附件说明](进组交付材料/OE1_attachments/README.md) | 离线规则流水线与合成轨迹须分开；本轮未复跑 |
| 未来方向 | [鲁×孙矩阵](计划与决策/2026-09-06__research__lu-sun-intersection-matrix-and-group-entry-reframe.md) | 候选假设，不是导师当前方向、novelty 或已定选题 |

用户已明确当前尚未学完、做完，因此本阶段不讨论“能否先诚实请教”，也不以填写占位符代替学习进度。当前唯一活动面是学习、本人实现、验收与可讲解产物；所有外联材料保持冻结。

## 2. 本轮事实账本

查核日均为 2026-09-20。论文事实以本仓 PDF 指定页为依据；未联网刷新导师主页、项目公告或外部仓库。

| ID | Claim / 旧问题 | 原始证据或反证 | 类型与裁定 | 下游处置 |
|---|---|---|---|---|
| J01 | EdgeIM 是并发 bug / deadlock 检测论文 | [EdgeIM PDF](../03_鲁组其他论文与研究谱系/99_其他论文与盘点/论文原文与拆解/EdgeIM-2025-ICWS.pdf) pp.404–405：*EdgeIM: An Efficient Edge-based Process Model Discovery Technique*；ICWS 2025；DOI `10.1109/ICWS67624.2025.00057`；作者 Xuan Su、Cong Liu、Faming Lu、Long Cheng、Qingtian Zeng、Shouli Zhang | SOURCE FACT：旧身份错误；实际是 process model discovery，采样→局部特征→中心聚合及 IM | 进组材料只引用真实身份；09 目录工程污染尚未清理 |
| J02 | SBTPN 可以直接当作死锁方法或 Agent safety 成果 | [SBTPN PDF](../03_鲁组其他论文与研究谱系/01_SBTPN/论文原文与拆解/SBTPN-2026-JAS.pdf) p.1054：*A New Knowledge Mining and Root Cause Analysis Methodology for Multivariate Time Series*；Xiaoliang Wang、Faming Lu、MengChu Zhou、Qingtian Zeng；JAS 13(5), May 2026；DOI `10.1109/JAS.2026.125837` | SOURCE FACT：多变量时间序列知识挖掘/RCA，结合 Petri nets 与 Bayesian networks；Agent 迁移是 HYPOTHESIS | 不写为已有 Agent 安全验证 |
| J03 | CrossEdgeIM 是鲁法明署名成果 | [CrossEdgeIM PDF](../02_四论文Ownership主线/04_CrossEdgeIM/论文原文与拆解/CrossEdgeIM-2026-IoTMag.pdf) p.55：*CrossEdgeIM: An Edge-Based Approach for Interactive Robotic Behavior Model Discovery*；Xuan Su、Cong Liu、Qingtian Zeng、Jinglin Zhang、Long Cheng；IEEE IoT Magazine, Jan 2026（在线发表 2025-12-03）；DOI `10.1109/MIOT.2025.3625047` | SOURCE FACT：作者表无 Faming Lu | 仅作相关谱系，不归为导师本人论文 |
| J04 | 已确认鲁法明 2026 知识图谱/大模型项目获批 | [09-17 BR-1 记录](交接与恢复/2026-09-17__outreach__oe1-br1-decision-and-draft-ab.md) 缺可复核的项目结果页、项目名称及批准号；门户可达不能支持个人获批 | UNSOURCED：撤回“部分确认”；不是“未获批” | α/B 祝贺稿撤出可用正文；普通请教不依赖此项 |
| J05 | 孙猛当前核心方向、基金/学生题目与合作网络已核清 | 交集矩阵主要依据会话转述，缺逐项一手证据 | UNSOURCED：当前画像未重建 | 不以主页或会话标签替代 CURRENT CORE；跨导师 bridge 保留为候选 |
| J06 | ③最有论文潜力，⑤不够新，⑥缺新意；CPL/TraceCompiler 等已证明桥成立 | 矩阵未提供足以支持这些结论的原文审计及同条件比较 | INFERENCE / HYPOTHESIS；具体命名先例 UNSOURCED | 撤回确定排序；不因没有查到就判不存在或虚构 |
| J07 | 8,800 行、43 测试、数月/数千轮日志等可直接写入个人简历 | 旧材料数字不等于当前代码计数、测试运行、本人贡献与公开授权 | UNSOURCED（本轮未复核） | 对外正文移除；需版本、命令/结果、贡献记录、本人确认后逐条恢复 |
| J08 | 附件代表真实 LLM 多 Agent 实验 | [生成器](进组交付材料/OE1_attachments/make_demo_assets.py) `main()`：`LocalRuleReviewer`，构造 diff，四个合成 variant；依赖失败会降级 | SOURCE FACT：源码支持离线规则路径与合成路径的区分；不证明本轮运行成功 | 文件存在 ≠ 本轮复跑 ≠ 本人实现；不能统称真实 LLM 实验，也不能统称全部伪造 |
| J09 | 课程 QA-PASS 或密封答案证明本人 ownership | v3 合同 §2、§4.2 明确分离课程资产与能力；[09-17 总交接](交接与恢复/2026-09-17__all-progress-and-group-entry-packages__handoff.md) §4 保留训练债 | SOURCE FACT（合同规则）；能力未在本轮验收 | 不改作答、Ledger、PASS 或冷测状态 |
| J10 | zancun 课程快照没找到指定提交，因此 EdgeIM 基本没做、应从 R1 重学 | 原课程源存在 EX-01/02/03 作答、EX-05a/05 代码和 EX-06 笔记；原仓 09-12 checkpoint 记录 EX-02、EX-05a 脚本退出码 0，同时明确 `EX-03 USER-REPORTED / NOT PASS`、综合能力门仍开放 | SOURCE FACT：存在实质 WIP 与 scoped runtime evidence；指定 G0/CONNECT/L-S1/SR/EC/全文回接/综合验收仍缺。两者必须同时保留 | 路由改为“复用既有 WIP，只补指定最小缺口”；不得写成空白，也不得升级为 PASS |

## 3. 修复顺序、执行标准与验收

| 阶段 | 执行动作 | 通过标准 | 未通过时 |
|---|---|---|---|
| A：事实止损（本批） | 改急用入口、项目卡、矩阵、BR-1、邮件/一页纸/简历及使用指南；旧审查记录保留历史身份 | 活跃正文不依赖未核获批/novelty/个人数字；论文身份有原文；新增本地链接目标存在；`git diff --check` 无错误；只读复核无未处置阻断项 | 保持修订草稿，不宣布全包可信 |
| B：学习与本人产物（当前） | 按学习路由补指定证据，继续本人实现、验收与冷测；不填写外联材料 | 学习产物、提示边界、运行证据和验收状态可定位；不把 WIP 升级为 PASS | 停在对应学习门，不转入材料装配 |
| C：材料定稿/外联（冻结） | 只有用户完成学习后重新明确授权，才核身份、贡献、用途、附件与收件人 | 新授权存在；每条个人声明有本人证据；最终副本由用户复核 | 继续冻结，不准备、不发送 |

本轮不执行生成器、不重跑研究实验、不补造研究结果、不发信。后续按事实止损 → 学习与本人产物 → 用户重新授权后的材料定稿推进；当前停在第二步。导师全画像、全仓污染图和四核系统恢复另案处理，不构成提前外联的理由。

## 4. 暂不可作为当前证据的材料

- 09-17 BR-1 α 草稿：撤回，不能复制祝贺段。
- 通用一页纸 v1 / 三声音中英版、旧图和旧渲染输出：本轮未逐项修订，`QUARANTINED_FOR_OUTREACH`；不删除，也不再由使用指南放行。
- `factcheck_onepager_20260813.md`、`final_review_20260813.md` 和旧维护表：历史审查记录，不自动给 09-20 修订版授予 PASS。
- 鲁×孙矩阵中的导师项目/学生/前沿先例：来源核验开放；不是已冻结研究路线。
- 09 目录的四核架构、harness 与验证宣传：本批未修，不得拿它们证明个人研究能力。

## 5. 恢复与变更边界

本轮绑定依据：用户“重点先修复进组文件”的明确请求、jinzu 项目卡、09-17 总交接、四论文 v3 合同；不能仅凭自动摘要恢复任务。第一批开始时记录为 `feature/moraine-companion-integration@ea91ab5f794f0ab066873948051b4568f0dad982`；原课程源复核前重新读取的当前身份为 `Alkaid-9/zancun`、`audit/redteam-external-ref-2026-09-20@15bb1d21f4b199f81e189e01ba882b3112960c06`，均不是最初任务写的 main。开始时已有 `.claude/`、`RESEARCH_AGENT_CONSTRAINT_v1.0.md` 未跟踪，本轮不动。

旧 09-19 清单的计数和 SHA-256 是导入快照，不是修订后文件的校验值。未改原始 PDF、题面/作答/能力 Ledger、密封文件和附件数据。需要撤销时，仅逐段逆转本轮文档 diff；不得重置整个工作树。

## 6. 本批验收回执（2026-09-20）

状态：`DOC-REPAIR-CHECKED / USER-CONFIRMATION-OPEN / NOT-SEND-READY`。本批修改 14 份既有 Markdown，新增本入口；不宣称全部进组资产或全仓可信。

- 真实运行 `git diff --check`，退出码 0、无输出；另以 Python 只读检查本批 15 文件：48 个本地 Markdown 链接目标存在，0 个错误。检查排除代码块/行内代码；不覆盖锚点、历史裸路径、外部网址或旧版本所有链接。
- 三份当前对外模板正文已做限定旧声明扫描：未保留所列旧数字、推算教育年份、默认 GitHub 地址或获批祝贺；这不是全面自然语言事实证明。占位符有意保留，当前不能直接发送。
- 一个独立上下文、只读子代理复核了全部文档 diff、新入口、三篇指定 PDF 页、附件生成器和 v3 指定章节；报告发现发送包旧分支残留、项目卡“仅等占位符”两组阻断。
- 主线程沿文件原文复查后修复两组阻断，并清理历史字段、交接路由、TraceCompiler“新证据”和未核门户域名等残留；实际重跑两条回归断言、链接检查及 `git diff --check` 均通过。最后修订由主线程检查，未声称第二轮独立模型已签收。
- 未做：导师近年画像外部检索、个人经历/奖项/项目数字核证、demo/研究实验复跑、用户能力验收或外发。原 `.claude/` 与 `RESEARCH_AGENT_CONSTRAINT_v1.0.md` 未改；没有 commit/push。

当前下一步只按 [10/两天双线执行入口](../10_双线材料加工与研究准备_2026-09-20/00_START_HERE.md) 与其 D1 入口执行；本页的 R1–R6 路由只作恢复资料。不同时做邮件、简历、一页纸或本人字段定稿，不继续扩建架构。

## 7. 第二批学习路由修复回执（2026-09-20）

状态：`ROUTE-REPAIRED / EVIDENCE-RECONCILIATION-NEXT / LEARNER-STATUS-UNCHANGED`。

- 新增 `CURRENT_LEARNING_ROUTE.md`：把历史 EX-05 记录、v3 六项恢复包、D2 后置和对账后的分流接成一个入口；没有读取作答或判定 PASS。
- 新增 `PERSONAL_EVIDENCE_CHECKLIST.md`：身份、学习、项目、数字、AI/团队归属、隐私许可逐项走 `KEEP / WEAKEN / PLAN / OMIT`，不自动填值。
- 修订 EdgeIM `START_HERE`、`BRIEF`、`MASTERY_GATE`、四论文调度与 `CONNECTIONS`：十五题不再作为当前动作，旧 EX-00 游标明确为历史，四篇长期目标统一为全文 5/5 但按不同适配器和依赖展开。
- 修复八站实际文件名、EdgeIM/CrossEdgeIM PDF、本仓 v3 合同、ownership-v3 八个模块及共享 rubric/source register 的当前链接。
- ownership-v3 状态拆开记录：模块回执的 `QA-PENDING` 是生成时状态；总表的 `QA-PASS` 是历史 controller 记录；当前 zancun 没有 sealed 正文，所以标为 `QA-NOT-REPLAYED-HERE`，rubric 仍 `NOT-FROZEN`，用户能力不变。
- 学习路由修复完成时，本批与第一批合计 46 份任务内 Markdown（43 份既有文件、3 份新增文件）通过本地链接检查；R1–R6 库存随后作为第 47 份任务文件新增，须以最新验收回执为准。预先存在的未跟踪 `.claude/` 与 `RESEARCH_AGENT_CONSTRAINT_v1.0.md` 不计入本任务。
- 子代理尝试因服务限流未形成可用报告；随后用户要求总并发最高 2，主线程确认后台为 0 并保持单线程完成。没有把失败的子任务写成独立复核。

## 8. R1–R6 快照库存回执（2026-09-20，已被 §9 原课程源复核订正）

- 总并发保持不超过 2：主线程 + 1 个只读子代理；子代理完成后回到主线程单线程。
- 子代理只读盘点 R1–R6，主线程抽查关键题面、现有作答片段、暴露记录、空白模板、旧批改和 Ledger；未读 sealed。
- 当前库存：R1 `MISSING/EXPOSURE-RECORDED`；R2 四卡提交 `MISSING/EXPOSURE-UNKNOWN`；R3 `MISSING/EXPOSURE-RECORDED/UNLOCK-UNKNOWN`；R4 `TEMPLATE-ONLY`；R5 `MISSING`；R6 `NOT-FROZEN` 且无 EdgeIM Ledger PASS 行。
- 当时结论上限：只覆盖 zancun 快照；不证明用户从未在仓外完成，不判 PASS/FAIL，不修改作答或 Ledger。关于“当前唯一动作 R1”的旧表述以 §9 为准。
- 最新机械检查覆盖 47 份任务内 Markdown、160 个本地链接目标，0 个断链；`git diff --check` 无输出，任务 diff 不含 answer、sealed、Ledger、代码、JSON、PDF 或 TSV。

## 9. 原 MAS 课程源复核回执（2026-09-20）

状态：`ORIGINAL-SOURCE-RECONCILED / PRIOR-MISSING-CLAIMS-NARROWED / LEARNER-STATUS-UNCHANGED`。

- 已只读检查 `/mnt/d/myresearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1` 的 131 个文件路径，并按权威路由继续核对原仓 `_scratch/seg0/`、09-12 checkpoint、v3 合同、项目卡与 Ledger；只确认密封资产路径存在，没有打开 `_sealed`、holdout/reference/retest 或正式口试正文。
- 原仓存在实质学习过程：EX-01 的 DFG/预测作答，EX-02/03 的学习记录，EX-05a/05 的实现与测试，EX-06 的笔记；09-12 checkpoint 真实记录 EX-02 和 EX-05a 脚本退出码 0。它们不得再被概括成“没有做过”。
- 指定恢复包仍未闭合：精确名 `G0_user_paper_note.md` 未找到；署名 SOL 的 A2 草稿只是定位底稿；C00/C01/C05a/C02 未见非 sealed 提交；L-S1 未见本人一页稿；`SR/EC` 仍只有模板槽；全文回接句和当前综合验收未找到；Ledger 无当前 EdgeIM PASS 行。
- 09-12 checkpoint 自身把状态限定为 `EX-03 USER-REPORTED / NOT PASS`，并说明 AI 解释与答案暴露最多支持 `SEEN` 和可复跑记录。因此本次没有把 WIP 升级为 PASS，也没有沿用快照库存造成的“空白课程”暗示。
- 当前恢复口径：R1 是下一份缺失交付，只补 G0 五问和来源标签；复用现有 DFG/预测，不从 EX-01 重学。其余恢复项按依赖迁移既有 WIP，禁止机械重做或倒填 Ledger。

## 10. 外联优先级纠偏（2026-09-20）

用户明确指出当前“还没学完、没做完”，因此撤回“可并行收口邮件/个人字段”的建议。邮件、一页纸、简历、占位符、附件和发送检查单统一标记为 `OUTREACH-FROZEN`；事实修复 commit 只保留为止损记录，不构成材料准备或发送授权。恢复外联必须等待用户完成学习/本人产物后另行明确提出。
