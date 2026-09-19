# Bridge → 鲁组：九月底完整计划提案（FABLE）

**Date**: 2026-09-03 Asia/Taipei
**Task**: `TASK-20260830-004`
**Type**: integrated research / learning / delivery plan proposal
**Status**: `PROPOSED / FOR-REVIEW / NOT-FROZEN / NO-EXECUTION-AUTHORITY`
**Window / author marker**: `FABLE`（Claude Code 主窗，claude-fable-5）
**Parallel plan**: SOL 版见 `2026-09-03__research__bridge-lu-complete-plan-proposal.md`（同日，437 行；两档独立、不覆盖）
**Related frozen method**: `learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md`

> 本文件是供用户审阅的完整计划草案，不是执行授权。
> 除用户明确批准对应项外，不开始下载、安装、实现、实验、建公开仓、发送邮件或提交代码。

---

## 0. 一句话

九月底前，用一条窄而真实的 T2 研究闭环，让鲁老师愿意给出下一单位注意力——不是证明自己成熟，而是证明可以安全地交给一件小事。

---

## 1. 目标与非目标

### 1.1 唯一阶段目标

让鲁老师愿意继续交流、看材料、给小任务、允许试做或后续跟进。

不要求一个月学完过程挖掘 / Petri net / 形式化验证，不要求做出完整论文，不要求面对任何问题都能回答。

### 1.2 最低可交付闭环

```
基础真的学过一块
→ 有一块关键逻辑自己实现
→ 有一个小而完整的实验
→ 关掉 AI 后能讲清楚、改条件、解释结果和边界
```

### 1.3 用户八条目标条件（09-02 原话，本计划的硬约束）

1. 目的是用一次真实小型研究周期证明有继续培养基础，不是临时包装邮件
2. 成果结构 = 已有相关项目作经历背景 + 与鲁组强相关的新研究训练成果
3. 新成果必须有真正跑通的最小闭环
4. 必须体现科研不只是工程
5. 必须确实属于用户
6. 对鲁老师能快速回答四问（为何相关、做了什么、到哪一步、下一步怎么指导）
7. 九月中下旬是质量检查点，延期换掌握不换架构
8. 允许重新设计乃至放弃 T3/T4

### 1.4 非目标

- 不完整复现 EdgeIM
- 不做 EdgeIM 新方法论文
- 不在本周期实现 T4、T3-lite 或 T2→T4 typed relation
- 不把 255 条材料全部核销
- 不重做整个 EvoAgent
- 不把 ProbGuard/VeriGuard/ProMAS 当本实验基线
- 不用 AI 生成量、运行次数或报告页数替代用户能力

---

## 2. 已锁定 / 待批准 / 待冻结

### LOCKED（用户已明确）

| 项 | 口径 | 出处 |
|---|---|---|
| 阶段主目标 | 九月底可以不虚地联系鲁老师 | OS §1 |
| 资源优先级 | T2 受保护主产物；A-min 可降级 | 用户在 SOL 窗选 A |
| 研究主轴 | T2：事件日志 / DFG / PN / IM / alignment / conformance | 用户"T2 做深做实" |
| 论断边界 | 不称"完整复现 EdgeIM"；claim 不超过 evidence | 用户八条 §4 + OS §13/§15 |
| T4/T3-lite | 撤出本周期 | 用户"T2 做深做实，一步一步来" |
| 学习协议 | 裸机先手 → AI 辅助 → 关答案重做 → 冷启动复测 | OS §7 |
| 每日硬训练 | 至少一次可能判错的验收 | OS §3 |
| OS 状态 | v0.1 FROZEN 2026-09-03 | 用户确认 |

### PROPOSED（两窗推荐，用户未正式批准）

| 项 | 推荐 | FABLE 立场 |
|---|---|---|
| T2 研究对象 | R1 EdgeIM 采样机制审计 | 支持（变量隔离最干净） |
| 切片称呼 | "T2 基础切片" / "replication-plus learning study" | 接受 |
| Toy 处置 | 披露先验的代码隔离（非封存） | 接受 |
| 检查点日期 | 09-20 内部冻结 / 09-25 对外包检查 | 同意 |
| A-min | 8–12h 封顶可裁工程微切片 | 同意作独立时间盒 |
| 移出项 | T4、T3-lite、RC1 255 条核销、typed relation（保留最小数据合同）| 同意 |
| Supersede | 等 1–5 定后再写 v2 检查点，不现在落盘 supersede | 同意 |

### OPEN（尚待冻结）

- 精确 hypothesis、dataset、baseline、metric threshold
- 哪些 PN/alignment 内容进核心圈
- failure downgrade 的具体触发条件
- A-min 是否实际做（还是只写贡献账本）
- 公开仓库名与公开时点
- 新资料下载范围
- EdgeIM PDF 原件是否缺失 [需验证]

---

## 3. 总体结构：T2 主线 + 可裁 A-min

### 3.1 T2 主线（保护对象）

```
读懂核心论文 → 结构化 paper note（CEIACF）
→ PN/DFG/IM/alignment 基础训练（手算 + 验收）
→ coverage sampling 有边界 clean-room 重实现
→ 合成真值 + 匹配保留规模的采样对照实验
→ 统一下游 PM4Py IM/IMf
→ 结构/模型/稳健性指标 + 预测→结果→verdict→claim ceiling
→ 24–72h 冷启动与未见扰动
→ 独立研究仓库 + 一页交付 + 边界表
```

### 3.2 A-min（辅助对象，可裁）

EvoAgent 只做一个独立、可解释、8–12h 封顶的工程微切片。若 T2 延误，A-min 立即降级为模块级贡献账本。降级顺序：

```
第二真实日志
→ 可选新基线实现（sigRank 等）
→ A-min 深度
→ A-min 本身
→ （T2 核心不缩减）
```

---

## 4. 研究对象：R1 EdgeIM 采样机制审计（推荐）

### 4.1 设计

```
已知过程模型生成的合成日志
→ 多种采样策略（不采样 / 匹配规模随机 / coverage sampling / 频次感知）
→ 相同 PM4Py IM/IMf 下游
→ DFG、PN、alignment 和质量评估
```

研究变量只有"采样策略"。下游发现器固定为同一 PM4Py IM/IMf，消除 Stage 3 未公开 fall-through 的混杂效应。

### 4.2 研究问题候选

> 在固定保留 trace 数量下，特征覆盖型采样是否比随机或频次感知采样更倾向保留制造新结构的记录错误，从而放大噪声并降低结构精度？

### 4.3 Claim Ceiling

可以说：在指定合成日志、扰动类型、seed 和匹配保留规模下，coverage sampling 表现出较高的噪声保留率。

不能说：coverage sampling 普遍不鲁棒；EdgeIM 存在根本缺陷；结论已适用于真实 multi-agent 系统。

### 4.4 为什么不选 R2 / R3

- **R2（全链复做）**：Stage 3 fall-through 缺失使采样效应与发现器效应混同，高风险白费 2–3 周
- **R3（agent trace conformance）**：解释成本高、鲁组论文承接弱、与 AI 辅助 EvoAgent 耦合

---

## 5. 论文阅读

论文阅读是 T2 输入，不是独立打卡。

### 5.1 必读

1. **EdgeIM 原文**（不是拆解）：三阶段、coverage sampling、(S,E,R)、中心聚合、未公开细节
2. **采样邻居**：至少核对 sigRank（TSC 2026）及其前后续 [DOI 需验证]
3. **Ground truth 方法**：行为偏差 vs 记录错误、评测需要真值（Sommers et al. [DOI 需验证]）

### 5.2 每篇 paper note 固定字段

```
核心 claim
方法 / 机制
我在看结果前的理解或预测
论文没有充分公开的细节
原文 vs 我的推断
对当前 research question / implementation / experiment 的影响
最值得质疑或验证的一点
```

---

## 6. 基础能力层（T2-Foundation）

以能解释、手推、改条件为通过标准，不以"看过 API"为标准。

### 6.1 最小知识链

```
event / case / lifecycle / timestamp
→ DFG
→ Petri-net place / transition / marking / firing
→ Inductive Miner / IMf 基本切分
→ token replay / alignment
→ model move / log move
→ fitness / precision / F-score
```

### 6.2 验收例

- 空白纸解释 place、transition、marking、firing rule
- 手算 5–6 活动日志的 DFG
- 从小 DFG 画出简单 IM 结构
- 对 1–2 条 trace 手算 token replay 或简化 alignment
- 解释为什么 fitness 高不代表 precision 高
- 修改一个初始 marking 或一条事件，预测结果变化

结果进 Hard Evidence Ledger 或 Mistake Log。

---

## 7. 实验设计（待 R1 批准后冻结）

### 7.1 最小闭环

```
question
→ hypothesis / pre-prediction（实验前必写）
→ input
→ method
→ baseline
→ metric
→ result
→ alternative explanation
→ falsifier check
→ verdict
→ claim ceiling
```

### 7.2 数据与真值

- **主实验**：已知过程模型生成的合成日志
- 扰动至少区分：插入 / 删除 / 相邻交换 / 时间戳粗化 / 标签替换 / 真实行为偏差
- 每个日志保留生成模型、扰动类型、比例、seed、case/event identity
- **Sepsis 只作外部压力检查**，不作 ground truth（其时间戳已随机化）

### 7.3 对照公平性

所有采样器使用相同的：retained trace/event 预算、下游 PM4Py IM/IMf、评测日志和指标实现、seed 集合与 trace ordering、参数调节预算。

EdgeIM coverage 输出规模内生 vs 其他方法固定比例 → 必须先定义匹配规模规则。

### 7.4 指标层次

| 层 | 指标 | 解释 |
|---|---|---|
| 采样层 | retained ratio、clean-retention、noise-retention、noise_amplification | 采样保留了什么 |
| 结构层 | DFG edge P/R/F1、伪边比例 | 结构是否被损坏 |
| 模型层 | fitness、precision、F-score、soundness、simplicity | PN 是否宽松或失真 |
| 稳定性层 | 多 seed 均值/区间、ordering sensitivity | 是否偶然 |

核心派生量：`noise_amplification = 采样后噪声占比 / 采样前噪声占比`（须配合 clean behavior coverage 报告）

### 7.5 预注册裁定

- **SUPPORTED**：多 seed + ≥2 类扰动下放大率稳定超阈值 + 结构精度下降
- **REJECTED**：无稳定放大，或 coverage sampling 明显优于对照
- **INCONCLUSIVE**：效应依赖顺序/规模/发现器

负结果和不确定结果都是合格研究输出。不能事后改 rubric。

---

## 8. 每个节点的四件套（来自 OS）

每个步骤（读论文、手算、写代码、跑实验）都产出：

1. **Pre-note**：要做什么、预测会发生什么、为什么
2. **Post-note**：实际发生了什么、与预测差异、CEIACF 六问
3. **Mistake entry**（如果预测错了）：错在哪层、可迁移 failure mode
4. **Boundary update**：做完后在三层（能独立 / 理解但不能独立 / 知道存在）里的位置

---

## 9. 所有权与冷启动

### 9.1 当天

不看答案解释 representation 和假设；说出 prediction；修改条件或做变体；解释结果。

### 9.2 D+2 / 24–72h

离开原对话和 AI summary，只用 repo 与最小笔记：找到关键实现 → 说出 representation → 预测改动影响 → 修改条件 → 运行并诊断。

### 9.3 D+7

复述整条研究链；指出一个替代设计、一个最大不确定性和当前 claim ceiling。

### 9.4 边界表（老师见面用）

| 层 | 含义 |
|---|---|
| 能独立解释 / 实现 | 硬核心，通过 hard evidence + 冷启动 |
| 理解但不能独立实现 | 邻接知识 |
| 知道存在但未系统学习 | 外围，诚实标出 |

---

## 10. 交付包

### 10.1 T2 研究仓库

独立于 MAS 和 EvoAgent，初期私有，ownership 检查后转公开。

```
paper_notes/        ← 结构化论文笔记
foundation/         ← 手算、基础验收证据
experiments/        ← 实验代码与结果
evidence/           ← Ledger、Mistake Log、claim matrix、边界表
README.md           ← 运行入口、数据边界、结论、失败边界
```

数据不入仓，放下载脚本 + MD5。

### 10.2 对外材料

- 一页技术简报（鲁组 / PM / PN / IM / alignment 语言）
- README（运行入口、实验结论、失败边界）
- 诚实贡献账本（文献 / AI / 现有代码 / 本人决策 / 本人独立实现 分开）
- 边界表
- 冷邮件草稿（不包装成成熟研究者）

---

## 11. 时间盒

默认 6h/日。检查点暂按 09-20 冻结 / 09-25 包检（待用户确认）。

| 段 | 天 | 主要工作 | 离线可做 | 降级点 |
|---|---:|---|---|---|
| 0 决策与资料 | 1–2 | R1 批准、核心论文/邻居核对、冻结范围 | — | 新源不全先用已有 |
| 1 基础 + paper notes | 3–4 | PN/DFG/IM/alignment 手算、结构化论文笔记 | 读、手算、写预测 | 减邻接阅读不减核心 |
| 2 采样器实现 | 3–4 | coverage sampling + 随机/频次基线 + 统一下游 | 写伪码与预测 | 先两种对照不追 sigRank |
| 3 合成实验 | 4–5 | 扰动生成、多 seed、指标、预注册裁定 | 设计噪声模型、预期曲线 | 减扰动类型不减主实验 |
| 4 外部压力 | 1–2 | Sepsis，仅作检查 | — | 可完全删除 |
| 5 所有权 | 3–4 | D+2/D+7 冷启动、未见扰动 | 复习自笔记 | 先砍 A-min |
| 6 收口 | 2–3 | README、简报、claim matrix、边界表、邮件 | 手写草稿 | 删装饰不删证据 |

合计约 17–24 天。缓冲在段 4（可删）和 A-min（可砍）。

---

## 12. 失败分支

| 场景 | 动作 |
|---|---|
| Stage 3 细节无法确定 | 停止追对表数值，改报有边界机制审计 + 差异清单 |
| 采样/发现/评测无法分离 | 不输出方向性结论，转 INCONCLUSIVE + 设计失败证据 |
| 冷启动只能依赖 AI/toy | 不公开包装，回到 foundation + 更小自有切片 |
| 时间不足 | 按降级顺序砍（§3.2），T2 核心不缩减 |

---

## 13. 诚实约束

- AI 先验已知（07_EDGEIM.md §6 假设 + toy 三注记）→ D5 账本显式披露
- 用户贡献 = 独立推导 / 实现 / 预注册 / 解释 / 失败诊断，不是"独立发现假设"
- 旧 toy 只作最终对照的参考答案，不算用户能力证据
- EdgeIM 官方代码：SOL 有界查找未发现 [需验证]；本窗网搜 400/429 未复核
- sigRank/CrossEdgeIM/Sommers DOI [需验证]

---

## 14. 待用户审阅并批准

| # | 项 | 默认建议 |
|---|---|---|
| 1 | R1 作为 T2 核心研究对象？ | 是（FABLE + SOL 均推荐） |
| 2 | 09-20 冻结 / 09-25 包检？ | 是 |
| 3 | A-min：8–12h 可裁微切片 or 只写贡献账本？ | 可裁微切片（T2 不受影响前提） |
| 4 | 新资料授权下载？ | 待定范围 |
| 5 | 公开仓库名？ | 用户给 |
| 6 | 从本周期移出 T4/T3-lite/255 条核销（保留最小数据合同）？ | 是 |

在上述获得明确答案前，本文件保持 `PROPOSED / FOR-REVIEW`。

---

## 15. 反向引用

- 学习 OS：`learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md`
- FABLE 提案原版：`progress/decisions/2026-09-02__research__bridge-requirements-realignment-and-edgeim-slice-proposal.md`（§12 含 SOL 输入登记 + FABLE 回应）
- FABLE 暂停交接：`progress/handoff/2026-09-02__bridge-requirements-realignment-pause__handoff.md`
- SOL 完整计划：`progress/decisions/2026-09-03__research__bridge-lu-complete-plan-proposal.md`
- SOL 三份交接档：见 `progress/handoff/INDEX.md` 09-02 三条 SOL 路由
- EdgeIM 事实边界：`research/papers_lu/teardown-joint-20260813/07_EDGEIM.md` + `.../repro/edgeim/README.md`
- 规划日志：`BRIDGE_LU_PLANNING_LOG.md` C-037 / C-038 / C-039
- 用户八条原话：FABLE 提案 §4.2

明确禁止：未获批准前不得修改任一窗既有档、下载/安装/运行、建仓、写代码、跑实验、发送邮件、stage/commit/push。
