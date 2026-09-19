# SKELETON — ProbGuard(ASE 2026)

**日期**:2026-08-13
**来源**:arXiv:2508.00500 HTML 全文(2026-08-13 实见,公式齐全)

---

## 一句话创新点

从执行轨迹学符号状态 DTMC(valid-transition-aware Laplace 平滑 + PAC 停机条件),运行时查 P_safe = P[AG ¬unsafe | s_i] 并在低于 θ 时提前干预,把 agent 运行时防护从"反应式拦截"改成"概率预测"。

---

## 论文结构骨架

```
Abstract
  └─ 反应式监控无长时程预见力 → 学 DTMC 做概率风险预测 → AV 提前 38.66s / 具身 -65.37% unsafe 保 80.4% 完成率

1. Introduction
  └─ LLM agent 自主性带来安全风险("agent 即软件")
  └─ AgentSpec/GuardAgent/ShieldAgent 反应式,缺时间前瞻
  └─ 三贡献:proactive 概率监控框架 / 两域实证 / LangChain 开源实现

2. Background and Problem Definition
  ├─ 2.1 LLM Agents:随机转移系统,轨迹 τ = ⟨v0 →a1 v1 →a2 ...⟩
  ├─ 2.2 动机例:炉灶开着离开厨房 >10min —— 风险随时间累积,反应式看不见
  └─ 2.3 三挑战:①形式规范 ②带统计保证的概率建模 ③高效估计 P[ψ|π] 并定干预时机

3. Proactive Runtime Monitoring Framework(方法核心)
  ├─ 3.1 性质规范:CTL(Def 3.1)→ 核心不变式 ψ = AG ¬unsafe
  │      ψ 是状态公式 → P[ψ] 不良定 → 附着到路径公式:ψ = A ψ^π, ψ^π = G ¬unsafe
  │      P[ψ|s] ≜ Pr^s_M{ρ ∈ Paths(s) | ρ ⊨ ψ^π} = PCTL 查询 P=?[ψ^π]
  ├─ 3.2 行为建模
  │   ├─ 3.2.1 谓词抽象:s_P(v) = (⟦φ1⟧(v),...,⟦φn⟧(v)) ∈ {0,1}^n;valid_tran(si,sj) 剪语义非法转移
  │   ├─ 3.2.2 DTMC 定义(Def 3.2);Figure 2 stove 例(s0→s1 = 31/184 = 16.85%)
  │   └─ 3.2.3 学习:Eq(1) valid-aware Laplace(α=1)→ Algorithm 1(采样-抽象-计数-平滑-PAC 检查循环)
  │          Def 3.3 (ε,δ)-PAC-correct → Bazille Thm 6 逐状态样本界(δ'=δ/|S|)
  │          Theorem 3.4:Algorithm 1 是 PAC-correct(证明在 App A)
  │          ⚠ 强持久域 B(P̂)≈10⁷⁻⁸ → 退频率估计(Bazille Thm 3,只保运行时可达性质)
  └─ 3.3 运行时监控:Algorithm 2(P_safe < θ → halt/steer;θ 是 P_safe 下界,越大越严)

4. Implementing ProbGuard
  └─ LangChain 集成 + PRISM 模型检查;干预 = prompt 附加三字段风险 alert(纯 advisory,不改控制流)
  └─ AV:嵌入 Apollo 感知-规划桥,每控制周期(100ms)提取符号状态
  └─ 域适配三件套:抽象函数 + valid_tran + CTL 性质;具身/AV 各约 200/250 行 Python

5. Application Domain: Autonomous Vehicles
  ├─ 5.1 STL_LB 片段 G(φs ⇒ F[0,K] φt)(Def 5.1)→ K 步倒计时监控自动机(Def 5.2,Q={idle,wait(0..K),viol})
  │      → 与 DTMC 同步积 M' → 归约为 AG ¬viol;Example 5.3(绿灯起步,K=100 周期=10s)
  └─ 5.2 评估:四法规(Law38_2 K=100 / Law51_5 K=2 / Law53 K=200 / NoCollision 纯不变式)
      ├─ RQ1:AWT = t_fail − t_pred(Eq 3);Table 1:最长 38.66s@θ=0.7;100% 检出
      │       FP 标定(6 安全场景):θ=0.3→0%,0.5→75%,0.7→100%
      ├─ RQ2:vs REDriver(STL 定量鲁棒度)——量纲不可通约,σ 阈值难定;ProbGuard 概率天然归一
      └─ RQ3:开销 100.79±16.96 ms(同步积后略增)
  ⚠ Apollo 不是 LLM agent(NN+规则)——作者明说这是 policy-agnostic 的演示

6. Application Domain: Embodied Agents
  ├─ 6.1 示例:ψ = AG ¬(stove_on ∧ ¬agent_in_kitchen ∧ elapsed≥T);P_ψ 三谓词;运行例 P_safe=0.86<θ=0.9 触发
  └─ 6.2 评估:SafeAgentBench + LangChain ReAct + gpt-4o-mini(temp=0),30 traces/任务
      ├─ RQ1:Table 2 Pareto —— None 40.63%/59.38%;stop@0.9 2.60%/10.42%;reflect@0.9 14.07%/47.74%
      ├─ RQ2:vs AgentSpec —— token -12.05%;声称"CTL 规范自动构造 vs 手工规则"
      └─ RQ3:未缓存推理 430ms/决策 → 缓存查表后 8 状态 13ms / 16 状态 28ms / 32 状态 <50ms

7. Discussion
  ├─ PAC in practice(ε=0.1, δ=0.05):Thm 3 频率估计 185–1016 traces;
  │   Table 3:具身 |S|=3–33, B=1.0–481, 需 530–10⁵;AV |S|=4–34, B=10⁷–10⁸(Laplace 下不可行)
  │   结构解释:具身=前向推进良混合;AV=强持久(自环>99.9%,状态间转移<10⁻⁵)
  ├─ Threats:①Markov 假设/抽象误设(PAC 不覆盖)②采样随机性 ③30 traces << 认证界
  └─ Future:主动学习/在线更新、谓词发现、更丰富 PCTL、NL→规范管线;谓词空间增长是可扩展性瓶颈

8. Related Work:Agent Safety(AgentSpec/ShieldAgent/GuardAgent/AgentDAM/LMQL/safe-RL shielding)
                + Runtime Verification(RVSE/adaptive RV/conformal RV/PSTMonitor/MDP monitors)
                差异:前人假设预定义概率模型或手工性质;本文从轨迹学模型
9. Conclusion
Appendix A:Theorem 3.4 证明(三步:逐状态集中+union bound → Thm 5 敏感度传播 → 合成)
```

---

## 核心符号表

| 符号 | 语义 | 来源 |
|------|------|------|
| V, Var, A | 具体状态集(agent+环境变量赋值)/ 变量集 / 动作集 | §2.1 |
| τ = ⟨v0 →a1 v1 ...⟩ | 具体执行轨迹,动作由隐式随机策略(条件于交互历史)选出 | §2.1 |
| ψ = AG ¬unsafe | CTL 安全不变式(核心形态) | §3.1 |
| ψ^π = G ¬unsafe | ψ = A ψ^π 中的路径公式,概率附着于此 | §3.1 |
| P[ψ\|s] | 从状态 s 出发路径满足 ψ^π 的测度 = PCTL P=?[ψ^π] | §3.1 |
| P = {φ1..φn} | 布尔谓词集;⟦φi⟧: V→{0,1} | §3.2.1 |
| s_P(v) ∈ {0,1}^n | 谓词抽象状态(真值向量) | §3.2.1 |
| S ⊆ {0,1}^n | 可采纳抽象状态空间(剪掉语义矛盾组合) | §3.2.1 |
| valid_tran(si,sj) | 语义合法转移谓词(物理不可逆性 → 吸收态) | §3.2.1 |
| M = (S_M, P_M) | DTMC;行随机:Σ_s' P_M(s'\|s)=1 | Def 3.2 |
| n^Π_ij / n^Π_i | 轨迹集 Π 中 si→sj 转移计数 / si 访问计数(=Σ_j n_ij) | §3.2.3 |
| k_i | si 的合法出边数(valid_tran 计数) | §3.2.3 |
| α | 平滑常数,=1 | Eq (1) |
| P̂^α_Π(sj\|si) | valid-aware Laplace 估计 | Eq (1) |
| (ε,δ)-PAC-correct | Pr(\|P_M̂(ψ^π)−P_M(ψ^π)\|≤ε) ≥ 1−δ,Pr 对采样过程 | Def 3.3 |
| B(P̂_Π) | 条件数:局部转移误差→全局可达概率误差的放大系数(精确定义在 Bazille,未展开) | §3.2.3 |
| δ' = δ/\|S\|,ε' = ε/B | union bound 分摊 / 局部精度目标 | App A |
| θ | 干预阈值 = P_safe 的下界;越大越严格 | Alg 2 |
| P_safe = P[ψ\|s_i] | 运行时安全概率(缓存查表) | §3.3 |
| STL_LB | G(φs ⇒ F[0,K] φt) 有界响应片段 | Def 5.1 |
| (Q, q0, δ) | 监控自动机,Q = {idle} ∪ {wait(i)}_{i=0..K} ∪ {viol}(viol 吸收) | Def 5.2 |
| M' = M ⊗ monitor | 同步积 DTMC;有界响应归约为 AG ¬viol | §5.1 |
| AWT = t_fail − t_pred | 提前预警时间;t_pred = P_safe 首次跌破 θ 的时刻 | Eq (3) |
| stop / reflect | 干预模式:终止 / 风险 alert 注入 prompt 再规划 | §6.2 |

---

## 方法流程图(文字版)

```
【离线:模型构造】
 域专家 ──写──> CTL 性质 ψ(= AG ¬unsafe) + valid_tran 谓词
   │
   ├─ Alg 1 L4:从 ψ 提取原子谓词集 P_ψ = {φ1..φn};抽象空间 S ⊆ {0,1}^n(剪矛盾组合)
   ├─ Alg 1 L5-13 循环:
   │    采样 trace v0→...→vm(默认均匀输入分布)
   │    → 抽象成符号 trace π = s_P(v0),...,s_P(vm)
   │    → 累计 n_ij;n_i = Σ_j n_ij
   │    → Eq(1):P̂(sj|si) = (n_ij+α)/(n_i+k_i·α) 若 valid_tran,否则 0
   ├─ Alg 1 L14:PACBoundSatisfied(S,Π,ε,δ)?(逐状态检查 Bazille Thm 6 样本界,δ'=δ/|S|)
   │    不满足 → 继续采样;满足 → 输出 M̂
   │    [强持久域:B 爆炸 → 改频率估计,只保单条可达性质(Thm 3)]
   │
   ├─ [AV 附加] STL 法规 G(φs⇒F[0,K]φt) ──Def 5.2──> K 步倒计时监控自动机
   │    ──同步积──> M' = M̂ ⊗ monitor;性质归约为 AG ¬viol
   └─ [缓存] 对每个符号状态 s 预计算 P[ψ|s](PRISM P=?[G ¬unsafe])→ 查找表

【在线:运行时监控(Alg 2)】
 每决策步:
   观测 v_i ──谓词抽象──> s_i(AV:再更新 q_{i+1}=δ(q_i, L(s_{i+1})),用积状态 (s_i,q_i))
   → P_safe = 查表[s_i](O(1),32 状态 <50ms)
   → P_safe ≥ θ:放行
   → P_safe < θ:干预
       stop:终止执行(强制,完成率代价大)
       reflect:prompt 注入三字段 alert(违反的规则/当前符号状态/违规转移及概率),
               agent 自行修订计划(advisory,不改控制流)
```

---

## 左墙右墙(适用边界)

### 左墙(至少要有这些,方法才成立)

1. **可反复采样的执行环境**:离线要采 30+ 条 trace(认证要数百到 10⁵);真实高危域采不到失败轨迹就学不出 unsafe 邻域的动力学。
2. **域专家给出布尔谓词化的 unsafe 定义**:瞬时、从具体状态可判定、可从 ψ 机械提取;还要一并给出 valid_tran(域不变量)。
3. **具体状态可观测**:policy-agnostic(不需要模型白盒、不读权重/logits),但环境状态变量必须暴露给插桩层。
4. **谓词抽象后近似 Markov**:未来只依赖当前符号状态。谓词从 ψ 派生是为此服务的启发式,不是保证。
5. **性质形态受限**:AG ¬unsafe 不变式,或可经监控自动机归约的 K 有界响应;更丰富的 PCTL 是 future work。
6. **抽象状态数小**(实验 3–34):缓存表、PRISM 求解、样本界的 |S| 因子都靠它;谓词数 n 增长 → 2^n 爆炸是自认瓶颈。
7. **DTMC 中存在安全吸收结构**(04_DERIVATION 发现 #1):没有安全 BSCC 则 P_safe≡0,任意 θ>0 恒报警。

### 右墙(超过这些,方法退化或失效)

1. **强行为持久域**(自环 >99.9%,如 AV):B(P̂)≈10⁷–10⁸ → 均匀 PAC 界样本天文 → 只能退频率估计,保证降档为"单条运行时可达性质"。
2. **历史依赖行为**:Markov 破坏 → 转移概率有偏 → 风险估计失真;PAC 界不覆盖这种抽象误设(§7 自认)。
3. **谓词难表达的 unsafe**:语义模糊、连续感知量、需要 LLM 判定的行为属性(T5 的 INTIMA 谓词正撞这堵墙——谓词求值本身带噪声,ProbGuard 假设谓词是环境真值)。
4. **非平稳/分布漂移**:trace 离线收集,运行时不更新(论文明说);agent 或环境变了,DTMC 过期无防。
5. **干预依从性**:reflect 是纯文本 advisory,agent 不听劝就没有强制力;stop 有强制但完成率崩(10.42%)。干预本身还会改变行为分布,使离线学的 DTMC 在"被干预系统"上不再校准(全文未讨论,见 03 批判)。
6. **认证语义误用**:30 traces 下的输出是"风险估计"不是"认证概率";引用时不得写"提供了 (ε,δ) 认证的运行时保证"。

---

## 边界检验初步(给 04 铺垫)

1. Eq(1) 归一化依赖"观测数据不含 invalid 转移"——若 valid_tran 设计与现实冲突,分布欠归一(04 发现 #3)。
2. 样本界的方差因子在经验频率=1/2 处最大(1/4),强确定转移处最小——AV 域自环 0.999 本该省样本,但 B² 因子完全压倒它。
3. 监控自动机 Def 5.2 逐字执行与 F[0,K] 端点差一步(04 发现 #2)。
4. P_safe 的 BSCC 结构性条件(04 发现 #1)。
