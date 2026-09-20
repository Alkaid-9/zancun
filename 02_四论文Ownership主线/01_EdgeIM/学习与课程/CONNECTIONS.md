# EdgeIM 跨站连接索引

**用途**：登记八张跨站概念卡的解锁条件与回答主题。
**读者**：按 `0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7` 学习的零基础学习者。
**边界**：本页不放卡片正文、不提供答案，也不直接链接受控文件。完成对应站核心题后，只从该站 README 的授权入口打开一张卡；入口尚未出现时，不自行搜索 `_sealed` 目录。

| 卡号 | 解锁条件 | 回答主题 |
|---|---|---|
| C00 | EX-00 核心题完成后 | 比较两类选择接口；检查遍历顺序改变时各输出量需要什么证据 |
| C01 | EX-01 核心题完成后 | 区分三类计数；判断某份摘要能否满足一个明确消费者 |
| C05a | EX-05a 核心题完成后 | 区分表示、运行中记忆、跨输入性质与外部裁判 |
| C02 | EX-02 核心题完成后 | 追踪图分组、日志子序列与阈值判断分别需要哪些信息 |
| C03 | EX-03 核心题完成后 | 分开两个判定维度；检查选择后样本能否代表原总体 |
| C05 | EX-05 核心题完成后 | 校准四类论证或验证手段各自能支持到哪里 |
| C06 | EX-06 核心题完成后 | 逐项对齐主张、直接证据、来源、归属和缺口 |
| C07 | EX-07 核心题完成后 | 检查量词、适用范围与不同模型质量判断是否被混用 |

## 使用规则

1. 先完成本站 README 的核心题并留下自己的答案或预测，再从本站授权入口开卡。
2. 每次只开当前站的一张卡；后续卡号存在不等于已获授权。
3. `CONNECT` 是核心题后的跨站检查，`EXTEND` 是可选研究题；两者都不改变各站 README 中冻结的 PASS 条件。
4. 卡片内容属于教学材料，不自动证明学习者掌握；状态仍按 `SEEN / SUBMITTED / PASS / RETAINED` 区分。
5. 充分信息、等价、效度等概念若出现在卡中，只能按卡内问题作答；不得把定义本身当成 EdgeIM 的对应结论。

## 提交规则

集中提交时用四栏：`卡号 | 我的判断 | 依据或反例 | 证据上限`。引用旧作答可写“文件路径 + 标题”，但预测、脱稿和冷启动复测必须产生新证据。

受控卡片的站内授权入口由对应 README 维护；本索引不承担开封功能。

## 四论文观察镜头（2026-09-05）

详细调度见 `FOUR_PAPER_TRAINING_LOOP.md`。这些镜头在站点 PASS 后打开，不替代 C00-C07，也不修改站点 PASS。

| 镜头 | 解锁 | 训练问题 | 深度 |
|---|---|---|---|
| L-S1 sigRank | EX-01 PASS | coverage vs importance；endogenous size vs ratio | 30-45 分钟 |
| L-S2 sigRank | EX-05 PASS | downstream model quality 与 fair comparison | 2-3 小时 |
| L-GT Ground Truth | EX-06 PASS；EX-07 前必过 | GT/deviation/recording error 与 claim-evidence | 2-3 小时 |
| L-CX1 CrossEdgeIM | EX-06 PASS + 能解释 IM/PN downstream | predecessor → residual → redesign → new residual | 60-90 分钟 |
| L-CX2 CrossEdgeIM | Transfer Card 阶段，可选 | interaction semantics residual | 按卡时间盒 |

当前不在本索引批量重判镜头状态。历史位置记录为 EX-05，但先按[证据对账路由](../../../01_进组总计划_OE1_材料交付/CURRENT_LEARNING_ROUTE.md)核 C00/C01/C05a/C02 与各自前置；有真实 PASS 证据才解锁对应镜头。十五题 D2 不是当前前置。
