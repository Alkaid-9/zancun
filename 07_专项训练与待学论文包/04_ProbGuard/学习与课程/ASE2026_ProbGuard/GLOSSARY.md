# GLOSSARY — ProbGuard(ASE 2026)核心术语

**日期**:2026-08-13 | 共 20 条,按主题分组

---

## 形式化与规范

1. **CTL(计算树逻辑)**:分支时间时序逻辑,路径量词 A(所有路径)/E(存在路径)× 时序算子 X(下一步)/F(最终)/G(全局)/U(直到)。本文只用其定性判断,概率交给 PCTL。
2. **PCTL / P=?[·] 查询**:概率 CTL;P=?[ψ^π] 返回"从当前状态出发路径满足 ψ^π 的概率",是 P_safe 的计算形式,PRISM 直接支持。
3. **安全不变式 AG ¬unsafe**:核心性质形态——沿所有路径、全局地不进 unsafe 状态。因 CTL 状态公式无概率语义,概率附着在路径公式 ψ^π = G ¬unsafe 上(ψ = A ψ^π)。
4. **谓词抽象(predicate abstraction)**:Graf–Saïdi 1997 经典技术。n 个布尔谓词把具体状态 v 映成真值向量 s_P(v) ∈ {0,1}^n,只保留安全相关信息。本文谓词从性质 ψ 机械提取。
5. **valid_tran(语义合法转移谓词)**:域专家声明哪些抽象状态间转移物理/语义可能(如 collision=true 是吸收态)。三重作用:剪状态空间、限定 Laplace 平滑范围(定义 k_i)、保证 B 有限。
6. **STL 有界响应片段 STL_LB**:G(φs ⇒ F[0,K] φt)——触发 φs 后 K 个时间单位内必须响应 φt。LawBreaker 交通法的形态,经监控自动机翻译进 CTL 世界。
7. **监控自动机(monitor automaton)**:确定性自动机 Q = {idle, wait(K..0), viol},把 K 步响应义务编译成状态倒计时;viol 吸收。使有界活性归约为可达性。
8. **同步积(synchronous product)**:环境 DTMC ⊗ 监控自动机;s 分量概率转移、q 分量确定更新,积仍是 DTMC,性质归约为 AG ¬viol。状态数 |S|×(K+3)。

## 学习与保证

9. **DTMC(离散时间马尔可夫链)**:M=(S, P),行随机转移矩阵;本文的行为模型,从执行轨迹的抽象序列统计而来。
10. **valid-transition-aware Laplace 平滑**:P̂(sj|si) = (n_ij+α)/(n_i+k_i·α)(仅合法转移,α=1),非法转移硬零。与标准加性平滑的差别:分母用合法出边数 k_i 而非 |S|,不给语义不可能事件质量;副产品是合法转移概率有正下界。
11. **(ε,δ)-PAC-correct**:Pr(|P_M̂(ψ^π) − P_M(ψ^π)| ≤ ε) ≥ 1−δ;外层 Pr 对**采样学习过程**——保证的是"学习程序可靠",不是单次学出的链有个体证书。
12. **条件数 B(P̂)**:局部转移误差被放大为全局满足概率误差的系数(|ΔP_global| ≤ B·max|ΔP_local|,Bazille Thm 5);以平方进入样本界,是样本复杂度主宰项。实测:具身 1.0–481,AV 10⁷–10⁸。精确定义在 Bazille 原文。
13. **union bound(δ' = δ/|S|)**:把全局失败预算 δ 均摊到每个状态;逐状态置信 1−δ' 检查通过后,总失败概率 ≤ |S|·δ' = δ。
14. **频率估计(frequency estimation)**:不平滑的 n_ij/n_i。放弃均匀 CTL 保证,换 Bazille Thm 3 的单性质界(185–1,016 traces)——强持久域(B 爆炸)的唯一现实选择。
15. **Markov 假设与抽象误设(misspecification)**:假设未来只依赖当前抽象状态。抽象过粗 → 历史依赖被压掉 → 转移概率有偏;**PAC 界只覆盖学习误差,不覆盖误设**(§7 自认)。
16. **行为持久性(behavioral persistence)**:AV 域自环概率 >99.9%、状态间转移 <10⁻⁵ 的结构特征;Laplace 平滑在此类链上把 B 顶到 10⁷⁻⁸,均匀 PAC 界失效。与之相对,具身任务"前向推进"链混合好。

## 系统与实验

17. **P_safe 与阈值 θ**:P_safe = P[ψ|s_i](当前状态出发保持安全的概率,离线预计算查表);θ 是其下界,P_safe < θ 触发干预;θ 越大越严格(全文统一约定)。
18. **stop / reflect(干预模式)**:stop = 终止执行(强制,完成率 10.42%);reflect = prompt 注入三字段风险 alert(违反的规则/当前符号状态/违规转移及概率),agent 自行修订(advisory,不改控制流,完成率 47.74%)。
19. **AWT(Advance Warning Time)**:t_fail − t_pred,预警领先违规发生的时间;只在真发生违规的 run 上有定义,必须与 FP 率成对报告(θ=0.3 时 0% FP / 最长 15.84s;θ=0.7 时 100% FP / 最长 38.66s)。
20. **实验设施谱系**:SafeAgentBench(具身安全任务)+ LangChain ReAct + gpt-4o-mini(具身域);Apollo 9.0 + LawBreaker(STL 交通法)+ μDrive(违法场景生成)(AV 域);PRISM(概率模型检查)。AgentSpec(同组 ICSE 2026)既是代码地基(controlled_agent_executor)又是被比基线;REDriver(同组 ICSE 2024)是 AV 域基线;Bazille CAV 2020(Jun Sun 参与)是 PAC 理论源头。
