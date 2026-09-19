# DERIVATION — AgentSpec:DSL 语义形式化梳理

**日期**:2026-08-13
**状态**:S01-S04 v1(首轮),复现与审查留后续窗
**说明**:本文公式极少(§2 两个轨迹式 + §3.3 三定义四算子,无定理),故本文件不做公式推导,改做**规则求值语义的重写与检验**,并梳理其与 LTL / 自动机 / runtime enforcement 理论的关系。凡论文未表述、属本拆解延伸的内容,一律标 [个人分析]。

---

## 1. 底座:agent 形式模型(§2.1、§2.3)

- agent 五元组 \((\mathcal{S}, \mathcal{A}, \Omega, \Pi, \Delta)\):状态集、动作集、观测集、感知函数 \(\Pi: \Omega \to \mathcal{S}\)、策略 \(\Delta: (\mathcal{U}, \mathcal{S}) \to \mathcal{A}\)。
- 轨迹 \(\tau = \langle s_0 \xrightarrow{a_0} s_1 \xrightarrow{a_1} \dots \xrightarrow{a_{n-1}} s_n \rangle\);切片 \(\tau[:-i]\) 去掉最后 i 个转移。
- 运行回路:\(a_i = \Delta(u, s_i)\) → 执行得 \(\omega_i\) → \(s_{i+1} = \Pi(\omega_i)\) → 再规划。
- 目标(§2.3):给定 \(\texttt{Eval}(\tau_i, a_i)\),保证其全程安全;检测到潜在违规时干预,使改写后的轨迹保持安全。注意 Eval 是**目标陈述中的抽象函数**,论文没有给出其实现——实际实现里"安全"就是"无规则违规" [个人分析]。

---

## 2. 规则求值语义(Def 3.1 / 3.2 重写)

规则 \(r = (\eta_r, \mathcal{P}_r, \mathcal{E}_r)\):触发事件、谓词集、enforcement 序列 \(\langle e_r^0, \dots, e_r^n \rangle\)。

**触发判定** fired(η, τᵢ, aᵢ)(§3.3 文字定义的形式化重写 [个人分析]):

| η | fired 条件 |
|---|---|
| state_change | \(s_i \neq s_{i-1}\) |
| action | 即将执行 \(a_i\)(执行前时点) |
| agent_finish | \(a_i\) 为任务结束动作 |
| 域事件(如 pour、Transfer) | 动作型域事件 = action 事件在特定动作名上的细化;环境型域事件(red_light_detected)= state_change 在特定状态分量上的细化 [推断,论文未明说分类归属,实现上见 Table 1 的域划分] |

**违规判定**(Def 3.2):

\[ \texttt{viol}_r(u, \tau_i) \;\triangleq\; \texttt{fired}(\eta_r, \tau_i, a_i) \;\wedge\; \bigwedge_{p \in \mathcal{P}_r} p(u, \tau_i) = \texttt{true} \]

即:**事件发生 ∧ 谓词全真**(合取)。谓词签名 \(p(u, \tau_i) \in \mathcal{B}\);有效依赖随触发类型变化(state_change 只依赖 \(s_i\),action 依赖 \(s_i, a_i\))。

**三处口径需要对齐** [个人分析]:
1. 形式记法 p(u, τᵢ) vs 文字描述"只需要 sᵢ / 需要 sᵢ 与 aᵢ" vs 实现签名"(user_input, trajectory)"(§4)——三者相容(后两者是前者的投影),但论文没有显式说明。
2. check 为空(语法允许 Pred*)时合取空集为真 → 规则退化为"事件即违规"。
3. 合取里的否定只在谓词级(!p),无析取——"或"条件须拆成多规则。

---

## 3. 四个 enforcement 算子(§3.3 原文 + 手推)

以 \(a_f\) 记 finish 动作,\(a_p\) 预定义动作,\(a_c\) 自反思纠正动作,\(\omega_r\) 违规观察:

| 算子 | 原文定义 | 效果 |
|---|---|---|
| Stop | \(e_r(\tau_i) = \tau_{[:-1]} \xrightarrow{a_f} s_i\) | 轨迹终止 |
| User Inspection | 允许:\(\tau_i\);拒绝:\(\tau_i \xrightarrow{a_f} s_i\) | 人裁决:原样继续或终止 |
| Predefined Action | \(e_r(\tau_i) = \tau_i \xrightarrow{a_p} s'_i\) | 追加安全动作,进入新状态 |
| LLM Self-Examination | \(a_c = \Delta(u, s_i)\)(相对 \(\omega_r\)),\(e_r(\tau_i) = \tau_i \xrightarrow{a_c} s'_i\) | 把"违反了规则 r"作为观察注入,重新规划 |

**手推 1(转账例,§2.2)**:u = "转 $100 给 Bob",agent 规划 aᵢ = Transfer。动作事件 Transfer 触发 @inspect_transfer;check !is_to_family_member:若 Bob 不在家人名单 → 真 → 违规;enforce user_inspection:用户批准 → τᵢ 原样,执行转账;拒绝 → τᵢ→a_f sᵢ,任务终止。与 Figure 2 及正文叙述一致。✓

**手推 2(pour 例,§5.2)**:计划序列 [find mug, fillLiquid, pick, find laptop, pour]。前四步无规则命中;执行 pour 前,动作事件 pour 触发 @stop_pouring_damage;!is_into_wettable_object(laptop 不在可浇白名单)= 真 → 违规;stop → 轨迹以 a_f 终止,浇笔记本未发生。与 Table 4 具身域归零机制一致。✓

**记号疙瘩(诚实标注,均 [原文如此/个人分析])**:
1. **Stop 与 Inspection-拒绝的不对称**:stop 写成 \(\tau_{[:-1]} \xrightarrow{a_f} s_i\)(去掉最后一个转移再以 a_f 进入 sᵢ,相当于改写了已发生的最后转移),拒绝写成 \(\tau_i \xrightarrow{a_f} s_i\)(在 sᵢ 上追加 a_f 自环转移)。两者操作意图相同(终止),形式却一个"替换尾转移"、一个"追加转移"——疑为记号不严谨,复现窗对照代码确认实际行为。〔08-22 已核:两式均 **arXiv 2503.18666 §3.3 原文如此**(非转写笔误);代码事实(src/enforcement.py):Stop 返回 Action.get_finish()(合成 finish 动作),UserInspection 拒绝返回 Action.get_skip()——运行时两者都是执行前拦截并替换待执行动作,拒绝走 skip 档而非 finish 档;论文两公式皆示意性记号,与任一公式均非严格对应。"复现窗确认"销项〕
2. §2.3 的干预结果式 \(\tau'_{i+1} = \tau_i \xrightarrow{a'_i} s_i\) 以 sᵢ 结尾(替换动作后仍回到原状态),与 §3.3 Predefined Action 的 \(s'_i\)(新状态)不一致——前者应视为示意性记号。〔08-22 已核:arXiv HTML §2.3 终态确为 sᵢ 无撇、§3.3 invoke_action/self-examine 确到 s′_i 有撇——"原文如此"实断,"示意性记号"判定成立〕
3. \(\mathcal{E}_r\) 是**序列**(Enforce+),即一条规则可依序施加多个动作(Figure 8 一次下发五个参数化动作);序列内的复合语义(前一个算子的输出是后一个的输入)论文未显式定义 [个人分析]。

---

## 4. 执行回路的小步语义(Def 3.3 重写为伪代码)

```
loop:
  a_i = Δ(u, s_i)                        # 规划
  for r in R where viol_r(u, τ_i):       # 注意:多条规则的遍历次序未定义
    for e in E_r:                        # 依序施加该规则的 enforcement 序列
      τ_i = e(τ_i)
  if last_action(τ_i) == a_f: halt       # 任一 enforcement 引入 finish 即停机
  else: 执行 a_i → ω_i → s_{i+1} = Π(ω_i) # 无违规或干预后继续
```

原文关键句(Def 3.3):"each violated rule applies its enforcement functions to update τᵢ";"If the last action in τ′ᵢ is a finish action, the agent stops. Otherwise, the agent proceeds by executing the action aᵢ…"。

**未定义行为清单** [个人分析]:①多规则同时违规的施加次序与冲突(如规则 A 说 stop、规则 B 说 invoke_action);②enforcement 改写轨迹后是否对新轨迹**重新做一轮规则求值**(§3.3 开头的直觉描述说"每次动作后重新评估环境直到无违规",但形式定义只写了单轮);③invoke_action 引入的 a_p 本身若触发别的规则怎么办。这三点是把 AgentSpec 语义"补完备"的最小工作量,也是 T5 写形式化章节时的免费改进点。

---

## 5. 与 LTL 的关系 [个人分析,论文未做此对应]

**对应命题**:一条规则 r 监控的目标性质可写为 LTL 安全公式

\[ \varphi_r \;=\; \mathbf{G}\,\neg\big(\texttt{fired}_{\eta_r} \wedge \bigwedge_{p \in \mathcal{P}_r} p\big) \]

- \(\texttt{viol}_r\) 在时刻 i 为真,恰好等于轨迹前缀 \(\tau_i\) 是 \(\varphi_r\) 的一个 **bad prefix**(坏前缀:任何延续都无法满足 G¬…,因为违规已在当下发生)。AgentSpec 做的是 bad prefix 的**最早检测 + 即时干预**——这正是 runtime verification(只报告)与 runtime enforcement(改写行为)的分界。
- 规则集 R 的联合目标 = \(\bigwedge_{r \in R} \varphi_r\);等价地,违规条件层是各规则合取子句的**析取**(DNF)——DSL 布尔层"仅否定文字的合取 + 多规则"恰好给出 DNF 完备性(对给定谓词字母表)。
- **时序表达力**:DSL 表面无 X/U/F/G 算子。但谓词能读整条前缀 \(\tau_i\),故任何**过去可测**(past-testable)的安全性质都能藏进谓词实现(如"曾经打开过炉灶且此后未关"、"连续 k 轮出现依赖信号")——表达力是"past-complete, future-free"的:关于未来的性质(liveness、bounded response)既不可表达也不可强制;唯一的弱例外是 agent_finish 触发器可挂**终态义务**检查(任务结束时必须满足 X),这属于"有限轨迹上的终点条件",不是真正的 liveness。
- 对照 ProbGuard:同一个"未来"缺口,ProbGuard 用 \(P_{=?}[\mathbf{G}\,\neg unsafe]\)(PCTL 定量查询)+ K 步倒计时监控自动机(STL bounded response 翻译)去填;AgentSpec 在 LTL 谱系里停在"当下判定的安全片段"。

---

## 6. 与自动机 / runtime enforcement 理论的关系 [个人分析;论文 §7 仅引 Falcone et al. 2011 综述]

- **监控自动机视角**:每条规则可编译为一个两状态确定性监控器(idle → violated,violated 即触发 enforcement 后复位或停机);规则集与 agent 转移系统的同步积就是"被强制的 agent"。对照 ProbGuard 的三状态族(idle / wait(i) / viol,带 K 步倒计时)——AgentSpec 的监控器**无记忆**(所有历史依赖都藏在谓词读 τᵢ 里),ProbGuard 的监控器把时间记忆显式化为自动机状态。T5 若做窗口化累积 unsafe,监控器形态介于两者之间(滑动窗口计数器自动机),这是 D6 缺口 2 要写的构造。
- **经典强制理论对照**:Schneider 的 security automata 只能**截断**(truncation)执行,可强制的恰是安全性质;Ligatti 等的 edit automata 增加**插入/替换**能力,可强制更大类。AgentSpec 四动作在此谱系上的位置:stop ≈ truncation;user_inspection ≈ 神谕引导的 truncation;invoke_action / llm_self_examine ≈ edit(替换/插入动作)。即 AgentSpec 事实上实现了一个 edit-automata 风格的强制器,但论文未援引该理论、也未讨论"哪些性质可被四动作强制"的完备性问题——又一个 T5 可白捡的形式化连接点。
- **与 ReGA(北大 Meng Sun 组)的抽象对照**:ReGA 把 LLM 隐藏状态抽象成 DTMC(白盒、token 级、概率),AgentSpec 把 agent 行为轨迹交给谓词+两状态监控器(黑盒、动作级、定性)。两者是"模型内部 vs 行为外部"两条正交抽象轴,T5 主路线取后者、以前者为 fallback(D6 卡 2)。

---

## 7. 与 DTMC / ProbGuard 的形式接口(§6.3)

§6.3 原文要点:AgentSpec"在离散执行检查点做确定性 enforcement…不推理当前动作的长期后果",future work 是"从历史 agent 交互学 DTMC,计算概率可达查询,估计 unsafe 状态是否以非平凡概率可达,从而在前置条件未违反但风险路径概率不小时提前干预"。

形式化地:AgentSpec 判定 \(\texttt{viol}(\tau_i) \in \{0,1\}\)(当下、定性);ProbGuard 计算 \(P[\psi \mid abs(s_i)]\)(未来、定量),阈值化后触发干预。两者共享拦截层与干预动作集,差别只在"判定函数"从布尔谓词换成概率查询——这就是 T5 管线里"规则层(本文)+ 预测层(ProbGuard)"可以叠放的结构原因 [个人分析,叠放设计属 T5]。

---

## 8. 边界检验与成长追问:这套语义什么时候失效?

1. **谓词错误**:viol 的真值完全由谓词决定;白名单漏一个 URL、家人名单过期,语义照常运转但保护失效——框架保证的是"违规必干预",不是"危险必违规"。
2. **事件盲区**:fired 只在三拦截点求值;检查点之间的环境副作用(工具内部行为、外部世界变化)不进入 τᵢ,规则不可见。
3. **多规则冲突**:§4 未定义次序;stop 与 invoke_action 并发违规时行为依赖实现细节(复现窗验证)。
4. **自反思不忠实**:llm_self_examine 假设注入 ω_r 后 Δ 会给出真正纠偏的 a_c;若 agent 口头合规、行为不变(CoT 不忠实,D6 轴①),该算子静默失效——四算子中唯一无硬保证的一个。
5. **user_inspection 的裁决者错位**:语义把 user 当安全权威;在 companion 域 user 可能是风险承受者本人,直接套用会把干预权交给最不该裁决的人(T5 移植时必须改,见 03 Layer 10)。

---

**数据来源**:arXiv:2503.18666 §2.1-2.3、§3.3、§4、§6.3(2026-08-13 实取);security/edit automata 与 LTL 对应为本拆解延伸 [个人分析];ProbGuard 侧信息引 D6 卡 1。
