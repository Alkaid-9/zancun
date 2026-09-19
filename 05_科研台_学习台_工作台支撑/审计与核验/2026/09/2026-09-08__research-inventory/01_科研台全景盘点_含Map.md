# 科研台全景盘点（含学习科研菌丝网、research/map、七图与工作台全图）

盘点日期：2026-09-08（Asia/Taipei）。署名：Codex 主窗口，TASK-20260908-002。

**科研台已有相当多的研究资产，但独立科研台产品仍处在设计阶段。** 现有资产分布在领域地图、论文库、训练包、研究方法库、实验与进度系统中；9 月 5 日的独立科研台方案拟把这些资产接到共同的研究对象与证据链上。现行 RD-1 和阶段 0 合同均未表示应用已经建成。

本篇专门总结整个科研台。近期具体论文、进组准备、CCF 材料、外部新稿和旧反馈订正，见同目录 [第二份清单](02_近期科研与进组材料清单.md)。这是盘点报告，不修改既有方案或宣告采纳。

**09-08 补充说明：科研菌丝网是准备纳入科研台的长期学习与科研体系，进组只是当前实例。** 初版对这层内容展开不足，现已补齐三份详版：[科研台版本／设计／资产](03_科研台当前版本进度_整体设计与资产详版.md)、[待整合体系／菌丝网／近期任务](04_待整合的学习科研体系_构想与近期任务详版.md)、[科研任务具体情况](05_科研任务盘点与具体情况详版.md)。按新详版阅读整体构想，以下保留第一版的实物盘点与地图索引。

## 1. 盘点范围与证据口径

重点检查 2026-09-01 至 09-08 的更新，并回溯 08-12 起仍在使用的地图、方法、提案与工程入口。检索覆盖外仓 MyResearch、MAS_Safety_Project、research_growth，以及被交接引用的桌面、下载和微信材料。按主题读入口、状态段和关键正文；文件索引不代表每篇论文、每个历史实验都重审过。

| 仓库／位置 | 本轮核实的身份 | 主要职责 |
|---|---|---|
| `/mnt/d/MyResearch` | 独立仓，origin 尾名 `my-cockpit.git`，HEAD `e757493` | 全局工作区、协作路由、外部参考库、根目录交接 |
| `/mnt/d/MyResearch/MAS_Safety_Project` | 独立仓，origin 尾名 `Research_Training_Undergraduate.git`，HEAD `da66308` | 地图、论文、学习、实验、进度和看板 |
| `/mnt/d/MyResearch/research_growth` | 独立仓，origin 尾名 `Research_Learning.git`，HEAD `22ace3d` | 方法论、摘录、迁移协议与研究反思 |
| `/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901` | MAS 的独立 worktree，HEAD `02da69b` | 工作台 v2 WP0 隔离实现；不是科研资料的最新主仓 |
| `/mnt/d/MyResearch/research` | 外仓普通目录 | 少量旧路径资产；不能与 MAS 内的 research 混用 |

三仓都有既有未提交修改。下文的“已存在／已落盘”只说明文件实物存在；“草稿”“历史快照”“待核验”保留原义，不换算为本人掌握、项目完成或产品上线。

## 2. 整个科研台现在包含什么

| 部分 | 已有载体 | 当前可用内容与缺口 |
|---|---|---|
| 研究全景与选路 | [research/map/GRAND_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/GRAND_MAP.md>)、[research/map/FUSION_ROADMAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/FUSION_ROADMAP.md>) | 全域、领域、交叉带和历史路线；日期与竞争判断需按来源时间读取 |
| 人物／团队／研究谱系 | [research/map/W1_lu_side/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W1_lu_side>)、[research/map/W2_sun_side/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W2_sun_side>)、[research/map/radar/teams/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams>) | 鲁侧、孙侧、兄弟团队与时间线；关系不是全部已核真的统一图数据库 |
| 文献与证据 | [research/papers_lu/](</mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu>)、[research/sun/phase1/papers/](</mnt/d/MyResearch/MAS_Safety_Project/research/sun/phase1/papers>)、[research/map/surveys/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys>) | PDF、拆解、批判件、综述与检索边界；详见第二份清单 |
| 横向比较 | [research/map/matrices/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices>)、论文家族合成、W4 评审元分析 | 方法、故障、conformance、shield 与论文家族比较；新增论文未全部回流 |
| 七图与成长记录 | [七图入口](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/KNOWLEDGE_MAP.md>)及下节五份地图文件 | 七个观察视角已有文本和模板；部分个人记录仍空白，不能当已测能力 |
| 研究动作／迁移 | [方法论/迁移审计协议_20260905.md](</mnt/d/MyResearch/research_growth/方法论/迁移审计协议_20260905.md>)、[方法论/TRANSFER_CARD_TEMPLATE.md](</mnt/d/MyResearch/research_growth/方法论/TRANSFER_CARD_TEMPLATE.md>) | 从机制对应、不对应、表示充分性到最小证伪的记录协议 |
| 研究方法库 | [方法论/科研体系三源整合_20260904.md](</mnt/d/MyResearch/research_growth/方法论/科研体系三源整合_20260904.md>)、[learning/methodology/RESEARCH_METHODOLOGY.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/methodology/RESEARCH_METHODOLOGY.md>)、W6 craft | 来源→适配→本人证据；部分体系采纳仍为提案 |
| 研究议程／提案 | [research/map/proposals/INDEX.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/INDEX.md>)、[research/tracebridge_full_spectrum_20260830/00_control/BRIDGE_LU_PLANNING_LOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/tracebridge_full_spectrum_20260830/00_control/BRIDGE_LU_PLANNING_LOG.md>) | T 系列、Bridge、鲁组与后续方向；有历史候选、暂停与待裁决线 |
| 实践与实验事实 | [research/experiments/](</mnt/d/MyResearch/MAS_Safety_Project/research/experiments>)、[research/edgeim_sampling_audit/](</mnt/d/MyResearch/MAS_Safety_Project/research/edgeim_sampling_audit>)、[research/map/oss_landscape/e2/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2>) | 已有代码、回执、失败与冻结记录；“有结果文件”不等于可引用证据 |
| 调研／雷达 | [research/map/surveys/RESEARCH_SOP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/RESEARCH_SOP.md>)、[research/map/radar/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar>) | 检索、证据分级、复扫与回流规则；不是已接通的自动科研系统 |
| 执行／治理桥 | [progress/TODO.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/TODO.md>)、[progress/projects/](</mnt/d/MyResearch/MAS_Safety_Project/progress/projects>)、[tools/dashboard/](</mnt/d/MyResearch/MAS_Safety_Project/tools/dashboard>) | 任务、项目、会话、验收的既有设施；承担执行事实 |
| 独立产品方案 | [progress/decisions/2026-09-05__research__independent-research-desk-design-alignment.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/2026-09-05__research__independent-research-desk-design-alignment.md>) | 产品边界已表达为独立科研台＋桥接；对象、接口、技术栈与实现尚未整体落定 |

## 3. Map 全量主干：不能只看七图

这里实际有三类不同用途的地图入口：**研究内容地图 `research/map/`、七个研究／学习视角、全工作区资产快照 `/wbmap`**。它们都纳入本盘点；后两类不能替代第一类。

### 3.1 research/map：L0／L1／L2 与 W1—W7

总入口：[research/map/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/README.md>)；给本人使用的入口：[research/map/USER_GUIDE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/USER_GUIDE.md>)；结构：[research/map/SCHEMA.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/SCHEMA.md>)；边界：[research/map/SEARCH_BOUNDARY.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/SEARCH_BOUNDARY.md>)；更新记录：[research/map/CHANGELOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/CHANGELOG.md>)。

| 层／波次 | 具体资产 | 实际覆盖 | 状态与注意点 |
|---|---|---|---|
| L0／W3 | [research/map/GRAND_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/GRAND_MAP.md>)、[research/map/W3_L0_global/L0_global_partition.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W3_L0_global/L0_global_partition.md>)、[research/map/W3_unified/UNIFIED_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W3_unified/UNIFIED_MAP.md>) | 全域分区、代表作、统一坐标与待核池 | 三处都在；主导航与伴随卷并存，不能当三个独立完整系统 |
| W1 鲁侧 | [research/map/W1_lu_side/LU_SIDE_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W1_lu_side/LU_SIDE_MAP.md>)；同目录 A/B/C | Petri net、process mining、并发验证三个版图 | 文档资产齐；“鲁本人／合作网络／邻域方法”需要分开标注 |
| W2 孙侧 | [research/map/W2_sun_side/SUN_SIDE_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W2_sun_side/SUN_SIDE_MAP.md>)；同目录 A/B/C | LLM-MAS safety、团队与 OpenReview、LLM safety 父级版图 | 文档资产齐；旧 USER_GUIDE 仍写“进行中”，应读总纲与当前实物 |
| L2 交叉带 | GRAND_MAP、[research/bridge_scan_2026-08-12/SYNTHESIS.md](</mnt/d/MyResearch/MAS_Safety_Project/research/bridge_scan_2026-08-12/SYNTHESIS.md>)、proposals | 鲁／孙／companion 方法交叉、竞争关系与候选问题 | 是带检索范围的历史判断，不是当前“无人做”的证明 |
| W4 | [research/map/W4_rejection_intel/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W4_rejection_intel>) | 两份公开评审元分析，转为实验与论证检查项 | 已有历史材料；增量评审与事实刷新另有计划 |
| W5 数据化 | [research/map/data/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data>)、[tools/scripts/map_to_yaml.py](</mnt/d/MyResearch/MAS_Safety_Project/tools/scripts/map_to_yaml.py>) | YAML、BibTeX、HTML explorer | v0 文件存在；v1 实施仍在 BR-11 |
| W5 v1 方案 | [research/map/w5_design_sprint_20260813/W5_V1_PLAN.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/w5_design_sprint_20260813/W5_V1_PLAN.md>) | cells、watchlist、reconciliation、邻域图 | 设计资产存在，不等于各数据对象和界面已实现 |
| W6 craft | [research/map/W6_craft/CRAFT_MANUAL.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/CRAFT_MANUAL.md>)；A/B/C/D、验收模板与回执 | 科研训练、代码 review、正确性、debug、实验、信息与 taste | 领域专用方法库已有；与通用方法论互补 |
| W7 companion | [research/map/W7_companion_side/COMPANION_SIDE_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W7_companion_side/COMPANION_SIDE_MAP.md>) | 关系型 agent 安全第三侧翼、C①—C⑤、T5 关联 | 总纲重复登记两次 W7，实际同一目录与主文件，不重复计数 |

### 3.2 配套地图资产也在范围内

| 子系统 | 入口与清单 | 用处 |
|---|---|---|
| 四张比较矩阵 | [research/map/matrices/conformance-lane-comparison.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices/conformance-lane-comparison.md>)、[research/map/matrices/shield-lane-comparison.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices/shield-lane-comparison.md>)、[research/map/matrices/fault-panorama.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices/fault-panorama.md>)、[research/map/matrices/cross-scan.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices/cross-scan.md>) | 一致性检查／shield／故障／交叉扫描 |
| 团队动向 | [research/map/radar/teams/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/README.md>)及团队卡 | 人、机构、工作与时间线；定期复查，不用模糊“相关”边替代关系类型 |
| 月度雷达 | [research/map/radar/2026-08-14_adhoc_scan_delta.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/2026-08-14_adhoc_scan_delta.md>)、[research/map/radar/signal-lights-2026-08.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/signal-lights-2026-08.md>)、[progress/runbooks/research-map-maintenance.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/runbooks/research-map-maintenance.md>) | 检索范围、零命中边界、竞争变化、改判条件 |
| 综述库 | [research/map/surveys/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/README.md>)、[research/map/surveys/SURVEY_LEDGER.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/SURVEY_LEDGER.md>)、[research/map/surveys/PLAN_survey_gapfill_202609.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/PLAN_survey_gapfill_202609.md>) | cards、PDF、crosswalk、对撞、T5/OE1 证据包与九月补缺计划 |
| 开源版图六簇 | [research/map/oss_landscape/SYNTHESIS.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/SYNTHESIS.md>)；C1—C6 | PM、conformance、PN tools、agent safety、传播归因、formal×LLM |
| 开源实践与接线 | [research/map/oss_landscape/GUIDE_r_window_nine_repo.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/GUIDE_r_window_nine_repo.md>)、[research/map/oss_landscape/MAINTENANCE_r_window_nine_repo.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/MAINTENANCE_r_window_nine_repo.md>)、e2/ | 九仓单仓验证、跨工具链、遗留问题；单仓 PASS 不代表研究闭环成立 |
| 研究提案与对外出口 | [research/map/proposals/INDEX.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/INDEX.md>) | T1/T4、T2、T3、T5-companion、OE1、简历、一页纸、占位表；具体内容见第二份清单 |
| 上游增量调研 | [research/bridge_scan_2026-08-12/](</mnt/d/MyResearch/MAS_Safety_Project/research/bridge_scan_2026-08-12>)、[research/deep_scan_2026-08-13/](</mnt/d/MyResearch/MAS_Safety_Project/research/deep_scan_2026-08-13>) | 老地图的来源池与合成依据，保留历史边界 |

本轮直接用 YAML 解析得到：`papers.yaml` **170 条**、`schools.yaml` **40 条**、`teams.yaml` **33 条**、`topics.yaml` **5 条**、`quicklooks.yaml` **19 条**。均与各自文件内 count 一致；生成时间字段仍为 **2026-08-14 05:35**。这些是不同对象类型的条目数，不能相加成“267 篇论文”，也不是全部已有 PDF 或全部已核验。

BR-11 当前仍列：cells.yaml 119 格、WATCHLIST/radar_hit、reconciliation、explorer 邻域图，以及实体分裂／团队词元／别名数量漂移三个修复项。当前 data/ 目录只有既有 YAML、schema、BibTeX、HTML；不能把 W5 v1 设计当成已做。旧数据内空白论断等残留问题仍需实施后的语义复核。

### 3.3 七图：七种视角，五份主文件

| 图 | 现有文件 | 记录什么 |
|---|---|---|
| 1 Knowledge | [learning/training/lu-edgeim-algo1/KNOWLEDGE_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/KNOWLEDGE_MAP.md>) | 当前问题需要的概念与依赖，按任务扩展 |
| 2 Method Landscape | [learning/training/lu-edgeim-algo1/RESEARCH_MAPS.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/RESEARCH_MAPS.md>)的 Map 2 | 方法问题、输入输出、保留／丢失信息、可比条件 |
| 3 Idea Genealogy | 同上 Map 3 | 来源可考证的继承与用户机制重建分开 |
| 4 Transfer | 同上 Map 4 | 对应点、不对应点、竞争解释、最小检查与证据上限 |
| 5 Competency | [learning/training/lu-edgeim-algo1/RESEARCHER_COMPETENCY_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/RESEARCHER_COMPETENCY_MAP.md>) | 行为、产物、帮助条件与假阳性；不做人格评分 |
| 6 Identity & Fit | [learning/training/lu-edgeim-algo1/RESEARCH_IDENTITY_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/RESEARCH_IDENTITY_MAP.md>) | 长期偏好、反向证据、问题与合作方式的匹配 |
| 7 Trajectory | [learning/training/lu-edgeim-algo1/RESEARCH_TRAJECTORY_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/RESEARCH_TRAJECTORY_MAP.md>) | T0/T1/T2 工作样本、反馈、修正与支架撤除 |

配套入口是 [learning/training/lu-edgeim-algo1/START_HERE.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/START_HERE.md>)、[learning/training/lu-edgeim-algo1/PAPER_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/PAPER_MAP.md>)、[learning/training/lu-edgeim-algo1/CONNECTIONS.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/CONNECTIONS.md>)、[learning/training/lu-edgeim-algo1/RESEARCH_NOTE_TEMPLATE.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/RESEARCH_NOTE_TEMPLATE.md>)。PAPER_MAP 是论文阅读导航，不是“第八张能力图”；RESEARCH_MAPS 一份文件承担三图。

七图已具备记录结构和课程例子，Identity/Fit、Trajectory 等个人表格仍可见空模板。不能由“图都写好了”推出“本人画像与成长轨迹已经建立”。学习入口的新旧版本问题见第二份清单。

### 3.4 全工作区资产地图

[docs/workbench-map-20260822.html](</mnt/d/MyResearch/docs/workbench-map-20260822.html>) 是跨仓工作区全图快照；[tools/dashboard/hub/wbmap.py](</mnt/d/MyResearch/MAS_Safety_Project/tools/dashboard/hub/wbmap.py>) 为 `/wbmap` 提供读取与章节导航。冻结／退役约定见 [progress/handoff/2026-08-24__workbench-map-finalize__handoff.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/handoff/2026-08-24__workbench-map-finalize__handoff.md>)。

它回答“资产、工具和工作区在哪”，不负责论文事实、个人能力或研究谱系。[WORKBENCH.md](</mnt/d/MyResearch/WORKBENCH.md>) 是板块注册表，许多心跳、旧截止日期仍停在八月；不能直接用它判断九月当前进度。

## 4. 五层框架与 Map：哪些已接，哪些没接

既有导航写作：

```text
WORLD / FIELD
    ↓
RESEARCH MAPS
    ↓
ACTIVE TRACKS
    ↓
EVIDENCE / PRACTICE
    ↓
ARTIFACTS

所有层回链 SOURCES；CLAIMS / GOVERNANCE 横切各层；证据可反向更新地图。
```

**已落地的是文字导航与部分入口。** [learning/training/lu-edgeim-algo1/MASTERY_GATE.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/MASTERY_GATE.md>) §8（更新记录到 v2.2）写入五层结构；[learning/training/lu-edgeim-algo1/FOUR_PAPER_TRAINING_LOOP.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/FOUR_PAPER_TRAINING_LOOP.md>) §9 写入四论文在各层的位置；[学习与科研体系-整合版.md](</mnt/d/Edge下载/学习与科研体系-整合版.md>) §6 明确保留七个视角，强调同一记录按需查看、不重复填七张表。

**仍欠完整接线。** FOUR_PAPER §9 的 RESEARCH MAPS 一行只有镜头／设计选择／前后继／residual 的说明，没有逐一指向七图主文件；旧 research/map、个人七图、WORLD/FIELD、新 T/R/F/E 的对象归属、复用记录、更新方向也未形成一个已验收的统一实现。

因此，旧窗口的“融合一个字没写”只能描述它自己中断的那段工作，不能代表当前整个盘面；“五层已经出现”也不能证明整个科研台融合完成。

下表是本次盘点的归属说明，**不是新冻结的架构**：

| 层 | 可复用的现有资产 | 接线时还要明确 |
|---|---|---|
| WORLD/FIELD | L0/L1、团队谱系、radar、工业与前沿素材 | 领域事实、团队关系、时间与来源，不把会话推测升为事实 |
| RESEARCH MAPS | 领域／方法矩阵、七个视角、论文谱系与迁移卡 | 同一对象的稳定身份；哪些是视图、哪些是原始记录 |
| ACTIVE TRACKS | EdgeIM／四论文、T/R/F/E、T 系列、JINZU | 当前线、候选线、暂停线及不同来源的开门条件 |
| EVIDENCE/PRACTICE | 手算、本人实现、实验回执、反例、失败、复测 | 本人／AI／原文贡献、提示量、可复算范围 |
| ARTIFACTS | 笔记、比较卡、方法摘要、进组材料、代码与研究报告 | 导出、版本、可引用条件与反向链接 |

## 5. 独立科研台设计链与建设清单

| 顺序 | 文件 | 已经决定／写出的内容 | 当前状态 |
|---|---|---|---|
| 09-04 讨论 | [progress/decisions/2026-09-04__research__luo-pengsida-fusion-workbench-mount-alignment.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/2026-09-04__research__luo-pengsida-fusion-workbench-mount-alignment.md>) | 方法库怎样挂载到工作台 v2／8899／独立科研台的比较 | 讨论存档；不能单独覆盖后续方向 |
| 09-05 边界 | [progress/decisions/2026-09-05__research__independent-research-desk-design-alignment.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/2026-09-05__research__independent-research-desk-design-alignment.md>) | 独立科研台＋与工作台、Obsidian/Reviva 打通 | 方向确认；对象／接口设计未整体冻结 |
| 09-05 三源提案 | [progress/decisions/2026-09-05__research__research-desk-three-source-improvement-proposal.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/2026-09-05__research__research-desk-three-source-improvement-proposal.md>) | 工作簿、操作符案例册、训练体系的角色；三栏工作面和六阶段路线 | PROPOSED / NOT-FROZEN / DESIGN-ONLY |
| 09-05 阶段 0 | [progress/decisions/2026-09-05__research__research-desk-stage0-semantic-contract.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/2026-09-05__research__research-desk-stage0-semantic-contract.md>) | Source、Excerpt、Claim、Evidence、Relation、学习记录的 ID、状态与定位规则 | PROPOSED / USER-REVIEW-PENDING；标题中的“合同”不等于已冻结 |
| 任务路由 | [progress/TODO.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/TODO.md>) RD-1；[progress/task_logs/2026/09/2026-09-05__research__research-desk-three-source-improvement.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/task_logs/2026/09/2026-09-05__research__research-desk-three-source-improvement.md>) | 继续设计与 P0 切片 | 尚未形成独立科研台全产品验收 |

对象主链提案为：`Question → Source/Paper → Excerpt/Note → Claim → Evidence → Relation/Map → Comparison → Decision/Experiment → Workbench Task`。七图从共同记录派生，研究内容与执行事实分工保存。

| 功能／阶段 | 现有基础 | 尚待落地 |
|---|---|---|
| 阶段 0：语义与边界 | 三源快照表、字段／状态／ID 提案 | 确认来源版本、权威归属、P0 问题和验收 |
| 阶段 1：只读来源库 | 本地 PDF/MD/XLSX、来源引用 | source_index、单元格／段落／页码浏览与可追溯导入 |
| 阶段 2：研究对象与证据 | 现有拆解和研究卡 | 可审阅的候选 Claim/Evidence、稳定关系、可恢复导出 |
| 阶段 3：操作符与学习记录 | OP 案例册、Transfer Card、七图模板 | 同一条学习记录支撑七图、反馈与延迟复测回链 |
| 阶段 4：Map／Comparison／Team | 旧 map、YAML explorer、比较表、团队卡 | 在共同对象上统一显示关系类型、时间、证据与量纲 |
| 阶段 5：桥接 | 工作台、Obsidian 文件、参考项目 | 文件→科研索引、研究决策→任务、执行结果→证据三方向接线 |
| 搜索／导出 | 文件检索、BibTeX、旧 YAML/HTML | 独立产品的全文检索与开放格式导出闭环 |
| AI 协助 | 外部方法库、现有拆解流程 | 候选→审阅→确认的产品行为；不能自动提升事实或能力状态 |

这是全范围建设账，不表示本次缩减原愿景。现有提案对 P0 排期仍有待澄清之处：界面路线把完整 Map 放 P1，P0 验收又需要展示一条 Map 关系；后续需明确最小关系展示与完整地图交互的边界。

## 6. 科研方法与成长底座

| 资产 | 用途与状态 |
|---|---|
| [learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md>) | 冻结 OS；真实闭环、本人证据、资源约束。不是独立科研台 UI 方案 |
| [learning/methodology/](</mnt/d/MyResearch/MAS_Safety_Project/learning/methodology>)、[tools/ai/](</mnt/d/MyResearch/MAS_Safety_Project/tools/ai>) | SOP、分析、综述、证据审计、review、idea、写作等通用方法 |
| [research/map/W6_craft/](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft>) | 形式化／PM／agent 实验的领域专用训练和 debug 方法 |
| [方法论/科研体系三源整合_20260904.md](</mnt/d/MyResearch/research_growth/方法论/科研体系三源整合_20260904.md>) | 已以 adapter 方式接入方法库；不替代 OS，B4 正式采纳仍另有未决项 |
| [方法论/迁移审计协议_20260905.md](</mnt/d/MyResearch/research_growth/方法论/迁移审计协议_20260905.md>)、[方法论/TRANSFER_CARD_TEMPLATE.md](</mnt/d/MyResearch/research_growth/方法论/TRANSFER_CARD_TEMPLATE.md>) | 从术语相似到结构、机制、干预、可验证迁移；有存在／可识别／充分性区分 |
| [反思与思考/2026-09-05_Execution-Structure-Intervention_研究母结构.md](</mnt/d/MyResearch/research_growth/反思与思考/2026-09-05_Execution-Structure-Intervention_研究母结构.md>) | 用户研究思考的保存；论文细节与跨域主张仍待逐条原文核验 |
| [反思与思考/2026-09-05_鲁法明研究谱系与稳定Research-Grammar.md](</mnt/d/MyResearch/research_growth/反思与思考/2026-09-05_鲁法明研究谱系与稳定Research-Grammar.md>) | 六分支与合作网络思考；SYNTHESIS-PENDING-CITATION-AUDIT |
| [反思与思考/2026-09-05_EdgeIM四论文十字训练闭环.md](</mnt/d/MyResearch/research_growth/反思与思考/2026-09-05_EdgeIM四论文十字训练闭环.md>) | 成长库中的概念镜像；执行入口用训练包的 MASTERY_GATE 与 FOUR_PAPER |
| [方法论/SKILL_INDEX.md](</mnt/d/MyResearch/research_growth/方法论/SKILL_INDEX.md>) | 方法索引；不要将其条目数当成已部署的新科研台技能注册表 |
| [research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/](</mnt/d/MyResearch/MAS_Safety_Project/research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system>) | B1 pengsida、B2 Supervisor、B2b Luo PDF、B3 成长库索引、B4 体系提案、C3 待登记项 |

原始三源：[工作簿1.xlsx](</mnt/d/Alkaid/Desktop/工作簿1.xlsx>)、[研究操作符与横向迁移案例册.md](</mnt/d/Edge下载/研究操作符与横向迁移案例册.md>)、[科研学习与训练体系-v0.1.md](</mnt/d/Edge下载/科研学习与训练体系-v0.1.md>)。最后一份文件名 v0.1、正文 v0.3 的冲突已写入阶段 0 合同；不能静默改成一种版本。Luo 源件为 [博士生科研入门辅导.pdf](</mnt/d/Edge下载/博士生科研入门辅导.pdf>)，其方法读本已单独存在。

[progress/STATUS.md](</mnt/d/MyResearch/research_growth/progress/STATUS.md>) 顶部日期仍是 2026-05-25，而方法库已有九月增量，故不能用该旧状态页断言“近期没更新”。

## 7. 工作台与参考工具怎样接入

工作台负责任务、会话、Git、测试与交付；科研台负责研究问题、来源、关系和证据。已有 v2 文档：[progress/runbooks/workbench-v2-architecture.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/runbooks/workbench-v2-architecture.md>)、[progress/decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md>)、[progress/decisions/2026-09-01__maintenance__workbench-v2-skill-registry-design.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/2026-09-01__maintenance__workbench-v2-skill-registry-design.md>)。WP0 隔离实现的恢复口在 [progress/handoff/2026-09-01__workbench-v2-wp0-codex-execution__handoff.md](</mnt/d/MyResearch/MAS_Safety_Project/progress/handoff/2026-09-01__workbench-v2-wp0-codex-execution__handoff.md>)；这不等于独立科研台的阶段 0—5 已做。

| 参考／现有工具 | 设计文档赋予的参考价值 | 本轮可以确认的范围 |
|---|---|---|
| Obsidian | 开放文件、笔记和深链接 | 文件互通的目标已写入方案；不是任意双向覆盖同步已经实现 |
| Reviva | 资料到 Wiki／笔记／复习 | [docs/superpowers/handoffs/2026-09-04__reviva-trial-stop-handoff.md](</mnt/d/MyResearch/docs/superpowers/handoffs/2026-09-04__reviva-trial-stop-handoff.md>)记录试用停止归档；试用不等于采用 |
| NotEMD | 概念抽取、链接与文献处理 | 参考项目已列入设计；本轮不把插件存在当成 PDF 处理已完成 |
| LearnGraph | 学习证据、掌握状态、成长图 | [LearnGraph/](</mnt/d/MyResearch/LearnGraph>)等试用目录存在；不等于个人能力已经测出 |
| Supervisor-Skills | 提问、检查、论文写作方法 | [external/Supervisor-Skills/](</mnt/d/MyResearch/external/Supervisor-Skills>)实体库存在，B2/B2b 有整理；当前未证明整套 skill 已挂入科研台 |
| pengsida learning_research | Research Project、读写、最小实验、debug | [external/learning_research/](</mnt/d/MyResearch/external/learning_research>)与成长库摘录存在，B1 已整理 |
| Keelson／ArHub／Scriverse／AI Project OS／Aeroric／Wegent | 搜索聚合、领域容器、时间线、协作与任务现场 | 是独立科研台设计文档的参考名单；不是本次验证过的采用清单 |

优先桥接普通 Markdown/PDF/BibTeX/JSON 与稳定 ID；AI 生成关系先进入候选层。这些是方案口径，实际桥接实现与验收仍须另查。

## 8. 当前未完成清单与恢复入口

- [ ] RD-1：阶段 0 语义与 P0 问题确认；独立科研台完整设计及后续实现。
- [ ] 五层、旧 research/map、七图、T/R/F/E 的具体对象与更新路径统一接线。
- [ ] BR-11：W5 v1 数据对象、邻域图和既有三个数据问题。
- [ ] BR-3／BR-12／九月综述计划：按既有范围核实是否已有新批次回执；旧检索结论不得自动保鲜。
- [ ] 新增 JOS 2021 拆解回流既有论文合成与地图；论文、合作网络和本人署名分类纠偏。
- [ ] 新外部整合版、方法适配卡、B4 提案与冻结 OS 的采纳／覆盖关系明确。
- [ ] 来源库、全文检索、证据审阅、团队时间线、导出与工作台桥接的独立产品验收。

另有一处登记缺口：task_logs/INDEX 中 `TASK-20260905-003` 声称存在“双平面架构与参考池复核存档”，但本轮未在其所指的 09 月 task log 路径找到对应文件，也未找到同题 decisions 原件。保留为“索引有记录、实体待定位”，不把该行的九项断言升级为当前已验证成果。

建议阅读顺序：先看本篇 §2—§5，再打开独立科研台阶段 0 合同、GRAND_MAP 和七图主文件；需要接近期工作时转第二份清单。旧任务的完成与否按其自身证据判断，本次只完成盘点。

## 附录：research/map 文件级索引

下列按当前磁盘枚举全部 Markdown 文件及 data/ 直接文件，便于防漏和检索；PDF、第三方实现与运行产物通过其目录／manifest 导航，不逐个膨胀为主清单。未对每个历史文件重做事实审查。

| 文件 | 字节数 |
|---|---:|
| [CATALOG_research-20260813.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/CATALOG_research-20260813.md>) | 5761 |
| [CHANGELOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/CHANGELOG.md>) | 57371 |
| [FUSION_ROADMAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/FUSION_ROADMAP.md>) | 22079 |
| [GRAND_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/GRAND_MAP.md>) | 12268 |
| [README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/README.md>) | 10137 |
| [SCHEMA.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/SCHEMA.md>) | 12712 |
| [SEARCH_BOUNDARY.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/SEARCH_BOUNDARY.md>) | 4826 |
| [USER_GUIDE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/USER_GUIDE.md>) | 6132 |
| [W1_lu_side/A_petri_net_landscape.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W1_lu_side/A_petri_net_landscape.md>) | 18639 |
| [W1_lu_side/B_process_mining_landscape.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W1_lu_side/B_process_mining_landscape.md>) | 18707 |
| [W1_lu_side/C_concurrency_verification_landscape.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W1_lu_side/C_concurrency_verification_landscape.md>) | 15638 |
| [W1_lu_side/LU_SIDE_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W1_lu_side/LU_SIDE_MAP.md>) | 8920 |
| [W2_sun_side/A_llm_mas_safety_landscape.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W2_sun_side/A_llm_mas_safety_landscape.md>) | 13540 |
| [W2_sun_side/B_teams_and_openreview.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W2_sun_side/B_teams_and_openreview.md>) | 15189 |
| [W2_sun_side/C_llm_safety_parent_landscape.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W2_sun_side/C_llm_safety_parent_landscape.md>) | 17789 |
| [W2_sun_side/SUN_SIDE_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W2_sun_side/SUN_SIDE_MAP.md>) | 8023 |
| [W3_L0_global/L0_global_partition.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W3_L0_global/L0_global_partition.md>) | 11872 |
| [W3_unified/UNIFIED_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W3_unified/UNIFIED_MAP.md>) | 40205 |
| [W4_rejection_intel/A_formal_x_agent_review_meta.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W4_rejection_intel/A_formal_x_agent_review_meta.md>) | 9195 |
| [W4_rejection_intel/B_agent_reliability_review_meta.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W4_rejection_intel/B_agent_reliability_review_meta.md>) | 9241 |
| [W6_craft/ACCEPTANCE_RECEIPT_TEMPLATE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/ACCEPTANCE_RECEIPT_TEMPLATE.md>) | 978 |
| [W6_craft/A_training_and_taste.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/A_training_and_taste.md>) | 9658 |
| [W6_craft/B_correctness_and_review.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/B_correctness_and_review.md>) | 10425 |
| [W6_craft/CRAFT_MANUAL.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/CRAFT_MANUAL.md>) | 18899 |
| [W6_craft/C_debug_and_experiments.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/C_debug_and_experiments.md>) | 8256 |
| [W6_craft/D_research_intelligence_trends_and_taste.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/D_research_intelligence_trends_and_taste.md>) | 15818 |
| [W6_craft/REPRO_TEARDOWN_ACCEPTANCE_CHECKLIST.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/REPRO_TEARDOWN_ACCEPTANCE_CHECKLIST.md>) | 4823 |
| [W6_craft/receipts/2026-08-22__pilot__sbpn-e2.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W6_craft/receipts/2026-08-22__pilot__sbpn-e2.md>) | 2640 |
| [W7_companion_side/COMPANION_SIDE_MAP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/W7_companion_side/COMPANION_SIDE_MAP.md>) | 7682 |
| [_schema-source-20260813.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/_schema-source-20260813.md>) | 5918 |
| [data/SCHEMA.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/SCHEMA.md>) | 8464 |
| [data/_meta.yaml](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/_meta.yaml>) | 13112 |
| [data/map_explorer.html](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/map_explorer.html>) | 315562 |
| [data/papers.yaml](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/papers.yaml>) | 122907 |
| [data/quicklooks.yaml](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/quicklooks.yaml>) | 52102 |
| [data/references.bib](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/references.bib>) | 40086 |
| [data/schools.yaml](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/schools.yaml>) | 86005 |
| [data/teams.yaml](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/teams.yaml>) | 33410 |
| [data/topics.yaml](</mnt/d/MyResearch/MAS_Safety_Project/research/map/data/topics.yaml>) | 8418 |
| [matrices/conformance-lane-comparison.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices/conformance-lane-comparison.md>) | 13209 |
| [matrices/cross-scan.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices/cross-scan.md>) | 16118 |
| [matrices/fault-panorama.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices/fault-panorama.md>) | 14078 |
| [matrices/shield-lane-comparison.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/matrices/shield-lane-comparison.md>) | 13982 |
| [oss_landscape/C1_process_mining.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/C1_process_mining.md>) | 7902 |
| [oss_landscape/C2_conformance_verification.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/C2_conformance_verification.md>) | 14488 |
| [oss_landscape/C3_petri_net_tools.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/C3_petri_net_tools.md>) | 15832 |
| [oss_landscape/C4_agent_safety_frameworks.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/C4_agent_safety_frameworks.md>) | 10883 |
| [oss_landscape/C5_propagation_risk.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/C5_propagation_risk.md>) | 9266 |
| [oss_landscape/C6_formal_llm.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/C6_formal_llm.md>) | 4554 |
| [oss_landscape/E2_KICKOFF.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/E2_KICKOFF.md>) | 5133 |
| [oss_landscape/GUIDE_attribution_benchmarks.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/GUIDE_attribution_benchmarks.md>) | 7945 |
| [oss_landscape/GUIDE_lp06.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/GUIDE_lp06.md>) | 5131 |
| [oss_landscape/GUIDE_r_window_nine_repo.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/GUIDE_r_window_nine_repo.md>) | 5685 |
| [oss_landscape/KICKOFF.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/KICKOFF.md>) | 4278 |
| [oss_landscape/MAINTENANCE_attribution_benchmarks.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/MAINTENANCE_attribution_benchmarks.md>) | 10517 |
| [oss_landscape/MAINTENANCE_lp06.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/MAINTENANCE_lp06.md>) | 5153 |
| [oss_landscape/MAINTENANCE_r_window_nine_repo.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/MAINTENANCE_r_window_nine_repo.md>) | 7166 |
| [oss_landscape/SYNTHESIS.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/SYNTHESIS.md>) | 9017 |
| [oss_landscape/e2/ARCHITECTURE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/ARCHITECTURE.md>) | 4606 |
| [oss_landscape/e2/DELTA.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/DELTA.md>) | 3443 |
| [oss_landscape/e2/FAILURE_RECONCILIATION.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/FAILURE_RECONCILIATION.md>) | 3170 |
| [oss_landscape/e2/LOCAL_INTERFACE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/LOCAL_INTERFACE.md>) | 5550 |
| [oss_landscape/e2/LP06_ARCHITECTURE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/LP06_ARCHITECTURE.md>) | 6931 |
| [oss_landscape/e2/NEXT_PLAN.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/NEXT_PLAN.md>) | 9670 |
| [oss_landscape/e2/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/RUNLOG.md>) | 14441 |
| [oss_landscape/e2/R_BATCH2_ARCHITECTURE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/R_BATCH2_ARCHITECTURE.md>) | 7352 |
| [oss_landscape/e2/R_WINDOW_LONG_TERM_OPTIMIZATION.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/R_WINDOW_LONG_TERM_OPTIMIZATION.md>) | 14294 |
| [oss_landscape/e2/R_WINDOW_NEXT_EXECUTION_PLAN.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/R_WINDOW_NEXT_EXECUTION_PLAN.md>) | 19445 |
| [oss_landscape/e2/R_WINDOW_NINE_REPO_ARCHITECTURE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/R_WINDOW_NINE_REPO_ARCHITECTURE.md>) | 8801 |
| [oss_landscape/e2/USER_GUIDE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/USER_GUIDE.md>) | 4391 |
| [oss_landscape/e2/W1A_ABM_RUN.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_ABM_RUN.md>) | 2526 |
| [oss_landscape/e2/W1A_CLONE_INTEGRITY.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_CLONE_INTEGRITY.md>) | 1227 |
| [oss_landscape/e2/W1A_CPN_AUDIT.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_CPN_AUDIT.md>) | 3212 |
| [oss_landscape/e2/W1A_MAPPING.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_MAPPING.md>) | 4620 |
| [oss_landscape/e2/W1A_PRIVACY.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_PRIVACY.md>) | 2691 |
| [oss_landscape/e2/W1A_PRIVACY_SAMPLE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_PRIVACY_SAMPLE.md>) | 2833 |
| [oss_landscape/e2/W1A_REVIEW.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_REVIEW.md>) | 3510 |
| [oss_landscape/e2/W1A_STROBE_AUDIT.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_STROBE_AUDIT.md>) | 2471 |
| [oss_landscape/e2/W1A_VALIDATION.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1A_VALIDATION.md>) | 2671 |
| [oss_landscape/e2/W1_APPROVAL_CARD.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1_APPROVAL_CARD.md>) | 2689 |
| [oss_landscape/e2/W1_ENV_PREFLIGHT.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1_ENV_PREFLIGHT.md>) | 2912 |
| [oss_landscape/e2/W1_INTEGRATION_PLAN.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1_INTEGRATION_PLAN.md>) | 4720 |
| [oss_landscape/e2/W1_METHOD_GATE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1_METHOD_GATE.md>) | 4418 |
| [oss_landscape/e2/W1_clone_gate.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1_clone_gate.md>) | 4015 |
| [oss_landscape/e2/W1_pn_preflight.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1_pn_preflight.md>) | 5067 |
| [oss_landscape/e2/W1_risk_preflight.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1_risk_preflight.md>) | 4442 |
| [oss_landscape/e2/W1_schema_preflight.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/W1_schema_preflight.md>) | 6115 |
| [oss_landscape/e2/aegis/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/aegis/RUNLOG.md>) | 6385 |
| [oss_landscape/e2/agentdojo/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/agentdojo/RUNLOG.md>) | 4238 |
| [oss_landscape/e2/artifacts/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/artifacts/README.md>) | 540 |
| [oss_landscape/e2/cunf/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/cunf/RUNLOG.md>) | 7211 |
| [oss_landscape/e2/declare4py/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/declare4py/RUNLOG.md>) | 7621 |
| [oss_landscape/e2/entropia/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/entropia/RUNLOG.md>) | 8572 |
| [oss_landscape/e2/pybeamline/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/pybeamline/RUNLOG.md>) | 7365 |
| [oss_landscape/e2/rbatch1_three_readings/PLAN.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/rbatch1_three_readings/PLAN.md>) | 12372 |
| [oss_landscape/e2/rbatch1_three_readings/PLAN_V2.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/rbatch1_three_readings/PLAN_V2.md>) | 2877 |
| [oss_landscape/e2/rbatch1_three_readings/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/rbatch1_three_readings/RUNLOG.md>) | 7673 |
| [oss_landscape/e2/rbatch1_three_readings/SPEC_EQUIVALENCE.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/rbatch1_three_readings/SPEC_EQUIVALENCE.md>) | 6293 |
| [oss_landscape/e2/rbatch1_three_readings/STATUS.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/rbatch1_three_readings/STATUS.md>) | 6584 |
| [oss_landscape/e2/rbatch1_three_readings/results/comparison.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/rbatch1_three_readings/results/comparison.md>) | 12857 |
| [oss_landscape/e2/rbatch1_three_readings/validation/final_replay.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/rbatch1_three_readings/validation/final_replay.md>) | 40605 |
| [oss_landscape/e2/rbatch1_three_readings/validation/spec_equivalence_review.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/rbatch1_three_readings/validation/spec_equivalence_review.md>) | 6204 |
| [oss_landscape/e2/risklab/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/risklab/RUNLOG.md>) | 4469 |
| [oss_landscape/e2/tamas/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/tamas/RUNLOG.md>) | 3707 |
| [oss_landscape/e2/tapaal/RUNLOG.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/e2/tapaal/RUNLOG.md>) | 7384 |
| [oss_landscape/migration-tags.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/migration-tags.md>) | 8496 |
| [oss_landscape/teardowns/AEGIS.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/AEGIS.md>) | 17051 |
| [oss_landscape/teardowns/AgentDojo.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/AgentDojo.md>) | 11497 |
| [oss_landscape/teardowns/Cunf.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/Cunf.md>) | 21972 |
| [oss_landscape/teardowns/Declare4Py.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/Declare4Py.md>) | 17049 |
| [oss_landscape/teardowns/Entropia.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/Entropia.md>) | 16199 |
| [oss_landscape/teardowns/ProbGuard_AgentSpec.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/ProbGuard_AgentSpec.md>) | 44811 |
| [oss_landscape/teardowns/ReGA_code.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/ReGA_code.md>) | 19231 |
| [oss_landscape/teardowns/RiskLab.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/RiskLab.md>) | 10906 |
| [oss_landscape/teardowns/TAMAS.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/TAMAS.md>) | 7969 |
| [oss_landscape/teardowns/TAPAAL.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/TAPAAL.md>) | 16977 |
| [oss_landscape/teardowns/pyBeamline.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/pyBeamline.md>) | 23762 |
| [oss_landscape/teardowns/strobe_cpnpy.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/oss_landscape/teardowns/strobe_cpnpy.md>) | 24901 |
| [proposals/COLLISION_AUDIT_V2_20260813.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/COLLISION_AUDIT_V2_20260813.md>) | 9471 |
| [proposals/F2_ONEPAGER_BASELINE_DECISION-20260824.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/F2_ONEPAGER_BASELINE_DECISION-20260824.md>) | 2342 |
| [proposals/GUIDE_external_materials.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/GUIDE_external_materials.md>) | 5688 |
| [proposals/INDEX.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/INDEX.md>) | 6117 |
| [proposals/MAINTENANCE_external_materials.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/MAINTENANCE_external_materials.md>) | 8695 |
| [proposals/OE1_attachments/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/OE1_attachments/README.md>) | 2568 |
| [proposals/OE1_lu_email_v4.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/OE1_lu_email_v4.md>) | 6232 |
| [proposals/OE1_send_kit.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/OE1_send_kit.md>) | 6393 |
| [proposals/T1_T4_propagation_containment.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/T1_T4_propagation_containment.md>) | 7893 |
| [proposals/T2_conformance_formal_guarantee.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/T2_conformance_formal_guarantee.md>) | 10902 |
| [proposals/T3_memory_integrity_valueflow.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/T3_memory_integrity_valueflow.md>) | 9877 |
| [proposals/T5_companion_prob_shield.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/T5_companion_prob_shield.md>) | 14038 |
| [proposals/TODO_20260814_user.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/TODO_20260814_user.md>) | 3051 |
| [proposals/diagram/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/diagram/README.md>) | 6646 |
| [proposals/factcheck_onepager_20260813.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/factcheck_onepager_20260813.md>) | 16820 |
| [proposals/final_review_20260813.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/final_review_20260813.md>) | 18213 |
| [proposals/onepager_draft_v1.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/onepager_draft_v1.md>) | 11758 |
| [proposals/onepager_lu_variant.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/onepager_lu_variant.md>) | 10864 |
| [proposals/onepager_v2_voices.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/onepager_v2_voices.md>) | 14448 |
| [proposals/onepager_v2_voices_en.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/onepager_v2_voices_en.md>) | 17801 |
| [proposals/placeholder_sheet.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/placeholder_sheet.md>) | 8251 |
| [proposals/render/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/render/README.md>) | 3574 |
| [proposals/resume_onepage.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/proposals/resume_onepage.md>) | 5876 |
| [radar/2026-08-12_radar_baseline.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/2026-08-12_radar_baseline.md>) | 8525 |
| [radar/2026-08-13_deep_scan_delta.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/2026-08-13_deep_scan_delta.md>) | 3704 |
| [radar/2026-08-14_adhoc_scan_delta.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/2026-08-14_adhoc_scan_delta.md>) | 6086 |
| [radar/signal-lights-2026-08.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/signal-lights-2026-08.md>) | 2622 |
| [radar/teams/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/README.md>) | 5574 |
| [radar/teams/team_cnrs_bollig.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_cnrs_bollig.md>) | 2600 |
| [radar/teams/team_emoagent.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_emoagent.md>) | 3215 |
| [radar/teams/team_griffith_zhe_hou.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_griffith_zhe_hou.md>) | 2122 |
| [radar/teams/team_hf_intima.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_hf_intima.md>) | 3091 |
| [radar/teams/team_ntu_yang_liu.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_ntu_yang_liu.md>) | 2590 |
| [radar/teams/team_nus_jin_song_dong.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_nus_jin_song_dong.md>) | 3114 |
| [radar/teams/team_smu_jun_sun.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_smu_jun_sun.md>) | 5363 |
| [radar/teams/team_smu_xiaofei_xie.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_smu_xiaofei_xie.md>) | 2501 |
| [radar/teams/team_tongji_guanjun_liu.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_tongji_guanjun_liu.md>) | 3542 |
| [radar/teams/team_toronto_mcilraith.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_toronto_mcilraith.md>) | 2334 |
| [radar/teams/team_utaustin_topcu.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/teams/team_utaustin_topcu.md>) | 1902 |
| [radar/tools/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/radar/tools/README.md>) | 4674 |
| [surveys/EXECUTION_PLAN.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/EXECUTION_PLAN.md>) | 10012 |
| [surveys/NEXT_SESSION.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/NEXT_SESSION.md>) | 2245 |
| [surveys/PLAN_survey_gapfill_202609.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/PLAN_survey_gapfill_202609.md>) | 6175 |
| [surveys/README.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/README.md>) | 3402 |
| [surveys/RESEARCH_SOP.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/RESEARCH_SOP.md>) | 5818 |
| [surveys/SURVEY_LEDGER.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/SURVEY_LEDGER.md>) | 6138 |
| [surveys/USER-TODO.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/USER-TODO.md>) | 3482 |
| [surveys/cards-formal/Bollig2026_runtime-verification-lectures.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/cards-formal/Bollig2026_runtime-verification-lectures.md>) | 27230 |
| [surveys/cards-formal/Murata1989_petri-nets.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/cards-formal/Murata1989_petri-nets.md>) | 31713 |
| [surveys/cards-security/LASM_layered-attack-surface.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/cards-security/LASM_layered-attack-surface.md>) | 27478 |
| [surveys/cards-security/QUICK_attack-defense-landscape_and_lifecycle.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/cards-security/QUICK_attack-defense-landscape_and_lifecycle.md>) | 21012 |
| [surveys/cards-security/TrustAgent_KDD2025.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/cards-security/TrustAgent_KDD2025.md>) | 26140 |
| [surveys/collision-report.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/collision-report.md>) | 22317 |
| [surveys/collision_tool/missing_agent-memory.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/collision_tool/missing_agent-memory.md>) | 16059 |
| [surveys/collision_tool/missing_trustagent.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/collision_tool/missing_trustagent.md>) | 13443 |
| [surveys/crosswalk-W2A.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/crosswalk-W2A.md>) | 31568 |
| [surveys/evidence-for-T5-OE1.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/surveys/evidence-for-T5-OE1.md>) | 32710 |
| [w5_design_sprint_20260812/KICKOFF.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/w5_design_sprint_20260812/KICKOFF.md>) | 612 |
| [w5_design_sprint_20260813/01_tool_landscape.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/w5_design_sprint_20260813/01_tool_landscape.md>) | 18958 |
| [w5_design_sprint_20260813/02_matrix_cell_schema.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/w5_design_sprint_20260813/02_matrix_cell_schema.md>) | 26618 |
| [w5_design_sprint_20260813/03_coverage_extension_radar.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/w5_design_sprint_20260813/03_coverage_extension_radar.md>) | 36828 |
| [w5_design_sprint_20260813/04_reconciliation_migration.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/w5_design_sprint_20260813/04_reconciliation_migration.md>) | 31015 |
| [w5_design_sprint_20260813/KICKOFF.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/w5_design_sprint_20260813/KICKOFF.md>) | 1388 |
| [w5_design_sprint_20260813/W5_V1_PLAN.md](</mnt/d/MyResearch/MAS_Safety_Project/research/map/w5_design_sprint_20260813/W5_V1_PLAN.md>) | 3514 |

本附录列出 182 个实际文件；是文件清单，不是研究完成度。
