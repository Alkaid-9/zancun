# B-S2 - Edge-side Local Feature Construction

**资产状态**：BUILT；学习状态默认 LOCKED
**论文坐标**：EdgeIM PDF physical pp.2-4，Definitions 3-4、section IV.A/C、Algorithm 2
**前置**：EX-05a；进入 EX-07 最终 verdict 前必须完成

## 零基础桥

- `S_i`：节点 i 见到的 trace 起点活动集合。
- `E_i`：节点 i 见到的 trace 终点活动集合。
- `R_i(a,b)`：节点 i 保存的相邻活动关系计数，不是 Stage 1 的集合 `R`。
- hash 分派：论文写 `hash(activity) mod k`；hash 家族、seed、负载平衡证据没有给出。
- 同时间戳：对相邻的两个事件同时累计两个方向；三事件同刻的排列规则没有给出。

## 任务

1. 闭卷画出 `D' -> event traversal -> node j -> S_i/E_i/R_i -> local triplets`。
2. 对 [训练微例](TRAINING_FIXTURE.md) 逐事件填写 before/update/after 表。
3. 写最小实现 `construct_local_features(filtered_log, node_of)`。活动到节点的映射作为参数传入，不依赖语言运行时 hash。
4. 至少测试：重复关系、同时间戳、singleton trace、空节点、跨节点相邻关系。
5. 把“论文明确规定”与“实现必须自行声明的 policy”分成两栏；三事件同刻、late event、missing key 不得伪装成论文答案。
6. 回写 Mechanism Map 草稿，但在本人 PASS 前不写共享正本。

## 提交

- 一份 Evidence Record；
- 逐事件状态表；
- 本人最小实现和测试输出；
- paper-stated / implementation-policy / SOURCE-OPEN 三栏；
- 一句“B-S2 怎样改变我对整篇 EdgeIM 的理解”。

作答写新文件，不修改本题。通过条件见 [RUBRIC.md](RUBRIC.md)。
