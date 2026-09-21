# JINZU_MASTER_V2 · 04_BRIDGE_LU_SUN_OPENAI

**版本**：v2.0 正式版  
**日期**：2026-09-21  
**状态**：METHOD TRANSFER / 研究接点

---

## 四个 Bridge 的统一问题

所有桥接都回答同一个核心问题（来自 00_OBJECTIVES_AND_CLAIMS）：

> **在给定可观测信息与干预能力下，什么表示足以可靠判断、验证或约束目标性质？**

四个 bridge 各自从一个维度攻击这个问题，但彼此互补、不排斥。

---

## B1 · Representation & Information Preservation

### 问题

**为了判定目标性质 φ，什么表示信息必须被保留？**

换句话说：从原系统映射到某个抽象表示后，φ 是否仍然可判定？如果不可，缺什么？

### 链条

```
EdgeIM（发现）
  ↓ 「两个发现结果相同吗？」
String Diagrams（trace 等价 vs partial-order 等价 vs signature 等价）
  ↓ 「什么表示对目标性质足够？」
抽象选择（什么维度必须保留，什么可以投影掉）
  ↓ 「学习最优的抽象」
ReGA（表示学习，鲁侧方向）
```

### 核心差异

| 系统 | 问题 | 答案形式 |
|------|------|---------|
| **EdgeIM** | 这两个发现的过程模型在外观上一样吗？ | YES / NO（具体）|
| **String Diagrams** | "一样"取决于我们保留什么信息；对于不同的等价概念，有不同的判据。 | 一个决策框架 |
| **ReGA** | 给定目标性质，自动找出最少必要的表示维度。 | 最优抽象 + 保留维度的证明 |

### 三种信息访问模式

监控系统时，我们可以观测到：

1. **Process events**（序列化的事件流）：a 然后 b 然后 c。
   - 能区分：顺序依赖、因果关系。
   - 不能区分：真正的并发 vs 快速序列化。

2. **Typed objects**（带身份的对象及其交互）：订单 A 的属性、资源 R 的所有者。
   - 能区分：对象恒等性、属性变化。
   - 不能区分：对象间的异步通信延迟。

3. **Hidden-state representations**（系统内部态、中间推理步骤）：算法变量、内部状态机。
   - 能区分：最细粒度的因果链。
   - 不能区分：外部依赖关系、环境约束。

**关键约束**：这三种模式彼此不互相推导。
- 从 process events 无法完全重建 object states（可能有消息丢失）。
- 从 typed objects 无法完全推导 hidden states（可能有内部操作不外泄）。

→ 一个关于 representation 的 bridge 结论，必须在所有三种模式下都成立。

### 本轮产物

**semantic_discrimination_matrix.tsv**（在 03 中已定义）

行：
- Trace language（完整序列集）
- Partial order（去掉序列化后的因果）
- Contexts / Selection awareness（环境可能的分支点）
- Typed relations（带对象恒等的关系）
- Signature（按 String Diagrams 定义）
- Downstream property preservation（目标性质是否还能判定）

列：
- 区分并发与选择？
- 区分对象恒等性？
- 对环境选择敏感？
- 能保证目标性质 φ？
- 最小冗余吗？

**两个手工反例**：
1. "同 trace 不同并发" → String Diagrams (RP-B)
2. "表示改变后 φ 不再成立" → 为未来的 ReGA 预留

### 接入 EdgeIM 的方式

不改变 EdgeIM 的发现算法，而是补一个"发现结果的事后审计"：

```
def audit_edgeim_discovery(model1, model2):
  """
  EdgeIM 发现了 model1 和 model2 看起来相同。
  我们现在问：它们的 signature 相等吗？
  如果不相等但 trace 相等，说明什么？
  """
  
  if signature(model1) == signature(model2):
    # String Diagrams 定理保证 trace 也相等
    assert trace_language(model1) == trace_language(model2)
  elif trace_language(model1) == trace_language(model2):
    # trace 相等但 signature 不等
    # 说明 EdgeIM 的发现算法隐含了某个 projection
    print(f"EdgeIM 投影掉了: {signature_diff(model1, model2)}")
```

### 与鲁侧的接点

**鲁侧 2026 明确方向**：ReGA（自动学习抽象）。

当我们完成了 B1 的"什么表示对什么性质必要"的矩阵时，就能判断：
- ReGA 学到的抽象维度是否覆盖了 EdgeIM/SBPN 的全部必要信息？
- 反过来，SBPN 的并发结构信息中有多少是 ReGA 的学习目标实际不需要的（可以安全投影掉）？

这是一个**互为验证**的关系，不是"ReGA 更好"或"String Diagrams 更强"。

### 停止条件 / CONTINUE 条件（含 DROP 触发）

**DROP**：
- 简单 trace 集、偏序、类型关系已完全区分，signature 无新信息 → 放弃论文，记录为"矩阵已饱和"。
- 论文假设（selection 单调性、connected 图、起止边界）在例上不成立 → DROP，保存反例。

**CONTINUE**：
- 反例构造正确，矩阵分析有意义（区分了两种性质或两种系统） → 继续到 RP-D（intervention semantics）进行迁移。

---

## B2 · Exact Reasoning & Verification

### 问题

**最终答案正确是否足够？怎样定位**第一个**错误推理步骤？**

换句话说：一个 checker 说"网络无死锁"时，我们怎样验证不是这个 checker 本身有 bug？

### 链条

```
PetriBench（六个任务的精确定义）
  ↓ 「构造独立于 LLM 的 oracle」
精确 oracle（TINA solver 或手工验证）
  ↓ 「独立反例与 baseline」
错误分类（不只 pass/fail，而是错在哪）
  ↓ 「step-wise 诊断」
MATP（step-wise verification：推理的每一步对吗？）
  ↓ 「代码级推理诊断」
FM-Agent（formal methods on agent reasoning）
```

### 核心差异

| 系统 | 问题 | 答案形式 |
|------|------|---------|
| **PetriBench** | 模型的最终答案对吗？ | CORRECT / INCORRECT |
| **精确 oracle** | 怎样独立生成这个答案，不依赖任何智能系统？ | 算法 + 证明 |
| **MATP** | 模型在推理的哪一步失败了？ | Step trace + error location |
| **FM-Agent** | Agent 执行代码时，哪步决策打破了程序的不变性？ | Invariant violation + cause |

### 三种关键假设

这些假设彼此独立，不能互推：

1. **Specification 正确**
   - 我声称的"性质 φ"是真的需求吗？
   - 例：deadlock-free 对 workflow 真的是必需吗？还是我们应该允许某种死锁？
   - 检查：给定一个不同的规格 φ'，oracle 答案会怎样变？

2. **Oracle 可信**
   - 我的"正确答案"是真的吗？
   - 例：TINA solver 说可达，但会不会有 bug？
   - 检查：金标在实现前冻结；独立手工验证；mutation test。

3. **Measurement 有效**
   - 我测的是真的目标对象吗？
   - 例：我在 Petri 网上验证的结论，对实际 workflow 也成立吗？
   - 检查：benchmark 的假设与真实系统的差距。

→ **答案对不代表推理对；推理对不代表性质对；性质对不代表工程上可行。**

### 本轮产物

**exact_oracle_eval_protocol.md**

包含：
1. 输入规格：一个有限时域任务（如"5 步内可达 P2"）+ 一个无限时域任务（如"boundedness"）。
2. Oracle 生成：不由 LLM，而是 TINA 或手工检查。
3. 错误分类：
   - Token error（标记理解错）
   - Transition error（变迁语义理解错）
   - Reachability error（无法正确遍历状态空间）
   - Liveness error（无限性质判定错）
4. 验收标准：3 个 gold-truth cases 独立于实现生成；mutation kills ≥ 3 个语义 bug。

**两个对比基线**

1. **Stateless rule**（最弱）：
   ```
   if marking has X tokens in place P then conclusion Z
   ```
   - 优点：简单、可解释。
   - 缺点：无法推理因果、无法处理循环。

2. **Object-aware FSM**（中等）：
   - 追踪订单版本、资源所有者等对象属性。
   - 对比 ContrAgent 的 DFA。

3. **ContrAgent monitor**（待接入 B3）：
   - 运行时约束检查。

**"Checker 可信吗"的审计清单**

- [ ] enabled(t, m) 的定义与标准 PN 定义一致？
- [ ] fire(t, m) 的 token 加减逻辑正确？
- [ ] canonical(m) 的 deduplication 无遗漏？
- [ ] BFS 的剪枝条件合理（不过度剪枝）？
- [ ] Gold standards 覆盖了哪 8 个 fixture 类？
- [ ] 金标生成过程可重现？

### 接入 PetriBench 的方式

PetriBench 本身有官方 oracle（TINA solver）。我们不复现它，而是：

1. 挑两个最小例（一个有限、一个无限），手工验证 oracle 结果。
2. 列出 oracle 的假设清单（closed-form marking、无时间、无随机化）。
3. 问：**如果打破某个假设，哪个任务首先无法判定？**

例如：
- 假设"每个 place 的 token 数有界"被打破 → boundedness task 变 UNKNOWN。
- 假设"转移是原子的"被打破 → reachability 可能有新路径。

### 与孙侧的接点

**孙侧 2026 明确方向**：MATP（step-wise verification on Formal Methods）。

当我们做了 PetriBench 的 oracle 审计后，可以问：
- MATP 对"代码推理的每一步"的分析，与"Petri 网变迁"的分析有什么相同与不同？
- 一个"推理步骤失败"的 MATP 反例，在 Petri 网上对应什么类型的错误？（都是因果链破裂吗？）
- 能否统一 "step-wise correctness" 的概念，适用于代码、形式化、workflow 多种情景？

### 停止条件 / CONTINUE 条件（含 DROP 触发）

**DROP**：
- Oracle 本身有原则性缺陷（e.g., 无法处理权重弧）且无法修复 → 不用 PetriBench，转用更简单的模型。
- 8 个 fixture 都通过，但所有通过都是"初态即满足目标"类型 → 金标覆盖不足。

**CONTINUE**：
- Oracle 正确，fixture 覆盖全面 → 继续到 B4（组合语义）。

---

## B3 · Runtime Assurance & Monitorability

### 问题

**Monitor 看见什么、什么时候看见、能采取什么干预？这三者怎样协调一致？**

换句话说：阻断一个调用真的阻止了副作用吗？如果系统异步，monitor 怎样保证决策有效？

### 链条

```
ContrAgent（离线评分 ≈ 在线阻断，用同一个 DFA）
  ↓ 「审计 monitor 看到了什么」
可观测合约（什么字段被 monitor 看见，什么隐藏）
  ↓ 「构造观测不足反例」
信息不足反例（两条轨迹观测相同但真值不同）
  ↓ 「增加 intervention 的考量」
Runtime verification（在线干预会改变什么，不改变什么）
  ↓ 「扩展到分布式」
MAS monitoring（多 agent 系统：谁看见什么？）
  ↓ 「扩展到部分可观测」
OpenAI monitorability（部分可观测 + 长轨迹 + hidden reasoning）
```

### 核心差异

| 系统 | 问题 | 答案形式 |
|------|------|---------|
| **ContrAgent** | DFA 能根据看见的字段挡攻击吗？ | DFA state + verdict |
| **Runtime verification** | 在线干预（block/retry/repair）会改变什么状态？ | 干预前后状态对比 |
| **MAS monitoring** | 多 agent 各看一部分时怎样判定全局性质？ | 分布式一致性协议 |
| **OpenAI monitorability** | 部分可观测下，哪些性质可判定，哪些不可？ | 可判定性的刻画 |

### 三层独立的假设

1. **观测完整**
   - Monitor 没有看不见的状态转移。
   - 例：所有批准调用都被 monitor 看见；没有"后门"批准路径。
   - 检查：我能枚举所有改变业务状态的操作吗？

2. **因果可追**
   - 一次调用的发起与它的返回一定能配对（不会混淆）。
   - 例：request_id 能唯一标识一次 approve_return 调用。
   - 检查：两条并发调用的返回会不会乱序？

3. **干预一致**
   - Block 调用真的阻止了副作用（先检查再执行，不是执行后撤销）。
   - 例：monitor.block(call) 意味着这个调用根本不会发生，不只是"记了 log"。
   - 检查：系统架构上能否做到"先检查再执行"？

→ **这三个都不是"合约正确"足以保证的。**

### 本轮产物

**observation_insufficiency_matrix.tsv**

行：
- Call 类型与参数（approve_request, approve_return 的 order_id, version 等）
- 返回值（success, error_code）
- 环境假设（系统初态、其他 agent 的并发操作）
- 资源状态（order 的版本、resource 的所有者）
- 时序顺序（调用的因果先后、乱序的可能性）

列：
- 各字段单独丢失时，是否存在"同观测异真值"反例？
- 若存在，首个反例是什么？

**观测不足反例**

```json
{
  "property": "commit(A) 安全 ⟺ 批准的是 A",
  "counterexample": [
    {
      "history": [
        "approve_return(order_id=A, version=0, request_id=r1, success=true)",
        "commit(A)"
      ],
      "observation": "success=true, request_id=r1, version=0",
      "truth": "ALLOW"
    },
    {
      "history": [
        "approve_return(order_id=B, version=0, request_id=r1, success=true)",
        "commit(A)"
      ],
      "observation": "success=true, request_id=r1, version=0",
      "truth": "BLOCK"
    }
  ],
  "critical_missing": "order_id 在 approve_return 中"
}
```

**ContrAgent vs FSM 对比**

在相同信息下：
- ContrAgent DFA 和对象感知的 FSM 是否等价？
- 若等价，那么"ContrAgent 的优势"不在表达力，而在什么（可组合性？可扩展性？）？
- 若不等价，差异来自什么（假设不同 vs 实现不同）？

### 接入 ContrAgent 的方式

ContrAgent 论文假设 monitor 能看见所有工具调用/返回。我们不改这个假设，而是：

1. 给定相同可见信息，哪些不同的底层场景（真实发生的事件）会导致 monitor 的同一个 verdict？
2. 如果性质改了（如"批准必须和当前版本绑定"），信息不足的表现如何变化？
3. 如果阻断一个调用，真的阻止了副作用吗？系统架构上的保证是什么？

### 与孙侧的接点

**孙侧 2026 明确方向**：MAS corruption monitoring（多 agent 系统中的污染追踪）。

当我们搞清了"什么信息足以判定"后，可以问：
- 在多 agent 系统中，每个 agent 只看自己的操作，足以保证全局性质吗？
- 需要什么额外的**通信**与**同步**来建立全局一致性？
- 污染（一个 agent 被攻破）怎样在系统中传播，monitor 怎样检测？

### 与 OpenAI 的接点

**OpenAI 明确研究 trajectory monitorability**。我们的观测不足反例直接应用：

- Action + output 总是可观测的；hidden reasoning 不可观测。
- 某个安全性质能仅从 action+output 判定吗？
- 若不能，需要什么额外信息（如思维过程的摘要、中间目标的声明）？
- 部分可观测下的监控**成本**是多少（通信 / 推理 / 存储）？

### 停止条件 / CONTINUE 条件（含 DROP 触发）

**DROP**：
- 系统架构上无法做到"先检查再执行"（分布式无原子性）→ DROP，保存设计记录为"不可能的需求"。
- 所有观测字段都加上后冲突消失，且修改 FSM 成本很低 → 停止，记录为"工程解"，不升 novelty。

**CONTINUE**：
- 观测不足确实存在，修复需要架构改进 → 继续到 RP-D（intervention consistency）。

---

## B4 · Composition & Multi-agent (Future)

### 问题

**局部的正确性证明怎样组合成系统级的保证？**

换句话说：如果我能保证单个 agent 的每个决策都对，那系统整体就对吗？多个 agent 交互时呢？

### 链条（暂不在本轮关键路径上）

```
对象与事件的因果关系（来自 B1: String Diagrams）
  ↓
MAS communication graph（谁与谁通信）
  ↓
Corruption propagation（孙侧 2026）
  ↓
Compositional semantics（局部 property 怎样组合成全局 property）
  ↓
OpenAI long-horizon trajectory（多步决策下的一致性）
```

### 本轮的角色

当 B1/B2/B3 各有初步结论时，B4 才能问：

- **String Diagrams (B1)** 提供"对象与事件的因果关系"的形式语言。
  - 两个 agent 的 trace 如何组合？
  - 全局的偏序怎样从局部偏序重构？

- **ContrAgent (B3)** 的 monitor 可以跨 agent 部署。
  - 每个 agent 都有自己的 DFA。
  - 全局属性怎样用分布式 DFA 表达？

- **PetriBench (B2)** 的 oracle 可以扩展到并发系统。
  - Petri 网本身就支持并发。
  - 多 agent 系统的 composition 怎样用 Petri 网模型化？

### 本轮产物

**空**（预留）。准备工作由 B1/B2/B3 完成后启动。

### 与孙侧 / OpenAI 的接点

**孙侧**：B4 与 MAS corruption monitoring 直接关联。

**OpenAI**：B4 涉及长轨迹的全局性质验证。

---

## B5 · Formal Agent Bridge（三合一 Toy，已立项）

**来源**：05_CROSSCHECK_GPT_ROUND2.md 第三节记录的 GPT 讨论提出过一个"B1 Formal Agent Bridge"概念（三篇论文合成一个可运行 agent toy）；该编号与本文件已有的 B1（EdgeIM→String Diagrams→ReGA）冲突，当时被明确拒绝直接采用，留给用户决定是否用新编号立项。**2026-09-21 用户已拍板立项**，编号定为 **B5**，不复用 B1–B4 任何现有编号。

### 问题

**把 String Diagrams 的表示、PetriBench 的状态空间推理、ContrAgent 的时序合约监控，组合进同一个可运行的 tool-using agent toy 之后，三者的结论是否还各自成立，组合处会不会出现任何单篇论文都不会暴露的新失败模式？**

这不是"三篇论文的加法"，而是专门去找**组合边界**——B1≠B3、B2≠B1、B3≠B2 这三条关键约束（见上文"概览：四个 Bridge 的交叉依赖"）各自成立，不代表把三者接在一条流水线上时接口处依然成立。

### 链条

```
process / Petri representation（String Diagrams，B1 产物）
        ↓
formal trace / state（PetriBench，B2 产物）
        ↓
temporal policy（ContrAgent 的合约定义）
        ↓
runtime monitor（ContrAgent 的 DFA，B3 产物）
        ↓
tool-using agent（组合运行环境）
```

### 前置条件（硬性，不是建议）

**B5 不允许在 B1/B2/B3 各自达到 P2 交付物之前启动**：

- B1（RP-B）：`semantic_discrimination_matrix` 完成。
- B2（RP-C）：`oracle.py` + 8 fixtures + 3 goldens 完成。
- B3（RP-A）：`observation_conflict_witness` + FSM baseline 完成。

理由与 B4 相同（见上文"本轮的角色"一节）：在任何一个分支的独立结论还没站住之前组合三者，无法判断组合失败是"组合本身的问题"还是"某个分支本来就没做完"。**在前置条件满足之前，B5 只能是一个占位的问题陈述，不能开始构造 toy、不能声称任何组合结论。**

### 本轮产物

**空**（预留，与 B4 相同的写法）。准备工作由 B1/B2/B3 完成后启动。

### 与 B4 的关系——两者都是"组合"，但方向不同

B4（Composition & Multi-agent）问的是"多个 agent 之间局部证据如何组合成全局判断"——横向组合，跨 agent。

B5 问的是"单个 agent 内部，三种不同 formal operator（表示/推理/监控）叠加使用时是否互相干扰"——纵向组合，跨 operator，单 agent。

两者不是同一个问题，不能合并；B5 的结论如果稳定，会是 B4 的一个前置构件（B4 需要先假设"单 agent 内部三层已经协调好"，才能问"多 agent 之间怎样组合"）。

### 停止条件（DROP 触发）

1. 三个分支独立看都成立，组合后也没有新失败模式（三者接口处的信息传递无损耗）→ 收为"组合本身是安全的"这一具体、有边界的结论，不能扩大宣称"formal agent stack 已验证"。
2. 组合后暴露的"新失败模式"经排查后发现只是某个分支本身没做完（例如 B2 的 oracle 还有 bug）→ 退回对应分支修复，不算 B5 的独立发现。

### CONTINUE 条件

三个分支的接口处确实存在无法用任何单分支结论解释的信息损耗或语义冲突，且可以复现 → 这才是 B5 真正贡献的东西，进入 novelty 讨论前仍需先过 00_OBJECTIVES_AND_CLAIMS.md 的 Novelty Gate（12 项条件）。

---

## 概览：四个 Bridge 的交叉依赖

| Bridge | 源 | 数据流依赖 | 被依赖 | 本轮状态 | 对应 RP | 里程碑 |
|--------|----|---------|---------|---------|----|--------|
| **B1** | EdgeIM | 无 | B2/B3/B4/B5 | P1/P2 | RP-B | semantic_discrimination_matrix |
| **B2** | PetriBench | 无 | B3/B4/B5 | P1/P2 | RP-C | oracle.py + 8 fixtures + 3 goldens |
| **B3** | ContrAgent | B1(可选) + B2(可选) | B4/B5 | P1/P2 | RP-A | observation_conflict_witness + FSM |
| **B4** | 合成 | B1/B2/B3 全部 | 无 | 空 | 无 | 无 |
| **B5** | 合成（三篇原生，非 B4 的横向合成） | B1/B2/B3 全部达到 P2 | 无 | 空／已立项，等待前置条件 | RP-A+B+C | 三合一 tool-using agent toy |

**关键约束**（来自设计，不是巧合）：

- **B1 ≠ B3**：表示相等（signature 相等 ⇒ trace 相等）不代表监控可行（可观测足够）。
  - String Diagrams 的等价在抽象层；ContrAgent 的观测在运行时。
  
- **B2 ≠ B1**：Oracle 正确不代表表示就正确。
  - 一个 bug-free oracle 仍然测的是基于某个特定表示（Petri 网）的结论。
  
- **B3 ≠ B2**：能监控不代表能计算。
  - Monitor 可以实时阻断，但遥难计算一个系统的所有可达状态。

→ **这四个 bridge 是平行发展的、各自独立的研究线，不是"串行"的学习路径。**

任何一个 bridge 的结论对其他 bridge 的工作没有前置要求。

---

## 与鲁侧、孙侧、OpenAI 的接点总结

| 团队 | 明确研究方向 | 接点 | 我们的贡献 |
|------|-----------|------|---------|
| **鲁侧** | ReGA（表示学习） | B1（什么表示对什么性质必要） | 提供矩阵与反例验证 ReGA 学到的抽象 |
| **孙侧** | MATP（步级验证） + MAS corruption | B2（oracle 审计） + B3（分布式观测） | 提供 oracle 的可信性界 + 观测不足反例 |
| **OpenAI** | Trajectory monitorability | B3（可观测足够性） + B2（长轨迹评价） | 提供部分可观测下的监控成本分析 |

---

## 下一步（执行计划）

1. **确认 B1–B4 的框架**是否抓住了你想要的接点。
   - 若有遗漏或需要调整，反馈后修改。

2. **三篇论文 P0–P2 的执行**（并行）。
   - 每篇论文独立交付反例 / 矩阵 / 代码。
   - 01 矩阵逐行填充（Mechanism_State 升级到 E2 或更高）。

3. **四个 bridge 的初步接口形成**（串行）。
   - B1（semantic_discrimination_matrix）完成后启动 RP-D / RP-B 后续。
   - B2（oracle + 8 fixtures）完成后启动 B3 的对比基线。
   - B3（observation_conflict_witness）完成后启动向 MAS/OpenAI 的转接洽谈。

4. **EX-05 的 transfer hook**（持续）。
   - 每周用新学到的概念重新解释 EX-05 的例。
   - 记录"从 RP-A/B/C 反馈回 EX-05 的洞察"。

达到上述，从"我在学 Formal Methods"进入"我能独立 formulate 一个 formal monitoring/verification problem"。
