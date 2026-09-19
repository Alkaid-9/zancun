# 鲁组学习—谱系—迁移研究计划差分

**Date**: 2026-09-05 Asia/Taipei
**Task**: `TASK-20260905-001`
**Status**: `APPROVED / ACTIVE-WITH-GATES`
**Authority**: 用户在“外围重排、地基不动”的方案 3 后明确回复“可以”
**Scope**: EdgeIM 学习顺序、鲁法明谱系核验、sampling 横向比较、迁移审计和最小研究出口
**Non-scope**: 不修改冻结 Learning-Research OS；不修改现有题面/PASS 条件；不启动实验；不建立新的 Agent logging/runtime infrastructure；不作 novelty claim

## 0. 决策

采用双层调整：

1. **地基不动**：保留 `lu-edgeim-algo1` 已冻结站序和 ownership-first 门禁；
2. **外围重排**：把鲁法明研究谱系、sampling genealogy、Transfer Audit 和 semantic scan 接到明确解锁点；
3. **不追五个新 gap**：新发现先作为 `PARK` 候选，不得跳过 Algorithm 1/DFG 所有权训练；
4. **计划日期纠偏**：当前进组预期是 2026 年 9 月底，精确日期待定；旧 `09-10` 不再作为压缩学习或开工的依据；OE1 旧 `08-25` 已滑线，期待定。

## 1. 为什么需要调整

新形成的研究谱系表明，EdgeIM 不是孤立算法，而可放入更长的 research grammar：

```text
真实问题
-> representation
-> structural assumption
-> method
-> property / evidence
-> failure boundary
```

同时，`Execution -> Structure -> Intervention` 提供了跨流程挖掘、并发程序、RCA、工业 AI 和 Agent assurance 的候选 Research Operator。

但当前用户能力证据仍停在更早位置：`EX-00` 未 PASS，Algorithm 1 的对象、状态、保留判据、终止和输出尚未形成新的冷启动证据。若现在转向大范围谱系或 Agent frontier，会再次出现“地图由 AI 建完、核心对象没有长在本人身上”的失配。

因此，新材料改变“为什么学、学完通向哪里”，暂不改变“先学什么”。

## 2. 保留不变的地基

现有顺序继续有效：

```text
0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7
```

以下内容不因本差分改变：

- 每站原 PASS 条件；
- `EX-00` 是 `EX-01` 进门票；
- 第 1 站后才能裁 T0；
- 第 5a 站必须由用户先纸上写再敲实现；
- 第 7 站才进入最小实验；
- AI 生成的谱系、地图、卡片和检索结果不进入用户能力 Ledger；
- D+2/D+7 冷启动失败时，能力状态仍须 `RE-OPEN`。

## 3. 新的 P0-P5 层次

### P0｜EdgeIM 地基

**包含**：EX-00 -> EX-01 -> EX-05a。

**目标**：用户独立掌握 Algorithm 1、DFG、论文对象和自己的最小实现。

**当前唯一游标**：完成 EX-00 v2 §6 脱稿并通过原 PASS 条件。

**硬门**：P0 未完成时：

- 不开始鲁法明四轨道系统核验；
- 不填写研究级 Transfer Card verdict；
- 不启动 Agent/process-mining 新实验；
- 不把谱系叙事包装成用户自己的研究判断。

### P1｜鲁法明谱系证据校准

**解锁**：EX-05a PASS 后；EX-01 PASS 提供论文阅读与来源标注基础。

**输入**：

- `research_growth/反思与思考/2026-09-05_鲁法明研究谱系与稳定Research-Grammar.md`；
- `learning/training/ra2716-survey/` 旧训练包；
- 现有 lu teardown、family synthesis、bridge cards、论文原文和官网。

**动作**：不是重新盲写一遍，而是做反证式 citation audit：

1. 分开鲁法明本人署名与公开合作网络；
2. 四条轨道各抽至少一项代表工作；
3. 对每条稳定 research grammar 找支持证据和至少一个不支持/替代解释；
4. 把“公开事实”“用户综合解释”“plausible next step”分栏；
5. 抽查官网身份、博士谱系、作者表、年份和关键数字。

**产出**：一张带来源坐标的 lineage map + 一份 conflict/unknown 表。

**PASS**：抽查项均有可复核来源；本人/网络零混称；至少记录两个会削弱当前叙事的反例或竞争解释。

### P2｜EdgeIM 深入

**包含**：EX-02 -> EX-03 -> EX-05。

**目标**：从 Algorithm 1 进入 IM、representation、结构保存与证据边界。

**新增关注问题**：

- `support`、`frequency` 和边权分别在哪一步产生或丢失；
- DFR/DFG representation 对 downstream miner 哪些性质充分、哪些不充分；
- feature preservation 与 model fidelity 之间是否存在未经证明的跳跃；
- adjacency、data dependency 与 causality 不得混称。

这些是跨站观察轴，不增加新站、不修改原题面和 PASS 条件。

### P3｜Sampling 横向比较

**解锁**：EX-05 PASS 后。

**比较对象**：

```text
2024 DFR-equivalence sampling
-> EdgeIM 2025
-> sigRank 2026
```

**固定比较维度**：

| 维度 | 必答问题 |
|---|---|
| Objective | 压缩、结构保证、排名还是 downstream discovery？ |
| Selection interface | 一遍过滤、ratio/budget 还是 ranking？ |
| Preserved quantity | support、frequency、significance 或其他？ |
| Representation | DFR set、weighted DFG、trace score 或 process model？ |
| Downstream consumer | 哪个 miner/metric 消费样本？ |
| Guarantee | 保证对象是什么，前提是什么？ |
| Failure boundary | rare behavior、noise、order sensitivity、distribution shift 如何影响？ |

**产出**：三工作对照表 + 一个未被文献自动回答的 downstream-fidelity 问题。

**边界**：EdgeIM 不因 sigRank 存在而被改写成 fixed-K/ratio sampler。

### P4｜迁移审计

**解锁**：EX-06 PASS 后，且 P1 谱系核验通过。

**首张候选卡**：

```text
source: event/program execution traces
operator: recover downstream-relevant latent structure
target: LLM multi-agent interaction traces
```

必须使用 `research_growth/方法论/TRANSFER_CARD_TEMPLATE.md`，回答：

- source mechanism 的原文证据；
- Agent target 中结构是否存在、可观察、可识别；
- DFR/adjacency、artifact data dependency、causal visibility 哪个 representation 才充分；
- 显式结构改变 monitor/verify/compile/repair 中哪个决策；
- `H_transfer` 与至少一个 `H_alt`；
- 最小反例和 translation cost。

**PASS**：只能得到 `DROP/PARK/PROMOTE` 之一；没有可证伪 prediction 时不得 PROMOTE。

### P5｜最小研究

**解锁**：EX-07 PASS，且 P4 verdict=`PROMOTE`。

**范围**：一次只验证一个 representation 或一个 prediction。

**优先测试**：构造 adjacency 相同但 causal/data dependency 不同的两个 toy workflows，检查候选 representation 是否能区分。

**不做**：

- 不先建新 logging platform；
- 不先造 benchmark；
- 不同时实现 compile + verify + monitor + repair；
- 不因 toy 成功升级成一般 Agent assurance claim。

## 4. 每周/月度扫描语义调整

现有仓内可定位的是 `BR-3 · 科研地图月度快查`，未找到独立“每周扫描任务”的权威文件。因此本轮只扩展 BR-3 的检索语义，不新造自动调度。

扫描单位从窄领域词：

```text
LLM Multi-Agent x Process Mining / Formal Verification
```

扩展为：

```text
agent traces
-> structure / dependency / workflow / protocol
-> compile / verify / monitor / diagnose / repair
```

每次扫描至少包含：

- 一组领域标签查询；
- 一组 action + object + result 查询；
- 一组替代 representation 查询；
- 一组会否定当前 residual 的查询。

只发现相似论文不升级 research queue；先进入 Transfer Card 的 prior-art 栏。

## 5. 导师画像训练兼容调整

`ra2716-survey` 的旧 EX-01 文件保持历史空白，不伪造成已经完成的 90 分钟盲写。

新增当前路径：`EX-01R · 谱系证据审计`。

- 旧 EX-01 训练“从零检索成像”；
- EX-01R 训练“面对一份已经很顺的叙事，逐条核验、拆归属、找反例、降低 claim”；
- 二者训练目标不同，EX-01R 不补记为旧 EX-01 PASS；
- 对外素材仍只能使用 `[VERIFIED] + 坐标 + 时效` 条目。

## 6. 进组表达门

在鲁老师面前可以使用的主线结构是：

```text
真实问题
-> representation
-> structural assumption
-> method
-> property / evidence
-> failure boundary
```

但对外表达必须满足：

1. 所举论文事实已在 P1 核验；
2. 所讲 EdgeIM 内容已由对应 EX PASS；
3. inferred next step 明确说成个人问题或观察，不说成老师计划；
4. 不用 AI 生成的整条 research grammar 冒充个人成熟判断；
5. 能在追问下给出具体 representation、反例和证据边界。

## 7. 日期与优先级纠偏

- 当前记录表明，`09-10` 已在 2026-09-03 被用户改为“9 月底”；精确日期仍未知。
- 本差分不擅自把“月底”解释为确定的 `09-30` 硬日，只移除旧 `09-10` 的强制性。
- OE1 原 `08-25` 已滑线，期待定；不得以过期日期制造虚假紧急度。
- 在精确日期确认前，优先级只由依赖决定：`EX-00 -> EX-01 -> EX-05a` 是当前关键路径。

## 8. 状态与停止条件

| 层 | 当前状态 | 解锁条件 | 停止条件 |
|---|---|---|---|
| P0 | ACTIVE | 当前即可做 | 任一站未 PASS，停在本站 |
| P1 | BLOCKED | EX-05a PASS | 来源不足或本人/网络无法分清 |
| P2 | BLOCKED | P0 PASS | 按原站点门 |
| P3 | BLOCKED | EX-05 PASS | 三篇身份/全文不足则标 UNKNOWN |
| P4 | BLOCKED | EX-06 + P1 PASS | 无 decision delta 或可证伪 prediction |
| P5 | BLOCKED | EX-07 + P4 PROMOTE | 需要扩 infrastructure 或 claim 超出 toy |

## 9. 本次计划变更的验收

- [x] 明确哪些不改：OS、站序、题面、PASS、实验代码；
- [x] P0-P5 各有依赖、产出、PASS/停止条件；
- [x] 当前唯一游标回到 EX-00；
- [x] 本人署名与合作网络核验进入 P1；
- [x] sampling 三工作比较进入 P3；
- [x] Transfer Card 与最小实验分别进入 P4/P5；
- [x] 周/月扫描只扩语义，不虚构自动任务；
- [x] 旧 09-10/08-25 不再作为当前硬压缩依据；
- [x] 未启动任何实验或新 infrastructure。

## 10. 下一动作

用户回到 `learning/training/lu-edgeim-algo1/EX-00/README.md`，完成 v2 §6 脱稿提交。除此之外的 P1-P5 维持阻断。

## Amendment

### A1 · 2026-09-05｜P3 单一后置比较改为“一主干三镜头”穿插调度

**Authority**：用户明确纠正“不是四篇里只学 EdgeIM，另外三篇放着”，并定义“一篇主干 + 一篇横向对照 + 一篇实验方法论 + 一篇纵向后继”。

**Task**：`TASK-20260905-002`

**Supersedes**：本档 §3 `P3｜Sampling 横向比较` 的“EX-05 后才接触相邻论文”读法。P3 的完整 sigRank comparison 仍保留，但三篇镜头按不同节点提前/穿插出现。

**新调度正本**：`learning/training/lu-edgeim-algo1/FOUR_PAPER_TRAINING_LOOP.md`。

| 论文 | 角色 | 第一次解锁 | 完整用途 |
|---|---|---|---|
| EdgeIM | 主干 learning object | 当前 | 独立重建、反例、实现、claim audit |
| sigRank | 横向 sparring | EX-01 PASS 后短开 | EX-05 后完整 fair comparison |
| Ground Truth Approach | 实验/证据方法论 | EX-06 PASS 后 | EX-07 前产 world contract |
| CrossEdgeIM | 纵向 genealogy | EX-06 PASS + 理解 IM/PN downstream | predecessor → residual → redesign → new residual |

**保持不变**：原站序、题面、PASS、答案密封、当前 EX-00 游标、P4/P5 的 Transfer Audit 与实验阻断。

**新增硬门**：EX-07 不得只拿真实日志上的漂亮 F-measure 作为 sampling fidelity 证据；必须先用 Ground Truth 镜头写清 GT model、behavioral deviation、recording error、sampling intervention 和区分指标。
