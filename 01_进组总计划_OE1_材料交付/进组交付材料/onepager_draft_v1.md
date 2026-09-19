# 对外一页纸 Research Statement — onepager_draft_v1

> **v1 初稿,待用户定声音,严禁未经用户确认外发。**
> 起草:2026-08-13 | 用途:下月进组的对外自我介绍一页纸(可按受众微调后用于其他对外场合)
> 素材:`casual/companion-survey/14_academic/proposal-notes.md`(主)、`T5_companion_prob_shield.md`、`INDEX.md` §1/§1b/§4、`FOCUS.md` 重心 2;语气参考 `OE1_lu_email_v4.md`(踏实、量化真实、宁少勿虚)

---

## 撰写说明(简体中文,外发前删除本节)

1. **声音未定**:v1 采用"踏实学生 + 有备而来"的混合声。可调方向:(a) 更谦逊(弱化"资产"措辞,强化"请教");(b) 更研究者(RQ 化,加引文编号);(c) 更工程(突出三件套细节)。待用户拍板后出 v2。
2. **占位符清单(发前必填)**:[姓名]、[学校]、[专业]、[身份表述](**本科生,2026-09 进组时为大三**;考研 2027-12,读研 2028 起——对外身份一律按"undergraduate researcher/本科生"口径,勿写成研究生)、[课题组/实验室名]、[联系方式]。(身份勘误 2026-08-13:用户为本科生)
3. **脱敏自查(已过)**:全文对自有系统只用"自建长期人机交互平台 / self-built long-term human-AI interaction platform";全文无"人机恋/AI 伴侣/角色扮演"字样;数据一律"经脱敏的(纵向)交互日志"。
4. **禁语自查(INDEX §4 + T5 禁语节,已过)**:无"全球唯一/保证所有风险/无漏报/证明 agent 系统安全";域空白表述带检索时点限定("在 2026 年 8 月的调研中未见");明确写"不声称端到端形式保证,保证止于符号模型层"。
5. **人名警示**:正文刻意不写任何作者人名。若口头被追问:ProbGuard(原 Pro2Guard)出自 SMU **Jun Sun** 组;与 PKU **Meng Sun** 是两个人,严禁混淆(实验室档案已专门警示)。
6. **名称口径(2026-08-13 核实更新,见 factcheck_onepager_20260813.md)**:arXiv:2508.00500 论文已更名 **ProbGuard** 并获 ASE 2026;对外以 ProbGuard 为主名,首次出现括注"(原名 Pro2Guard,ASE 2026,arXiv:2508.00500)",此后直接写 ProbGuard;官方代码仓库仍名 Pro2Guard(口头可补充说明)。
7. **量化数字来源(2026-08-13 实测,外发前请用户确认愿意公开)**:
   - EvoAgent:44 个 Python 文件约 8,800 行、43 个单元测试(本仓统计,不含 .git/output);XES/GraphML 双出口经 PM4Py/networkx 读取验证——按 039 波审计(Gate R0 FAIL),**只可表述为互操作事实,不得表述为实验/研究结果**,正文已按此措辞。
   - 平台:"持续运行数月、数千轮纵向日志"沿用 proposal-notes/T5 既定口径,未虚构精确数。
   - MindBridge:2,400 条 = `psychqa_synthetic.jsonl` 实数;Qwen2.5-7B + q4_k_m GGUF(约 4.7 GB)为模型文件实况;事件驱动 5-agent 协作 runtime 为 README 实况。
8. **伦理表述**:近期计划中已写明"不做真人实验、评测用模拟用户;自有数据仅作模型学习、不作评测主数据"(对齐 T5 §5 与 W4 门禁③)。
9. **待用户确认**:①声音方向;②占位符;③备选方向一句是否保留;④量化数字是否对外;⑤英文版是否需要进一步润色。
10. **信息更新(2026-08-13 晚,用户口头确认,已落正文)**:①复现顺序改为 **ReGA 先行**,ProbGuard 官方仓库实拆确认处于半完成重构、暂不可整仓跑通,对外措辞为"官方代码仓库现处重构中,改以论文与代码对照的定向精读跟进";②**谓词表 v0 已完成**(INTIMA 分类学 → 16 个带时间窗可执行谓词),计划段由"12–16 个(计划)"改为"16 个(已完成)",双人标注/κ/trace 导出/最小闭环仍为计划项。三声音版(中英)已同步。

---

## 中文版(正文约 780 字,一页 A4 当量)

# Research Statement · [姓名]

**一、身份定位。** 我是[学校][专业]的[身份表述],将于 2026 年 9 月进入[课题组]学习与研究。我的方向是 LLM agent 运行时安全与形式化方法的交叉:用概率模型检验为长期运行的交互 agent 构建可量化的行为护栏。与常见的"再搭一个模拟环境"路径不同,我带来的是一个自建并持续运营的长期人机交互平台——真实运行、有真实用户、沉淀了数月纵向交互数据,可直接充当运行时护盾方法的新应用域与试验台。

**二、已有工作(三件套)。**
- **EvoAgent**:自进化 PR 审查多智能体平台(约 8,800 行 Python、43 个单元测试),含 harness 生命周期管理、LangGraph 编排与评测门禁下的提示词进化闭环;已实现 agent 轨迹到 XES 1.0 事件日志与 GraphML 交互图的同源双出口,经 PM4Py 与 networkx 读取验证。
- **自建长期人机交互平台**(FastAPI):向量记忆管线、显式情绪状态引擎、定时主动行为、WebSocket 多端同步;持续运行数月,沉淀数千轮经脱敏的纵向交互日志,为轨迹级安全研究提供了难得的真实数据来源。
- **MindBridge**:校园心理支持多智能体系统;基于 Qwen2.5-7B 以 2,400 条合成心理问答指令微调,量化为 q4_k_m GGUF 经 Ollama 本地部署;事件驱动 5-agent 协作 runtime,动态路由混合检索(向量 + BM25),含 Recall@K/MRR/NDCG 评测。

**三、研究兴趣。** 主线是**面向长期人机交互 agent 的概率行为护盾**。问题:这类 agent 存在现有护栏未覆盖的失效模式——单条消息均无害,但多轮累积轨迹越界(边界侵蚀、依赖强化、人格漂移);实证研究(INTIMA;MIT/OpenAI 四周 RCT)已确认风险普遍,而现有防护以 prompt 规则与 LLM-judge 为主,缺乏量化承诺。方法:把交互状态谓词抽象为符号状态,从执行 trace 学习 DTMC、以 PAC 区间提升为 iMDP,离线综合干预策略并压缩为决策树,运行时 O(1) 查表、越界概率超阈值时分级干预(改写/冷却/降级);在谓词抽象、日志完备性与模拟用户评测的明确假设下,对可表达的越界轨迹给出带 PAC 区间的概率预测——不声称端到端形式保证。为什么是我:现有概率护盾工作(ProbGuard,原名 Pro2Guard、ASE 2026;ShieldAgent)的评测域集中在具身、自动驾驶与 web 场景,在我 2026 年 8 月的调研中未见长期交互域带概率保证的同类护盾工作,而该域的第一道门槛——长程真实 trace——恰是我平台的既有资产。备选方向(同一平台资产):情绪-人格状态机的概率模型检验与运行时 monitor 合成;主动调度与多端同步的并发正确性(TLA+)。

**四、近期计划(2026.09–12)。** ① 复现打底(9–10 月):跑通 ReGA 的公开实现,输出一页复现简报;ProbGuard 官方代码仓库现处重构中,改以论文与代码对照的定向精读跟进——两者与主线方法同构,复现与精读即是预研;② 域建模(10–11 月):谓词表 v0 已完成——INTIMA 行为分类学已改写为 16 个带时间窗的可执行谓词;下一步做双人标注并报告一致性 κ,从平台导出脱敏 trace,跑通"符号 trace → DTMC → 越界概率验证"最小闭环;③ 12 月前:整理为 workshop/arXiv 短文占位。伦理边界:不做真人实验,评测采用模拟用户范式;自有数据仅用于模型学习,不作评测主数据。

---

## English Version (~one A4 page)

# Research Statement · [Name]

**Who I am.** I am a [status] in [major] at [university], joining [lab] in September 2026. My research direction sits at the intersection of runtime safety for LLM agents and formal methods: using probabilistic model checking to build quantifiable behavioral guardrails for long-running interactive agents. Rather than building yet another simulated environment, I bring a self-built long-term human-AI interaction platform — actually deployed, with real users and months of longitudinal interaction data — which can serve as both a new application domain and a testbed for runtime shielding methods.

**Selected work.**
- **EvoAgent**: a self-evolving multi-agent pull-request review platform (~8,800 lines of Python, 43 unit tests) with harness-managed task lifecycle, LangGraph orchestration, and an evaluation-gated prompt-evolution loop; implemented dual export of agent traces into XES 1.0 event logs and GraphML interaction graphs from the same evidence space, validated by loading with PM4Py and networkx.
- **A self-built long-term human-AI interaction platform** (FastAPI): vector-memory pipeline, explicit affective-state engine, scheduled proactive behavior, and WebSocket multi-device sync; months of continuous operation have accumulated thousands of turns of anonymized longitudinal interaction logs — a rare source of real data for trajectory-level safety research.
- **MindBridge**: a campus mental-health support multi-agent system; fine-tuned Qwen2.5-7B on 2,400 synthetic counseling QA instructions, quantized to a q4_k_m GGUF and served locally via Ollama; event-driven five-agent collaboration runtime with dynamically routed hybrid retrieval (vector + BM25), evaluated with Recall@K, MRR, and NDCG.

**Research interests.** My main thread is **probabilistic behavior shields for long-term human-AI interaction agents**. Problem: such agents exhibit a failure mode that existing guardrails do not cover — every single message looks harmless, yet the accumulated multi-turn trajectory drifts out of bounds (boundary erosion, dependence reinforcement, persona drift); empirical studies (INTIMA; the MIT/OpenAI four-week RCT) confirm these risks are common, while current defenses rely on prompt rules or LLM judges with no quantitative commitment. Approach: abstract interaction states into symbolic states via predicates, learn a DTMC from execution traces, lift it to an iMDP with PAC intervals, synthesize intervention policies offline and compress them into decision trees for O(1) runtime lookup, triggering graded interventions (rewrite / cool-down / de-escalation) when the predicted out-of-bound probability exceeds a threshold; under explicit assumptions on predicate abstraction, log completeness, and simulated-user evaluation, this yields PAC-interval probabilistic predictions for expressible out-of-bound trajectories — no end-to-end formal guarantee is claimed. Why me: existing shield pipelines (ProbGuard, formerly Pro2Guard — ASE 2026; ShieldAgent) are evaluated in embodied, autonomous-driving, and web domains, and as of my August 2026 survey I found no comparable probabilistic-shielding work in the long-term interaction domain — whose first barrier, long-horizon real traces, is precisely what my platform already provides. Secondary directions on the same platform: probabilistic model checking of the affective/persona state machine with runtime monitor synthesis; concurrency correctness of proactive scheduling and multi-device sync (TLA+).

**Near-term plan (Sep–Dec 2026).** (1) Reproduction first (Sep–Oct): run the public implementation of ReGA and deliver a one-page reproduction brief; the official ProbGuard repository is currently mid-refactor, so I will track it through a targeted paper-and-code reading — both are methodologically isomorphic to the main thread, so reproduction and close reading double as pilot work. (2) Domain modeling (Oct–Nov): predicate table v0 is complete — the INTIMA behavior taxonomy has been rewritten into 16 executable predicates with time windows; next, dual annotation (reporting κ), export anonymized traces from my platform, and close the minimal loop "symbolic trace → DTMC → out-of-bound probability checking". (3) Before December: consolidate into a workshop/arXiv short paper for positioning. Ethics: no human-subject experiments — evaluation uses simulated users; my own data is used for model learning only, never as primary evaluation data.
