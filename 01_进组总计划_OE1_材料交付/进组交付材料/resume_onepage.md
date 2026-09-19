# 一页学术简历(中英双版)· resume_onepage

> **草稿,严禁未经用户确认外发。**
> 日期:2026-08-13 | 起草:A7(W-对外材料窗口)
> 使用说明:① 本简历配合同目录一页纸 Research Statement(`onepager_draft_v1.md` 及后续版本)递交——简历陈列"做过什么"(量化事实),一页纸论证"要研究什么/为什么是我"。
> ② 占位符([姓名][学校][专业][联系方式][GPA(选填)])原样保留,发前对照 `placeholder_sheet.md` 填写,可用 `fill_placeholders.sh` 批量替换。

---

## 中文版(一页当量)

**[姓名]** | [学校] [专业] 本科在读(大三) | [联系方式] | GitHub: alkaid

**教育经历**
[学校],[专业],2024.09 – 2028.06(本科在读) | GPA: [GPA(选填)]

**研究方向**
LLM agent 运行时安全 × 形式化方法(概率模型检验)

**项目经历**

**EvoAgent — 自进化 PR 审查多智能体平台**
- 设计并实现多智能体 PR 审查平台的自进化闭环:harness 任务生命周期管理、LangGraph 多智能体编排、评测门禁下的提示词进化;约 8,800 行 Python、43 个单元测试。
- 实现 agent 执行轨迹到 XES 1.0 事件日志与 GraphML 交互图的同源双出口。
- 双出口经 PM4Py 与 networkx 读取验证,打通与流程挖掘/图分析工具链的互操作。

**自建长期人机交互平台(Python/FastAPI)**
- 自建并长期运营:向量记忆管线、显式情绪状态引擎、定时主动行为、WebSocket 多端同步。
- 持续运行数月,沉淀数千轮经脱敏的纵向交互日志,为轨迹级安全研究提供真实数据来源。

**MindBridge — 校园心理支持多智能体系统**
- 事件驱动 5-agent 协作 runtime,动态路由混合检索(向量 + BM25)。
- 以 2,400 条合成心理问答指令对 Qwen2.5-7B 微调,量化为 q4_k_m GGUF,经 Ollama 本地部署。
- 检索与问答质量以 Recall@K、MRR、NDCG 评测。

**竞赛奖项**
- 2026 美国大学生数学建模竞赛(MCM)C 题,M 奖(Meritorious Winner):实现 C++ 并行 MCMC 采样内核(自适应 Metropolis-Hastings、23 核 OpenMP 并行、pybind11 绑定并释放 GIL),含收敛诊断与重参数化调优;总计 4,470 行 Python + C++。
- 代码已开源:GitHub alkaid/MCM-2026-The-Prestige-TV-Paradox。

**技能**
- 编程:Python(FastAPI、pybind11)、C++(OpenMP)
- 形式化与验证:概率模型检验工具链(Storm/stormpy、PRISM 语言,学习中)
- 流程与图分析:流程挖掘(PM4Py、XES)、图分析(networkx、GraphML)
- LLM 工程:LangGraph;模型微调与量化本地部署(Qwen2.5、GGUF、Ollama);混合检索(向量 + BM25)

---

## English Version (one A4 page)

**[Name]** | [university], [major], Undergraduate (3rd year) | [联系方式] | GitHub: alkaid

**Education**
[university] — [major], undergraduate program, Sep 2024 – Jun 2028 (expected) | GPA: [GPA(选填)]

**Research Focus**
Runtime safety for LLM agents × formal methods (probabilistic model checking)

**Projects**

**EvoAgent — self-evolving multi-agent platform for pull-request review**
- Built the self-evolution loop of a multi-agent PR-review platform: harness-managed task lifecycle, LangGraph orchestration, and an evaluation-gated prompt-evolution loop; ~8,800 lines of Python with 43 unit tests.
- Implemented dual export of agent execution traces from the same evidence space into XES 1.0 event logs and GraphML interaction graphs.
- Validated interoperability of both exports by loading them with PM4Py and networkx, connecting agent traces to the process-mining/graph-analysis toolchain.

**Self-built long-term human-AI interaction platform (Python/FastAPI)**
- Built and operate the platform long-term: vector-memory pipeline, explicit affective-state engine, scheduled proactive behavior, and WebSocket multi-device sync.
- Months of continuous operation, accumulating thousands of turns of anonymized longitudinal interaction logs — a real trace source for trajectory-level safety research.

**MindBridge — campus mental-health support multi-agent system**
- Event-driven five-agent collaboration runtime with dynamically routed hybrid retrieval (vector + BM25).
- Fine-tuned Qwen2.5-7B on 2,400 synthetic counseling QA instructions; quantized to q4_k_m GGUF and deployed locally via Ollama.
- Evaluated retrieval and QA quality with Recall@K, MRR, and NDCG.

**Awards**
- Mathematical Contest in Modeling (MCM) 2026, Problem C, Meritorious Winner: implemented a parallel MCMC sampling kernel in C++ (adaptive Metropolis-Hastings, 23-core OpenMP parallelism, pybind11 bindings with GIL release), including convergence diagnostics and reparameterization tuning; 4,470 lines of Python + C++ in total.
- Code open-sourced: GitHub alkaid/MCM-2026-The-Prestige-TV-Paradox.

**Skills**
- Programming: Python (FastAPI, pybind11), C++ (OpenMP)
- Formal methods & verification: probabilistic model checking toolchain (Storm/stormpy, PRISM language — currently learning)
- Process & graph analytics: process mining (PM4Py, XES), graph analysis (networkx, GraphML)
- LLM engineering: LangGraph; model fine-tuning and quantized local deployment (Qwen2.5, GGUF, Ollama); hybrid retrieval (vector + BM25)

---

> **适配提示(发前按受众微调)**:若递交对象为流程挖掘方向的老师,可把 EvoAgent 的 XES/PM4Py 双出口 bullet 前移至该项目首条、并将技能行"流程挖掘"前置;声音基调与一页纸保持一致(踏实、量化真实、宁少勿虚)。
> **递鲁场景(OE1 §3"不堆术语"纪律)**:"研究方向"行改为"多智能体系统行为分析 × 形式化方法(Petri 网/流程挖掘)";技能行"概率模型检验工具链"降格到末位或删除;全文不得出现 shield/护盾/DTMC/iMDP/PAC 字样(与 onepager_lu_variant.md 配套自查)。
> **教育经历年份**:2024.09–2028.06 由"2026-09 时大三"口径推算,发前请确认与实际一致。
