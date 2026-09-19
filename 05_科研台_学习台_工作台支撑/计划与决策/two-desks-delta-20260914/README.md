# 科研台与学习台：增量设计及首批施工方案

> 当前全局恢复入口（TASK-20260917-002）：[科研台、学习台、工作台与驾驶舱总交接](../../handoff/2026-09-17__research-desk-workbench-global__handoff.md)。科研台A/B与N3人工切片已提交，首次真实短试用为`USER-TRIAL-RED / SAVE-NOT-REQUESTED`；工作台WP0仍待异构审／接受／采收／加载；驾驶舱G0完成但P1a-P7未施工。先修8878保存主路径，不启动新壳或自动桥。

> 当前恢复入口（TASK-019）：[最新窗口总交接](../../handoff/2026-09-15__desks-window-current__handoff.md)。A/B、人工N3及新隔离试用准备已提交；用户试用、完整A/B独立审、WP0自动桥仍开放。下方按任务保留历史设计/实施口径，不作为今天的未提交声明。断电收口未采收的历史实体见新交接§6。

> 试用准备更新（TASK-20260915-017）：[两份DEMO的新隔离入口](/mnt/d/MyResearch/research-desk/acceptance/user-trial-TASK-20260915-017/README.md)已完成启动/读取/首页检查，未留常驻服务、未填用户证据。本轮A/B只读复审因429无有效结果，仍INDEPENDENT-REVIEW-OPEN；[任务记录](../../task_logs/2026/09/2026-09-15__implementation__desks-ab-review-and-user-trial.md)明确已做/未做，N4真实用户验收仍OPEN。

> 最新实施（TASK-20260915-013）：[本次任务与恢复入口](../../task_logs/2026/09/2026-09-15__implementation__desks-n2-closeout-and-workbench-link.md)。N2已新根复验并提交b54ea71；N3人工交接/身份返回/普通note保存已实现，专项20/20、后端28/28、B27/27、A38/38、C0322/22通过，三项独立静态发现修复闭环。见[N3回执](/mnt/d/MyResearch/research-desk/acceptance/n3-TASK-20260915-013/RECEIPT.md)。真实试用、A/B全包独立代码审及WP0自动接驳门仍开放；进组与课程归另一窗口。以下旧“未提交/未实施”均保留原时点，不作为当前停点。

> 2026-09-15 窗口存档（TASK-20260915-012）：先读[总交接](../../handoff/2026-09-15__lu-onboarding-and-desks-window__handoff.md)。进组新的补充计划、三台进度/线路/分工、下一批执行方案、架构/使用/维护手册已集中接线。最新用户要求先存档，本批不实施应用/课程/WP0；A/B仍待限定提交与真实试用，工作台接驳未完成。文档检查及本批commit以[TASK-012](../../task_logs/2026/09/2026-09-15__archive__lu-onboarding-and-desks-window.md)为准，旧状态保留当时时点。

日期：2026-09-14。任务：`TASK-20260914-002`。会话：`01a09aa5-24c1-7233-868b-7426b5d94476`。

状态：`DESIGN-DELIVERED / PROPOSED / IMPLEMENTATION-NOT-AUTHORIZED`。本包完成状态与检查结果见[任务记录](../../task_logs/2026/09/2026-09-14__research__two-desks-incremental-design-first-build.md)。

> 后续执行更新（2026-09-15）：上面的状态及下文授权说明记录本设计交付当时。用户后续分别批准“施工A”和“B启动”。A 已完成主线程技术验收，见[A 任务](../../task_logs/2026/09/2026-09-15__implementation__two-desks-a-source-save.md)与[A 回执](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/RECEIPT.md)。B1／B2 也已完成有界主线程技术验收，见[B 任务](../../task_logs/2026/09/2026-09-15__implementation__two-desks-b-goals-return.md)与[B 回执](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/RECEIPT.md)：B 浏览器27/27、后端28/28、A回归38/38、C03回归22/22。真实用户试用、C03 AC03-12 和独立复核仍开放；未部署或提交，不是多层网络／两台全包完成。恢复实施进度以两份任务及回执为准，不沿用下文设计时的未授权口径。

> 交付说明：5 份设计文档（含续作补齐的 B 接口提案）、九项旧稿对照、三条纸面路径与首批 A/B 范围已完成主线程自查；未运行应用验收。只读子代理因 429 未产出证据，独立设计复核未完成，不能标为独立复审通过。

## 0. 授权、状态与恢复

用户要求推进科研台和学习台，明确最高 2 并发，并在范围问题中选择：

> 先完成两台增量设计与首批施工方案（推荐）

当前授权只到设计、当前代码只读核对、方案落盘和范围内审查。没有选择“同时直接修复来源检索、保存反馈”；本包不能作为已经获准运行的 Sol 指令。实施前需用户批准首批范围及其合同差异，C03 的真实用户验收不由本包代签。

恢复顺序：本页 → [增量设计](DESIGN_DELTA.md) → [九项场景对照](SCENARIO_RECONCILIATION.md) → [首批施工方案](FIRST_BUILD_PLAN.md) → [B 接口提案](B_CONTRACT_PROPOSAL.md) → 本任务记录的实际检查与未完成项。不要按旧 handoff 的“未独立 Git”状态或旧系统功能三级表恢复。

本包承接[暂定知识内容版图](../2026-09-14__research__multilayer-content-map-provisional-baseline.md)，不覆盖其明确要求。科研 map 在上次存档时尚未展开；本包首次把它具体展开为设计提案，不能倒写成上次用户已接受的方案。

## 1. 本次交付

| 文件 | 解决什么 |
|---|---|
| [DESIGN_DELTA.md](DESIGN_DELTA.md) | 科研 map 的内容及各档要求、学习台的目标要求与个人证据、两台入口与三条使用路径、必要合同差异 |
| [SCENARIO_RECONCILIATION.md](SCENARIO_RECONCILIATION.md) | 补齐旧两稿九项行为对照，分开共同结论、覆盖缺口、真实取舍与本次建议 |
| [FIRST_BUILD_PLAN.md](FIRST_BUILD_PLAN.md) | 首批 A 体验修复＋B 两台往返切片的范围、前置、源码位置、验收、写域、交付及停止条件 |
| [B_CONTRACT_PROPOSAL.md](B_CONTRACT_PROPOSAL.md) | 目标／要求、个人反馈／研究判断、跨工作区归属、原视图返回及显式版本导出的推荐接口；待批准，不是实际实施差异 |

建议的首批终点不是“完整科研台／学习台上线”，而是用户能够走通：从一个研究问题进入必要知识，看到该知识对不同目标的要求，留下有帮助条件的尝试／反馈，回到原问题作独立的研究判断。

## 2. 当前底座：本次静态核对与历史回执分开

| 部分 | 当前依据 | 结论及边界 |
|---|---|---|
| 应用仓库 | `/mnt/d/MyResearch/research-desk`，`main`，HEAD `d53d188faff8e64ae9d22d92dd1eeab1b8309b84`；本次开工 status 干净 | 已独立 Git；不能再把旧“无独立版本”当当前事实。本轮不提交／推送，不改源码 |
| 规划仓库 | `/mnt/d/MyResearch/MAS_Safety_Project`，`master`，HEAD `f9f42db39be4286e6275ffbeb636ffae53e1f23e`；本地跟踪 ahead 14，未 fetch；共享树有既有改动 | 本包只写自己的设计、任务和索引，不采收其他窗口改动 |
| 共同工作区 | P1 与 C00–C03 历史主控回执：来源、草稿、Attempt／Feedback、版本冲突、挂起、导出、专题往返 | 这些是已有能力，不重新从空系统设计；本次未重新运行测试或确认旧端口在线 |
| C03 修复 1–3 | [返修任务](../../task_logs/2026/09/2026-09-11__research__rd2-c03-user-experience-repair.md) | 历史 `CONTROLLER-REPAIR-PASS / USER-RECHECK-OPEN`；AC03-12 仍开放，不能当用户已验收 |
| 来源选择 | [app.js](/mnt/d/MyResearch/research-desk/app/static/app.js:1041) 的 `renderP1Source` 仍用 `assets.slice(0, 300)` | 可选来源集合被截断，无该入口的检索；不是断言资产总数今天仍为 2432 |
| 首次保存 | [app.js](/mnt/d/MyResearch/research-desk/app/static/app.js:932) 的 capture `save` | 保存多个阶段已有部分成功后的恢复提示，但入口未见提交中锁定／明确成功态；本次为静态核对，未模拟重复点击 |
| 对象、关系与返回 | [research_service.py](/mnt/d/MyResearch/research-desk/app/research_service.py:14) | 已有 Object／Revision、七类关系与受限 return_context；任意 attrs 可保存不等于完整功能已支持 |
| 学习专有闭环 | [C06 原方案](../rd2-construction-v0.3/MANUAL.md:140)、[纠错本整合](../2026-09-12__learning__correction-notebooks-and-growth-v0.1.md) | 目标覆盖、要求深度、纠错与两类评价仍需具体界面和合同；不是已可运行的学习产品 |
| 多层科研 map | [三台原方案](../three-desks-v0.1/README.md:97)与两份场景稿 | 八类研究观察内容、七图、L0–L2 与 W1–W7 已有设计来源；完整语义融合、事件／使用与网页来源全链未交付 |

旧[三台 NEXT_STEP](../three-desks-v0.1/NEXT_STEP.md)及应用 HANDOFF 中的“未独立版本化”仅作历史。本次不批量改旧回执；后续施工以本页新核仓库状态为基线，其他旧功能验收边界继续有效。

## 3. 不再混在一起的四个层面

1. 知识本体：概念、定义、条件、机制与关系。
2. 目标要求：同一知识对考研、鲁侧训练等目标分别要求多深。
3. 研究认识：问题、假设、方法选择与依据如何变化。
4. 本人证据：在什么帮助、输入和时间条件下做到什么。

两台共同使用来源、内容和活动产物，但分别解释研究判断与个人能力。多层网络不是单层加筛选；共享对象身份也不要求共享所有断言的真假或评价。

考研范围为用户指定的数三、英一、统计学、数据结构；按 2027 年 12 月考试，专业课细目与“北大数院31822”仍待核。近期鲁侧、后续希望孙侧、毕业后工业／OAI 的阶段导向保留。经济学、近期小模型训练、猜测百分比、自动排期均不进入首批。

## 4. 本包完成与代码开工是两道门

本轮设计完成需具备：可追溯的需求对账、科研／学习内容结构、九项对照、三条纸面场景、首批功能及反例验收、源码位置与边界、未决项和恢复入口。

之后若要施工：用户明确批准 A／B 的范围；B 的目标要求、两类评价和返回上下文合同差异被确认；C03 使用反馈按首批方案处理。批准设计讨论不等于批准 C04–C07 全包、迁移真实数据、部署或联系导师。

总并发最多 2。主线程拥有设计与共享登记面；最多一个只读核验位，不改文件、不派生。应用、原始来源、用户答案、sealed、Ledger、Mistake Log、真实数据库与旧验收根保持只读。

## 5. 继续点

续作已补齐 B 的关键接口选择；现在可结合科研 map、两台路径和 B 接口提案，决定是否按 A → B 分段施工，不再扩一轮架构。未选具体科研题、未恢复数值权重、未获得真实试用材料的部分明确留空；不因此阻止本轮设计完成，也不由 AI 代填个人记录。

> 2026-09-15 后续参考更新（TASK-20260915-008）：上段保留设计时点，A／B实际进度见页首执行更新。用户三次输入已集中于[两台统一参考清单](REFERENCE_NOTES_20260915.md) §0，并加入[首批方案§9](FIRST_BUILD_PLAN.md#9-2026-09-15-后续施工参考备注)：PlanWeave／视频、工程与学习方法评论、两款身份待补的OpenScience、OrbitStart、ThoughtDAG、TreeTalkGPT、TreeTalk-Obsidian及享做。两款TreeTalk都保留参考价值，原库停止维护与错误发布警告另记。全部仅为参考，不是安装／运行授权或施工新前置；享做设备、同步、导出和备份待核，不改课程／多层网／真实库。

> 同日续补：统一清单新增内部资料I01（§9），链接ownership-v3三缺口执行交接与方案。当前共10项外部工具／方法参考＋1项内部施工交接，所有内容仍在同一清单；部分执行、授权文字差异、状态冲突与待审项分别记录，未启动课程补修。

> 当前后续设计入口（TASK-20260915-009）：[参考清单评估与融入两台：详细计划及划分标准](REFERENCE_INTEGRATION_PLAN.md)。用户授权先构造方案；11项分类、六阶段、检查／评审／验收／测试方案已写，原始参考仍由统一清单维护。方案交付不等于已启动深评、试点、安装或新施工，独立评审与真实试用不能由文档自查代替。

> 当前执行进度（TASK-20260915-010，取代上一段的未开始口径）：用户已明确“继续推进／直接做／做”，[第一轮评估结果](REFERENCE_EVALUATION.md)已落盘：A/B能力与旧课程遗留对账、11项处置、ThoughtDAG／两个TreeTalk同场景比较、PlanWeave／工程方法对照及最小提案。优先候选为带身份原段摘录与返回；保留现有版本、往返及选择导出，不照搬隐式来源写回。关键源码静态核对不是实测；独立复审／真实小样开放，未安装、改应用／课程或commit/push。恢复先读评估及[本任务](../../task_logs/2026/09/2026-09-15__research__reference-evaluation-first-pass.md)。

> 最新继续点（TASK-20260915-011）：用户授权及时commit，首批设计与参考文档已存档`ac87186`，其他窗口及应用A/B未采收。已补[发送与定位链的静态核验](REFERENCE_EVALUATION.md#9-task-011续评实际调用边界与摘录合同)，并交付[原段摘录窄合同](SOURCE_EXCERPT_PROPOSAL.md)：UTF-8文本整行区间、片段与原件版本分开、缓存不串段、显式来源返回、v2导出及EXR-01–10。代码／真实试用未执行。后续授权范围内的小批次及时提交，不自动push；恢复先读[TASK-011](../../task_logs/2026/09/2026-09-15__research__reference-followup-and-scoped-archive.md)，不要沿用旧“未commit”或“等再次写方案”的口径。

> 2026-09-16 产品壳参考与复核更新（TASK-20260916-008；原草稿号004作废）：用户提供“科研副导师 / AI Research Copilot”截图并要求与原参考清单一起形成详细计划、划分、检查、评审、验收和测试标准。截图以R11登记，保持`IDENTITY-OPEN / SCREENSHOT-ONLY`；[科研项目驾驶舱方案](RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md)规定八阶段只是科研台／学习台／工作台／Skills现有正本的派生导航，采用五门状态向量和G0-P7横向工作包，不建第四套正本。[主控复核对账](./_review/20260916_cockpit-review-controller-reconciliation.md)已把A-E意见校正为P1a静态验证、有效运行回执、实际B合同依赖、P5身份合同和分级评审语义。当前只交设计，G0、P1a／P1b、P2-P7、EXR、C04-C07、WP0接驳、外部安装与真实试用均未由此自动授权。
