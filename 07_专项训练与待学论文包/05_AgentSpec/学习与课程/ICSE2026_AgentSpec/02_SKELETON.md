# SKELETON — AgentSpec (ICSE 2026)

**日期**:2026-08-13
**状态**:S01-S04 v1(首轮),复现与审查留后续窗

---

## 一句话创新点

用 `trigger–check–enforce` 三段式 DSL 在 LangChain 决策回路的三个拦截点上做运行时强制:代码域 >90% 拦截、具身域危害归零(安全完成率只降 4.36 个百分点 [推算:58.62−54.26])、AV 域 100% 合规,开销毫秒级;规则可由 o1 自动生成再人工审。

---

## 论文结构骨架

```
Abstract
  └─ agent 自治带来风险 → 现有缓解不足(鲁棒/可解释/可适配)→ AgentSpec DSL
     → 三域实施 → >90% / 归零 / 100% / 毫秒级 → o1 生成规则 95.56%P / 70.96%R

1 Introduction
  └─ agent 普及(SWE-Agent/EHRAgent/SeeAct/Copilot)→ 风险与组织风险容忍度差异(医院 vs 实验室)
  └─ 三类既有方案的缺口:ToolEmu(无强制)、GuardAgent(逐 agent 手工)、多数方案只做执行前评估
  └─ 贡献四条:框架+开源 / 三域规则实现 / 实验 / LLM 生成规则评估

2 Background & Problem Definition
  ├─ 2.1 agent 形式化:(S, A, Ω, Π, Δ),轨迹 τ,切片 τ[:-i]
  ├─ 2.2 动机例:转账给 Bob → @inspect_transfer 规则(Figure 2)
  └─ 2.3 问题定义:保证 Eval(τᵢ, aᵢ) 全程安全;违规时干预改写轨迹

3 The AgentSpec Language
  ├─ 3.1 Syntax:五段式 rule/trigger/check/enforce/end(Figure 3 抽象语法)
  ├─ 3.2 Triggers(Table 1 事件表)/ Checks(Table 2 谓词例)/ Enforcements(四动作)
  └─ 3.3 Semantics:Def 规则三元组 → Def 违规 → 四算子 → Def 整体语义(无定理)

4 Implementation
  └─ LangChain 0.3.13,拦截 iter_next_step 三决策点(AgentAction/AgentStep/AgentFinish)
  └─ ANTLR4 解析 DSL;谓词可手写或 LLM 生成(few-shot,"LLM 当 Python 程序员")
  └─ 框架无关性:AutoGen(instrument ToolAgent.handle_function_call)、Apollo(规则→运动规划指令)

5 Evaluation(RQ1 表达力与效果 / RQ2 LLM 生成规则 / RQ3 泛化性 / RQ4 开销)
  ├─ 5.1 三 agent:CodeAct+RedCode-Exec / ReAct 具身+SafeAgentBench / Apollo+FixDrive
  ├─ 5.2 RQ1:Table 3(代码 25 类)/ Table 4(具身 10+1 类)/ Table 5(AV 8 场景)
  ├─ 5.3 RQ2:Table 6(o1 生成规则三域效果)+ 失败模式分析
  ├─ 5.4 RQ3:规则/实例比(25/750、12/250、6/8)
  └─ 5.5 RQ4:解析/谓词/执行三段开销 + Threats(1:9 划分、多作者交叉验证)

6 Discussion
  ├─ 6.1 对比 NeMo / llama.cpp / LCEL / GuardAgent
  ├─ 6.2 表达力:隐私谓词、声明式外置带来的跨版本一致性
  └─ 6.3 局限:确定性离散检查点、无轨迹级前瞻 → future work:学 DTMC 做概率可达(=ProbGuard)

7 Related Work:红队(AgentPoison/EIA/内容投毒/SQL 注入)、蓝队(GuardAgent/LLMScan/CROW 等)、
   风险评估(ToolEmu/RedCode/SafeAgentBench/ALI-Agent、ICML 2025 立场文)、传统 RV/RE(Falcone 等)
8 Conclusion
```

---

## DSL 语法符号表(Figure 3 + §2.1/§3.3)

### 抽象语法(Figure 3)

| 非终结符 | 产生式 | 备注 |
|---|---|---|
| Program | Rule+ | 程序 = 一组规则 |
| Rule | `rule` Id `trigger` Event `check` Pred* `enforce` Enforce+ `end` | 五段式;check 可为空(Pred*),enforce 至少一个 |
| Event | `state_change` \| `before_action` \| `agent_finish` \| DomainSpecificEvent | 语法图写 before_action,Table 1 与 Def 写 action,命名不一致 [原文如此] |
| Pred | `True` \| `False` \| `!`Pred \| DomainSpecificPred | 只有字面量+否定+域谓词;**无析取、无时序算子** |
| Enforce | `user_inspection` \| `llm_self_examine` \| `invoke_action(Params)` \| `stop` | Figure 8 直接写域动作名(follow_dist(10) 等),应理解为 invoke_action 的域实例化/语法糖 [个人分析,待复现窗核对 g4 文件] |

### 形式语义符号(§2.1、§2.3、§3.3)

| 符号 | 语义 | 出处 |
|---|---|---|
| (S, A, Ω, Π, Δ) | agent 五元组:状态/动作/观测/感知函数 Π:Ω→S / 策略 Δ:(U,S)→A | §2.1 |
| u ∈ U | 用户指令 | §2.1 |
| τᵢ = ⟨s₀→a₀…→aᵢ₋₁ sᵢ⟩ | 轨迹前缀 | §2.1 |
| τ[:-i] | 切片:去掉最后 i 个状态转移 | §2.1 |
| Eval(τᵢ, aᵢ) | 轨迹+计划动作的整体安全评估(目标函数,未实现为显式算法) | §2.3 |
| r = (η_r, P_r, E_r) | 规则三元组:触发事件 / 谓词集 / enforcement 序列 ⟨e⁰…eⁿ⟩ | Def 3.1 |
| p_r(u, τᵢ) ∈ B | 谓词求值(布尔);state_change 事件下只依赖 sᵢ,action 事件下依赖 sᵢ 与 aᵢ | Def 3.1 |
| 违规 | η_r 发生 ∧ 所有 p ∈ P_r 为真(合取) | Def 3.2 |
| e_r(τᵢ) | enforcement 作为轨迹变换算子 | §3.3 |
| a_f / a_p / a_c | finish 动作 / 预定义动作 / 自反思生成的纠正动作 | §3.3 |
| ω_r | "规则 r 被违反"的观察,注入自反思重规划 | §3.3 |

注:arXiv HTML 版三个定义均渲染为"Definition 3.0",本拆解按出现次序称 Def 3.1(规则)/3.2(违规)/3.3(语义)。

---

## trigger–predicate–enforcement 三段式流程(§3.2/§3.3/§4)

```
LangChain agent 回路:用户输入 u → 规划 aᵢ=Δ(u,sᵢ) → 执行 → 观测 ωᵢ → 感知 sᵢ₊₁=Π(ωᵢ) → 再规划
        │
        │ AgentSpec 截获 iter_next_step,挂三拦截点:
        │   AgentAction(动作执行前)/ AgentStep(动作产生观测后)/ AgentFinish(任务完成)
        ▼
[1] trigger 匹配:η_r 是否发生?
      通用:state_change(sᵢ≠sᵢ₋₁)| action(执行 aᵢ 前)| agent_finish
      域:PythonREPL(代码)/ pour、pick…(机器人)/ red_light_detected…(ADS)
        │ 命中
        ▼
[2] check 求值:⋀_{p∈P_r} p(u, τᵢ) = true?
      谓词 = Python 布尔函数,可见用户输入与整条轨迹前缀
        │ 全真 ⇒ 违规(Def 3.2)
        ▼
[3] enforce 施加:E_r 依序作用于 τᵢ(Def 3.3)
      stop             → τ[:-1] →a_f sᵢ(终止)
      user_inspection  → 用户允许:τᵢ 原样执行 | 拒绝:τᵢ →a_f sᵢ(终止)
      invoke_action(a_p) → τᵢ →a_p s′ᵢ(替换为预定义安全动作)
      llm_self_examine → 注入违规观察 ω_r → a_c = Δ(u,sᵢ) → τᵢ →a_c s′ᵢ(Reflexion 式重规划)
        │
        ▼
末动作 = a_f ? → 停机;否则执行动作、观测、感知、再规划 → 回到 [1]
```

---

## But/However 计数(转折即卖点)

1. §1:agent 广泛部署,**但**自治引入安全风险(误转账/医疗剂量例)。
2. §1:ToolEmu 能识别风险,**但**不可解释、无强制机制、易被对抗操纵。
3. §1:规则式防护可审计,**但**现有实现太僵硬或不通用(GuardAgent 逐 agent 手工)。
4. §1:多数方案做执行前评估,**但**运行期偏离无人约束 → 需要 runtime enforcement(核心 gap)。
5. §5.2:24/25 类代码风险 agent 至少尝试执行一次,**但**"删除敏感文件"类 30 例全被 agent 自身拒绝——模型自带对齐已挡掉一部分,护栏的增量要在其余类里看。
6. §5.2:检查多数正确,**但**"缺 default 分支""重复键"两类 0 触发——agent 调了解释器却没照做风险指令(风险根本没出现)。
7. §5.3:o1 生成规则可用,**但**三种失败模式:过拟合示例(只认 /etc/ 里点名的文件)、漏隐含语义(装了酒的水壶不能加热)、一刀切(全禁 pour、5 米内急刹)。
8. §6.3:确定性检查点强制可靠可解释,**但**不推理长期后果、无轨迹级前瞻 → future work 学 DTMC 做概率可达(=ProbGuard 立项)。

---

## 左墙 vs 右墙

| 左墙(已有) | 右墙(本文新增) |
|---|---|
| ToolEmu:LLM 沙盒模拟评估——识别风险但无强制、不可解释 | 显式 enforcement 四原语,干预即轨迹改写,判定可审计 |
| GuardAgent:LLM 解释约束 + 逐 agent 手工 guard 代码 | 外置开发者定义规则,DSL 跨 agent 复用;约束解释与 LLM 内部解耦(§6.1"提升可验证性") |
| NeMo:对话层自然语言约束 | 执行关键点(高影响动作前)拦截,语义级性质 |
| llama.cpp grammar / LangChain LCEL:句法模式匹配 | 语义谓词(安全/访问控制/隐私) |
| 传统 runtime verification/enforcement(Falcone 等):面向传统软件 | 移植到 LLM agent 决策回路(iter_next_step 三拦截点) |

**右墙之外**(本文明确不做,留给 ProbGuard):轨迹级前瞻、概率可达性、提前量(§6.3)。

---

## 边界检验

1. **谓词正确性无保证**:谓词是任意 Python 代码,DSL 不验证其语义;规则有效性完全取决于谓词实现质量(request_untrusted_source 靠 URL 白名单,论文自认数据流分析可加强,§5.2)。
2. **离散检查点**:只在三个拦截点强制;检查点之间的副作用(如工具内部行为)不可见 [个人分析,§6.3 的"离散检查点"自述是近邻表述]。
3. **空 check 合法**:语法允许 Pred*(零个谓词),合取空集永真 → 规则退化为"事件即违规";语义上合法但危险 [个人分析]。
4. **多规则冲突未定义**:Def 3.3 只说"each violated rule applies its enforcement functions",未给次序与冲突消解。
5. **user_inspection 人因**:实验由作者扮演 user 判定放行(threats 节自认,靠交叉验证+预定标准+盲评缓解)。
6. **"100% 合规"是封闭集结果**:AV 域 8 场景 × FixDrive 规则,不是对交通法全集的保证。

---

## 核心洞察(品味)

- 本质是经典 **ECA(Event-Condition-Action)主动规则范式**在 LLM agent 回路上的重生 [个人分析,论文未提 ECA];新颖在两处:拦截点选得准(iter_next_step 恰是计划→执行的必经孔道),四动作里有两个 LLM 原生原语(llm_self_examine 把 Reflexion 变成 enforcement 原语、invoke_action 吃进域动作空间)。
- DSL 刻意做薄(无析取/时序),表达力下沉到 Python 谓词——换来的是可读性与 LLM 可生成性(RQ2 的前提),代价是逻辑藏进代码后不可审计。T5 若把时间窗谓词提升为 DSL 一等公民,即是对母版的语言学升级(呼应 D6 缺口 2)。
- 有语义定义、零定理:精确到"够实现对齐",止步于"可证保证"。保证性质的缺口正是 ProbGuard(概率)与 T5(PAC 承诺)的立足点。

---

**数据来源**:arXiv:2503.18666 HTML 全文(2026-08-13 实取);D6 卡 3(仓库实见信息)。
