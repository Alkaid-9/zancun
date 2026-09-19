# B-S3B Training Fixture

本题把 pattern detection 作为 oracle 给出，只训练递归编排。

Global DFG nodes：`{A,B,C,D}`。

- root oracle：`sequence({A},{B,C,D})`
- subgraph `{B,C,D}` oracle：`choice({B},{C,D})`
- subgraph `{C,D}` oracle：`sequence({C},{D})`
- singleton：leaf

任务：

1. 画完整 call tree，给每个 call 编号。
2. 写每个 call 的输入 nodes、oracle pattern、partitions、返回对象和 merge order。
3. 用 process-tree 记号表达补充表示，但标明它不是 EdgeIM PDF 明写的中间对象。
4. 列出要把该补充树转换为可执行 Petri net 仍需哪些定义、marking 和验证。
5. 题面 oracle 另给 `NO_BASE_PATTERN`。你只需说明 EdgeIM 原文在该分支没有给 fall-through；不要自行证明某张图“确实没有 cut”。
