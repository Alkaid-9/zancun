# QUESTIONS — ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction

**日期**:2026-08-13
**论文**:ProbGuard(原 Pro2Guard),ASE 2026
**类型**:实验论文(方法 + 定理 + 两域实验 + 开源代码)
**关联**:SMU Jun Sun 组核心;T5(companion 域概率护盾)的方法学母版;Phase 1 复现首选

---

## 核心问题

### Q1: 这篇论文的核心创新点是什么?

> 前人的 agent 运行时防护(AgentSpec/GuardAgent/ShieldAgent)是**反应式**的:只有当某个状态转移违反规则、或违规已不可避免时才拦截,对"长时程累积风险"(炉灶开着离开厨房、加速冲向繁忙路口)没有预见力。本文把防护改写成**概率预测问题**:离线从执行轨迹学一个符号状态上的 DTMC,运行时查询"从当前状态出发、未来永远保持安全的概率" P_safe = P[AG ¬unsafe | s_i],低于阈值 θ 就干预。AV 域预警最长提前 38.66 秒,且在全部评估场景中警告严格早于违规发生。
>
> 注意创新的真实位置:谓词抽象(Graf–Saïdi 1997)、DTMC 学习、PRISM 查询、PAC 界(Bazille CAV 2020,Jun Sun 本人是共同作者)全是现成件;新的是**问题重构(reactive→proactive)+ valid-transition-aware Laplace 平滑 + PAC 界在两个真实域的实测与诚实的不可行性报告**。

### Q2: 论文的方法流程是什么?

```
离线(Algorithm 1):
  域专家写 CTL 性质 ψ = AG ¬unsafe(AV 域:STL 法规先经监控自动机翻译)
    → 从 ψ 提取原子谓词集 P_ψ = {φ1..φn}
    → 循环:采样 trace → 逐状态抽象 s_P(v) ∈ {0,1}^n → 符号 trace
        → 累计转移计数 n_ij → valid-transition-aware Laplace 平滑(Eq 1)
        → 直到 PACBoundSatisfied(ε,δ)
    → 输出 DTMC M̂;对每个符号状态离线预计算 P[ψ|s](PRISM),存缓存表

在线(Algorithm 2):
  每决策步:观测具体状态 v_i → 抽象 s_i(AV 域再同步监控自动机状态 q_i)
    → 查表得 P_safe = P[ψ|s_i],O(1)
    → P_safe < θ ?→ 干预:stop(终止)或 reflect(prompt 注入三字段风险 alert:
       违反的规则 / 当前符号状态 / 违规转移及其模型检查概率)
```

### Q3: 这篇论文和 AgentSpec、ReGA、ShieldAgent、Bazille 2020、T5 是什么关系?

- **AgentSpec(ICSE 2026,同组)**:反应式 DSL 规则强制层,其 §6.3 明确把"学 DTMC 做概率可达性查询"列为 future work——ProbGuard 就是那个 future work。代码上 ProbGuard 依赖 AgentSpec 的 `controlled_agent_executor`(复现顺序:先 AgentSpec 后 ProbGuard)。实验里 AgentSpec 又是被比较的基线(token -12.05%)。
- **ReGA(FSE 2026,北大 Meng Sun 组,注意重名)**:同属"DTMC 抽象 + 运行时评分"家族,但 ReGA 是**白盒表示抽象**(读 LLM 隐藏状态,token 级),ProbGuard 是**黑盒行为抽象**(只看环境符号状态,动作级,policy-agnostic)。T5 主路线是后者;ReGA 是 K1 kill criteria 触发时的退路。
- **ShieldAgent(ICML 2025,Bo Li 组)**:概率语义来自 Markov Logic Network 的规则权重,是"每步动作合规判定"(空间维度),无轨迹动力学模型,不产生提前量;ProbGuard 是"轨迹级风险预测"(时间维度)。
- **Bazille et al.(CAV 2020)**:PAC 界的理论源头(Thm 3/5/6),ProbGuard 的 Thm 3.4 + Appendix A 是把它组装到 Laplace 平滑学习循环上;Jun Sun 是 CAV 论文共同作者——这条线是同一团队十年积累的变现。
- **T5**:域迁移目标。ProbGuard 的 unsafe 是瞬时物理谓词;T5 要的"窗口化累积 unsafe"(依赖螺旋)在本文只有 AV 域 K-bounded response 的近亲(语义不同:响应义务 vs 累积超阈)——正是 T5 的形式化空位。

### Q4: 核心公式的直觉是什么?

- **Eq (1)(valid-aware Laplace)**:没见过的合法转移不判死刑(给 α=1 伪计数),语义上不可能的转移判死刑(硬零)。副产品:所有合法转移概率有正下界 → 条件数 B(P̂) 有限可算 → PAC 界能在运行时检查。
- **Def 3.3(PAC-correct)**:两层概率要分清——外层 Pr 是对"采样学习过程"的(95% 的实验里学到的链够准),内层 P_M(ψ^π) 是对"轨迹分布"的(这条链上永远安全的概率)。
- **样本界**:三因子相乘——(11/10·B)² 是"局部转移误差 → 全局可达概率误差"的放大系数;2/ε²·log(2/δ') 是标准 Chernoff 集中;[1/4−(max_j|1/2−p̂_ij|−2ε/3)²] 是经验方差修正(转移越确定,方差越小,需要的样本越少)。
- **Algorithm 2 阈值**:θ 是 P_safe 的下界,越大越严格;P_safe 随轨迹逼近危险区单调恶化,θ 画在哪里决定"预警多早"与"误报多少"的交换比。

### Q5: 一个值得质疑的假设

- **假设**:谓词抽象后的符号状态满足 Markov 性——未来行为只依赖当前抽象状态,与历史无关。
- **为什么可能不成立**:谓词集从 ψ 派生,只编码安全相关的瞬时信息;延迟效应、历史依赖行为(LLM agent 的上下文记忆正是历史依赖的!)会被抽象压掉,导致转移概率有偏。
- **论文是否已回应**:§7 Threats 第一条明确承认:抽象过粗会破坏 Markov 性,且 **PAC 界只覆盖"学习误差",不覆盖"抽象误设(misspecification)"**。回应是诚实的,但没有给任何检测/量化抽象误差的手段(如高阶依赖检验)。
- **边界检验**:AV 域 FP 率对 θ 的悬崖式敏感(0.3→0%,0.5→75%,0.7→100%)暗示学到的 P_safe 在安全场景上分布挤在 0.3–0.7 之间,校准质量存疑——这可能就是抽象误差+30 traces 小样本的合成症状。具身域 stop@0.9 完成率崩到 10.42% 同理:P_safe 估计对安全轨迹也普遍偏低。
- **判断**:**方法论上诚实,工程上未解决**。"PAC 保证"的营销与"30 traces 演示"的现实之间的张力,是本文最需要批判性引用的地方;但作者在 §7 把差距摊开说了,这比多数同类论文体面。

---

## S02 跟进问题(读骨架后)

1. 条件数 B(P̂) 的精确定义是什么?ProbGuard 全文只引用不定义——需读 Bazille CAV 2020 原文(S05 复现窗任务)。
2. Figure 2 的 stove DTMC 里,安全吸收态(任务完成)的结构是什么?s0→s1 概率 31/184 的分母 184 是"s0 的访问次数"——30 条 trace 产生 184 次 s0 访问,每条 trace 平均 6 次,合理。
3. FP 标定用 6 个安全场景,Table 1 有 7 个违规场景 × 4 条性质——FP 是按性质还是按场景聚合的?(正文只给了汇总数字)
4. 监控自动机 Def 5.2 逐字执行与 F[0,K] 语义差一步(见 04_DERIVATION 发现 #2)——代码实现取哪种?〔08-22 已核销项:都不取——公开监控路径(Pro2Guard 仓)不走显式自动机,实为 PRISM 查询 P=?[G !unsafe]+概率阈值 prob≥0.9,无 K 计数器;Def 5.2 系论文语义装置〕
5. 具身域 `elapsed ≥ T` 谓词的时间语义如何进 valid_tran?(elapsed 单调递增、agent 回厨房后重置——这些不变量必须由 valid_tran 编码,否则 DTMC 会学出"时间倒流"转移)
6. reflect 模式只报了 θ=0.9 一个点,reflect 的阈值扫描(0.3/0.5/0.7)在哪?——Pareto 前沿只有 stop 一侧是完整的。

---

## 品味判断(S01 初评)

- **新颖性分布**:谓词抽象(低,1997 经典)< DTMC 学习+PRISM 查询(低,LUNA/DeepStellar 谱系)< STL→监控自动机→同步积(低,教科书构造)< valid-aware Laplace(中,小而实在)< proactive 范式落在 LLM agent(中高,问题重构)< **PAC 界在两个真实域的实测与负结果**(高,B≈10⁷–10⁸ 的不可行性报告是文献里第一次有人给出这个数字)。
- **核心价值**:不是发明新方法,而是**给"概率护盾"路线画了一张可行性地图**——什么域能用均匀 PAC 界(前向推进型)、什么域只能退频率估计(强持久型)、认证需要多少样本、30 traces 能买到什么。对 T5 来说这张地图比方法本身值钱。
- **最大软肋**:实验规模(7 AV 场景 + SafeAgentBench 子集、30 traces、单 LLM 单框架)与"保证"叙事不匹配;reflect 模式缺阈值扫描;干预后分布漂移问题(干预改变行为分布,DTMC 是无干预分布学的)全文未讨论。
- **对 T5 的意义**:管线一比一可抄;差异化空位(窗口化累积语义、干预 Pareto、对话域 B 值)已验证存在。

---

## Critical Thinking 审计

- Q1 审计:"proactive"的实证支撑成立(AWT 表 + 100% 检出),但检出率的分母只有 7 个场景,外推要谨慎。
- Q2 审计:流程闭环清晰;缓存查表是把"模型检查在线开销"问题转化为"离线预计算 + 状态数小"的前提,左墙之一。
- Q3 审计:谱系关系有代码依赖(AgentSpec)和作者连续性(Bazille)双重证据,不是拼贴;ReGA 的对照(白盒/黑盒)是 T5 决策的关键轴。
- Q4 审计:公式直觉与 04_DERIVATION 手推一致;样本界中方差因子的 ε 尺度(全局 vs 局部)存疑,已标注待核。
- Q5 审计:Markov 假设的质疑有论文自认(§7)+ FP 悬崖旁证,成立;但"校准差"目前是推断而非实测,复现时应画 P_safe 的可靠性图(reliability diagram)验证。
