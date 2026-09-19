# TODO v4 · 七线任务主账

**Last updated**: 2026-09-03（姜老师论文与相关产出归档收口）
**Type**: 主控 todo · 按 line 分区
**数据契约**: `progress/decisions/2026-08-12__maintenance__dashboard-v3-data-contracts.md`
**迁移前快照**: `progress/_archive/TODO-v3-purpose-2026-08-12.md`

> **状态权威**：当前 actionable 以本 TODO 为准；已完成状态以 `progress/task_logs/INDEX.md` + 具体 task log 为最终验收证据。`progress/NOW.md` / `STATUS.md` 是自动生成视图，不得反向覆盖本档。
> **归线规则**：任务唯一归属由所在 `## ... <!-- line:... -->` 决定；旧 `[topic:...]` 只作历史检索标签。
> **计数规则**：只统计本文件中合法的 `- [ ]` / `- [x]` 任务行；`progress/lines/*.md` 不再内嵌可计数任务。
> **迁移基线**：原 TODO 54 件任务全部保留（含 4 个由坏 checkbox 恢复的任务），另迁入 `lines/pending.md` 23 件挂起任务。动态件数由生成器计算；状态修复与逐项理由见迁移审计。

---

## EvoAgent 作品集改造 + 学习 <!-- line:evoagent -->

> **状态**：ACTIVE（EA-4 D1–D4 已技术收口；EA-5/EA-7 与研究层按各自门禁推进）
> **当前主入口**：EA-7.1~EA-7.10 分波实施 / EA-3b / EA-5 / EA-6L-KG / EA-6L-P2 / EA-6L-F1；EA-4 技术回执见 TASK-20260826-012；代码路径 `/mnt/d/MyResearch/EvoAgent`。
> **承接档**：`progress/decisions/2026-08-09__research__evoagent-context-verification.md`
> **审计档**：`progress/audits/2026/08/2026-08-06__audit__evoagent-code-review.md`
> ⚠️ `progress/` 下仍有旧 EvoAgent 路径引用；历史 prompt 档只加路径变更说明，活档再真改。

### 前置与最低成本闭环

- [x] [topic:evoagent-refactor] **EA-0 · `.git` / `docs/` / `git init` 安全性实测** ✅ 8-9
  - **结果**：`.git` **不存在**（`.gitignore` 在但 `.git` 不在 —— 模板带来的孤儿文件）· `docs/` **不存在** · `git init` **安全**（全仓 540K,无 `node_modules`/`.venv`;`.gitignore` 已排 `__pycache__`/`*.db`/`.env`）
  - **顺带解掉**：`TASK-20260809-001` 标的 `[需验证]`（"无 .git 是推断非实测"）—— **源档 L138 的推断是对的**
  - **方法**：`ls -a` + `du -sh` + 读 `.gitignore`

- [x] [topic:evoagent-refactor] **EA-1 · `git init` + 首个 baseline commit** ✅ 8-11
  - **价值点**：8075 行**无版本历史**，任何改造无回滚基线
  - **验收**：`git log -1` 有 initial commit；`git status --short` 为空；`git check-ignore -v` 确认 `.env` / `*.db` / `__pycache__` 受忽略规则覆盖；首个 commit 的实际文件数以 `git show --stat` 为准
  - **完成记录**：baseline commit `ef768b5`（「EA-1 baseline commit 2026-08-11（重构 Phase 0 前置）」· 52 files / +9405）；详见 `progress/task_logs/2026/08/2026-08-11__maintenance__folder-restructure-execution.md` Phase 0-3
  - **优先级**：高
  - **done 类型**：verify-done

- [x] [topic:evoagent-refactor] **EA-2 · 补 `docs/` 占位（已改用友好报错方案）** ✅ 8-9
  - **⚠️ 原方案已否决**：补空占位会让脚本从"崩"变成"输出一个空 PDF"。而简历对外宣称的是「把 md 知识库转 PDF」——
    **空 PDF 比崩更危险：崩会被发现,空 PDF 看起来像成功。** 参 `DECISION-20260806-005` 风险 R7。
  - **实际做法**：`render_knowledge_base_pdf.py:479` 加 `SOURCE.exists()` 检查 + `SystemExit` 友好中文报错
  - **实测**：退出码 1,输出"找不到知识库源文件…请把 Markdown 知识库放到 docs/EvoAgent知识库.md 后再运行"
  - **副产品**：消掉 `DECISION-20260806-005` 步 2 的 `[⚠️矛盾]`（任务表 L178 标 30 min / 收尾清单 L249 标 5 min）—— 实际约 15 min

- [x] [topic:evoagent-refactor] **EA-3 · 跑脚本验 ENOENT 已消** ✅ 8-9
  - **结果**：友好报错生效,不再抛 traceback
  - **⚠️ 本轮真收获（audit 漏记项）**：`register_fonts()` 在 `SOURCE.read_text()` **之前**执行,硬编码
    `os.environ.get("WINDIR", r"C:\Windows")` —— WSL 下 `WINDIR` 不存在 → fallback 到字面 `C:\Windows`
    → 实测报错 `Can't open file "C:\Windows/Fonts/msyh.ttc"`。**WSL 下永远先死在字体上,走不到 `docs/` 那步。**
  - **为什么 audit 漏了**：audit 是静态读代码,没实际执行 —— 问题 7 方向对但**顺序错**
  - **修法**：加 `FONT_DIR_CANDIDATES`（含 `/mnt/c/Windows/Fonts`）+ `find_font_dir()` 逐个探测 + 全不命中时列出所有尝试路径

### 改造与验证

- [x] [topic:evoagent-refactor] **EA-3b · 字体修复端到端验证** `[需验证]` [8-12~8-15] [P2] [note:先放一份 md 再跑] [done:2026-08-15]
  - **现状**：逻辑改对 + `/mnt/c/Windows/Fonts/` 下 `msyh.ttc`/`msyhbd.ttc`/`simhei.ttf` 三字体 `find` 命中 + `reportlab 4.5.1` 已装于 solver —— 但**未实际渲染出 PDF**
  - **验收**：放一份真 md 进 `docs/` → 跑出 PDF → 中文不乱码
  - **优先级**：高

- [x] [topic:evoagent-refactor] **EA-4 · PN 加载改造（= known-improvements A3）** [P0] [批准:2026-08-24完整版] [done:2026-08-26] [evidence:aa14115/ad2e5e9/acc762c;focused=29passed;full=71passed+1既有EA7.7引号失败]
  - **价值点**：EvoAgent 接鲁组 SBPN/SBTPN 线的技术接驳点，9 月邮件卖点
  - **验收**：`PetriNetReviewer` 可加载 `.pnml/.pnml.gz`，结构检查与 token replay 接口在位，服务开关默认关闭；focused tests 29/29
  - **完成记录**：D1–D4 已由 `aa14115`/`ad2e5e9`/`acc762c` 收口；2026-08-26 fresh focused `29 passed`、EvoAgent 工作树 clean；全套 `71 passed + 1` 既有 EA-7.7 引号断言
  - **优先级**：中（技术收口；EA-5/研究层另计）
  - **done 类型**：verify-done（工程侧；用户接轨/研究侧另门）

- [ ] [topic:evoagent-refactor] **EA-5 · README 加研究线接驳章节 + 修 3 处文档不一致** [2026-08-24批准] [note:拍板范围=接驳章节+修3处;Prometheus实接(P1-2)不在本批维持挂账] [P2]
  - **价值点**：audit 查出 3 处文档与代码不一致（含 Prometheus 指标：README 宣称有 label，实际**7 个** counter/summary 无 label 无 histogram）
  - **验收**：README 修正 3 处 + 加"研究线接驳"段
  - **⚠️ 数字纪律**：对外必须分清——**8-6 audit 正文有 18 个编号问题，概览另给 5 实质 + 6 改进 + 3 文档不一致的摘要计数（不是对 18 项的一一分类），六维度均分 4.15（5 分制）**；**R1+R2 = 60 条原始 P0 候选 / 去重后约 50，10 分制 5.25→3.5**。不同体系与量纲不可混用（见代码审计 handoff §2.1）
  - **可打点**：**27 个真测试**（非 smoke · audit L31/L380）
  - **优先级**：中
  - **done 类型**：commit-done

### 学习体系与审计基线

- [x] [topic:evoagent-learning] **EA-6L · EvoAgent 渐进式学习体系 Phase 1：工程案例、元模块与双方向最小切片**
  - **设计档**：`progress/decisions/2026-08-09__research__evoagent-learning-system-design.md`
  - **Fusion-0 双出口：文件互操作 PASS / 审计 Gate R0 FAIL**（08-13 收口窗按 039 波裁定收窄口径；TASK-20260812-009 event-log + TASK-20260812-024 interaction graph）：只读转换层 + 两个 SQLite CLI（XES / GraphML）；不迁数据库、不加生产依赖。event log 经 PM4Py 2.7.23.4 真实导入（1 case/11 events）、interaction graph 经 networkx 真实读取（9节点/7边），两出口共用 `message:NNNN` evidence id 空间并有一致性测试锚定。**但 9 findings 修复（R0）前不得当实验结果**——修复设计波 TASK-20260813-022 在产（`research/experiments/t2_r0_repair_plans_20260813/`）。
  - **实施验收（2026-08-12）**：基线 commit `ef768b5`；Python 3.11 新增 10+6 测试全过；Python 3.10 全量 43 项 = 42 PASS + 1 个实施前既有单双引号断言失败，失败面未扩大；缺口 = 跨表因果序、node start/end、duration、风险层（留 Fusion-1）
  - **下一门禁 = Fusion-1 单向桥**（kill 检查点①）：从 event log conformance/发现结果抽 handover/循环/共享工具特征 → 作交互图/风险模型的结构或参数输入；不成立则降级 T2 单线
  - **目标**：以 EvoAgent 为案例学习框架、模块契约、不变量、设计权衡、优秀模式、失败传播、测试/安全/运维、元模块抽取与迁移
  - **双方向**：A = PM4Py → LLM Agent 工作流建模/过程挖掘/可观测性；B = SBPN/SBTPN → MAS 协同效应/自传播风险；C = Agent Process-Risk IR 融合闭环
  - **融合要求**：PM4Py 输出必须进入 SBPN/SBTPN 的结构、参数或约束；传播模型输出必须形成可在 EvoAgent Canary/Shadow 中验证的干预，防止“工具名词拼接”
  - **产物规划（修订后）**：首轮只做 `00_LEARNING_MAP.md` + 一个完整 `01_VERTICAL_SLICE.md` + pattern/failure/pilot/sources 共 6 件；原二十余文件结构降为远期蓝图
  - **首轮方法**：学习起点诊断 → 知识依赖图 → Pre-test/Guided read/Evidence/Reconstruction/Transfer/Reflection 六步 → 学习收益账本
  - **双方向最小化**：A 先做 trace→event log→conformance；B 先做 3-Agent 风险状态传播 toy；融合按 Fusion-0 共同数据 → Fusion-1 单向桥 → Fusion-2 干预 → Fusion-3 闭环递进
  - **停止规则**：若 PM4Py 输出不能成为风险模型的结构/参数/约束/先验，或 SBPN/SBTPN 对普通图/基础 PN 无增量，则停止当前融合而非继续堆模块
  - **证据纪律**：研究问题和融合新颖性均标 `[需验证]`，后续需查新和实验；引用当前源码需记录 snapshot/symbol/verified_at
  - **状态**：`done-phase-1`（T9 Step 3 用户裁定「可用」PASS @8-12 20:47；Task 1–9 记录全闭环〔`TASK-20260812-020`〕；未批准课程扩展，整个学习体系不得标完成）；EA-6b triage 已完成，后续见 EA-7.1~EA-7.10
  - **优先级**：高

- [ ] [topic:evoagent-learning] **EA-6L-KG · 建立可逐步点亮的 EvoAgent 知识图谱学习地图**
  - **触发原文**：用户提出“按照知识图谱、学习顺序来点亮的路径和完整知识图谱地图”。
  - **目标**：把系统链、工程模式、失败证据、PM4Py、InteractionRisk、SBPN/SBTPN 与 Fusion 的概念节点、依赖边和推荐学习顺序放在一张总图中，并提供当前学习进度视图。
  - **点亮规则**：不得只按“读过文件”点亮；至少绑定 `L0 听过 / L1 能解释 / L2 能重建或验证`、对应 reconstruction artifact、evidence status 与 review trigger。
  - **建议产物**：完整静态知识图谱 + 当前点亮状态图 + 节点索引表（concept_id / prerequisites / source section / mastery evidence / status）。实现形式在设计时决定，优先考虑 Obsidian/Markdown 可读的 Mermaid + 机器可校验状态表，避免先造复杂前端。
  - **前置**：Tasks 6/7 稳定后提取真实概念和依赖；Task 8 完成后补 Process-Risk/Fusion 节点，避免基于空骨架画图。
  - **验收**：新读者能从任一未点亮节点看到先修节点、下一阅读、练习与通过证据；状态更新不依赖手工改两份互相漂移的图。
  - **优先级**：高（学习导航增强）；独立于当前 Tasks 6/7 并发写入。

- [ ] [topic:evoagent-learning] **EA-6L-P2 · 学习课程 Phase 2 扩展** [P2] [blocked:课程扩展未批准]
  - **边界**：EA-6L Phase 1 已完成；本项只承接新增章节、练习与新人工 Gate，不得反向把 Phase 1 改回 open。
  - **启动条件**：用户明确选择扩展方向与投入范围。
  - **验收**：独立计划、章节 brief、review、双 validator 和人工 Gate 全部落盘。

- [ ] [topic:evoagent-learning] **EA-6L-F1 · Fusion-1 单向桥与 kill checkpoint①** [P1] [blocked:先完成工作树归属与实验基线对账]
  - **目标**：从真实 event-log 的 conformance/发现结果提取 handover、循环或共享工具特征，作为交互图/风险模型的结构、参数、约束或先验输入。
  - **停止规则**：若 PM4Py 输出不能成为风险模型的结构、参数、约束或先验，立即降级为 T2 单线，不继续堆融合模块。
  - **验收**：至少三类受控偏差、一个外部 trace、完整基线、可复现实验 receipt 与明确 PASS/KILL 裁定。

- [x] [topic:evoagent-refactor] **EA-6a · 汇总 EvoAgent 当前进度、已有收获与审计材料，建立初步统计基线**
  - **触发原文**：`progress/decisions/2026-08-09__maintenance__user-statement-archive-1.md`
  - **目标**：先回答“目前做到了什么、获得了什么、审过什么、数字口径有哪些冲突”，再进入源码级 P0 核验
  - **统计分层**：项目资产/功能与规模 · 已验证亮点 · 已修复事项 · 审计批次与评分 · finding 原始数/去重数/复核状态 · 未完成动作
  - **证据等级**：A 当前源码/实跑复核 · B 审计原文有文件行号 · C 汇总档转述 · D 待验证；不得将 C/D 写成已确认事实
  - **产物**：一份初步统计报告 + 一份审计材料索引/口径对照表（最终路径在设计阶段锁定）
  - **验收**：每个数字可回指来源；明确 **18 个编号问题 / 概览 5+6+3 摘要计数（非一一分类）** 与 **60 条原始 P0 / 去重后约 50（R1+R2）** 是不同审计体系；列出冲突与缺口
  - **完成证据（8-12）**：`METRICS.md`（11 指标）+ `CODE_MAP.md`（52 tracked / 38 py / 7,832 LOC @ `ef768b5`）+ EA-6b triage §0/§1；旧「约 50」估计已被 25 个实测根因组取代
  - **优先级**：高

- [x] [topic:evoagent-refactor] **EA-6b · R1+R2 的 60 条原始 P0 候选四分类后落 TODO**
  - **欠账**：`TASK-20260809-001` 已标 —— **60 条原始候选（跨视角去重后约 50）**尚未完成当前源码 triage 并落看板
  - **不逐条照抄**：R1/R2 六视角有跨视角重复；且已实测静态 audit 会漏（字体）也会过期（当前源码变化会导致 finding 降级/撤销）
  - **四分类**：① `CONFIRMED` 当前源码仍存在 → 落 TODO 带当前 `file:line` ② `DOWNGRADE` 已部分覆盖或不构成 P0 → 记录依据并降级 ③ `UNVERIFIABLE` 缺 Git 历史/部署/运行证据 → 标 `[需验证]` ④ `WITHDRAW` 当前源码找不到或旧 review 误读 → 撤销并留复核说明
  - **产物**：`progress/audits/2026/08/2026-08-09__audit__evoagent-p0-triage.md`
  - **状态（8-12 晚）**：✅ 四分类 triage 与入板均完成（6 路只读并行 @ `ef768b5`：55 行；测试实测后终态 = CONFIRMED 32 / DOWNGRADE 20 / WITHDRAW 3 / UNVERIFIABLE 0；去重 25 根因组，其中新确认 10 组）。
  - **前置已完成**：EA-6a 已锁定统计基线；历史“全量或 B2 子集”粒度决策已按执行事实关闭。
  - **源档位置**：`runbooks/2026-08/evoagent-review/` A1-A4 + B1-B2 + R2-C/F/O/S/T · `runbooks/2026-08/` 根下 R2 四视角 + R2.5 四视角 + `v3-evoagent-reverse-grade.md` · `decisions/` 8-06 六份

### EA-7 修复实施队列

- [ ] [topic:evoagent-refactor] **EA-7.1 · G10 SSRF：fetch_diff 对 webhook 可控 URL 带 Bearer 外发**（`github.py:34 fetch_diff`）[P0] [note:安全] [blocked:待Phase1动仓对账·D1已批8-13]
- [ ] [topic:evoagent-refactor] **EA-7.2 · G11 多租户隔离缺口 ×3**（`postgres_store.py:42-45` skill_versions 无 tenant_id；`:323` 读无 tenant；`:370` UPDATE 无 tenant）[P0] [note:安全·D2已定租户级8-13] [blocked:待Phase1动仓对账+S1波后单列]
- [ ] [topic:evoagent-refactor] **EA-7.3 · G7 500 兜底回显 str(exc)**（`api.py::do_POST`）[P0] [note:安全] [blocked:待Phase1动仓对账·D1已批8-13]
- [ ] [topic:evoagent-refactor] **EA-7.4 · G8 提示注入弱黑名单**（`api.py::/v1/evolution/propose` + `evolution.FORBIDDEN`）[P0] [note:安全] [blocked:待Phase1动仓对账·D1已批8-13]
- [ ] [topic:evoagent-refactor] **EA-7.5 · G22 进化审计链缺失**（`evolution.py::propose/rollback` 零调 `store.audit`）[P0] [blocked:待Phase1动仓对账·D1已批8-13]
- [ ] [topic:evoagent-refactor] **EA-7.6 · G18 DDL 双源漂移**（postgres DDL 缺 `release_observations` 表）[P0] [blocked:待Phase1动仓对账·D1已批8-13]
- [ ] [topic:evoagent-refactor] **EA-7.7 · G6 测试体系群**（无 CI + `.dockerignore:6` 排除 tests + postgres_store/api/metrics 零测试 + 零 mock/conftest/并发；前置 = 清既有引号失败）[P0] [blocked:待Phase1动仓对账·D1已批8-13]
- [ ] [topic:evoagent-refactor] **EA-7.8 · G13 部署硬化四件**（compose 无 healthcheck/资源限制/日志轮转 + Dockerfile 无 USER）[P0] [blocked:待Phase1动仓对账·D1已批8-13]
- [ ] [topic:evoagent-refactor] **EA-7.9 · G15 依赖全浮动无 lockfile**（`requirements.txt:1-6`）[P1] [note:部署时评估升 P0] [blocked:待Phase1动仓对账·D1已批8-13]
- [ ] [topic:evoagent-refactor] **EA-7.10 · G20/G21 无 OpenAPI + 错误响应无 hint**（`api.py` stdlib server；5 处泛化消息）[P1] [blocked:待Phase1动仓对账·D1已批8-13]

> **告一段落信号**：EA-3b、EA-6L-KG、EA-6L-P2、EA-6L-F1 与 EA-7 分波各按独立验收收口；EA-4/EA-5/EA-7 写入均受各自门禁约束。

---

## 科研主线（鲁组 + 方法论 + MCM 复盘） <!-- line:research -->

- [x] [topic:jiang-archive] **姜老师论文与相关产出全量归档核验、统一入口补齐** [P2] [done:2026-09-03]

> **当前状态**：ACTIVE（P1）。鲁组 9 月报到在即；MCM 仅作方法论复盘素材，不维护代码。
> **Sun 子线**：PAUSED，定位为归档收尾；任一条件满足时重启：用户说“重构完成/科研主线可以继续”、给出新方向/方案路径、或重构任务独立落 task 并完成。
> **MCM 边界**：不开 PR 链、不补全 M 奖；MV-1~5/F030 与五轨 Gate2 均已完成。当前只从 `PLAN_NEXT.md` 的用户决策路线继续，旧 W1b/W2-W6 仅作历史映射。

### 教学包整改收口移交项（TASK-20260821-001 · 2026-08-22 落）

> **主档**：`progress/handoff/2026-08-14__teaching-prefab-batch/`（REMEDIATION_LOG + PENDING_VERIFICATION_TRIAGE_20260822 §一/§七.A + RESOLUTION_RECEIPTS_20260822）
> **task log**：`TASK-20260821-001`

- [x] [topic:teaching-prefab] **TP-1 · 鲁组正本统一修正波（✅ 08-22 02:5x 执行完毕：鲁线窗 02:4x 关窗冻结解除；鲁1 符号错 μ/η 修正 ~30 处+鲁2-5 销项+鲁6 落盘+01b S1/S2 销项，全带勘误注；commit 见 MAS 仓）** [P1]
  - **内容**：鲁1 符号错级联（式3 μ 误作 Θ、阈值 η1/η2 误作 θ1/θ2 → 01 卡+teaching 五件+05:17）；鲁2-7 销项注记；其 01b 卡 S1/S2 一并销——裁决文本已全部 staged 于 triage §一 + 回执档 §三
  - **验收**：级联后 grep 六包无未注记 θ1/θ2 残留；verify 思路同 PLAYBOOK §四.1
  - **优先级**：高（首考包）

- [ ] [topic:teaching-prefab] **TP-2 · Bazille CAV 2020 全文抽取（ProbGuard P1/P2/P3 终裁）** [P2]
  - **内容**：DOI 10.1007/978-3-030-53291-8_17（OA），Springer cookie 墙阻抽取；需白名单外镜像或浏览器通道
  - **验收**：Thm 5/6 原式对照 → answer_key:77①②③/mistakes R-11 销项
  - **优先级**：中

- [ ] [topic:teaching-prefab] **TP-3 · ProbGuard 版本迁移对账（arXiv v2 vs 拆解旧版数字）** [P2]
  - **内容**：v2 已删 FP 列与任务数/trace 计数；拆解 FP 0%/75%/100%、30 traces 等出自旧版，逐数字对账 v2
  - **验收**：拆解/教学引用全部锁版本号或更新为 v2 口径
  - **优先级**：中

- [ ] [topic:teaching-prefab] **TP-4 · PLAYBOOK §四.1 候选第三条待用户拍板**（"FAIL 发现当日转 TODO 或显式销项"）[P3]

### Bridge 调研与占坑（8-12 四 Agent 调研产出）

> **主档**：`research/bridge_scan_2026-08-12/SYNTHESIS.md`（T1-T5 排序 + RQ1-RQ5 查新裁定 + 竞争者地图）
> **task log**：`TASK-20260812-003`
> **关键时窗（2026-08-13 深挖波再校准）**：宽泛“PN×agent=0”已被碰撞审计推翻；狭义空白收窄为“PN 并发语义 + alignment/过程发现 + 多 agent 运行时保障 + 可复核保证”的合取，按 **3-6 个月偏紧管理**（策略估计）；新增最近邻 = ProbGuard(ASE'26)、ProMAS、yashch03 原型。证据：`research/map/radar/2026-08-13_deep_scan_delta.md`。

- [ ] [topic:bridge-scan] **BR-1 · 8-25 后复查 NSFC 2026 放榜（鲁法明是否中"知识图谱/大模型"方向项目）** [8-25~8-31] [P1]
  - **价值点**：决定 9 月邮件话术分支——中了则"助您加速已立项方向"，没中则"自带课题上门"
  - **验收**：letpub/x-mol/NSFC 官网任一渠道确认 + 更新 SYNTHESIS §5 行动项 1
  - **优先级**：高

- [ ] [topic:bridge-scan] **BR-2 · Bridge 课题 T1-T3 细化为 1 页方案 + 2026-12 前 arXiv 占坑计划** [9-1~12-31] [P1]
  - **T1**：PN 展开 × AgentWorm 防御（着色 PN 传播可达集 + 最小切断集）——最高价值蓝海
  - **T2**：agent 轨迹 conformance + 形式保证（vs SAP 2606.20669 错位竞争）——最快上手，执行载体 = EA-6L 方向 A 最小核心（不在此重复计数）
  - **T3**：use-after-poison 记忆投毒值流检测（UAF 迁移，对接刚中 ICML 2026 的 Securing MAS）——新增候选
  - **验收**：每个课题 1 页方案（RQ/方法/数据/基线/风险）；12 月前至少 1 个 toy 挂 arXiv
  - **提案部分已完成（TASK-20260812-032）**：`research/map/proposals/INDEX.md` + T1/T4、T2、T3 三份；W4 评审门禁已回填，T2 过度保证声明已主控收窄
  - **剩余**：T2 三类偏差受控实验 + 外部 trace + 全基线；过 kill criteria 后才写稿/arXiv（窗口已下调 3-9 月）
  - **优先级**：高

- [ ] [topic:bridge-scan] **BR-3 · 科研地图月度快查（每月 1 次 · 10 分钟）** [P2] [note:例行]
  - **执行细则**：`progress/runbooks/research-map-maintenance.md`（§2 七项监测清单 + §3 事件日历 + §7 派发模板）
  - **09-05 semantic 扩展**：扫描单位从窄领域标签扩为 `agent traces -> structure/dependency/workflow/protocol -> compile/verify/monitor/diagnose/repair`；每次同时搜领域标签、action+object+result、替代 representation 和否定 residual 的工作；命中先入 Transfer Card prior-art 栏，不直接升级 research queue（TASK-20260905-001）
  - **验收**：每次快查在 `research/map/CHANGELOG.md` 追加日期戳增量行；策略变化时同步对应地图"动向"节
  - **基线 #0 已完成**：`research/map/radar/2026-08-12_radar_baseline.md`；下次 diff 水位线 + 新监测词（STEAD/AgentLTL/agent conformance/agentic BPM）见该档 §5
  - **增量 #1 已完成（TASK-20260813-018）**：`research/map/radar/2026-08-13_deep_scan_delta.md`；新增 ProbGuard/ProMAS/conformance-shield 原型/NeurIPS 双 workshop，并与 TASK-021 碰撞审计对账
  - **优先级**：中

- [ ] [topic:bridge-scan] **BR-13 · 执行鲁组学习—谱系—迁移双层计划** [P0] [note:TASK-20260905-001/002/20260906-001/004；用户报告 EdgeIM 已过 EX-03；当前入口=MASTERY_GATE v2.1 Whole-Paper Diagnostic 15题；诊断后按 W0→W4 滚动窗口推进；EdgeIM 学习主干、研究邻域、进组应用层分离；四论文仍一主干三镜头：sigRank@EX-01/05、GroundTruth@EX-06→07、CrossEdgeIM@EX-06/TransferCard；科研菌丝网五层映射只作导航，不改冻结OS、题面/PASS，不扩实验infrastructure]
- [ ] [topic:bridge-scan] **BR-14 · 鲁×孙交集矩阵与进组计划重构（草稿）** [P1] [note:TASK-20260906-003产出=progress/decisions/2026-09-06__research__lu-sun-intersection-matrix-and-group-entry-reframe.md；状态DRAFT/PROPOSED-AWAITING-USER-REVIEW；不改MASTERY_GATE.md/不改研究执行门；孙猛团队谱系+鲁×孙六候选+V0-V2问题收窄+可证伪首实验；来源=只拆论文会话第15-18轮，署名区分隔壁窗口TASK-20260906-001/002]
- [ ] [topic:bridge-scan] **BR-15 · 鲁组进组准备三件套复核（整合版v1.1/执行细化v1.3/双入口v1.1）+ CCF优博访谈材料归档** [P1] [note:三文件均在 /mnt/d/Edge下载/ 外部路径非本仓产物，疑似另一并行窗口/ChatGPT分享快照产出；学习与科研体系-整合版.md §8已将CCF优博10期访谈(docx全文/ccf优博系列.pdf/杨学讲座笔记)正式整合为教学启发对照表，解决此前材料用途未明疑问；鲁组进组准备v1.3定义T/R/F/E四线，第二条研究线v1.1定义P(并发死锁)/O(对象一致性)双入口候选；与MASTERY_GATE.md v2.2/FOUR_PAPER_TRAINING_LOOP.md §9关系尚未核验，是否构成WORLD/FIELD↔七图融合既成答案需用户裁定；EX-01哈希异常(见交接档2026-09-05__edgeim-learning-package-additive-upgrade__pause-handoff.md §7)三文件均未提及仍是独立未决项]
- [ ] [topic:bridge-scan] **BR-16 · BR-15三件套之R线双入口素材落地+D2谱系补环（本轮实际产出）** [P1] [note:TASK-20260908-EXP窗产：①`papers_lu/DeadlockLockSegGraph-2021-JOS.pdf`(jos.org.cn官网直链拉取,sha256 514198a7...c670)补全D2谱系2021史环+建`15_DEADLOCK_JOS2021.md`/`15b_..._kg_critique.md`(与02/04对齐,§5判断本篇为04 SegLock方法学直系前身)；②`papers_lu/pending-r-track-20260908/`新建(R线P/O双入口方法学参考5篇+MANIFEST.md，鲁组署名与外部文献分放未混)；③Ground Truth/Fragility三篇两处历史缺口误判已排除(见MANIFEST.md脚注)；④EX-01哈希三值互异非本轮新发现——09-08早前会话已查出并落盘`HANDOFF_2026-09-08__ex01-hash-status-and-ccf-youbo-intake.md`(结论=待上报用户裁定,尚未执行)；本轮`0157b372...`复核结果与该档一致，确认"上报"这一步至今仍未做，本轮已正式转告用户；⑤MASTERY_GATE.md确认已是v2.2(09-06)非v2.1，BR-15疑问可销；FOUR_PAPER_TRAINING_LOOP.md §8/§9确认现行游标仍为MASTERY_GATE §4.2 Whole-Paper Diagnostic，三镜头未解锁，09-08三件套所述"Stage 3/cut课堂进度"与本仓训练包游标脱节，如实并存不调和]
- [ ] [topic:research-desk] **RD-3 · 工作台/科研台/考研插件参考批（社媒帖+用户自选链接，2026-09-18）** [P2] [note:TASK-20260918-002；用户贴社媒帖转述批(11项，含Research OS/Xove Dashboard/markwhen/Claudian/obsidian_math等)+自选确切链接批(考研1/工作台9/科研4)，明确要求存为工作台/科研台参考；已追加进progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md R13/R14(§7.8)，遵循该清单铁律不新开平行档；仅核身份未选型未安装]
- [ ] [topic:research-desk] **RD-4 · 工作台/科研台/考研插件参考机制层深查（R15，2026-09-18）** [P2] [note:TASK-20260918-004；承接RD-3，6批子代理并行把R13全11项+R14非重复13项+新增2项(共26个URL)升级到机制层核查(核心内容/工作流/能不能用得上，不预设槽位归类)，已追加进REFERENCE_NOTES_20260915.md §7.9；考研对比组(obsidian_math/Pkmer-Math/Math-And-English-Library/Lazy-Kaoyan-Library/已深查kaoyan)发现Lazy-Kaoyan-Library明确声明借鉴前两者笔记但自行独立加装AI+OCR+Dataview+Templater三段式工作流，与kaoyan的人工+Python+外部AI三段式为同一问题两种独立解法；仍不做借鉴/转化/隔离/接入/暂存五选一处置判断，未安装未选型]
- [ ] [topic:research-desk] **RD-5 · 是否新增"考研台"（架构问题，待用户拍板，2026-09-18）** [P1] [note:用户在派发TASK-20260918-004时提出"注意现在我还想新增一个考研台"，属于全新未拍板的架构决策点，与已有的two-desks-purpose-redefinition-proposal.md（09-17，学习台/科研台/工作台槽位重定义提案，PROPOSED未采纳）是两个独立待决问题——一个问"槽位怎么重定义"，一个问"要不要加第四个槽位"；RD-4的§7.9.1考研对比表（obsidian_math/Pkmer-Math/Math-And-English-Library/Lazy-Kaoyan-Library/kaoyan五项横向比较）可作决策输入但不代替拍板；不由AI代为判断是否新增]
- [ ] [topic:research-desk] **RD-1 · 科研台导航首版与后续解耦建设** [P1] [note:TASK-20260908-002；2026-09-10用户确认B/A/B/B/C：Markdown导航+结构化目录+本地网页，首页继续优先，全量登记位置/活跃深整理，版本/核验日期/范围分列，指导库来源/场景双入口；导航首版已由TASK-20260910-001完成：独立目录、Markdown CURRENT、2432条结构化资产、本地搜索网页、工作簿18表/27媒体/29放置、pengsida来源/场景双入口；5单测+链接检查+实现者浏览器20/20通过，独立浏览器复核PARTIAL，用户使用验收仍开；完整Graph/Canvas、工作台闭环、独立Git仓、TaskQuay和服务器为后续；恢复=/mnt/d/MyResearch/research-desk/HANDOFF.md]
- [ ] [topic:research-desk] **RD-2 · 科研台探索发展层重建（Astra 诊断，2026-09-10）** [note:2026-09-12 TASK-20260912-001：纠错本与能力增长完整讨论已保存=progress/decisions/2026-09-12__learning__correction-notebooks-and-growth-v0.1.md；评价分开/材料共用/全过程可追溯；下一步两条真实案例走查，未改冻结合同或应用] [note:2026-09-12 TASK-20260912-002：v0.3与Astra v0.1比较就绪度评估=progress/decisions/2026-09-12__research__knowledge-network-v0.3-vs-astra-comparison-readiness.md；Astra §7九问六到七条已独立收敛，两到三条真分歧(轻量观察拆类型/v0.3场景A缺反转测试/两稿反例严谨度不对等)未拍板；不代为拍板第7节最终版] [note:2026-09-11 TASK-20260911-007：kaoyan参考按用户纠偏收口为结构提炼，入口=progress/audits/2026/09/2026-09-11__kaoyan-deep-review/STRUCTURE.md；后续抓层次与连接，数据验算停止；未改施工合同或应用] [note:2026-09-11 TASK-20260911-006：Astra路线三场景已写=progress/decisions/2026-09-11__research__knowledge-network-scenarios-astra-v0.1.md；已见Fable摘要，未打开对方场景稿正文，非严格盲审；下一步由Fable按该稿第7节比较，未改代码或施工合同。] [P1] [note:Astra窗核对08-12科研地图/08-13人机恋调研原始任务书后指出：当前RD-1导航实现只做已有文件查找，压缩掉了地图最初要求的"发现/探索/发展问题"层；已用registry抽查独立验证——curation.json(35条)/guidance.json(9条)/proposals.json(3条)均无字段承载"缺口/候选问题/新发现如何修正理解"；引用核实：08-12用户原话见decisions/2026-08-12__maintenance__user-statement-archive-1.md:28（流派/脉络/团队动向/拒稿原因/taste）、四份任务书agent-briefs/{modules,channels,academic,deep-dive}-briefs.md、回流协议companion-survey/MAINTENANCE.md §8；Astra提出的"循环图对应architecture-overview.md:28已设计"一句为二次归纳非逐字引用，已在窗口内更正；旧任务书"可发表gap"要求过强判断，改判需求=候选缺口+待验证条件（沿用SEARCH_BOUNDARY.md纪律：只能说指定日期/渠道/查询范围内未发现，不宣布领域空白）；下一步待用户拍板修复深度与范围] [note:Codex本轮已按用户“先存档？”暂停：讨论及证据=progress/decisions/2026-09-10__research__map-learning-redesign-review-archive.md；恢复=progress/handoff/2026-09-10__map-learning-redesign__pause-handoff.md；下一步先还原四条使用过程与原需求追踪表，再定最小整改范围；新增多尺度Map/连接生长/注意力维护/学习覆盖等均待审，未改代码。] [note:2026-09-10 再核：用户所贴细化提案逐句对应review-archive.md §5-10，系同一Codex会话(01a08005)提案的展开，非独立来源；用户重申"F基础线独立于论文进度"与"探索可纯兴趣不必转研究任务"须保留（v0.3§4已含）+"研究入口不应只是失败→缺口"须修（定位旧问题=v0.3§5 failure→evidence→prior-art→contribution四检查，提案已修，另FUSION_ROADMAP.md旧方法论亦偏此模式）；独立核实发现：F基础线在两份现行学习文档(learning/Learning–Research OS v0.1 FROZEN/MASTERY_GATE.md v2.2)均无独立实体，只有EdgeIM单论文机制+已归档的Jiang时代占位(00_MASTER_INDEX.md)，四线并行设计尚未落地对象；下一步仍待用户拍板范围] [note:2026-09-10第二次落盘：详档第13-21节保存用户确认的自由捕获后整理、工业线独立与学术联动、横纵脉络/goal-item关联、草稿纸/失败/转向过程；人机恋为搜索方法范例。恢复先做视角遗漏审查与功能联动图；来源=decisions/2026-09-10__research__workflow-notes-and-coe-source-intake.md，09-01碎碎念涉及自身工作流优化；Chain-of-Experience arXiv:2608.18027定向核查/拆解待做，文章数字/Manus来源/dspark身份未核，未改上下文策略或代码。] [note:2026-09-10恢复设计：首批开发合同v0.1与rd2-sol-luna-execution-packets.md已写；合同/执行包位于progress/decisions/。总并发≤2，Astra以规划/取舍/最终审阅为主，琐事交Sol/Luna；下一步E04需求对账及E03本地适配差异，再E05低保真；桌面主入口与B1/B2施工范围待审。应用未改，旧暂停为历史状态。] [note:2026-09-10 v0.2施工包已写（三页/27项需求/演示对象/数据接口/分包验收/工作簿18表用途）；用户最新要求暂停并给Sol方案落盘。入口=progress/decisions/rd2-first-build-v0.2/SOL_START_HERE.md；第一包WB-1仅Sheet1/18真实来源文档，后续桌面/存储/3D待审。工作簿已登记抽取，不等于全部语义融合或已用；应用未改，PAUSED/RECOVERABLE。] [note:2026-09-10再核（回执核对）：WB-1实际有两份独立交付——sol-delivery/wb1-20260910-sol/（18:48，身份未知）与wb1-20260910-sol-xhigh/（19:04，独立执行，明确声明未读取/依赖前者正文）；二者核心结论收敛一致（Sheet1真实图片锚点Q26:AF65、Sheet18在OOXML层面无drawing关系仅A17/A45/A53/A72等为纯文字占位、两资产adapted=false/used=false）；后者另做42单元格逐格MATCH=True核验+check-links工具实跑(ok=true/2432 assets/0 errors)+git status实查；两份均未注册进外层CROSSWINDOW.md（该表本身要求开工登记，此次缺登）；MAS仓git status显示40+已改/60+未跟踪文件积压09-04至今未reconcile，与本轮SessionStart hook判定的CONTEXT_RECOVERY_STATUS=UNVERIFIED互相印证；下一步：两份WB-1交付需人工比对取舍或明确并存，CROSSWINDOW补登记，MAS未提交积压需用户决定是否/何时清理。] [note:2026-09-11 P1实施收口：Sol实施与主控独立复跑均通过，P1 120/120、Legacy 25/25、后端17/17；最终回执=progress/decisions/three-desks-v0.1/sol-delivery/p1-20260910-sol/RECEIPT.md，当前入口=progress/decisions/three-desks-v0.1/NEXT_STEP.md。已开127.0.0.1:8883全新用户验收沙盒，原配置/工作簿/registry/真实SQLite未改；下一步只做用户实际使用验收，记录找不到/不自然/术语不清/预期不同。commit/push/deploy、P2/P3/B2/3D、完整Map/画布/学习模型仍开放，不自动推进。] [note:2026-09-11施工总审后已落盘v0.3：入口=progress/decisions/rd2-construction-v0.3/SOL_START_HERE.md；用户授权交Sol连续执行第一波C00-C03（维护与版本基线、自然资料入口、关系/提案、全局-专题-工作区往返），C03交付即停并保留用户体验门；C04-C07及画布/3D/工作台/TaskQuay/版本化/部署另包。手册编制TASK-20260911-001，应用未在编制窗口修改。] [note:2026-09-11第一波实施与主控验收：TASK-20260911-002 已完成 C00-C03 技术交付；接收主控独立复跑 unittest 21/21、隔离 check-links 2432 assets/0 errors/0 warnings、C03 Playwright 17/17，状态 CONTROLLER-ACCEPTED / USER-ACCEPTANCE-OPEN。入口=progress/decisions/rd2-construction-v0.3/sol-delivery/20260911-sol-c03-113925/CONTROLLER_REVIEW.md；AC03-12 等用户实际小过程，C04-C07与X-*未启动；用户已授权提交MAS文档与证据，应用源码仍未独立版本化，未push/deploy。] [note:2026-09-11用户实际体验未签USER-ACCEPTED，状态保持CONTROLLER-ACCEPTED/USER-ACCEPTANCE-OPEN；重新打开AC03-04/10并报告非工作簿来源undefined/永久加载。TASK-20260911-003限定返修前三项，控制器复验22/22 unittest、2432/0/0、C03 Playwright 22/22、用户复现快照7/7、当前8873只读烟测8/8；AC03-04/10待用户复验，AC03-12开放。问题4=2432资产入口截断前300项且无检索；问题5=保存缺提交态/明确回执且快速重复点击可重复创建，均待下一次C03范围；C04-C07未启动。] [note:TASK-20260911-004 知识网络架构整合v0.2：对齐Map八层/七图/指导库A-F六层三份此前未对账的分层清单，工业维度确认为三重独立发现的真实缺口(节点类型/关系白名单/七图均无)；新增dimension_refs(学术/工业/团队/方法/问题/领域，与指导库既有layer字段刻意区分避免P1/P2式命名碰撞)、Relation.growth_mode(depth_dig/breadth_scan/cross_pollination，对应个人深挖菌丝网原始构想[9-6 TASK-20260906-004]与工业广度扫描两种不同判据)、Relation.maturity(emerging/established，落实菌丝网=科研地图两态说)；Competency/Identity&Fit/Trajectory重定性为个人投影非世界维度；时间维度、cross_pollination是否入白名单、maturity升级判据、团队维度是否纳工业界人物均列为待用户裁定的开放决策点；入口=progress/decisions/2026-09-11__research__knowledge-network-architecture-v0.2.md；仅设计契约文字，未改CONTRACTS.md/DATA_CONTRACT.md正文、未改C00-C03代码。] [note:TASK-20260911-005 三场景走查（独立版，用户拍板"两边各自独立画，你来对比"）：论文深挖撞工业应用/工业动向倒查方法谱系反哺基础学习/学习失败调用指导再回研究问题；已自我修正v0.2三处（工业缺口据TRACEABILITY.md R02原文改判"需求已有未具体化"非三重真空；maturity字段本稿不用改用既有state+basis_refs；growth_mode不焊在Relation上改挂Attempt活动记录）；具体发现relation_type白名单缺"公司-产品"与"活动引用指导"两类、SourceRef anchor不覆盖网页来源；入口=progress/decisions/2026-09-11__research__knowledge-network-architecture-v0.3-scenarios.md；仍设计契约文字，未改代码，另一路对照版本待后续任务对比。]
- [ ] [topic:research-map] **BR-4 · 科研地图 W1-W6 波次推进（总纲：research/map/README.md）** [P1]
  - **已完成**：W1 鲁侧 / W2 孙侧 / W3 L0+L2 统一总图（`GRAND_MAP.md` v1）/ W4 ICLR 评审元分析 / **W5 v0 schema+解析器+交互 HTML（TASK-20260813-018）** / W6 craft 手册（含 D 信息/风向/taste 专档）
  - **剩余**：W5 v1 补缺设计已收口（TASK-20260813-023，4/4 齐 + `W5_V1_PLAN.md`，实施见 BR-11）；W4 2027-01 再增量 ICLR 2027 评审
  - **验收**：每波次产出落对应子目录 + CHANGELOG 增量行 + 波次完成时新监测对象追加进维护 runbook §2
  - **优先级**：高

- [x] [topic:bridge-scan] **BR-5 · 方向相关开源项目 + 工具型 Paper 版图（鲁组侧重 · 孙组远期占位）** [P1] [2026-08-13~2026-09-15]
  - **范围五簇**：① process mining × LLM/agent（PM4Py 生态与 agent trace 分析）② conformance checking 工具与 agent 行为验证 ③ PN 建模/验证开源工具（含 SBPN/SBTPN 有无公开实现）④ LLM Agent 安全治理框架（EvoAgent 同类：监控/guardrails/可观测性）⑤ agent 传播风险实现（AgentWorm 系，接 bridge_scan T1）；孙组接轨（形式化验证 × LLM）只做占位小节
  - **与 BR-4 边界**：BR-4 = 学术论文版图；本条 = 开源实现层 + 带代码 paper 增量，纯文献不重复
  - **产物**：`research/map/oss_landscape/`（任务书 KICKOFF.md 已备 · 清单表 + SYNTHESIS + external 收纳建议）
  - **验收**：五簇各 ≥5 条目（URL/活跃度/接驳点/三类定性：可用工具-竞品-参考实现）+ external 收纳建议清单 + `research/map/CHANGELOG.md` 增量行
  - **优先级**：高（9 月邮件前完成，支撑"我了解你们的工具生态"话术）
  - **完成**：2026-08-12 · `TASK-20260812-019`；C1-C5 各 ≥5 条、C6 5 条占位、`SYNTHESIS.md`/external Top 5/邮件话术均落盘，E1 缺陷审计后收口

- [ ] [topic:bridge-scan] **BR-6 · 开源版图 E2 验证 + 增量续研入口（BR-5 后继，不重扫）** [P1]
  - **任务书（历史起点）**：`research/map/oss_landscape/E2_KICKOFF.md`
  - **现行入口**：`progress/handoff/2026-08-12__research__oss-landscape-final-closeout.md`
  - **后续 Plan / Agent 分工**：`research/map/oss_landscape/e2/NEXT_PLAN.md`
  - **模式 A（推荐）**：strobe+ABM+OTel schema 对标 / cpn-py+Coverability 最小 PN / RiskLab 静态轨迹映射；clone 与运行须用户单独放行
  - **模式 B（无需放行）**：只做 SBPN/SBTPN、ClawWorm/AgentWorm、主要竞品与 2026 带代码论文的增量查漏，写 `e2/DELTA.md`
  - **验收**：至少一个外部 trace 被当前 PM4Py 管线真实消费，或形成带 commit/命令/退出码的 NO-GO；PN 对普通图无增量则停止扩展
  - **优先级**：高（可现在另开窗口；不阻塞本窗收尾）
  - **进度**：Phase 0（`TASK-20260812-028`）与 Wave 1A（`TASK-20260812-033`）已完成；机械 ABM→PM4Py E2 PASS，Schema PATCH / strobe XES NO-GO / PN E1 NOT TESTED；Wave 1B 等新授权
  - **旁路增量（TASK-20260813-018 B1）**：cpn-py 结构、pgmpy noisy-OR/RCA、Sirio STPN 三个最小参考实验 E2 PASS；这不等于 SBPN/SBTPN 完整算法已复现，完整代码仍未发现

### bridge 收口窗遗留（8-13 晚 · TASK-20260813-021 系登记）

> **主档**：`progress/handoff/2026-08-13__bridge-map-fusion__final-closeout.md`（bridge 线现行唯一入口）
> **证据**：`progress/audits/2026/08/2026-08-13__audit__bridge-7agent-verification/` + `research/map/proposals/COLLISION_AUDIT_V2_20260813.md` + `research/map/SEARCH_BOUNDARY.md`

- [ ] [topic:bridge-scan] **BR-7 · OpenReview 5 条隐藏 ID 人工核验（唯一可能改变 T2 威胁评估的未知量）** [P1] [user-action:需登录态浏览器]
  - **对象**：`openreview.net/forum?id=` + fSN4yfqIiA / sjA1RIORpY / I8MxUcuaIG / b2oARovfki / QqoaApYzgQ（5 条 2025 在审隐藏标题，清单见证据档 05 号回执 b 节末）
  - **验收**：5 条判定（无关/近邻/直接竞品）回填 `COLLISION_AUDIT_V2` §3 watchlist；若现直接竞品立即触发 T2 重裁
  - **优先级**：高

- [ ] [topic:bridge-scan] **BR-8 · Semantic Scholar API key 申请 + S2 面 6 条查询复扫** [P2] [user-action:申请（免费，官网表单）→AI 复扫]
  - **现状**：8-13 实测无 key 时 24/24 全 429；全仓检索确认没有已存 key（勿与 8-11"爬虫 .env 历史"、pending 的 TAVILY_API_KEY 混淆）
  - **验收**：key 到手（放本机环境变量，禁入 git）→ 复扫 `SEARCH_BOUNDARY.md` §A S2 行的 6 条查询并回写状态
  - **优先级**：中

- [ ] [topic:bridge-scan] **BR-9 · SAP ABM conformance 口径冲突重裁（T2 引用前置）** [P1]
  - **冲突**：039 波判"实做 discovery+conformance+缺失/插入偏差" vs 深挖波 A5 全文核读判"纯描述性、无 conformance/alignment"（登记见 `COLLISION_AUDIT_V2` #16 冲突框）
  - **动作**：重开 arXiv:2606.20669 原文逐节裁决（疑为"偏差挖掘 vs alignment 级检查"的口径之差）；裁决前两种表述都不得单方采信
  - **验收**：审计 v2 #16 冲突框关闭 + T2 提案 §2/§7 ABM 行按裁决定稿
  - **优先级**：高（阻塞 T2 写作的对比基线措辞）

- [ ] [topic:bridge-scan] **BR-10 · R0 修复三波实施（9 findings 落地）** [P1] [blocked:DEC-R0-IMPL-GO + EvoAgent 009/024 收口 commit]
  - **依据**：`research/experiments/t2_r0_repair_plans_20260813/`（7 设计 + SYNTHESIS + IMPLEMENTATION_ORDER，SHA256 已封）
  - **顺序**：W1（E1 稳定 ID ∥ M1 manifest 门）→ W2（E2-E5 串行 ∥ M2/M3）→ W3（M4 独立 oracle → M5 OOV 信封，不可倒置）；每波末双仓基线 43=42+1
  - **两个实施期陷阱（设计已标注）**：负控制必须同时校验 stderr 前缀（三种错误共用 rc=2）；历史 EX-03 full-log TBR=1.0 已判不可引用
  - **验收**：回归矩阵五行全绿 + Gate R0 通过 → 解锁"窗 1"三类偏差注入实验
  - **优先级**：高（T2 实验主链前置）

- [ ] [topic:research-map] **BR-11 · W5 v1 实施 + data/ 三缺陷修复（移交 B4 写区归属方）** [P2] [owner:深挖波汇合裁定]
  - **实施优先级**（`W5_V1_PLAN.md` §2）：P1 cells.yaml（119 格，空白论断载体）→ P2 WATCHLIST.md + radar_hit（下次月度雷达要用）→ P3 reconciliation/ 对账层 → P4 explorer 邻域图（cytoscape.js 内联）
  - **顺带修三缺陷**（W5-4 路实测）：Resilience/AgentHarm 论文实体跨 ID 分裂 ×2、`team-w2c-meta` 括号词元 bug 零边、别名表"代码 16 vs 档案 17"漂移
  - **验收**：实施后重跑 `map_to_yaml.py --check` 幂等 PASS；data/ 生成物中旧口径（"整片无人占/13 条零命中"残留于 quicklooks/topics yaml）随重生成自然消失
  - **优先级**：中

- [ ] [topic:bridge-scan] **BR-12 · 未搜面 12 项补扫（并入 BR-3 下次月度雷达执行）** [P2] [note:例行扩容]
  - **队列**（`SEARCH_BOUNDARY.md` §B，按威胁排序）：OpenReview forum 级（=BR-7）＞ S2 复扫（=BR-8）＞ GitHub code search（需 PAT）＞ BPM/ICPM/AAMAS 2026 全量接收列表 ＞ Google Scholar 被引反查（2003.07291）＞ CNKI（需校园网）＞ Zenodo AXIOM 日期 ＞ HF 词族补扫 ＞ NeurIPS/ICML/ICLR 2026 workshop 列表 ＞ GitLab/Bitbucket 面 ＞ 鲁法明学校主页复访
  - **纪律**：执行按 radar §6 三重过滤 SOP + 噪声源表；结果回写 SEARCH_BOUNDARY 对应行
  - **优先级**：中

- [ ] [topic:outreach] **OE-3 · MAESTRO 本地副本获取** [P3]
  - **现状**：8-13 实测 external/ 全目录零命中，无本地副本（ABM/strobe/cpn-py 均已在）
  - **验收**：external/ 下出现 MAESTRO 固定 commit shallow clone 并登记 RE-30 外部工具账本
  - **优先级**：低

### 深挖训练系统（8-12 立 · learning/training/）

> **总纲**：`learning/training/00_SYSTEM.md`（用户四拍板：按资产混合训练模式 · RA-27/16 全训练改造 · 每周 3-4 个 90 分钟块 · 死线优先降级）
> **与 BR-4 W6 的关系**：本系统 = 动手实操训练（你做题 + AI 出题/陪练/批改）；W6 craft 手册 = 文档沉淀。训练铸的方法论卡（`learning/training/methodology/`）是 W6 的输入源，两者互补不重复建设。

- [ ] [topic:deepdive-training] **TR-1 · 深挖训练首轮（4 训练包 · 约 15 个练习 · 4-6 周）** [P1] [2026-08-13~2026-09-30]
  - **价值点**：五资产深挖从"Agent 代做"转为"练你的肌肉"——盲 review / 判断代码 work / 故障注入 debug / PN 形式化建模 / 调研画像；方法论卡拉动式沉淀
  - **执行**：按 `00_SYSTEM.md` §6 周计划（W1-W2 ra28 样板包 → W3 ra26 toy → W4 ra30 形式化 → W5 ra2716 贴 8-25 BR-1）；进度唯一真相 = `learning/training/LEDGER.md`
  - **验收**：四包毕业判据（`00_SYSTEM.md` §5 表）达标；衔接产出转正（PM4Py toy 报告 → 邮件素材 · OE-1 素材包 · SBPN 200 字段）
  - **阻塞**：仅 ra26 EX-01 的运行路径等 `DEC-REUSE-ROLLOUT-E3`（静态路径不阻塞，可先开工）
  - **ra30 当前断点**：赛前就绪、训练本体 0%；严格按 EX-01→02→03，下一步由用户完成 `EX-01/EX-01_批判精读.md`
  - **ra30 EX-04 硬门禁**：至少一篇目标 SBPN 论文已有真实精读产物，并记录论文文件与定义编号；8 月六篇鲁组论文（SBPN/SBTPN/UAF/EdgeIM/Healthcare/MHP）是更大的 research 阅读计划，不要求六篇全部完成才开 EX-04
  - **文献状态（2026-08-13 复核）**：`research/papers_lu/` 的 5 个 OA PDF 本体曾缺失，现已从 MANIFEST 官方 URL 恢复且 SHA-256 5/5 匹配；SBPN 2024 Inf. Sci. / EdgeIM / MHP 仍为付费墙未取得。EX-04 保持锁定；若改为 SBTPN 必须用户明确拍板并先同步改题
  - **优先级**：高
  - **done 类型**：verify-done（按 LEDGER + 毕业判据核）

### Sun 方向归档收尾

- [ ] [topic:sun-archive] **SA-1 · 移动 `research/sun/` 下所有文件到 `_archive/research/sun/legacy-2026-Q3/`**
  - **价值点**：清空 research/sun/ 让 phase1 工作区干净，为新论文/新方向腾地方
  - **验收**：`git mv` 成功 + `_archive/research/sun/legacy-2026-Q3/MANIFEST.md` 写完
  - **阻塞**：无（agent A 已完成 1091 文件移动）
  - **注记**：2026-08-12 验收：物理移动疑似已发生（`_archive/research/sun/legacy-2026-Q3` 内容已在）但无 task_log 证据，状态待核
  - **优先级**：中（归档动作，非核心）
  - **done 类型**：commit-done

- [ ] [topic:sun-archive] **SA-2 · 写 MANIFEST 索引**
  - **价值点**：让后人能追溯归档来源（哪个文件、保留原因、对应阶段）
  - **验收**：`MANIFEST.md` 列出每个文件 + 1-2 句摘要 + 原 commit hash
  - **阻塞**：无
  - **优先级**：中
  - **done 类型**：commit-done

- [ ] [topic:sun-archive] **SA-3 · 更新 `research/sun/` 为空骨架**
  - **价值点**：保留目录占位，等新论文/新方向启动
  - **验收**：`research/sun/` 只留 `README.md`（标 "Status: archived, awaiting new direction"）+ `.gitkeep`
  - **阻塞**：无
  - **优先级**：中
  - **done 类型**：commit-done

- [ ] [topic:sun-archive] **SA-4 · 写决策档** [blocked:等 SA-1~3]
  - **价值点**：解释为什么归档、新方向待选、未来重启条件
  - **验收**：`progress/decisions/2026-07-27__maintenance/sun-archive-post-action.md` 落档（已存在 sun-direction-archive-2026-Q3.md 决策档，本件指收尾后的 post-action 补充）
  - **阻塞**：等 SA-1~3 完成才能写
  - **优先级**：中
  - **done 类型**：commit-done

- [ ] [topic:sun-archive] **SA-5 · 更新 STATUS.md "Current phase"**
  - **价值点**：把 "PAUSED" 改为 "ARCHIVED"，明确科研主线状态
  - **验收**：`progress/STATUS.md` 的 "Current phase" 字段含 "ARCHIVED"
  - **阻塞**：等 SA-4 决策档落地
  - **注记**：2026-08-12 验收回改：无 INDEX 完成证据（SA-5 前置 SA-4 未完成）
  - **优先级**：中
  - **done 类型**：commit-done

- [ ] [topic:sun-archive] **SA-6 · 更新 INDEX.md**
  - **价值点**：旧 `task #10 (TASK-20260726-001)` 链接到新归档
  - **验收**：`progress/task_logs/INDEX.md` 含归档链接
  - **阻塞**：无
  - **注记**：2026-08-12 验收回改：无 INDEX 完成证据（SA-5 前置 SA-4 未完成）
  - **优先级**：中
  - **done 类型**：commit-done

> **告一段落信号**：SA-1..SA-6 全部完成 + STATUS.md 标 "ARCHIVED"。

### 孙线重审波收口（issue4-4B · 2026-08-24 关窗）

- [ ] [topic:sun-review] **SR-Q · 孙线 28 篇重审拍板队列（README §⑤ A-G 共 19 项，只列不执行）**
  - **价值点**：四波重审+终审的全部用户决策点集中于此——梯队升降×4（AgentWorm→T1/Roadmap→T1 入口级/ProbGuard→T2/Salami→T3 候补）、存量 P0×2（S3-A02 venue 行污染 9 月套磁链、PG-A5 arXiv v2 漂移无 owner）、复现实验×4、证据冲突×2（VOW 归属等）、流程制度×3（含 F-R34-F1 402 兜底制度化）、话术纪律×4
  - **验收**：逐条或打包拍板后另开维护窗落地（被审件哈希已钉死，禁即时改）
  - **阻塞**：无（等用户拍板）
  - **入口**：`research/sun/phase1/papers/_review_20260815/README.md` §⑤；TASK-20260824-008 task log
  - **优先级**：高（S3-A02 直接污染套磁材料引用链）
  - **done 类型**：拍板-done

### MCM 2026 已完成验证（历史索引）

> **权威记录**：`task_logs/INDEX.md` 中 `TASK-20260802-003` = done，6 条全升 HIGH。
> **分布快照**：MV 验证完成时 `HIGH=18, MEDIUM=18, OTHER=0, total=36`；F037-F044 后当前 fact dump 为 `HIGH=26, MEDIUM=18, total=44`。
> **更正档**：`progress/decisions/2026-08-09__research__mv-1-5-already-done.md`

- [x] [topic:mcm-recheck] **MV-1 · F002a · r_hat 子集均值口径已复核** ✅ 8-2
  - **结果**：三个口径必须分开：`r_hat<1.5` 子集均值 **1.0167**；当前 2686 行结果的 `r_hat<10` valid 子集均值 **1.1657**；论文报告 **1.0314**。旧 task log 曾把 `<10` 筛选结果写成 1.0314，当前 fact dump notes 已用实测 1.1657 覆盖；F004 仍需解释该口径差异。
  - **confidence**：MEDIUM → **HIGH** · 证据见当前 fact dump F002a/F002b notes

- [x] [topic:mcm-recheck] **MV-2 · F002d · C++ 内核 final_res.r_hat = max_r** ✅ 8-2
  - **结果**：`final_res.r_hat = max_r` 单一标量,配合 F002a 串证 CSV 端一对一
  - **confidence**：MEDIUM → **HIGH** · 源 §1767+1777

- [x] [topic:mcm-recheck] **MV-3 · F010 · 配置改动叠加** ✅ 8-2
  - **结果**：4 项改动叠加（1M→100K · 0.2→0.5 · 0.02→0.05 · 10→20）→ R̂ 1.016→**1.1657**, Fidelity 92.19%→**84.3%**
  - **含义**：M 奖确实受"配档退步"影响 —— 9 月对外叙述需诚实处理
  - **confidence**：MEDIUM → **HIGH** · 源 §1844-1852

- [x] [topic:mcm-recheck] **MV-4 · F016 · cpp_kernel 0.65s 23 核** ✅ 8-2
  - **结果**：C++ MH + 23 核 OpenMP + commit `36fd853` + 0.65s 全季反演（22,133→22,788）—— **真实,可讲**
  - **confidence**：MEDIUM → **HIGH** · 源 §60-71 + §1822

- [x] [topic:mcm-recheck] **MV-5 · F019 · DAW 寻优参数** ✅ 8-2
  - **结果**：DAW 参数对照表 —— default `10.0/0.6` vs 论文 `13.37/0.41`
  - **confidence**：MEDIUM → **HIGH** · 源 §646-680

- [x] [topic:mcm-recheck] **F030 · （第 6 条）SNR 是否包装词** ✅ 8-2 · **结论反转**
  - **结果**：SNR 在 paper Page 14 §4.2（`2622651_extracted.md:354`）有完整数学定义 + SNR Gain **+18.4%** 真实 metric
  - **原判误**：24 KB Claude 初稿 §B5 标其为"包装词" —— **误判,已摘除**
  - **confidence**：MEDIUM → **HIGH**

### MCM26 学习系统与差分复审

- [ ] [topic:mcm-learning] **ML-1 · 完成 MCM26 首个纵向学习切片（F004 · R-hat 三口径）**
  - **设计档**：`progress/decisions/2026-08-09__research__mcm26-learning-system-design.md`
  - **专题入口**：`progress/mcm26/README.md`
  - **目标**：把问题定义、代码计算、CSV 口径、论文叙述、失败模式与迁移练习串成一个可自测案例
  - **前置**：获得 `/mnt/d/Code/MCM_2026` 源码审计授权，并重新定位当前 `file:line`
  - **验收**：F004 有当前源码坐标、三方对齐、分类结论和自测题；不重复 MV-1~5
  - **状态**：`[需验证]`
  - **优先级**：高

- [ ] [topic:mcm-learning] **ML-2 · 建立 MCM26 后台证据控制层（来源注册 + 口径主账 + 差分复审）** [P0]
  - **目标**：在实际使用时建立 `progress/mcm26/control/`，只记录当前状态和证据关系，不复制历史原档
  - **前置**：ML-1 纵向切片暴露出真实字段需求后再建，避免空目录和过度搭框架
  - **验收**：每个数字有证据等级；历史审计坐标与当前源码坐标分栏；新增待办前回查 `task_logs/INDEX.md`
  - **状态**：`[需验证]`
  - **优先级**：中

### MCM26 五轨审计（review-v2）

> **主档**：`progress/audits/2026/08/mcm26-five-track/`；交接档 `progress/handoff/2026-08-12__mcm26__review-v2-scaffold-paused-handoff.md`。
> **推进序**：FT-P1（R1 续脚手架）→ FT-B ∥ FT-E → Gate。

- [x] [topic:mcm-review-v2] **FT-P1 · 续完五轨脚手架** [P1]
  - **验收**：`REVIEW_HOME.md` 存在且 `validate.py` 对种子表 PASS
  - **完成（2026-08-12）**：REVIEW_HOME/validate/RUNLOG/tracks README 全落地，validate 首跑 exit 0（0 ERROR / 9 WARN 均为 legacy_ref 预期提示）；记录 `progress/task_logs/2026/08/2026-08-12__research__mcm-five-track-scaffold-r0-r1.md`（TASK-20260812-006）
  - **指针**：`progress/audits/2026/08/mcm26-five-track/` + `progress/handoff/2026-08-12__mcm26__review-v2-scaffold-paused-handoff.md`
  - **优先级**：高（FT-B / FT-E 的前置）

- [x] [topic:mcm-review-v2] **FT-B · Track B 六头条数字溯源** [P1]
  - **验收**：`METRICS.csv` M001–M006 坐标/复算/verdict 填满且诚实（禁 E0→CONFIRMED）
  - **完成（2026-08-12）**：R2 收口 + R3-Gate 裁决 PASS——M001-M003 mismatch@E2（README 三头条为孤值誊写失真，F031 CONFIRMED@E2）、M004 pending@E2（inf 折叠不可静态回溯）、M005/M006 computed@E2 保持；记录 `progress/task_logs/2026/08/2026-08-12__research__mcm-five-track-trackbe-gate.md`（TASK-20260812-018）
  - **优先级**：高

- [x] [topic:mcm-review-v2] **FT-E · Track E 双入口可达性重计** [P2]
  - **验收**：`REACHABILITY.csv` 有实质行 + 白名单草稿
  - **完成（2026-08-12）**：R2 收口 + R3-Gate 裁决 PASS——REACHABILITY 59 行（44 confirmed / 15 白名单候选 pending）；死代码新口径毛 3395 / 净可删 1876 vs 历史 1907，M010 回填 mismatch@E2；白名单草稿 `WHITELIST_DRAFT.md` 落盘；记录同 FT-B（TASK-20260812-018）
  - **优先级**：中

- [x] [topic:mcm-review-v2] **FT-A · Track A F004-F007 三方对齐** [P1]
  - **验收**：F004-F007 四行终判（≥E2 或如实 pending）+ 证据包
  - **完成（2026-08-12 W4）**：四行全 CONFIRMED@E2/closed——F004 论文 R̂ 口径未披露过滤且与三桶全不符、F005 论文 53.4 溯源成功（双口径并存未披露）、F006 假图实锤（Week6 硬编码 vs 实算 Week1）、F007 论文方向与数据相反；另升 F034（92% vs 84.44%）；记录 `progress/task_logs/2026/08/2026-08-12__research__mcm-five-track-w4-a-c.md`（TASK-20260812-038）
  - **优先级**：高

- [x] [topic:mcm-review-v2] **FT-C · Track C 论文图表取证** [P1]
  - **验收**：`FIGURES.csv` 实质行（classification+sha256+repro_cmd），假图指控有物证链
  - **完成（2026-08-12 W4）**：论文 16 图表全登记——2 fabricated（FIG-08/FIG-14 硬编码实锤）/ 6 suspect（vis 死区）/ 6 real / 2 unverifiable；classification 枚举 SCHEMA 定稿；记录同 FT-A（TASK-20260812-038）
  - **优先级**：高

- [x] [topic:mcm-review-v2] **FT-D · Track D N1-N8 静默正确性** [P2] [done:2026-08-13]
  - **验收**：N1-N8 复现证据 + 影响半径（污染 metric_id 清单）
  - **完成（2026-08-13 recovery + Gate2）**：N1-N8 全部 closed（7×CONFIRMED@E3 + 1×CONFIRMED@E2）；污染 metric=M001/M002/M003/M004/M005/M007/M008/M009；`TRACKD_EVIDENCE.md` + 13 行 `RUNLOG.D.jsonl` + 恢复工具齐；隔离副本已删、原仓 clean；Gate2 Overall=`PASS (audit-complete)`。记录 `TASK-20260813-003`，承接中间态 `TASK-20260812-049`。

- [x] [topic:mcm-review-v2] **FT-FIX · MCM README 三孤值修复** [P2]
  - **验收**：README:27-29 三数字改为实测口径（或双口径注记）；SNAPSHOT 记增量重定位
  - **完成（2026-08-12 W5）**：MCM 仓 commit `ceff63f`（84.1→84.3 / 1.6111→1.24 / 26.5→27.1 双口径注记；:30 随 M004 pending 未动；禁 push）；留痕 = 审计根 `FIX_RECORD.md` + SNAPSHOT 增量重定位段 + F031 notes；登记 `TASK-20260812-049`

### W1b / W2-W6 修正链

> **2026-08-13 Gate2 勘误**：原迁移链把“事实审计”和“源码/论文修复”混在一起。事实审计已由五轨完成；以下未勾项均是新的维护或输出项目，受 `DEC-MCM-SOURCE-FIX` / `DEC-MCM-ERRATA` / `DEC-MCM-DEADCODE` 约束，不得无授权自动开工。

- [x] [topic:mcm-recheck] **W1b · 验 4 件矛盾事实 F004-F007** [done:2026-08-12]
  - **完成**：Track A 已将 F004-F007 全部终判为 CONFIRMED@E2/closed，并新增 F034；见 `TASK-20260812-038`。原 8-10/11 停摆记录保留为首次尝试历史，不代表当前未完成。
  - **停摆记录**：`progress/incidents/2026/08/2026-08-11__w1b-ten-agent-task0-stall.md`（8-10/11 · Task 0 卡死 · 零产物）
- [ ] [topic:mcm-recheck] **W2-W3 · 修 Rank flip_rate 方向反转** [P0] [blocked:DEC-MCM-SOURCE-FIX]
  - **已审计**：F007 已 CONFIRMED@E2；本项只表示是否修改源码/论文叙事，不再重复事实核验。
- [ ] [topic:mcm-recheck] **W3 · 修 Bobby Bones Week 6 vs Week 1 叙述** [blocked:DEC-MCM-SOURCE-FIX;DEC-MCM-ERRATA]
  - **已审计**：F006/N4 已确认 Week 6 硬编码与产物 Week 1 冲突。
- [ ] [topic:mcm-recheck] **W4 · 修 Fairness Lift 口径（53.4% vs 27.15%）** [blocked:DEC-MCM-SOURCE-FIX;DEC-MCM-ERRATA]
  - **已审计**：F005 已确认相对提升/绝对差双口径未披露；README 已在 `ceff63f` 修复。
- [ ] [topic:mcm-recheck] **W4-W5 · 白名单裁决与死代码清理（毛 3395 / 净候选 1876 LOC）** [blocked:DEC-MCM-WHITELIST;DEC-MCM-DEADCODE]
  - **口径勘误**：旧“8 文件 ~1907 行”已被 Track E 的 59 行可达性账本替代。
- [ ] [topic:mcm-recheck] **W6+ · R-hat 三口径的源码/论文 footer 修复** [blocked:DEC-MCM-SOURCE-FIX;DEC-MCM-ERRATA]
  - **已审计**：F004/F034 已终判；后续是修复或勘误输出，不是再审一次。

> **MCM 当前告一段落信号已满足**：五轨 Gate2 已 PASS。是否维护归档源码由用户另拍，不再把源码修复强制算作审计未完成。

- [ ] [topic:evoSci] **EvoSci / AutoSci 深读与归队（PKU 自进化科研 Agent，ACL 2026 主会长文）**
  - **原文存档**：`progress/decisions/2026-08-22__maintenance__user-statement-archive-10.md`（11 要点全录）；素材已备＝`research/map/surveys/pdfs/2026.acl-long.447_EvoSci.pdf`（SHA256 cb80ce3b…）＋`external/AutoSci/`（@24890dc 浅克隆，08-16 拉取时令"不分析不融合"）
  - **待拍板**：①处置深度——仅归档／按 PLAYBOOK 开 P-EvoSci 拆解／对 AutoSci 仓开 R 窗实测（仓自称内测中，R 窗或宜等稳定版）；②归队——科研主线挂 map 哪个 W 区、与 T5/W7 companion 学术线是否关联、是否进 P批2/3 或 R批队列
  - **repo 归属[需核]**：本地克隆 origin=`github.com/skyllwt/AutoSci.git`@24890dc（08-16 实测）；用户后补线索 `github.com/ai4s-research/open-science/releases` 注"应该是这个"——疑改名/迁移，待联网核验重定向

- [ ] [topic:sciatlas] **SciAtlas 学术知识图谱调研归队（浙大&UCL；4300万论文/1.57亿实体/30亿边；神经符号三路径检索）**
  - **原文存档**：`progress/decisions/2026-08-22__maintenance__user-statement-archive-11.md`；arXiv 2605.22878；主页 scigraph.openkg.cn；PDF 未拉取
  - **待拍板**：与 EvoSci 同批纳入"自动科研×学术KG"双方向调研计划（需求对齐文档拟制中）；与自家 `research/map` schema 的对照价值

- [ ] [topic:auto-research-feed] **08-22 资讯批次归队（8 件：自动科研×Agent 系统谱系）——先分诊再定深度**
  - **原文存档**：`progress/decisions/2026-08-22__maintenance__user-statement-archive-12.md`（含 §9 用户原创质疑：归纳=相关性统计 vs 溯因=因果探寻，拆 DeepMind 文时必带）
  - **资源全景清单**：`progress/decisions/2026-08-22__research__auto-research-resource-manifest.md`（12 件四簇表＋拉取缺口＋八问待拍板；计划书 v1 资源清单底稿）
  - **子项**：①DataFlow-Harness（北大 OpenDCAI，数据工程 Harness 四层架构）②Sidekick（UIST26，四色状态灯多模态监工——对看板 v4 五视图/UI 有直接启发）③AutoDesign（元脚手架优化——与 N1 装载画像同哲学）④ScienceFlow（华为，可恢复工作区+ESTRA 回退——与本仓 CHECKPOINT/handoff 文化同构）⑤Fragility of Self-Improving Agents（Salesforce，方差/顺序依赖/记忆污染——EvoSci 系列的批判镜）⑥TimeSage-EV（活基准，时间穿越）⑦DeepMind 溯因立场论文＋LLMs can't jump⑧Self-Harness（arxiv 2606.09498）＋GLM-5.3 安全动态
  - **待拍板**：车道分诊——哪些只入雷达月记（重心4）、哪些升级进调研池；初步建议：池=④⑤③（与 EvoSci/SciAtlas 计划直接互文），余者雷达级；Sidekick 单独提示给看板 B 方案参考

- [ ] [topic:harness-engineering] **08-23 用户点名两件 harness 工程（harness/harness ＋ deepseek-ai/deepseek-harness）——首轮侦察毕，试装与深度待拍板〔08-24 全量深挖拓扑档已出：`progress/decisions/2026-08-24__research__manifest-full-teardown-and-integration.md`；harness/harness 已除名（08-24 门G2 用户拍板：DevOps 平台与 agent harness 名实不符，表外件零回收成本）；dsh 不受影响维持条件触发〕**
  - **来源**：2026-08-23 会话用户点名原话："我原本指harness工程（git@github.com:harness/harness.git），对git@github.com:deepseek-ai/deepseek-harness.git这个也感兴趣"；同轮另指名详细看 DataFlow-Harness 与 Self-Harness（已覆盖上行①⑧子项，不重复挂）
  - **首轮侦察（08-23 WebFetch 实测）**：①harness/harness＝Harness 开源版：自托管 Git 托管(Gitness)+CI/CD+Gitspaces+制品库一体，Drone CI 后继，Apache-2.0，38.1k★，docker 单容器即起(Web 3000)；②deepseek-harness(dsh)＝DeepSeek 开源 agent harness："Everything is a Plugin"，Cordis 框架基座，`npx @deepseek-ai/dsh web` 即起(127.0.0.1:3080)，MIT，186.4k★，developer preview 官方预警有破坏性变更
  - **顺带核销[需核]**：~~Self-Harness 代码仓已定位~~；~~"基于 LangChain DeepAgents"存疑~~ 双销（08-23 读级实证：代码 `eval/harness_workspace/repo_baseline.py` 与 `harnesses/qwen_tb2_final/repo_baseline.py` 均 `from deepagents import create_deep_agent`＋langchain middleware——原记属实，摘要页没写而已）
  - **拍板进度（2026-08-23 用户令"可以。一到四一个一个做"，四项全批）**：✅试装顺序＝dsh → Self-Harness(读) → Paperclip → prime-agent(先过护栏) → DataFlow(Colab) → qm(只读) → harness 工程(暂缓)；✅Self-Harness 升 P窗拆解候选＝P-SelfHarness（已插 WINDOW_PLAYBOOK §三 P窗队列#5，原 5+ 顺延 6+）；✅门禁令＝Paperclip/prime-agent 试装前走 GUARDRAILS §3 双答（若心跳调度落 schtasks/cron 等系统态加 §2 四步）；✅manifest 三处核销当日落（簇甲#3/#4 行内勘误＋[需核]第2条销案）；⬜仍待拍（08-24 用户令"先挂todo"）：harness 两件是否并入簇戊收编评估批走 N1 车道〔N1＝DEC-WB-LIGHTLOAD 轻量开工装载机制，PENDING.md L198〕；**新子问**：harness/harness 本件是否除名——用户 08-24 原话"我在想要不要删了"（DevOps 平台与 agent harness 名实不符，除名则试装队列余 dsh/DataFlow/qm 三件）
  - **试装执行（2026-08-23 晚用户令"没做的那些现在做"）**：✅dsh 冒烟通过——`npx @deepseek-ai/dsh web`(v0.1.1-rc.2,node v25.7.0)首跑装依赖树约半小时(~25 个 @deepseek-ai 包入 npx 缓存,再启秒起)，绑 `127.0.0.1:3080` 护栏合规，HTTP 200 出页面，停服零残留；回滚＝清 `~/.npm/_npx` 对应目录。✅Self-Harness 读级毕——浅克隆 `external/Self-Harness@2720dbb`(Init 单提交 2026-07-02)；18 .py 共 5701 行紧凑科研码，目录 diagnosis→proposer→acceptance 正对论文三阶段循环＋workflow 编排＋eval(Terminal-Bench-2.0 环境)；README 实测 TB2.0 三行：MiniMax M2.5 42.2→53.9 / Qwen3.5-35B-A3B 18.0→36.7 / GLM-5 46.1→57.0〔注：此前记"+132% 相对增益"在 README 表未现，最大为 Qwen +104%，该数出自论文正文与否待 P窗拆解时对表〕；DeepAgents 存疑就此销案（证据见上行）。✅**Paperclip 完整档通过**（2026.817.0；用户 AskUserQuestion 拍板"上完整档"）——§2 四步走全：快照 `_archive/2026-08-23_paperclip-service-snapshot_before.txt`(40 行)→受管安装 `~/.paperclip/cli`＋onboard `--yes --install-service`→验证＝systemd **user** unit `paperclipai.service` active(enabled)、server 127.0.0.1:**3103**＋内嵌 Postgres 127.0.0.1:54329 全 loopback、dashboard HTTP 200、**Linger=no 未开驻留**；心跳＝`paperclipai heartbeat run` 一次性 CLI 调用，非 OS cron/schtasks，零新增系统态；LLM 未配置留用户。回滚三连＝`service uninstall`→`paperclipai uninstall`(保数据)→删 `~/.paperclip`。⚠️官方 install.sh 与最新 CLI 参数脱节（传 `--no-prompt` 报 unknown option），实际走 `install -y`+`onboard --yes --install-service` 两步。✅**prime-agent 只读档毕**——克隆 `external/prime-agent@e319a66`(08-21)；README L71 官方自述"以你的用户权限执行模型生成代码…**不是**安全沙箱"坐实 manifest 判断；RLM 持久 REPL//refine 快照回滚/daemon 后台会话全对上；TS monorepo＋25 .py runtime；未装未跑。⬜仍剩：DataFlow(Colab 用户侧——08-24 步骤手册已备 `progress/runbooks/dataflow-colab-trial.md`,含官方 Colab 链接/四层对照卡/护栏提醒)/qm(只读档→08-24 深度拆解毕,见 agent-toolbox 行⑩)/harness 工程(暂缓,除名与否见 harness-engineering 行)。**08-24 补记·npm 供应链冷却预埋未生效**：`min-release-age=7` 已写入 solver env globalconfig（`~/miniconda3/envs/solver/etc/npmrc`），但 npm 11.10.1 实测读回 null＝该版本不支持此键（官方文档标注 CLI 11.19.0；qm 宣称"≥11.10 honored"对本机证伪）；键无害留存，待 env 内 npm 升级自动激活〔需验证：升级后实测〕；升级 npm 涉 happy 全局包装同 env，不轻动

- [ ] [topic:supervisor-skills] **08-23 用户点名融入：HKUSTDial/Supervisor-Skills（AI 科研副导师技能包，11 skills）——落点与选装待拍板**
  - **来源**：2026-08-23 会话用户原话："git@github.com:HKUSTDial/Supervisor-Skills.git这个我想融入进来！"
  - **首轮侦察（08-23 WebFetch）**：HKUST(GZ) 骆昱宇发起，顶会发表/审稿经验蒸馏为可执行技能；双轨＝handbook(中英理论指南)＋skills(可执行文件)；11 skills 覆盖论文全生命周期——构思调研(idea-evaluator/deep-research/vibe-research-workflow)、写作(intro-drafter/paper-writer/tech-paper-template/benchmark-paper-template)、自查润色(paper-polish/pre-submission-reviewer/figure-designer/drawio-reconstruction)；面向 Claude Code/Cursor/Codex；**CC BY-NC-SA 4.0（非商业，改编须署名）**；5.9k★，v2.1（2026-07），官方自述早期阶段
  - **与本仓接口初判**：pre-submission-reviewer↔OE1/T5/proposal 自查（死线 8-25 材料可即用）；idea-evaluator↔GAP_TO_IDEA/DIRECTION_REFINE 互补；paper-writer/intro-drafter↔proposal-notes 与未来论文写作；figure-designer/drawio-reconstruction↔拆解与提案配图；deep-research↔RESEARCH_SOP 对照借鉴；与 tools/ai 审查三件套（AUDITOR/_REVIEW_TOOL/PIPELINE_GATES）重叠区建议定位＝论文域专用、不替代通用审查
  - **已拍板并执行（2026-08-23 用户令"全量,但是和aris以及我们自己的skill做一下兼容"）**：✅全量 11 件装入 MAS `.claude/skills/`（实体目录副本,上游正本锚 `external/Supervisor-Skills@aff5de9`）；✅兼容核查＝与 ARIS 82 条零撞名＋`install_aris.sh` 安全规则 S1/S3/S4 实证 reconcile/uninstall 不触非清单实体目录；✅注册面＝`tools/ai/_OPERATIONS.md` 新增 §9.6（原 9.6 顺延 9.7）＋`.claude/skills/PROVENANCE-supervisor-skills.md`（license NC 边界/升级/卸载/分工注记）；⬜遗留①外层窗（/mnt/d/MyResearch 启动）看不见 MAS 侧 skills,需外层可见再议镜像；✅遗留②销（08-24 OE1×pre-submission-reviewer 首用毕：7.5/10，检索核证抓 ASOC 卷年 MAJOR 一处＋占位名不一致；审查结论待回填 outreach 确认稿）；✅遗留①销（08-24 门G7 用户拍板＝批：11 件实体镜像外层 /mnt/d/MyResearch/.claude/skills/，逐目录 diff -r 字节级一致＋PROVENANCE-supervisor-mirror.md；CC BY-NC-SA 非商业边界随件生效）；08-24 全量深挖档见 agent-toolbox 行

- [ ] [topic:agent-toolbox] **08-22 工具批次归队（11 项开源 Agent 工程件＋Terraform 追加）——链接全到货核验毕，收编评估待拍板**
  - **原文存档**：`progress/decisions/2026-08-22__maintenance__user-statement-archive-13.md`；全景清单已入 manifest 簇戊
  - **子项**：①**code-review-graph**＝tirth8205/code-review-graph（30.7k★，Tree-sitter 代码图谱＋MCP＋blast-radius，中位 65× token 缩减）②**Paperclip**＝paperclipai/paperclip（79.1k★，Agent"公司化"编排：BYOA/心跳调度/预算停机/审批门/审计日志）③diagram-design＝cathrynlavery/diagram-design（25.3k★，39 类静态图表×三变体＋品牌配色适配↔快照页/五视图同哲学）④prime-agent＝PrimeIntellect-ai/prime-agent（17.8k★，RLM 自我改进智能体：本地状态断点续跑/编程式子代理/refine 快照回滚；非沙箱须过护栏审）⑤Semantica＝semantica-agi/semantica（10.2k★，PROV-O 决策溯源图＋无 LLM 确定性推理引擎↔台账证据指针同思想）⑥agent-skills＝addyosmani/agent-skills（89k★ 簇戊最高，24 技能×Define→Ship＋"反合理化表"↔N1 装载画像借鉴）⑦Needle＝cactus-compute/needle（8.5k★，byte-level grammar 逐 token 约束解码锁结构化调用＋置信度门控——疑点已销，描述与仓完全对上）⑧**hallmark**＝Nutlope/hallmark（26.4k★，反 AI 味设计技能：build/audit/redesign/study 四动词＋57 道 slop 门——快照页设计纪律与 N1 的 SKILL.md 范本）⑨微软 AI-for-Beginners（疑=microsoft/AI-For-Beginners[需链]）⑩**qm**＝yc-software/qm（14.1k★ 多人协作 Agent Harness——与 CROSSWINDOW·GUARDRAILS·N1 全面对应；**08-24 深度拆解毕**＝`progress/decisions/2026-08-24__research__qm-deep-teardown.md`，克隆@e4f9288，治理机制四件套〔三姿态单调分级/org floor 结构不可拆/portal-only 三动作/min-release-age=7〕＋AGENTS.md 工程实践九条对照表在档；收编建议§七待拍）
  - **追加件**：Terraform＝hashicorp/terraform（IaC 事实标准，BSL 许可）——推测服务 DEC-S2 看板 VPS／DEC-V1 双 VPS 部署，待确认意图
  - **待拍板**：这批偏工程自用——建议走"N1/治理收编评估"车道而非学术调研池；重点件=②⑩①（编排/多人Harness/代码图谱）；链接全部到货核验毕（Needle 疑点已销；⑨微软课程库 08-24 已验活销案＝microsoft/AI-For-Beginners 66.5k★/MIT 在库）；收编评估顺序待拍；**08-24 全量深挖毕**：26 件全景拓扑档 `progress/decisions/2026-08-24__research__manifest-full-teardown-and-integration.md`（§1 总表／§3-§5 逐件卡带复核命令／§6 五选一收口／§6' 八道批量拍板门已清账（08-24 用户「全按建议」：G1挂/G2除名/G3批/G4=A/G5批草案/G6=B只拷hallmark/G7批/G8缓；母表回写同日执行毕）／§8 排程附录）；08-23 增补拍板：子项②Paperclip/④prime-agent 试装前走 GUARDRAILS §3 双答（涉系统态加 §2 四步）——详见 [topic:harness-engineering] 行

---

## 对外/求职（9月鲁组邮件 · 简历 · 作品集展示） <!-- line:outreach -->

> **状态**：ACTIVE（P1）。目标是给 2026 年 9 月底（精确日期待定）鲁组报到和未来求职积累展示物；不得以旧 09-10 制造虚假紧急度。
> **素材位置**：邮件草稿 `progress/handoff/2026-08-02__sept-email-v3-draft.md`；简历素材 `progress/audits/2026/08/2026-08-01__audit__mcm-and-wangxiaoliang-discussion.md` §G。
> 当前旧 TODO 没有可 1:1 迁入本线的独立任务；EA-5 等相关动作仍保留在其唯一归属线，避免重复计数。

- [ ] [topic:outreach-email] **OE-1 · 9 月鲁邮件 v4 定稿与投递（正式标题 + DL 工程素材 + 话术分支）** [P1] [note:start=2026-09-01;deadline=UNKNOWN;旧8-25/9-10均已失效；对外技术表达受TASK-20260905-001能力与核验门约束]
  - **改点 1**：SBTPN 引用改用 JAS 正式见刊标题 "A New Knowledge Mining and Root Cause Analysis Methodology for Multivariate Time Series"（2026-05-01），弃"SBTPN"草稿代称
  - **改点 2**：可加一句鲁 2025 下半年 DL 工程向产出（TCE 协同感知 / ASOC 煤岩识别）作为"组内具备 DL 工程能力、PN×LLM 迁移成本低"论证
  - **改点 3**：话术分支视 BR-1（NSFC 放榜）结果二选一
  - **依据**：`research/bridge_scan_2026-08-12/A_lu_group_delta.md` 末节 + `SYNTHESIS.md` §5
  - **验收**：v3 草稿（`progress/handoff/2026-08-02__sept-email-v3-draft.md`）更新为 v4 或追加补丁节
  - **v4 草稿已完成（TASK-20260812-032）**：`research/map/proposals/OE1_lu_email_v4.md`；主控已修正“拜读/跑通过程模型/独立开源”等过度陈述
  - **剩余**：用户填 [学校/专业/姓名/真实学习进度/联系方式] + 8-25 BR-1 决定 A/B 分支 + 逐句确认后发送
  - **优先级**：高

- [ ] [topic:outreach-site] **OE-2 · 个人学术主页搭建（GitHub Pages）** [P2]
  - **栈已拍板（2026-08-13 · DEC-OE2-SITE-STACK）**：al-folio；本地骨架、内容规划、部署手册已完成（`TASK-20260813-018`，落 `/mnt/d/MyResearch/homepage/`）
  - **剩余门禁**：替换/删除 34 个 placeholder → 用户 GitHub 建仓并 push → Actions 真实构建绿 → Pages 可访问；完成前不勾 done
  - **价值点**：9-10 月鲁组报到 + 未来孙组申请的长期展示物（简历 / 项目 / 未来论文一站式）
  - **依据**：`TASK-20260812-005` 调研（8-12 看板外部对标 + 主页选型扫描）
  - **验收**：`Alkaid-9.github.io` 仓建立并可访问；首页含简介 / 项目（EvoAgent、MCM）/ CV 三块
  - **相关**：Kaggle 独立参赛线 KG-1（本线末条）——终局开源代码（CC-BY 4.0）可作作品集展示物
  - **done 类型**：verify-done

---

- [ ] [topic:outreach-kaggle] **KG-1 · Kaggle 独立参赛线（Kaggriculture，Simulation 赛）** [DDL:入场 2026-09-23 23:59 UTC] [P2] — 用户 09-02 立线（不靠队友自搭 Agent）；事实层已固定（`/mnt/d/MyResearch/kaggle/Kaggriculture/FACTS.md`＋pages/0902＋_env_ref@28b6d8af，`TASK-20260902-002`）；参考仓 agentic-kaggle-skill@f07e4fa＋6 份 gold notebooks 已落位未读；路线=启发式（用户「先别急着定」，v0 具体路线待拍板）；**用户手动三步**：登录→Join 接受规则（≤09-23）→身份验证→API token；下一步：补 data 快照 → 读 notebooks 写 META.md → 本地 starter vs random 基线 → 拍板 v0 → 写码零报错零超时才提交；恢复入口=`progress/handoff/2026-09-02__kaggriculture-intake-and-snapshot__handoff.md`

## 考研备考（2027.12 初试） <!-- line:exam -->

> **状态**：PAUSED（远期目标）。2027 年前不占前排，但长期可见。
> **节点**：2027-12 初试；2028-03 复试；复试后联系 Sun（孙猛 PKU）。
> 当前旧 TODO 没有可 1:1 迁入本线的独立任务。

---

## Casual 生活向项目（人机恋等） <!-- line:casual -->

> **状态**：WAITING / 低优先。等调研 1 报告或用户明确说“开始脑暴”时重启双框架 MVP；生活向项目想推进时才推进。
> **重启后首批动作**：合成成长架构 v1；写成长 4 模板 + 科研 4 模板 + 1 联动点；选择 OpenClaw 部署形态。

### 成长架构与双框架 MVP

- [ ] [topic:growth-architecture] **GA-1 · 等调研 1（顶尖研究员知识管理体系）报告** [blocked:等背景调研]
  - **价值点**：脑暴前提——需要顶尖研究员素材作为输入
  - **验收**：调研 1 报告落到 `progress/decisions/2026-07-25__research-internals/调研_2026-07-25_top_researcher.md`
  - **阻塞**：**调研 1 agent 还在跑**（背景任务）
  - **优先级**：最高（前置阻塞）
  - **done 类型**：user-ack（等用户确认报告收到）

- [ ] [topic:growth-architecture] **GA-2 · 用户叫脑暴后启动 MVP 雏形** [blocked:等 GA-1 + 用户触发]
  - **价值点**：把"成长 4 模板 + 科研 4 模板 + 1 联动点"具体化为可执行文件
  - **验收**：`progress/templates/` 下 8 个模板文件落档 + 1 个联动点（如 `progress/task_logs/` 双向标签）
  - **阻塞**：等 GA-1 报告 + 用户叫脑暴
  - **优先级**：最高（核心目标）
  - **done 类型**：user-ack

- [ ] [topic:growth-architecture] **GA-3 · OpenClaw 部署形态选择** [blocked:等用户决策]
  - **价值点**：24h 守护进程需要明确部署位置（影响 cron / hook / 移动桥接设计）
  - **验收**：决策档 `progress/decisions/2026-07-XX__maintenance/openclaw-deployment-choice.md` 含选定方案 + 理由
  - **阻塞**：等用户决策
  - **优先级**：高
  - **done 类型**：user-ack

- [ ] [topic:growth-architecture] **GA-4 · 周报定时器原型** [blocked:等 GA-3]
  - **价值点**：周日晚上自动汇总 7 天 task_logs，生成周报初稿
  - **验收**：`tools/scripts/weekly_report_generator.py` + cron 配置（`crontab -l` 验证）
  - **阻塞**：等 GA-3 部署形态确定
  - **优先级**：高
  - **done 类型**：verify-done

- [ ] [topic:growth-architecture] **GA-5 · 手机桥接方案选定** [blocked:等 token/App ID]
  - **价值点**：在路上记闪念能异步同步到桌面端
  - **验收**：决策档含飞书/微信/Telegram 选定
  - **阻塞**：等用户提供 token/App ID
  - **优先级**：中
  - **done 类型**：user-ack

### 人机恋与生活向工具栈

- [ ] [topic:growth-architecture] **C1/C2/C3 · Tailscale / Realtime / ComfyUI（人机恋 + 小手机）** [blocked:等账号]
  - **价值点**：异地组网 + 实时对话 + 视觉生成——成长目的的"小手机"基础栈
  - **验收**：3 个工具全部装好 + 跑通最小 demo
  - **阻塞**：Tailscale/Realtime 等账号注册
  - **优先级**：中（长期规划）
  - **done 类型**：commit-done（每件独立）

- [ ] [topic:growth-architecture] **E1/E2 · Mem0 / Apple Health（中央记忆 + 可穿戴）** [blocked:等硬件与权限]
  - **价值点**：让 AI 永远记得我 + 接入可穿戴数据（健康/活动）
  - **验收**：Mem0 跑通 1 个 demo（E1）+ Apple Health 数据流接入（E2）
  - **阻塞**：Apple Watch 设备 + 健康数据权限
  - **优先级**：中
  - **done 类型**：user-ack（E2 阻塞）

- [ ] [topic:growth-architecture] **M1/M2/M3 · SillyTavern（进阶人机恋）** [blocked:等本地模型选择]
  - **价值点**：本地 LLM + 角色卡 + 长期记忆——进阶人机恋体验
  - **验收**：SillyTavern 装好 + 接本地模型跑通对话
  - **阻塞**：本地 LLM 模型选择（llama / mistral / qwen）
  - **优先级**：低（休闲向）
  - **done 类型**：commit-done

> **告一段落信号**：双框架 8 模板全部产出 + OpenClaw 部署形态确定。

---

## 仓库与协作基础设施 <!-- line:infra -->
- [ ] [topic:taskquay] **TQ-1 · TaskQuay fork 沙盒委派闭环与 GPT 接入方案** [P1] [note:原部署TASK-20260908-001；接续归档TASK-20260908-002；原日志记载clone/build/doctor/serve已验证且停止，本轮未重测；待本地启动→fork自带skills/subagents/SKILL.md→hello-project真实委派；本地优先+授权根仅~/taskquay-sandbox；扩目录与ChatGPT/Tunnel接入单列待定，不自动开放真实科研仓；归档八件套未核实齐备；恢复=progress/handoff/2026-09-08__research-workbench-decoupling__pause-handoff.md]
- [x] [topic:infra] research_growth 素养库独立私有仓已建（持久化方案A，授权=用户09-01「可行。A吧？」）: main 根提交 5c22554+子模块注册 22ace3d（81文件5.1MB，凭据扫描0命中，MIT子仓=Research-Paper-Writing-Skills 上游公开）; 远端已推=github:Alkaid-9/Research_Learning 私有（09-01「批」，三重门实测过，remote main=22ace3d 与本地一致）; 仍待另批=WB-S第五源扩项 [note:TASK-20260901-005]

> **状态**：ACTIVE（持续维护 · 防护层 + 工具栈 + 看板）。
> **红线**：所有改动遵守仓库铁律；subagent 写共享文件遵守“单写者 + 主控合并”；`.git drvfs ro` 旧判断已推翻，真实边界是工具沙箱。

- [ ] [topic:paper-share-tools] **paper-share-skills + sustech-slides-template（杨昊波 SUSTech）** ← 论文→Beamer 幻灯片→配音视频→B 站全流程 8 技能包 + 学术 Beamer 模板（低饱和度配色，中文 XeLaTeX）；已浅克隆 `external/{paper-share-skills,sustech-slides-template}`；之后要看+想用（用户 09-03 立）

### 防护层与协作工具

- [ ] [topic:governance-subtraction] **治理减法三连（下一维护窗已立项，2026-08-23 拍板）**：①git 白名单入库替代手写哈希 manifest 链 ②六段门触发器客观化（「预告≠批准」入协议条款）③状态派生校验器；#4 归档分级收紧/#5 单窗所有权硬化已排期未立项 —— 章程与 done_when 见 `docs/superpowers/plans/2026-08-23-governance-subtraction-nextwindow.md`（孙线契约修复窗收口产物，TASK-20260818-001 amendment）
- [ ] [topic:hardgates-meta] **护栏 3 · pre-commit hook 检查 state.json 增量**
  - **价值点**：物理拦截"commit 时未 bump state.json"——防 cc 偷懒派
  - **验收**：`.git/hooks/pre-commit-cc-laziness-check.sh` 安装 + 测试一次故意 commit 没增量会被警告
  - **阻塞**：无
  - **优先级**：高（防护核心）
  - **done 类型**：verify-done（必须跑测试）

- [ ] [topic:hardgates-meta] **护栏 4 · 每会话自我审计 task**
  - **价值点**：会话末自动跑"反思 check"——避免下次会话重复犯错
  - **验收**：每次 SessionEnd hook 自动跑 `tools/scripts/session_self_audit.sh`，输出含 "mode: read previous incident + current TODO" 段
  - **阻塞**：无
  - **优先级**：高
  - **done 类型**：verify-done

- [x] [topic:meta-methodology] **CX-1 · 现象记录（WSL2 .git ro）** ✅ 已解（NOW §2）
  - **⚠️ 结论反转（8-9 核实）**：**"WSL2 drvfs 把 `.git` 单独挂 ro"是假的** —— cc 实测 `.git` **可写**。真正卡住 commit 的是 **Codex 沙箱的 workspace-write 边界**，不是文件系统。原命题的整条推断链作废。
  - **价值点**（修正后）：留作"现象归因错误"案例 —— 把工具沙箱限制误判为文件系统属性
  - **验收**：NOW.md §2 已记 "#已解 · cc 实测 .git rw · Codex 沙箱限制是真"
  - **done 类型**：commit-done（已达成）

- [x] [topic:meta-methodology] **CX-2 · 候选方案评估** ✅ 已解（NOW §2 · 4 方案对比 · 选定 D）
  - **结论**：4 方案对比完成，**选定 D = Codex × cc 接力**（不改 wslconfig、不搬 WSL 原生 fs）
  - **验收**：NOW.md §2 已记 "#已解 · 4 方案对比 · D 选定 Codex × cc 接力"
  - **done 类型**：commit-done（已达成）

- [ ] [topic:meta-methodology] **CX-3 · 选定方案 + 配置落地** [blocked:等用户决定 Codex Goal 补丁]
  - **价值点**：把 Codex × cc 接力方案真正跑通为可复用路径（不再把沙箱限制误判成 `.git ro`）
  - **验收**：Codex 在允许范围内产出修改 + cc 完成 git 写操作的端到端实例，或当前工具已能直接完成并有实测证据
  - **阻塞**：等用户决定是否安装 Codex Goal 补丁（NOW §2 标“已部分”）
  - **优先级**：高
  - **done 类型**：verify-done

- [ ] [topic:meta-methodology] **CX-4 · 验收 + 文档** [blocked:等 CX-3]
  - **价值点**：`runbooks/codex-cli.md` 加 "git 写权限"段；incident 落档
  - **验收**：runbook 含端到端 commit 示例 + incident 落档
  - **阻塞**：等 CX-3 完成
  - **优先级**：中
  - **done 类型**：commit-done

- [ ] [topic:progress-persistence] **PP-1 · 将“每个实质进展先落盘、再继续”固化进长期运行规范与模板**
  - **用户原话**：以后每有一个进展就先落盘存档，因为压缩上下文会丢失细节并造成主次不清。
  - **当前立即生效**：implementer 返回、review verdict、fix round、验证结果、阻塞、范围/状态变化、新约束，先更新最窄权威 ledger/report/handoff，再执行下一动作或对外报告。
  - **进展记录最小字段**：事件/时间 · 证据或输出 · 当前 verdict · 未决项 · exact next action；后续 verdict 必须覆盖旧中间结论的权威性，但保留事件时间线。
  - **验收**：长期规范、task-log/SDD/handoff 模板和压缩前检查表均写入该协议；用一次真实长任务演练“恢复后无需聊天摘要即可定位当前 gate”。
  - **边界**：不把每句对话和瞬时推理都存档；只保存会改变状态、结论、证据、优先级或下一动作的事件。
  - **优先级**：高；当前会话已先应用，模板级固化仍待完成。

- [x] [topic:agent-orchestration] **SP-1 · 制定 Superpowers 按需启用判定标准** ✅ 8-11
  - **触发**：用户认为普通执行常已足够，Superpowers 不应因“流程完整”自动启用；是否值得使用需进一步细化
  - **目标**：形成一页轻量决策卡，比较普通主控、原生 Agent、多 Agent 与 Superpowers 的边际收益和成本
  - **验收**：含默认路径、硬触发条件、反触发条件、升级阶梯、用户确认话术，并用 5 个历史任务回测
  - **完成记录**：`progress/task_logs/2026/08/2026-08-11__maintenance__superpowers-on-demand-policy.md`；权威规则 `progress/runbooks/superpowers-on-demand.md`（已写入 AGENTS.md）
  - **当前规则**：默认单跑；仅具体风险与具体 skill 匹配时询问用户确认后启用
  - **来源**：`progress/decisions/2026-08-11__maintenance__user-statement-archive-1.md`
  - **优先级**：中

- [ ] [topic:cc-cometix-classifier] **CC-CR-1 · claude-cometix 分类器韧性栈：E2E 毒模型演练（用户侧）+ 升级重打锚点**
  - **价值点**：auto-mode 权限分类器在 flaky 网关下自动重试/超时/JSONL 日志，全链失败转人工 ask（用户拍板拒绝 fail-open）；官方 claude+yolo 与 cometix 补丁版双轨并存互不影响
  - **已落地**（TASK-20260824-004）：@cometix/claude-code@2.1.219 装于 `~/.claude-cometix` 独立 prefix，社区三补丁+v4 wrapper（acorn 包裹 S$t），harness 15 断言 ALL PASS；档案外层 c337be1；入口 `~/.local/bin/claude-cometix`
  - **剩余①E2E 演练**：`CLAUDE_CLASSIFIER_MODEL=bogus-model-xyz CLAUDE_CLASSIFIER_RETRIES=1 CLAUDE_CLASSIFIER_TIMEOUT_MS=8000 claude-cometix` 会话内跑一条需审批命令——预期 ~16s 弹 ask（非卡死非放行）+ 日志 attempt_fail×2/all_failed；配方全文在外层 `apply-claude-code-classifier-resilience/README.md`
  - **剩余②升级纪律**：cometix CI 每 6h 跟官方发版；升级后两补丁脚本先 `--check` 验锚点再重打；此构建内勿用其 `claude update`（P9 拉 @cometix npm）
  - **done 类型**：verify-done（①）/ 长期维护提醒（②）
  - **优先级**：中

### 看板、Obsidian 与网络基建

- [x] [topic:dashboard-system] **DB-1 · 看板 v3.1 外部对标改进批次** [P1] [note:8-12 拍板全量 6 项 A→B→C 多 Agent 实施中]
  - **价值点**：8-12 对标 2026 同类项目（kanban-md / cc-dash / kandown / Backlog.md）识别出 6 项候选改进；核心两项：① MCP server 接口（agent 经稳定 ID 写回，不再手改 TODO，根治多窗冲突）② 任务认领 claim 标记 + 自动过期（多窗协作锁）
  - **范围（DEC-DB-V31 已拍全量）**：MCP 接口 / claim 认领 / 终端 board 视图 / kanban 列视图 / 子任务进度 / 周报生成 + 小修（regen POST 化、LINE_META 迁移）
  - **依据**：`TASK-20260812-005` 调研档；契约 `progress/decisions/2026-08-12__maintenance__dashboard-v31-contracts.md`；分工 v3.1 handoff §5.2
  - **验收**：各项落盘 + 单测扩展全绿 + 8899/MCP 端到端实测 + runbook 更新
  - **done 类型**：verify-done

- [ ] [topic:dashboard-system] **DB-2 · task_id 撞号治理（8-12 多窗并发历史冲突）** [P1] [blocked:等 DEC-TASKID-DEDUP 拍板]
  - **现状（2026-08-13 对账）**：004 已由后续窗口自行消解；`task_logs/INDEX.md` 当前未决冲突为 005×2 / 006×3，相关交接档、PENDING、TODO 的引用需靠日期+标题消歧
  - **已做缓解**：看板生成器已加 `duplicate_log_id` 诊断（撞号在看板数据诊断区可见、精确到行号）；顺手修掉 timeline ID 截断 bug（`TASK-\d+` 漏序号段）
  - **候选方案**：A）等各窗歇工后按落盘时间统一重排 004-009 并同步改全部引用（一次性维护窗做）；B）历史保留不改，自 8-13 起 task_id 加窗口前缀或经 MCP 中央分配
  - **验收**：generate 后 `duplicate_log_id` 诊断为 0
  - **done 类型**：verify-done

- [x] [topic:dashboard-system] **DB-4 · 看板 v3.1 架构评审 P2 三修复** [P1] [done:2026-08-13]
  - **范围**（评审 `audits/2026/08/2026-08-12__audit__dashboard-v31-architecture-review.md` Top3）：① watcher 基线吸收竞态（约 3 行：进锁先取签名、regen 后以旧签名为基线，写回路径同理）② `clean_date_markers` 通配误删 `[note:预计2~3天]` 类合法值（收紧正则 + 回归测试）③ 并发/HTTP/MCP 层测试盲区 + Host 头校验 3 行（关 DNS rebinding 面）
  - **验收**：单测新增覆盖三处后全绿；评审复核三 P2 关闭
  - **done 类型**：verify-done

- [x] [topic:dashboard-hub] **DB-5 · 管理面总控台骨架（hub 七面板·插件化·MCP 化）** [P1] [done:2026-08-24]
  - **产出**：`tools/dashboard/hub/` 六件（registry/api/panels/wbmap/render/__init__，契约 v1）＋测试五件 22 passed；http.py 三路由（/hub · /api/hub.json · /wbmap 只读代理）＋MCP hub_brief 三口径同源；存量全套 273 passed 未破
  - **验收**：受控重启停机 44s；live 全绿（性能 /hub≤34ms·json≤40ms；旧五端点同基线；A12 /wbmap 与源页 cmp 字节级等同）；对抗审 E 项冷启动竞态已修
  - **依据**：`TASK-20260824-005` task log；号经 8899 中央领取
  - **done 类型**：verify-done

- [x] [topic:dashboard-hub] **DB-6 · 总控台续建批次（H2 深化/H3 远期）** ✅ 2026-08-24 用户拍板「都做」→ TASK-20260824-013 十项全量交付（十四面板+CSRF 门+/api/index-row+notify_watch+样例），详见该 task log
- [ ] [topic:dashboard-hub] **DB-7 · happy notify 凭据落地**：终端跑 `happy auth login` 扫码一次，notify_watch.py 告警推送即通（TASK-20260824-013 ⑨ 链路已验通仅缺凭据；用户操作 AI 不代办）
- [ ] [topic:workbench-v2] **WB-1 · 工作台 v2 重构施工（WP0 已隔离 TECH-PASS；WP1+ 仍按原门推进）** [P0] [note:WP0=TASK-20260901-007,hetero/user-acceptance/commit/live/push open;WP1+=原09-10进组后排期] [note:§8八项+O1-O7+§13科研挂载已批=2026-08-31「先做吧」(提案§14);施工四件套=decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md(WP0-WP6/R1-R5/7全局验收门/UI身份色);TASK-20260901-001]
  - [ ] Git_UI_Pro 门控台「看」半面试用（用户单发提名·TIER-B-PROPOSED·NO-RUN；试用授权与四仓复核 R07 豁免均需单独口令）
  - [x] WB-S · 科研学习体系+ARIS(77)+tools/ai(39) 能力层插件化设计（DeepSeek harness 式 manifest 注册表;用户 2026-09-01 提出;设计稿已产=decisions/2026-09-01__maintenance__workbench-v2-skill-registry-design.md,§9五项已批=09-01「冻结，都接受」,已并入施工方案v1.2作WP-S,WPS作业书DRAFT已预写(TASK-20260901-003/004)）
  - [x] 关窗存档 · 交接档＋架构/使用/维护三手册＋素养库仓手册（授权=用户09-01关窗令;交接档=progress/handoff/2026-09-01__workbench-v2-design-window__handoff.md 为新窗恢复入口,恢复读序在其§七;手册=runbooks/workbench-v2-{architecture,user-guide,maintenance}.md+research-growth-repo.md;已随本次登记面清算批入库，不 push）[TASK-20260901-006]
  - [x] WB-C · WP0 作业书已升 FINAL-v1.0 并在隔离 worktree 完成 Lot A-E（TECH-PASS / CONTROLLER-PASS；未 commit/merge/push，未重启 8899；Claude 异构审与用户 accepted 待办）[TASK-20260901-007]
  - **路线图十项**：H2＝等你拍板收件箱/DDL 雷达/僵尸窗探测/watchdog 自证面/存量五视图聚合；H3＝台账仪式机械化（事件史最高价值）/事件流化/协调面 API 化/通知闭环(happy)/采集器插件市场雏形
  - **升位建议（08-24 夜碰撞事故存在性证明·用户拍板挂账）**：④「协调面 API 化」最小版＝POST /api/index-row 走 WRITE_LOCK＋ledger_edit.py 保形内核；⑤「事件流化」为根治形态（INDEX 行进 events.jsonl 追加＋表格视图化）——两项提为 H2 候选优先，随本行整体待拍板
  - **依据**：`TASK-20260824-005` task log「可拓展方向」附录（含逐项口径）；拍板前不动工
  - **done 类型**：verify-done
- [ ] [topic:dashboard-system] **DS-1 · PIN 按钮（看板）** [blocked:等非 WSL2 环境]
  - **价值点**：让 `dashboard_floating` 桌面悬浮窗能 pin 在最前
  - **验收**：非 WSL2 Qt 环境下 PIN 按钮可见可点
  - **阻塞**：WSL2 Qt 下 `setWindowFlag` 卡死事件循环（已删实现）—— 非 WSL2 环境才能做
  - **优先级**：低（功能性，非核心）
  - **done 类型**：user-ack（需用户切换环境）

- [ ] [topic:repo-infra] **V1 · VPS 双节点 + 甲骨文申请（海外出口 + 防封冗余）** [blocked:等用户拍板与沙箱外实操]
  - **价值点**：单点 VPS ≈ 防御不足（IP 风控 → 全栈断）；双 VPS + 甲骨文 Always Free 为主节点（A）+ 付费低价 VPS 备用（B）+ Tailscale mesh，账号敏感流量与工具流量分离
  - **验收**：
    - 决策档 `progress/decisions/2026/2026-07-31__ops-vps-dual-node.md` ✅ 已落（7-31）
    - runbook `progress/runbooks/oracle-cloud-free.md`（甲骨文 Always Free 申请步骤 · 待建）
    - runbook `progress/runbooks/tailscale-mesh-setup.md`（双节点组网 · 待建）
    - 实际跑通：节点 A 拉起 Clash 规则 + 节点 B 注册 Tailscale + 本地 WSL2 加入 mesh
  - **阻塞**：用户拍板（是否走双 VPS + 甲骨文）；沙箱外（要实操写网站账号）
  - **优先级**：高（与 B6 Clash / C1 Tailscale / C2 Realtime 强绑定）
  - **关联**：NOW §6 V1 · NOW §6 B6 · NOW §5 C1/C2 · 决策档 2026-07-31__ops-vps-dual-node
  - **done 类型**：verify-done

- [ ] [topic:remote-supervision] **RS-1 · 远程监工栈重选 + DMIT 常驻化 + Max 订阅判读**（TASK-20260826-014）：Happy 退役（会话跟随固有缺陷：手机离开 cc 窗口即断推）；驻留原则＝常开海外机跑官方 CLI、本地/手机只当终端；候选＝官方 remote-control 过渡 → tmux 驻留栈/AionUI 二选一；DMIT=CC 常驻开发机（$0 增量）+工作副本 git 同步禁 SSH 回盘+VIRCS 家宽不碰；Max 先 Pro(\$20) 试两周看 Usage 再议 5x，⚠️cometix 非官方二进制×付费订阅张力待拍板；阻塞=T1 Pro 试水/T2 cometix 分工/T3 立项时机（09-10 后排期）三门；详见 decisions/2026-08-26__infra__remote-baseline-and-max-subscription-notes.md · 关联 V1 行/DB-7 行/07-31 ops-vps-dual-node
- [ ] [topic:obsidian-render-debug] **OR-1 · Obsidian vault 路径确认 + 渲染严格调试（v3 重构压力测）**
  - 用户原文：「D:\MyResearch\MAS_Safety_Project\progress\cards\INDEX.md 应该就是直接到这个 progress 啊？0135324bb28bdffe 这里之前问过我，没记录吗？做完之后就调试和压力测一下」
  - **价值点**：验 v3 重构在 Obsidian 端真生效（不是 git-only 漂亮）；验 Dataview GROUP BY purpose 渲染；验跨链接点击；验 v3 spec 设计初衷（3 purpose + 4 护栏 + 3 状态机）
  - **关联 ID**：0135324bb28bdffe（用户提到的某次对话/记录 ID，需定位）
  - **阻塞**：无（功能层 + 架构层双调试）
  - **优先级**：高（v3 收官前必做）
  - **done 类型**：verify-done
  - **调试路径**：(1) 确认 vault 路径 + Obsidian 是否开 (2) 5 文件实测渲染 (3) Dataview GROUP BY purpose 渲染 (4) 跨链接点击 (5) v3 spec 设计初衷复核

- [x] [topic:reuse-catalog] **RC-1 · 建可复用资产目录系统（progress/reuse/）** ✅ 8-12
  - **价值点**：两根约 20 条可复用资产线收进单一权威账本（两级卡片：实体卡 + 资产卡，自动生成总表），吸收 4 份碎片旧账（external/TOOL_REGISTRY.yaml · external/README 分类树 · lines/pending.md 档案馆段 · 8-11 项目总账画布），已拍板约束随卡携带
  - **验收**：`progress/reuse/`（_schema.md + entities/ + assets/ + CATALOG.md）落盘；`tools/scripts/validate_reuse.py` 全量 0 error；CATALOG.md 自动生成且幂等；4 份旧账本标「已被取代」指针；generate.py 重跑无新增 diagnostic —— **全部达成（verify-done 已跑）**
  - **完成记录**：`progress/task_logs/2026/08/2026-08-12__maintenance__reuse-catalog-buildout.md`（TASK-20260812-002）；设计决策 `progress/decisions/2026-08-12__maintenance__reuse-catalog-design.md`
  - **成果**：11 实体卡 + 23 资产卡；浏览入口 `progress/reuse/CATALOG.md`；维护回路 = 改卡 → 跑 validate_reuse.py
  - **done 类型**：verify-done

### 四主题一致性（已完成）

- [x] [topic:progress-persistence] **HV-1 · 修复四主题交接的三类跨文件一致性漂移** [done:2026-08-15]
  - **核验档**：`progress/handoff/2026-08-10__5-four-topic-handoffs-verification__handoff.md`
  - **问题 1**：当前 MCM CSV 真值为 44 条、HIGH=26、MEDIUM=18，但 `progress/task_logs/INDEX.md` 的 `TASK-20260809-003` 行和本 TODO 的历史快照段仍写反
  - **问题 2**：四份 8-10 handoff 实际为 §7 禁止越界、§8 完成判据、§9 默认问句，但 `progress/handoff/INDEX.md` 固定结构说明仍采用旧章节语义
  - **问题 3**：`TASK-20260810-002` 已标 done，但 `docs/superpowers/plans/2026-08-10-four-topic-handoffs.md` 仍为 13 个未勾选项
  - **验收**：两处 MCM 当前口径统一为 26 HIGH / 18 MEDIUM；INDEX 固定结构与当前模板一致；原实施计划勾选完成项或追加 completion amendment；重跑本核验档 §8 检查
  - **边界**：只修共享记录，不修改 EvoAgent/MCM 源码，不推进四条业务线
  - **优先级**：高
  - **完成记录**：`progress/task_logs/2026/08/2026-08-10__maintenance__four-topic-handoff-drift-fix.md`；核验档 completion amendment 见 `progress/handoff/2026-08-10__5-four-topic-handoffs-verification__handoff.md` §10。

### 延后落盘护栏（9 月 W1）

> **状态**：WAITING（不紧急 · MV-1~5 已于 8-2 done，保留原 9 月 W1 节奏）
> **承接**：`progress/runbooks/no-tmp-archive.md`（130→253 行 / 11 节 · 8-2 16:00 落地）
> **背景**：8-2 16:00 立的 11 节护栏已经覆盖主条，这 3 件是边界补强，不强求 8 月做。

- [ ] [topic:tmp-guard-extension] **TG-1 · 沙盒内 /tmp/codex-bwrap-*/ 反弹产物必须经 apply_patch 落仓库** [blocked:等一次 Codex 长任务实证]
  - **价值点**：runbook §2.1 提了沙盒内路径 ≠ 用户视角 /tmp/, 但没说"沙盒产物如何回写"
  - **验收**：`progress/runbooks/no-tmp-archive.md` 新增 §2.2 "沙盒产物回写",明示 apply_patch 唯一渠道
  - **deadline**：2026-09-07（与 MV-1~5 同）
  - **阻塞**：需先看 1 次 Codex 长任务跑全流程,确认沙盒内反弹场景真实存在
  - **done 类型**：commit-done

- [ ] [topic:tmp-guard-extension] **TG-2 · handoff 内的 /tmp/ 死链加废止标记 + 巡检脚本**
  - **价值点**：8-2 凌晨 0:57/0:58 交接档还引用 /tmp/mcm_audit/AUDIT_FINAL.md,新窗口 grep 会撞死链
  - **验收**：(a) `2026-08-02__mcm-audit-cross-session.md` §10 加"权威源已废"段 (b) `progress/runbooks/no-tmp-archive.md` §1 加"已废路径"黑名单 (c) `progress/runbooks/sweep-dead-tmp-refs.sh` 巡检脚本落地
  - **deadline**：2026-09-07
  - **done 类型**：commit-done

- [ ] [topic:tmp-guard-extension] **TG-3 · sed/heredoc 反引号灾难§7 提级为全局铁律**
  - **价值点**：当前只锁在 `2026-08-02__maintenance__forbid-tmp-archive.md` §7.3,subagent 派发时不读这个 task log
  - **验收**：(a) `progress/runbooks/no-tmp-archive.md` 新增 §12 工具雷专章 (b) `AGENTS.md` 工具用法段加 4 行铁律 (c) 派发 subagent 的 4 caps 模板加 `tool: forbidden_sed_heredoc` 一行
  - **deadline**：2026-09-07
  - **done 类型**：commit-done

> **告一段落信号**：护栏 3/4 全部 verify-done + CX-1~4 全部完成；TG-1~3 完成后 runbook 工具雷规则升级。

---

## 挂起学习 + 档案馆可复用 <!-- line:pending -->

> **状态**：PAUSED。此处任务由旧 `lines/pending.md` 清单迁入；想重启某件时，再移入对应业务线。
> **档案馆边界**：`D:\Code` 只读参考，不维护；想复用时再翻。

### 科研方法论（旧 research_growth P1/P2）

- [ ] [topic:pending-research-methods] **PEND-RM-01 · 摘录"如何有效地读论文"**
- [ ] [topic:pending-research-methods] **PEND-RM-02 · 摘录"论文写作模板"**
- [ ] [topic:pending-research-methods] **PEND-RM-03 · 摘录"怎么 rebuttal"**
- [ ] [topic:pending-research-methods] **PEND-RM-04 · 摘录"怎么做学术报告 slides"**
- [ ] [topic:pending-research-methods] **PEND-RM-05 · 摘录"怎么找论文"**
- [ ] [topic:pending-research-methods] **PEND-RM-06 · 摘录"如何给算法 debug"**
- [ ] [topic:pending-research-methods] **PEND-RM-07 · Notion toggle 子块展开（1_想idea的能力.md）**
- [ ] [topic:pending-research-methods] **PEND-RM-08 · 读书笔记目录填充**
- [ ] [topic:pending-research-methods] **PEND-RM-09 · 反思与思考目录填充**

### 技术栈挂起（旧 info 卡片）

- [ ] [topic:pending-toolstack] **B4 · Tavily MCP 接入（等 TAVILY_API_KEY）**
- [ ] [topic:pending-toolstack] **B6 · Clash 规则模式 + GEOIP（阻塞-沙箱）**
- [ ] [topic:pending-toolstack] **C2 · OpenAI Realtime / Fish Speech（等账号）**
- [ ] [topic:pending-toolstack] **C3 · ComfyUI + Flux.1**
- [ ] [topic:pending-toolstack] **E1 · Mem0 中央记忆**
- [ ] [topic:pending-toolstack] **E2 · Apple Health（阻塞-需硬件）**
- [ ] [topic:pending-toolstack] **P4 · Zep vs Mem0**
- [ ] [topic:pending-toolstack] **L1 · CherryStudio 知识库（阻塞-装机）**
- [ ] [topic:pending-toolstack] **L3 · CherryStudio 多模型对比**
- [ ] [topic:pending-toolstack] **M2 · SillyTavern Vector Storage**
- [ ] [topic:pending-toolstack] **VSM-1 · vsummary 本地模型字幕增强复测** [P3] [note:不重要不紧急;启动前准备本地 OpenAI-compatible 模型服务;用 BV1Qa8c6NE7A 复测专名纠错与新增错误;默认不使用付费云 API]

### 档案馆可复用（不维护 · 想用才翻）

- [ ] [topic:pending-archive] **PEND-ARC-MCM26 · MCM_2026（美赛代码 · 看能不能复用 R-hat/SNR 方法 · 不维护）**
- [ ] [topic:pending-archive] **PEND-ARC-GTR · methods / GameTheory_Reproduction（博弈论复现）**
- [ ] [topic:pending-archive] **PEND-ARC-STOCHASTIC · methods / Stochastic_Lab（随机实验室）**
- [ ] [topic:pending-archive] **PEND-ARC-LIVESTREAM · livestream 直播线（旧线 · 可能复用爬虫/动态定价）**
