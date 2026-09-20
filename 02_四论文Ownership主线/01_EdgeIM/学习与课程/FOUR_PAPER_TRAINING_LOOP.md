# 四论文十字训练闭环

**Date**: 2026-09-05
**Task**: `TASK-20260905-002`
**Status**: `ACTIVE-ROLES / V3-CONTENT-GATED`（深度与当前游标由 09-13 v3 合同订正）
**Parent**: `BRIEF.md` + `progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md`
**不改变**: EdgeIM 站序、题面、PASS 条件、答案密封与 ownership 规则

**层级定位（2026-09-06）**：本档负责 `RESEARCH MAPS -> ACTIVE TRACKS` 的四论文调度。它服务 EdgeIM 学习主干和研究邻域，进组材料只是下游消费面，不是四论文训练的唯一目的。会话与新增桌面材料只作输入，论文事实和作者归属仍需回到对应原始来源核验。

## 1. 定位

四篇不是“只学 EdgeIM，其余以后再说”，也不是四篇平均逐页精读。课程结构是：

> 一篇主干 + 一篇横向对照 + 一篇实验方法论 + 一篇纵向后继。

| 论文 | 课程角色 | 主要训练 | 相对深度 |
|---|---|---|---|
| EdgeIM | 主干，拆到能独立重建 | DFG、sampling、representation、distributed discovery、IM、claim 边界、算法审计 | 长期全文 5/5 |
| sigRank | 横向方法对照 / sparring partner | sampling 优化对象、预算、ranking、model-quality objective、fair comparison | 长期全文 5/5；按镜头依赖展开 |
| Sommers et al. Ground Truth Approach | 实验与证据方法论 | ground truth、behavioral deviation、recording error、claim-evidence alignment | 长期全文 5/5；按镜头依赖展开 |
| CrossEdgeIM | 纵向后继 / genealogy | predecessor、residual bottleneck、redesign、new residual | 长期全文 5/5；先浅后深 |

核心记法：

\[
\boxed{\text{EdgeIM 是学习对象，另外三篇是三个观察镜头。}}
\]

## 2. 十字结构

```text
                         CrossEdgeIM
                          【往后长】
                              ^
                              |
                           genealogy
                              |
sigRank  <------ compare --- EdgeIM
【横向方法】                  【主干】
                              |
                           evaluate
                              |
                              v
                    Ground Truth Approach
                      【证据/实验地基】
```

四个核心问题：

- EdgeIM：方法是什么，representation 为什么这样设计？
- sigRank：还有什么解决法，sampling objective 与接口差在哪里？
- Ground Truth：怎么知道比较真正击中了 claim？
- CrossEdgeIM：方法完成后，研究路线为什么继续生长？

## 3. EdgeIM 主干的 ownership 标准

EdgeIM 不是摘要理解任务。最终应能：

1. 不看论文重建 Algorithm 1；
2. 解释每个 representation 为什么存在；
3. 自己构造反例；
4. 改一个 assumption 并预测哪里失效；
5. 重实现最小版本；
6. 审查论文 claim；
7. 用相邻方法攻击其设计选择。

主链为：

```text
event log
-> sampling
-> S/E/R
-> DFG
-> distributed aggregation
-> Inductive Miner
-> Petri net
```

Algorithm 1 只按 `S/E/R` 集合覆盖决定是否保留 trace；Stage 2 从过滤后 `D'` 重新累计关系次数。这个集合 support 与后续 weight/frequency 的接口是主干问题，但必须由原文和用户手算建立，而不是从本页背答案。

## 4. 三个镜头的分时调度

### L-S1｜sigRank 第一次开镜：selection philosophy

**解锁**：EX-01 PASS 后。

**时间盒**：30-45 分钟。

**只问四题**：

1. EdgeIM 为什么保留一条 trace？
2. sigRank 为什么保留一条 trace？
3. 两者的 sample size 是 endogenous 还是 user-defined ratio？
4. coverage 与 importance 分别是什么 surrogate？

**输出**：一张不超过一页的 `coverage vs importance` 对照。

**停止点**：不逐页精读 sigRank，不读结果表全套，不提前评价 downstream model quality。

### L-S2｜sigRank 第二次开镜：sparring 与 fair comparison

**解锁**：EX-05 PASS 后。

**时间盒**：2-3 小时。

**固定比较轴**：

- `coverage vs importance`；
- `endogenous sample size vs fixed sampling ratio`；
- `structural preservation vs downstream model quality`；
- 相同预算如何对齐；
- 原日志评价发现模型意味着什么、不意味着什么；
- 同样 sampling ratio 下模型质量差异能支持什么 claim；
- EdgeIM 的 surrogate objective 是否与最终 consumer 对齐。

**输出**：EdgeIM vs sigRank sparring table + 一个 fair-comparison contract。

**PASS**：能明确指出至少一个不公平比较设计，并提出 matched interface 或 matched cost 的修正。

### L-GT｜Ground Truth Approach：实验与证据门

**解锁**：EX-06 PASS 后可读方法框架；EX-07 实验设计前必须完成。

**时间盒**：2-3 小时。

**不以背新算法为目标**。只重建以下世界生成链：

```text
initial ground-truth model
-> known behavioral deviation
-> deviating model
-> injected recording errors
-> imperfect event log
```

**必须回答**：

1. underlying process 的 ground truth 在哪里？
2. missing/extra behavior 是 sampling、behavioral deviation 还是 recording error 造成？
3. 当前实验测的是 correctness、fidelity、robustness、conformance 还是别的量？
4. fitness/precision 高为什么不自动等于“恢复正确”？
5. verifier/environment 本身如何验收？
6. 哪个 synthetic world 才能击中 EdgeIM sampling distortion 的具体 claim？

**输出**：EX-07 的 `world contract`，至少包含 GT model、deviation operator、recording-error operator、sampling intervention 和可区分指标。

**硬门**：没有 world contract，不得把 BPIC/Sepsis 上一个漂亮 F-measure 当作 sampling fidelity 证据。

### L-CX1｜CrossEdgeIM 第一次开镜：genealogy reconstruction

**解锁**：EX-06 PASS，且用户已经能解释 EdgeIM 的 IM/Petri-net downstream 链。

**时间盒**：60-90 分钟。

**重建四步**：

```text
predecessor
-> residual bottleneck
-> architecture redesign
-> new residual
```

候选架构差异：

```text
EdgeIM
case filtering
-> edge feature
-> central global DFG
-> central discovery

CrossEdgeIM
activity node incremental feature maintenance
-> delta DFR / delta S / delta E
-> organization-level DFG
-> organization-level model discovery
-> central merge of local models
```

**必须区分**：CrossEdgeIM 是公开合作谱系的后继，不是鲁法明署名论文；它的价值是理解圈子的 research evolution，不用于夸大鲁老师个人产出。

**输出**：一页 genealogy card。

**PASS**：指出 EdgeIM 解决的瓶颈、CrossEdgeIM 新增的对象/约束/架构，以及 redesign 后仍未解决的一个 residual。不能只写“更分布式”。

### L-CX2｜CrossEdgeIM 第二次开镜：interaction-semantics residual

**解锁**：首张 Transfer Card 准备阶段；不是必修前置。

**问题**：跨组织合并是否充分表达 message flow、data dependency、causal visibility、agent protocol 和 interaction property？

**边界**：这是 residual 候选，需 semantic prior-art audit；不得从“模型分层”直接跳到“LLM multi-agent novelty”。

## 5. 与原站序的穿插图

```text
EX-00  EdgeIM Algorithm 1
  |
EX-01  DFG / frequency / Stage 1
  +---- L-S1 sigRank 短开镜
  |
EX-05a 自写 Algorithm 1
  +---- P1 鲁法明谱系 citation audit 可解锁
  |
EX-02 -> EX-03 -> EX-05
  +---- L-S2 sigRank 完整 sparring
  |
EX-06  claim / evidence / genealogy prerequisites
  +---- L-CX1 CrossEdgeIM genealogy
  +---- L-GT Ground Truth 方法框架
  |
EX-07  experiment
  +---- L-GT world contract 是开工门
  |
Transfer Card
  +---- L-CX2 interaction-semantics residual（可选）
```

三镜头会在相应节点真正打开，不会被推到“以后”；同时任何镜头都不能跨过当前 EdgeIM 站点门。

## 6. 三篇镜头不采用相同读法

| 镜头 | 主要读法 | 不做什么 |
|---|---|---|
| sigRank | 设计选择对照 + fair comparison | 不从第一页逐句复刻第二套主干课 |
| Ground Truth | 重建 evaluation world + claim-evidence audit | 不背全部框架分类或把其自评当绝对标准 |
| CrossEdgeIM | genealogy reconstruction + residual analysis | 不把 DFG 重学一遍，不冒充鲁本人论文 |

## 7. 证据与 claim 边界

- 四篇拆解件是阅读辅助，不替代用户读原文和自己的作答。
- sigRank 与 CrossEdgeIM 的 F-measure 口径不可直接并表。
- sigRank 用原日志评价模型，不等于拥有 underlying-model ground truth。
- Ground Truth Approach 提供评估方法论，不自动证明我们的 synthetic world 有效。
- CrossEdgeIM 的公开合作关系不等于实验室组织关系。
- 任何新 residual 在 prior-art 和 Transfer Audit 前只标 `PARK`。

## 8. 当前游标

当前先按[证据对账路由](../../../01_进组总计划_OE1_材料交付/CURRENT_LEARNING_ROUTE.md)核 v3 六项恢复证据；历史位置记录为 EX-05，本轮不重判 PASS。十五题为最终 D2，不是当前前置。L-S1、L-S2、L-GT、L-CX1、L-CX2 的解锁条件不变，实际是否解锁须按本人证据复核，不能由会话阅读或密封答案自动升级。

## 9. 五层架构中的位置

| 层 | 本档承担的内容 |
|---|---|
| `WORLD / FIELD` | 只接受经过来源标注的外部谱系和邻接方向 |
| `RESEARCH MAPS` | 三篇镜头与 EdgeIM 设计选择的关系、前序/后继和 residual |
| `ACTIVE TRACKS` | 按 EX 节点解锁的 L-S1/L-S2/L-GT/L-CX1/L-CX2 |
| `EVIDENCE / PRACTICE` | 用户亲手完成的对照、world contract、genealogy card 和 prediction→check→verdict |
| `ARTIFACTS` | 通过 claim ceiling 后才可复用的比较卡、实验回执和对外材料片段 |

所有层回链原论文、原始数据、代码和可核验输出；没有来源坐标的跨领域断言保持 `UNKNOWN / PARKED`。
