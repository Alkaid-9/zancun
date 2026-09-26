# Deep14 本窗口暂停交接 · 2026-09-25（America/Los_Angeles）

> **控制态：PAUSED_BY_USER；仅本窗口存档。** 本地核验时间 2026-09-25 19:14 PDT = 2026-09-26 02:14 UTC；记录跨 UTC 日期，不回填为 09-22/23 的 D1/D2 产物。用户最后明确说“停一下，写一下交接文档”，因此不再派 Agent、不继续读下一篇论文、不跑研究实验或改学习者文件。本文件是窗口交接入口；论文进度以同目录 `TASKS.tsv` 的当前行及各篇 `ACCEPTANCE.md` 核对。本交接不是论文验收，也不恢复生产授权。

## 0. 怎样恢复上下文（先后顺序）

1. 当前项目根入口：`/mnt/d/Alkaid/Desktop/zancun/00_先看这里.md` → `10_双线材料加工与研究准备_2026-09-20/00_START_HERE.md`；两入口顶部现均设本交接指针，旧行内的“D1=2026-09-22 / D2=2026-09-23、EXECUTING”是历史两天包措辞，**不得覆盖本次暂停令**。
2. 先读本文件，再读 `00_control/TASKS.tsv` 中 `D14-*`、`R2_INCREMENT`、`TB0` 行和 `00_control/DEEP14_SCOPE_2026-09-25.md`。旧 `03_两天任务看板.tsv` 是 planning snapshot，不是执行状态。
3. 查证原始输入与派工失败：`00_control/R2_C0_2026-09-25.md`、`00_control/DEEP14_WAVE1_DISPATCH_2026-09-25.md`、`00_control/DISPATCH_SPECS_2026-09-25.md`。
4. 唯一新论文包：`B/papers/contragent/README.md` → `sources.tsv` → `claims.tsv` → `analysis.md` → `DELTA.md` → `reuse.md` → `fixtures/predicate_blindspot_pairs.json` → `ACCEPTANCE.md`。它是 **PARTIAL**，请先读 `ACCEPTANCE.md` 的开放门禁。
5. 本窗口的完整操作日志与文件清单见 `00_control/WORK_LOG_DEEP14_2026-09-25.tsv` 和 `00_control/WINDOW_ARCHIVE_MANIFEST_2026-09-25.tsv`；后者为文件完整性清单，不证明内容正确。
6. 后续施工、目录/角色/数据流、日常阅读和维护分别见 `NEXT_PLAN_DEEP14_2026-09-25.md`、`ARCHITECTURE_DEEP14_2026-09-25.md`、`USER_GUIDE_DEEP14_2026-09-25.md`、`MAINTENANCE_DEEP14_2026-09-25.md`。这些是**暂停状态下的下次执行方案**，不是已经启动的后续波次。

## 1. 需求变更与属于哪条线

- 用户先问 zancun 进度，后澄清重点是 **AI 后台可做/未做、论文拆解要与本人学习并行**；对先前“原 11 篇仅 P0＋PNULock/SBPN P1”的深度不满意，明确要求 **全部 14 篇逐篇深入拆**，允许“一个一个来”或多 Agent 并行。这改变 B 线论文加工的**目标深度**，不追认旧两天包已经完成，也不把九篇直接标 P1/P2。
- **A 线（本人近期学习材料）**：本窗口没有修改 A/D1、旧 EdgeIM 作答、原 MAS 课程或本人能力判定。先前 A0–A5 材料 READY/材料复核通过，但本人首次运行 NOT-STARTED、R1 指定提交缺失、EX-05 WIP/PASS 未裁定、EX-06 LOCKED。A6/A7 必须等真实本人回执；详见 `00_control/REVIEW_D1.md:29-39`。不能用本窗口 AI 论文工时抵本人学习。
- **B 线（14 篇 AI 论文深入加工）**：原 11 篇及第二轮 3 篇各有独立身份。当前一个 ContrAgent 仅有控制器来源审阅 **PARTIAL**；其余 13 篇没有新深拆包。TB0 的 `B/PAPER_QUEUE.tsv` 仍不存在。14 篇深拆的新授权记录在 `DEEP14_SCOPE_2026-09-25.md`，逐篇排队状态只认 `TASKS.tsv` 的 D14 行。
- **CONTROL/REVIEW 线**：本窗口冻结输入、记录任务/派工、失败、状态与交接；三次子代理请求**全部传输失败且无可用论文输出**；没有异构独立论文复核通过。
- **研究综合/外部行动**：跨论文 bridge、novelty、toy、Fable 教学转换、Gemini 生产门禁、LearnGraph 服务器部署、外联/简历/邮件均不属于本窗口已完成工作；未触及服务器、账号、旧课程 Ledger、sealed/holdout。

## 2. 本窗口确实做过（严格限定）

1. 在已有的历史合同、施工卡、任务表、14 篇工作池中确认：旧两天硬交原为 11 篇 P0 与两篇 P1，新增三篇是独立增量；原 P2=全文可复用包，而第二轮能力管线 P2=主动证伪，两者同名不同义。该发现记录在新 scope，旧合同未被静默重写（`01_两天执行合同.md:90-113`；`03_PAPER_TO_CAPABILITY_PIPELINE.md:11-22`）。
2. 开工前读出 Git HEAD、分支和现存的 3 个 tracked 修改＋3 个 untracked 文件；重新计算 PNULock、SBPN 与第二轮三份 PDF 哈希，其中三份第二轮映射落入 `R2_C0_2026-09-25.md`；建三份**仅表头** claim ledger。它们是基线/预留，不是原文主张已核。
3. 对 PNULock、SBPN、ContrAgent 分别派 1 个自包含、只读、无子代理的深拆任务；实际环境固定子代理为 `gpt-5.6-sol / xhigh`，并**非**用户提议的 `gpt-6-sol / xhigh`。三者均返回 `stream disconnected before completion: Transport error: network error: error decoding response body`；无有效研究报告、无可见准确用量，未自动大包重试。参见派工失败回执。
4. 失败后主控仅自行读完 ContrAgent **13 个物理 PDF 页**，渲染检查 Eq.(1)–(3) 所在 p.3、Table 2/3 所在 pp.6–7、Appendix E/F 表所在 p.13；读旧管线相关段落和旧交叉核验，区分一手/旧稿；新建一份来源包（36 条 claims、机制与四评测分轴、2 对**仅规格**反例、可复用接口及旧稿差分）。检查过两对反例 JSON 可解析，但**没有运行算法、监视器、作者程序、基准或独立 oracle**；独立审查仍 OPEN。详见该包 `ACCEPTANCE.md`。
5. 追加 `D14-*` 共 14 个纸面排队行和 `D14-W1` 失败行至任务表；`R2_INCREMENT` 上限改为 `PARTIAL_SOURCE_REVIEW`。用户发出“停一下”后，将 `D14-SCOPE` 改为 `PAUSED_BY_USER`，只进行本交接存档。此前的 `T00/TA1/TA2/TA4/TV1/TB0` 历史行未追溯改动。

## 3. 未完成、不得声称完成

| 对象 | 截止本窗口关闭的真实上限 | 未闭合的必要动作 |
|---|---|---|
| 14 篇整体 | 14 个排队条目；仅 1 个 ContrAgent PARTIAL 来源包；0 篇完全验收 | 逐篇 PDF 来源/主张/机制/主动反例/强简单基线/适用时的可运行证据与独立复核；不强制错误宣传 14 篇已 P2/P3 |
| ContrAgent | 13/13 PDF 页读过，36 条 source-mapped candidates；作者实验是转录，2 对 local fixtures 仅规格 | 更窄的独立 reviewer 核心公式/表格/反例；验证对抗例与对象感知 FSM；作者代码和数据若要复现须另过授权、来源与运行门 |
| PNULock / SBPN | PDF 哈希冻结；原只读 worker **无结果** | 各自新开小的可检验原文单元；旧稿不能抵回源；无 P1/P2 深拆通过 |
| PetriBench / String Diagrams | PDF 哈希与身份映射冻结；预置 claim ledger 只有表头 | 未派新深拆、未审各篇形式/定理/实验/局限；不得因旧局部 Luna 回源报全篇完成 |
| 原队列另九篇 | 已有旧输入路径和 D14 队列占位；本窗口无逐篇新包 | 逐篇回源，并建立来源、机制、反例/失效、复用和验收文件 |
| 用户学习 / A6/A7 | 历史 A0–A5 材料 READY；无新本人回执 | 用户自行决定开学时间、做 R1/EX-05 预测与首次运行；AI 不代写、不倒填 PASS |
| 代码/测试/研究 toy | ContrAgent fixture 只有 JSON 规格；无 runs/ 与真实退出码 | 明确协议、独立预期与授权后才运行；现在 NOT_RUN，不能称再现/证明新颖 |

## 4. Git 与环境边界（可审计）

- 仓库：`/mnt/d/Alkaid/Desktop/zancun`，分支 `audit/redteam-external-ref-2026-09-20`，起点和暂停检查 HEAD 同为 `6f31e797b3cf6210ba4f5389b53c03ebcabf3c11`。本窗口**未 commit / push / stage / 切分支 / reset / clean**。
- 进入本窗口前已有的 6 个 dirty 路径：`.claude/gemini-guard/test_guard.py`、`.claude/gemini-guard/worker.py`、`GEMINI_WORKER_CONTRACT.md`（tracked 修改）；`.claude/gemini-guard/README.md`、本包根 `DRAFT_00_OBJECTIVES_AND_CLAIMS.md`、`DRAFT_04_BRIDGE_LU_SUN_OPENAI.md`（untracked）。这些**不是本窗口产物**，不得纳入我们的交付计数或误删。`00_control/BASELINE_2026-09-22.md:21-32` 也记录同类旧背景差异，但须以本次实测 Git 状态为准。
- 本窗口修改既有文件仅 `00_control/TASKS.tsv`（追加 14 深拆行及新控制行，并改一条增量状态）、根 `00_先看这里.md` 与包内 `00_START_HERE.md`（两者均只增加暂停指针）；其余本窗口文件均新建于本包 `00_control/`、`B/papers/contragent/`。来源 PDF `/mnt/d/Alkaid/Downloads/` 与旧 11 篇仓内 PDF 均未修改；原 MAS 仓只读。
- 当前机器观测本地 2026-09-25 19:14 PDT；UTC 已跨 2026-09-26。Windows 路径为 `D:\Alkaid\Desktop\zancun\10_双线材料加工与研究准备_2026-09-20\`。请避免把历史 D1/22、D2/23 当当前的日程或执行凭据。

## 5. 下一窗口何时可继续

只有用户再次明确要求恢复深拆后，才按 `NEXT_PLAN_DEEP14_2026-09-25.md` 对账：先重读本交接和 `TASKS.tsv`、核 HEAD/status/源哈希、查看本包现有文件有无被其他窗口改动，然后**只开一个范围明确、输出可验的小任务**来验证 Agent 路由或由主控逐篇做。不得直接重投三个全文大包，不先跑旧 D1 学习脚本，不动 Gemini HOLD 或其他窗口配置。收到新的用户约束时以最新用户指令为准，将新增决策写在下一回执；本交接仅保存目前状态。
