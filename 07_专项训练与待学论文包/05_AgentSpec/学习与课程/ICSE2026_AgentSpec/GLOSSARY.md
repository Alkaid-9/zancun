# 术语表 — AgentSpec (ICSE 2026)

**日期**:2026-08-13
**状态**:S01-S04 v1(首轮),复现与审查留后续窗
**用途**:本论文及其谱系(ProbGuard/T5)拆解通用术语;[个人分析] 标注论文未用、本拆解引入的概念。

---

## DSL 与规则层

| 术语 | 英文 | 一句话解释 | 出处 |
|---|---|---|---|
| 运行时强制 | Runtime Enforcement | 运行中检测违规并**改写行为**(区别于只报告的 runtime verification) | §1、§7 |
| 领域特定语言 | DSL (Domain-Specific Language) | 本文指五段式规则语言 rule/trigger/check/enforce/end | §3.1 |
| 触发事件 | Trigger / Event | 激活规则的事件:通用三种(state_change/action/agent_finish)+ 域事件 | §3.2, Table 1 |
| 谓词 | Predicate | Python 布尔函数 p(user_input, trajectory)→bool,check 段的合取单元 | §3.2, §4 |
| 强制动作 | Enforcement | 违规时施加的轨迹变换,四原语见下 | §3.2-3.3 |
| 规则三元组 | — | r = (η_r, P_r, E_r):事件+谓词集+enforcement 序列 | Def 3.1 |
| 规则违规 | Rule Violation | 触发事件发生 ∧ 全部谓词为真(合取) | Def 3.2 |
| ECA 范式 | Event-Condition-Action | 数据库/主动系统的经典规则范式;AgentSpec 三段式即其 agent 化 [个人分析] | — |

## 四个 enforcement 原语

| 术语 | 轨迹变换 | 直觉 | 出处 |
|---|---|---|---|
| stop | τ[:-1] →a_f sᵢ | 立即终止任务 | §3.3 |
| user_inspection | 允许原样 / 拒绝则终止 | 暂停并请人裁决 | §3.3 |
| invoke_action(params) | τᵢ →a_p s′ᵢ | 替换为预定义安全动作(键值参数) | §3.3 |
| llm_self_examine | 注入 ω_r → τᵢ →a_c s′ᵢ | Reflexion 式自反思重规划 | §3.3 |

## 实现层

| 术语 | 一句话解释 | 出处 |
|---|---|---|
| iter_next_step | LangChain agent 回路核心函数,AgentSpec 的拦截对象 | §4 |
| AgentAction / AgentStep / AgentFinish | 三个拦截决策点:动作执行前 / 观测产生后 / 任务完成 | §4 |
| ANTLR4 | 解析器生成器,解析 DSL(仓库语法文件 `spec_lang/AgentSpec.g4` [D6]) | §4 |
| controlled_agent_executor | 仓库中的受控执行器,ProbGuard 直接依赖 [D6] | — |
| handle_function_call | AutoGen 中 ToolAgent 的成员函数,框架移植时的动作事件孔道 | §4 |
| μDrive | 同组用户可控自动驾驶工作(Kun Wang 一作),AV 域谓词与预定义动作来源 | §5.2, 参考文献 40 |

## 基准与域

| 术语 | 一句话解释 | 出处 |
|---|---|---|
| CodeAct | 代码执行 agent 框架(代码域被保护对象) | §5.1 |
| RedCode-Exec | 代码执行风险基准:25 风险类 × 30 例 | §5.1 |
| SafeAgentBench | 具身 agent 安全任务基准:10 危害类 + 安全对照任务 | §5.1 |
| FixDrive | 同组 AV 违法行为修复工作(ICSE 2025),提供 8 个违法场景与规则 | §5.1, 参考文献 37 |
| LawBreaker | 同组交通法规范化+AV 模糊测试工作(ASE 2022),法条编号来源(Law38/44/46/53) | §5.2, 参考文献 36 |
| Apollo | 百度自动驾驶栈,AV 域 agent 底座 | §5.1 |
| ToolEmu | LLM 沙盒式 agent 风险评估(对比对象:无强制) | §1, §7 |
| GuardAgent | LLM 解释约束+生成 guard 代码(对比对象:逐 agent 手工) | §1, §6.1 |
| NeMo / LCEL / llama.cpp grammar | 对话层/句法层约束机制(对比对象:非语义级) | §6.1 |

## 指标与实验

| 术语 | 一句话解释 | 出处 |
|---|---|---|
| #inv / #vio / #pass | 代码域三列:计划调用解释器次数 / 触发规则次数 / 人工放行次数 | Table 3 |
| enforcement rate | LLM 生成规则在未见风险场景上成功强制的比例(Table 6 "Enforced%") | §5.3 |
| precision / recall(RQ2 口径) | 具身域 95.56%/70.96%;recall 借安全对照任务计算〔08-22 已核:论文口径——实为拦截率 TPR 与不误拦率 specificity(1−FPR)的标签互换,引用标"论文口径"〕 | §5.3 |
| 安全税 | 安全任务完成率损耗(58.62%→54.26%)[个人分析用语] | Table 4 |

## 形式化与理论(04 文件用)

| 术语 | 一句话解释 | 出处 |
|---|---|---|
| 安全性质 | Safety Property | "坏事永不发生"类性质,G¬bad;runtime enforcement 的经典可强制类 | [个人分析] |
| 坏前缀 | Bad Prefix | 使安全性质不可再满足的有限前缀;viol 为真 = 检测到坏前缀 | [个人分析] |
| security automata / edit automata | 截断式 / 编辑式强制器;stop≈截断,invoke_action/self_examine≈编辑 | [个人分析];§7 引 Falcone 2011 |
| DTMC | 离散时间马尔可夫链;§6.3 future work 的概率前瞻模型,ProbGuard 的核心 | §6.3 |

## 谱系

| 术语 | 一句话解释 |
|---|---|
| SMU Jun Sun 组 | 孙军(新加坡管理大学):AgentSpec、ProbGuard、FixDrive/LawBreaker/μDrive 工具链 |
| PKU Meng Sun 组 | 孙猛(北大):ReGA(FSE 2026);与本文无作者重叠,桥文献为 ICML 2025 立场文(本文参考文献 53) |
| ProbGuard | 同组后继(ASE 2026):学 DTMC 做概率可达预警;代码依赖本仓库执行器 [D6] |
| T5 | companion 域概率护盾提案;本文四动作 = 其分级干预规则层母版 |

---

**最后更新**:2026-08-13(S01-S04 v1)
