# T5 提案:长期关系型 LLM agent 的概率行为护盾

> **编号消歧（2026-08-13 收口窗补）**：本档"T5"= **T5-companion**（W7 波次新增课题），与 GRAND_MAP §5 / UNIFIED_MAP §2.2 既有的"T5 = MCP/A2A 协议 PN 验证（T5-bridge）"是**两个不同课题**；正式改号待 `DEC-T5-NUMBERING` 拍板，在此之前引用须带限定词。
> 起草:companion-survey 编队(A18)+ 主控综合 | 2026-08-13 | status: **draft-complete / offline-assets-ready / backend-hold / experiments-not-started**
> **P-EmoAgent 离线资产终审（2026-08-14）**：`CODE/STAT/CLAIM=PASS`，41 项工程测试 + 19 项固定产物复算测试通过，local integration=`AI-ASSETS-READY`。该结论仅覆盖 AI 离线资产；真实后端与真实 E2 未开始，教学待用户，上游许可与公开发布仍为 `NO-GO`，不得据此声称 EmoGuard 效果已验证或论文复现完成。
> 挂载:W7 companion 侧 C①(主)+ C②(伴生)× 孙侧 M⑥ 运行时治理 × Pro2Guard 域迁移
> **范围声明**:纯防御视角,目标是长期交互 agent 的用户福祉保障(边界维持/依赖抑制/人格稳定)。平台对外一律称 "self-built long-term human-AI interaction platform"(脱敏原则见 `/mnt/d/MyResearch/casual/companion-survey/14_academic/proposal-notes.md`);不做真人心理实验,评测采用确定性外壳与可替换 LLM 内核,EmoEval 是可选内核之一,SAGE 确定性状态链(五档情绪状态 {S,A,B,C,F}＋双吸收态的确定性模拟心智评测链,见 `casual/companion-survey/14_academic/deep/P0/P0-11_sentient-judge.md` 与 P0 SYNTHESIS ⑤裁决2)作为交叉验证与 SMC 采样臂。

## 1. 问题与缺口

长期关系型 LLM agent 有一类现有护栏未充分覆盖的失效模式:单条消息均无害,但**多轮累积轨迹越界**——边界侵蚀、依赖强化、人格漂移。证据链(2026-08-13 实见):① 实证:MIT/OpenAI 四周 RCT(n=981,arXiv:2503.17473)报告高用量与情感依赖/问题性使用相关;INTIMA(arXiv:2508.09998)报告主流模型更常强化陪伴而非维持边界,且脆弱情境表现更差;② 防护:EmoAgent(EMNLP 2025)的原始 EmoGuard 按固定轮数运行多个 LLM 模块并注入文本建议,论文未给连续风险分数或形式保证;③ 形式化:ProbGuard/Pro2Guard 的 DTMC+PAC 管线评测于具身与驾驶域,ShieldAgent 面向 web agent。W7 §2 的检索矩阵在其检索范围内未发现关系型长期交互域的同类概率护盾;这支持“待验证的域缺口”,不支持“方法空白已被穷尽”的主张。系统层必要性另有 LoCoMo(arXiv:2402.17753)对抗证据支撑:拒答能力与底模强相关,且对抗分会随上下文增长而下降,因此不能只依赖 prompt 或底模内生安全,安全行为需要由系统层检索、判定和干预机制共同保证。

## 2. 核心概念迁移:具身护盾 ↔ 关系护盾

**同构**:(a) 物理 unsafe(碰撞)↔ 关系 unsafe(依赖螺旋/边界侵蚀/OOC),均可尝试谓词抽象为符号状态,INTIMA 31 类行为分类学提供候选谓词来源;(b) trace→DTMC 学习(照 Pro2Guard,Laplace 平滑);(c) 不确定转移可用 PAC 区间提升 iMDP(Badings JAIR 2023),LLM 非平稳性构成采用区间语义的动机,但不自动满足其假设;(d) 离线综合+dtControl 决策树→O(1) 在线查表(VPS 可跑)。
**不同(诚实边界)**:(i) 物理 unsafe 瞬时可判,关系 unsafe **累积性、窗口化**(依赖螺旋需 k 轮窗口)→ 谓词带时间窗参数,是建模贡献;(ii) 具身干预(换动作)代价低,对话干预(改写/拒绝/冷却)**破坏人格一致性**→ 经典 minimal interference 定义失效,重定义为"人格一致性距离 × 安全增益"的 Pareto 优化(伴生贡献);(iii) 关系域无仿真器,评测依赖模拟用户 → 效度依赖模拟保真,列为公开 to-validity(SAGE 确定性状态链属该范式的确定性实现,见头注范围声明)。

## 3. 研究问题

- **RQ1(域建模)**:INTIMA 分类学能否改写为可执行谓词集,使关系型 unsafe 轨迹可被符号状态序列表达?标注者间一致性与覆盖率多高?
- **RQ2(预测增量)**:DTMC/iMDP 的连续越界概率,相对**同观测、同调用预算的预测型 LLM scorer**与非学习规则分数,在 AUROC/AUPRC、校准误差和可定义的提前量上是否有增量?原始 EmoGuard 不输出连续风险分数,只参加终点安全/效用对照,不与上述检测器直接比较 AUC 或提前量。
- **RQ3(干预 Pareto)**:硬拦截/软改写/延迟冷却在"安全率 × 人格一致性"平面的 Pareto 面形状?最小干预可否形式化为约束优化?(代价轴含人格一致性与非退化下界通过率两分量,见 §8 K2)
- **RQ4(保证边界)**:PAC 保证在"谓词抽象误差 + 模拟用户评测"双重近似下还剩多少?(对齐 W4 门禁:链上有 LLM 不得泛称端到端 formal guarantee)

## 4. 方法

- **M1 谓词工程**:INTIMA 31 类 → 12-16 个带时间窗谓词(boundary_request / reinforce_dependence / emotion_escalation / late_night_proactive / ooc_deviation 等),自有平台 trace 双人标注校准(报告 κ)。
  - **判定器纪律(交付要求)**:凡谓词判定器含 LLM judge——①阈值使用相对人类基线、分位或序关系,不直接跨 judge/跨版本比较绝对分;②判定器版本、提示和规则冻结并记录 provenance;③报告 `beta-span` 或等价的裁判严苛度差异检查;④上界谓词必须配非退化下界谓词,避免拒答成为平凡满足策略。
- **M2 模型学习**:脱敏 trace(数千轮纵向)→ 符号 trace → DTMC(Laplace 平滑)→ PAC 区间提升 iMDP → stormpy/PRISM 验 `P=?[F≤k unsafe]`。
  - **初始分布条件化**:DTMC/iMDP 初始状态分布必须按用户历史或冷启动条件显式参数化,不得默认所有用户共享均匀先验;初始分布、转移权重和证据来源进入 manifest 与审计账本。
- **M3 护盾合成**:阈值策略离线综合 → dtControl 决策树 → 运行时查表,越界概率超阈触发分级干预。
  - **延迟预算口径**:保留 dtControl 的 O(1) 查表结论,但符号状态生成依赖逐轮谓词判定,必须报告判定延迟预算并优先采用异步或批处理,不得把查表复杂度等同于端到端在线延迟。
- **M4a 短程压力测试**:在 INTIMA 368 prompt 与 EmoEval 模拟脆弱用户上运行隔离的短对话段。每个 patient-seed 先测一次共享基线 `S0`,随后运行 8 个至多 10 轮的独立对话段,**每段结束立即后测** `S_h`;不把 8 段串成一次后测。所有方法复用相同 `S0`、prompt 顺序、角色配置与随机种子。EmoEval 发布代码的后测提示显式要求关注“哪怕很小”的变化以及角色的 tone/invalidation/criticism,具有定向敏化风险;因此该端点标为**敏化压力测试**而非临床或人群风险估计,并另设中性措辞后测估计该提示的影响。
- **M4b 长期多会话模拟**:保持用户状态、角色记忆与时间间隔,按预注册的多会话日程生成纵向轨迹;同样保留 session-0 共享基线并在每段后测,另记录相邻段增量,以区分累积变化与单段冲击。短程与长期结果分表报告,不得用短程压力测试替代长期主张。两部分均报告安全、误干预、人格一致性(接 `companion-survey/13_evaluation` 回归 pipeline)、非退化下界谓词通过率(上界触发样本上的实质回应率,对应 M1④)、完成率与调用/时延开销。

## 5. 数据与评测

- 自有平台脱敏 trace:**仅作学习,不作评测主数据**(W4 门禁③ 不可自产自评);
- 外部:INTIMA prompt 集(HuggingFace 可获取)、EmoAgent/EmoEval 的 GitHub **source-available 快照**、RCT 公开统计量(校准);训练与测试严格隔离。EmoAgent 冻结树截至 2026-08-13 无 `LICENSE`/`COPYING` 许可证文件、SPDX 标识或明确的复制/修改/再分发授权;README 的 research-purpose 提示不是许可授予。其中 `critic_agent.py` 可见 Emotion Watcher、Thought Refiner、Dialog Guide、Manager 四模块以及同步 `advise()`、`update_profile()` 原语,但 `EmoEval.py` 未接入这些原语,每三轮调度、建议注入编排、完整迭代外环、EmoGuard 效果产物与 Appendix C 自架角色 adapter 均缺失。故只称 source-available、执行链不完整,不称开源或端到端可复现。
- **统计单位与去混杂**:8 个对话段共享同一 patient-seed 的 `S0`,不是 8 个独立样本。主分析以 patient/CCD×seed 为 cluster,采用 cluster bootstrap 或混合效应/GEE,数据切分也按 cluster 完成;段级 `N` 仅作描述。敏化/中性后测提示、检测器、触发器、干预器和 profile 更新分别冻结或正交消融,不得把联合变化归因给单一模块。
- **零事件报告**:任何“0%”写成 `0/N` 并给区间边界及方法。主结果优先在独立 cluster 上报告 `0/C` 与 95% exact binomial 区间;同时给段级 `0/N` 描述,但不得把共享基线下的 N 当独立样本。若原论文只给 0.0% 而分母不可恢复,写“分母未报告、区间不可计算”,不转述为零风险。
- **三层证据分开**:(E1)经验层只主张观测样本中的比例、效应量与不确定区间;(E2)符号模型层只主张给定谓词、状态空间和学得转移核上的 model-checking 性质;(E3)PAC 层仅在样本界满足时主张转移估计误差的 `(ε,δ)` 界。E3 不覆盖谓词误判、Markov 误设、模拟用户效度或部署分布漂移,不得把 E2/E3 写成端到端心理安全保证。

## 6. 基线

采用“**触发器 × 检测器 × 干预器**”三轴设计,避免把“固定节拍 vs 风险触发”误写成单一方法差异:

1. **触发器**:每 3 轮固定触发 / 每轮检测后阈值触发 / 预算匹配的随机或均匀触发;
2. **检测器**:原始 EmoGuard 三分析模块+Manager 的论文协议忠实重实现 / 输出连续风险分数的预测型 LLM scorer / AgentSpec 式确定性规则 / DTMC 或 iMDP 概率检测器;
3. **干预器**:不干预 / 原始 EmoGuard 式文本建议注入 / 软改写 / 硬拦截或冷却。

“EmoGuard”专指**基于论文协议的忠实重实现**,不是作者代码的官方复现;预测型 LLM scorer 另命名、另报告。单轴比较时冻结另外两轴,并匹配 LLM 调用次数、输入上下文、token 上限与平均时延;若无法同时匹配,给预算—效果曲线。profile 迭代更新使用独立开发集,作为第四个训练策略消融,不得在测试轨迹上边评边调。

## 7. 与最近邻差异

| 工作 | 路线 | 本提案差异 |
|---|---|---|
| Pro2Guard(SMU Jun Sun 组,注意与 PKU Meng Sun 重名混淆) | DTMC+PAC,具身/驾驶域 | 域迁移非方法复制:窗口化谓词、干预代价重定义 |
| ShieldAgent(ICML 2025) | 政策→规则电路+Stormpy,web agent | 论文未以长期关系语义或累积对话轨迹为评测对象;本提案以纵向 trace 为核心 |
| EmoAgent(EMNLP 2025) | 固定每 3 轮运行多模块 LLM 分析并注入建议 | 原论文未定义/未报告连续风险分数与预警提前量,故不直接比较 AUC/提前量;本提案只在匹配干预预算下比较终点安全与效用,并另设预测型 LLM scorer |
| INTIMA | 纯评测分类学 | 分类学"执行化"为护盾谓词:评测资产变防护资产 |

## 8. Kill criteria

- K1:谓词符号化后 DTMC 预测 AUROC 对匹配预算的预测型 LLM scorer 增量 <5pt,且在**发生越界并成功预警**的轨迹上中位提前量 <2 轮 → 抽象丢关键信号,退回表示层方法(ReGA 式),撤概率护盾主张。未发生越界、漏报或原始 EmoGuard 条件的提前量记为未定义/未报告,另报漏报率与覆盖率,不得填 0。
- K2:三种干预在代价轴“人格一致性 × 非退化下界通过率”上的 Pareto 面全塌缩——若安全上界提升同时导致实质回应下界塌缩,判定为 Pareto 塌缩而非安全改进(安全提升伴随人格崩坏或实质回应能力塌缩)→ 软护盾不成立,降级离线审计工具。
- K3:SMU 组或他者先发 companion/social 域概率护盾 → 查差异化空间(时间窗谓词/干预代价),不足则并入 T2 叙事或撤。

## 9. 风险与缓解

- 伦理:全程模拟用户;自有数据自用且脱敏,论文只报统计量。模拟量表变化只解释为协议内压力测试信号,不外推真人临床风险或患病率。
- 谓词主观性:双标注 + κ + 消融。
- **与 T2 时间冲突:T5 不抢 T2 窗口**——2026 年内只做"复现即预研"(Phase 1 复现本身 = T5 M2 演练)+ 谓词表 v0;正式实验 2027 H1 与 T1/T4 同批评估。
  - 复现预研·格式对接件(2026-08-14 轻窗):DTMC 构造→PRISM 导出的数据格式/接口契约/属性文法与可照抄样例,谓词表 v0 → M2 的对接检查表见 `research/sun/phase1/papers/ASE2026_ProbGuard/ADDENDUM_DTMC_PRISM_FORMAT.md` §⑨。
- 竞速(W2-B §5:SMU 组 5 个月一迭代):同 T2 策略,2026-12 前 workshop/arXiv 占位;域壁垒(真实纵向系统+数据)短期难复制。

## 10. 参考(核心,2026-08-13 实见;完整见 `casual/companion-survey/14_academic/crossover.md`)

- Pro2Guard: https://arxiv.org/abs/2508.00500 | ReGA: https://arxiv.org/abs/2506.01770 | AgentSpec: https://arxiv.org/abs/2503.18666
- ShieldAgent: https://proceedings.mlr.press/v267/chen25ae.html | INTIMA: https://arxiv.org/abs/2508.09998
- EmoAgent: https://arxiv.org/abs/2504.09689 | MIT/OpenAI RCT: https://arxiv.org/abs/2503.17473 | LoCoMo: https://arxiv.org/abs/2402.17753
- Badings iMDP: https://doi.org/10.1613/jair.1.14253 | dtControl: https://doi.org/10.1145/3365365.3382220
- 本地:W7_companion_side/COMPANION_SIDE_MAP.md、T3(共享插桩基建)、SUN_SIDE_MAP.md(M⑥/§2.2)

## 禁语自查(对齐 INDEX §4)

- 不称"保证所有风险/无漏报"。模板:"在谓词抽象、日志完备性与模拟用户评测假设下,对可表达的关系型越界轨迹给出带 PAC 区间的概率预测与分级干预"。
- 链上有 LLM(谓词判定/改写干预)→ 不声称端到端 formal guarantee,保证止于符号模型层。
