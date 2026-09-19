# Bridge → 鲁组：九月底完整计划提案

**Date**: 2026-09-03 Asia/Taipei  
**Task**: `TASK-20260830-004`  
**Type**: integrated research / learning / delivery plan proposal  
**Status**: `PROPOSED / FOR-REVIEW / NOT-FROZEN / NO-EXECUTION-AUTHORITY`  
**Window / author marker**: `SOL`  
**Related frozen method**: `learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md`

> 本文件是供用户审阅的完整计划草案，不是执行授权。除用户明确批准对应门外，
> 不开始下载、安装、实现、实验、建公开仓、发送邮件或提交代码。

## 0. 计划一句话

九月底前，用一条窄而真实的 T2 研究闭环，证明用户已经具备继续培养的基础：读懂一篇
目标方向核心论文，独立掌握一块 PN/DFG/IM/alignment 基础，亲自实现一个可解释的
核心组件，在带真值的受控数据上完成一个有预测、有对照、有反证和有 claim ceiling 的
小实验，经过 24–72 小时冷启动后仍能接管并向鲁老师清楚说明。

## 1. 目标与非目标

### 1.1 唯一阶段目标

不是保证进组，也不是在一个月内学完过程挖掘、Petri net 或形式化验证，而是让鲁老师
愿意给出下一单位注意力：继续交流、看材料、给小任务、允许试做或后续跟进。

### 1.2 最低闭环

```text
基础真的学过一块
→ 有一块关键逻辑自己实现
→ 有一个小而完整的实验
→ 关掉 AI 后能讲清楚、改条件、解释结果和边界
```

### 1.3 非目标

- 不完整复现 EdgeIM；
- 不做 EdgeIM 新方法论文；
- 不在本周期实现 T4、T3-lite 或 T2→T4 typed relation；
- 不把 255 条材料全部分类/L1/T0/T1 作为前置条件；
- 不重做整个 EvoAgent；
- 不把 ProbGuard、VeriGuard、ProMAS 等 agent-runtime 系统当作本实验基线；
- 不用 AI 生成量、运行次数或报告页数替代用户能力。

## 2. 已锁定约束与仍未锁定事项

### 2.1 已锁定或用户明确选择

| 项 | 当前口径 |
|---|---|
| 阶段主目标 | 九月底前达到可以不虚地联系鲁老师的状态 |
| 资源优先级 | T2 研究工件受保护；A-min 不得挤压 T2，可缩减或降级 |
| 研究主轴 | T2：事件日志、DFG/PN、IM、alignment/conformance 基础 |
| 论断边界 | 不称“完整复现 EdgeIM”；不超过证据支持范围 |
| 学习协议 | 裸机先手 → AI 辅助 → 关答案重做 → 冷启动复测 |
| 每日反馈 | 至少一次可能判错的 hard training/verification |
| OS 状态 | `Learning–Research OS v0.1 — FROZEN 2026-09-03` |

### 2.2 仍需用户批准

- T2 研究对象是否正式选 `R1：EdgeIM sampling-mechanism audit`；
- 是否正式从本周期移出 T4/T3-lite/255 条核销，并保留最小数据合同；
- 检查点采用 `09-20 内部冻结 + 09-25 对外包`，还是其他日期；
- 是否实际做 A-min（默认可降级为只写 EvoAgent 贡献账本）；
- 公开仓库名与公开时点；
- 新增资料的下载范围和 SOL 隔离目录。

## 3. 总体结构：T2 主线 + 可裁 A-min

### 3.1 T2 主线（保护对象）

```text
目标方向核心论文
→ 结构化 paper note
→ PN/DFG/IM/alignment 基础训练
→ EdgeIM coverage sampling 有边界重实现
→ 合成真值 + 匹配保留规模的采样对照
→ 统一下游 PM4Py IM/IMf
→ 结构/模型/稳健性指标
→ alternative / falsifier / verdict / claim ceiling
→ 24–72h 冷启动与未见扰动
→ 独立研究仓库和一页交付
```

### 3.2 A-min（辅助对象）

EvoAgent 只做一个独立、可解释、8–12 小时封顶的工程微切片；不重构全仓，不让 T2
依赖它。若 T2 基础、主实验或 ownership 验收发生延误，A-min 立即降级为模块级贡献
账本，不进入外发包主叙事。

## 4. 研究对象候选与推荐

### R1（推荐）：EdgeIM 采样机制审计

```text
已知过程模型生成的日志
→ 不采样 / 匹配规模随机 / coverage sampling / 频次感知基线
→ 相同 PM4Py IM/IMf
→ DFG、PN、alignment 和质量评估
```

研究问题候选：

> 在固定保留 trace 数量下，coverage-based sampling 是否比随机或频次感知采样更倾向
> 保留制造新结构的记录错误，从而提高噪声放大率并损害结构精度？

优点：变量隔离最好，最少依赖 EdgeIM 未公开的 Stage 3 fall-through，最容易形成可信
的 question → prediction → evidence → verdict 链。

限制：它是 EdgeIM-inspired component audit / replication-plus learning study，不能称
完整 EdgeIM 复现。

### R2：EdgeIM 有界全链重演

重演采样、局部 `(S,E,R)`、聚合和发现，再做窄实验。表面最贴近论文，但会把采样效果
和未公开的发现器细节混在一起，风险较高。

### R3：EvoAgent trace conformance

直接对 EvoAgent trace 建参考 PN 并做 alignment。长期方向最接近，但 ground truth、解释
成本和 AI-assisted 资产耦合风险更高，不作为默认路线。

## 5. 论文阅读计划

论文阅读是 T2 主线的输入，不是独立打卡。

### 5.1 必读层

1. **EdgeIM**：理解三阶段、coverage sampling、`(S,E,R)`、中心聚合及其未公开细节；
2. **sampling 邻居**：至少核对 sigRank 及其前后续关系，避免重复提出已有问题；
3. **ground-truth / PN-alignment 方法**：理解行为偏差、记录错误、模型质量和 conformance
   评测为何需要真值。

EdgeIM 官方记录将其描述为特征保持采样、边缘局部处理和中心聚合的 process-model
discovery 方法，而不是完整 alignment/deviation 系统。

### 5.2 每篇 paper note 的固定字段

```text
核心 claim
方法 / 机制
我在看结果前的理解或预测
论文没有充分公开的细节
原文 vs 我的推断
对当前 research question / implementation / experiment 的影响
最值得质疑或验证的一点
```

至少一篇与鲁组或 frozen slice 直接相关的论文必须形成这种结构化理解产物。

## 6. 基础能力层（T2-Foundation）

基础层不以“看过 API”为通过标准，而以能解释、手推、改条件为标准。

### 6.1 最小知识链

```text
event / case / lifecycle / timestamp
→ DFG
→ Petri-net place / transition / marking / firing
→ Inductive Miner / IMf 基本切分
→ token replay / alignment
→ model move / log move
→ fitness / precision / F-score
```

### 6.2 基础验收例

- 空白纸解释 place、transition、marking、firing rule；
- 手算一个 5–6 活动日志的 DFG；
- 从小 DFG 画出一个简单 IM 结构；
- 对 1–2 条 trace 手算 token replay 或简化 alignment；
- 解释为什么 fitness 高不代表 precision 高；
- 修改一个初始 marking 或一条事件，预测结果变化。

这些验收结果进入 Hard Evidence Ledger 或 Mistake Log，不直接以“完成学习”表述。

## 7. R1 实验设计（待 R1 批准后冻结）

### 7.1 最小闭环

```text
question
→ hypothesis / pre-prediction
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

- 主实验：已知过程模型生成的合成 event logs；
- 记录错误与行为偏差分开生成和标注；
- 至少区分 insertion、deletion、adjacent swap、timestamp coarsening 和真实行为偏差；
- 每个日志保留生成模型、扰动类型、比例、seed 和 case/event identity；
- Sepsis 只作外部 stress check，不作干净 ground truth。

### 7.3 对照公平性

所有采样器使用相同：

- retained trace 或 retained event 预算；
- 下游 PM4Py IM/IMf；
- 评测日志和指标实现；
- seed 集合与 trace ordering policy；
- 参数调节预算。

EdgeIM coverage 输出规模是内生的，而其他方法可能使用固定比例，因此必须先定义匹配
规模规则，否则比较不成立。

### 7.4 指标层次

| 层 | 指标 | 解释 |
|---|---|---|
| sampling | retained ratio、clean-retention、noise-retention、noise amplification | 采样保留了什么 |
| structure | DFG edge precision/recall/F1、伪边比例、真边覆盖率 | 结构信息是否被损坏 |
| model | fitness、precision、F-score、soundness、simplicity | 发现出的 PN 是否宽松或失真 |
| conformance | alignment cost、log/model move 比例、偏差定位召回 | 偏差解释是否受影响 |
| stability | 多 seed 均值、区间、ordering sensitivity | 是否只是一次排序偶然性 |
| efficiency | sampling time、end-to-end time、communication proxy | 是否存在效率收益 |

核心派生量：

```text
noise_amplification
= sampled-log noise proportion / original-log noise proportion
```

它必须和 clean behavior coverage 一起报告，不能单独用来宣称鲁棒性。

### 7.5 三种预注册裁定

- `SUPPORTED`：多 seed、至少两类扰动下，放大率稳定超过预设阈值且结构精度下降；
- `REJECTED`：没有稳定放大，或 coverage sampling 明显优于对照；
- `INCONCLUSIVE`：效应依赖顺序、规模、发现器或某个未控制因素。

负结果和不确定结果都是合格研究输出，不能事后改 rubric。

## 8. Claim–Evidence 结算

每个重要实验节点必须回答：

1. **Claim**：最强的 claim 是什么？
2. **Evidence**：哪个证据直接支持它？
3. **Identification**：设计真正识别了声称的对象吗？
4. **Alternative**：什么其他机制也能产生同样结果？
5. **Falsifier**：什么结果会迫使我改口？
6. **Ceiling**：当前证据最远允许说到哪里？

默认 claim ceiling 示例：

```text
可以说：在指定合成日志、扰动类型、seed 和匹配保留规模下，coverage sampling
表现出较高的噪声保留率。

不能说：coverage sampling 普遍不鲁棒；EdgeIM 存在根本缺陷；结论已适用于真实
multi-agent 系统。
```

## 9. 每日运行协议

每日使用冻结的 Learning–Research OS v0.1：

### 9.1 每天的最小节奏

```text
上午/第一自由 block：Active Check List 写清目标与 PASS 条件
白天：一项裸机先手、手算、论文预测或小实现
等待机器/上课：后台仅运行已冻结的核验任务
晚间 23:00：先讲/先做 → 追问 → 变体/反例 → 结算
```

### 9.2 三本账

- `Hard Evidence Ledger`：只收已经 PASS 的能力；
- `Mistake Log`：只收可迁移的认知模型错误或 recurring failure mode；
- `NO-HARD-OUTPUT`：当天三者都没有时只记一行，次日首个自由 hard block 优先做 hard
  training，不是惩罚，也不阻断固定课程和 deadline。

### 9.3 后台并行

后台同时最多 1–2 条主要验证线，可做文件核验、数据/基线查找、冻结实验、环境 smoke
test 和批量运行。后台输出只算研究输入或风险地图，不算用户能力增长。

## 10. 所有权与冷启动验收

### 10.1 当天验收

- 不看答案解释 representation 和假设；
- 说出 prediction；
- 修改一个条件或做一个变体；
- 解释结果与预期是否一致。

### 10.2 D+2 / 24–72 小时

离开原对话和 AI summary，只用 repo 与最小个人笔记：

- 找到关键实现；
- 说出 representation；
- 预测改动影响；
- 修改一个条件；
- 运行并诊断结果。

### 10.3 D+7

能复述整条研究链，指出一个替代设计、一个最大不确定性和当前 claim ceiling。

### 10.4 老师见面边界表

| 层级 | 内容 |
|---|---|
| 能独立解释/实现 | 已通过 hard evidence 与冷启动 |
| 理解但不能独立实现 | 能解释机制和限制，但尚未独立完成实现 |
| 知道存在但未系统学习 | 只作背景地图 |
| 未验证 | 官方实现、未公开 fall-through 或未运行的新基线 |

## 11. 交付包

### 11.1 T2 研究仓库

建议公开仓独立于 MAS 主仓和 EvoAgent，初期私有开发，满足 ownership 与许可检查后再公开。

```text
paper_notes/
foundation/
experiments/
artifacts/
evidence/
  hard_evidence_ledger.md
  mistake_log.md
  claim_evidence_matrix.md
  boundary_table.md
README.md
```

数据本体不直接入仓；保留合法下载入口、版本、元数据、校验/身份信息和转换脚本。

### 11.2 对外材料

- 一页技术简报：只写鲁组/PM/PN/IM/alignment 语言；
- 研究仓 README：运行入口、数据边界、实验结论和失败边界；
- 诚实贡献账本：文献、AI、现有代码、本人决策和本人独立实现分开；
- 老师见面边界表；
- 冷邮件：不包装成成熟研究者，不称完整复现或新方法。

## 12. 时间盒（提案）

默认按 6 小时/日；8 小时以上只作为偶发缓冲，不作为 scheduler 基线。

| 阶段 | 建议天数 | 主要工作 | 降级点 |
|---|---:|---|---|
| 0. 决策与资料 | 1–2 | 选 R1、核对核心论文/邻居、冻结 contract 和范围 | 新源不全时先用已有原件，不阻塞讨论 |
| 1. 基础与 paper notes | 3–4 | PN/DFG/IM/alignment 手算、结构化论文笔记 | 减少邻接阅读，不减核心基础 |
| 2. 采样器实现 | 3–4 | coverage sampling、随机/频次基线、统一下游接口 | 先保留两种对照，不追 sigRank |
| 3. 合成真值实验 | 4–5 | 扰动生成、多 seed、指标和预注册裁定 | 减少扰动类型，不减主实验和预测 |
| 4. 外部压力检查 | 1–2 | Sepsis 或第二日志，仅作外部检查 | 可完全删除第二真实日志 |
| 5. 所有权验收 | 3–4 | D+2/D+7、24–72h 冷启动、未见扰动 | A-min 先删，不删 T2 ownership |
| 6. 收口 | 2–3 | README、简报、claim matrix、边界表、邮件草稿 | 删除装饰，不删证据与边界 |

检查点建议：`09-20` 内部技术冻结，`09-25` 对外包检查；两者均待用户确认。

## 13. 失败分支与停止条件

### 13.1 论文/实现依赖失败

若 EdgeIM 关键 fall-through 细节无法确定：停止追求论文表格数值，改报有边界机制审计，
并保留差异清单。

### 13.2 实验主张不可识别

若 sampling、discovery、metric 或 ordering 无法分离：不输出方向性结论，转为
`INCONCLUSIVE`，保留设计失败证据。

### 13.3 所有权失败

若冷启动只能依赖 AI 或旧 toy：不公开包装；回到 foundation 和一个更小的自有切片。

### 13.4 时间不足

按以下顺序删减：

```text
第二真实日志
→ 可选新基线（如 sigRank 的本地实现）
→ A-min 深度
→ A-min 本身
```

不得先删掉 T2 核心基础、主实验、预预测或冷启动验收。

## 14. 当前状态与待用户审阅项

### 已完成

- Learning–Research OS v0.1 已冻结；
- T2 优先于 A-min 已明确；
- Fable/SOL 双窗事实已分开存档；
- EdgeIM、sigRank、CrossEdgeIM、ground-truth 资料定位已形成边界记录；
- 本计划草案已落盘供审阅。

### 尚未完成

- R1 尚未正式批准；
- 精确 hypothesis、dataset、baseline、metric threshold 尚未冻结；
- 新资料尚未下载；
- 代码、实验、公开仓库和邮件均未开始；
- D1–D5/A1–A4 尚未通过。

### 需要用户确认的最小问题

1. 是否批准以 R1 作为 T2 核心研究对象？
2. 若批准，是否同意 `09-20 内部冻结 + 09-25 对外包`？
3. EvoAgent 是否只保留贡献账本，还是在 T2 不受影响前提下做 8–12h A-min？
4. 新资料是否授权以 SOL 独立目录增量固化？

在上述问题获得明确答案前，本文件保持 `PROPOSED / FOR-REVIEW`，不升级为冻结规格。

## 15. 反向引用与边界

- 学习 OS：`learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md`；
- SOL 当前游标：`progress/handoff/2026-09-02__bridge-t2-priority-and-research-object__sol-pause-handoff.md`；
- SOL 方案评估：`progress/handoff/2026-09-02__bridge-scheme-evaluation-framework__sol-pause-handoff.md`；
- Fable 提案：`progress/decisions/2026-09-02__research__bridge-requirements-realignment-and-edgeim-slice-proposal.md`；
- EdgeIM 事实边界：`research/papers_lu/teardown-joint-20260813/07_EDGEIM.md` 与
  `research/papers_lu/teardown-joint-20260813/repro/edgeim/README.md`；
- 材料取得边界：`research/tracebridge_full_spectrum_20260830/08_materials/DOWNLOAD_RECEIPT.md`。

明确禁止：未获批准前不得修改 Fable/SOL 既有档、下载/安装/运行、建仓、写代码、跑实验、
发送邮件、stage、commit、push、reset、clean 或 merge。
