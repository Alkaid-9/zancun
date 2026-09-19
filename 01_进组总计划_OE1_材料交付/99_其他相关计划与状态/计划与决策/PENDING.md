---
date: 2026-08-12
type: decision-inbox
status: active
---

# 待拍板决策

> checkbox 只表示“待拍板 / 已拍板”；结论须另落正式 decision 记录。来源优先指向原始审计、harvest、决策档或 TODO 条目。

## EvoAgent review 框架（审计 §5 四项）

- [x] **DEC-EA-REREVIEW · 是否砍掉 re-review 子代理环节** [line:evoagent] [source:progress/audits/2026/08/2026-08-11__audit__evoagent-review-state-and-framework-assessment.md#5]
  - **影响**：R6/R7 是由主控逐条核验 + 人工抽验，还是继续尝试派发 scoped re-review。
  - **来源**：EvoAgent review 状态与框架评估 §5.1；论证见同档 §4.3。
  - **结论（2026-08-12）**：砍掉 re-review 子代理；R6/R7 改主控逐条核验。正式决策档：`progress/decisions/2026-08-12__decision__evoagent-rereview-cut-and-guardrails.md`；SDD ledger 末行已记方法降级。

- [x] **DEC-EA-SEQUENCE · 先清学习线断点还是先固化框架护栏** [line:evoagent] [source:progress/audits/2026/08/2026-08-11__audit__evoagent-review-state-and-framework-assessment.md#5]
  - **影响**：下一步走 R6→R7→T8→T9，或先更新按需启用与防爆窗规则。
  - **来源**：EvoAgent review 状态与框架评估 §5.2。
  - **结论（2026-08-12）**：先固化护栏（runbook §5/§5.1/§7 已落盘）再清 R6/R7 断点。正式决策档同 DEC-EA-REREVIEW。

- [x] **DEC-EA-AUDIT-INTAKE · 是否登记 8-11 审计并转为正式 decision / intake handoff** [line:evoagent] [source:progress/audits/2026/08/2026-08-11__audit__evoagent-review-state-and-framework-assessment.md#5]
  - **影响**：该审计是否进入 task log 权威链，以及后续窗口从何处 intake。
  - **来源**：EvoAgent review 状态与框架评估 §5.3。
  - **结论（2026-08-12）**：已登记 `task_logs/INDEX.md` 行 `TASK-20260811-007`；intake 入口 = `progress/handoff/2026-08-12__evoagent__guardrails-codemap-w1-paused-handoff.md`。

- [x] **DEC-EA-STATE-AUTHORITY · 是否确认未登记审计不改变 TODO / ledger 状态** [line:evoagent] [source:progress/audits/2026/08/2026-08-11__audit__evoagent-review-state-and-framework-assessment.md#5]
  - **影响**：保持学习线断点以 SDD ledger 第 18 行为准、审计线以 8-10 handoff 为准。
  - **来源**：EvoAgent review 状态与框架评估 §5.4。
  - **结论（2026-08-12 · moot）**：随 DEC-EA-AUDIT-INTAKE 落地（审计已登记）前提消失；期间 TODO 修偏与 ledger 追加均出自已登记的决策/审计，状态权威未被未登记材料改动。

## MCM26 五轨审计（harvest §6 两项）

- [x] **DEC-MCM-AUDIT-HOME · 五轨审计产物落 MAS 仓还是独立审计新仓** [line:research] [source:D:/Code/mcm26-harvest-and-inventory-2026-08-11.md#6]
  - **影响**：单一权威源、跨仓死链与后续复审入口；harvest v2 推荐 MAS 仓 `progress/audits/2026/08/mcm26-five-track/`。
  - **来源**：`D:\Code\mcm26-harvest-and-inventory-2026-08-11.md` §6“未决”第 1 项。
  - **结论（2026-08-12 口头开工）**：落 MAS 仓 `progress/audits/2026/08/mcm26-five-track/`（正式 decision 档可由后续脚手架波次补写）。
  - → 正式档（2026-08-12 R1 补写）：`progress/decisions/2026-08-12__research__mcm-five-track-home-and-scope.md`

- [x] **DEC-MCM-AUDIT-SCOPE · 五轨审计全开还是先只跑 Step 0+1** [line:research] [source:D:/Code/mcm26-harvest-and-inventory-2026-08-11.md#6]
  - **影响**：本轮投入范围、何时进入 B→E→A→D→C 五轨执行。
  - **来源**：`D:\Code\mcm26-harvest-and-inventory-2026-08-11.md` §6“未决”第 2 项。
  - **结论（2026-08-12 口头开工）**：首期 Step 0+1 + Track B/E（不一次全开五轨）。
  - → 正式档（2026-08-12 R1 补写）：`progress/decisions/2026-08-12__research__mcm-five-track-home-and-scope.md`

## 可复用资产深挖（8-12 方案档 §6 三项）

- [x] **DEC-REUSE-TASKS · 三执行单元是否照方案立 TODO 任务** [line:research] [source:progress/decisions/2026-08-12__research__reuse-deepdive-review-learning-plan.md#6]
  - **结论（2026-08-12 晚拍板）**：升级执行——用户四项拍板（混合训练模式 / RA-27+16 全训练改造 / 每周 3-4 块 / 死线优先）后，以**深挖训练系统**（`learning/training/00_SYSTEM.md` + 4 训练包）落地，TODO research 线已立 `TR-1`；原方案的 Agent 拓扑降级为死线预案。

- [ ] **DEC-REUSE-ROLLOUT-E3 · EvoAgent rollout 若需 LLM key/联网是否放行** [line:research] [source:learning/training/ra26-evoagent-toy/BRIEF.md#0]
  - **影响**：训练包 ra26 EX-01 的运行验证路径（RUNTIME-CONFIRMED 升级）能否走；不放行则只做静态采证（训练照常开工）。
  - **来源**：原方案档 §1 E3 授权点；现载体为 ra26 训练包 BRIEF §0 待确认项。

- [x] **DEC-REUSE-OE1-TIMING · OE-1 弹药波现在跑还是贴 8-25 BR-1 复核点** [line:outreach] [source:progress/decisions/2026-08-12__research__reuse-deepdive-review-learning-plan.md#6]
  - **结论（2026-08-12 晚随四拍板落定）**：贴 8-25 之后——训练包 ra2716 排 W5（EX-03 素材包合成明确要求不早于 8-25，NSFC 放榜复核后素材最新鲜）；EX-01/02（盲写画像+对账）可提前做不受此限。

## Bridge 调研（8-12 四 Agent 调研 §5）

- [ ] **DEC-SUN-EARLY-CONTACT · 孙组套磁是否从 2027 提前到 2026 年 11-12 月** [line:research] [source:research/bridge_scan_2026-08-12/SYNTHESIS.md#5]
  - **影响**：是否带着 T1/T2 toy 在 2026 秋先建立弱联系（栾小坤毕业空位 + ICML/FSE 变现导致 2027 热度上升 vs 当前无成果贸然联系的风险）。
  - **来源**：`TASK-20260812-003`（B 报告"套磁宜早"判断 + SYNTHESIS §5 行动项 4）。
  - **2026-08-13 新证据（尚未替用户拍板）**：`research/deep_scan_2026-08-13/A4_sun_reconciled.md` 建议**不在 2026 秋正式套磁，2027 年 4-5 月带可验证产出再联系**；依据包括栾晓坤已赴 NUS、导师个人招生页强调研究证据、大陆硕士通道规则。具体招生规则是导师个人页单源，2028 报考前须按当年 PKU 正式目录/本人回复复核。

## 看板与 VPS

- [x] **DEC-DB-V31 · 看板 v3.1 改进批次做哪些（6 项候选打包拍板）** [line:infra] [source:progress/task_logs/2026/08/2026-08-12__maintenance__dashboard-v31-external-scan.md]
  - **影响**：是否投入实现 MCP 接口 / claim 认领 / 终端 board / kanban 列 / 子任务进度 / 周报生成；MCP + claim 两项直接决定多窗并发写 TODO 的冲突率。
  - **来源**：`TASK-20260812-005`（8-12 外部对标调研：kanban-md / cc-dash / kandown / Backlog.md）。
  - **结论（2026-08-12 晚 · 用户拍板）**：**全量 6 项，按套餐 A→B→C 顺序多 Agent 实施**（MCP+claim+小修 → 终端 board+周报 → 子任务+kanban 列）。接口契约 `progress/decisions/2026-08-12__maintenance__dashboard-v31-contracts.md`；分工按 v3.1 handoff §5.2。

- [x] **DEC-OE2-SITE-STACK · 个人学术主页选 al-folio（Jekyll）还是 HugoBlox academic-cv（Hugo）** [line:outreach] [source:progress/task_logs/2026/08/2026-08-12__maintenance__dashboard-v31-external-scan.md]
  - **影响**：OE-2 的起步模板与长期维护成本；al-folio = 学术圈事实标准（15.8k★ · Jekyll/Ruby），HugoBlox = 构建快 + BibTeX/DOI 自动导入（Hugo 单二进制）。
  - **来源**：`TASK-20260812-005` 主页选型扫描；两者均免费部署 GitHub Pages。
  - **结论（2026-08-13 晚 · 用户拍板）**：**al-folio**（深挖波需求对齐 q4 选项 d2 明选"al-folio 推荐并搭骨架"）。骨架搭建已派 Agent 执行（`TASK-20260813-018` B2 路，落 `/mnt/d/MyResearch/homepage/`）；OE-2 解除 blocked。

- [x] **DEC-TASKID-DEDUP · task_id 历史撞号治理选重排（A）还是保留消歧（B）** [line:infra] [source:progress/TODO.md#db-2]
  - **影响（2026-08-13 对账）**：当前未决仅 005×2、006×3；A = 一次性重排冲突行并同步全部引用档（需各窗歇工，破历史 task log 基本不可变惯例）；B = 历史保留，引用强制日期+标题消歧，新号继续统一走中央发号器。
  - **来源**：8-12 看板 `duplicate_log_id` 诊断 + 21:17 跨窗快照 §1；004 已自愈，不再列入当前冲突。
  - **结论（2026-08-15 随 DEC-DB-V40 追认）**：**方案 B+（legacy 精确抑制）**已于 v4.0 冲刺实施（R3 接线：`legacy_collisions.json`，warning 3→0，新撞号仍告警）；正式决议档 `decisions/2026-08-14__maintenance__dashboard-v40-refactor.md` §3（commit `820ecdb`，v3.13.28）。

- [ ] **DEC-S2-DASHBOARD-VPS · 选择看板 VPS 机器、部署版本、同步方式与访问控制** [line:infra] [source:progress/decisions/2026-08-11__infra__dashboard-next-steps.md#s-2]
  - **影响**：部署静态只读版还是可操作版、哪边作为 TODO 真相源，以及公网暴露面。
  - **约束**：`app.py` 当前无认证；上公网前必须选 Tailscale 私网、nginx basic auth + HTTPS，或仅部署静态版。
  - **来源**：看板系统后续计划 S-2；当前状态为“等用户选机器”。

## TODO 中明确等待用户决定 / 拍板

- [x] **DEC-EA4-PN · 是否解除 EvoAgent 源码护栏并启动 EA-4 PN 加载改造** [line:evoagent] [source:progress/TODO.md#ea-4]
  - **影响**：是否投入 3–5 天实现 `PetriNetReviewer`，以及是否形成鲁组 SBPN/SBTPN 技术接驳点。
  - **结论（2026-08-24 · 用户拍板）**：**立项 · 完整版**——MVP（PetriNetReviewer 子类调 PM4Py 加载 .pnml + token replay 合法性检查）再加 3 个测试用例（合法 PN / dead transition / unreachable place）；"不动 EvoAgent 代码"护栏对 EA-4 单卡解除。前置工作树对账同日执行完毕：EvoAgent 干净基线=`78f8bd9`（对账包 A=Fusion-0 七件 `d4cf180`、B=EA-3b 载荷+output/ 忽略）。

- [x] **DEC-EA6B-SCOPE · EA-6b 做全量约 50 条 triage 还是只做 B2 security** [line:evoagent] [source:progress/TODO.md#ea-6b]
  - **影响**：约 2–3 小时全量映射，或约 40 分钟安全子集；决定审计线下一阶段粒度。
  - **结论（2026-08-12 · resolved-by-execution）**：用户要求「继续，尽可能多 Agent 并行」后已执行全量方案；6 路只读核查覆盖 R1/R2 十二份材料，结果落 `progress/audits/2026/08/2026-08-09__audit__evoagent-p0-triage.md`。该记录描述执行事实，不冒充更早的显式选项答复。

- [ ] **DEC-EA6L-P2 · 是否启动 EvoAgent 学习课程 Phase 2，以及选择扩展方向与投入范围** [line:evoagent] [source:progress/TODO.md#ea-6l-p2]
  - **影响**：未批准时 EA-6L Phase 1 保持完成，EA-6L-P2 独立 blocked；批准后必须另立课程计划、章节 brief、review、双 validator 与人工 Gate，不得复用 EA-7 修复计划。

- [x] **DEC-EA7-WRITE-AUTH · 是否解除 EA-7.1~EA-7.10 的 EvoAgent 源码写入护栏** [line:evoagent] [source:progress/TODO.md#ea-7]
  - **影响**：未解除时只允许读源码、跑只读测试、写 MAS 侧方案/证据；解除后才可按安全波→工程波修改 `D:\MyResearch\EvoAgent`。
  - **前置约束**：EvoAgent 工作树已有并行研究线的 README 修改与 6 个未跟踪文件；开工前必须先对账并确定分支/提交边界，禁止覆盖。
  - **结论（2026-08-13 16:41 · 用户拍板）**：**批准**。解锁 EA-7.1、EA-7.3~EA-7.10 九卡 + 引号测试修复；按 next-plan §0-D1 语义，动仓前仍须先完成 Phase 1 工作树归属对账，且 6 个未跟踪文件按拍板「由 009/024 研究线先提交」固化干净基线。正式决策档：`progress/decisions/2026-08-13__evoagent__ea7-write-auth-tenancy-decision.md`；开工包：`progress/handoff/2026-08-13__evoagent__cli-concurrency-kickoff.md`。

- [x] **DEC-EA7-TENANCY · `llm-review` 技能版本是否按 tenant 隔离** [line:evoagent] [source:progress/TODO.md#ea-7-2]
  - **影响**：决定 EA-7.2 的 schema、唯一键、API 参数和迁移范围；租户级需要 `(tenant_id, skill_name, version)`，全局级则只修 task 更新的 tenant 过滤并明确共享语义。
  - **结论（2026-08-13 16:41 · 用户拍板）**：**租户级隔离**（档案推荐项）——`skill_versions` 唯一键改 `(tenant_id, skill_name, version)`，API/evolution/service/store 全链透传 tenant；无论语义如何均须修复 `update_task_input` 缺 tenant 过滤的越权洞。解锁 EA-7.2 租户波（Phase 3 单列，S1 稳定后执行）。正式决策档同 DEC-EA7-WRITE-AUTH。

- [ ] **DEC-CX3-CODEX-GOAL · 是否安装 Codex Goal 补丁并完成 CX-3** [line:infra] [source:progress/TODO.md#cx-3]
  - **影响**：Codex × cc 接力方案的端到端配置与验收路径。

- [ ] **DEC-V1-DUAL-VPS · 是否采用双 VPS + 甲骨文 Always Free 拓扑** [line:infra] [source:progress/TODO.md#v1]
  - **影响**：海外出口、防封冗余、Tailscale mesh 与账号敏感流量隔离。
  - **去重说明**：本项决定底层双节点拓扑；`DEC-S2-DASHBOARD-VPS` 决定看板如何部署到已选基础设施。

- [ ] **DEC-GA3-OPENCLAW-HOME · OpenClaw 部署在 WSL2 本机、NAS 还是云端** [line:casual] [source:progress/TODO.md#ga-3]
  - **影响**：24h 守护进程、cron / hook 和移动桥接设计。

- [ ] **DEC-GA5-MOBILE-BRIDGE · 手机桥接选飞书、微信还是 Telegram** [line:casual] [source:progress/TODO.md#ga-5]
  - **影响**：移动端闪念入口与所需 token / App ID。

- [ ] **DEC-GA2-BRAINSTORM · 何时明确触发双框架 MVP 脑暴** [line:casual] [source:progress/TODO.md#ga-2]
  - **影响**：GA 子线是否从 WAITING 重启，并开始 8 模板 + 1 联动点。

- [x] **DEC-EA5-README · 是否将 EA-5 README 接驳补写列入当前改造批次** [line:evoagent] [source:progress/TODO.md#ea-5]
  - **影响**：是否在 8-20~8-22 批次修文档不一致并补研究线接驳。
  - **需核实**：旧 TODO 仅在阶段收尾叙事写“EA-4/EA-5 等用户拍”，EA-5 正文未单列阻塞。
  - **结论（2026-08-24 · 用户拍板）**：**列入执行**，范围=接驳章节＋修 3 处文档不一致（半天级）；Prometheus 实接（P1-2）不在本批，维持挂账。

- [ ] **DEC-M1-LOCAL-LLM · SillyTavern 本地模型选择 llama、mistral 还是 qwen** [line:casual] [source:progress/TODO.md#m1m2m3]
  - **影响**：M1/M2/M3 的本地对话栈与后续长期记忆方案。
  - **需核实**：旧 TODO 写为“本地 LLM 模型选择”阻塞，但未明确由谁、何时拍板。

## 2026-08-13 全局审计补入的漏登门禁

- [ ] **DEC-W3-MERGE · 是否按 W3 合并建议卡执行主导航图 + 伴随索引卷收束，并采用导航层 F①-⑧ / 细分层父域·序号口径** [line:research] [source:progress/decisions/2026-08-12__research__w3-merge-proposal.md]
  - **影响**：决定 `GRAND_MAP.md` 与 `W3_unified/UNIFIED_MAP.md` 的增量并入、README 三件套登记和月度快查唯一靶入口；未拍前两版按顶部横幅并存。

- [ ] **DEC-BR6-W1B · BR-6 后续是全量预授权、按 P1→P2→P3 逐门批准，还是停在 Wave 1A** [line:research] [source:research/map/oss_landscape/e2/NEXT_PLAN.md]
  - **影响**：决定 Schema PATCH、cpn-py 独立环境、PN toy 和 Fusion-1 Gate 是否继续；默认不自动续工。

- [ ] **PEND-RESTRUCT-1 · MAS 深度重构时是否归档 MAS 根与 progress 双 `.obsidian` 配置，只保留 MyResearch 根 vault** [line:infra] [source:progress/decisions/2026-08-12__maintenance__mas-deep-restructure-plan.md#9]
  - **影响**：Obsidian 日常打开方式和 Dataview cards 历史配置去留；Agent 不可代拍。

- [ ] **PEND-RESTRUCT-2 · MAS 深度重构 P1 的执行时点** [line:infra] [source:progress/decisions/2026-08-12__maintenance__mas-deep-restructure-plan.md#9]
  - **影响**：P1 会短时打断 progress/tools/8899/INDEX 写入，必须选择无并发窗口且用户在场完成 P0 保护点与 push 后执行。

- [ ] **DEC-MCM-SOURCE-FIX · 是否解除 MCM 归档仓只读边界，修复 N1-N8 源码缺陷** [line:research] [source:progress/audits/2026/08/mcm26-five-track/PLAN_NEXT.md#1]
  - **影响**：决定是否把审计发现转成新的维护项目；若批准，必须新分支/worktree，先建失败测试，再按 N5/N6/N8 与 N1/N2/N3/N4/N7 分波修复。

- [ ] **DEC-MCM-RECOMPUTE · 源码修复后是否重算受污染的 M001-M005/M007-M009，并对 M006 做性能回归** [line:research] [source:progress/audits/2026/08/mcm26-five-track/PLAN_NEXT.md#1]
  - **影响**：现存产物值已被 Gate2 标注科学有效性污染；只有源码修复 Gate 通过后，才可在新目录重算并以新 hash 分栏登记，禁止覆盖历史产物。

- [ ] **DEC-MCM-PUSH · 是否 push MCM 仓 `50c4578` + `ceff63f`，以及 MAS 当前分批 commit/push** [line:research] [source:progress/audits/2026/08/mcm26-five-track/PLAN_NEXT.md#1]
  - **影响**：决定 MCM 修复链能否形成远端保护点；`50c4578` 来源需先确认。

- [ ] **DEC-MCM-WHITELIST · Track E 的 15 条白名单候选删/留裁决** [line:research] [source:progress/audits/2026/08/mcm26-five-track/PLAN_NEXT.md#1]
  - **影响**：决定可达性与死代码净口径，约需人工 15 分钟逐条确认。

- [ ] **DEC-MCM-DEADCODE · 是否执行 MCM 死代码清理 wave** [line:research] [source:progress/audits/2026/08/mcm26-five-track/PLAN_NEXT.md#1]
  - **影响**：毛 3395 / 净可删 1876 LOC，属于源仓写操作；必须在 push、白名单裁决后另立 wave 并设全量回归门。

- [ ] **DEC-MCM-M004-E3 · 是否授权 E3 重跑 survival 段以终判 M004 infinite** [line:research] [source:progress/audits/2026/08/mcm26-five-track/PLAN_NEXT.md#1]
  - **影响**：不做则 M004 永久如实 pending；做则需隔离环境和运行证据。

- [ ] **DEC-MCM-ERRATA · 是否输出论文侧勘误清单/队友报告** [line:outreach] [source:progress/audits/2026/08/mcm26-five-track/PLAN_NEXT.md#1]

## 进组材料+研究方法论基建全景盘点补入（9-16 · TASK-20260916-006）

- [ ] **DEC-OE1-WINDOW-SLIP · OE-1 邮件原定投递窗口(9-15)已过期+BR-1(NSFC放榜复查)逾期16天从未执行，如何处理** [line:outreach] [source:progress/audits/2026/09/2026-09-16__jinzu-and-research-infra-landscape/LANDSCAPE_AND_PROPOSALS.md#1.2]
  - **影响**：BR-1 操作卡窗口写明 8-25~08-31，检索本身只需 10 分钟公开网页查询（不需登录态），但至今从未被任何窗口执行；继续拖延会进一步压缩或错过投递时机。是否现在立即补做 BR-1 检索、投递窗口顺延到何时，均需用户表态。
  - **紧急度**：高（每天都在继续过期）。

- [ ] **DEC-PROPOSAL-NOTES-PATH · `proposal-notes.md` 死链指针核实：文件到底在哪，还是从未创建** [line:outreach] [source:progress/audits/2026/09/2026-09-16__jinzu-and-research-infra-landscape/LANDSCAPE_AND_PROPOSALS.md#1.4]
  - **影响**：`jinzu-sprint.md`§5 与 T5 提案内部引用同一份材料时路径互相矛盾（有无 `casual/` 前缀），全仓搜索两种变体均零命中。可能文件在仓外（桌面等），也可能是超前引用从未真正创建。不确定前不擅自修复或新建。

- [ ] **DEC-BRIDGE-DORMANT-OR-ARCHIVE · `bridge/` 跨领域方法论比对悬空状态是否现在正式判定为无限期搁置并归档** [line:research] [source:progress/audits/2026/09/2026-09-16__jinzu-and-research-infra-landscape/LANDSCAPE_AND_PROPOSALS.md#2.3]
  - **影响**：五个核心文件自 07-25 起是空骨架，08-31 决策档降级但未说清是否彻底停填，目前"没人正式判死也没人在推"。若判定归档，需转入 `learning/_archive` 或类似路径，避免继续误导"这是活跃线"；若保留悬空，等下次真实需要跨论文比较素材时再触发。
  - **紧急度**：低。

- [ ] **DEC-SCHOLAR-ALERT-SETUP · 是否现在设置鲁法明+EdgeIM相关作者的轻量学术更新订阅（Scholar Alert/关键词订阅）** [line:research] [source:progress/audits/2026/09/2026-09-16__jinzu-and-research-infra-landscape/LANDSCAPE_AND_PROPOSALS.md#2.5]
  - **影响**：当前 OpenReview/重要成果追踪只有一次性事件（BR-7），无常态机制。轻量订阅设置成本 <15 分钟、零维护，比自建扫描脚本划算；不设置则继续保持纯事件驱动现状。
  - **紧急度**：低。

## bridge 收口窗补入（8-13 晚 · TASK-20260813-021 系）

- [ ] **DEC-T5-NUMBERING · "T5"编号双用消歧：companion 提案改 T6（A）/ bridge 协议 PN 验证改号（B）/ 维持双横幅限定词（C，现状）** [line:research] [source:research/map/proposals/INDEX.md 顶部警示 + COLLISION_AUDIT_V2_20260813.md §2]
  - **影响**：GRAND_MAP §5、proposals/INDEX、T5_companion 三处引用与 W5 schema 的 topic ID（T1-T5 全局唯一假设）；W3 合并与 cells.yaml 实施前宜先拍。

- [ ] **DEC-R0-IMPL-GO · 是否授权 R0 修复三波实施开工（BR-10）** [line:research] [source:research/experiments/t2_r0_repair_plans_20260813/IMPLEMENTATION_ORDER.md]
  - **影响**：动 EvoAgent 与 pm4py_toy 源码；硬前置 = EvoAgent 009/024 研究线产物收口 commit + 各窗停写回执 + 独立分支/worktree（08 Gate 五条件）；未拍前 7 份设计只读。
  - **影响**：决定 F004/F005/F007/F034 与 2 张 fabricated 图是否形成新的对外材料；未经拍板只保留内部审计证据。


## 鲁线窗口2关窗移交（8-22 凌晨 · TASK-20260822-006 系）

> 来源：`research/papers_lu/teardown-joint-20260813/_archive_window2_20260815/ACCEPTANCE_REPORT_20260822_WINDOW2.md` §5。五项均不阻断已完成的关窗（CLOSED-PASS），属关窗后实质跟进。

- [x] **DEC-LU-U1-PDF-CHECK · 原 PDF 三处终核：SEGLOCK p.14(Table 5)/PNULOCK p.24(Table VII)/SBTPN p.6(λ± 式)** [line:research] [source:research/papers_lu/teardown-joint-20260813/_audit_finishing_20260821/G3G4_registry_cross_audit.md]〔✅ 08-24 销账(TASK-20260824-007,用户拍板)：三子项双路(pdftxt＋vision)核毕——SegLock T5 错位 8/8 成立／PNULOCK T VII 无误／SBTPN λ± 与 01b 校正转写逐字吻合(S1 双重核销)；报告=`research/papers_lu/teardown-joint-20260813/_audit_remediation_20260824/A4_pdf_verification.md`〕
  - **影响**：SegLock Table 5 对标数据疑制表错位(三路独立收敛)的最终裁决只剩此一步——若证实错位,"精度持平、开销降一个量级"卖点数字单源存疑,影响后续引用口径;SBTPN λ± 式终核关 01b 卡 S1 存疑项。需开原 PDF 目验。

- [x] **DEC-LU-U2-ERRATA-POINTER · "1/2–1/6" 卖点链勘误指针加否(09/README 正本就地注记)** [line:research] [source:research/papers_lu/teardown-joint-20260813/_audit_finishing_20260821/G1_content_audit.md]〔✅ 08-24 销账(TASK-20260824-007,用户拍 A 案精确口径)：指针已落 8 处(README/05/09×2/04卡×2/STUDY_ROADMAP×2)；终口径="共享 8 基准 1.70–6.35×(中位 2.76×),自建例最大约 1/5.8 系单源"＋Table 5 整列制表错位声明；**08-24 深夜二次勘误**：初版口径"1/1.7–1/4.5(中位 1/2.3)"系 A4 比值表 Test6 行串行所致,fable 独立审计抓获后按脚本重算修正——结论方向反转为"宣称范围大体成立、危害=名实错位而非注水",指针数字已同步,新 A 案话术待用户复核；话术正本=A4 报告 §终判(勘误版)〕
  - **影响**：该数字链在正本论述中仍按原文转述;加指针=就地标注存疑防未来误引,不加=保持正本纯净等 U1 终核后一并处理。

- [ ] **DEC-LU-U3-L2-PROP-A · L2 命题甲百行级实验是否立项(L2/L4 路线分歧唯一实证解法)** [line:research] [source:research/papers_lu/teardown-joint-20260813/02b_PNULOCK_sixpoint_kg_critique.md 〇.4]
  - **影响**:立项则 PNULock 剩余价值命题甲(PNU 锁 vs SegLock 的实证可比性)进入实验队列,约百行级代码;不立项则分歧维持登记态(T-B 并列,裁决权留用户)。

- [ ] **DEC-LU-U4-SUN-NAMING · 作者名称口径最终采信(Jun Sun(SMU)/孙猛(PKU,ReGA)/Meng Sun(PKU) 三分 vs 两人合并)** [line:research] [source:research/papers_lu/teardown-joint-20260813/fusion_sun_20260815/00_SYNTHESIS.md §0]
  - **影响**:影响鲁线全部卡片的引用与归属表写法;采信三分则跨卡同名者须逐一区分,合并则须给出证据链。

- [ ] **DEC-LU-U5-FOCUS-P1 · FOCUS/WINDOW_PLAYBOOK 的 P批1 行是否刷新一句(补齐波已完成事实回写)** [line:research] [source:/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/HANDOFF-20260816-finishing-wave.md §7.5]
  - **影响**:顶层两档当前仍写"P批1 待发射";刷新=状态对齐(注意 FOCUS.md 当前已有未 commit 修改,需先弄清其归属);不刷=等 P 批正式复盘时一并改。

## 可视化工作台·轻量装载·按项目联动(8-22 凌晨 · 用户陈述存档 #9 系)

- [ ] **DEC-WB-LIGHTLOAD · 轻量开工装载机制(N1)是否立项设计:启动减重＋开工前"本窗 skill/工具选装声明"(装载画像)** [line:infra] [source:progress/decisions/2026-08-22__maintenance__user-statement-archive-9.md#三]
  - **影响**:会话启动上下文重量与工具呈现方式。若立项,**收编升级**既有件而非新建:superpowers-on-demand(已是按任务启用判定协议,仅覆盖 Superpowers 族→推广为全工具族)+new-window-assignment+session_preflight/postflight 书挡;并与另一窗架构提案线头 C 缺口(合同 JSON 模板+装载画像)合并设计。
  - **约束**:看板写域在四块执行窗手中(B+ I40 在途),I90 收档前不开工、不越写域。

- [ ] **DEC-WB-PROJ-HUB · 控制面×可视化工作台×日志&待办按项目联动(N2)是否立项设计** [line:infra] [source:progress/decisions/2026-08-22__maintenance__user-statement-archive-9.md#三]
  - **影响**:项目为一等公民的进度管理与交接视图(卡＝项目主页,日志/待办经 [proj:slug] 标签聚合,交接沿卡内权威链入口)。轨道已铺:项目卡体系(TASK-20260822-005)/WORKBENCH 两步走+模块面板候选/看板五视图已批待实施/CAMPAIGNS.md(B+ I20 刚立)。
  - **红线**:TODO 按 line 分区结构不动,project 只做聚合路由不侵入 TODO(注册表 §1 明文)。

## 安全护栏·系统级写操作(8-22 凌晨 · 用户引外部事故讨论)

- [x] **DEC-SEC-GUARDRAIL · 是否将三条安全护栏立为正式规则(R1 密钥卫生/R2 系统级写操作门禁/R3 影响面+回滚双答)** [line:infra] [source:用户 2026-08-22 引外部论坛事故(某模型在 codex 执行时打印本地工具密钥/为固定端口擅改防火墙为 public/另一例打印 .ssh/config 致公网 IP 暴露)]
  - **影响**:多工具(Claude Code/Codex/ZCode)权限模式策略;仓库外状态(防火墙/端口绑定/计划任务/系统服务/env 持久化)变更默认禁止、逐次显式授权、改前快照、改后验证、CROSSWINDOW 认领销账;凭据类路径(.ssh/、*.env、key/token/cookie)默认禁读禁展开,一经进入上下文即按已泄露处置(轮换+incidents 登记)。
  - **既有基础(收编对象)**:铁律9(跨系统文件操作三禁)、子代理 4+1 caps、白名单 commit、tools/scripts/api_key_manager.py、progress/incidents/ 档制、watchdog DISABLE 先例(认领+板面销账+I90 恢复责任人=系统级变更的正确姿势已在实战中出现,未成文)。
  - **关联**:DEC-S2-DASHBOARD-VPS(app.py 无认证上公网三选一)属同类风险敞口,本项结论应作为其决策输入。
  - **结论(2026-08-22 · 用户拍板「独立、全局使用」)**:已立全局档 `/mnt/d/MyResearch/GUARDRAILS.md`(一句话版护身符＋G1 密钥卫生/G2 系统级四步门禁/G3 双答/§4 端口纪律/§5 权限模式基线/§6 泄露应急卡/§7 先例库);runbook 即正式记录,另立 decision 档免。修订走 amendment;§5 其他工具开关名 [需核] 待回填。
- [x] **DEC-DB-HUB-CSRF · 8899 写类端点是否补 Origin/CSRF 校验（/api/regen、/api/task、/api/next-task-id）** [line:infra] [source:TASK-20260824-005 Amendment 6 红蓝对抗 R4 复审（蓝队补漏+R2 裁定，2026-08-24 晨）] ✅ 2026-08-24 用户拍板「都做」→ 当日 TASK-20260824-013 落地三信号门：Origin 白名单(127.0.0.1/localhost/[::1]:port，null 拒)→Sec-Fetch-Site(cross-site 拒)→Referer 兜底；三信号全缺=无头客户端(curl/MCP urllib 实证不发浏览器信号)放行零破坏；CSRF token 否决(无会话本机服务加 token 只破坏 CLI 可用性)；live 三连 403 验收
  - **影响**：浏览器里任意网页可跨站 POST 触发 regen/改任务/消耗号（Host 白名单挡 DNS rebinding 但不挡 CSRF 简单请求；响应虽不可读，副作用已发生）。修法三选一：Origin/Referer 校验（最轻）／自定义请求头要求（X-Dashboard-Agent 已有基础）／CSRF token。属 v3/v4 既有服务面，非 hub 骨架引入——故走决策门而非本窗直接改。
  - **关联**：DEC-S2-DASHBOARD-VPS（上公网前置门）与本项同护一条服务边界；仅绑 127.0.0.1 的现状下风险=本机浏览器访问的恶意页面，非远程攻击者。
- [x] **DEC-DB-CAMPENUM · CAMPAIGNS 冻结表值与 B+ overlay 枚举冲突处置** [line:infra] [source:TASK-20260826-016 批B 端到端首跑发现（2026-08-26），披露于 decisions/2026-08-26__infra__project-axis-six-segment-plan.md §9.5]
  - **现象**：批A 写入的 CMP-JINZU 行 next_actor='user+ai' 与 MS-JINZU-ENTRY/MS-OE1-DEADLINE 两行 kind='deadline' 被 :8899 B+ overlay 校验器判非法（其合法枚举不含此二值）→ 三行在 B+ 层「整行不发布」；PROJECTS.md 生成器直读冻结表不受影响，两套消费并存口径不一。
  - **选项**：a) 改值适配 B+ 枚举（动共享登记面，需过写入门＋先查 B+ 合法值表）；b) 扩 B+ 校验器枚举（动代码，需回归 B+ 测试）；c) 维持现状双轨（接受 B+ 层缺该三行）。批C 双登记面建档前应先核 B+ 校验覆盖范围避免再造冲突。
  - **结论(2026-08-26 · 用户拍板 a「三个格子改成冻结枚举里已有的值：next_actor mixed，两条 MS kind point」)**：当日 TASK-20260826-016 收尾窗四格 CAS 替换毕（同窗回写 OE1 滑线核实注记＋updated_at）；generate.py 复验 campaigns=4 行/milestones=2 行/bplus.parse_error=0，CMP-JINZU 与两条死线在 B+ 层恢复发布。
