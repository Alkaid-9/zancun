# B-S3A - Central Aggregation

**资产状态**：BUILT；学习状态默认 LOCKED
**论文坐标**：EdgeIM PDF physical p.5，section IV.D，Algorithm 3 lines 1-8
**前置**：B-S2

## 核心区别

中心端对 endpoint 做集合 union，对关系 weight 做加法：

`{Local_i=(S_i,E_i,R_i)} -> S union / E union / sum R_i(a,b) -> weighted global DFG`

“DFG 有 weight”是论文事实；“后续 cut 一定使用 weight”不是论文已说明事实。

## 任务

1. 闭卷写出中心端输入、状态更新、输出和下游 consumer。
2. 完成 [训练微例](TRAINING_FIXTURE.md) 的 endpoint-union 表和 relation-sum 表。
3. 写最小 aggregate 函数，并检验 local-node permutation、空节点、相同总量不同分布。
4. 单列信息保留/丢失：总权重、endpoint membership、节点来源、trace multiplicity、事件顺序。
5. relation endpoint 不在 `S/E` 仍按 Algorithm 3 的关系循环进入 DFG；真正保持 SOURCE-OPEN 的是完全没有 relation 的 singleton/isolated activity 是否进入 DFG。
6. 形成 Mechanism Map 草稿。

提交 Evidence Record、两张表、代码/测试、信息损失表和全文回接句。
