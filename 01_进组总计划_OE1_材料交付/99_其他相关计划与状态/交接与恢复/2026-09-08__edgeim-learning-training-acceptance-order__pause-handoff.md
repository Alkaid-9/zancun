# EdgeIM 学习—训练—验收顺序进度交接

**Date**: 2026-09-08 Asia/Taipei  
**Type**: pause handoff / progress archive  
**Status**: `ARCHIVED / PAUSED / RECOVERABLE`  
**Scope**: 只归档 EdgeIM 学习、训练、验收顺序与研究解锁关系；不启动诊断、实验、代码修改或进组材料改写。  
**Authority**: 本档记录本次对齐结果；学习站点和 PASS 条件仍以关联正本为准。

## §0 · TL;DR

先诊断，再按 EdgeIM 主干补缺；每站“学习→手算/代码→预测/反例→PASS→冷复测”，横向论文按解锁点插入，EX-07 后才进入最小研究。

## §1 · 本次已完成

1. 重新核对并确认 EdgeIM 的冻结主干顺序：

   ```text
   EX-00 → EX-01 → EX-05a → EX-02 → EX-03 → EX-05 → EX-06 → EX-07
   ```

2. 确认当前入口不是机械重做旧站，而是先完成 `MASTERY_GATE.md §4.2` 的 Whole-Paper Diagnostic（15 题）。

3. 确认每一站的训练闭环：

   ```text
   学习概念
   → 本人手算/画图
   → 对新例子先预测
   → 本人最小实现或修改
   → 对照原文/运行结果
   → 原站 PASS
   → D+2/D+7 或 D+3 冷复测
   ```

4. 确认 EdgeIM 是唯一主干；sigRank、Ground Truth Approach、CrossEdgeIM 是受控观察镜头，不是三套并行主课。

5. 确认研究解锁关系：

   - EX-01 PASS 后，短开 sigRank selection philosophy；
   - EX-05 PASS 后，做完整 EdgeIM–sigRank fair comparison；
   - EX-06 PASS 后，打开 Ground Truth Approach 与 CrossEdgeIM genealogy；
   - EX-07 开始前必须有 world contract；
   - EX-07 PASS 且 Transfer Card=`PROMOTE` 后，才允许一个 toy research test。

6. 确认鲁侧研究路线不抢跑：EX-05a 后可做谱系 citation audit；EX-05 后做 sampling 横向比较；EX-06 后做 Transfer Card；EX-07 后才做最小研究。

## §2 · 当前状态边界

### 已确认的规划事实

- `BRIEF.md` 冻结站序为 `0 → 1 → 5a → 2 → 3 → 5 → 6 → 7`。
- `MASTERY_GATE.md` 将 Whole-Paper Diagnostic 设为当前入口。
- `EX-04` 不另建新站；测量与证据边界由诊断缺口、EX-06 和 EX-07 承接。
- EdgeIM 的“学完”不等于 EX-07 跑出数字，而是同时具备全文重建、算法 ownership、形式对象掌握、claim–evidence 审计、attack mode 和四档表达证据。
- 完整工程复现不是硬门；本人可运行、可修改、可解释的最小实现是硬证据之一。

### 尚未由本次对话验收的事项

- 15 题 Whole-Paper Diagnostic 尚未执行。
- 没有因本次对齐新增任何 EX 站点 PASS。
- 没有新增本人冷启动、手算、代码或反例证据。
- 没有启动 EX-07 实验、Ground Truth world contract 或 Transfer Card verdict。
- 没有将六个鲁侧候选方向中的任何一个选定为研究题目。
- 用户此前报告“已过 EX-03”仍是 `USER-REPORTED`，不能替代新验收记录。

## §3 · 恢复后的第一动作

恢复这条线时，先按下面顺序执行，不先读横向论文、不先跑实验：

1. 读取本档 §2 和 §6；
2. 读取 [MASTERY_GATE.md](../../learning/training/lu-edgeim-algo1/MASTERY_GATE.md) §3、§4.2–§4.3；
3. 在不复习、不打开 `_sealed/` 的情况下完成 15 题诊断；
4. 每题标记 `OWNED / SEEN / OPEN / UNKNOWN`，记录具体掉包点；
5. 只选择 2–4 个最高价值缺口，回流到对应 EX 站点；
6. 诊断未完成前，不打开后续密封答案，不开始研究实验，不把材料写成对外能力证明。

## §4 · 站点验收口径

### P0：地基

`EX-00 → EX-01 → EX-05a`。目标是本人能独立掌握 Algorithm 1、DFG、论文对象和最小实现。EX-05a 必须先纸上写，再敲代码。

### P2：深入主干

`EX-02 → EX-03 → EX-05`。目标是掌握 IM、过程树、噪声、反例、不变量和生成器层；不能把 DFG 保持直接升级为模型等价。

### P3：证据与实验

`EX-06 → EX-07`。目标是把 measurement、claim、evidence、world contract、prediction 和 verdict 串成一条可审计链。

## §5 · 停止条件与边界

- 诊断未完成：停在诊断。
- 证据来源混杂：停在来源澄清，不把 AI 讲解或密封答案记为本人能力。
- 任一站未满足原 PASS：停在该站，不用横向论文掩盖主干缺口。
- 没有可证伪 prediction：研究想法保持 `PARKED`，不升级为题目或 novelty claim。
- 需要新增 infrastructure 才能继续：停下来重新评估范围，不默认扩建平台。
- 本档不授权 commit、push、部署、实验运行或修改学习题面、PASS 条件、Ledger、答案和进组材料。

## §6 · 权威文件与阅读顺序

1. [BRIEF.md](../../learning/training/lu-edgeim-algo1/BRIEF.md) §2、§4、Amendment A1–A7：冻结站序、原题面、PASS 与历史变更。
2. [MASTERY_GATE.md](../../learning/training/lu-edgeim-algo1/MASTERY_GATE.md) §1–§4.3、§6：六道能力门、当前入口、诊断合同和进组应用边界。
3. [FOUR_PAPER_TRAINING_LOOP.md](../../learning/training/lu-edgeim-algo1/FOUR_PAPER_TRAINING_LOOP.md) §3–§5：三篇横向镜头的解锁点。
4. [鲁侧谱系—迁移差分计划](../decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md) §2–§5：P0–P5 解锁关系。
5. [EdgeIM 进组重构稿](../decisions/2026-09-06__research__edgeim-plan-rewrite-draft.md)（如需恢复进组应用层时再读）。

## §7 · 完成标准

本条线只有在以下条件都满足时，才可从“学习主干进行中”升级为“EdgeIM ownership 已形成”：

- Whole-Paper Diagnostic 后的缺口已经回补；
- 原站 PASS 有本人手算、代码、预测或反例证据；
- 至少一次延迟冷复测通过；
- 六道能力门均有可复核记录；
- EX-07 完成 prediction → check → verdict，并写明 claim ceiling；
- 对外进组材料只消费已经过门的证据。

## §8 · 本次窗口结论

本次只完成了路线和验收顺序的重新对齐，未推进学习站点本身。恢复时的唯一默认动作是做 15 题诊断；诊断结果出来后，再决定回补哪些站点。

## §-1 · 复核记录（2026-09-08）

| 维度 | 结果 | 备注 |
|---|---|---|
| L0-1 | ✅ | 本档无 `/tmp/` 路径 |
| L1-1 | ✅ | 交接档已落盘，内容超过 50 行 |
| L1-2 | N/A | 本次未产生新的决策档 |
| L1-3 | N/A | 本次未进行 task 审计 |
| L2-1 | N/A | 本档不新增 task list |
| L2-2 | N/A | 本档不新增并行任务 |
| L2-3 | N/A | 本档不声明 completed task |
| L3-1 | N/A | 本次未新增全局 memory 护栏 |
| L3-2 | ✅ | 未重复建立已有护栏 |
| L4-1 | ✅ | 关联路径使用 Markdown 相对链接 |
| L4-2 | ✅ | 已通过 `progress/handoff/INDEX.md` 登记反向路由 |
| L4-3 | ✅ | §0 TL;DR 为单句短摘要 |

**主控自审结果**：本档已完成自审；未授权事项保持未执行。
