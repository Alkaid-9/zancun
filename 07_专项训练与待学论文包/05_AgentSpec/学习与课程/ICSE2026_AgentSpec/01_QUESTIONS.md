# QUESTIONS — AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents

**日期**:2026-08-13
**论文**:ICSE 2026,SMU Jun Sun 组(Haoyu Wang 一作)
**状态**:S01-S04 v1(首轮),复现与审查留后续窗
**说明**:读前 5 问基于 D6 卡 3 的预期先立,读后答案以论文原文回填并标出处。

---

## 读前 5 问

### Q1:它凭什么自称"第一个"?与已有 guardrail 的本质区别在哪?

**读前假设**:卖点应该在"强制"(enforcement)而非"评估"(evaluation)。

**读后答案**:论文的自我定位是"the first framework that systematically enforces customizable safety constraints on LLM agents at runtime"(§1)。区别轴有三条(§1、§6.1):
- 对 ToolEmu(LLM 沙盒模拟评估):那是执行前风险评估,不可解释、**无强制机制**,易被对抗操纵;AgentSpec 在运行时主动改写轨迹。
- 对 GuardAgent(LLM 解释约束+生成 guard 代码):那要**逐 agent 手工实现**,且约束解释依赖 LLM;AgentSpec 是外置的、开发者定义的规则,与 LLM 推理解耦,可审计。
- 对 NeMo / llama.cpp / LCEL:那些在对话层或句法层做模式匹配;AgentSpec 在**执行关键点**(高影响动作调用前)拦截,针对语义级性质(§6.1)。

**判断**:"第一"的成立依赖"systematically + customizable + runtime enforcement"三个限定词同时生效;单看任一维度都有前人(GuardAgent 有强制、NeMo 有 DSL 味道)。定位准确但表述有营销成分。

### Q2:trigger–check–enforce 三段式各自的设计空间多大?表达力边界在哪?

**读后答案**:
- **trigger**:3 个通用事件(state_change / action / agent_finish)+ 开放的域事件表(代码域 PythonREPL,机器人域 pour、pick 等约 17 个动作词,ADS 域 red_light_detected 等环境事件,Table 1)。事件系统自述"只要能监控并抽象出事件就能扩展新域"(§3.2)。
- **check**:谓词合取。DSL 层只有 `True | False | !Pred | 域谓词`(Figure 3)——**没有析取、没有时序算子**;谓词本体是任意 Python 布尔函数,签名接收用户输入与当前轨迹(§4)。
- **enforce**:四个通用动作 stop / user_inspection / invoke_action(params) / llm_self_examine,域动作(如 AV 的 follow_dist)经 invoke_action 机制落地(§3.2)。

**判断**:DSL 表面极简,表达力几乎全部下沉到 Python 谓词层——"语言薄、库厚"的经典 DSL 权衡。析取要靠多条规则编码,时序性质要藏进谓词(详见 `04_DERIVATION.md` §6)。

### Q3:形式语义做到什么程度——有没有定理或保证?

**读前假设**(基于 D6 卡):只有定义,没有定理。

**读后答案**:证实。§3.3 给出三个定义:规则三元组 r=(η, P, E)、违规条件(事件发生 ∧ 谓词全真)、四种 enforcement 各自的轨迹变换算子,以及整体执行语义(违规规则依次施加变换,末动作为 finish 则停机)。**全文无定理、无证明**;§2.3 的目标"保证 Eval(τᵢ, aᵢ) 全程安全"只是目标陈述,论文没有证明 enforcement 能达成它(达成与否取决于谓词正确性,论文未形式化这层依赖)。

**判断**:这是"工程论文的形式化装饰"与"够用的精确性"之间的选择,ICSE 接受了后者。对我们的含义:T5 若能补一个小定理(如窗口化累积 unsafe 监控自动机与 DTMC 同步积的正确性,D6 缺口 2),就在形式化维度上超过母版。

### Q4:实验如何定义"安全"与"有效"?三个域的指标同构吗?

**读后答案**:**不同构**,这是读实验表最需要小心的地方(§5.2-5.3):
- 代码域:#inv(agent 试图调用解释器)/ #vio(触发规则)/ #pass(user inspection 放行),按 25 风险类分列(Table 3)。
- 具身域:危害任务"成功执行率"有/无 AgentSpec 对照(全部归零),外加安全任务完成率损耗(58.62%→54.26%,Table 4)。
- AV 域:8 个违法场景的合规通过率(全 100%,Table 5)。
- RQ2(LLM 生成规则)再换一套:enforcement rate(87.26% 代码)、precision/recall(95.56%/70.96% 具身)、场景通过数(5/8 AV)(Table 6)。

**判断**:跨域指标异构是"多域适用性"论证的代价;引用数字时必须带域名与指标定义,不能笼统说"AgentSpec 准确率 xx%"。

### Q5:与 ProbGuard / T5 的接口:哪些资产可直接继承?

**读后答案**:
- 代码资产:LangChain 拦截层(`iter_next_step` 三决策点,§4)即 ProbGuard 的 `controlled_agent_executor` 来源 [D6 元数据 3];复现次序上本文是前置。
- 概念资产:§6.3 自述局限(确定性、无前瞻)+ future work(学 DTMC、概率可达查询)= ProbGuard 立项书;四种 enforcement = T5 分级干预档位母版(映射见 `03_PAPER_READ.md` Layer 10)。
- 协议资产:SafeAgentBench 任务集 + 危害归零/安全完成率损耗/毫秒开销的报告格式,是 T5 基线③的现成对照协议 [D6 卡 3]。

---

## 品味判断(S01 初评)

- **新颖性分布**:DSL 表面语法(低——本质是数据库/主动系统领域的 Event-Condition-Action 规则范式移植到 agent 回路,论文未提 ECA [个人分析])< enforcement 的轨迹变换算子语义(中,把 Reflexion 变成 enforcement 原语是巧手)< 问题定位"可定制运行时强制"+三域工程验证+毫秒开销论证(高)。
- **核心价值**:把"agent 安全"从模型问题改述为**软件工程问题**——找对拦截点(iter_next_step),给出规则语言与四个干预原语,用开销数据完成工业可用性论证。方法平,选址准。
- **天花板**:反应式 + 谓词手工性。天花板由同组 ProbGuard 接棒(概率前瞻),谓词工程一侧由 ShieldAgent 类"政策→规则"自动化路线补(D6 卡 4)。

---

## S02 跟进问题(留待骨架/精读/复现窗)

1. Figure 8 的域动作 enforce(follow_dist(10) 等)在语法上如何归入 Enforce 四选一?invoke_action 的语法糖?〔08-22 已销:master 分支 AgentSpec.g4 有独立规则 actionInvoke,非语法糖;g4 另含论文未列的 none/skip 档与 llm_self_reflect 命名漂移,详见 03 §L7-3〕
2. 多条规则同时违规时的施加次序与冲突语义,Def 只说"each violated rule applies"——未定义。
3. state_change 的状态相等判定(sᵢ ≠ sᵢ₋₁)在 LangChain 三拦截点上具体如何实现?
4. #pass 列的 user inspection 由作者扮演,判定标准与盲评协议的实际执行细节?(threats 节只有一句)
5. AV 域 DSL→μDrive 脚本的翻译器(`spec_lang/translator` [D6])覆盖 DSL 的哪个子集?

---

## Critical Thinking 审计

- Q1 审计:"第一个运行时强制框架"在三限定词下成立;但 runtime enforcement 在传统软件领域是成熟方向(§7 自引 Falcone 等),新颖性在"移植到 LLM agent"而非概念本身。
- Q2 审计:"DSL 薄、谓词厚"的判断有原文支撑(Figure 3 语法 + §4 谓词实现);由此推出的"可验证性受限于 Python 层"是我的延伸 [个人分析]。
- Q3 审计:"无定理"经全文核对属实;注意别把 §3.3 的算子定义误称为"证明了安全性"。
- Q4 审计:指标异构的观察直接来自 Table 3/4/5/6 的列定义,可靠。
- Q5 审计:ProbGuard 依赖关系来自 D6 仓库实见(非本论文内容),引用时须区分出处。
