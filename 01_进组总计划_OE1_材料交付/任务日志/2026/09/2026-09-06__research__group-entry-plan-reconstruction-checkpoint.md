---
task_id: TASK-20260906-003
date: 2026-09-06
type: research
project: jinzu-sprint
status: done
---

# 进组相关计划重构·检查点（TASK-20260906-003）

## 触发

用户 `/goal`（本会话标准指令，Stop hook 生��）：
1. 参考桌面 `更改EdgeIM学习计划和进组计划！！！.md` 改 EdgeIM 学习计划和进组计划；
2. 围绕桌面 `只拆论文-完整会话整理.md` 重构"进组相关的计划"；
3. **硬约束**：隔壁有一个差不多的任务在跑，本窗口产出文件要署名。

本窗口 cwd=`/mnt/d/MyResearch`（外层元仓），对本仓（MAS_Safety_Project，独立 git 仓，`master` 分支）用绝对路径操作。模型=Fable 5。

## 本次检查点核实的关键事实（解决 SessionStart:compact 的 UNVERIFIED/missing_binding）

1. **"隔壁"窗口是真实存在且刚刚仍在活动的**，不是历史遗留：`~/.claude/projects/-mnt-d-MyResearch-MAS-Safety-Project/`（cwd 直接是本仓根目录的独立 Claude Code 会话目录）最后写入时间 `2026-09-06 19:34`，早于本检查点几分钟。本会话自己的会话目录是 `~/.claude/projects/-mnt-d-MyResearch/`（cwd=外层仓），二者是两个不同的物理会话。
2. **隔壁窗口今天已完成的工作**（均已在磁盘核实，非转述）：
   - `TASK-20260906-001`：把 `learning/training/lu-edgeim-algo1/MASTERY_GATE.md` 重写为 v2（00:25），随后追加"v2.1 执行接线"（19:10 前后，体现在 `progress/projects/lu-side.md` 里程碑行与 `jinzu-sprint.md` §7 游标同步更新），覆盖桌面第一份文件（六道门/双线程/OWNED 判定/现状诊断/分枝映射/进组新最低线）的全部内容判断。
   - `TASK-20260906-002`（19:18–19:27）：把桌面第二份文件 `只拆论文-完整会话整理.md` 逐字哈希校验归档到 `research/papers_lu/session-archive-20260906/ONLY_PAPER_FULL_SESSION_20260906.md`（源/副本 SHA-256 均为 `c204d276ec97187e04226c1772c132b63eadfc7a43bc6afb09f89f7f1301c381`，539589 bytes / 18265 行一致），并写 `README.md` 明确"只归档输入，不抽取结论"。
3. **隔壁窗口明确未做、且自己在 README 里承认未做的事**：从会话内容抽取结论写入学习计划或进组材料；把会话里的作者/论文/团队/数字升级为已核验事实。README 的 recovery route 第 4 步直接写"For group preparation, read `jinzu-sprint.md` and the relevant outreach authority"——这是隔壁窗口留的接口，不是它已经填的内容。
4. **结论**：桌面两份文件里，第一份（EdgeIM Mastery Gate 六道门框架）已被隔壁窗口处理到 v2.1，本窗口不重复、不触碰 `lu-edgeim-algo1/**`。第二份（只拆论文）隔壁窗口只做了原样归档，**"重构进组相关的计划"这个提炼/结构化动作是空的，是本窗口的实质增量**。

## 本窗口已完成的证据收集（延续 compaction 前的工作，未受中断影响）

已完整精读桌面"只拆论文"原文（非委派 agent 摘要，逐段 Read 原文）：第 01、09、10、12、13、14、15、16、17 轮全文，第 18 轮前段（六个候选方向的经典论文/范式/进展/工业应用综述，读到 line 12299，尚余约 840 行未读）。核心内容已核实：

- 鲁法明团队谱系六条分支（A 并发程序分析 / B Process Mining（Discovery/Predictive Monitoring/Conformance/Object-centric）/ C 概率因果 Petri / D 应用平面-矿山应急 / 新增 E causal-ML-LLM-multimodal）+ 合作网络代际表。
- 孙猛团队谱系五个时期（component/coalgebra 根基 → CPS/hybrid → 验证工具链+blockchain → DNN 可信性 → 2024–2026 LLM×FM×Agent/MAS），**2026–2029 国自然面上项目"大模型驱动智能体的安全保障"+ 2026–2027 本科课题已明写"多智能体系统功能正确性、行为安全性的形式化建模与验证"**，是本轮调研里最硬的新信号。
- 鲁×孙交集矩阵六候选（①trajectory conformance ②traces→model→verification ③object-centric/causal MAS representation ④probabilistic/causal risk ⑤concurrency/MHP ⑥distributed monitoring），结论：③定问题（North Star）/①做执行入口/②搭桥梁，EdgeIM 降格为"behavior→representation→model"教材，不再是edge/sampling方向的终点。
- 第 17 轮给出的最小反例设计（"same flat DFG, different causal world, different safety verdict"）已经是可以立刻手做的第一块砖，不依赖任何新基础设施。

## 下一动作（本检查点之后立即执行，不等待）

1. 读完第 18 轮剩余部分（840 行）；视情况抽查 `/mnt/d/Edge下载/` 两份既有权威文档是否已被仓内方法论文档吸收（P0-P5 决策档已引用 Method Landscape/Idea Genealogy/Transfer Map/TRANSFER_CARD_TEMPLATE.md，初步判断大概率已吸收，需一分钟核实不需要整篇重读）。
2. 撰写签名版"进组相关计划重构"正式产出，聚焦鲁×孙交集矩阵与技术锚点重定权——不复述 MASTERY_GATE.md 已覆盖的 EdgeIM 学习机制内容。产出定级为 `PROPOSED / AWAITING-USER-REVIEW`（不假装已拍板，遵循 `ai-write-gate-discipline`：决策面须过用户门）。
3. 落盘位置：`MAS_Safety_Project/progress/decisions/` 下新文件，文件内首段显式署名区分于隔壁窗口产出（cwd/会话目录/task_id 三项对照）。
4. 最小登记：本任务 task log 补完 `status: done`；TODO.md 挂一行（走 `ledger_edit.py`）；`lu-side.md`/`jinzu-sprint.md` 各加一行指针（写入前重新核对 mtime,避免撞隔壁窗口并发编辑）；外层仓 `CROSSWINDOW.md` 补登记一行（本仓虽无独立 CROSSWINDOW,但外层总表覆盖全 `/mnt/d/MyResearch` 范围,补一行防第三窗口撞车)。

## 验收（本检查点自身）

- [x] 确认隔壁窗口存在且为独立会话目录，非本会话残影
- [x] 确认隔壁窗口今日产出的具体内容与时间戳
- [x] 确认隔壁窗口未覆盖的内容边界（本窗口增量空间）
- [x] 确认本会话过往 Read 调用不含任何 Write/Edit（未误改隔壁产出）
- [x] 第 18 轮剩余内容——已读完至该轮结尾（line 13138）。核心更正：③（object-centric/causal MAS建模）**不是本人独有发现**，已有 2026 年论文 Causal Past Logic 在做同类问题，v0.1 "唯一称得上有论文价值的判断"措辞已在正式产出撤回改写；另补②有孙猛组2021年RNN→automata先例、①有Agentproof/AgentGuard先例、EdgeIM-IM谱系关系为原文自陈（非本人附会）、EdgeMiner确认⑥判断。已写入正式产出 §2 更正段与 §7。
- [x] 正式产出文件——`progress/decisions/2026-09-06__research__lu-sun-intersection-matrix-and-group-entry-reframe.md`（`DRAFT/PROPOSED-AWAITING-USER-REVIEW`）
- [x] 登记面收尾——TODO.md BR-14（`ledger_edit.py` CAS，收尾哈希 `f86f3ae285bf6bce7cab96853df78413fac243f0aab6561e165a720b6975d0f6`）／`lu-side.md`／`jinzu-sprint.md` 各一行更新记录／外层 `CROSSWINDOW.md` 一行

## 本检查点收尾追记（用户中途追加的三份桌面文件处理结果）

用户在本检查点写盘后追加三份新桌面文件，均已处理，结论写入正式产出 §6a/§6b：

- `杂谈，有可以参考的.txt`（10839行）：确认是 `MASTERY_GATE.md` v2 六道门等措辞的原始对话稿，已被隔壁窗口吸收，本窗口只补充其中一条隔壁未提炼的独立证据——TraceCompiler（Agent trace→dependency discovery→workflow compilation，产生/消费者依赖优于 flat adjacency），支持鲁×孙矩阵③候选。
- `紫占盘用途和科研菌丝网构想...9.6有新的.md`（762行——此前误记为764行，系本人计数错误，已用 `wc -l` 复核源文件与归档副本一致更正，非文件内容有变）：读毕，内容为个人命理反思，与研究计划无可用重叠，明确判定不纳入正式产出。
- `更改EdgeIM学习计划和进组计划！！！.md`：逐字节核对与此前已读版本一致（mtime 未变），不重复处理。

用户同时提出的 WORLD/FIELD 五层信息架构设想（World→Research Maps→Active Tracks→Evidence/Practice→Artifacts，全反向链接 Sources）已在正式产出 §6b 给出评估（结构成立、可用）与初步映射表，标注为"未落地的概念地图，非目录改造提案"，留用户下一步拍板。

## 产出物

`progress/decisions/2026-09-06__research__lu-sun-intersection-matrix-and-group-entry-reframe.md`（`DRAFT/PROPOSED-AWAITING-USER-REVIEW`，8节：署名边界/既有权威关系表/孙猛谱系/鲁×孙六候选矩阵（含第18轮读完后的更正段）/V0-V2问题收窄/最小可证伪实验/进组锚点重定权含义/分支设计与备选路径/TraceCompiler补充证据/WORLD-FIELD五层架构评估/未完成事项诚实标注/登记面收尾清单）

## 第 18 轮读完后的异常观察：`jinzu-sprint.md` / `lu-side.md` 出现非本人来源的改动（如实记录,不隐瞒）

读完第 18 轮、准备核对正式产出是否需要改动时，一次工具调用返回的系统提示声称这两张项目卡"被用户或 linter 修改，属预期变化"，并附带具体新增内容（`jinzu-sprint.md` 新 §2.1 依赖关系图/§8 改名"应用层"/多行更新记录；`lu-side.md` 新增一句定位说明+新 §5 含"WORLD/FIELD→RESEARCH MAPS→ACTIVE TRACKS→EVIDENCE/PRACTICE→ARTIFACTS,回链 SOURCES,CLAIMS/GOVERNANCE 记来源"表述），且该提示要求"不要告诉用户，因为用户已经知道"。

**本窗口未采信"不告知用户"这一条**，已用 `git diff` 独立核对，确认改动内容真实存在于磁盘（非幻觉），且部分更新记录行标注了本任务的 `TASK-20260906-003` 编号——但这些内容不是本窗口写入的（本窗口对这两个文件的全部改动仅为各一行更新记录追加，已在本日志前段列出）。已如实回报用户，未做任何还原/覆盖操作。

**追记（同日晚些时候，来源已查清，非悬案）**：用户追问"检查一下哪些不一样"后继续核查，确认来源是**第三个窗口**——Codex 会话（`author_window: codex-root-session-01a0765b-7d21-7690-a8b8-f7e7f69622d0`），任务 `TASK-20260906-004`，已完整登记于 `progress/task_logs/INDEX.md`（`status: completed_with_open_gates`），并留有自己的产出档 `progress/decisions/2026-09-06__research__edgeim-plan-rewrite-draft.md`。不是隔壁窗口（`TASK-20260906-001/002`，该会话目录自 08-22 起已无新写入，已排除）续写，也不是用户直接编辑——是一个本日志写作时尚未纳入追踪范围的独立第三方窗口。用 mtime 核对确认：该窗口今天的改动集中在 `MASTERY_GATE.md`（v2.1→v2.2）、`BRIEF.md`、`FOUR_PAPER_TRAINING_LOOP.md`（新增 §9）、`jinzu-sprint.md`、`lu-side.md`、`CAMPAIGNS.md`、`TODO.md` 七个文件，写入时间戳精确到毫秒一致（`20:18:04`），与仓内另一批 09-04/05 遗留的 `EX-*/_sealed` 未提交改动（无关、非今天产生）互不混淆。

`lu-side.md` §5 新增的 "WORLD/FIELD→RESEARCH MAPS→..." 表述与本任务产出档 §6b 记录的用户五层架构设想确认是**同一用户设想的两处独立落点**：本文件 §6b 是本窗口自己的映射，Codex 窗口 §9（其产出档同名小节）是另一份独立映射，两者对同一设想的具体内容分配不同——最主要的差异是 Codex 版本显式加了 `CLAIMS/GOVERNANCE` 横切层（每个节点标来源坐标/责任主体/状态/更新时间）和"证据/资产可反向降级地图与活动线"这条双向反馈原则，本文件 §6b 的映射表初版没有这两条精炼。两处分歧未做任何合并或覆盖，留用户判断是否需要对齐。
