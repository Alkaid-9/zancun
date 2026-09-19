# B-S3B - Recursive Discovery and Model Boundary

**资产状态**：BUILT-WITH-SOURCE-OPEN；学习状态默认 LOCKED
**论文坐标**：EdgeIM PDF p.3 Definition 5；p.5 section IV.D、Algorithm 3 lines 9-23；p.6 soundness 叙述
**前置**：B-S3A 与既有 EX-02

## 两层必须分开

1. **EdgeIM PRIMARY**：base case、检测四类 pattern、split、递归、merge，输出写成 Petri Net。
2. **补充教学层**：具体 cut predicate、priority、partition、fall-through、process tree、PN conversion、soundness checker。EdgeIM 原文没有完整给出，必须标为外部理论或 PM4Py `2.7.23.6` implementation evidence。

## 任务

1. 对 [训练微例](TRAINING_FIXTURE.md) 使用题面提供的 pattern/partition oracle，追踪递归调用，不自行发明 cut。
2. 写每次 call 的 input、pattern、partition、sub-return、merge 和终止理由。
3. 将同一结构分别写成“论文明确的 orchestration”和“补充表示”；每句标源。
4. 使用 PM4Py 时记录版本、API、输入接口和输出；明确它消费 event log，不是 EdgeIM Algorithm 3 的 aggregated DFG 实现证据。
5. 给出一个“fitness 高但不能由此证明 soundness”的反例论证。
6. 对 no-cut、empty graph、global `S/E` 是否投影等项保持 SOURCE-OPEN。

提交递归 trace、来源分层表、PM4Py 运行或 NOT RUN、soundness proof obligation、全文回接句。
