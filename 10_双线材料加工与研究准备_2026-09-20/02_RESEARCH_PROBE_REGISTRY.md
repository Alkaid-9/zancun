# JINZU_MASTER_V2 · 02_RESEARCH_PROBE_REGISTRY

**版本**：v2.0 正式版  
**日期**：2026-09-21  
**状态**：PROBE DEFINITIONS / 执行入口

---

**文件格式说明**：v2.0 §27 建议的目录树里，本文件名为 `02_RESEARCH_PROBE_REGISTRY.tsv`。实际内容包含研究问题的完整论证、Python 接口签名、JSON 反例与嵌套 markdown 表格——这些无法压缩进 TSV 的行列格式而不严重损失信息（这正是 Q2 Representation Preservation 要警惕的"表示降级"）。因此本文件保留 `.md`，把 v2.0 §27 的建议视为一个已知的、有意识的偏离，而非未处理的疏漏。若未来需要机器可读的扁平索引，应从本文件派生一张精简表（如 RP 编号/名称/对应问题/优先级/状态），而不是把本文件整体改名为 `.tsv`。

---

## RP-A · Observation Sufficiency

**对应问题**：Q1（Observation Sufficiency，见 00_OBJECTIVES_AND_CLAIMS.md）

### 研究问题

**在给定可观测字段下，是否足以判断目标安全性质？**

核心研究操作：RO-1（information sufficiency test）

### 首件环境

**系统**：双订单 workflow

**状态对象**：
- order：{id, version, approval, reservation, committed}
- resource：{available, owner}

**事件**：
- approve_request(order_id, version, request_id)
- approve_return(order_id, version, request_id, success)
- revise(order_id) → version++
- reserve(order_id)
- commit(order_id)
- release(order_id)

**可观测信息**（初始配置）：
- order_id ✓
- version ✓
- request_id ✓
- return_success ✓
- resource_owner ✓

### 首件任务

**目标性质** φ：
> commit(A) 必须满足：当前版本的同一订单已经获得过至少一次成功批准，且批准后版本未改变。

**任务**：构造两段完整可实现历史 h₁、h₂，满足：
- α(h₁, commit(A)) = α(h₂, commit(A)) （观测相同）
- q(h₁, commit(A)) ≠ q(h₂, commit(A)) （真值不同）

示例：
```
h₁: approve_return(A, 0, r1, true) → commit(A) ✓ ALLOW
h₂: approve_return(B, 0, r1, true) → commit(A) ✗ BLOCK

观测相同（都看到成功的 approve_return + request_id）
真值不同（h₁ 批准的是同一对象，h₂ 批准的是不同对象）
```

### 交付物

**P0–P1**（本轮必交）：
```
observation_conflict_witness.json
{
  "conflict_pair": [
    {
      "history": "h₁: approve_return(A, 0, r1, true) → commit(A)",
      "observation": "event=approve_return, order_id=?, version=0, request_id=r1, success=true",
      "truth": "ALLOW (批准的是同一对象 A)"
    },
    {
      "history": "h₂: approve_return(B, 0, r1, true) → commit(A)",
      "observation": "event=approve_return, order_id=?, version=0, request_id=r1, success=true",
      "truth": "BLOCK (批准的是不同对象 B，不是 A)"
    }
  ],
  "observation_conflict": true,
  "critical_missing_field": "order_id (在 approve_return 中)",
  "fix": "增加 approve_return 的 order_id 字段"
}
```

（实际格式由执行者定义，上述仅示意）

### 停止条件（DROP 触发）

**以下任一成立，停止此探针**：
1. 仅是"删掉关键字段导致不可区分" → 收为 **abstraction/observability 教学结果**，不升 novelty。
2. 现有 observation 足以判定，加新信息无本质收益 → 停止。
3. 发现目标性质本身就没有合法实现（e.g. 分布式系统无法同步检查版本）→ 停止。

### CONTINUE / REVISE 条件

**继续**：
- 信息足以但实现有 bug → 修 bug，保留探针。
- 信息不足，但不是显然的"关键字段缺失"，有本质的观测难度 → 继续到 RP-D（intervention consistency）。

**修改**：
- 观测时序有问题（e.g. return 到达时间不确定）→ 修改规格/假设，重新测试。
- 目标性质表述不清 → 澄清后重跑。

---

## RP-B · Representation Preservation

**对应问题**：Q2（Representation Preservation，见 00_OBJECTIVES_AND_CLAIMS.md）

### 研究问题

**从原系统映射到某个表示后，是否还保留了目标性质判定所需的信息？**

核心研究操作：RO-2（representation preservation test）

### 首件目标

选择 **String Diagrams** 中的 signature representation。

**目标性质** φ：
> 两个过程的完整执行轨迹相同，但它们的"并发结构"不同。

### 首件反例

```
Process 1: a ; (b || c) ; d
Process 2: choice( a;b;c;d, a;c;b;d )
```

**完整 trace 都可以是**：
- abcd（先 b 后 c）
- acbd（先 c 后 b）

**但**：
- Process 1：b 和 c 在真实执行中可能真正并发（取决于环境）。
- Process 2：b 和 c 互斥（环境决定选哪一个，不会都发生）。

**任务**：
1. 独立分析这两个过程的：
   - 完整 trace 集合
   - 偏序（partial order，不同路径的因果关系）
   - contexts（环境可能的分支点）
   
2. 根据 String Diagrams 定义核算它们的 signature。

3. 结论：
   - 在相同 selection 假设下，两者的 signature 是否不同？
   - 若不同，说明 signature 区分了并发与选择。

### 交付物

**P0–P2**（本轮必交）：

```markdown
semantic_discrimination_matrix.md

| 观察维度 | Process 1 (b||c) | Process 2 choice | 结论 |
|---------|---------|---------|---------|
| 完整 trace 集 | {abcd, acbd} | {abcd, acbd} | ✗ 不能区分 |
| 偏序（因果） | a→b,c; b,c→d（b,c 无约束） | a→{b XOR c}; {b XOR c}→d（互斥） | ✓ 能区分 |
| contexts | ... | ... | ... |
| signature (按论文定义) | ... | ... | ✓ 区分 |
```

加上：
```
one_concurrency_vs_choice_counterexample.md
- 给出具体可执行例（e.g. a=收订单, b=支付, c=发货, d=确认）
- 说明两种情况的现实差异
```

### 停止条件（DROP 触发）

1. 简单 trace 集或偏序已完全区分，signature 无新信息 → DROP "需要 signature"。
2. 论文假设（selection 单调性、connected 图、起止边界）在这个例上不成立 → 修改例或标注前提。

### 接入 EdgeIM 的方式

不改发现算法，补一个"事后审计"：
- 你发现的两个模型的 signature 相等吗？
- 若相等，trace 必然相等（String Diagrams 定理）。
- 若不相等但 trace 相等，说明你的算法隐含了某个 projection。

---

## RP-C · Verification Validity

**对应问题**：Q4（Verifier Correctness，同名对应）+ Q6（Evaluation Validity，仅部分对应——RP-C 只覆盖 oracle 独立性一项，不覆盖 Q6 下 leakage / parsing failure 等其余检查项；详见 00_OBJECTIVES_AND_CLAIMS.md）

### 研究问题

**怎样建立一个我们有资格信赖的 oracle？**

核心研究操作：RO-3（independent oracle + claim ceiling）

### 首件：Petri 网精确 oracle

**目标**：实现一个最小的、可信的 Petri 网 oracle。

**接口**：
```python
def enabled(transition: str, marking: dict[str, int]) -> bool:
    """该标记下哪些变迁可触发？"""

def fire(transition: str, marking: dict[str, int]) -> dict[str, int]:
    """触发一个变迁，返回新标记。"""

def canonical(marking: dict[str, int]) -> str:
    """标记的规范形式（用于去重）。"""

def bounded_bfs(net: PetriNet, max_depth: int) -> BfsResult:
    """有限深度 BFS；未在限制内找到则返回 UNKNOWN。"""
```

### 八类对抗 fixture

必须覆盖：
1. 多前置变迁（multi-input）
2. 自环（self-loop）
3. 权重 arc（weight ≥ 2）
4. 初态即满足目标
5. 不同路径汇合同一标记
6. 正常终止标记（无使能变迁，但非死锁）
7. 真实死锁（无使能变迁，且无法继续）
8. 可重复增长（token 可无限增加）

### 三个独立金标

**关键约束**：金标必须在实现前冻结。

示例：
```json
[
  {
    "fixture_id": "growth_1",
    "net": "P0 → T1 → P1 → T2 → P0, P1 → T3 → P2",
    "initial": {"P0": 1, "P1": 0, "P2": 0},
    "question": "5 步内 enabled transitions?",
    "expected": ["T1", "T1→T2→T1", "..."],
    "claim_ceiling": "在此有限网和步数内的结论"
  },
  ...
]
```

### 交付物

```
pn_oracle_min/
├── oracle.py          # 4 个接口的实现
├── test_fixtures.py   # 8 个 fixture 的运行
└── goldens.json       # 3 个冻结真值
```

### 停止条件（DROP 触发）

1. Oracle 本身有原则性缺陷（e.g. 无法处理权重）且无法修 → BLOCK。
2. Oracle 正确，但用 fixture 测试时一直 UNKNOWN（上限太低） → 提高 max_depth，重跑。

---

## RP-D · Intervention Semantics

**对应问题**：Q5（Intervention Semantics，见 00_OBJECTIVES_AND_CLAIMS.md）

### 研究问题

**Runtime monitor 的阻断/重试/修复，真的在副作用前还是后发生？**

核心研究操作：RO-4（intervention consistency）

### 首件检查

对 ContrAgent 的 block/retry/repair 语义，检查：

| 干预操作 | 应该改变的状态 | 不应该改变的状态 | 检查 |
|---------|----------|----------|------|
| block(call) | audit_attempt_count ✓ | approval, resource_owner, business_success ✗ | 断言查看 business state 未变 |
| retry(call) | audit_retry_count ✓ | 同上 | ... |
| approval_update | approval 字段 ✓ | order 其他字段 ✗ | ... |

### 交付物

```
intervention_consistency_tests.py

def test_block_no_side_effect():
    before = query_business_state()
    monitor.block(bad_call)
    after = query_business_state()
    assert before == after, "阻断调用产生了副作用"
```

### 停止条件（DROP 触发）

1. Block 确实无副作用，audit log 分离清晰 → 停止。
2. 系统架构上无法做到"先检查再执行"（分布式无原子性）→ DROP，保留设计记录。

---

## RP-E · Specification Evolution

**对应问题**：Q3（Specification Adequacy）——⚠ 此映射是本注册表的推断，非 v2.0 原文明说。Q3 问"规格是否测中真正目标"，RP-E 问"规格改变后维护成本如何变化"，两者相关但不是同一问题；详见 00_OBJECTIVES_AND_CLAIMS.md

### 研究问题

**规格改变时，不同表示/监控方案的修改成本和错误模式如何变化？**

核心研究操作：RO-4（intervention consistency）+ RO-2（representation preservation）

### 首件规格变更

```
OLD: commit(order) 需要至少一次成功的 approve_return

NEW: commit(order) 需要成功的 approve_return 
     且批准的版本必须等于当前版本
```

### 任务

分别用以下两种方式实现，对比修改成本：
1. Object-aware FSM（状态机）
2. 教学 contract monitor（约束）

检查：
- 各改多少行？
- 改错的地方多吗（regression test 失败 vs 通过）？
- 诊断 bug 时，哪种表示更容易定位问题？

### 停止条件（DROP 触发）

1. 两种方式修改成本相同 → DROP "方法差异"，保留工程数据。
2. 一种方式明显更易维护，但原因是"语言简洁"而非"结构清晰" → 标注为"风格优先"，不升 novelty。

---

## 优先级与时间线

### P0（当前）：
- RP-A（Observation Sufficiency）
- RP-C（Petri Exact Oracle）

**注意力顺序建议**：RP-A、RP-C 是并行的两个 WIP 槽位（v2.0 §20），不强制先后。但若同一时段只能专注一件事，建议先攻 RP-C——它是不依赖其他探针结论的基础设施，其"状态追踪"直觉对 RP-A 的反例构造也有迁移价值。依据见 05_CROSSCHECK_GPT_ROUND2.md 第四节。

### P1（EX-05 收口后）：
- RP-B（String Diagrams 反例）
- RP-D（Intervention Consistency）
- 未见 transfer task

### P2（全部 P1 通过后）：
- RP-E（Specification Evolution）

### P3（当前不启动）：
- Compose Bridge（B4）

---

## 状态追踪

使用 01_CAPABILITY_EVIDENCE_MATRIX.tsv 追踪每个 RP 的：
- Source_Truth（一手证据状态）
- Mechanism_State（理解等级）
- Artifact_Status（产物状态）
- Research_Status（研究进展）

每完成一个 fixture 或交付物，更新对应行。
