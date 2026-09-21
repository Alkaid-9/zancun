# JINZU_MASTER_V2 · 03_PAPER_TO_CAPABILITY_PIPELINE

**版本**：v2.0 正式版
**日期**：2026-09-21
**状态**：PAPER-CAPABILITY MAPPING / 进组入口

---

## 三篇论文的共同架构

每篇论文统一走 **P0–P5** 六阶段（原样对齐 v2.0 §9，不再压缩为四段）：

| 阶段 | 名称 | 回答的问题 | 产物 | 检查点 |
|------|------|-----------|------|--------|
| **P0** | SOURCE | 作者是谁？到底声称什么？条件是什么？artifact 在哪里？哪部分没核？ | `identity_manifest` + `claim_ledger` + `source_locator` | 论文你真的理解了吗？ |
| **P1** | MECHANISM | 去掉域名词后，机制的 Input/State/Transition/Output/Assumption/Invariant/Failure Mode 是什么？ | `mechanism_sheet` | 能独立描述机制、能用一个最小例手推吗？ |
| **P2** | FALSIFICATION | 最强反例、最强简单 baseline、矛盾案例、信息不足、语义不匹配、负结果，主动找到了吗？ | 反例 / 最简单 baseline 的失败证据 | 没有反例设计，不算深拆完成 |
| **P3** | EXECUTABLE | 有没有至少一个非作者自证的可运行 artifact？ | 代码 + 完整复现记录（input/independent_expected/command/cwd/environment/input_hash/exit_code/stdout/stderr/output_hash） | 能独立运行、独立复现吗？ |
| **P4** | TRANSFER | 换一个未见过的变体，本人能不能独立预测、修改、解释？ | unseen variant → prediction → modification → run → explanation → delayed retest | 能迁移吗，还是只会背这一个例子？ |
| **P5** | RESEARCH | 这个问题在最近邻、强竞争方法、开源实现、矛盾证据、负结果、工业实践、失败复盘面前，还剩下什么？ | nearest-neighbor 检索记录 + 可证伪的 novelty claim | 才允许进入 novelty 讨论——且必须先通过 00_OBJECTIVES_AND_CLAIMS.md 的 **Novelty Gate**（12 项条件） |

**本轮范围**：三篇论文本轮要完成 **P0–P2**；力争把 P3 至少跑通一个最小可运行 artifact；**P4、P5 明确不在本轮范围内**——不是"暂不强求"这么松散的说法，而是本轮连尝试都不做，等 P0–P3 三篇论文都扎实之后再排期。P5 尤其不能提前做，因为它必须先满足 00 文档 Novelty Gate 的 12 项条件，本轮任何一篇论文都还没有 strong baseline、independent oracle、nearest neighbor 检索这些前置项。

---

## 论文 1：String Diagrams

### 出发问题

Given two process notations (traces, partial orders, process signatures, etc.), **when are they semantically equivalent?**

### P0 · SOURCE

**`identity_manifest`**（待核实——本轮未从原始 PDF/arXiv 页面逐项核对，以下为占位模板，正式使用前必须补全真实值。**本论文不在 06_HANDOFF_LUNA_VERIFICATION.md 的派发范围内，authors/page_count 仍待补**，不要与下方 ContrAgent/PetriBench 两篇的已核实状态混淆）：

| 字段 | 值 |
|------|-----|
| paper_id | 待填 |
| filename | 待填 |
| title | String Diagrams for Process Mining（暂用工作标题，需核对论文正式标题） |
| authors | 待填 |
| version | 待填 |
| hash | 待填 |
| page_count | 待填 |

**`claim_ledger`**：

**主张**：
- String diagrams 可以统一表示并发程序的多种等价概念。
- 两个图的等价性可以通过"graph rewriting"的观点检查。
- Signature 是一种特定的"selection-based"等价，不同于 trace language 或 partial order。

**来源**：论文 §2–3（定义）+ §4–5（定理）

**关键假设**（= 条件）：
- 每个 node / edge 都 labeled（有名字）。
- Graph 是 acyclic 或按照特定模式循环。
- "Selection" 是单调的（环境的选择不会随后悔）。

**边界（本轮不支持的）**：
- Timed systems（时序）。
- Probabilistic（随机）。
- Infinite processes（直到 RP-D 后）。

**`source_locator`**（待核实）：

| 字段 | 值 |
|------|-----|
| paper_url | 待填（arXiv/发布页链接） |
| artifact_url | 待填（若作者公开了代码/数据，填仓库链接；若无公开 artifact，明确写"无公开实现"） |
| unverified_claims | 三条主张均未独立复现验证；"selection 单调性"假设是否在真实并发系统中普遍成立，未核 |
| access_date | 待填 |

### P1 · MECHANISM

**Input**：
- A process (sequential, parallel, or choice)
- A property to check (trace language, partial order, selection awareness, etc.)

**State**：
- current_marking（各 place 的 token 数，或者 process tree 的 reduction state）
- pending_events（还没执行的事件）

**Transition**：
```
fire(event) ::=
  if event is enabled in current_marking
    then remove precondition tokens, add postcondition tokens
  else FAIL
```

**Output**：
- Canonical marking form (用于去重)
- Full trace set (所有可能的执行序列)
- Partial-order set (去掉序列化后的因果结构)
- Signature (根据论文定义，通常是selection-based)

**Assumption**：
- Events 不重名（distinct IDs）。
- 无时间约束。
- 无随机化（deterministic environment）。

**Invariant**：
- 每条从初始到末端的路径都是合法的。
- signature(x) = signature(y) ⇒ trace_language(x) = trace_language(y)。

**Failure Mode**：
- 如果两个过程的 signature 相同但 trace 不同 → 你的"等价性"定义有问题。
- 如果 signature 不同但你想要它们"等价" → 你的目标性质不在 selection 层。

### P2 · FALSIFICATION

**v2.0 §9 对 P2 的要求**：主动寻找 strongest counterexample / strongest simple baseline / contradictory case / information insufficiency / semantic mismatch / negative result。以下反例覆盖其中的 **contradictory case** 与 **semantic mismatch** 两项；**strongest simple baseline** 这一项本轮尚未做（"更简单的表示是否已经够用"这个问题留给 P3 的矩阵去回答，但矩阵本身不是一次主动的 baseline 攻击尝试，这是一个已知缺口，未来轮次应该补一个"只用 trace language 能不能解决这个反例"的显式失败演示）。

**要求**：构造两个过程，使得：
- 完整 trace 集相同：L₁ = L₂
- 但 signature 不同：sig(P₁) ≠ sig(P₂)

**示例**（已给出）：
```
P₁ = a ; (b || c) ; d
P₂ = choice( a;b;c;d, a;c;b;d )
```

**分析方式**：
1. 列举所有可能的完整 trace（从 init 到 terminal marking）。
2. 对每个 trace，标记其中的 choice point（环境必须做出的决策）。
3. 注意：P₁ 中 b 和 c 可能真正并发；P₂ 中 b 和 c 互斥。

**你要产出的**：
```markdown
## P₁ vs P₂ 分析

**P₁: a ; (b || c) ; d**

- Initial: [a_pending]
- After a: [b_pending, c_pending] (both can fire independently)
- Choice points: (b 先 vs c 先) 由**环境**决定
- Possible traces: {abcd, acbd}
- Partial order: a→{b,c}; b,c→d (b,c concurrent)
- Signature: ...（按论文公式计算）

**P₂: choice( a;b;c;d, a;c;b;d )**

- Initial: [choice_point]
- Environment picks: either "b first" OR "c first" (互斥)
- Possible traces: {abcd, acbd}
- Partial order: a→(b XOR c); (b XOR c)→d (b,c 互斥)
- Signature: ...（按论文公式计算）

**结论**：
- Trace language ✓ 相同：{abcd, acbd}
- Partial order ✗ 不同：并发 vs 互斥
- Signature ✗ 不同（如果定义保留因果约束的话）
```

**`semantic_discrimination_matrix.tsv`**（把上面的反例结构化，同时是 P2 的产物、也是 P3 要被机械化复核的对象）：

| 维度 | P₁ | P₂ | 结论 |
|------|----|----|------|
| Event set | {a,b,c,d} | {a,b,c,d} | ✓ 相同 |
| Trace language | {abcd, acbd} | {abcd, acbd} | ✓ 相同 |
| Causal order | a→b,c; b,c→d (无约束) | a→{b XOR c}; {b XOR c}→d (互斥) | ✗ 不同 |
| Concurrency | (b \|\| c) in both traces | (b XOR c) in both traces | ✗ 不同 |
| Selection awareness | Selection varies per trace | Selection per scenario, then replay | ✗ 不同 |
| Signature (per paper def) | ? | ? | ✗ 不同 |

### P3 · EXECUTABLE

**目标**：把 P2 手工推导的矩阵结论，变成一段可独立重跑、机械验证的代码——而不是永远只停留在"我手算过一次"。

**最小 artifact**：`signature_diff_checker.py`——输入 P₁、P₂ 的过程描述，按论文定义计算各自 signature，输出是否相等，并与手算矩阵的结论比对。

**必须记录的复现字段**（v2.0 §9 P3 的强制 schema，本轮尚未运行，以下为待填模板）：

| 字段 | 说明 | 状态 |
|------|------|------|
| input | P₁、P₂ 的形式化描述（如上） | 已定义（在 P2 中） |
| independent_expected | 手算矩阵给出的"Signature 不同"结论 | 已定义（P2 的矩阵） |
| command | 待填（如 `python signature_diff_checker.py`） | 未运行 |
| cwd | 待填 | 未运行 |
| environment | 待填（Python 版本等） | 未运行 |
| input_hash | 待填 | 未运行 |
| exit_code | 待填 | 未运行 |
| stdout | 待填 | 未运行 |
| stderr | 待填 | 未运行 |
| output_hash | 待填 | 未运行 |

**接入 EdgeIM 的方式**（04_BRIDGE_LU_SUN_OPENAI.md 中 `audit_edgeim_discovery()` 的最小版本，可直接作为这个 artifact 的骨架）：不改发现算法，补一个"事后审计"——比较 signature 相等 vs trace 相等的含义。

### P4 · TRANSFER（本轮不做，仅记录未来的第一个未见变体长什么样）

**unseen variant 草案**：一个第三过程 P₃，既不是论文原例也不是 P₁/P₂，例如引入第三个并发分支或嵌套 choice。本人在**看到 P₃ 之前**先预测它的 trace 集/偏序/signature 关系，再用 P3 的脚本验证预测，再解释预测错在哪（如果错的话）。

**当前状态**：未构造 P₃，未做预测，未跑验证。本节只是占位，防止将来跳过"预注册预测"直接看答案。

### P5 · RESEARCH（本轮不做）

需要先查 nearest neighbor / strongest competing approach / open-source implementation / contradictory evidence / negative result / industrial practice / failure postmortem，并给出可证伪的 novelty claim——这些一项都还没做。在此之前，即使 P2–P4 全部做完，这个探针也只能标记为 `MECHANISM_ASSET` 或 `RESEARCH_PROBE`，不能自称 novelty（见 00_OBJECTIVES_AND_CLAIMS.md 的 Novelty Gate）。

### 本轮目标

达到 **RP-B 的 P0–P2 交付物**，力争 P3：
- `claim_ledger` + `identity_manifest`（占位待补） + `source_locator`（占位待补）
- `one_concurrency_vs_choice_counterexample.md`（上述矩阵与分析）
- `semantic_discrimination_matrix.tsv`（完整填充）
- 能脱稿解释两个过程的区别。
- 力争：`signature_diff_checker.py` 至少跑通一次，产出完整复现记录。
- **明确不做**：P4 unseen variant、P5 nearest-neighbor 检索。

---

## 论文 2：ContrAgent

### 出发问题

Given a monitor that enforces a contract during execution, **can we prove the monitor makes decisions based only on observed information, and doesn't hide side effects?**

### P0 · SOURCE

**`identity_manifest`**（authors/page_count 已核实——Luna，2026-09-21，见 06_HANDOFF_LUNA_VERIFICATION.md 顺带任务；其余字段仍待补）：

| 字段 | 值 |
|------|-----|
| paper_id | 待填 |
| filename | 待填 |
| title | Symbolic Temporal Supervision of LLM Agents Using Contracts（暂用工作标题，需核对正式标题） |
| authors | Yifeng Xiao, Pierluigi Nuzzo（已核实，PDF p.1） |
| version | 待填 |
| hash | 待填（SHA-256 已在 07 文件冻结，见 06 交接文档第二节；此处 identity_manifest 的 hash 字段仍留待补，与冻结值保持一致） |
| page_count | 13（已核实） |

**`claim_ledger`**：

**主张**：
- Runtime monitor 可以用 DFA 表示（离线评分规则 = 在线阻断规则）。
- Monitor 的"observe–block–log" 分离是可审计的。
- 相同观测下，不同的底层事件可能导致不同的真值（observation sufficiency gap）。

**来源**：论文 §3–4（定义）+ §5–6（评估）

**关键假设**（= 条件）：
- 所有工具调用和返回都被 monitor 看见。
- Monitor 决策本身是 side-effect-free（只 log，不改 business state）。
- "批准"是一个原子操作（approve_return 完成或完全回滚）。

**边界（本轮不支持的）**：
- 分布式系统中的部分可观测（只支持单 agent 或同步 MAS）。
- ALTLf 的完整语义（只用教学规范子集）。
- NL→formula 的自动翻译（手工编写）。

**`source_locator`**（待核实）：

| 字段 | 值 |
|------|-----|
| paper_url | 待填 |
| artifact_url | 待填（若无公开实现，明确写"无公开实现"） |
| unverified_claims | "DFA 离线评分=在线阻断"的等价性未独立验证；"所有工具调用都被 monitor 看见"这一假设在真实部署中是否成立，未核 |
| access_date | 待填 |

### P1 · MECHANISM

**Input**：
- A sequence of events: `[event₁, event₂, ..., eventₙ]`
- Each event: `{type: "call" | "return" | "effect", ...fields...}`
- A DFA specification: `transitions(state, observed_event) → new_state`

**State**：
- dfa_state（当前监控态）
- audit_log（记录的所有观测）
- monitor_verdict（ALLOW / BLOCK / UNCERTAIN）

**Transition**：
```
process_event(e) ::=
  observed = project(e, observable_fields)
  new_dfa_state = dfa_transition(current_state, observed)
  if is_blocking_state(new_dfa_state)
    then audit_log.append(BLOCK_DECISION)
         return BLOCK
  else
    audit_log.append(ALLOW_DECISION)
    return ALLOW
```

**Output**：
- Verdict sequence：每个事件的决策。
- Audit log：所有观测和决策。
- Claim ceiling：当前观测足以保证什么？

**Assumption**：
- Observable 字段的定义是正确的（没有遗漏关键字段）。
- DFA 本身是正确的（根据规格）。
- 底层系统确实执行了 monitor 的决策（阻断调用不会有副作用）。

**Invariant**：
- Monitor 的决策只取决于已观测的信息。
- Monitor 的日志记录不改变业务状态。

**Failure Mode**：
- 两条历史的观测相同，但真值不同 → observable 字段不足。
- Monitor 的决策改变了业务状态 → 阻断操作有副作用。
- 规格改变后，monitor 的修改成本很高 → 表示不够灵活。

**Predicate 词表**（已核实——Luna，2026-09-21，对照论文原文 Appendix A Table 4，见 06_HANDOFF_LUNA_VERIFICATION.md 核对任务 B；05_CROSSCHECK_GPT_ROUND2.md §5.2 记录完整核实过程）：

论文定义的 interaction predicate（Def. 3，p.3）共 **22 项**，不是最初二手转述给出的 10 项。已核实精确语义（arity 与 GPT 转述一致）的 10 项：

| 谓词 | 语义 |
|------|------|
| `Call(T)` | 工具 T 被调用 |
| `ArgHas(T,f,p)` | T 的参数字段 f 匹配模式 p |
| `OutHas(T,p)` | T 的结果匹配模式 p |
| `Match(f,k)` | 参数字段 f 等于上下文值 k |
| `Flow(s,d)` | 数据从 source s 到达 sink d |
| `Perm(P)` | 调用者持有权限 P |
| `Cnt(T)` | T 的当前调用次数 |
| `Tok` | 累计消耗的 tokens（无显式参数） |
| `Depth` | agent delegation depth（无显式参数） |
| `Num(T,f)` | 参数字段 f 的数值 |

另有 12 项仅确认**存在于 Table 4**、语义未逐一核实（本轮核对任务范围只覆盖前 10 项，这 12 项的名称本身就是本次核实的新发现，不在原派发问题清单内，故标 UNKNOWN 语义，只记录存在性）：`Path、Subset、Said、In、Ctx、Has、Run、Len、InLen、Words、Chars、Since`。其中 `Since(e)` 论文表注特别说明是实现层的时间扩展，不进入 Def. 1 的形式模型——这一点是唯一附带核实到语义的第 11 项。

**层次关系**（已从假设升级为核实确认）：这套谓词与本文件下方"事件分解"`proposal/accepted_call/return/effect/END` 是不同层，不冲突。Def. 1（p.2）把事件定义为工具调用 `a=(tool,args)` 和返回 `a′=(tool,result)`；Def. 3（p.3）的谓词是对 session state/事件/参数求值的确定性布尔函数，逐事件评估，再组装成 ALTLf 合约。谓词层描述"用什么原子条件构造合约"，事件层描述"能观测到什么事件类型"——两者互补。

**使用限制**：写具体教学 contract monitor subset 时，只能使用上述已核实语义的 10+1 项；若需要用到另外 11 个仅确认存在的谓词，必须先补做语义核实，不能凭名称猜测参数或行为。

### P2 · FALSIFICATION

**v2.0 §9 对 P2 的要求**：以下反例直接就是 **information insufficiency** 这一项（RO-1 的标准形式：α(h1,x1)=α(h2,x2) 但 q(h1,x1)≠q(h2,x2)）。**strongest simple baseline** 这一项由 P3 的 FSM baseline 承担——构造 baseline 本身不是"证明它会赢"，而是主动测试"这个最简单的表示，在这个反例上到底够不够"，所以 FSM baseline 同时也是本阶段"寻找最强简单 baseline"的落地，不是重复劳动。

**要求**：构造两段历史 h₁、h₂，使得：
- α(h₁) = α(h₂)（观测相同）
- φ(h₁) ≠ φ(h₂)（真值不同，以目标性质 φ 判定）

**目标性质 φ**：
```
commit(order_A) 合法 ⟺
  存在一次成功的 approve_return 调用
  且调用的对象是 order_A
  且调用后 order_A 的版本未改变
```

**示例**（简化版）：

```
h₁:
  approve_return(order_id=A, version=0, request_id=r1, success=true)
  → commit(A)

  真值：ALLOW（因为批准的确实是 A）

h₂:
  approve_return(order_id=B, version=0, request_id=r1, success=true)
  → commit(A)

  真值：BLOCK（因为批准的是 B，不是 A）

观测相同（都看到 success=true, request_id=r1, version=0）
缺失字段：approve_return 中的 order_id
```

**你要产出的**：
```json
{
  "observation_conflict": {
    "h1": {
      "trace": ["approve_return(...order_id=A...)", "commit(A)"],
      "observation": ["success=true", "request_id=r1", "version=0"],
      "truth": "ALLOW"
    },
    "h2": {
      "trace": ["approve_return(...order_id=B...)", "commit(A)"],
      "observation": ["success=true", "request_id=r1", "version=0"],
      "truth": "BLOCK"
    }
  },
  "critical_missing_field": "order_id (在 approve_return 中)",
  "fix": "增加 approve_return 的 order_id 字段到 observable 集合"
}
```

### P3 · EXECUTABLE

**最小 artifact**：`explicit_fsm_monitor.py`——object-aware FSM baseline，实现一个简单的对象感知 monitor：

```python
class OrderApprovalMonitor:
    def __init__(self):
        self.approved_orders = {}  # order_id -> (version, request_id)
        self.blocked = set()

    def on_approve_return(self, order_id, version, request_id, success):
        if success:
            self.approved_orders[order_id] = (version, request_id)

    def on_commit(self, order_id):
        if order_id not in self.approved_orders:
            return BLOCK  # 无批准记录

        stored_version, stored_rid = self.approved_orders[order_id]
        current_version = get_order_version(order_id)

        if stored_version == current_version:
            return ALLOW
        else:
            return BLOCK  # 版本已改变
```

**这段代码同时回答两个问题**：
1. （P2 的延伸）加上 order_id 观测后，FSM 是否完全解决了 h₁/h₂ 冲突？—— 若是，按 v2.0 §13 规则，DROP"必须用更强形式体系（如完整 ALTLf）才能判定"这一具体主张，只保留 FSM 作为 strong baseline。
2. （P3 本身）这段代码能不能被独立跑通、独立验证？

**必须记录的复现字段**（本轮尚未运行，以下为待填模板）：

| 字段 | 说明 | 状态 |
|------|------|------|
| input | h₁、h₂ 两条历史的事件序列 | 已定义（在 P2 中） |
| independent_expected | h₁→ALLOW, h₂→BLOCK（P2 定义的真值） | 已定义 |
| command | 待填 | 未运行 |
| cwd | 待填 | 未运行 |
| environment | 待填 | 未运行 |
| input_hash | 待填 | 未运行 |
| exit_code | 待填 | 未运行 |
| stdout | 待填 | 未运行 |
| stderr | 待填 | 未运行 |
| output_hash | 待填 | 未运行 |

### P4 · TRANSFER（本轮不做，仅记录未来的第一个未见变体长什么样）

**unseen variant 草案**：把"订单批准"换成一个未见过的业务规则（例如库存预留的多步退款场景），本人独立构造一对新的 h₁'/h₂' 冲突历史，预测 FSM baseline 能否直接复用、需要改哪里，再实际修改代码验证。

**当前状态**：未选定新场景，未做预测，未做修改。本节只是占位。

### P5 · RESEARCH（本轮不做）

同上（见 String Diagrams 的 P5 说明）——nearest neighbor、prior art、negative result 检索均未开始，本探针在通过 00 的 Novelty Gate 之前只能算 `TRAINING` 或 `RESEARCH_PROBE`。

### 本轮目标

达到 **RP-A 的 P0–P2 交付物**，力争 P3：
- `claim_ledger` + `identity_manifest`（占位待补） + `source_locator`（占位待补）
- `observation_conflict_witness.json`（上述反例）
- 能脱稿解释什么观测足以、什么不足。
- 力争：`explicit_fsm_monitor.py`（working baseline）跑通一次，产出完整复现记录。
- **明确不做**：P4 unseen variant、P5 nearest-neighbor 检索。

---

## 论文 3：PetriBench

### 出发问题

**How can we evaluate LLM reasoning on Petri net problems without trusting the LLM's answer?**

关键约束：需要一个独立于 LLM 的 oracle。

### P0 · SOURCE

**`identity_manifest`**（authors/page_count 已核实——Luna，2026-09-21，见 06_HANDOFF_LUNA_VERIFICATION.md 顺带任务；其余字段仍待补）：

| 字段 | 值 |
|------|-----|
| paper_id | 待填 |
| filename | 待填 |
| title | PetriBench（暂用工作标题，需核对正式标题） |
| authors | Pyrros Koussios, Benjamin Jäger, John Hua Yao, Ajay Sridhar, Violet Xiang, Chenhao Li（已核实，PDF p.1） |
| version | 待填 |
| hash | 待填（SHA-256 已在 07 文件冻结，见 06 交接文档第二节；此处 identity_manifest 的 hash 字段仍留待补，与冻结值保持一致） |
| page_count | 33（已核实） |

**`claim_ledger`**：

**主张**：
- Petri 网的六个标准任务（reachability, liveness, deadlock, boundedness, etc.）有精确的、可自动验证的答案。
- 我们可以用 TINA solver 或手工检查生成真值。
- LLM 的答案可以按"错在哪一步"分类，不只是 pass/fail。

**来源**：论文 §2–3（任务定义）+ §4–5（oracle）

**关键假设**（= 条件）：
- Petri 网是"低级"的系统模型（无时间、无概率、无无限行为外的量化）。
- Oracle 实现的 enabled/fire/marking 与标准 PN 定义一致。
- 我们能在有限步内判定某些性质（有界性可能需要无限搜索，但我们可以 cap）。

**边界（本轮不支持的）**：
- Colored Petri 网（只支持普通 PN）。
- 时间约束（timed PN）。
- Probability（stochastic PN）。
- 无限性质的完全判定（只支持有限 BFS + 推理）。

**`source_locator`**（待核实）：

| 字段 | 值 |
|------|-----|
| paper_url | 待填 |
| artifact_url | 待填（若作者公开了 TINA solver 对接代码/数据集，填链接） |
| unverified_claims | TINA solver 本身的正确性未独立核实（我们把它当作参照，但没有验证它没有 bug）；"六个任务覆盖了所有实用场景"这一隐含主张未核 |
| access_date | 待填 |

### P1 · MECHANISM

**Input**：
- A Petri net: `{places, transitions, pre, post, initial_marking}`
- A query: `{type: "reachability" | "liveness" | "deadlock" | ..., target_marking | target_transition}`

**State**：
- current_marking：当前的 place token 分布。
- visited_markings：已探索过的标记集（用于死锁检测和无限性质判定）。
- enabled_transitions：当前可触发的变迁集。

**Transition**：
```
fire(transition) ::=
  if all preconditions satisfied in current_marking:
    for each input arc (place, t):
      current_marking[place] -= weight
    for each output arc (t, place):
      current_marking[place] += weight
    return new_marking
  else:
    return ERROR
```

**Output**：
- Answer: `REACHABLE | UNREACHABLE | LIVE | DEAD | BOUNDED | ...`
- Witness: 一条从初始到目标的变迁序列（若存在）。
- Proof sketch: 简单说明（e.g., "visited 10 states, no deadlock found in BFS depth 5"）。

**Assumption**：
- Network 是 closed 的（没有外部输入）。
- Initial marking 是明确的。
- Queries 一次一个（没有并发查询）。

**Invariant**：
- 任何可达标记都是从初始标记通过合法变迁序列得到的。
- 若无变迁使能，那就是死锁（或终止）。

**Failure Mode**：
- Oracle 说"可达"但实际上我手工推导不出那个路径 → oracle 有 bug。
- Oracle 说"有界"但没有给出上界 → claim 不完整。
- Oracle 在有限步内返回 UNKNOWN，但我们其实能判定 → search depth 太小。

**任务分类法（2×2 taxonomy）**（已核实——Luna，2026-09-21，对照论文原文 §3.1/Fig.2/Table 14，见 06_HANDOFF_LUNA_VERIFICATION.md 核对任务 A；05_CROSSCHECK_GPT_ROUND2.md §5.1 记录完整核实过程）：

| | Finite horizon | Infinite horizon |
|---|---|---|
| **Local** | Minimum Token Steps | L0 / L4 Liveness |
| **Global** | Reachable Markings | Deadlock / Boundedness |

这个 2×2（scope: local/global × temporal extent: finite/infinite）结构与六个任务的映射关系已核实与原文一致（Fig. 2 分类图，Table 14 完整分布，p.29）。用来充实上方 Input 部分"A query: {type: reachability | liveness | deadlock | ...}"这个扁平描述，区分"这道题需要深度搜索还是广度枚举、有限步还是需要 invariant 推理"。

**必须一并写明的澄清**（否则会误读）：论文 §3.1（p.3）特别说明 "local" 指**被查询属性的范围**，不代表求解过程本身是局部的——例如 L4 liveness 的判定仍可能需要分析整个状态空间。"local" 不等于"更简单"。

**必须保留的限制**（核实后仍不成立/未定，不能因为大部分对上了就整体照单全收）：
- 本仓 07/08 文件"六个标准任务"的"标准"一词**不是论文自称**——论文原文（§3.1, p.4）明确声明这是自己提出的任务集，不主张覆盖所有有意义的 Petri 网性质或推理问题，是刻意的紧凑近似。今后表述这六个任务时，只能说"本仓选定分析的六个任务"，不能说"论文认定的标准任务"。
- livelock 或其他未被这张表覆盖的任务是否存在于原文，核实后仍是 **UNKNOWN**（Luna 检索 PDF 可提取文本未检出，但不能排除图像/公式区域漏检）——不能声称"只有这四类/六个任务"是穷尽的。

**PCA 发现**（已核实，含修正）：第一主成分解释力三档均确认存在于 Table 2（p.6）：**Easy=91.7%，Medium=87.3%，Hard=78.9%**——原转述只给了 Easy/Hard 两端，遗漏了 Medium 档，引用时必须三档一起给出，否则会把一个单调渐变过程误读成两点对比。衡量对象是"第一主成分解释的、task-level model performance 的方差"，即跨模型表现画像共享轴的解释力，不是单个模型单题的分数方差。原文结论句（p.6）："harder PetriBench instances increasingly differentiate models in ways that are not captured by overall performance alone, with task-specific variation becoming more pronounced as structural difficulty increases despite a strong shared component of model capability"——转述"model-specific reasoning profile 开始分化"是意译，不是原句，如需引用应优先用原文英文句。

**使用限制**：这些是 03/04 文件当前唯一被批准写入正文的、来自二手转述且经过独立核实的内容（对应 05 文件 §5.1 的裁定）；PCA 数字仅作背景参考，不改变 00/03/04 已有的"本轮不测 LLM leaderboard"立场（见上方 P5 说明）。

### P2 · FALSIFICATION

**v2.0 §9 对 P2 的要求**：这里主动构造的是 **strongest simple baseline**——一个比完整 oracle 简单得多、看起来"够用"的规则，然后主动证明它在某个 fixture 上失败。这不是拖延，而是回答"为什么真的需要一个完整的 enabled/fire/canonical/bounded_bfs 实现，而不是一条简单规则"。

**最弱 baseline**（取自 04_BRIDGE_LU_SUN_OPENAI.md 的 B2 定义）：
```
if marking has X tokens in place P then conclusion Z
```
——不追踪变迁历史，不做状态搜索，只看"某个 place 现在有没有 token"就下结论。

**要求**：挑一个 8 类 fixture 中的具体例子（建议用 growth / 可重复增长这一类），证明这条 stateless rule 在这个例子上给出错误结论。

**示例分析**（草案，尚待实际编号验证）：
```
net: P0 --T1--> P1 --T2--> P0, P1 --T3--> P2
initial: {P0: 1, P1: 0, P2: 0}

stateless rule 判断 "P2 是否可达 1 个 token"：
  若规则只检查 "P1 当前是否有 token" → 初始时 P1=0，规则会说 UNREACHABLE
  但实际上：fire(T1) → {P0:0, P1:1} → fire(T3) → {P0:0, P1:0, P2:1}
  真实结论：REACHABLE（只需两步）

stateless rule 因为不追踪"经过 T1 之后 P1 会变化"，得出错误结论。
```

**你要产出的**：一份 `stateless_baseline_failure.md`，明确记录：这条最简单规则错在哪个 fixture、错误的具体表现（假阴性还是假阳性）、为什么完整 oracle（追踪 marking 而不是快照）能避免这个错误。

### P3 · EXECUTABLE

**`pn_oracle_min/` 三件套**：

```python
class PetriNetOracle:
    def __init__(self, net: PetriNet):
        self.net = net

    def enabled(self, marking: dict, transition: str) -> bool:
        """Check if a transition can fire in this marking."""
        pre = self.net.pre.get(transition, {})
        return all(marking.get(place, 0) >= weight
                   for place, weight in pre.items())

    def fire(self, marking: dict, transition: str) -> dict:
        """Fire a transition and return new marking."""
        if not self.enabled(marking, transition):
            raise ValueError(f"{transition} not enabled")

        new_marking = marking.copy()
        for place, weight in self.net.pre.get(transition, {}).items():
            new_marking[place] = new_marking.get(place, 0) - weight
        for place, weight in self.net.post.get(transition, {}).items():
            new_marking[place] = new_marking.get(place, 0) + weight
        return new_marking

    def canonical(self, marking: dict) -> str:
        """Canonical form for deduplication."""
        return str(sorted(marking.items()))

    def bounded_bfs(self, max_depth: int = 20) -> BfsResult:
        """BFS with depth limit."""
        visited, queue = set(), [(self.net.initial, 0, [])]
        max_tokens = 0

        while queue and queue[0][1] <= max_depth:
            marking, depth, path = queue.pop(0)
            canon = self.canonical(marking)

            if canon in visited:
                continue
            visited.add(canon)
            max_tokens = max(max_tokens, sum(marking.values()))

            for t in self.net.transitions:
                if self.enabled(marking, t):
                    new_marking = self.fire(marking, t)
                    queue.append((new_marking, depth+1, path+[t]))

        return BfsResult(visited_count=len(visited),
                        max_depth_reached=max_depth,
                        bounded_up_to=max_tokens)
```

**八类对抗 fixture**：

1. **multi-input**：多个 place 连向一个 transition，需要全部有 token。
2. **self-loop**：transition 的 input 和 output 有交集。
3. **weight ≥ 2**：arc 权重 > 1。
4. **initial-satisfied**：初态就满足目标（reachability 问题）。
5. **path-merge**：不同路径汇合同一标记。
6. **normal-end**：无使能变迁但非死锁（最后一个 place 有 token，没有出度）。
7. **deadlock**：无出路的真实死锁。
8. **growth**：token 可无限增加（unbounded）。

**三个独立金标**（在实现前冻结）：

```json
[
  {
    "fixture_id": "growth_unbounded",
    "net_description": "P0 --T1--> P1 --T2--> P0, P1 --T3--> P2",
    "initial_marking": {"P0": 1, "P1": 0, "P2": 0},
    "queries": [
      {"type": "reachability", "target": {"P0": 1, "P1": 2}},
      {"type": "bounded", "target": "infinite"}
    ],
    "expected_answers": [
      "REACHABLE (via T1, T2, T1 sequence)",
      "UNBOUNDED"
    ],
    "claim_ceiling": "在此有限网和配置下，结论有效"
  }
]
```

> **与 02_RESEARCH_PROBE_REGISTRY.md 的 growth fixture 对照说明**：02 文件 RP-C 章节给出的同一个网结构（`P0 → T1 → P1 → T2 → P0, P1 → T3 → P2`）配了另一个查询——"5 步内 enabled transitions?"。两处不是互相矛盾的"同一个例子写错了两次"，而是**两个独立的 fixture 用例，共享同一个网拓扑**：02 的版本是 RP-C 研究问题下的一个简化教学示例（问"哪些变迁可用"），03 这里是 P3 EXECUTABLE 阶段要求"三个独立金标在实现前冻结"的完整可达性+有界性判定实例。两者的 `initial_marking` 已统一写成显式的 `{"P0":1,"P1":0,"P2":0}` 三键形式，避免因为"隐式 0"造成误读；但查询类型本身允许不同，不需要强行合并成一条。

### P4 · TRANSFER（本轮不做，仅记录未来的第一个未见变体长什么样）

**unseen variant 草案**：一个第 9 类 fixture——例如带有两个独立 growth 循环、彼此不连通的网。本人在跑 oracle 之前先预测 boundedness 判定结果，再运行验证，再解释预测错在哪（如果错的话）。

**当前状态**：未构造第 9 类 fixture，未做预测，未做验证。本节只是占位。

### P5 · RESEARCH（本轮不做）

同上（见 String Diagrams 的 P5 说明）——本轮明确"不测 LLM leaderboard"，先验证 oracle 自身可信，nearest-neighbor（如与 TINA 之外的其他 PN 验证工具对比）检索完全没开始。

### 本轮目标

达到 **RP-C 的 P0–P2 交付物**，力争 P3：
- `claim_ledger` + `identity_manifest`（占位待补） + `source_locator`（占位待补）
- `stateless_baseline_failure.md`（最弱 baseline 的失败证据）
- 力争：`pn_oracle_min/oracle.py`（working implementation）+ `test_fixtures.py`（8 fixtures 通过）+ `goldens.json`（3 independent truths）
- 能脱稿解释 enabled/fire/bounded 的定义和边界。
- **明确不做**：P4 第 9 类 fixture、P5 nearest-neighbor 检索、LLM leaderboard 测试。

---

## 三篇论文的进组时间表

| 论文 | P0 SOURCE | P1 MECHANISM | P2 FALSIFICATION | P3 EXECUTABLE | P4 TRANSFER | P5 RESEARCH | 里程碑 |
|------|-----------|---------------|-------------------|----------------|--------------|--------------|--------|
| String Diagrams | 当周（identity_manifest/source_locator 待补） | 当周 | 当周（反例已定义；strongest-simple-baseline 攻击待补） | 力争当周（signature_diff_checker.py 未运行） | 不在本轮范围 | 不在本轮范围 | semantic_discrimination_matrix 完成 |
| ContrAgent | 当周（identity_manifest/source_locator 待补） | 当周 | 当周（反例已定义） | 力争当周（explicit_fsm_monitor.py 未运行） | 不在本轮范围 | 不在本轮范围 | observation_conflict_witness + FSM 完成 |
| PetriBench | 当周（identity_manifest/source_locator 待补） | 当周 | 当周（stateless baseline 失败证据待补） | 力争当周（oracle.py 未运行；金标已冻结） | 不在本轮范围 | 不在本轮范围 | oracle.py 通过 8 fixtures + 3 goldens |

**关键约束**：
- P2 的交付物（反例 + 最弱 baseline 失败证据）必须是你本人独立产出的，不是复制论文。
- 金标在实现前冻结（防止"按答案改金标"）。
- 每篇论文的产物必须都能独立讲解。
- P4/P5 一旦被提前做出"结果"，先检查是不是违反了"没有先跑 P0–P3 就抢跳"这条纪律——按 v2.0 的顺序要求，跳阶段本身就是一种需要 REVISE 的信号。

---

## 进组验收检查表

当三篇论文都达到 **P0–P2、力争 P3** 时，检查：

- [ ] String Diagrams：能脱稿解释"trace 相同但并发结构不同"的反例。
- [ ] ContrAgent：能脱稿解释"观测相同但真值不同"的反例和缺失字段。
- [ ] PetriBench：能脱稿解释最弱 baseline 错在哪、oracle 为什么需要追踪完整 marking。
- [ ] （力争）三篇论文各自的 P3 artifact 都至少跑通一次，有完整复现记录。
- [ ] 01 矩阵：五个 RP 各自的 Source_Truth / Mechanism_State 至少达到 E2。
- [ ] 02 注册表：五个 RP 各自有"交付物"和"停止条件"的具体记录。
- [ ] 03 管道（本文件）：能把每篇论文映射到一个 RP + Bridge，且能说清楚当前卡在 P0–P5 的哪一段。
- [ ] 04 桥接：四个 Bridge 各自有初步的"进一步研究"方向。

**这份检查表只覆盖到 P3。** 达到上述八项，**允许进组**，但**不等于**任何一个 RP 已经是 research candidate——那需要单独满足 00_OBJECTIVES_AND_CLAIMS.md 的 **Novelty Gate**（12 项条件全部满足），且必须先做完 P4 TRANSFER 与 P5 RESEARCH。进组验收和 Novelty Gate 是两道独立的门，不能用前者替代后者。
