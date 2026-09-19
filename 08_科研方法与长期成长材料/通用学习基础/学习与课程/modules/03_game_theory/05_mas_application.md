# MAS 应用的博弈论方法论

**状态**: 🔜 重写中。jiang OR 案例已挪至 `learning/_archive_v3_jiang/05_mas_application.md`。

## 目的

把博弈论方法论迁移到 MAS 安全场景。**不预设 OR 范式（BBP/损失厌恶/参考时间）作为主语**——v3 的"jiang 训练 → MAS 安全"映射被反复警告不可行性，v2 重写。

## 框架

### 1. agent 视角
- 每个 agent 有策略空间 `S_i`
- 策略由效用 `u_i` 排序

### 2. 系统视角
- 多 agent 集合 `A = {a_1, ..., a_n}`
- 全局效用 `U = Σ u_i` 或 Pareto 边界

### 3. 安全约束
- 信息流完整性
- agent 行为可验证
- 不出现 Nash-equilibrium-bypass 漏洞

## Sun 论文实例占位

| 论文 | 博弈视角实例 | 待验证 |
|---|---|---|
| Paper 01 MAS Safety | 信任博弈 | [需验证] |
| Paper 02 Trustworthy Agents | persona 协调 | [需验证] |
| Paper 03 Automata Steering | 状态覆盖博弈 | [需验证] |
| Paper 04 ReGA | 验证机制博弈 | [需验证] |
| Paper 05 RL+SMT | 奖励黑客博弈 | [需验证] |
| Paper 06 Backdoor FL | 信任传播博弈 | [需验证] |

## v3 案例

`learning/_archive_v3_jiang/05_mas_application.md` 保留原文。
