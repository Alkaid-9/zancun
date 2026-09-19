# Paper 01 — BBP 论文节点

**文件名 tag**：`论文节点` `Paper01` `BBP` `Omega` `Jiang` `2026` `行为定价` `不完美识别` `质量差异`

**版本**：v1.0
**创建日期**：2026-05-03

---

## 基本信息

| 字段 | 内容 |
|---|---|
| **标题** | Behavior-Based Pricing strategy of quality-differentiated products with imperfect customer recognition capability |
| **作者** | Jiang, Shen, Guo, Guan |
| **期刊** | Omega 2026 |
| **PDF** | `research/_archive/jiang/01.pdf` |
| **Track** | 明线（OR + 机制设计，姜老师方向）|

---

## 一句话总结

研究在消费者不完美识别产品质量时，企业如何设计基于行为的定价策略（BBP），发现识别精度 θ 作为一个"行为旋钮"，会翻转经典"高质高价"的单调性。

---

## 核心模型

### 两企业价格博弈 + 两期逆向归纳

```
Stage 1: 企业定价（P_O, P_N）+ 消费者识别高质量产品（概率 θ）
Stage 2: 消费者购买 + 企业决定质量（S_H）
```

### 四种均衡类型

| 类型 | 企业 A | 企业 B | 说明 |
|---|---|---|---|
| **UU** | 用 BBP | 用 BBP | 两企业都识别消费者 |
| **DD** | 不用 BBP | 不用 BBP | 两企业都不识别（默认值）|
| **DU** | 用 BBP | 不用 BBP | 仅 A 识别 |
| **UD** | 不用 BBP | 用 BBP | 仅 B 识别（不存在）|

---

## 关键参数

| 参数 | 定义 | 范围 | 作用 |
|---|---|---|---|
| θ | 识别精度 | (0, 2/7) | 控制信息不对称程度 |
| S_H | 质量差异 | 见约束 | 影响企业成本和消费者效用 |
| P_O | BBP 价格 | — | 识别消费者时定高价 |
| P_N | 普通价格 | — | 不识别时定低价 |
| k | 伪装成本系数 | — | 消费者伪装努力成本 |

---

## 关键结论

### ✅ 已独立验证

1. **"联合凹性" = 全局联合凹**（非分段）
2. **∂P_A1/∂S_H 符号修正**：应为 "> 0"（论文误印 "< 0"）
3. **UD 无均衡**：A 通过 deviation 到 D 获益 +0.035
4. **Footnote 7 自洽性**：在全部测试点成立

### ⚠️ 待验证（需 Elsevier 附录）

1. Stage-1 P_A1^DD* 与 Table 5/6 有 3-7% 偏差
2. Proposition 4 市场分割反转（θ̄₃）无法复现

---

## 行为旋钮：θ

**核心发现**：θ 是一个"行为旋钮"，转动时翻转经典模型的单调性。

- θ 高 → 消费者更聪明 → 价格歧视更难 → 企业策略受限
- θ 低 → 消费者更"傻" → 企业有信息租金

**与 Paper 02 的 α/β 平行**：都是打破经典单调性的行为参数。

---

## MAS 桥接

| BBP 元素 | MAS 对应物 |
|---|---|
| θ（识别精度）| Monitor-agent 观测精度 |
| σ（伪装努力）| Agent 对抗行为（prompt injection）|
| κ(θ)（识别成本）| Sensor/probe 计算成本 |
| P_O > P_N | Incentive-compatibility |
| UD no-equilibrium | Peer monitoring is stable |

---

## 发现的 Gap

| Gap | 类型 | 描述 |
|---|---|---|
| G1 | 假设过强 | Rational expectations（消费者必须知道 θ）|
| G2 | 范围有限 | θ_A = θ_B 对称假设 |
| G3 | 缺少分析 | 无福利分析 |
| G4 | 假设过强 | UD no-equilibrium 无形式化证明 |
| G5 | 应用空白 | 未映射到 MAS monitoring |
| G6 | 方法限制 | 无 discounting（δ=1）|

---

## 研究方向

| 方向 | 新颖性 | 可行性 | 推荐度 |
|---|---|---|---|
| A: Self-Blinding Equilibrium | ⭐⭐⭐⭐ | ⭐⭐⭐ | 🔴 |
| B: Mechanism Design View | ⭐⭐⭐ | ⭐⭐⭐⭐ | 🟡 |
| C: MAS Safety Mapping | ⭐⭐⭐⭐⭐ | ⭐⭐ | 🟡 |
| D: Erratum Correspondence | ⭐ | ⭐⭐⭐⭐⭐ | 🔴 |

---

## 相关文件

| 文件 | 作用 |
|---|---|
| `research/_archive/jiang/01_behavior_pricing/AUDIT.md` | 完整审计报告 |
| `research/_archive/jiang/01_behavior_pricing/RESEARCH_DIRECTIONS.md` | 研究方向 |
| `research/_archive/jiang/01_behavior_pricing/code/bbp_model.py` | 符号引擎代码 |
| `learning/modules/09_research_wiki/05_graph/bridge_map.md` | MAS 桥接 |
| `learning/modules/08_thought_extensions/0103_theta_alpha_beta_parallel.md` | 参数平行性 |

---

## 审计状态

| 项目 | 状态 | 日期 |
|---|---|---|
| 公式推导验证 | ✅ Stage-2 完成 | 2026-05-02 |
| AUDIT.md | ✅ 完成 | 2026-05-02 |
| RESEARCH_DIRECTIONS.md | ✅ 完成 | 2026-05-02 |
| 代码验证 | ✅ 7 测试通过 | 2026-05-02 |
| WORKING_LOG | 🔜 待补 | — |

---

## 下一步

1. 补全 `research/_archive/jiang/01_behavior_pricing/log/` 的推导日志
2. 如果要做方向 A，从方向 A 的 pilot 开始
3. 考虑发送勘误邮件给作者