# 科研台与学习台统一参考清单（2026-09-15）

日期：2026-09-15。任务：`TASK-20260915-008`。状态：`ARCHIVED / REFERENCE-ONLY / NO-ADOPTION-OR-RUN-AUTHORIZATION`。

> 后续执行更新：TASK-009已交[评估与融入详细计划](REFERENCE_INTEGRATION_PLAN.md)；用户随后明确“继续推进／直接做／做”，TASK-010已交[第一轮评估结果](REFERENCE_EVALUATION.md)，包括需求对账、固定源码比较及最小提案。TASK-008（原草稿号004已作废）续将用户提供的“科研副导师 / AI Research Copilot”截图登记为R11，并交[科研项目驾驶舱详细方案](RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md)。下文保留各阶段事实，§7.5记录前序核验，§7.6记录R11边界；当前仍不含安装、模型调用、真实试用、应用／课程修改或正式采用。本件继续是唯一参考事实清单。

返回[两台方案入口](README.md)与[首批方案后续参考](FIRST_BUILD_PLAN.md#9-2026-09-15-后续施工参考备注)。本件不是新施工合同，不改变 A／B 的验收结论、C04–C07 的授权边界或既有多层网络设计。

## 0. 三次输入统一登记

本件是本轮参考清单的唯一正本，合并：① PlanWeave 链接、存档要求及享做笔记意向；② 用户追加的项目介绍与工程／学习方法评论；③ TreeTalk-Obsidian 迁移地址及“原 TreeTalkGPT 仍值得参考”的补充。用户随后明确要求三次输入先统一存档；本轮到此收束，不继续扩展选型或施工。其他文件只保留指针和任务回执，不另建平行清单。

同日续补：用户再提供 ownership-v3 三缺口执行交接，单列为内部资料 I01（§9），不混入工具选型。2026-09-16再增加截图参考R11；2026-09-17增加外置记忆与跨窗口连续性教程／文献清单R12。2026-09-18分两批追加R13（工作台／科研台社媒帖参考，来自压缩前会话）、R14（用户自行按考研／工作台／科研台三类标注的链接批，见§7.8）。**同日用户再追加两个考研链接（Pkmer-Math、Math-And-English-Library）要求与R14考研项、R13的obsidian_math及已独立深查的kaoyan放一起比较，登记为R15；随后用6个并行子代理把R13全部11项＋R14非重复13项＋R15新增2项（合计26个URL，逐一核对无遗漏无重复计数）统一推进到机制层核查（核心内容／工作流／能不能用得上），见§7.9**。当前共 **16 项：R01–R15 外部工具／方法／产品壳参考＋I01 内部施工交接**。TASK-010“11项”仍指R11加入前的历史评估批次。原交接与方案仍是各自工作的记录，本清单只汇集入口、当前缺口和待决事项，不另复制一套执行合同。

| 编号 | 参考项与入口 | 借鉴位置／用户关注 | 核对状态与边界 |
|---|---|---|---|
| R01 | [PlanWeave](https://github.com/GaosCode/PlanWeave)；[main目录](https://github.com/GaosCode/PlanWeave/tree/main)；[中文说明](https://github.com/GaosCode/PlanWeave/blob/main/readme/README.zh-CN.md)；视频 [BV18oTq65Ez9](https://www.bilibili.com/video/BV18oTq65Ez9/) | 从计划到任务依赖、执行、评审与反馈 | 固定版本说明及部分源码已核，详见 §2–5、§7.5；视频仅登记用户所给编号，未观看或转载 |
| R02 | 工程经验评论：Docker Desktop、Anaconda Navigator、JupyterLab；doctor、trace/log、CI/CD、DevSecOps | 环境／启动入口、状态反馈、诊断、可追踪执行与交付方法 | 用户转述评论，无独立原帖地址；是背景参考，不是全部引入要求 |
| R03 | 学习方法评论：类比、费曼式复述；提示词包含条件＋特殊要求＋目的 | 零基础解释、暴露理解缺口、把任务交代清楚 | 个人经验材料，非已验证的教学定律或新冻结学习规则 |
| R04 | OpenScience A：终端启动、浏览器访问版 | 本地科研工作区、skills／MCP 扩展的候选参照 | **项目身份待补**：用户材料未给唯一仓库／视频链接，不按名称或 star 数猜测认领 |
| R05 | OpenScience B：桌面版 | Python／R 环境、数据库连接、论文评审与分析界面的候选参照 | **项目身份待补**：与 R04 分开登记；其本地性、功能、测试版与发布时间均仅为介绍方声明 |
| R06 | [OrbitStart](https://github.com/xuxinxi14/OrbitStart)；[用户提供的夸克分享](https://pan.quark.cn/s/b8c4a1de0daf?pwd=eV2f) | Windows 应用、网址、文件夹、脚本与真实任务工作区入口 | 固定提交 README／MIT 许可有界核对；未访问网盘、未下载安装包，详见 §7 |
| R07 | [ThoughtDAG](https://github.com/chenxiachan/thoughtdag)；[介绍页](https://chenxiachan.github.io/thoughtdag/) | 分支／合并／裁剪对话上下文，材料摘录与回链 | 固定README／许可及上下文、生成调用边界、导出关键源码已读；未实测，详见 §7.5 |
| R08 | [TreeTalkGPT（README 标题 TreeTalk）](https://github.com/safasffa111/TreeTalkGPT) | 原桌面客户端的问题树、框选追问、本地知识引用等交互参考 | **保留参考价值**；当前 README 同时注明停止维护、下载暂停与错误发布警告；不推荐现有安装包 |
| R09 | [TreeTalk-Obsidian](https://github.com/safasffa111/TreeTalk-Obsidian) | 用户补充的迁移去向；Obsidian 内分支追问、来源上下文与 Markdown 沉淀 | README／许可及摘录、回链、沉淀投影和来源写回关键源码已核，详见 §7.5；不删除 R08，不称已适配两台 |
| R10 | 享做笔记；[App Store 产品说明](https://apps.apple.com/cn/app/id1642325772) | 平板／电脑上的部分具体学习、手写推导与批注 | 保留用户使用意向；厂商多端声明已核，真实设备／导出／备份未测，详见 §6 |
| R11 | 用户提供截图：“科研副导师 / AI Research Copilot”；原始链接、作者、版本与许可待补 | 项目台、资料与证据、研究路线、Idea评估、文献调研、论文蓝图、章节写作、图表整稿、投稿审查、Skills、导出和Codex入口的一体化产品壳 | `IDENTITY-OPEN / SCREENSHOT-ONLY`；只核截图可见信息架构，不证明功能存在或可用。作为[驾驶舱方案](RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md)的UI参考，不安装、不复制、不新建第四套正本 |
| R12 | [agent-stack-notes](https://github.com/marikagura/agent-stack-notes)，固定提交 [`e17d0a8`](https://github.com/marikagura/agent-stack-notes/tree/e17d0a8edff0b01d340c385d936b5ecaca5e8178) | 外置记忆的写入／存储／维护／检索／注入／遗忘；跨窗口 ingestion／injection／routing／delta；组件分层与评测问题 | `REFERENCE-ONLY / README+3-TUTORIALS-READ / NOT-ADOPTED`；可用于G0/P1/P4的恢复、来源权威、新鲜度与评测检查。文章声明 CC BY-NC-SA 4.0；当前只登记链接与摘要，不复制文章、不接入其关联实现、不证明文献核证质量或本地适用性 |
| R13 | 社媒帖转述的 Obsidian 插件批（无原始 URL，本轮按名称 WebSearch 核身份）：Research OS、Xove Dashboard、markwhen、Claudian、obsidian_math、Editing Toolbar、Apex Dashboard、Calendar、Custom Frames、Excalidraw、Xiaohongshu Importer；另提及"Lazy-Kaoyan-Library"未附链接 | 工作台候选：仪表盘/看板/时间线/网页嵌入/社媒导入；科研台候选：文献/概念/AI 服务一体插件、考研笔记组织范例 | `IDENTITY-PARTIAL / NAME-SEARCH-ONLY`；11 项按名称找到高置信匹配仓库（见§7.8.1），"Lazy-Kaoyan-Library"当时未找到同名仓库——**已在R14解决**，见下 |
| R14 | 用户 2026-09-18 自行分类给出的确切 URL 批（考研 1／工作台 9／科研 4，含 R13 未解决的 Lazy-Kaoyan-Library 及与 R13 重复的 Research OS） | 考研笔记库组织范例；工作台候选：vault 模板／任务与时间管理插件；科研台候选：个人概念库／科研入门指南／Python 研究方法教程 | `URL-CONFIRMED / README-READ`；用户自带分类，本轮按原样保留三分类，见§7.8.2；与 R13 重叠项已去重，不重复计数 |
| R15 | 用户 2026-09-18 追加两个考研链接（[Pkmer-Math](https://github.com/PKM-er/Pkmer-Math)、[Math-And-English-Library](https://github.com/WandD2277/Math-And-English-Library)），要求与 R14 的 Lazy-Kaoyan-Library、R13 的 obsidian_math、已独立深查的 `virtualxiaoman/kaoyan`（TASK-20260911-007）放一起比较；随后 6 个并行子代理把 R13 全 11 项＋R14 非重复 13 项＋本次 2 项新链接（共 26 个 URL）统一推进到机制层核查 | 考研笔记库组织范例横向比较（血缘关系／工作流有无／能否迁移到学习台或科研台）；R13/R14 里工作台／科研台插件的核心机制与具体可用场景（不预设槽位归类） | `URL-CONFIRMED / MECHANISM-LEVEL-READ`；`TASK-20260918-004`；6 批只读子代理各自遵守 5 caps（URL/字数/时间/工具/done_when），逐项产出身份坐标／核心工作流／血缘或与已知缺口的匹配场景／边界，见§7.9；仍不做"借鉴/转化设计/隔离试用/正式接入/暂存不采用"五选一处置判断，不判断是否新增"考研台"这一架构槽位 |

R06 分享提取码由用户提供为 `eV2f`，仅作为原始入口信息保存。R08／R09 的用户原始 SSH 地址分别是 `git@github.com:safasffa111/TreeTalkGPT.git`、`git@github.com:safasffa111/TreeTalk-Obsidian.git`；本次只读核对使用 HTTPS，不配置 SSH、不 clone 或导入。

来源归属：项目声明归相应仓库维护者；视频、评论及两款 OpenScience 的介绍来自用户本轮转交，未逐一核验作者。`BV18oTq65Ez9` 只关联所给 PlanWeave 介绍，不擅自绑定到其他段落。保留“未经作者授权禁止转载”的限制，本件仅登记链接、归属和必要研究摘要，不复制视频／安装包、不公开分发原介绍。代码的 MIT 许可不自动覆盖视频或其他平台素材。

## 1. 用户要求与本轮结论

用户提供 [PlanWeave 中文 README](https://github.com/GaosCode/PlanWeave/blob/main/readme/README.zh-CN.md)，随后明确要求“先进行存档，加入下一步的施工方案里，做备注参考用”。同时提出准备让平板和电脑使用享做笔记承担部分具体学习，并询问意见。

- **已经确认**：将 PlanWeave 评估存档，并加入后续方案的候选参考。
- **没有确认**：正式选型、安装 skills／CLI／桌面端、导入真实计划、Auto Run、部署、Tunnel、远程 Agent、替换现有任务正本。
- **享做笔记是当前使用意向与建议**：适合作为部分手写／批注活动的工具候选；设备组合、同步条件、导出与备份仍待核。不把询问可行性改写为已完成接入或已选定全部学习软件。
- 本次仅文档存档和路由接线；不改应用、默认配置、真实数据库、课程、答案、sealed，不购买、不安装、不提交或推送。
- 后续追加的参考统一纳入 §0 与 §7；“值得参考”不等于“仍在维护／可安全安装／已决定采用”。本轮不为每个参考创建施工任务，也不要求全部工具相互接入。

## 2. PlanWeave：评估范围与来源

上一轮只读核对版本：`0.4.0`；`git ls-remote` 返回 main 提交 `21ea024eb23bd35d88f5183c9a2622d624ea5185`。以下使用固定提交链接，避免 main 更新后把新行为倒写成本次观察。当前存档只保存结论、关键语义及来源指针，未镜像整个仓库，未运行上游测试。

| 来源 | 本次用于核对的内容 |
|---|---|
| [中文 README](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/readme/README.zh-CN.md) | 计划块、执行／Review／Feedback、桌面与CLI、导入路径；未签名安装包与实验性远程协作声明 |
| [DEVELOPMENT](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/DEVELOPMENT.md) | Node.js ≥22.13；运行与分布式边界；不管理Git分支、worktree、合并；测试分层及live证据要求 |
| [plan-importer 文档](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/skills/plan-importer/SKILL.md) | 从已有强来源计划构造执行包；目标覆盖、对象生命周期、提示放置、依赖；sharedResources只是协调提示 |
| [plan-auditor 文档](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/skills/plan-auditor/SKILL.md) | 从输入到消费者／产出与失败路径审计划，不以任务数代替覆盖；审计不等于自动修改授权 |
| [claimScheduler.ts](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/packages/runtime/src/taskManager/claimScheduler.ts#L155) | manifest中parallel.enabled和maxConcurrent参与领取容量计算 |
| [reviewSubmission.ts](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/packages/runtime/src/taskManager/reviewSubmission.ts#L696) | 反馈次数耗尽但未通过时，status仍可能为completed，同时verdict=needs_changes、completionReason=max_cycles_reached |
| [并发测试定义](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/packages/runtime/src/__tests__/autoRunParallelExecution.test.ts)／[评审次数测试定义](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/packages/runtime/src/__tests__/submitReviewMaxCycles.test.ts) | 已有对应测试源码；本轮未运行，不声称上游当前测试全过 |
| [LICENSE](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/LICENSE) | MIT；若后续复用代码或文档须保留许可与署名要求 |

GitHub API 元数据访问在上一轮返回403；README、开发文档、固定提交源码与git远端引用可读。不据此评价维护活跃度、release质量或长期稳定性，也没有证明它与TaskQuay是同一项目。

## 3. 适用位置与不承担的职责

优先考虑它帮助**两台的工程施工**：把已获批要求变成有依赖、有检查和评审的执行块，留下可恢复回执。以后是否承担常态研究执行另评估。

| 现有系统／工具 | 保留职责 |
|---|---|
| 学习台 | 目标三档要求、教学路线、尝试／反馈／复测、本人能力证据 |
| 科研台及多层网络 | 问题、知识、方法、来源、跨层关系、研究判断与认识变化 |
| 既有工作台／任务正本 | 授权、优先级、任务身份、预算、依赖、最终验收与跨台回链 |
| PlanWeave候选执行包 | 获准任务的block、运行事实、检查／评审反馈与恢复；不得反向定义研究真伪或本人掌握 |

任务依赖图不等于多层知识／科研网络。共享对象不等于共享所有断言的真假；执行块通过不自动更新课程PASS或研究结论。

既有[工作台设想](../three-desks-v0.1/WORKBENCH.md#6-taskquay及现有工作台的接入位置)已给TaskQuay保留候选连接器位置。后续应比较各自角色和成本，不同时引入两套重复调度、不默认替换任一已运行系统。

## 4. 采用前必须核实的适配问题

1. **状态映射**：不得将completed直接映射为TECH-PASS；必须同时读取verdict与completionReason。轮次耗尽应保留未通过事实，由现有验收负责者裁定，不能自动转绿。
2. **并发与写域**：总并发2包含主控；有主控时不能再开两个Agent。上游共享资源提示不是文件互斥，依赖边、只读子代理约束、单写域和Git合并责任继续由本地约定承担。
3. **来源与任务正本**：保留现有需求／合同的权威；执行包与任务ID、来源路径及版本建立明确对应，不能双向静默改写。运行状态由对应runtime管理，不手改state伪造完成。
4. **导入路径差异**：README推荐draft validate／quality／preview／import；同提交的importer说明仍含直接写package文件的流程。试点须核所选版本的实际行为，不盲目执行任一路径。
5. **运行与恢复**：显式持久目录、执行范围和输出；先本地单步。远程Host、Tunnel、桌面壳与无人值守循环不是首轮默认项。它不能解除429或提供未获得的账户权限。
6. **审计能力上限**：graph quality和审计提示能发现结构问题，但不能保证知识内容正确、需求穷尽或真实使用有效；独立复核及用户验收继续分开。

## 5. 下一步施工中如何引用（仅候选）

下一批仍先处理：最新需求追踪与A／B覆盖对账、内容和多层关系反例、真实试用、独立评审开放项。**PlanWeave不是继续两台施工的新增硬前置**，即使不采用，也可借鉴其流程覆盖与可验证完成条件。

若以后明确批准试点，建议只选一个未施工、主要只读的小包，例如“C06剩余需求与验收对账”，不重跑A／B：

1. 固定版本和隔离持久目录，核任务号／来源版本与写域映射。
2. 从现有强来源文档构造少量任务块及必要依赖，预览不直接改真实任务。
3. 校验、人工审阅后单步执行，先不用远程或无人值守循环。
4. 验证失败／中断／评审退回／恢复与回执回链，明确模型、时间和轮数限制。
5. 根据成本与结果决定采用、仅借用方法或停放；本件不代替试点任务授权。

候选验收标准（尚未实跑）：原需求没有减弱；每块有输入／范围／产物／检查依据；评审未过、429、中断、轮次耗尽均不误报通过；恢复不重复提交或覆盖既有记录；并发及只读边界满足；回执可回现有任务；维护开销可接受。是否启用、顺序与具体测试矩阵在批准试点时单列。

## 6. 享做笔记：部分具体学习的候选入口

### 已核与待核

2026-09-15读取[开发者在App Store的产品说明](https://apps.apple.com/cn/app/id1642325772)：列明手写、PDF/PPT/WORD/EPUB导入、文档批注、脑图／闪卡，以及Android、iOS、Mac、Windows、HarmonyOS和跨设备同步。本次通过Apple公开产品查询取得这些说明；它们是厂商声明，不是本机兼容性／同步可靠性实测。

尚未确认：用户平板系统和两端软件版本、跨平台功能差异、账号／套餐条件、导出格式与页码／笔迹保真、原生可编辑备份及恢复、离线冲突行为、是否有稳定页面深链接或可用API。不据厂商“支持多端”推定零差异或免配置。已向用户询问平板系统；电脑暂按现有Windows＋WSL环境理解。

### 建议分工（待真实试用）

- 享做：手写数学／统计推导、数据结构图解与手推、英文／论文批注、临时草图；不必每页登记任务或生成正式关系。
- 电脑：源码阅读、实现、实验和正式文件管理；具体学习也可以按输入习惯留在电脑端。
- 学习台：目标、知识关联、必要来源位置、本人尝试及帮助条件、反馈／复测和继续点。重要原始作答引用或附可读快照，不重抄全部笔记。
- 科研台：从批注或作答中提炼确实值得追踪的问题／判断，关联原产物；笔记中的脑图／草图先是表达，未经确认不能当正式多层关系。

建议先以一个短小真实学习过程验证：写一页图／递归或概率题→电脑查看→按实际支持格式导出或保存清晰页面快照→检查符号、页序、笔迹与来源→在学习记录中保存引用和一句继续点。只有重要反馈／重做节点才留版本，普通草稿无需重复录入。

离线与同步、导出可读性、独立备份恢复分别检查；云同步不等于独立备份。若使用AI讲解或答案提示，注明发生在独立尝试之前还是之后；原尝试不要被清稿覆盖。OCR只作辅助，公式和代码以原笔迹／原文件核对。

目前没有享做自动接入学习台的实现；先人工导出／附页或来源引用，确有重复负担后再讨论自动化。不得把兼容字段未实现写成已能跳回享做某页。受版权、保密或sealed约束的材料不默认上传云或AI。

## 7. 追加清单的来源备注与适用边界

### 7.1 固定来源与本次阅读范围

以下提交为 2026-09-15 只读 `git ls-remote --symref … HEAD` 的返回值；不以 README 版本号代替安装包的来源验证，不评价未核查的 release 或长期维护质量。

| 项目 | 固定提交与来源 | 已读／未做 |
|---|---|---|
| OrbitStart | `5cea025c21f19d436e8503ff6c2a443dea84a3d5`；[README](https://github.com/xuxinxi14/OrbitStart/blob/5cea025c21f19d436e8503ff6c2a443dea84a3d5/README.md)、[LICENSE](https://github.com/xuxinxi14/OrbitStart/blob/5cea025c21f19d436e8503ff6c2a443dea84a3d5/LICENSE) | README 标为 0.9.1；核入口／工作区、数据与隐私、备份及边界相关段；MIT（Xinxi Xu）；未审全源码或实跑 |
| ThoughtDAG | `3c57d429f83946498fce06d8e2a579c99f102e1e`；[README](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/README.md)、[LICENSE](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/LICENSE) | README上下文、材料、导出与隐私；MIT（Xia Chen）；TASK-010续核graph/context-builder/streaming/export关键路径，见§7.5；未装客户端／MCP／插件、未索引本地会话 |
| TreeTalkGPT | `6b15e5bc428c36302e00069ed23036911e91a252`；[README](https://github.com/safasffa111/TreeTalkGPT/blob/6b15e5bc428c36302e00069ed23036911e91a252/README.md)、[LICENSE](https://github.com/safasffa111/TreeTalkGPT/blob/6b15e5bc428c36302e00069ed23036911e91a252/LICENSE) | README明确停止维护、转向Obsidian与v0.2.3错误发布；MIT（TreeTalk contributors）；TASK-010续核PROJECT_SOURCE来源订正，见§7.5；未审可信历史实现／安装包 |
| TreeTalk-Obsidian | `09de5a6ea424a4ed32af0555c95540fa42bb806d`；[README](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/README.md)、[LICENSE](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/LICENSE) | README首135行声明0.9.5桌面版；MIT（Len_shan）；TASK-010续核excerpt-drag/source-link-handler/relationship-graph/capture-service关键路径，见§7.5；未实测移动端或实际请求 |

### 7.2 可以借鉴什么，不要混淆什么

- **OrbitStart 是资源与启动入口参考。** README 列出资源搜索、工作区步骤／依赖和启动控制；也声明当前无内置云同步、插件权限展示不等于系统级沙箱。可借鉴按任务找到工具与材料，不把“打开环境”算成“执行成功”。其 Obsidian 集成声明可将任务勾选写回 Markdown，未来若试用需明确写域，不能让它自动修改现有任务正本。当前不接入 WSL 脚本或真实 Vault。
- **ThoughtDAG 是对话上下文控制参考。** README 的核心是连线决定后续模型输入，并支持材料来源、分支合并／裁剪、过时提示和导出。它的边首先表达上下文选择，不等于知识的前置、支持／反驳或科研因果关系；裁剪下次输入也不代表删除原始研究证据。宣传中的准确率改善不作为本次独立结论。
- **两个 TreeTalk 都保留。** 用户指出旧库仍值得参考；这与上游“停止维护”的声明可以同时成立，分别属于参考价值和维护状态。原仓库适合保留交互／历史思路；Obsidian 版适合参考精确选段、来源回跳和显式 Markdown 沉淀。迁移不是本地资料迁移授权，不要求用户转用 Obsidian，也不能声称已经与享做联通。
- **TreeTalk-Obsidian 的两类图操作不能混用。** README 将沉淀关系图中的边限定为树结构／框选来源／关联笔记；右键排除主要用于图上聚焦及下一次沉淀范围。不能据此宣称它与 ThoughtDAG 的“改连线即改模型输入”行为相同。README 还说明对话存在 Vault 私有目录，主动沉淀才成为普通 Markdown；原对话永久删除后，来源回链可能失效。
- **多层知识／科研网络仍按自己的语义建设。** 启动依赖图、任务执行图、对话上下文图和知识／证据层可以引用同一产物，但不是同一张图，也不能用对话树或 WikiLink 自动替代跨层关系、来源条件与本人能力证据。

### 7.3 工程与学习方法评论

工程评论提醒：环境管理、启动自检、状态反馈、日志追踪与交付检查已有成熟方法可参考。Docker Desktop、Anaconda Navigator、JupyterLab 的职责并不完全相同；此处登记启发，不据评论为它们做逐项功能背书。后续先查两台现有机制，确有缺口再提出增量，不因此加入 Docker、CI/CD、DevSecOps、通用遥测或新的基础设施。

学习评论保留三点：用已有经验类比陌生对象；让学习者以自己的话解释、暴露缺口；提问时说明已有基础、限制和目的。类比要标出失效位置，复述不是唯一掌握证据，还需独立作答、修改／预测、迁移或延迟复测。AI 再次回答也不等于独立事实核验；提示词应清楚，不把篇幅或固定模板当质量保证。这里只作方法参考，不改四论文 rubric、本人 PASS 或考研科目，不因评论例子新增课程。

### 7.4 OpenScience 与本地隐私：未决项

用户材料介绍两款同名 OpenScience：A 为终端＋浏览器版，声称约 2.1k star、内置 skills／MCP、较适配生物／物理／机器学习；B 为桌面测试版，声称内置或检测 Python／R、数据库 MCP 与论文评审，且启动早于 Claude Science。它们的唯一项目地址缺失，均标为 `IDENTITY-OPEN / CLAIMS-UNVERIFIED`，等待用户提供仓库或可定位视频；不扩展搜索并猜测选中任一同名项目。

介绍中的账号封禁经历、平台数据保存方式、两款工具“完全本地／支持任意模型”及实测效果，均为介绍方声明，本次未独立验证。能借鉴的是关注数据可控和工作流可恢复，不能据此保证任一工具不外传数据。

**本地存储、本地运行、模型推理位置、联网检索与同步是不同问题。** ThoughtDAG README 明说提问时抽取文本可能发往所接模型；TreeTalk-Obsidian README 明说对话、框选和关联笔记正文会发送至所配 API。以后评估需逐项看实际数据流、权限与可恢复导出，不能仅凭“本地工作台”判断隐私。当前不上传研究数据、原作答、sealed 或完整会话，不配置远程模型／MCP。

### 7.5 TASK-010新增源码核验与链接补充

固定版本沿用§2／§7.1，没有把main当前内容混入旧结论。准确`file:line`及比较决定集中在[评估§3–5](REFERENCE_EVALUATION.md#3-thoughtdag与两个treetalk同场景比较)：

- R07：`graph.ts:80–123`分材料／引用／主线；`context-builder.ts:285–349`区分折叠与归档；`streaming.ts:211–228`在组装后另插memory，`:276–295`接llmCallStream并只记请求摘要等元数据。`export.ts:42–69`的JSON备份与`:253–287`的Markdown不同，后者不含附件正文且截短branchContext。各provider／工具发送链、真实请求和恢复未验证。
- R08：[PROJECT_SOURCE](https://github.com/safasffa111/TreeTalkGPT/blob/6b15e5bc428c36302e00069ed23036911e91a252/PROJECT_SOURCE.md#L18)的18–25行订正旧发布来源，47–49行说明移除旧源码；这是维护者声明，不是本轮签名／安装包核验。保留交互参考，当前安装候选暂停。
- R09：`excerpt-drag.ts:204–228`为带身份／anchor的摘录回链；`source-link-handler.ts:28–73`先查活动再查历史；`state.ts:55–73`和`model.ts:201–218`控制沉淀投影。`capture-service.ts:569–585`单回答只额外写标题和正文；`:594–635`整树沉淀调用`:512–549`来源笔记写回，错误被捕获而不令导出失败。不能把导出成功当全部回链成功。
- R01：续核`reviewSubmission.ts:664–730`的通过／轮数耗尽分支、`claimScheduler.ts:155–173`容量语义和importer强来源／消费者检查；实际导入、恢复与429未实测。R02与本地配置、链接检查、日志和A/B恢复入口作静态对照，不增加基础设施。
- 用户在执行中又提供6个链接：PlanWeave仓库根与`tree/main`为同一R01，另外四个为现有R06/R07/R08/R09。已把main目录入口补在R01；**不是6个新项目**，总数仍为11项。该消息未补OpenScience身份，也不是安装或真实库接入授权。

### 7.6 TASK-008新增产品壳截图参考（原草稿号004作废）

R11的截图可见左侧项目台、资料与证据、研究路线、Idea评估、文献调研、论文蓝图、章节写作、图表整稿、投稿审查、科研Skills、导出与系统入口；主区显示八阶段、原始资料数、Skill运行数、人工待办、下一门、本地证据目录和“在Codex中打开”。这些只是界面文字与布局观察，不能证明计数来源、Skill实际运行、阶段验收、数据本地性、Codex派发、正式导出或任何后端能力。

对本地最有价值的是“一项目入口＋证据脊柱＋阶段门＋下一步”的组织方式。R01-R10与R12提供机制与边界，R11提供产品封装参考；这些参考已在[科研项目驾驶舱方案](RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md)合并。八阶段只作现有正本的派生导航，不等于RD2八层／七图或八个新施工包；Skill运行、技术通过、独立评审、研究判断与用户接受保持分离。

R11恢复条件是取得原始产品链接、仓库、作者页面或可核版本。取得前不进行同名搜索猜测、不复制截图视觉资产、不登记许可证结论；不阻塞本地只读信息架构设计。

### 7.7 R12：外置记忆与跨窗口连续性方法参考

2026-09-17只读核对 `agent-stack-notes` 的 README 与三篇教程《记忆系统拆解》《无缝换窗拆解》《系统清单和名词手册》，并用远端 HEAD 固定为 `e17d0a8edff0b01d340c385d936b5ecaca5e8178`。仓库把记忆拆为写入、存储、维护、检索、注入和遗忘，把跨窗口连续性拆为 ingestion、injection、routing 和 delta；同时强调进程无状态、外部存储作为权威来源、按需注入、append-only／人工整理、路由隐私边界、增量水位线，以及先建评测台再增加检索组件。

对驾驶舱可借鉴的是检查框架，而不是照搬一套新系统：G0可用“写入者—正本—维护者—检索者—注入消费者—失效／遗忘规则”补查跨仓权威和恢复链；P1可核启动注入、来源版本、新鲜度及 `NON-ATOMIC`；P4可区分Skill目录、引用和有效运行回执；恢复测试可覆盖旧快照、增量游标、并发写入和上下文轮转后的来源可追溯。现有task log、handoff、CURRENT、对象revision和append-only证据仍是本地正本，不因R12另建“记忆库”。

当前证据仅支持方法参考：未审完整文献地图及每条引用，未运行关联的 `kimi-core`、`kimi-room` 或其他实现，未比较检索指标，也未验证其结论适合本项目数据分布。README声明文章采用 CC BY-NC-SA 4.0；因此本清单只保留必要摘要与署名链接，不复制或改编其正文。若以后要采用实现或大段改编，须另核对应仓库、代码许可证、数据流、固定版本、评测集和退出方案。

### 7.8 R13/R14：2026-09-18 工作台／科研台/考研插件批（两次追加）

用户明确要求"存一下是工作台参考和科研台参考"。以下按用户给的类别原样保留，只做身份核验和去重，不改用户分类，不做选型建议。

#### 7.8.1 R13：社媒帖转述批（无原始链接，按名称 WebSearch 核身份）

| 名称 | 核实身份 | 一句话用途 | 用户帖子里的原始描述要点 |
|---|---|---|---|
| Research OS | [kivvng726/obsidian-research-os](https://github.com/kivvng726/obsidian-research-os) | 文献/概念/AI 服务一体化科研插件 | 帖子给的是插件商店安装路径提醒（`.obsidian/plugins/research-os/manifest.json`，警告"不要多套一层文件夹"），非仓库链接；`nachiket273/obsidian-research-flow`、`Louanna1208/research-atlas-obsidian` 等同类仓一并搜出，未逐一核实是否为独立项目或改名/fork |
| Xove Dashboard | [cenyuhing11-png/Xove-Dashboard-Custom](https://github.com/cenyuhing11-png/Xove-Dashboard-Custom) | 本地优先任务/项目/甘特图/看板一体仪表盘 | 帖子含 v0.2.9 版本发布说明（甘特图缩放、看板、日历、Markdown+frontmatter本地存储、首页banner/热力图/倒计时）及评论区功能请求（日期选择器联动、去banner、独立任务、日历联动、CPU占用、Tasks插件迁移兼容性、编辑模式易发现性、冷启动慢、`.mw`格式吐槽） |
| markwhen | [mark-when/obsidian-plugin](https://github.com/mark-when/obsidian-plugin) | `.mw` 格式时间线/甘特图插件 | 帖子含语法说明、"网页版>VSCode插件>Obsidian插件"能力排序、日历/地图视图提及 |
| Claudian | [YishenTu/claudian](https://github.com/YishenTu/claudian) | 把 Claude Code/Codex 等 AI 编码 agent 嵌入 Obsidian vault 当工作目录 | MIT 许可，帖子称"1.8M+下载"（厂商/社区自述，未独立核实）；`rawlencecn`/`wnghr`/`heranliu`/`vrevolverrr` 等同名同描述仓大概率为 fork/镜像，未逐一验证独立性 |
| obsidian_math | [BlandAlpha/obsidian_math](https://github.com/BlandAlpha/obsidian_math) | 考研数学2笔记（非插件，是内容仓） | 来自"上岸浙大光电"帖提及"搜 GitHub 找 obsidian_math"；`Sun8854/...`（明确注明基于本仓）、`PKM-er/Pkmer-Math`、`goodnight654/Math`、`WandD2277/Math-And-English-Library` 等衍生/相邻仓一并搜出，未核实血缘关系 |
| Editing Toolbar | [cumany/obsidian-editing-toolbar](https://github.com/cumany/obsidian-editing-toolbar)（社区页面显示版本4.1.4，另有前身/关联仓 `PKM-er/obsidian-editing-toolbar`，两者关系未核实） | 仿 MS Word 工具栏式编辑插件 | 帖子称"新手直接下载的7个OB插件"之一（该帖在原文中重复出现两次） |
| Apex Dashboard | [PandoraReads/apex-dashboard](https://github.com/PandoraReads/apex-dashboard)（另有 `EngineeringHu/apex-dashboard` 同名同描述仓，未核实二者关系） | 备忘卡/交互待办/项目卡的单页仪表盘 | 同上"7个插件"帖之一 |
| Calendar | [liamcain/obsidian-calendar-plugin](https://github.com/liamcain/obsidian-calendar-plugin) | 侧边栏日历，导航每日笔记 | 同上"7个插件"帖之一 |
| Custom Frames | [Ellpeck/ObsidianCustomFrames](https://github.com/Ellpeck/ObsidianCustomFrames) | 用 iframe 把网页/Web App 嵌入 Obsidian 面板，含 Google Keep/Todoist 等预设 | 同上"7个插件"帖之一；桌面端专属（Obsidian Mobile 非 Electron，多数站点无法用） |
| Excalidraw | [zsviczian/obsidian-excalidraw-plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin) | 手绘草图/示意图编辑与嵌入 | 同上"7个插件"帖之一；README 明确"个人业余项目非公司维护" |
| Xiaohongshu Importer | [bnchiang96/xiaohongshu-importer](https://github.com/bnchiang96/xiaohongshu-importer) | 把小红书分享链接内容（标题/正文/图片/视频/标签）导入 vault 并分类 | 同上"7个插件"帖之一 |

未核实项：以上全部只做"WebSearch 找到同名/同描述仓库"层级的身份核对，**star 数、下载量、"维护活跃"等表述均为厂商/社区自述**，未安装、未跑、未读源码、未验证与用户实际看到的帖子指向同一仓库（尤其 Research OS/obsidian_math/Claudian 存在多个同名或衍生仓，无法排除用户帖子指向的是其中另一个）。"Lazy-Kaoyan-Library" 在本轮按名称搜索**未找到**，直到 R14 用户自己给出确切链接才解决。

#### 7.8.2 R14：用户自选链接批（确切 URL，用户自行三分类）

用户原话"这些"+"还有这些"+"这是今天找的"，分三类贴出确切 GitHub 链接。以下按用户原始分类整理，只读 README 核对用途，未装、未 clone、未做选型建议：

**考研**（1项，与 R13 的 "Lazy-Kaoyan-Library" 缺口互补，同一项目，不重复计数）

| 项目 | 用途 |
|---|---|
| [RoxyRhHg/Lazy-Kaoyan-Library](https://github.com/RoxyRhHg/Lazy-Kaoyan-Library) | 面向"不想手搓重复劳动"考研人的 Obsidian vault：数学思维导图、英语作文模板、错题系统；强调用 AI 减少笔记/刷题重复劳动，把精力放在理解而非机械做题上 |

**工作台**（9项——vault 模板/任务管理/项目管理插件为主）

| 项目 | 用途 |
|---|---|
| [IvyChim/Obsidian-Template](https://github.com/IvyChim/Obsidian-Template) | 新手友好 vault 模板，PARA框架+Periodic Notes，含预配置仪表盘/阅读管理/模板/社区插件 |
| [groepl/Obsidian-Templates](https://github.com/groepl/Obsidian-Templates)（用户重复贴了两遍同一链接） | Zettelkasten 方法论模板集（fleeting/literature/permanent/project 四类笔记）+ 可选插件 |
| [tuan3w/obsidian-template](https://github.com/tuan3w/obsidian-template) | Zettelkasten 起步模板；维护者自述"AI agent 新方案可能比这套更好"（自我保留意见） |
| [SilentVoid13/Templater](https://github.com/SilentVoid13/Templater) | 模板语言插件，支持变量/JS函数/系统命令动态生成笔记；**5.3k star**，社区采用率高 |
| [masonlr/obsidian-starter-templates](https://github.com/masonlr/obsidian-starter-templates) | 收集社区 backlink/Markdown 技巧范例，含 Technology Radar／Researcher／Researcher-with-Plugins 三套模板；**1.0k star / 138 fork**，19次提交，无法判断近期维护频率 |
| [obsidianmd/obsidian-sample-plugin](https://github.com/obsidianmd/obsidian-sample-plugin) | Obsidian 官方插件开发脚手架（非终端用户工具，是开发者模板） |
| [WebBreacher/obsidian-osint-templates](https://github.com/WebBreacher/obsidian-osint-templates) | 面向 OSINT 调查场景的 Obsidian 用法模板，含示例数据/SOP |
| [xxone111/Time-Manager-for-Obsidian](https://github.com/xxone111/Time-Manager-for-Obsidian) | 番茄钟+每日时间记录+可视化时间回顾插件 |
| [programerni/obsidian-TaskNexus-free](https://github.com/programerni/obsidian-TaskNexus-free) | 交互式甘特图项目管理插件，支持拖拽排期/行内编辑/批量操作 |

**科研**（4项——含与 R13 重叠的 Research OS，已去重不重复计数）

| 项目 | 用途 |
|---|---|
| [t626644510/personal-research-os](https://github.com/t626644510/personal-research-os) | Obsidian+Git+Python 组合的个人"概念数据库"：稳定定义/关系/决策日志，离线悬浮预览查询；目标是确定性、可审计，不依赖 AI 查询/向量库/爬虫 |
| [TiesdeKok/LearnPythonforResearch](https://github.com/TiesdeKok/LearnPythonforResearch) | 面向社科实证研究（会计/金融/政治学）的 Python 教程：五个 notebook（基础/文件处理/Pandas/可视化/爬虫）+ 练习文件 |
| [kivvng726/obsidian-research-os](https://github.com/kivvng726/obsidian-research-os) | **与 R13 重复**——用户今天自己又贴了一遍同一仓库，说明这是用户确认过的目标仓库（不是 R13 阶段"同名仓中猜的那个"），身份置信度提升为 `URL-CONFIRMED-BY-USER` |
| [LAMDA-NeSy/Research-Starter-Kit](https://github.com/LAMDA-NeSy/Research-Starter-Kit) | 面向刚进组的本科/研究生新人及初带学生的导师的科研入门指南：找文献/读论文/想法/做报告/论文全流程（摘要到rebuttal） |

对两台的初步定位（**仅观察，非选型结论**）：工作台清单里的模板/插件解决的是"vault 怎么搭骨架、任务怎么排期可视化"，天然落在 §3 表格的"材料/对象组织层"或工作台的任务执行参照；科研清单里 `personal-research-os`／`LAMDA-NeSy` 更贴近"科研台的研究视角"（概念库、进组指南），`LearnPythonforResearch` 更像方法论工具而非底座候选。是否真正采纳、与已在试用的 NotEMD/LearnGraph 什么关系，本轮不判断。

### 7.9 R15：2026-09-18 机制层深查（26 项 URL，含考研对比组）

`TASK-20260918-004`。用户明确指示"看核心内容、工作流、核心运作机制、能用在哪一个台……不要拘泥在某一个角，不要钻牛角尖，我们是看具体是用来干什么的，怎么用的，我们能不能用得上"——本节因此**不预设槽位归类**，"能不能用得上"一栏原样保留子代理给出的具体场景，允许一项挂多个台、也允许"想不到具体用得上的地方"。分组标题按调研时的技术相似性分批（vault 模板／任务管理／仪表盘／嵌入绘图／科研 AI-agent），不代表最终归属判断。

执行方式：6 个只读子代理并行核对（`general-purpose`，本次不构成 Workflow 级编排），每个 prompt 顶部显式给出 **5 caps**——URL cap（仅限 github.com／raw.githubusercontent.com 且仅限指定 URL 自身页面）、word cap（≤1100 汉字）、time cap（≤12 分钟）、tool cap（仅只读，不下载/clone/装依赖/执行脚本/写本地文件）、done_when（每项必须产出身份坐标／核心内容与工作流／血缘或场景匹配／能不能用得上／边界五个字段，读不到就写"读不到"不许留空）。全部 6 批均在各自 time cap 内完整交付，无超时缺项、无"读不到"字段触发。深度停在 `REFERENCE_INTEGRATION_PLAN.md` §2.2 的"定位→机制"两档，不到"实现"（读源码）或"实测"（真跑）；不做该文档 §2.3 的五选一处置判断（借鉴／转化设计／隔离试用／正式接入／暂存不采用）；也不判断是否新增"考研台"这一架构槽位——这两层判断权留给用户。

26 个 URL 中 24 个已经在 R13／R14 登记过身份（本次是从"按名称核身份"升级到"读机制"），真正首次出现的只有 Pkmer-Math、Math-And-English-Library 两项（即 R15 新增部分）；已核对无遗漏、无重复计数。

#### 7.9.1 考研内容对比组（5 项，另见已独立深查的 kaoyan）

用户要求把 R13 的 obsidian_math、R14 的 Lazy-Kaoyan-Library、R15 新增的 Pkmer-Math／Math-And-English-Library，与已经深查过的 `virtualxiaoman/kaoyan`（`TASK-20260911-007`，固定版本 `3c6ca382b3bacbbc863fc00f16dac2064cbdd128`）放一起比较。kaoyan 一行引用既有审查结论，本轮未重新读取。

| 项目 | 内容定位 | 血缘痕迹 | 三段式工作流 | 版权来源声明 |
|---|---|---|---|---|
| [BlandAlpha/obsidian_math](https://github.com/BlandAlpha/obsidian_math) | 高等数学＋线性代数笔记库（张宇讲义笔记化），纯静态 Obsidian vault，支持 LaTeX／CallOut／知识图谱可视化 | 未见明显血缘声明；但自身已是 fork（README 未声明源头），且有 20+ 下游 fork | **没有**——纯静态笔记合集，无程序统计、无 AI 对话记录、无人工调整过程记录 | GPL-3.0 |
| [PKM-er/Pkmer-Math](https://github.com/PKM-er/Pkmer-Math) | 微积分、线代／概率论知识库，Obsidian 双链概念网络；603 commit／348 star，可在线访问 | 未见血缘声明；README 仅说"开发资源有限，内容缺漏和错误难免"，未提衍生关系 | **部分**——有双链标记和概念分类，但无程序统计脚本、无 AI 对话工具、无人工调整记录机制 | 未声明（GitHub API license 字段为 null） |
| [WandD2277/Math-And-English-Library](https://github.com/WandD2277/Math-And-English-Library) | 高等数学＋英语笔记库，纯静态＋Excalidraw／EasyTyping 插件配置；303 star／9 commit | README 无血缘声明；但下游某 fork 用户（Stefansky07）将其改名为"Stefansky-Kaoyan-Library" | **没有**——纯笔记集合，无程序统计、无 AI 应用、无人工评估记录 | MIT |
| [RoxyRhHg/Lazy-Kaoyan-Library](https://github.com/RoxyRhHg/Lazy-Kaoyan-Library) | 考研数一＋英一知识库，AI 辅助 Obsidian vault；83 star／12 commit，最近更新即当天（2026-09-18） | **明确声明**"灵感来源于 Math-And-English-Library 和 Pkmer-Math"；另感谢 Gemini 2.5 Pro 对本仓库的关键作用 | **有**——① AI+OCR 转录课程与题目（前期）② 思维导图＋AI 对话入口→章/知识点/方法/题型/题目层级组织＋Dataview 动态查询（中期）③ Templater 模版驱动笔记扩展（后期） | 未声明 |
| `virtualxiaoman/kaoyan`（引用 `TASK-20260911-007`，不重读） | 数三/英一/统计学/数据结构学习记录，Markdown 记录学习过程 | 独立项目，不在本批血缘脉络内 | **有，但实现路径不同**——人工判断和调整＋Python 脚本生成离线统计＋外部 AI 对话提供讲解和批改（12 份 Python 已审查，无自动教学/学习者模型/间隔复测/自动改计划实现） | 未发现 LICENSE 文件 |

**值得点出的发现**：obsidian_math 和 Math-And-English-Library 本身都是"纯静态笔记，没有任何工作流"，Lazy-Kaoyan-Library 声明的"灵感来源"只覆盖笔记内容/组织风格的继承，它那套"AI+OCR转录→Dataview/Templater自动化"的三段式工作流是自己另外加上去的，不是从两个"血缘对象"那里继承来的。这套工作流与已深查的 kaoyan 三段式（人工记录+Python统计+外部AI批改）目标相似（都想用 AI/程序化手段减少考研笔记的重复劳动）但实现路径完全不同、彼此独立（无任何一方声明借鉴对方），可视为同一问题的两种收敛解法。两者与 Pkmer-Math、Math-And-English-Library、obsidian_math 相比，共同点是后三者都停在"纯内容/笔记仓"层级，没有工作流可言。

#### 7.9.2 vault 模板／脚手架类（5 项）

| 项目 | 身份坐标 | 核心机制 | 能不能用得上（具体场景） |
|---|---|---|---|
| [IvyChim/Obsidian-Template](https://github.com/IvyChim/Obsidian-Template) | 402★/42fork/19commit，GPL-3.0 | PARA＋周期笔记混合系统；下载 ZIP 后在 Obsidian 打开为 vault，安装 15 个社区插件（核心 Dataview＋Templater）即用；产出 Home 仪表板＋周期笔记＋项目/领域/资源/存档分类 | 学习台/科研台初始架构骨架搭建——用 PARA 快速建立分类结构，周期笔记+Dataview 关联追踪进度 |
| [groepl/Obsidian-Templates](https://github.com/groepl/Obsidian-Templates) | 1900★/171fork/570commit，CC BY-SA 4.0，高活跃 | Zettelkasten 五层模板实装：碎片笔记→文献笔记→永久笔记→项目笔记→结构笔记，每层预设模板片段；5 个必需插件+9 个可选插件 | 学习台"补学回溯"机制——文献笔记→永久笔记转化模板可直接用于研究问题驱动的学习流程；科研台知识网络建设（永久笔记实装多层依赖） |
| [tuan3w/obsidian-template](https://github.com/tuan3w/obsidian-template) | 1100★/150fork/36commit，MIT；**项目方已标注不再活跃维护** | Zettelkasten 模板+20 余插件（Spaced Repetition／Anki 卡生成／Kanban 阅读追踪／LLM 总结模板／自动标签分类脚本） | 学习台"掌握分级"——Anki 间隔重复可直接对接最低/正常/长期掌握要求分级需求；但维护停止意味着插件兼容性风险 |
| [masonlr/obsidian-starter-templates](https://github.com/masonlr/obsidian-starter-templates) | 1000+★/138fork/19commit，CC0-1.0 | 三套独立模板：Technology Radar（YAML+状态字段追踪工具评估阶段）／Researcher（scratch/concepts/projects/people/books/tools/meta 七目录，标签驱动 #next/#backlog/#priority）／Researcher+插件版 | 工作台分布式任务标签（减轻看板 UI 维护负担）；考研台用 Technology Radar 框架追踪学习资源评估阶段（如"目标院校简章=hold，备选参考书=trial"） |
| [obsidianmd/obsidian-sample-plugin](https://github.com/obsidianmd/obsidian-sample-plugin) | 4500★/1800fork/102commit，0BSD，官方维护 | 插件开发脚手架（非 vault 模板）；TypeScript+esbuild+ESLint+GitHub Actions，`npm i`+`npm run dev` 热重载调试 | 非现成工具；若需定制插件填补"PDF 精确原段回跳"等已知缺口，可用此脚手架起步，但需要开发投入 |

#### 7.9.3 任务／时间管理插件类（4 项）

| 项目 | 身份坐标 | 核心机制 | 能不能用得上（具体场景） |
|---|---|---|---|
| [SilentVoid13/Templater](https://github.com/SilentVoid13/Templater) | 5286★/332fork | 动态模板语言：模板中声明变量+JS 函数，创建笔记时选模板触发渲染，支持任意 JS 和系统命令执行 | 学习台/科研台复盘记录自动填日期、统计字段、计算学习时长；工作台任务模板插入优先级公式/期限计算——不直接解决"跨层依据复核" |
| [xxone111/Time-Manager-for-Obsidian](https://github.com/xxone111/Time-Manager-for-Obsidian) | 8★/0fork | 番茄钟+时间记录+dashboard：ribbon/命令板启动计时器，完成后写入 daily note（幂等不重复），dashboard 按日期显示焦点时长+分类分布 | 考研台学习时长追踪；工作台任务执行焦点时长记录；不覆盖"研究问题→补学→返回"嵌套路由 |
| [programerni/obsidian-TaskNexus-free](https://github.com/programerni/obsidian-TaskNexus-free) | 0★/0fork；free/pro 分离 | 交互式甘特图：5 种缩放级别，拖拽调整日期/工期，关键词+下拉筛选，wiki-link 建层级；free 版限≤100 任务/≤200 文件扫描，pro 版含 AI 分解 | 工作台任务可视化调度——甘特图+拖拽+状态筛选直接满足看板需求；科研台实验任务链时间规划；不支持复杂依赖但 wiki-link 可用于简单父子链 |
| [WebBreacher/obsidian-osint-templates](https://github.com/WebBreacher/obsidian-osint-templates) | 810★/134fork，CC-BY-SA 4.0，创建于 2022 年 | OSINT 调查取证模板：用 wikilink/backlink/graph view 记录案例间关联，按模板结构填充笔记 | 科研台多层知识网跨层依据映射——人物/事件关联图范式可迁移到学术概念/引文/假设的有向关联；不提供"原段回跳"机制 |

#### 7.9.4 仪表盘／时间线插件类（4 项）

| 项目 | 身份坐标 | 核心机制 | 能不能用得上（具体场景） |
|---|---|---|---|
| [cenyuhing11-png/Xove-Dashboard-Custom](https://github.com/cenyuhing11-png/Xove-Dashboard-Custom) | 0★/0fork，最近更新 2026-08-31；为 TanYinaia/Xove-Dashboard 衍生版 | 四象限任务分类+Gantt/日历/列表/看板四视图+灵感板 kanban（收集→评估→进行中→归档）；纯 Markdown+YAML 本地存储，零外部依赖 | 工作台任务优先级管理与甘特图可视化；灵感板评估流程可参考学习台资源分类机制——但都不含跨层依据追溯 |
| [mark-when/obsidian-plugin](https://github.com/mark-when/obsidian-plugin) | 442★/20fork，最近更新 2026-05-14 | Markwhen 语法时间线：笔记内写 Markwhen 格式文本，解析为交互式时间线 | 科研台研究问题时间线可视化（论文发布序列、实验阶段规划）；缺少与论文/资源的双向追溯 |
| [cumany/obsidian-editing-toolbar](https://github.com/cumany/obsidian-editing-toolbar) | 1.5k★/86fork，最近更新 2026-09-14（活跃），152 个开放议题 | MS-Word 风格工具栏：字体/背景色/对齐/标题级数/格式刷等按钮化操作；可选 LLM 端点/PKMer 同步不上传仓库内容 | 直接降低学习台笔记编辑门槛（减少 Markdown 语法记忆负担）；与科研/工作台无直接关联 |
| [PandoraReads/apex-dashboard](https://github.com/PandoraReads/apex-dashboard) | 772★/45fork，最近更新 2026-09-13（活跃） | 整合备忘录/待办/项目/笔记/日历/dataview 查询/web 嵌入；11 种侧栏小件（番茄钟/阅读追踪/记账等）；习惯/番茄/阅读/记账数据存独立 JSON 可跨设备合并，零云依赖 | 工作台任务/项目/日历可视化+跨工具同步；与科研/学习台的知识网图、原段回跳、层级复核无直接关联 |

#### 7.9.5 嵌入／导入／绘图插件类（4 项）

| 项目 | 身份坐标 | 核心机制 | 能不能用得上（具体场景） |
|---|---|---|---|
| [liamcain/obsidian-calendar-plugin](https://github.com/liamcain/obsidian-calendar-plugin) | 2.3k★/259fork，**最近更新 2022 年 11 月，维护陷停** | 侧边栏日历导航每日笔记；每 250 字显示一点可视化写作量；仅桌面端 | 工作台日程导航；学习台学习进度可视化（点阵可改造为课程完成度指示器） |
| [Ellpeck/ObsidianCustomFrames](https://github.com/Ellpeck/ObsidianCustomFrames) | 845★/48fork，最近更新 2026-08-09（v2.6.0） | iframe 网页嵌入：预设 Google 日历/Todoist/Notion 或自定义 URL，支持 CSS 样式注入；移动端功能受限 | 工作台外部工具集成（Todoist/日历嵌入看板）；科研台在线文献库访问窗口；考研台答题系统原地嵌入 |
| [zsviczian/obsidian-excalidraw-plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin) | 7.6k★/504fork，最近更新 2026-09-17，3264 commit（高度活跃） | 手绘工具：形状/文本/LaTeX 公式，自动导出 PNG/SVG，支持 OCR；ExcalidrawAutomate 脚本 API 可联动 QuickAdd/Dataview；桌面+移动支持 | 科研台概念关系图绘制；学习台笔记插图与公式推导标注；脚本 API 可驱动三台跨层可视化依据的自动生成 |
| [bnchiang96/xiaohongshu-importer](https://github.com/bnchiang96/xiaohongshu-importer) | 134★/27fork，最近更新 2026-01-14（v1.1.3） | 小红书分享链接→标题/正文/图片/视频/标签结构化导入，支持本地媒体下载或 URL 嵌入 | 考研台经验笔记批量导入；学习台社媒学习资源采集；不适用科研/工作台（专用小红书平台） |

#### 7.9.6 科研／AI-agent 类（5 项）

| 项目 | 身份坐标 | 核心机制 | 能不能用得上（具体场景） |
|---|---|---|---|
| [kivvng726/obsidian-research-os](https://github.com/kivvng726/obsidian-research-os) | 12★/0fork，v0.4.4（pre-release） | PDF 导入+AI 自动填充题目/作者/摘要→按研究主题语义聚类→选 2-12 篇生成综合结论+十题式总结→arXiv 检索+论文关联网络；多 AI 服务商可选（DeepSeek/OpenAI/Claude/Kimi/OpenRouter/SiliconFlow），不配置 AI 时基础功能（阅读队列/笔记）仍可用 | 多层知识网跨层依据复核（部分，论文关联图可视化影响关系）；研究问题→补学→返回（按主题综合分析可用于复杂嵌套往返）；原段回跳暂无明确精确定位机制 |
| [t626644510/personal-research-os](https://github.com/t626644510/personal-research-os) | 0★/0fork | Concept 库+Inbox 工作流：资料→人工判断→创建/更新 Concept 草稿（YAML 固定标识+关系）→validate schema→scan 索引→人工审阅 git diff→commit→Obsidian 刷新；完全本地 Python 3.9+ 标库，无 AI 无网络 | 多层知识网跨层依据复核（YAML 结构化关系原生支持，schema 强制区块规范依据记录）；同一知识不同目标分级掌握（Concept 固定字段编码）；原尝试/AI 辅助留痕（git commit boundary 区分人工 vs 自动） |
| [TiesdeKok/LearnPythonforResearch](https://github.com/TiesdeKok/LearnPythonforResearch) | 269★/88fork，**最后更新 2020 年 6 月（已过时 5 年+）**，MIT | 5 套 Jupyter 教学 Notebook（基础/文件 I/O/Pandas/可视化/爬虫）+ 练习文件；Binder 在线运行或本地 Anaconda | 难以明确对应具体缺口；若考研台需要 Python 教材块可借鉴其 notebook 结构化教学模式，但内容本身已过时 |
| [LAMDA-NeSy/Research-Starter-Kit](https://github.com/LAMDA-NeSy/Research-Starter-Kit) | 873★/32fork，南大教授郭蓝哲编写 | 纯文字研究入门指南：找文献/读论文/想 idea/学术展示/会议/写作全流程（摘要到 rebuttal）；资源托管 Feishu+GitHub | 不直接对应具体功能；若考研台需要科研流程规范指南可参考其组织结构 |
| [YishenTu/claudian](https://github.com/YishenTu/claudian) | 15.4k★/1.0k fork/962 commit，MIT，仅限桌面 | 将 Claude Code/Codex/Grok/Opencode/Pi 等 AI coding agent 嵌入 Obsidian vault：内联编辑+字级 diff 预览、@mention 引用文件、MCP server 扩展、多标签会话；**必须联网**，数据发送至所选 AI 提供商，LAN 模式存宿主机／Cloud 模式存自托管服务器 | AI 辅助留痕（多标签会话可记录多轮对话，但需明确与"工作台人工决策门"的交互设计，其权限模型默认 agent 对 vault 有完全读写权）；隐私流向需评估涉密项目是否可接受（数据必然离开本机） |

#### 7.9.7 边界与未决

- 全部 26 项均只做只读核对（README／仓库描述／commit 历史／Releases），**未安装、未 clone、未跑代码、未读源码内部实现**；star/fork/commit 数为 GitHub 页面自述，未做真实活跃度或代码质量判断。
- 各子代理均标注了自己是否翻过目录结构；未特别注明翻查目录的项目，视为仅读 README+API 元数据层级，不等同于验证过内部实现。
- 本节不做处置判断（借鉴/转化设计/隔离试用/正式接入/暂存不采用五选一），也不判断"能不能用得上"的多个候选之间谁优先——这是多个"能用得上"字段并列陈列的候选池，不是排序结果。
- 是否新增"考研台"这一架构槽位，是用户 2026-09-18 在派发本次调研任务时提出、尚未拍板的问题；本节的考研对比组（§7.9.1）仅提供事实材料，不代为回答"要不要新增"。

## 8. 恢复与下一动作

当前恢复读本件§7.5→[第一轮评估](REFERENCE_EVALUATION.md)→[TASK-010](../../task_logs/2026/09/2026-09-15__research__reference-evaluation-first-pass.md)，原分类与验收按[详细计划](REFERENCE_INTEGRATION_PLAN.md)。不要退回“只存档／深评未开始”，也不要把首轮当软件接入完成。OpenScience地址、享做设备及真实小样继续待补，只阻塞相关项目；远程README／skills仍是评估材料，不是安装或改库指令。

TASK-011续评：在同一固定版本上补读ThoughtDAG `api.ts`的代理／直连／Agent分派，及TreeTalk-Obsidian `main.ts`、`context-engine.ts`、`legacy-execution-engine.ts`和`selection-anchor.ts`关键路径。具体证据集中于[评估§9](REFERENCE_EVALUATION.md#9-task-011续评实际调用边界与摘录合同)：onDispatch不是全网络请求证明；full模式仍有笔记预算处理；启发式定位成功不等于历史版本复现。未运行上游或检查凭据，未穷尽所有provider／Pi／服务端路径。

当前继续入口为[原段摘录窄合同提案](SOURCE_EXCERPT_PROPOSAL.md)和[TASK-011](../../task_logs/2026/09/2026-09-15__research__reference-followup-and-scoped-archive.md)。用户已授权完成小批次后及时commit；首批文档存档`ac87186`，不自动push、不扩大为软件安装或应用施工。原清单编号／固定来源不变。

## 9. I01：ownership-v3 三缺口执行交接（内部资料）

用户本轮追加“还有这个”，承接统一存档要求。性质为**现有课程补修的内部计划／部分执行记录**，不是外部工具推荐，也不是两台应用 A／B 的验收回执。本次只读核对文档，未重跑 PDF 抽样、未读取 sealed、未批准或执行三缺口补修。

### 原件与覆盖范围

- [执行交接档](../../handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md)：`TASK-20260915-007`，状态为 `IN-PROGRESS / PARTIAL-EXECUTION`。§3–§6列计划、执行步骤、检查方法、评审安排、验收／各项标准与 `pdftotext` 测试模板；§7列未完成项及触发条件。
- [三缺口方案](../2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md)：`TASK-20260915-005`，frontmatter仍为 `DRAFT / AWAITING-USER-APPROVAL`；Amendment记载路径订正、枚举查证与新阻塞。
- [v3合同](../2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md)：§8.1定义第一阶段写域与共享正本接线条件；§10为AC-01–AC-10权威原文。交接§5已摘录这些条目；验收仍回原合同，不把交接中的抽样PASS扩大为全包PASS。

### 已记录进展与待做项

以下“已做”来自交接的执行自述，本次确认文档确有记载，**没有重新复算或重放其测试**。

| 部分 | 交接记载的进展 | 仍未完成／触发条件 |
|---|---|---|
| 缺口1：独立QA | B-S3B三处论文坐标抽样均通过；B-EVAL部分公式／表格坐标、CrossEdgeIM部分结构／作者边界已核 | B-EVAL六任务及CrossEdgeIM P0–P3内容可执行性未核完；AC-04/05/08等未核；正式`CONTROLLER_ACCEPTANCE.md`尚待产出，独立性安排仍需核清 |
| 缺口2：研究问题出口 | 枚举为`DROP/PARK/PROMOTE`；桥接目标路径已从Sol写域移到`learning/training/lu-edgeim-algo1/TRANSFER_CARD_BRIDGE.md` | 桥接正文未写；交接§7列用户批准方案A后撰写并交叉核对。枚举已查明不等于执行已获批；不代填用户判断 |
| 缺口3：跨论文连接点 | 方案记录CrossEdgeIM→EdgeIM的具体来源锚点；发现`TASK-20260906-004`状态冲突 | 原交接列状态处理／授权确认及后续正本写入未完成。本轮不裁定、不修改该任务或Sol写域 |
| 原方案自身修正 | 独立QA回执目标改为`progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`；桥接文件移出`ownership-v3/`；枚举待查项解除 | 目标路径是预定产出，不据“已订正路径”认定文件已建好或内容通过 |
| 整体改进优化 | 交接§8明确其实际工作仅覆盖三个已知缺口 | 更广的课程优化范围尚未落为本件完整方案；不能把这三个缺口当成两台／多层知识网／整体教学重构的全部覆盖 |

### 本次归档核对发现与恢复提醒

1. 状态冲突当前确实存在：[TASK-20260906-004日志](../../task_logs/2026/09/2026-09-06__research__edgeim-plan-rewrite-draft-and-input-review.md) frontmatter与当前状态段为`in_progress`，并说明旧索引回执已过时；共享INDEX该行仍是`completed_with_open_gates`。v3合同§8.1也明确要求先解决状态和写域。本清单登记此差异，不代替原任务整合或授权裁定。
2. 原文件授权文字尚未完全一致：交接§4写“方案A已选定”，同时步骤表／§7写继续抽样或桥接需用户确认，方案frontmatter仍待批准。恢复施工须核原任务授权与实际写域；不能仅凭本次转发启动。原文保留，本次不替其他窗口改状态。
3. 交接§5对AC-07提出“预填consumer不等于真实消费／回写”，认为原自报PASS可能偏宽；作为**待正式审查的发现**保留，尚非本窗口独立裁定。单一commit或作者信息本身也不足以证明有无独立复审，应核审查者、过程与回执。
4. `pdftotext`坐标核对验证的是引用位置与对应文字，不自动证明完整IM／Petri net教学、数字复算、任务可执行性或真实学习效果。三处坐标通过不关闭整模块、全包或用户能力验收；原交接也明确正式验收尚未完成。

后续若获准继续课程补修，先从上述交接§7恢复具体剩余动作；若继续两台应用施工，只把I01用作内容与流程对账输入，不把课程补修、参考工具采用和应用功能混成一个完成状态。
