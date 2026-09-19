---
task: agent_f_onboarding_learning
date: 2026-08-27
artifact_status: DRAFT_READY
claim_status: PREP_ONLY_NO_REAL_E1_SCORE
scope: isolated_onboarding_learning_only
---

# E1 技术匹配话术与首月补课图

这是一份面谈排练稿，不是用户原话记录、能力评级或 E1 成绩。所有“我”句在使用前须由本人确认；没有真人 E1 记录，不能写成“E1 通过”。

## 0. 背景草稿（仅供本人改写）

当前可找到的用户自述草稿是：商科本科，先接触随机运筹优化/博弈论/排队论，后来因可信 AI 议题转向；之后独立检索并拆解相关论文，寻找可信 AI、形式化验证与 MAS 安全的交叉路径。该段来自历史交接材料，未在本任务中独立核验；MCM、Kaggle、既有论文复现等细节只能在本人逐句确认后使用。本稿不把这些细节写进技术 claim。

建议开场保留一个可替换槽位：

> 我的背景是【本人确认的 2–3 句事实】；我转向可信 AI/形式化验证的触发点是【本人确认的 1 句】。

## 1. 三档 E1 talk track

### 30 秒版（电梯开场）

> 我是【本人确认的背景】。我想从可信 AI 走向形式化验证，当前最需要补的是系统安全工程和并发语义。准备上，我按问题、假设、方法、评测和局限拆解了鲁组方向论文，也做过 SegLock 原文核对和 SBPN 公式锚点复算。它们是阶段性、可回查的准备；进组后我想先从一个小型轨迹/PN 复现开始。

使用边界：不报复现成功率，不说完整论文复现、真实 Bridge 已验证或实验室认可。

### 90 秒版（技术匹配主线）

> 我的个人背景和转向原因以我确认的版本为准。技术上，我把鲁组 D2 线理解为一条“找回被主流模型丢掉的因果信息”的路线：PNULock 把运行轨迹编码成 Petri 网并展开，再用伴随构造和确定性重演区分潜在交错与可执行死锁；SegLock 用锁增广分段图、历史锁因果和轻量图算法保留关键语义；MHP/UAF 则从静态分段、值流和约束兼容性补候选过滤。我的准备不是只列论文名，而是统一记录问题、假设、方法、评测和局限，再用原文取证和小规模复算检查自己是否真的理解。能负责地说的是：SegLock 表格有独立双路核对链，SBPN 有公式层和官方数据锚点可复算；不能说成完整论文主实验或真实 Bridge 验证。第一个月我会先补状态/迁移、偏序与 happens-before、Petri 网使能/可达性，再手算 PNULock 的展开和重演；之后按组内优先级转到 MHP/UAF 的静态链。

建议停顿点：说完“能负责地说的是”后等待追问，避免堆项目名。

### 3 分钟版（分段讲，不背论文摘要）

**0:00–0:25｜背景与缺口**

> 我的背景是【本人确认】。我关注可信 AI，是因为【本人确认的触发点】。现在最想补的不是泛泛的安全知识，而是把系统安全工程中的对象、假设、证据和停止条件，落到可执行的并发语义上。

**0:25–1:10｜我做过的可核查准备**

> 我把鲁组方向的论文按问题、假设、建模、判定、评测和局限拆成结构化卡片，并做反事实/对抗性自查。一个具体例子是 SegLock：我把原 PDF 与 PNULock 对应表逐项核对，发现共享基准的时间列存在整列错位，并单独记录了内存栏缺失和可比性边界。另一个例子是 SBPN：公式和官方数据锚点可以复算，但结构挖掘、完整 benchmark 和独立 truth 还没有闭合，所以我只称它为公式/锚点层复算。这个工作方式让我能把“结果是什么”和“证据支持到哪一级”分开。

**1:10–2:05｜为什么和鲁组技术匹配**

> 我看到的共同方法论是：先找现有模型忽略的信息，再把这类信息编码回模型，最后用可解释的离散判定和重演消除一类假阳性。PNULock 的轨迹网、展开、deadlock-adjoint configuration 和授权序列，正好是我需要补的动态并发语义；SegLock 展示了在语义目标不变时怎样退到更轻的图表示；MHP/UAF 又把静态分段、控制流因果和值流约束接上。我的 D2→D1 接口想法是把 D2 输出的反例配置、源汇路径或假阳性环整理成 D1 可接收的异常变量，但目前只是设计/合成契约层，真实 trace 语义闭环尚未证明。

**2:05–2:40｜第一个月怎么补**

> 第一周先补状态迁移、集合/关系、偏序、HB、锁语义和安全/非法终态；第二周手算轨迹网、occurrence net、cut-off 和三分重演；第三周做 MHP 分段属性传播与 UAF 的分段 PN/值流双图；第四周读重演调度器并跑一个 toy prefix-alignment，把每个输入、输出、代价和失败处理写下来。每一步都有二值验收，不以“看过”代替学会；FA/概率副线只有在主线通过后才启用。

**2:40–3:00｜边界与下一步**

> 目前这些是阶段性准备，不是导师认可、完整复现或真实系统验证。若进组，我希望先和老师确认一个小问题的对象、数据和验收门，完成一次可回查的 PN/轨迹复现，再根据结果扩大范围；如果细节当场不能确认，我会先查原文、数据或日志，不猜数。

## 2. 建议的两个技术展示件

### 展示件 A（首选）：PNULock “轨迹 → 展开 → 重演”一页图

- **展示内容**：一条含 `start/stop/join/acq/rel` 的小轨迹；轨迹网的库所/变迁；`deadlock-adjoint configuration` 与非法死标记；配置张成子网和每锁授权序列 `δ`；最后落到真死锁/假死锁/未知三分。
- **为什么匹配**：这是 D2 并发语义的最短闭环，直接对应 S 梯队 02、进组首周手算任务和知识地图 C1–C7、F4/F7；能展示“潜在交错不等于可执行轨迹”的边界意识。
- **现场一句话**：

  > 我想先展示语义链，而不是先报性能数字：模型如何产生候选交错，伴随构造如何编码安全终态，最后由确定性重演把候选分成真、假、未知。

- **准备度**：论文卡和路线已存在；用户自己的手算稿/口头演示尚未在本任务中产生，故标为“可展示骨架，需本人演练后使用”。
- **证据**：`02_DEADLOCK_PNULOCK.md` §2、§5；`STUDY_ROADMAP.md` §二第 2 篇、§四练习表；`STUDY_EXECUTION_PLAN.md` W0-5/W1-1；`STUDY_KNOWLEDGE_MAP.md` C1–C7、F4/F7。

### 展示件 B（第二张）：SegLock Table 5 独立取证与模型边界

- **展示内容**：Table 5 与 PNULock Table VII 的共享基准逐项映射，标出 8/8 的整列上移；另标出 Table 5 缺少 PNULock 内存数据。右侧只写技术含义：表格标签、跨文数值和“内存更低”的文字宣称必须分开。
- **为什么匹配**：它把系统安全工程中的 provenance、可比性和 fail-closed 习惯，连接到鲁组“重模型 vs 轻模型”的路线问题；也正面覆盖 E1-04 的独立取证追问。
- **现场一句话**：

  > 这张图的重点不是证明某个加速倍数，而是说明我怎样发现名实错位、怎样保留残余不确定性，以及为什么不能把原文宣称直接当成完整定量证据。

- **准备度**：A4 终核报告已存在，具体数字使用前仍应打开原报告/原 PDF；真人口头防守尚未运行。
- **证据**：`_audit_remediation_20260824/A4_pdf_verification.md` 核点 1–2；`04_DEADLOCKSEG_SEGLOCK.md` §2、§3、§5；`ONBOARDING_PREP_PACK_20260824.md` §二 M2、§三 A 级话术。

展示顺序建议：先 A 说明技术语义，再 B 说明证据纪律。若对方明确偏静态分析，可把 B 的右半替换为 MHP Figure 3b 的“分段→属性传播→四对真值”草图，但这不是本稿的首选展示件。

## 3. 首月 gap map：从 FV/系统安全基础到并发语义

### 口径先行

知识地图规定“⬜=未学、⚠=读过但没有自己的例子、✅=有自己的例子、✓✓=考过”，且当前统计行和 W0 自评仍为空。因此下表是**首月学习假设与验收路线**，不是对用户能力的定罪或测评结果。

| 进组后阶段 | 要跨的概念缝 | 对应地图/计划节点 | 可交付与二值验收 |
|---|---|---|---|
| 第 1 周（W4） | FV 基础的“状态—迁移—性质—证据”与安全工程的“资产—威胁—边界—停止条件”，接到离散关系、偏序、HB、锁语义 | A1/A2/A4/A5/A6/A7；C1–C5、C9；D1/D7；W4-1 话题 8、W4-2/W4-3 可作入口 | 一页术语/假设表 + 两锁两线程例；能手推 marking/enable/fire，区分 safety 目标与尚未验证的 claim；未知项给出查证路径 |
| 第 2 周（W5） | 从并发直觉进入 PN 语义：occurrence net、完全有限前缀、cut-off、潜在交错与实际可执行性 | C2–C7；F4/F7；W5-1/W5-3；W5-2 FA 仅为可选闸门 | 完成 PNULock 小例手算和授权序 `δ`；能解释 recover、deadlock-adjoint configuration，并输出真/假/未知三分 |
| 第 3 周（W6） | 从动态轨迹转到静态抽象：MHP 分段属性、lock/fork 关系、UAF 控制流/触发/条件三约束、值流与别名边界 | C8/C10；D4；F5/F6；W6-1/W6-2 | 复出 MHP Figure 3b 指定属性集/真值对，画 UAF 双图；能说清“候选并发”与“数据确实到达”的分工 |
| 第 4 周（W7–W8） | 从语义模型到可审计工程：日志 schema、重演代码、alignment move 成本、baseline、失败计入分母和 provenance | C11/C12；D3/D5/D6/D7/D8；F9/F10；W7-W8 T2 最小闭环与迁移考 | 跑通 toy prefix-alignment 或完成调度器数据流笔记；每个输入/输出/代价/失败处理可回查。FA 的 DTMC/PCTL 仅在主线稳定后启用，失败按计划降档 |

### 首月的“补课完成”定义

不是“看过形式化验证”或“熟悉并发”，而是能在一个小例上完成：

`对象/威胁边界 → 状态与迁移 → 因果/互斥关系 → PN/图抽象 → 判定 → 重演或反例 → 证据/失败记录`。

## 4. 两个反向问题（带计划分支）

1. **方向优先级**：

   > 对新成员第一个月，您更建议我先把 PNULock/SegLock 的动态死锁语义补齐，还是先做 MHP/UAF 的静态分段和值流？如果有优先级，我会据此调整第 1–2 周的手算、复现和考核顺序。

   **答案如何改计划**：前者保留 PNULock 展开/重演为首项；后者把 MHP Figure 3b 和 UAF 双图提前，PN 手算降为并行基础。

2. **入口数据与验收**：

   > 组内是否有一个可公开或可申请的真实/半真实并发 trace、固定 baseline 和推荐工具链，适合我在第 3–4 周做一次小型复现？如果暂时没有，我会先做 toy 版，并把它明确标成 artifact-only，而不把它写成真实系统结论。

   **答案如何改计划**：若有合格 trace，优先做 provenance/输入门预检后再跑；若没有，则按 W4 toy prefix-alignment/调度器通读推进，研究 claim 保持不升级。

## 5. 证据、状态与边界台账

### 当前可说到的层级

- 结构化论文拆解、原文取证、公式层复算和可审计实验习惯：可作为准备材料；具体产物归属仍由本人确认。
- SBPN：公式/官方数据锚点可复算；不说完整主实验复现。
- Bridge：设计与合成契约/隔离 artifact 层；不说真实 D2/MAS 语义已验证。
- Lu 接轨：材料与题库已备；真人 E1/E2、真实评分、导师认可均未发生。

### 本稿 claim verdict

`PREP_ONLY`：话术可用于排练和用户自填，不产生新的实验结论、合作关系或个人能力评级。`E1_SCORE = NOT_RUN`。

## 6. 复核收据

### 实际读取的主要来源（绝对路径）

1. `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/ONBOARDING_PREP_PACK_20260824.md`
2. `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/_codex_20260825/onboarding/CURRENT_E1_EVIDENCE_TALK_TRACK_20260825.md`
3. `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/_codex_20260825/onboarding/E1_RESPONSE_SCAFFOLD.md`
4. `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/STUDY_ROADMAP.md`
5. `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/STUDY_KNOWLEDGE_MAP.md`
6. `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/STUDY_EXECUTION_PLAN.md`

Supporting evidence used for technical display/boundary wording:

- `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/02_DEADLOCK_PNULOCK.md`
- `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/04_DEADLOCKSEG_SEGLOCK.md`
- `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/_audit_remediation_20260824/A4_pdf_verification.md`
- `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/repro/sbpn/README.md`
- `/mnt/d/MyResearch/MAS_Safety_Project/progress/handoff/2026-08-26__ai-side-window-closeout__archive/WINDOW-ARCHIVE-20260826.md` (仅用于识别“背景草稿”，非技术 claim 正本)

关键行段索引：准备包 `23–71,73–114`；当前 E1 卡 `8–35,37–101,103–117`；E1 scaffold `7–70`；路线图 `11–28,32–90,98–151`；知识地图 `11–18,20–107,109–140`；执行计划 `12–19,21–63,65–115`；PNULock 卡 `24–49,76–91`；SegLock 卡 `19–80,94–108`；A4 终核 `9–38,40–65`；SBPN 简报 `1–8,25–37,80–93`。

### 读取/核验命令

```sh
cd /mnt/d/MyResearch
find /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813 -maxdepth 4 -type f | rg -i 'onboard|e1|roadmap|knowledge_map|execution_plan'
nl -ba /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/ONBOARDING_PREP_PACK_20260824.md
nl -ba /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/_codex_20260825/onboarding/CURRENT_E1_EVIDENCE_TALK_TRACK_20260825.md
nl -ba /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/_codex_20260825/onboarding/E1_RESPONSE_SCAFFOLD.md
nl -ba /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/STUDY_ROADMAP.md
nl -ba /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/STUDY_KNOWLEDGE_MAP.md
nl -ba /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/STUDY_EXECUTION_PLAN.md
sha256sum /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/{ONBOARDING_PREP_PACK_20260824.md,STUDY_ROADMAP.md,STUDY_KNOWLEDGE_MAP.md,STUDY_EXECUTION_PLAN.md}
test -e /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/learning/ROADMAP.md || echo 'MISSING historical learning/ROADMAP.md reference'
```

### 读取快照（sha256，2026-08-27）

| 来源 | SHA-256 |
|---|---|
| `ONBOARDING_PREP_PACK_20260824.md` | `584a6440fd4d326e7ab8e1a3acff2c07595f865ca9e998f3559d4f4af426c798` |
| `_codex_20260825/onboarding/CURRENT_E1_EVIDENCE_TALK_TRACK_20260825.md` | `a22d5f43657d0e586c66986ce99fe474a25415c097f87979c24fda9c8693548d` |
| `_codex_20260825/onboarding/E1_RESPONSE_SCAFFOLD.md` | `74718095d7c9bd4e075963ddcbb23ab857c9571a71dfa67f2a3814c506153f10` |
| `STUDY_ROADMAP.md` | `0357ff2ba25349cbe57552b306b015c5b1e5bfe12a3cca00ae7dcc773885c01c` |
| `STUDY_KNOWLEDGE_MAP.md` | `23ab6ba19ea8fc1d97ef76c05171e0a43031fb177bfa197fb546719f297e8dc6` |
| `STUDY_EXECUTION_PLAN.md` | `3133ca7526e784e55b1c9cc4f123e8ae1cf30b49354a706619c1508c8d0217e2` |
| `A4_pdf_verification.md` | `e6f1ddf8da380af3b5557c7322aeef50ffcffecb2ef53eaa82b7b48945987967` |
| `repro/sbpn/README.md` | `242badd3727c856b17be152159c36f7f2b1d0c4e97e4b79633850b0505290dab` |
| `WINDOW-ARCHIVE-20260826.md` (背景草稿来源) | `b703c50299f2007feb34e199923cc7b2e1546a42ce815f3db266e0fa317421a2` |

Checkout observed during read: MAS project `HEAD=33b29a5ec35228a3f559a3d4c940cfc5f324f6ed`. The source files above were read-only inputs; no canonical file was edited.

### Artifact-only verification after writing

```sh
TARGET=/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/_codex_20260827/agent_f_onboarding_learning/E1_TECHNICAL_FIT_BRIEF_20260827.md
test -f "$TARGET"
rg -n '30 秒版|90 秒版|3 分钟版|展示件 A|展示件 B|gap map|反向问题|PREP_ONLY|E1_SCORE = NOT_RUN' "$TARGET"
wc -l -c "$TARGET"
sha256sum "$TARGET"
git -C /mnt/d/MyResearch/MAS_Safety_Project status --short -- "$TARGET"
```

## 7. Ambiguities and open gates

1. 用户请求路径写作 `/mnt/d/myresearch`，实际挂载路径为 `/mnt/d/MyResearch`；本收据使用实际路径。
2. 准备包和当前 E1 卡引用过 `learning/ROADMAP.md`，该文件在本次 checkout 不存在；本稿以现存 `STUDY_ROADMAP.md` 为路线源，并保留缺失记录。
3. `ONBOARDING_PREP_PACK_20260824.md` 是历史规划快照；当前状态以 2026-08-25 E1 卡/门禁包为准。两者的 P1/P2/P3/P4 描述不能混读。
4. `STUDY_KNOWLEDGE_MAP.md` 的 57 个节点状态仍为 ⬜/统计空白；首月 gap 是待测学习计划，不是已测能力缺口。
5. “八篇论文”与“七篇家族 + 综合卡”的计数语境不同；口头建议说“方向论文/拆解卡”，避免在数量上被追问。
6. A4 报告已区分文本级确证与数值解释的推断；展示件 B 不应凭记忆补性能数字，必要时现场打开 A4 和原 PDF。
7. 当前没有真人 E1 回答、追问、卡壳记录或评分；本稿不能关闭真人门，也不能产生任何 E1 分数。
8. 背景草稿来自历史用户自述，未在本任务重新确认；所有个人经历、成绩、导师关系和动机仍是用户待填字段。

**最终 artifact verdict：`PASS_FOR_DRAFT`（所需内容齐全，写入范围仅限指定 agent 目录）。**

**最终 claim verdict：`PREP_ONLY / NO_SCORE / NO_CLAIM_UPGRADE`。**
