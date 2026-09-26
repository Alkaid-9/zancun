# Deep14 下一窗口施工计划（暂停时的提案，不是派工令）

**状态：PROPOSED / PAUSED_BY_USER。** 建档本地日为 2026-09-25 PDT（UTC 已是 09-26）。目标：原 11 篇＋增量 3 篇各自形成可追溯、可质疑的深拆资产；不是把原两天 D1/D2 截止日期顺延，也不是允许现在启动 Agent。当前进度只认 `TASKS.tsv`：ContrAgent 仅 `PARTIAL_SOURCE_REVIEW`，其余 13 篇无本窗口完成的深拆，原 `TB0` 队列仍 `READY`。用户必须**重新明确恢复**，才可执行本文件任何论文、Agent 或实验步骤；继续存档不等于恢复。

## 1. 入场、排程与依赖

1. 从 `HANDOFF_DEEP14_WINDOW_2026-09-25.md` → `TASKS.tsv` → 本文件 → `ARCHITECTURE_DEEP14_2026-09-25.md` 恢复；核对 `git branch --show-current`、`git rev-parse HEAD`、`git status --short`，逐一保留原六项背景 dirty 文件；逐篇重算当前将使用的 PDF SHA-256，对照 `R2_C0_2026-09-25.md`、`DEEP14_WAVE1_DISPATCH_2026-09-25.md` 或 `资料输入清单.tsv`。哈希漂移停该篇并记新来源，不暗中沿用旧结论。
2. 若用户恢复 B 线，先建立缺失的 `B/PAPER_QUEUE.tsv`：14 篇身份、原件路径、旧稿、当前深拆状态、未覆盖页/节和任务 ID 分栏；**仅有 P0 登记不等于论文加工**。更新 `TB0` 前必须对账实际文件，3 篇新增保留 `INCREMENTAL_3` 原身份。A 线需要用户本人回执才能继续 A6/A7，不能让 B 线代写；`EX-06` 仍锁定。
3. Agent 路由只做**一篇/一个节或一个定义/表格的只读短包**烟测，不重投三个全文大包。返回流再断，记 `TRANSPORT_ERROR`，不假定原因、不补造输出或开销；控制器独立读 PDF，单篇串行验收。旧“两天最多 7 活动模型”是历史资源上限，不是新轮次预算授权；本轮默认控制器 1＋至多 1 个只读核查试包，异构复核占既有槽；实际并发与额度必须由恢复时用户约束确认。
4. 按“来源齐备/近期使用价值/依赖”轮转，不设空口 D3/D4 日历：先给 ContrAgent 缩窄复核关口，同时 PNULock、SBPN 各自重新回源；再 String Diagrams / PetriBench；随后九篇原队列按单篇施工卡滚动。**这是候选顺序而非取消另外九篇**。每篇一次只推进一个实证关口；受阻可轮转下一篇，原篇保留 BLOCKED 与精确断点。

## 2. 单篇定义完成：文件、门禁和判定

每篇独立建 `B/papers/<slug>/`，至少有 `README.md`、`sources.tsv`、`claims.tsv`、`analysis.md`、`reuse.md`、`DELTA.md`、`ACCEPTANCE.md`；计算适用才有 `fixtures/`、`expected/`、`src/`、`tests/` 和对应真实 `runs/<run_id>/`。缺文件记未建，不用空模板充数。标准源：`02_逐篇施工与专项验收.md:5-20`、`01_两天执行合同.md:90-131`；术语区分见架构的“双轴合同”。

| 关口 | 可操作验收；达不到时上限 |
|---|---|
| G0 身份 | PDF 本地存在＋哈希、版本、封面/作者、物理页码；旧稿标次级线索；不同源不混引。仅此为 SOURCE_LOCAL/P0，不算深拆。 |
| G1 全文与机制 | 摘要＋贡献＋结论的**主张并集**逐条入 `claims.tsv`，全部论证相关章节标 READ/FOCUSED/NOT_READ；关键定义/图/式/表逐条给物理页和对象号；机制列 input/state/transition/output、前提/不变量/失败、一个独立手推、旧稿差分。漏任何重大贡献或反证记 PARTIAL，不写“全文完成”。 |
| G2 主动质疑 | 至少一组与本篇性质相配的正/负或不可区分对，真值来源与观测字段冻结；一条**同信息、同预算**强简单 baseline，说明何时能击败复杂机制。规格写 `SPEC_ONLY`；独立反例/oracle 真正核过才写 `VALIDATED`。不适用项写明理由并由复核者同意，不机械要求所有理论论文提供可运行基准。 |
| G3 使用/运行 | 接口、前后条件、失败分支、成本与下游消费者明确；有计算断言的提供独立预期和真实命令、cwd、输入/代码 hash、环境、exit、stdout/stderr、差分日志。没有运行一律 `NOT_RUN`；作者表格转录不是复现，模拟算法不是作者 P3。 |
| G4 独立复核和结案 | 独立复核者从原 PDF 而非控制器稿件检查身份、所有拟使用关键主张、定理/数值、至少一条反例与 baseline；`ACCEPTANCE.md` 按关口列证据/失败/未覆盖范围/允许消费的 claim IDs。论文级“完整可复用包”只在 G0–G2、适用的 G3 和 G4 都闭合时裁定；任何一轴 OPEN 均仅 PARTIAL。复核者非运行 oracle。 |

## 3. 全 14 篇的单篇任务、既有输入与完成检查（**全部待做，CA 仅部分**）

原件/旧稿准确相对路径优先查 `资料输入清单.tsv`，新增三篇查 `R2_C0_2026-09-25.md`；如下为每篇**未来复核焦点**，不是研究结论。基础细目另见 `02_逐篇施工与专项验收.md:22-105`、`07_第二轮研究动态_三论文拆解与JINZU应用计划.md`。

| task / 输入身份 | 当前状态 | 本篇必答问题 / 最小强核查 | 后续关口 |
|---|---|---|---|
| D14-EDGE / SRC_EDGEIM | QUEUED | 原 Algorithm 1 排序、S/E/R、停止/返回；结构覆盖≠频次；独立 210 日志枚举核对建议 `EI-T1..T4`；与本人 EX-05 答案隔离 | G1 原机制 + G2 同覆盖异频次；运行另过 G3 |
| D14-SIG / SRC_SIGRANK | QUEUED | 评分/并列及预算 K 回原式；与 EdgeIM 信息合同/预算对齐，不虚构精确排序 | `SIG-T1..T2`、G1/G2 |
| D14-GT / SRC_GT | QUEUED | 世界真实行为、记录噪声、采样干预三轴；标签独立于待测策略 | `GT-T1..T2`、G1/G2 |
| D14-CROSS / SRC_CROSS | QUEUED | 活动/组织/中心三层、delta、字节和隐私；乱序/丢失没有原文保证则 UNKNOWN | `CX-T1..T3`、G1/G2 |
| D14-PNU / SRC_PNU | WORKER_TRANSPORT_ERROR/QUEUED | 原定义 1/3/4/5、recover 前后集、合法/非法终态、cut-off、按锁调度到真实重演上限 | `PNU-T1..T5`、G1/G2；原 worker=0 成果 |
| D14-SEG / SRC_SEG | QUEUED | 分段对象、重复加锁轮次与释放、表面锁环/真实可实现条件 | `SEG-T1..T3`、G1/G2 |
| D14-JOS / SRC_JOS | QUEUED | 原作锁增广分段图；与后作差分**双向**回源，不以家族图顶替 | `JOS-T1`、G1/G2 |
| D14-MHP / SRC_MHP | QUEUED | 六属性/规则，fork/join/lock 与漏对的最小可枚举时序 | `MHP-T1..T2`、G1/G2 |
| D14-UAF / SRC_UAF | QUEUED | 分配/释放/use、对象身份、值流与并发过滤；告警≠漏洞已复现 | `UAF-T1..T2`、G1/G2 |
| D14-SBPN / SRC_SBPN | WORKER_TRANSPORT_ERROR/QUEUED | 式 (6)–(9)、定理 1/2、独立手算 `.8/.15/.475/.82`、协同独立性/阈值条件 | `SBP-T1..T6`、G1/G2；原 worker=0 成果 |
| D14-SBTPN / SRC_SBTPN | QUEUED | 时序/滞后/根因，SBPN→SBTPN 五项**双源**差分，补充材料身份 | `STP-T1..T3`、G1/G2 |
| D14-SD / R2_STRING_DIAGRAMS | QUEUED/PDF_HASH_ONLY | 四 notation、签名定理前提、recovery study；相同 trace 不推等价 signature | 原 PDF 再核，G1/G2；旧 v2 文档不可直接当真 |
| D14-CA / R2_CONTRAGENT | PARTIAL_SOURCE_REVIEW | 36 个候选主张已列；先审 p.3 公式上划线、表 2/3/8 分母、两对反例**全 AP 轨迹**及 object-aware FSM；host-effect 是推断 | `B/papers/contragent/ACCEPTANCE.md:17-25` 的 1–4＋G4；可运行需第 5 关 |
| D14-PB / R2_PETRIBENCH | QUEUED/PDF_HASH_ONLY | 六任务定义/有限与无限性质、exact oracle、难度分层；有限 BFS 不证明全局有界 | 原 PDF 再核，独立金标与 `P2/P3` 分轴 |

## 4. 分工、成本、停机、交接

- **主控 M**：唯一写入者/任务状态决策，保存实际 PDF 坐标、对照旧材料、裁定门禁；**只读 Agent**：一个冻结输入＋一个狭窄问题，`fork_turns="none"`，一次终态，仅返回候选和未覆盖范围；**独立复核者**：用原件直接反驳主控的关键句、反例及表格，不以同模型复述或作者自报替代 oracle；**学习者**：只本人产生 EX-05/R1 证据；**用户**：明确是否重启、实验/外联/服务器/超旧写域是否另授权。
- 实际观察：三次 `gpt-5.6-sol / xhigh` 只读 Agent 均传输失败，token/费用 **UNKNOWN**；下一包先固定 1 个极小问题＋中止线。预计 14 篇深拆需多轮人工核源/复核，**不编造人时/金额或“一天全完成”承诺**。每个工作单元停在可验收的小节；缺来源、哈希变化、关键公式不清、来源冲突、连续短包错误时记录 BLOCKED 与精确下一步，不作无证据重试。
- 每篇完成一关才在 `TASKS.tsv` 更新该行的 evidence/next_action；必要时新增独立 reviewer 收据，包含任务 ID、日期、来源 SHA、引用页码、实际运行 ID、OPEN 与结论上限。一次只提交属于当前包的文件；不 `reset/clean` 全仓，不擅自提交/推送；原六项 dirty 不能以本窗口归档覆盖。
- **回滚/停机**：同一文件出现冲突先停该篇，保存冲突双版本/哈希；有错的 claim 降级为 UNKNOWN 并检视依赖引用，不直接删整包。任何材料被学习者正式题面污染则停止释放并另走课程验收路径。本计划不改变现有暂停态。
