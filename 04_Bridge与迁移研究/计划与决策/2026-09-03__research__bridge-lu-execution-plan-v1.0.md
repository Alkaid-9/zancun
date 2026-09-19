# Bridge → 鲁组：九月底执行计划 v1.0

**Date**: 2026-09-03 Asia/Taipei
**Task**: `TASK-20260830-004`
**Status**: `APPROVED / READY / NOT-YET-EXECUTING`
**Authority**: 用户 controller 2026-09-03 正式批准（六项决策 + 五项补丁）
**Related**: `learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md`
**2026-09-15 订正**：本文件全文出现的 `09-20`/`09-25` 两个日历日期已被用户脱钩改为条件触发，原文数字保留不改，具体口径见文末 **§13 修订记录**。

> R1 批准。09-20 核心冻结 / 09-25 包检。A-min 默认账本、gate 后解锁。
> 精确 hypothesis、measurement contract、primary metrics 仍需实现前冻结。
>
> **2026-09-15 订正**：见 §13——冻结时点已改为条件触发，不再是日历日期。

---

## 0. 一句话

九月底前，用一条窄而真实的 T2 研究闭环，让鲁老师愿意给出下一单位注意力——不是证明自己成熟，而是证明可以安全地交给一件小事。

---

## 1. 目标与约束

### 1.1 唯一阶段目标

让鲁老师愿意继续交流、看材料、给小任务、允许试做或后续跟进。

### 1.2 最低闭环

```
基础真的学过一块
→ 有一块关键逻辑自己实现
→ 有一个小而完整的实验
→ 关掉 AI 后能讲清楚、改条件、解释结果和边界
```

### 1.3 用户八条（硬约束，09-02 原话）

1. 目的是用一次真实小型研究周期证明有继续培养基础
2. 成果结构 = 已有相关项目作经历背景 + 与鲁组强相关的新研究训练成果
3. 新成果必须有真正跑通的最小闭环
4. 必须体现科研不只是工程
5. 必须确实属于用户
6. 对鲁老师能快速回答四问
7. 九月中下旬是质量检查点，延期换掌握不换架构
8. 允许重新设计乃至放弃 T3/T4

### 1.4 非目标

- 不完整复现 EdgeIM
- 不做 EdgeIM 新方法论文
- 不在本周期做 T4、T3-lite 或 T2→T4 typed relation
- 不把 255 条材料全部核销
- 不重做整个 EvoAgent
- 不把 ProbGuard/VeriGuard/ProMAS 当本实验基线
- 不用 AI 生成量替代用户能力

---

## 2. 决策状态

### APPROVED（用户 09-03 批准）

| 项 | 口径 |
|---|---|
| T2 受保护主产物 | A-min 不得挤压 T2；降级顺序见 §3.2 |
| R1 EdgeIM 采样机制审计 | 当前 T2 核心研究对象（批准研究对象，非批准当前 hypothesis 原样冻结） |
| 09-20 核心技术闭环冻结（原文，**已被 §13 订正为条件触发，不再是日历日期**） | 至少：核心 paper note + CORE foundation + sampling 实现 + primary experiment + 初步 verdict/claim ceiling + ≥1 次 D+2 ownership |
| 09-25 对外包检查（原文，**已被 §13 订正为随核心闭环触发点浮动**） | Sepsis / robustness / D+7 / 美化可落在两者之间或删除 |
| T4/T3-lite/255 条移出本周期 | 保留最小数据合同、历史指针和长期路线 |
| 有限资料取得 | 仅 R1 直接依赖的核心论文与事实源 |
| 工作仓暂名 event-log-sampling-audit | 初期私有；最终名等 ownership/许可检查后定 |
| A-min 默认账本 | Gate = T2 primary experiment PASS + D+2 ownership PASS + schedule green → 才解锁 8–12h |
| OS v0.1 冻结 | 除真实运行暴露 bug 外不修改 |

### OPEN（实现前必须冻结）

- 精确 hypothesis（当前 research question 为中性版本，H1 为候选假设）
- measurement contract（§6.1：sampling / budget / noise / denominator / ground-truth 五单位）
- 2–3 primary metrics + 2–3 diagnostic metrics
- CORE / ADJACENT dependency depth（§5.5）
- failure downgrade 具体触发条件
- EdgeIM PDF 原件是否缺失 [需验证]

---

## 3. 总体结构：T2 主线 + 可裁 A-min

### 3.1 T2 主线（保护对象）

```
读懂核心论文 → 结构化 paper note
→ CORE 基础训练（手算 + 验收）
→ coverage sampling 有边界 clean-room 重实现
→ 合成真值 + 匹配保留规模的采样对照
→ 统一下游 PM4Py IM/IMf
→ primary metrics + 预测→结果→verdict→claim ceiling
→ 24–72h 冷启动与未见扰动
→ 独立研究仓库 + 一页交付 + 边界表
```

### 3.2 A-min（辅助，gate 后解锁）

EvoAgent 默认只保留模块级贡献账本。满足三个 gate 条件后才解锁 8–12h 微切片：

1. T2 primary experiment 跑通
2. 至少一次 D+2 ownership PASS
3. schedule green

降级顺序（时间不足按此砍）：

```
第二真实日志 → 可选新基线（sigRank 等）
→ A-min 深度 → A-min 本身
→ （T2 核心不缩减）
```

---

## 4. R1：EdgeIM 采样机制审计

### 4.1 设计

```
已知过程模型生成的合成日志
→ 多种采样策略（不采样 / 匹配规模随机 / coverage sampling / 频次感知）
→ 相同 PM4Py IM/IMf 下游
→ DFG、PN、alignment 和质量评估
```

研究变量只有"采样策略"。Primary downstream 固定为 PM4Py Inductive Miner (IM)；IMf 仅作 sensitivity check（可选，落在段 4 或删除）。这消除了 Stage 3 未公开 fall-through 和 downstream miner 选择两个混杂效应。

### 4.2 研究总问题（中性）

> 在匹配采样预算下，coverage-based sampling 相比随机/频次感知采样，如何改变合法稀有行为与注入记录错误的保留权衡，并如何影响固定 downstream process-discovery pipeline 的结果？

**H1**（候选假设，非题目预设结论）：coverage sampling 由于"带来新特征即保留"的判据，在噪声日志上倾向放大噪声。

### 4.3 Claim Ceiling

可以说：在指定合成日志、扰动类型、seed 和匹配保留规模下，观察到某种保留权衡。

不能说：coverage sampling 普遍不鲁棒；EdgeIM 存在根本缺陷；结论适用于真实系统。

### 4.4 R2/R3 排除

- **R2（全链复做）**：Stage 3 fall-through 缺失使采样与发现器效应混同
- **R3（agent trace conformance）**：解释成本高、鲁组承接弱、与 AI 辅助 EvoAgent 耦合

---

## 5. 论文阅读与基础

### 5.1 必读

1. **EdgeIM 原文**（Su et al., ICWS 2025, DOI 已核实）：三阶段、coverage sampling、(S,E,R)、中心聚合、未公开细节 [全文取得+实现可用性 需核实]
2. **采样邻居**：至少核对 sigRank（Su et al., TSC 2026, DOI 已核实）及 CrossEdgeIM（IoT Magazine 2026, DOI 已核实）[全文取得 需核实]
3. **Ground truth 方法**：Sommers et al.（Process Science 2025, DOI 已核实）；行为偏差 vs 记录错误、评测需要真值 [全文取得 需核实]

### 5.2 Paper note 固定字段

```
核心 claim / 方法机制 / 看结果前的预测 / 未公开细节
原文 vs 我的推断 / 对 R1 的影响 / 最值得质疑或验证的一点
```

### 5.3 最小知识链

```
event / case / lifecycle / timestamp → DFG
→ PN place / transition / marking / firing → IM / IMf 切分
→ token replay / alignment → model move / log move
→ fitness / precision / F-score
```

### 5.4 验收例

- 空白纸解释 PN 基本概念
- 手算 5–6 活动日志的 DFG
- 从 DFG 画简单 IM 结构
- 对 1–2 条 trace 手算 token replay 或简化 alignment
- 解释 fitness 高不代表 precision 高
- 改条件预测变化

### 5.5 CORE / ADJACENT

按 R1 dependency graph 划分。R1 直接需要的为 CORE（必须硬过），邻接能力标 ADJACENT。不为"知识链完整"吃掉前三天。具体划分在 hypothesis 冻结后确定。

**执行门**：CORE/ADJACENT 未冻结，不得进入正式采样器实现。

---

## 6. Measurement Contract 与实验设计

### 6.1 Measurement Contract（实现前冻结）

以下五项必须在写第一行实验代码前定死：

| 项 | 当前状态 |
|---|---|
| sampling unit（trace / event / 其他） | OPEN |
| budget unit（retained trace count / retained event count / 比例） | OPEN |
| noise unit（noise trace / noise event / noise edge） | OPEN |
| denominator（noise_amplification 的分母定义） | OPEN |
| ground-truth object（生成模型 + 扰动注入 + 标注粒度） | OPEN |

`noise_amplification = 采样后噪声占比 / 采样前噪声占比`——分母不清楚就不许跑。

每项冻结时必须写明：数学定义（含分子/分母）、一个 toy example（≤10 traces）、边界情况（全噪声/零噪声/空集）、对应代码输出字段名、什么结果会导致合同作废或重写。

### 6.2 最小实验闭环

```
question → hypothesis / pre-prediction → input → method → baseline
→ metric → result → alternative → falsifier → verdict → claim ceiling
```

prediction 必须实验前写。不能事后改 rubric。

### 6.3 数据与真值

- **主实验**：已知过程模型生成的合成日志
- 扰动分类（六类）：插入 / 删除 / 相邻交换 / 时间戳粗化 / 标签替换 / 真实行为偏差
- **主实验只选 1–2 类**（段 0 冻结选哪些）；其余为候选扩展，落在段 4 或删除
- 每个日志保留生成模型、扰动类型、比例、seed、case/event identity
- **Sepsis 只作外部压力检查**，不作 ground truth

### 6.4 对照公平性

所有采样器使用相同的 retained budget、下游 IM/IMf、评测日志、seed 集合、参数预算。EdgeIM coverage 输出规模内生 → 必须先定义匹配规模规则。

### 6.5 指标

**Primary**（≤3，待 measurement contract 后冻结）：从 noise_amplification、DFG edge F1、fitness/precision 中选。

**Diagnostic**（≤3）：用于区分 alternative explanation。从 clean-retention、伪边比例、ordering sensitivity 中选。

**候选池（不默认启用）**：conformance 层（alignment cost、log/model move 比例）、efficiency 层（sampling time）——只在明确需要区分 alternative explanation 时纳入。

### 6.6 三级裁定

- **SUPPORTED**：多 seed + ≥2 类扰动下效应稳定
- **REJECTED**：无稳定效应，或 coverage sampling 明显优于对照
- **INCONCLUSIVE**：效应依赖顺序/规模/发现器

负结果和不确定结果都是合格研究输出。

---

## 7. 过程证据与所有权

### 7.1 关键 checkpoint 协议

Pre-note（预测）和 Post-note（CEIACF 六问）只用于重要 research checkpoint：读核心论文、完成基础验收、实现关键算法、跑主实验、做裁定。Mistake entry 只在真出现可迁移错误时写——质量标准：原 belief → 哪个验收打掉它 → 观察到什么 evidence → 正确模型 → 下次 recognition cue；只写"我错了 + 正确答案"不算有效 entry。Boundary update 每日结算或阶段结算。

### 7.2 Ownership 验收

| 时点 | 要求 |
|---|---|
| 当天 | 不看答案解释、说出 prediction、改条件、解释结果 |
| D+2 | 离开对话和 AI summary，只用 repo + 笔记重新接管 |
| D+7 | 复述研究链 + 替代设计 + 最大不确定性 + claim ceiling |

### 7.3 边界表

| 层 | 含义 |
|---|---|
| 能独立解释 / 实现 | 通过 hard evidence + 冷启动 |
| 理解但不能独立实现 | 邻接知识，能解释机制和限制 |
| 知道存在但未系统学习 | 外围，诚实标出 |
| 未验证 | 官方实现、未公开 fall-through、未运行的新基线 |

### 7.4 旧 toy 隔离

`repro/edgeim/`（08-15 AI toy）保持隔离。自己的算法 contract → 自己实现 → 自己跑完主实验 → 自己解释结果 → 然后才打开旧 toy 做 discrepancy comparison。它是历史先验和后验对照，不是答案册。

---

## 8. 交付包

### 8.1 研究仓库（event-log-sampling-audit，初期私有）

```
paper_notes/        ← 结构化论文笔记
foundation/         ← 手算、基础验收证据
experiments/        ← 实验代码与结果
evidence/           ← Ledger、Mistake Log、claim matrix、边界表
README.md           ← 运行入口、数据边界、结论、失败边界
```

数据不入仓，放下载脚本 + SHA-256。独立于 MAS 和 EvoAgent。

### 8.2 对外材料

- 一页技术简报（鲁组 / PM / PN / IM / alignment 语言）
- README（运行入口、实验结论、失败边界）
- 诚实贡献账本（文献 / AI / 现有代码 / 本人决策 / 本人独立实现 分开）
- 边界表
- 冷邮件草稿（不包装成成熟研究者）

---

## 9. 时间盒

默认 6h/日。17–24 天不直接串行相加——必须留 buffer 并与课程现实对齐。

| 段 | 天 | 主要工作 | 降级点 |
|---|---:|---|---|
| 0 决策与资料 | 1–2 | 冻结 measurement contract、核心论文核对 | 新源不全先用已有 |
| 1 基础 + paper notes | 3–4 | CORE 手算、论文笔记 | 减 ADJACENT 不减 CORE |
| 2 采样器实现 | 3–4 | coverage sampling + 基线 + 统一下游 | 先两种对照不追 sigRank |
| 3 合成实验 | 4–5 | 扰动生成、多 seed、primary metrics、裁定 | 减扰动类型不减主实验 |
| 4 外部压力 | 1–2 | Sepsis（仅检查） | 可完全删除 |
| 5 所有权 | 3–4 | D+2/D+7 冷启动、未见扰动 | 先砍 A-min |
| 6 收口 | 2–3 | README、简报、边界表、邮件 | 删装饰不删证据 |

**09-20 core freeze 至少需要**（原文，**已被 §13 订正为条件触发**）：核心 paper note、CORE foundation PASS、自己的 sampling 实现、primary experiment 初步结果、初步 verdict/claim ceiling、≥1 次 D+2 ownership。

**09-25 package check**（原文，**已被 §13 订正为随触发点浮动**）：对外材料齐备、冷启动验收完成。

**段 0 必须产出四张表**（SOL 审查要求）：①核心论文核对表 ②操作化 Measurement Contract ③CORE/ADJACENT dependency graph ④时间倒排与降级表（可用人类小时 → 各 gate 最低小时 → 最坏情况缓冲）。四表完成后 v1.0 从 APPROVED 推进到 EXECUTION-SPEC-FROZEN。

---

## 10. 失败分支

| 场景 | 动作 |
|---|---|
| Stage 3 细节无法确定 | 改报有边界机制审计 + 差异清单 |
| 采样/发现/评测无法分离 | 转 INCONCLUSIVE + 设计失败证据 |
| 冷启动只能依赖 AI/toy | 不公开包装，回到 foundation + 更小自有切片 |
| 时间不足 | 按 §3.2 降级顺序砍，T2 核心不缩减 |

---

## 11. 诚实约束

- AI 先验已知（07_EDGEIM.md §6 假设 + toy 三注记）→ D5 账本显式披露
- 用户贡献 = 独立推导 / 实现 / 预注册 / 解释 / 失败诊断，不是"独立发现假设"
- 旧 toy 保持隔离直到自有实现与初步解释完成（§7.4）
- EdgeIM / sigRank / CrossEdgeIM / Sommers DOI 已核实；全文取得与官方实现可用性 [需核实]

---

## 12. 引用

- 学习 OS：`learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md`
- 提案草案（FABLE）：`progress/decisions/2026-09-03__research__bridge-lu-complete-plan-proposal__fable.md`
- 提案草案（SOL）：`progress/decisions/2026-09-03__research__bridge-lu-complete-plan-proposal.md`
- 09-02 检查点：`progress/decisions/2026-09-02__research__bridge-requirements-realignment-and-edgeim-slice-proposal.md`
- SOL 三档：见 `progress/handoff/INDEX.md` 09-02 三条 SOL 路由
- EdgeIM 事实：`research/papers_lu/teardown-joint-20260813/07_EDGEIM.md`
- 规划日志：`BRIDGE_LU_PLANNING_LOG.md` C-037 ~ C-040
- 用户八条原话：09-02 检查点 §4.2

未通过对应 gate 不得下载超授权范围资料、建仓、写实验代码、跑实验、发邮件、commit/push。

---

## 13. 修订记录

**R1 · 2026-09-15 | 09-20/09-25 日历日期脱钩，改为条件触发 | 用户 2026-09-15 拍板「09-20 本身要往后挪一点」，选定方案「脱钩日历，改成条件触发」 | 依据：`learning/training/lu-edgeim-algo1/BRIEF.md` A9（同步修订）；触发本次订正的背景见 `progress/decisions/2026-09-12__research__four-paper-full-ownership-design-for-sol.md` §6 与 `progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md`**

**背景**：本文件 §2 与文末原写的 `09-20 核心技术闭环冻结` / `09-25 对外包检查` 是 2026-09-03 controller 批准时按彼时工作量估算画的日历日期。2026-09-12 用户拍板四论文全部升级到全文 ownership（EdgeIM 5/5、sigRank/Ground Truth/CrossEdgeIM 均由 4/5 或 3/5 升 5/5），`BRIEF.md` 时间预算随之由 15–20h 改为 22–28h；2026-09-13 `TASK-20260913-001` v3 施工合同据此在磁盘落地建成 `ownership-v3/` 课程包（`BUILT/QA-PASS`，见该合同 §11："09-20 只用于冻结短期 EdgeIM 核心闭环……它不等于四篇全文 OWNED"）。这一工作量变化未曾经用户就 09-20/09-25 两个日期本身重新表态——09-12 设计稿 §6 已指出这条冲突需要用户单独确认，但截至本次订正前一直悬空未决。

**本次裁定**：

1. `09-20 核心技术闭环冻结` 与 `09-25 对外包检查` 两个**日历日期本身作废**，不再以固定日期形式存在。原文数字（本文件 §2、§9、文末三处）保留不改，仅在旁标注指回本节，供追溯当时依据。
2. 冻结时点改为**条件触发**：`ownership-v3/` 四个 EdgeIM 桥接模块——`B-S2`、`B-S3A`、`B-S3B`、`B-EVAL`——的用户侧能力状态（`ownership-v3/BUILD_STATUS.md` 定义的资产轴 `BUILT/QA-PASS` 之外、独立的用户能力轴）全部到达 `PASS` 时，即视为"核心技术闭环冻结"达成，不再依赖任何日历日期。`B-DEFENSE` 与三篇镜头论文（sigRank/Ground Truth/CrossEdgeIM 各自 P0-P3）的全文 ownership 进度不计入本触发条件——它们是长期四篇 5/5 目标的一部分，继续按 v3 合同 §11"长期四篇 5/5"轨道推进，不受此次触发点变动影响。
3. `09-25 对外包检查` 原有"落在核心冻结之后 5 天"的相对位置改为**跟随触发点浮动**：核心闭环条件达成之日即可开始对外包检查窗口，不再锚定固定日历日；具体窗口长度沿用原设计（Sepsis / robustness / D+7 / 美化可落在两者之间或删除），只是起点改为触发日而非 09-25。
4. 本条订正不改变、不豁免本文件 §10 失败分支与 §11 诚实约束里列出的任何证据或降级规则；也不改变 `ownership-v3/` 课程资产轴与用户能力轴禁止互相自动推导的既有规则（v3 合同 §2）——条件触发看的是用户能力轴的 `PASS`，不是资产轴的 `BUILT/QA-PASS`，两者不可混用来宣告触发条件已满足。
5. 待执行的同步动作（本次订正范围之外，留给下一步）：`BRIEF.md` 需追加对应 A9 条目（本次已同步执行，见该文件修订记录）；`progress/projects/lu-side.md`、`progress/projects/jinzu-sprint.md` 两张路由卡的 `last_verified`（停留在 2026-09-05）与 DDL 表尚未反映 `ownership-v3/` 已落地和本次触发条件变更，需要单独一轮更新，本次不动这两张卡。
