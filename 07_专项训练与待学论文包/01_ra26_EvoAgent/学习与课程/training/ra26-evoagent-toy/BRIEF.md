# 训练包 ra26 · EvoAgent trace → PM4Py toy：工程 + 科研混合

**训练对象**: `D:\MyResearch\EvoAgent`（资产卡 RA-26，baseline `ef768b5`）+ PM4Py 工具链
**这是什么性质的包**: 和 ra28 相反——**不能动的代码**（EA-4 护栏）+ **没用过的工具**（PM4Py）。练的是真实科研工程里最常见的两个处境：在只读约束下做采证判断；快速上手一个领域工具并做出可信的第一个实验。产出直接是方向 A 的 P0 toy（9 月邮件证据）。
**主训练模式**: 盲做先行 + 对账（EX-01）· 角色反转 code review（EX-02）· 先写后审（EX-03/04）

---

## §0 开箱清单（新窗口第一动作）

1. 读 `learning/training/00_SYSTEM.md` §2/§3 + 查 `LEDGER.md` 断点。
2. **待确认项**：`DEC-REUSE-ROLLOUT-E3`（decisions/PENDING.md）——跑 EvoAgent rollout 若需 LLM key/联网，需用户放行；未放行则 EX-01 只做静态采证（BRIEF 已设计两条路径）。
3. **环境前置**：MAS 仓侧建工作目录 `research/pm4py_toy/`（脚本、数据、报告都落这，**EvoAgent 仓零写入**）；Python 环境装 `pm4py`（独立 venv 或 solver env，装好跑 `import pm4py` 冒烟）。
4. **输入白名单**：`EvoAgent/evoagent/observability.py`、`harness.py`、`rollout.py`、`agents.py`（只读）；EA-6L 切片 `learning/case_studies/evoagent/00_LEARNING_MAP.md` 的 D4/D5 两节（rubric 参照）；PM4Py 官方文档。
5. **禁读清单**：本包 `_sealed/`；`progress/reuse/assets/RA-26__evoagent-research-bridges.md` 正文（有预写的接驳结论）；旧方案档 §1（有预写的采证问题清单）。
6. EX 顺序 01→04。EX-01 前先派 Setter。

## §1 训练目标与毕业判据

| 能力 | 通过 EX | 毕业判据 |
|---|---|---|
| 陌生代码结构侦察（只读约束下） | EX-01 | 三要素判定与密封采证结论一致率 ≥70%，且 GO/PATCH/NO-GO 建议论据充分 |
| 数据工程（转换脚本 + 自测） | EX-02 | 脚本一次通过 AI review 无 P0/P1；自测覆盖三要素缺失/乱序/重复三类脏数据 |
| 领域工具上手 + 实验设计 | EX-03 | 独立跑通 discovery + conformance，参数选择能说出为什么 |
| 科研写作（证据分层、不越层） | EX-04 | toy 报告被 Grader 判"零越层结论"，且含明确的"本 toy 不能证明什么"一节 |

## §2 练习序列

### EX-01 · trace 采证判断（90 min）｜首铸卡：陌生代码结构侦察

**题面**：目标 = 回答一个工程判断题："EvoAgent 的 trace 能不能喂 PM4Py？"
1. （0-60 min）只读四个白名单文件，回答：① trace 在哪产生、什么格式、落到哪？② 有没有过程挖掘三要素——case id（一次运行/一个任务的边界标识）、activity（状态或动作名）、timestamp？各对应源码哪个符号（file:line）？③ 事件粒度对 discovery 是太粗/太细/合适？
2. （60-80 min）产**判定报告**：GO（三要素齐，直接转换）/ PATCH（缺什么字段，在 MAS 仓侧怎么包装补齐——给包装方案草图）/ NO-GO（为什么不可用，缺口清单）。每条判断带证据标签（STATIC-CONFIRMED 要有行号）。
3. （80-90 min）若 E3 已放行：跑一次最小 rollout 拿真 trace 样本，对照你的静态判断（RUNTIME-CONFIRMED 升级）；未放行则写"需运行验证的存疑点"清单。
**交付物**：`research/pm4py_toy/EX-01_采证判定.md`。
**hint**：H1"trace 的写入点不止一处/只有一处，数清楚"→ H2 指模块 → H3 给三要素中一个的答案。
**rubric**：三要素判定正确性 40% · 坐标精确度 20% · GO/PATCH/NO-GO 论证 25% · 越层扣分 15%（静态读码就敢下"能跑"结论 = 越层）。
**Setter 需求**：有——独立做同题采证，密封判定报告（Grader 对账分歧点；你和 Setter 结论都可能错，运行验证是最终裁判）。
**铸卡点**：《陌生代码结构侦察》v0.1（入口选择：从数据落点倒推 vs 从入口正推；符号追踪法；何时停——回答判断题所需的最小读码量）。

### EX-02 · trace→XES 转换脚本（90 min）｜磨卡：判断代码 work 五步（对自己的代码用）

**题面**：按 EX-01 的判定（GO 或 PATCH 路径）写转换脚本：输入 EvoAgent trace（真样本或按 schema 构造的合成样本），输出 PM4Py 可读 XES/CSV。**工程要求**：① 自带自测——至少覆盖三类脏数据（字段缺失/时间乱序/重复事件）的处理决策（丢弃/修复/报错，你定并写明理由）；② README 三行（用法/输入假设/已知限制）；③ 对 ra28 EX-05 的 log 格式**留兼容位**（四字段 case/activity/timestamp/agent——那边的数据之后要进同一管线）。
**交付物**：`research/pm4py_toy/convert/`（脚本 + 测试 + README）。
**批改形态**：角色反转——AI 对你的脚本做正式 code review（P0-P3 分级）；你修一轮（封顶 2 轮）。
**rubric**：一次过无 P0/P1 50% · 自测的"能判死"程度 30% · 边界决策的理由质量 20%。

### EX-03 · PM4Py 实验：discovery + conformance（90 min）｜首铸卡：证据分层写作

**题面**：
1. （0-30 min）学：XES 结构、inductive vs heuristic vs alpha 的适用差异（写 5 行对比笔记，够用即可，别陷进去）。
2. （30-75 min）做：inductive miner 跑 EvoAgent event log → 出流程图；以 `harness.py` 状态机为参照模型做 conformance → 记录 fitness / precision；**若 ra28 EX-05 已完成**：黑板拓扑 log 跑同一管线，出对照流程图。
3. （75-90 min）写：每个指标一句话解读 + 证据标签。关键纪律：fitness 低 ≠ "代码有 bug"——先分诊是 log 质量问题 / 参照模型抽象层级问题 / 真实偏差，写出你的分诊过程。
**交付物**：`research/pm4py_toy/EX-03_实验记录.md` + 图。
**hint**：H1"参照模型和 log 的 activity 命名对上了吗"→ H2 给对齐方法 → H3 给指标解读框架。
**rubric**：管线跑通 30% · 参数/算法选择有理由 20% · 指标分诊质量 35% · 越层扣分 15%。
**铸卡点**：《证据分层写作》v0.1（每个数字带：怎么算的/输入是什么/能支撑什么结论/不能支撑什么）。

### EX-04 · toy 报告定稿（60-90 min，衔接产出）

**题面**：把 EX-01~03 合成 `research/pm4py_toy/TOY_REPORT.md`：动机（方向 A 一句话）→ 数据（trace 来源与转换决策）→ 方法（算法与参数）→ 结果（流程图 + 指标 + 对照）→ **"本 toy 能/不能证明什么"**（必须有——这节的质量直接决定 9 月邮件里这个 toy 是加分还是翻车点）→ 下一步。全文每个数字按《证据分层写作》卡执行。
**批改形态**：Grader 按"审稿人视角"过一遍（专挑越层结论和无出处数字），一轮修订。
**产出衔接**：报告定稿 → 9 月邮件素材（OE-1 引用）；报告的"下一步"节 → 方向 C（Discover→Model）的接口。

## §3 Agent 派单要点

- **Setter（仅 EX-01）**：输入 = 四个白名单文件 + EX-01 题面；输出 = `_sealed/EX-01_answer.md`（独立采证判定）；caps = EvoAgent 仓只读、零剧透。
- **Coach**：同总纲；本包 EX-03 的 H3 可给"指标解读框架"但不代写分诊。
- **Grader**：EX-01 对账采证分歧；EX-02 走正式 code review 协议（P0-P3 + 两轮封顶）；EX-03/04 按"审稿人视角"（越层零容忍）。
- 全部继承 8-12 纪律；**EvoAgent 仓对所有角色只读**（EA-4）。

## §4 产出衔接

TOY_REPORT.md = 方向 A 的 P0 交付（9 月邮件证据）；转换脚本 = 可复用管线（ra28 对照数据、未来任何 agent trace 源共用）；conformance 分诊记录 = 方向 C 的 Observe→Discover 环节首个实例。

## §5 死线降级

toy 是 9 月邮件的支撑性证据（非阻断项）。若 8 月底仍未到 EX-03 → 启用旧方案档 §1 拓扑（T1/T2 代做），你转逆向训练：review Agent 的转换脚本 + 独立复算一遍 conformance 指标（复算能力本身是毕业判据的一部分）。

## §6 红线

- EvoAgent 仓零写入（含临时文件）；一切产物落 `research/pm4py_toy/`。
- rollout 涉 LLM key/联网 → 等 DEC-REUSE-ROLLOUT-E3，未放行不跑。
- F1 82.5% 等 EvoAgent 历史数字如需引用，必须带"合成基准"口径（不因为是训练就放松）。
- toy 报告对外引用前过 EX-04 的审稿人批改（未过审的版本不进邮件素材）。
