# Paper 02 — 损失厌恶排队论文节点

**文件名 tag**：`论文节点` `Paper02` `损失厌恶` `JSSC` `Jiang` `2023` `心理异质性` `M/M/1` `排队`

**版本**：v1.0
**创建日期**：2026-05-03

---

## 基本信息

| 字段 | 内容 |
|---|---|
| **标题** | Psychological Heterogeneity in a Queue: The Impact of Loss Aversion on Service Pricing |
| **作者** | Jiang, Gao, Chai, Bu |
| **期刊** | Journal of Systems Science and Complexity (JSSC) 36: 2536-2558 |
| **PDF** | `research/_archive/jiang/02.pdf` |
| **Track** | 明线（OR + 排队 + 行为定价，姜老师方向）|

---

## 一句话总结

首次把心理异质性（经验理性型 E vs 首次损失厌恶型 F）结合双维度损失厌恶（价值 + 时间）嵌入 M/M/1 排队定价，发现两类顾客通过共享等待时间相互影响，存在分段均衡和损失厌恶依赖的价格截止阈值。

---

## 核心模型

### 两类顾客 + 损失厌恶效用函数

**E 型（经验/理性）**：
$$U_E = R_{12} - P - \theta_E W_0$$

**F 型（首次/损失厌恶）**：
$$U_F = R_{12} - P - (\alpha-1)\gamma(1-\gamma)(R_H-R_L) - \left(1 + \frac{\beta-1}{e}\right) \theta_F W_0$$

### 关键参数

| 参数 | 定义 | 范围 | 作用 |
|---|---|---|---|
| α | 价值损失厌恶系数 | ≥ 1 | 价值维度的损失放大 |
| β | 时间损失厌恶系数 | ≥ 1 | 时间维度的损失放大 |
| γ | 高感知概率 | [0, 1] | 感知价值分布 |
| R_H, R_L | 感知服务价值 | — | 两点分布 |
| θ_E, θ_F | 延迟敏感度 | — | 单位时间等待成本 |

---

## 四段均衡

| 段 | 价格范围 | E 型 | F 型 |
|---|---|---|---|
| **段 1** | P > P̄₁ | 混合策略 | 全部 balk |
| **段 2** | P₁ < P ≤ P̄₁ | 全部加入 | 全部 balk |
| **段 3** | P₂ < P ≤ P₁ | 全部加入 | 混合策略 |
| **段 4** | P ≤ P₂ | 全部加入 | 全部加入 |

---

## 关键结论

### ✅ 已独立验证

1. **F 型效用函数系数 (β-1)/e 正确** — SymPy 验证
2. **感知服务价值增益-损失分解正确**
3. **四段均衡结构逻辑自洽**
4. **最优定价结构良定义**
5. **α = β = 1 时退化为经典模型**

### ⚠️ 待验证

1. 命题 5.3 中 R₂ vs R_L 疑似笔误
2. 命题 4.3 的"类似证明"（未独立验证）
3. Figures 1-10 数值复现

---

## 行为旋钮：α 和 β

**核心发现**：α/β 是"行为旋钮"，转动时改变均衡结构。

- α/β 高 → F 型顾客支付意愿被压低 → 最优价格降低
- α/β 低 → F 型顾客更像理性 → 最优价格升高

**与 Paper 01 的 θ 平行**：都打破经典单调性。

| 参数 | Paper 01 | Paper 02 |
|---|---|---|
| 行为旋钮 | θ | α, β |
| 类型 | 识别精度 | 损失厌恶 |
| 作用对象 | 消费者 | 顾客 |
| 经典单调性被打破 | 高质高价 | 价格低→顾客多 |

---

## MAS 桥接

| 损失厌恶概念 | MAS 对应物 |
|---|---|
| F 型顾客 | 有行为偏差的 agent |
| E 型顾客 | 理性 agent |
| α（价值损失厌恶）| Reward sensitivity |
| β（时间损失厌恶）| Patience / planning horizon |
| 参考点 R̄, W̄ | Initial prompt / context |
| v_E, v_F | Agent participation threshold |
| 四段均衡 | Resource competition phases |
| Crowd-out | Resource contention |
| 价格截止阈值 | Safety threshold |

---

## 发现的 Gap

| Gap | 类型 | 描述 |
|---|---|---|
| G2.1 | 假设过强 | REE vs "无经验"内在矛盾 |
| G2.2 | 缺少分析 | 无福利分析 |
| G2.3 | 缺少分析 | Crowd-out 未量化 |
| G2.4 | 范围有限 | 参考点固定为 REE |
| G2.5 | 方法限制 | 单期模型，无学习机制 |
| G2.6 | 结构平行 | α/β 与 θ 平行 |

---

## 研究方向

| 方向 | 新颖性 | 可行性 | 推荐度 |
|---|---|---|---|
| A: 放松 REE 假设 | ⭐⭐⭐⭐ | ⭐⭐⭐ | 🔴 |
| B: 福利分析 | ⭐⭐⭐ | ⭐⭐⭐⭐ | 🔴 |
| C: Crowd-out 量化 | ⭐⭐⭐ | ⭐⭐⭐⭐ | 🟡 |
| D: 参考点敏感性 | ⭐⭐⭐ | ⭐⭐⭐ | 🟡 |
| E: 多期模型 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 🟡 |
| F: MAS 映射 | ⭐⭐⭐⭐ | ⭐⭐⭐ | 🔴 |

---

## WORKING_LOG 索引

| Session | 主题 | 文件 |
|---|---|---|
| Session 1 | 验证 (β-1)/e 系数 | `log/02_01_verify_beta_coefficient.md` |
| Session 2 | 理解四段均衡逻辑 | `log/02_02_understand_equilibrium.md` |
| Session 3 | 待续... | — |

---

## 相关文件

| 文件 | 作用 |
|---|---|
| `research/_archive/jiang/02_loss_aversion_queue/AUDIT.md` | 完整审计报告 |
| `research/_archive/jiang/02_loss_aversion_queue/RESEARCH_DIRECTIONS.md` | 研究方向 |
| `log/` | 推导日志 |
| `learning/modules/09_research_wiki/05_graph/bridge_map.md` | MAS 桥接 |
| `learning/modules/08_thought_extensions/0103_theta_alpha_beta_parallel.md` | 参数平行性 |
| `learning/modules/08_thought_extensions/0102_loss_aversion_multi_angle.md` | 多角度思考 |

---

## 审计状态

| 项目 | 状态 | 日期 |
|---|---|---|
| 公式推导验证 | ✅ (β-1)/e 完成 | 2026-05-03 |
| AUDIT.md | ✅ 完成 | 2026-05-03 |
| RESEARCH_DIRECTIONS.md | ✅ 完成 | 2026-05-03 |
| WORKING_LOG | ✅ Session 1-2 完成 | 2026-05-03 |
| Session 3 | 🔜 待做 | — |

---

## 下一步

1. 完成 Session 3：命题 4.3 验证
2. 从 Gap 2.1（放松 REE）或 Gap 2.2（福利分析）开始研究方向
3. 把 α/β 的"行为旋钮"思想记录到 learning/modules/09_research_wiki/