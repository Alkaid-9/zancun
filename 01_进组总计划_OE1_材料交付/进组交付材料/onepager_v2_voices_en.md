# 对外一页纸 Research Statement(英文三声音版)— onepager_v2_voices_en

> **草稿,严禁未经用户确认外发。**
> 日期:2026-08-13 | 起草者:A2(并行文档波)
> 基线:`onepager_draft_v1.md` 英文版(事实与数字全部冻结,只改语气与组织);素材:`casual/companion-survey/14_academic/proposal-notes.md`(Pitch 1 主线);禁语与门禁:`INDEX.md` §4。
> 占位符 [Name] / [university] / [major] / [status] / [lab] 全文保持原样,发前必填;**[status] 一律按"本科生(2026-09 进组时大三)"口径填写,严禁写成研究生**。
> 三版共同红线(已逐一自查):XES/GraphML 双出口只作互操作事实陈述;域空白表述带"2026 年 8 月调研"时点限定;三版均保留"不声称端到端形式保证"与伦理句;正文无任何作者人名。
> 名称口径(2026-08-13 核实,见 factcheck_onepager_20260813.md):arXiv:2508.00500 已更名 **ProbGuard**(ASE 2026);各版首次出现处括注 "formerly Pro2Guard",此后直写 ProbGuard;代码仓库仍名 Pro2Guard。
> 信息更新(2026-08-13 晚,用户口头确认,三版已同步):①复现顺序 **ReGA 先行**,ProbGuard 仓库 mid-refactor 改定向精读;②**谓词表 v0 已完成**(INTIMA → 16 个带时间窗谓词),计划段写完成时,双人标注/κ/trace/最小闭环仍为计划。

## 对比导读(三声音一览)

| 声音 | 核心差异 | 首句示例 | 适用场合 |
|---|---|---|---|
| **A 谦逊版** | 弱化"资产/我带来"措辞,突出"学习、请教、在指导下做事";事实密度不减,不卑不亢 | "I am a [status] in [major] at [university], and I will join [lab] in September 2026. … my first goal is to learn the group's methods properly." | 首次接触、邮件附件、对方尚不了解本人时 |
| **B 研究者版** | 研究兴趣改写为 RQ1/RQ2(+RQ3),正文加编号引文 [1]–[8],文末附紧凑参考文献(参考文献不列作者人名,以免口径失误);正文相应精简以保一页 | "I work at the intersection of runtime safety for LLM agents and probabilistic formal methods, with one empirical advantage …" | 学术读者、组会分发、随正式申请/套磁材料 |
| **C 工程版** | 三件套细节前置加厚(技术栈/架构决策/量化事实),研究兴趣压缩为"问题 + 我的切入";人设是"能交付、能长期运维的建造者" | "I build and operate agent systems end to end — and I keep them running after the demo." | 偏工程/系统背景的读者,或需快速证明执行力的场合 |

---

## Voice A — 谦逊版(英文全文)

# Research Statement · [Name]

**Who I am.** I am a [status] in [major] at [university], and I will join [lab] in September 2026. I am an undergraduate, still early in my research training, and my first goal is to learn the group's methods properly — probabilistic model checking, runtime shielding, and the discipline of honest evaluation — and to contribute usefully under supervision. The direction I hope to grow into sits at the intersection of runtime safety for LLM agents and formal methods: quantifiable behavioral guardrails for long-running interactive agents. One thing I can offer from day one is a self-built long-term human-AI interaction platform that has been in continuous operation for months; with the group's guidance, I hope it can serve as an application domain and a testbed for runtime shielding methods.

**Selected work.** These are student projects, but I built each of them end to end and still maintain them, and they taught me the engineering this direction needs.

- **EvoAgent** — a self-evolving multi-agent pull-request review platform (~8,800 lines of Python, 43 unit tests), with harness-managed task lifecycle, LangGraph orchestration, and an evaluation-gated prompt-evolution loop. I implemented dual export of agent traces into XES 1.0 event logs and GraphML interaction graphs; both load correctly with PM4Py and networkx. I state this as an interoperability fact, not as a research result.
- **A self-built long-term human-AI interaction platform** (FastAPI) — vector-memory pipeline, explicit affective-state engine, scheduled proactive behavior, and WebSocket multi-device sync. Months of continuous operation have accumulated thousands of turns of anonymized longitudinal interaction logs.
- **MindBridge** — a campus mental-health support multi-agent system. I fine-tuned Qwen2.5-7B on 2,400 synthetic counseling QA instructions, quantized it to a q4_k_m GGUF served locally via Ollama, and built an event-driven five-agent runtime with hybrid retrieval (vector + BM25), evaluated with Recall@K, MRR, and NDCG.

**Research interests.** The problem I keep returning to: long-running interactive agents can fail in a way current guardrails do not cover — every single message looks harmless, yet the accumulated multi-turn trajectory drifts out of bounds (boundary erosion, dependence reinforcement, persona drift). Empirical studies (INTIMA; the MIT/OpenAI four-week RCT) indicate these risks are common, while deployed defenses remain prompt rules or LLM judges without quantitative commitments. From my reading of ProbGuard (formerly Pro2Guard; ASE 2026), ReGA, and ShieldAgent, I believe the group's pipeline fits this problem: abstract interaction states into symbolic states via predicates, learn a DTMC from execution traces, lift it to an iMDP with PAC intervals, synthesize intervention policies offline, and compress them into decision trees for O(1) runtime lookup with graded interventions (rewrite / cool-down / de-escalation). I want to state the limits carefully: under explicit assumptions on predicate abstraction, log completeness, and simulated-user evaluation, this yields PAC-interval probabilistic predictions for expressible out-of-bound trajectories — no end-to-end formal guarantee is claimed. As of my August 2026 survey I found no comparable probabilistic-shielding work in the long-term interaction domain (existing shield pipelines are evaluated in embodied, autonomous-driving, and web settings) — I may well have missed something, and I would welcome pointers — but if the gap is real, the domain's first barrier, long-horizon real traces, is something my platform can already supply.

**Near-term plan (Sep–Dec 2026).** (1) Sep–Oct: reproduce the public implementation of ReGA and write a one-page reproduction brief; I have read through the official ProbGuard repository — it is currently mid-refactor and not yet runnable end to end — so I plan to follow that work through a targeted paper-and-code reading instead. Reproduction and close reading are how I intend to learn the pipeline, and both works are methodologically close to the direction above. (2) Oct–Nov: I have drafted predicate table v0 — the INTIMA behavior taxonomy rewritten into 16 executable predicates with time windows; next, with feedback from the group, complete dual annotation (reporting κ), export anonymized traces from my platform, and attempt the minimal loop "symbolic trace → DTMC → out-of-bound probability checking". (3) Before December: if the results merit it, consolidate them into a workshop/arXiv short note under the group's direction. Ethics: no human-subject experiments — evaluation uses simulated users; my own platform data is used for model learning only, never as primary evaluation data.

(Contact: [contact])

---

## Voice B — 研究者版(英文全文,含参考文献)

# Research Statement · [Name]

**Who I am.** I am a [status] in [major] at [university], joining [lab] in September 2026. I work at the intersection of runtime safety for LLM agents and probabilistic formal methods, with one empirical advantage: a self-built long-term human-AI interaction platform in continuous operation for months, yielding anonymized longitudinal traces of exactly the kind that trajectory-level safety research lacks.

**Selected work.**

- **EvoAgent** — a self-evolving multi-agent pull-request review platform (~8,800 lines of Python, 43 unit tests): harness-managed task lifecycle, LangGraph orchestration, evaluation-gated prompt evolution; dual export of agent traces to XES 1.0 event logs and GraphML interaction graphs, loadable with PM4Py and networkx (an interoperability fact, not an experimental result).
- **A self-built long-term human-AI interaction platform** (FastAPI) — vector-memory pipeline, explicit affective-state engine, scheduled proactive behavior, WebSocket multi-device sync; months of continuous operation, thousands of turns of anonymized longitudinal logs.
- **MindBridge** — a campus mental-health support multi-agent system: Qwen2.5-7B fine-tuned on 2,400 synthetic counseling QA instructions, quantized to q4_k_m GGUF and served locally via Ollama; event-driven five-agent runtime; hybrid retrieval (vector + BM25) evaluated with Recall@K, MRR, and NDCG.

**Research interests.** Long-running interactive agents exhibit a failure mode outside the scope of message-level guardrails: individually innocuous turns accumulate into an out-of-bound trajectory — boundary erosion, dependence reinforcement, persona drift. Empirical studies document the risk at scale [1, 2], while deployed defenses remain prompt rules or LLM judges without quantitative commitments [3]. My main thread is **probabilistic behavior shields for long-term human-AI interaction agents**, organized around three questions:

- **RQ1 (domain modeling).** I have rewritten the INTIMA taxonomy [1] (31 behaviors) into **16 executable, time-windowed predicates** (predicate table v0); can this predicate set express out-of-bound trajectories in this domain as symbolic state sequences with acceptable annotation agreement (κ) and coverage?
- **RQ2 (prediction gain).** Does out-of-bound probability prediction — a DTMC learned from execution traces [4], lifted to an iMDP with PAC intervals [6] — deliver a significant gain in lead time (turns) and AUC over LLM-judge [3] and prompt-only baselines?
- **RQ3 (intervention trade-off, optional).** What Pareto shape do graded interventions (rewrite / cool-down / de-escalation), synthesized offline and compressed into decision trees [7], exhibit on the safety × persona-consistency plane?

*Scope and positioning.* Under explicit assumptions on predicate abstraction, log completeness, and simulated-user evaluation, the approach yields PAC-interval probabilistic predictions for expressible out-of-bound trajectories; the execution chain contains an LLM, so no end-to-end formal guarantee is claimed — the guarantee stops at the symbolic model layer. Existing shield pipelines are evaluated in embodied and autonomous-driving domains [4] and on web tasks [5]; as of my August 2026 survey I found no comparable probabilistic-shielding work in the long-term interaction domain, whose first barrier — long-horizon real traces — my platform already provides.

**Near-term plan (Sep–Dec 2026).** (1) Sep–Oct: reproduce the public implementation of ReGA [8] and deliver a one-page reproduction brief; the official repository of ProbGuard (formerly Pro2Guard) [4] is currently under refactoring, so I will track that work via a targeted paper–code reading (both are methodologically isomorphic to RQ1–RQ2, so reproduction and close reading double as pilot work). (2) Oct–Nov: building on predicate table v0 (16 predicates), complete dual annotation (reporting κ); export anonymized platform traces; close the minimal loop "symbolic trace → DTMC → out-of-bound probability checking", answering RQ1's agreement and coverage questions. (3) Before December: consolidate into a workshop/arXiv short paper. Ethics: no human-subject experiments — evaluation uses simulated users; my own data serves model learning only, never as primary evaluation data.

**References**(编号与中文声音 B 逐条对齐)

[1] INTIMA — behavioral benchmark for boundary and dependence risks in human-AI interaction (arXiv:2508.09998).
[2] MIT Media Lab / OpenAI — four-week randomized controlled trial on psychosocial effects of chatbot use (arXiv:2503.17473).
[3] EmoAgent — LLM-judge-style monitoring and safeguarding of emotional safety in human-AI dialogue (EMNLP 2025; arXiv:2504.09689).
[4] ProbGuard (formerly Pro2Guard) — proactive runtime monitoring for LLM agent safety via probabilistic prediction (ASE 2026; arXiv:2508.00500).
[5] ShieldAgent — verifiable-policy shielding for LLM agents (ICML 2025; PMLR vol. 267).
[6] PAC-interval MDP abstraction for controller synthesis under uncertainty (JAIR 2023; DOI: 10.1613/jair.1.14253).
[7] dtControl — decision-tree representations of verified controllers (HSCC 2020; DOI: 10.1145/3365365.3382220).
[8] ReGA — representation-guided abstraction for LLM safety monitoring (FSE 2026; arXiv:2506.01770).

(Contact: [contact])

---

## Voice C — 工程版(英文全文)

# Research Statement · [Name]

**Who I am.** I am a [status] in [major] at [university], joining [lab] in September 2026. I build and operate agent systems end to end — orchestration, retrieval, memory, deployment, and the logging that makes them measurable — and I keep them running after the demo. The three systems below are mine end to end: designed, built, tested, and maintained. My research goal is to point the lab's shield pipeline at a domain where I already control both the runtime and the data.

**Selected work.**

- **EvoAgent — a self-evolving multi-agent pull-request review platform.** ~8,800 lines of Python, 43 unit tests. Architecture: harness-managed task lifecycle; LangGraph orchestration; an evaluation-gated prompt-evolution loop (prompt changes must pass the gate before they land). Observability was a first-class design decision: agent traces export from a single evidence space into two standard formats — XES 1.0 event logs and GraphML interaction graphs — and both load cleanly with PM4Py and networkx. That is an interoperability fact about the tooling, not a research result.
- **A self-built long-term human-AI interaction platform.** FastAPI backend; vector-memory pipeline; an explicit affective-state engine (state lives in inspectable code, not buried in a prompt); scheduled proactive behavior; WebSocket multi-device sync. Operations record: months of continuous operation, with thousands of turns of anonymized longitudinal interaction logs. This is precisely the long-horizon real trace data that trajectory-level safety work usually lacks.
- **MindBridge — a campus mental-health support multi-agent system.** Fine-tuned Qwen2.5-7B on 2,400 synthetic counseling QA instructions; quantized to a q4_k_m GGUF (~4.7 GB) and served locally via Ollama. Runtime: event-driven, five agents, dynamic routing over hybrid retrieval (vector + BM25). Retrieval quality measured with Recall@K, MRR, and NDCG.

**Research interests.** The problem: today's guardrails check messages, but the failure mode that matters here lives in trajectories. In long-running interaction, every single turn can look harmless while the accumulated trajectory drifts out of bounds — boundary erosion, dependence reinforcement, persona drift — a pattern that empirical studies (INTIMA; the MIT/OpenAI four-week RCT) have documented and that prompt rules and LLM judges do not quantify. My angle: run the shield pipeline end to end in this domain — predicates over interaction state (adapted from the INTIMA taxonomy), a DTMC learned from real traces, PAC-interval lifting to an iMDP, offline policy synthesis compressed into decision trees, O(1) lookup at runtime, graded interventions (rewrite / cool-down / de-escalation). The scarce input is long-horizon real traces, and my platform already produces them. Honest limits: under explicit assumptions on predicate abstraction, log completeness, and simulated-user evaluation, the output is PAC-interval probabilistic prediction for expressible out-of-bound trajectories — no end-to-end formal guarantee is claimed. As of my August 2026 survey I found no comparable probabilistic-shielding work in the long-term interaction domain; existing shield pipelines (ProbGuard, formerly Pro2Guard — ASE 2026; ShieldAgent) are evaluated on embodied, autonomous-driving, and web tasks.

**Near-term plan (Sep–Dec 2026).** Deliverables, not intentions. (1) Sep–Oct: get the public ReGA implementation running; ship a one-page reproduction brief. I tore down the official ProbGuard repo — it is mid-refactor and does not currently run end to end — so I will track it through a targeted paper-and-code read instead; same pipeline my direction consumes, so this is pilot work either way. (2) Oct–Nov: predicate table v0 is already shipped — the INTIMA taxonomy turned into 16 executable predicates with time windows; remaining: dual annotation (κ reported), export anonymized platform traces, close the minimal loop "symbolic trace → DTMC → out-of-bound probability checking", CPU-only. (3) By December: consolidate into a workshop/arXiv short paper. Ethics constraint, by design: no human-subject experiments — evaluation uses simulated users; my own platform data is used for model learning only, never as primary evaluation data.

(Contact: [contact])

---

## 尾注(给用户)

- **中英同向原则**:英文声音应与中文版选择保持同向。请先在中文三声音文件中拍板 A/B/C,再取本文件**同字母**版本使用,避免中英两份材料气质错位。
- 三版事实与数字完全一致,任选其一不影响事实审计;差异仅在语气、详略与组织。
- 发前统一动作(任一版本):①填五个占位符([status] 按本科生口径);②删除本文件全部中文说明区(头部、导读表、本尾注);③按受众决定是否保留 Voice B 的参考文献(其余两版无引文编号,可直接用)。
