# 技能模块索引：博弈论均衡思维

**目标**：掌握用博弈论建模多智能体系统安全问题的能力

**最后更新**：2026-05-04

---

## 模块结构

| 文档 | 内容 | 状态 |
|---|---|---|
| `00_INDEX.md` | 模块索引 | ✅ |
| `01_overview.md` | 博弈论在 OR 中的角色 | ✅ |
| `02_equilibrium_concepts.md` | 均衡概念对比（纳什/Wardrop/Stackelberg）| ✅ |
| `03_paper02_equilibrium.md` | 案例：Paper 02 的 Stackelberg + Wardrop 嵌套 | ✅ |
| `04_paper01_equilibrium.md` | 案例：Paper 01 的 UU/DD/DU/UD 四象限 | ✅ |
| `05_mas_application.md` | 多智能体系统应用 | ✅（骨架）|
| `06_practice_tasks.md` | 练习任务 | ✅ |

---

## 核心能力清单

- [x] 区分纳什均衡、Wardrop 均衡、Stackelberg 均衡的适用场景（见 02）
- [x] 能分析 Paper 02 的 v_E > v_F / v_E < v_F 双场景均衡（见 03）
- [x] 能分析 Paper 01 的 UU/DD/DU/UD 四象限均衡（见 04）
- [x] 理解"crowd-out"机制的形式化表达（见 03 §5）
- [x] 能将均衡分析映射到多智能体系统（见 05）

---

## 学习路径

新手按 01 → 02 → 03 → 04 → 05 → 06 顺序学。

进阶（已读完 Paper 01/02 拆解）可直接从 02 读起，03 和 04 是"方法论演练"。

---

## 关联素材

- WORKING_LOG: `research/_archive/jiang/02_loss_aversion_queue/log/02_02_understand_equilibrium.md`
- Paper 01 均衡: `research/_archive/jiang/01_behavior_pricing/code/bbp_model.py`
- Paper 01 拆解: `research/_archive/jiang/01_behavior_pricing/source/03_equilibrium.md`
- Paper 02 拆解: `research/_archive/jiang/02_loss_aversion_queue/01_breakdown/03_equilibrium.md`

---

## 篇幅与待补

- `05_mas_application.md` 是**骨架**，每个映射可展开成独立论文（见 RESEARCH_DIRECTIONS.md Direction C）。
- 形式化验证（LTL / Coq / Lean）工具链未涉及——等 Sun 论文收集完成后补充。
- 机制设计（Myerson / Mussa-Rosen）放到下一模块或 Direction B 工作中。
