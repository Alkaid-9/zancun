# EdgeIM Mastery Gate 与学习路线重构

**日期**：2026-09-05  
**状态**：`SUPERSEDED`——本文件由错模型窗口产出，用户 2026-09-06 拍板「设计新计划」重构，取代文件见 `learning/training/lu-edgeim-algo1/MASTERY_GATE.md`。本文件原样保留作历史记录，不再是现行判断。
**目标**：从"节点式学习"升级到"整篇论文 ownership + 小而真实的 research neighborhood"

---

## 核心转变

### 旧模式的风险

- **问题**：局部节点学很深（如 Algorithm 1 的每行代码）→ 但整篇论文联系不上 → 面试时掉包
- **症状**：能讲 `R_tmp`、`u`、`+1`，但不能回答"EdgeIM 整体解决什么问题""三阶段为什么必须这样接"
- **影响**：进组面试风险极高

### 新模式的核心原则

> **实践 scope 可以窄；认知 scope 不能窄。**

- 完整复现可以不是硬门槛
- 完整吃透论文**必须**变成硬门槛
- 每个学习节点都要成为往四周发射问题的接口

---

## EdgeIM Mastery Gate：六道门

### 1️⃣ Whole-Paper Reconstruction（整篇重建）

**要求**：关掉 PDF，能从头讲完整流程

```
Event Log  
  ↓  
Sampling / Filtering (Stage 1)  
  ↓  
Local (S_i, E_i, R_i) @ each edge node  
  ↓  
Global Aggregation (union)  
  ↓  
DFG (Directly-Follows Graph)  
  ↓  
Inductive Miner Decomposition  
  ↓  
Petri Net  
  ↓  
Evaluation (fitness / precision / F-measure / runtime)
```

**核心问题**：每个箭头都要回答
- "为什么需要它？"
- "它保存了什么信息？"
- "它丢了什么？"

**检验方法**：随机给一个小日志，能否口头完整走一遍不看论文

---

### 2️⃣ Algorithm Ownership（三段算法都要手推）

**Stage 1 (Algorithm 1)**
- 输入：Event log L
- 维护的状态：U（已覆盖特征集）
- 保留判据：新 trace 中有未被 U 覆盖的 S/E/R
- 输出：D' (filtered log)

**Stage 2 & 3**
- 为什么中心端收到 (S, E, DFG) 以后还能跑 IM？
- DFG 作为输入时，IM 怎样递归分解？
- cuts 是什么？IM 为什么要检测 sequence/parallel/choice/loop？

**检验方法**：
- 随机给一个 synthetic event log（如 10-20 条 trace）
- 不看论文，手工走完整条 pipeline
- 写出每步的中间结果（S、E、R、DFG、process tree 片段）

---

### 3️⃣ Formal-Object Mastery（每个表示都不只是术语）

**要掌握的对象**

| 对象 | 五层掌握 |
|------|---------|
| Event | 定义 → 最小例子 → 为什么下游需要 → 丢失的信息 → 何时映射成同一个表示 |
| Trace | 活动序列；记录 start/end → 相邻对的顺序与重复 → 与日志的关系 |
| Event Log | 多条 trace 的多重集 → 事件总数与 trace 条数分开 → DFG 计数公式（Σ\|σ\|-trace条数） |
| DFR (Directly-Follows Relation) | 相邻活动对（集合） → 与 weight 的区别 → 为什么 DFR 够给 IM |
| Weight | 相邻对出现次数 → 与 DFG 支持集合的关系 → 下游用途 |
| DFG | (节点=活动、边=DFR、权重=出现次数) → 与 Petri net 的区别 → 什么信息丢了 |
| Process Tree | IM 输出；代表控制流 → 与 Petri net 的关系 → 为什么 IM 要递归切分 |
| Petri Net | (P, T, F, λ)；并发与同步 → soundness 的直觉 → 为什么需要它 |

**检验方法**：
- 我不提示，你能定义；
- 我换例子，你能算；
- 我改参数，你能预测失效

---

### 4️⃣ Claim–Evidence Audit（论文的每个结论都要知道证据）

**论文的主要 claims**

| Claim | 实验直接支持？ | 作者解释？ | 证据充分度 |
|-------|---------------|-----------|----------|
| 结构无损（zero loss at Stage 1） | ✓ (DFG 不变) | ✓ (相对 IMd) | partial（仅限采样后保持 DFR） |
| 通信开销低 | 理论分析 | ✓ | 无实际网络实验 |
| 隐私保护 | × | ✓ (仅边缘不传日志) | 无加密/差分隐私分析 |
| Scalable | ✓ (9 个公开日志上的 runtime) | ✓ | 仅限该 9 个日志；与 centralized 对比有可比性限制 |
| 质量接近 IM | ✓ (fitness/precision/F-measure) | ✓ | 仅当 DFG 损失不大时 |

**检验方法**：
- 面试时如果老师问"它证明了 privacy-preserving 吗"，你要能说：
  - "论文说了但没有加密/DP 分析，所以只是相对于日志本身集中存放的风险降低"
  - "不要复读 abstract"

---

### 5️⃣ Attack Mode（能把论文弄坏）

**改哪条假设会坏**

- 改 Algorithm 1 的保留判据（从"新增 S/E/R"→ "固定 K"）→ 样本量不再内生 → 采样偏差风险
- 改 timestamp 处理（从"完全乱序"→ "已有因果顺序"）→ 算法变化
- 改分布（从"论文假定的场景"→ "热更新"）→ 通信/质量 trade-off 变化
- 改下游（从"IM"→ "Alpha Miner"）→ DFG 是否仍然足够

**反例与最小对照**

不要把 Algorithm 1 脑补成"噪声检测器"；用 toy trace 与反例明确区分：
- 选择机制是什么（基于特征新增性）
- 数据生成机制是什么（概率分布）
- 两者交互时的具体行为

**检验方法**：
- 给你一个新的日志特性（如高重复率、多环结构、噪声事件）
- 预测 Algorithm 1 会怎样表现
- 实验验证预测

---

### 6️⃣ Interview Compression（四种深度都能讲）

**30 秒**：  
问题 + 核心 idea + 结果
```
"EdgeIM 是分布式过程发现方法。在 IoT 边缘场景，日志分散在各边缘节点。
我们通过在边缘只保留必要的 directly-follows 信息，而不是采样 case，
把通信开销从全日志降低到 DFG 摘要。实验表明质量接近中央 IM。"
```

**2 分钟**：  
完整 pipeline + 三个 contribution
```
Stage 1: 采样决策（新特征保留）
Stage 2: 边缘节点各自维护局部 (S_i,E_i,R_i)，聚合不丢特征
Stage 3: 中心 IM，处理环与并发

Contribution: 
1) 特征保留比例抽样更精准
2) 聚合不是传模型而是传 DFG  
3) 三阶段架构实验验证
```

**10 分钟**：  
算法细节 + 表示 + 实验与局限
- Algorithm 1 完整推导
- DFG 表示的损失与恢复
- 与 EdgeAlpha 的关键差异（IM vs Alpha）
- 实验：9 个日志、fitness/precision 对比、runtime
- 局限：假设 DFG 足够、无加密、无分布式一致性假设

**被追问 30 分钟**：  
手推反例 + 改 assumption + 相关工作 + 自己的批评
- "如果要求保留 trace-level 并发关系，DFG 还够吗？"
- "与 sigRank 相比，为什么不用 significance ranking？"
- "后来的 CrossEdgeIM 改成模型组合而不是特征聚合，为什么？"
- "我最怀疑的是：通信开销对比没有真实网络，只是理论"

---

## 学习节奏重构：双线程推进

### ❌ 旧的"串行"模式
```
学 Algorithm 1 特性 → 全吃透  
  → 回到整篇论文  
  → 发现自己忘了 DFG 定义  
  → 又回去补  
  → 最终时间浪费，知识孤立
```

### ✅ 新的"双线程"模式

**纵向线程**（深度）
- 当前节点往下吃透
- 公式、算法、反例、toy example 都做
- 比如学 DFG → 为什么权重很关键 → 相邻对计数的三层定义 → 与 DFR 的区别

**横向线程**（接回）
- 每学完一个节点，立刻更新整篇论文心智模型
- "这个节点在 EdgeIM 整体里解决哪一段？"
- "它的输入从哪里来？输出被谁消费？"
- "如果删掉它，整篇哪里断？"

**每节课结束必须回答**
```
Q: "我今天学的这个东西，让我对整篇 EdgeIM 的理解改变了什么？"

例如：
- 今天学了 DFG 的权重计算 → 现在明白为什么 Stage 1 必须保留 case 而不能直接采样
- 今天学了聚合规则 → 明白中心端为什么能直接跑 IM
```

---

## 学习方向树：一棵树干 + 多个枝干

**主脊柱**：EdgeIM 完整流程

```
Edge node → Local (S_i, E_i, R_i)  
    ↓  
Central Aggregation  
    ↓  
Global DFG  
    ↓  
IM Decomposition  
    ↓  
Petri Net  
    ↓  
Evaluation
```

**四个关键的横向/纵向分枝**

### 分枝 A：Sampling & Selection 设计空间
- **源**：Algorithm 1（"新增 S/E/R"保留判据）
- **横向对比**：sigRank (significance-based)、fixed-K sampling、MaxCoverage
- **核心问题**：coverage vs significance vs budget 是不是同一个目标？
- **实验**：用 synthetic log 对比三种采样在不同数据分布下的结果
- **研究操作符**：覆盖标准审计、偏差诊断、成本对比

### 分枝 B：Representation & Loss 分析
- **源**：DFG 是怎样的摘要？什么信息丢了？
- **纵向**：sufficient statistics → identifiability → recovery conditions
- **相关概念**：information theory、lossy compression、coreset
- **核心问题**：DFG 足以支持哪些下游任务？不足以支持哪些？
- **实验**：人为删除 trace 特性（重复 event、环、并发），观察 DFG 与 IM 输出变化
- **研究操作符**：表示质疑、保持条件审计、下游需求对齐

### 分枝 C：Model Discovery 与 Petri Net 语义
- **源**：为什么 IM 能在 DFG 上工作？
- **纵向深度**：IM 算法的完整递归过程 → cuts 的定义 → soundness 与 precision
- **相关概念**：process tree、loop handling、concurrency detection
- **核心问题**：IM 的输出对哪些性质有保证？对哪些性质无保证？
- **实验**：用同一个 DFG 跑 IM vs Alpha Miner，对比输出结构
- **研究操作符**：保证审计、模型选择对比、算法边界诊断

### 分枝 D：Evaluation & Evidence 训练
- **源**：论文说"质量接近 IM"，实验怎样证明的？
- **Ground Truth 之用**：构造已知真相的合成日志 → 控制变量 → 排除混杂因素
- **核心问题**：fitness/precision/F-measure 三指标各测什么？通信/时间 trade-off 真的存在吗？
- **小实验**：
  - 生成不同规模的 synthetic log
  - 人为注入噪声、丢事件、改并发关系
  - 对比 EdgeIM vs IM vs EdgeAlpha 的响应
- **研究操作符**：测量有效性审计、混杂因素控制、合理性检查

### 分枝 E：思想谱系与后继（纵向）
- **前置瓶颈**：Centralized IM 在 IoT 场景为什么不可行？（通信、存储、延迟）
- **EdgeAlpha 的方案**：Alpha Miner 的特征（快但表达力弱）
- **EdgeIM 的改进**：不是聚合模型，而是聚合 DFG 特征 → 为什么？
- **CrossEdgeIM 的后继**：顶层改成模型组合 + 跨组织交互表示 → 新瓶颈是什么？
- **研究操作符**：瓶颈迁移追踪、设计转折点分析、演进脉络重建

---

## 每个节点下的标准检验清单

每个分枝的每个节点都要同时挂：

```
[原论文怎么做]  
  → 这是基于什么假设  
  → 假设对吗  
  
[别人怎么做]  
  → 为什么不同  
  → 哪个更好  
  
[能不能手造反例]  
  → 什么条件下 EdgeIM 的选择会变坏  
  
[能不能写最小实现]  
  → 用 pseudocode 写 Algorithm 1  
  → 用 numpy 模拟一个 toy example  
  
[能不能做小实验]  
  → synthetic log 对比  
  → 预测 → 验证  
```

---

## 进组面试升级标准

### ✅ 新的最低线

```
✓ EdgeIM 全文可重建（无论深度问什么都能接回整篇逻辑）
✓ 核心算法可手推（给任意小日志能完整走一遍）
✓ 最小实现可重建（pseudocode + 一个 toy example 的手工计算）
✓ Claim 可审计（知道每个结论的证据边界）
✓ Assumption 可攻击（能说出改哪个会坏、反例是什么）
✓ 一个小研究问题跑完闭环（比如 sampling criterion 对比实验）
✓ 脱稿承受连续追问（30 分钟被问都不掉包）
```

### 面试模拟题库

**30 秒一句话**  
- "说一句 EdgeIM 是干什么的"

**2 分钟**  
- "完整讲 EdgeIM 的三个阶段"
- "EdgeIM 相对 IM 改了什么"
- "EdgeIM 相对 EdgeAlpha 的优势"

**5 分钟**  
- "Algorithm 1 的保留判据为什么是'新增 S/E/R'"
- "为什么中心端收到 DFG 后还能跑 IM"
- "论文的实验怎样证明'质量接近 IM'"

**10 分钟**  
- "给你一个新日志，手工走一遍整个 pipeline"
- "如果改成固定 K 采样会怎样"
- "DFG 相对完整日志丢了什么关键信息"

**30 分钟追问**  
- "为什么不用 significance ranking（sigRank）"
- "timestamp 冲突的假设改变后算法还对吗"
- "CrossEdgeIM 为什么要改成模型组合而不是特征聚合"
- "论文有哪些没证明但声称的东西"
- "你最怀疑论文哪一个 claim"

---

## 进组前的现状重测

**不用复习，直接诊断（前 3-5 天）**

我会随机问这 15 个问题，根据实际掉包位置重新长知识树：

1. "一句话说 EdgeIM。"
2. "为什么 Stage 1 不能单独算贡献闭环？"
3. "S、E、R 分别保什么？"
4. "DFG 丢掉什么？"
5. "为什么中心端还能跑 IM？"
6. "EdgeAlpha 的问题到底是什么？"
7. "论文哪个实验能支持'scalable'，哪个不能？"
8. "Algorithm 1 去掉顺序依赖会怎样？"
9. "给你一个新日志，手走一遍。"
10. "你最不信论文哪一个 claim？"
11. "如果改采样标准会怎样？"
12. "DFG 对哪些下游任务足够？"
13. "论文的隐私声称有多少实际支持？"
14. "为什么不用固定比例采样？"
15. "CrossEdgeIM 改架构的理由是什么？"

**结果**：知道你在哪里真掌握、哪里只是听懂、哪里能迁移、哪里面试一戳穿。

---

## 节点状态定义（防止"熟悉感冒充掌握"）

**只有满足这些条件，我才标 OWNED**

```
✓ 我不提示，你能定义
✓ 我换例子，你能算
✓ 我改条件，你能预测失效
✓ 我给反例，你能诊断哪里坏了
✓ 我问"为什么不是另一个设计"，你能比较
✓ 我隔三天再问，你还能讲
✓ 我问它在整篇论文哪个位置，你能接回去
```

**不然最多 SEEN / OPEN**

---

## 实践 scope vs 认知 scope

### 旧的混淆

> 做完一个窄实验，能讲清楚 → 就算形成闭环

### 新的原则

> 实践 scope 可以窄（比���只做 sampling 对比实验）
> 认知 scope 不能窄（必须理解整篇 EdgeIM 背景）

**例子**

- **窄实验**：EdgeIM filtering vs fixed-K vs significance ranking 对比
- **广认知**：这个对比为什么重要？背后的采样设计理论是什么？与下游模型质量的关系如何？整篇论文在这点上的立场是什么？

---

## 递推式冻结的计划（按周推进）

### Week 1 (09-05 ~ 09-08)：现状诊断 + 知识树重建

- 做完 Whole-Paper Diagnostic（15 题）
- 根据掉包位置，重新画出个人的"理解缺口地图"
- 不补基础，直接对齐痛点

### Week 2 (09-09 ~ 09-15)：主脊柱 + 单个分枝深入

- 按 Mastery Gate 的六道门，逐个自测
- 挑一个分枝（比如 Sampling & Selection）集中做
- 完成一个对比实验（synthetic log、变量控制、结果对比）

### Week 3 (09-16 ~ 09-22)：面试模拟 + 压力测试

- 每天做 2-3 个面试题（不同深度）
- 记录每次掉包的细节
- 针对性补充反例与设计比较

### Week 4 (09-23 ~ 09-30)：冷复测 + 自信度验证

- 隔一周重新做一遍诊断题
- 验证是否满足六道门
- 准备进组自我介绍的两个版本：30 秒版 + 2 分钟版

---

## 成功标志

当满足以下所有条件，才能说"可以去找鲁老师"：

```
□ 整篇论文能无纸笔讲出逻辑闭环
□ 三个 Algorithm 都能手推（不看公式）
□ 所有形式对象都能定义 + 举例 + 说明下游用途
□ 每个主要 claim 都知道证据边界
□ 至少能指出 3 个"改 assumption 会坏的地方"
□ 做完了一个对比实验（sampling 或其他），结果自己能讲清
□ 能用四种深度讲（30秒、2分钟、10分钟、30分钟追问）
□ 冷复测（隔三天）的掉包率 < 10%
```

---

## 核心心态

不是"我已经学了很多东西，应该差不多了"。

而是：

> **以 EdgeIM 为中心，建立一个小而真实的 process-discovery research neighborhood。**
> 
> 在这个 neighborhood 里完成至少 1-2 个自己真正走过的比较 / 反例 / 实验闭环。
> 
> 最后能自然地说：  
> "我从 EdgeIM 的采样设计进去，发现它牵涉到更一般的问题……我对比了几种方案，现在的观点是……"

这样才不是"背老师论文"，而是"沿着老师论文里的一个设计问题自己走了几步"。

---

## 权威链接

- 《科研学习与训练体系 v0.3》：整体框架（七图、操作符、能力观察）
- 《研究操作符与横向迁移案例册》：具体实例与可借动作
- BRIEF.md + Amendment：当前站点冻结与 PASS 条件
- 本文件：进组准备的新硬门与学习路线

---

**更新记录**  
- 2026-09-05：v1.0 冻结，六道门 + 双线程 + 四个分枝架构确定
