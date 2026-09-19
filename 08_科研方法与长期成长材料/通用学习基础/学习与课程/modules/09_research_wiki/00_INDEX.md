# 知识图谱 — 总入口

**文件名 tag**：`知识图谱` `总入口` `索引` `图谱导航` `节点` `关系`

**版本**：v1.0
**创建日期**：2026-05-03

---

## 什么是知识图谱？

知识图谱把分散的概念、论文、结论、想法组织成一张**网**。

**节点**：论文、结论、概念、想法
**边**：关系（验证、扩展、矛盾、桥接）

**好处**：
- 看到知识之间的联系
- 发现新的研究方向
- 追踪你的思考过程

---

## 图谱结构

```
learning/modules/09_research_wiki/
├── 00_INDEX.md              ← 本文件
├── 01_papers/              ← 论文节点
│   ├── paper01_bbp.md
│   └── paper02_loss_aversion.md
├── 02_claims/              ← 结论节点
│   ├── claim_beta_coefficient.md
│   └── claim_hessian_ndf.md
├── 03_concepts/            ← 概念节点
│   ├── concept_utility_function.md
│   ├── concept_loss_aversion.md
│   └── concept_equilibrium.md
├── 04_ideas/               ← 想法节点
│   ├── idea_self_blinding.md
│   └── idea_bayesian_learning.md
└── 05_graph/               ← 关系图
    ├── or_concepts_map.md
    ├── mas_concepts_map.md
    └── bridge_map.md
```

---

## 快速查询

### Q1: 我想查某个概念

去 `03_concepts/` 目录，找对应的概念卡。

### Q2: 我想看 Paper 01 和 Paper 02 的关系

去 `05_graph/bridge_map.md`

### Q3: 我想看所有已验证的结论

去 `02_claims/` 目录

### Q4: 我想找某个 Gap 相关的想法

去 `04_ideas/` 目录，文件名包含 Gap 来源

---

## 节点类型说明

### 论文节点 (papers/)

**内容**：论文的核心信息卡
- 标题、作者、期刊
- 一句话总结
- 关键公式/命题
- 审计发现
- MAS 钩子

### 结论节点 (claims/)

**内容**：从论文中独立验证的结论
- 结论内容
- 验证方法
- 状态（confirmed/pending/contradicted）

### 概念节点 (concepts/)

**内容**：核心概念的定义
- 一句话定义
- 形式化定义
- 在论文中的位置
- 相关概念

### 想法节点 (ideas/)

**内容**：研究方向的想法
- 来自哪个 Gap
- 核心假设
- 预期结果
- 可行性评估

### 关系图 (graph/)

**内容**：节点之间的关系
- OR 概念关系图
- MAS 概念关系图
- 桥接关系图

---

## 知识积累流程

### 每次学习后

1. **新学概念** → 添加到 `03_concepts/`
2. **新验证结论** → 添加到 `02_claims/`
3. **新产生想法** → 添加到 `04_ideas/`
4. **新建立联系** → 更新 `05_graph/` 下的关系图

### 每次审计后

1. 更新 `01_papers/` 的论文节点
2. 补充 `02_claims/` 的结论节点
3. 如果有新 Gap → 新建 `04_ideas/` 想法

---

## 知识图谱示例

### OR 核心概念链

```
效用函数
    ↓ 衍生
损失厌恶 ←→ 等待时间成本
    ↓          ↓
支付意愿 v_E, v_F
    ↓
四段均衡（Wardrop）
    ↓
最优定价（Stackelberg）
```

### 明暗线桥接

```
Paper 01 θ (识别精度) ←→ Paper 02 α/β (行为旋钮)
        ↓                        ↓
MAS observation accuracy    MAS agent 行为偏差
```

---

## 相关文件

| 文件 | 作用 |
|---|---|
| `learning/modules/00_MASTER_INDEX.md` | 学习框架总入口 |
| `learning/methodology/SOP.md` | 学习 SOP + 科研 SOP |
| `learning/modules/07_training/0101_gap_to_idea.md` | Gap→Idea 思维训练 |
| `learning/modules/08_thought_extensions/` | 思维拓展模块 |

---

## 下一步

1. 先读 `05_graph/bridge_map.md` 了解 OR 和 MAS 的桥接关系
2. 再读 `05_graph/or_concepts_map.md` 了解 OR 概念之间的关系
3. 如果你要生成研究方向，先查 `04_ideas/` 看看有没有相关想法