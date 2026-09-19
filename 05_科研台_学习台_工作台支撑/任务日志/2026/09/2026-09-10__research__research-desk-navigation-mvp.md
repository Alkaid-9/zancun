---
id: TASK-20260910-001
title: 科研台导航首版 N0-N5 实施与验收
date: 2026-09-10
runtime:
  model: GPT-6 Codex
  effort: n/a
  effort_source: 当前平台会话未暴露独立 effort 档位
  launch: Codex API workspace session
type: research
status: completed_with_open_gates
area: research-desk
project: none
todo_ids: [RD-1]
owners:
  - user
  - codex-session-01a08005-01ad-7921-b696-1cd455f6434b
related:
  - progress/decisions/2026-09-10__research__SOL_START_HERE.md
  - progress/decisions/2026-09-10__research__research-desk-navigation-sol-execution-plan.md
---

# 目标

按用户确认的 B/A/B/B/C 取舍实施独立科研台导航首版：固定 Markdown 入口、结构化资产登记、本地搜索筛选页面、工作簿覆盖、指导库双入口，并完成 N0-N5 与 A1-A12 验收。

# 最终结果

独立科研台导航首版已在 `/mnt/d/MyResearch/research-desk/` 完成。当前提供固定 `科研台_CURRENT.md`、结构化资产/版本/覆盖/继续/指导/提案记录、本地搜索筛选网页、Excel 18 表与原图导出、指导库来源/场景双入口，以及 README、维护、验收和交接文档。

终态为 `completed_with_open_gates`：N0-N5 的导航首版技术工作完成；用户使用验收和独立浏览器全点击复核仍开放。完整 Graph/Canvas、工作台执行闭环、独立 Git 仓、服务器和 TaskQuay 属后续任务。

# 修改内容

- 新建 `/mnt/d/MyResearch/research-desk/`，按 app/content/runtime/logs/acceptance 分离职责。
- 标准库 Python 实现扫描、XLSX ZIP/XML 提取、CURRENT 生成、链接检查、回环 HTTP 服务和受控原件读取。
- 普通 HTML/CSS/JS 实现首页继续优先、板块筛选、全局搜索、详情、科研指导双入口、工作簿图片和规划中画布。
- 登记 24 个声明范围、2432 条资产；最终 2432 available / 0 missing / 0 scan failure。
- 导出工作簿 18 张可见表、27 个媒体实体、29 次 placement，unsupported drawing=0；Sheet2-6 与五讲义 5/5 对账。
- 将 Map、论文、学习、pengsida/research_growth、Luo、Supervisor-Skills、CCF、讨论稿、实验入口和 LearnGraph 纳入可追溯导航。
- 修复 6 个真实 Map 策展子目录被陈旧记录误标 `missing` 的问题；增加策展目录可用性和陈旧状态恢复测试。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 环境预检 | `solver` 环境与显式解释器通过 | PASS | `require_solver_env.sh`；Python 3.10.19 |
| A1-A10 | 执行方案 §8 | PASS | `/mnt/d/MyResearch/research-desk/ACCEPTANCE.md`；5 tests PASS；check-links 0 error/0 warning |
| A11 浏览器 | 桌面/手机实际导航与截图 | PASS（实现者） | Edge 152，`acceptance/browser-check.json` 20/20；两张截图无横向溢出、图片非空 |
| N4 独立复核 | 来源、状态与界面抽查 | PARTIAL-PASS | 只读代理独立通过 HTTP/catalog/代码/截图核验；CDP 中途一次连接拒绝，未完成全点击复跑 |
| A12 接手 | CURRENT、启动、清单、回退、维护和模型回执 | PASS | `README.md`、`MAINTENANCE.md`、`ACCEPTANCE.md`、`HANDOFF.md` |
| A9 原件 | Excel、五讲义、Map 与受保护内容不被本轮修改 | PASS（本轮范围） | 扫描基线后 Map 307、受保护/答案 34、讲义 5、Excel 1 均 0 mismatch；Excel SHA-256=`d28ce510...f52f34` |

# 当前状态

N0-N5 导航首版完成。本地服务运行在 `http://127.0.0.1:8765`，只监听回环地址。软件主流程不依赖新增第三方包；浏览器验收使用本机已有 Playwright/Edge CDP。

资产状态只表示声明范围内的发现、读取、抽取、适配和使用情况；当前 read=51、extracted=1605、adapted=5、used=0，不能宣称知识库内容全部读完或指导条目已经实际采用。

# 尚未完成

- 用户实际使用验收，以及由不同执行者完成的整套浏览器点击复跑。
- 科研台独立私有 Git 仓的收录边界、初始化、commit 和 push。
- 完整 Track/Mycelium/Collaboration Graph/Canvas 与飞书/Miro 样本验证。
- 工作台执行请求、CLI/Agent 回执、TaskQuay、服务器和账号接入。
- pengsida/Luo/CCF/Supervisor-Skills 剩余条目的逐项适配与真实使用回执。
- EdgeIM 真实学习游标、CrossEdgeIM 图像证据、论文 MANIFEST 四项缺口等内容侧开放项。

# 下一步

1. 用户打开 `http://127.0.0.1:8765`，实际找一次 EdgeIM 停点、一个 pengsida 指导条目和一张工作簿图片，按具体对象反馈找不到/过时/归类问题。
2. 由独立窗口补一次完整浏览器点击复核；已有实现者 20/20 结果不冒充独立验收。
3. 单独拍板科研台私有仓内容边界，再初始化 Git；不要把本机配置、日志、运行态或私人原件提交。

# 可拓展方向

- 完整 Graph/Canvas、工作台回链、服务器部署和 TaskQuay 均属后续独立任务。

# 风险与回滚

- 外层仓库存在与本任务无关的既有修改；本任务不触碰。新应用可按本任务文件清单定向撤回，原资料不移动、不删除。
- `research-desk/` 当前被外层 `/mnt/d/MyResearch/.gitignore` 忽略且不是独立仓；落盘不等于提交或远端持久化。
- 回退前保留 `content/registry/curation.json` 与 `content/records/`；runtime/logs/acceptance 可重建。

# 文件和产物

- `/mnt/d/MyResearch/research-desk/README.md`
- `/mnt/d/MyResearch/research-desk/MAINTENANCE.md`
- `/mnt/d/MyResearch/research-desk/ACCEPTANCE.md`
- `/mnt/d/MyResearch/research-desk/HANDOFF.md`
- `/mnt/d/MyResearch/research-desk/app/`
- `/mnt/d/MyResearch/research-desk/content/`
- `/mnt/d/MyResearch/research-desk/acceptance/`

## Amendment

- 同窗实时状态补充：本窗口开始收口时MAS HEAD为`b76ccaf`；03:55:58 -0700另一进程提交`3e36af1 docs: record three-desk P1 delivery`，范围仅`three-desks-v0.1/`内五份规划和P1 RECEIPT/USAGE/CONTROLLER_ACCEPTANCE共八份文档，未含应用代码、共享登记或本轮应用侧验收配置。本窗口未创建或回退该提交；当前“commit开放”特指仍被外层忽略且无独立仓的`research-desk`应用版本采收，不能再写成所有P1文档均未提交。push仍未核到已发生。

- 2026-09-11（P1实施交付后的主控收口与用户验收准备）：核对Sol最终[RECEIPT](../../../decisions/three-desks-v0.1/sol-delivery/p1-20260910-sol/RECEIPT.md)、[CONTROLLER_ACCEPTANCE](../../../decisions/three-desks-v0.1/sol-delivery/p1-20260910-sol/CONTROLLER_ACCEPTANCE.md)、应用EVIDENCE与USAGE。记录结果为P1 120/120、Legacy 25/25、后端17/17，主控复跑同样通过；原配置、工作簿、registry和真实SQLite未改，验收服务已停，用户实际使用门仍开。将三台README、NEXT_STEP、旧Sol入口、MAS及应用交接/验收改为当前事实；新增`acceptance/p1-20260910-sol/user-acceptance/config.user-acceptance.json`，只引用原资料、写全新用户验收SQLite，监听127.0.0.1:8883。当前不进入P2/P3/B2/3D，不commit/push/deploy；用户验收后再决定问题修复或版本采收。

- P1实施包文档收尾实测：5份文档的25个本地链接存在、代码围栏闭合、A01–A16齐全，DOC_CHECK errors=0；定向diff检查按既有CRLF行尾解释通过（默认检查把INDEX的CR报行尾空白，未因此归一化共享文件）。TODO、task/handoff INDEX定向CAS写入后再次确认未漂移；generate.py成功，派生dashboard已有新入口。生成器仍报告与本续段无关的旧任务标记、TASK-20260821-001重复号及bplus陈旧告警，本轮不清理这些历史问题。以上是文档/登记检查，不是产品验收。

- 2026-09-11 UTC / 09-10 America/Los_Angeles（评审并入与P1交Sol准备）：用户授权“做，然后我拿去给sol执行”。修订[三台规划](../../../decisions/three-desks-v0.1/README.md)及WORKBENCH/LEARNING/NEXT_STEP，交[SOL_P1_EXECUTION](../../../decisions/three-desks-v0.1/SOL_P1_EXECUTION.md)。HOME合并但保留协调权威；同活动可有学习与研究产出；普通阅读/草稿不经调度；不强行统一评价schema。定点核源码确认工作区列表/历史HTTP/原子成员保存/工作簿原段/下载缺口，固定现有网页、隔离数据、写域、A01–A16及回执；source回归为Sheet1!R6与Sheet18!A14:A43（sheet12.xml）。恢复检查wrong_repo已通过MAS独立仓及应用外层位置实查、重开权威规划解决；应用仍被外层Git忽略。solver门禁通过，产品测试未重跑（17项是B1a历史回执），未启动服务/Sol、未改应用/原件/配置，无安装/迁移/部署/commit/push。文档收尾核相对链接、必需条款与入口状态；源台账定向CAS更新后生成派生页。应用验收尚待Sol执行，文档完成不升级产品状态。回退仅本续段文档和对应登记，保留他窗备注；后续独立复核释放执行位后顺序安排，P2/3D不自动启动。

- 2026-09-11 UTC / 09-10 America/Los_Angeles（三台规划完成，用户令停）：基于0911讨论及本会话对齐，交[三台方案四件](../../../decisions/three-desks-v0.1/README.md)：总览/现状/共享边界、工作台调度设想、学习台主要深入工作入口设想、P1后续执行合同。前段唯一只读位核WB-1/B1a/旧WP0，主控抽查比较表、B1a验收与ResearchService入口、旧WP0权威；17 tests为既有回执报告，本轮未重跑。明确新desk.sqlite3权威记录与旧WP0派生SQLite不可混同；旧“先WB-1/B1a未做”入口补新指针。按用户“规划完就停下来，不要推进”完成规划后暂停，不启动P1/新检索/应用改动；只补文档/路由/台账及派生页，无原件/配置/代码/commit/push。

- 2026-09-10（用户暂停与Sol执行交接）：按“先停一下？你把给sol的执行方案落盘”停止扩展，只写[Sol入口](../../../decisions/rd2-first-build-v0.2/SOL_START_HERE.md)：当前状态、最短阅读、WB-1两表最多6段的真实来源样例、独立文档写域、三件产物、验收/停止条件、后续代码选择与并发≤2。未派新任务、未启动Sol、未改应用或原件；交接状态改PAUSED/RECOVERABLE，共享登记同步当前入口。

- 2026-09-10（首批施工包v0.2与工作簿复核）：用户要求继续收敛设计并追问工作簿是否全部融合。写[施工包v0.2](../../../decisions/rd2-first-build-v0.2/README.md)：三页面、27项需求追踪、演示JSON、对象/API/存储选择、施工写域/验收/回执、参考核验、18表具体用途。唯一只读执行位串行核UA（raw/官网/demo均连接失败）、需求和workbook；主控抽查八层/七图及workbook关系表、18项资产记录、关键单元格，纠正显示表名与worksheet编号不能直接等同。既有29放置及5/5讲义对账仅沿用维护证据，不冒称新验；used:0为台账无使用回执，不证明用户未用。SQLite/桌面/3D为待审，应用/原件/学习作答未改，无新安装/部署/模型配置/commit/push。

- 2026-09-10（成本规则再明确）：用户要求“Astra尽量规划为主”，已修执行包§1与开发合同§9，实施不默认由Astra承担；交接当前状态改为设计已恢复，保留旧暂停历史并明确项目/外层/应用三个路径。共享登记收口只更新本任务指针，保留他窗备注；未启动新的子代理或代码实施。

- 2026-09-10（成本与并发分工）：用户明确总并发2（含主），将琐事交Sol/Luna或给完整执行指导；已核本线程仅主窗口活跃，既有子代理完成。写[五个自包含执行包](../../../decisions/2026-09-10__research__rd2-sol-luna-execution-packets.md)，含参考核验/适配差异/需求对账/低保真目标、输入、限制、文档写域、验收和统一回执。主控留架构/取舍/承重抽查；当前工具不能指定Sol/Luna，未改模型配置或起新代理。合同/交接/共享待办与索引同步路由；应用未施工。

- 2026-09-10（桌面与参考项目对齐）：用户纠正应考虑desktop日常入口及今晚参考；UA候选指定Egonex-AI/Understand-Anything。开发合同第13节记录NotEMD本地manifest、LearnGraph/graphify/TaskQuay只读代理静态审查及主控README抽查；UA/NotEMD GitHub/Cognitive网络读取均失败(No route to host/Network is unreachable)，不声称已核远端能力。产品形态仍待选择；轻网页为候选不当最终选型。没有安装/克隆/启动服务或改应用代码；待办路由接复用评估与低保真设计。

- 2026-09-10（开发合同草案）：用户请求全览/开发流程后继续问怎么开始开发，主控定向核research_desk.py GET接口、continue/proposals结构，写[首批开发合同v0.1](../../../decisions/2026-09-10__research__research-desk-first-development-contract-v0.1.md)：原需求去向、三尺度页面、记录/修订/关系提案、RD2-D/B1–B6工作包和V01–V12验收。沿用旧代码底座，应用改动未开始；合同schema/API/范围待审。另记录用户委派的只读代理自报完整读《一些讨论》1–10289行，主控已抽查树/小视窗/操作符及盘点；不把代理“约七成”估计当统计。交接/待办路由指向D低保真与样例下一步；无代码/原件/学习答案改动，无安装/服务启动/实验/commit/push。

- 2026-09-10（第二次落盘中新来源）：用户补贴09-01工作流优化碎碎念及Chain-of-Experience文章/评论，[原始接收档](../../../decisions/2026-09-10__research__workflow-notes-and-coe-source-intake.md)保存所贴文本，详档第21节记录自身工作流改进和过程保存/经验提炼/上下文装载分工提案。arXiv:2608.18027身份/数字/对照、Manus来源、“dspark”所指均待核；只接收存档，未新联网/拆论文/实验或改配置。RD-2补待办与来源链接。

- 2026-09-10（第二段设计讨论落盘）：用户确认先自由保存后整理、工业界独立并与学术联动，纠正companion为通用搜索方法范例，明确横纵脉络/类比/goal-item关联及草稿纸、失败、分歧、转向过程的重要性。按“先落盘？”把本段追加到[讨论详档第13–20节](../../../decisions/2026-09-10__research__map-learning-redesign-review-archive.md)，更新原暂停交接与research-desk/HANDOFF入口；RD-2补注，保留别窗备注。恢复先做视角/遗漏审查与完整功能联动，再定场景/验收/施工。存档不等于全设计采纳，无代码/原件变更、未运行研究或浏览器测试；文档回读和链接检查，登记面ledger_edit/CAS定向保形，generate.py刷新派生页，未commit/push。

- 2026-09-10（设计复核及存档续段）：用户质疑导航与原地图发展框架的差距，要求追溯原科研地图与人机恋搜索方案；两路只读代理检索、主控直接抽查原需求/四份任务书/维护边界/学习方案和app.js。形成[讨论详档](../../../decisions/2026-09-10__research__map-learning-redesign-review-archive.md)和[暂停交接](../../../handoff/2026-09-10__map-learning-redesign__pause-handoff.md)。用户“先存档？”授权本次收口；新方案均为待审，产品整改未施工。沿用他窗已有RD-2，只追加恢复指针；research-desk/HANDOFF.md补最新入口。原技术回执保留，独立浏览器全点击/用户产品验收仍开放；本续段不重跑资产/浏览器测试，不改代码/原件/学习证据，不安装/上传/部署/commit/push。共享登记面按ledger_edit.py/CAS保形更新，派生页按generate.py刷新；相关命令结果在本轮工具回执可追溯。

- 2026-09-10：开工登记。实际执行者是当前 GPT-6 Codex 会话；“Sol”仅为上游执行方案中的接手窗口称呼。
- 2026-09-10：N0-N5 技术收口。三路来源盘点中两路完成、Excel 子代理因 429 失败后由主控按结构化结果复核；另派只读代理做事后独立页面/数据抽查，结果 PARTIAL-PASS，限制已写入 ACCEPTANCE/HANDOFF。
