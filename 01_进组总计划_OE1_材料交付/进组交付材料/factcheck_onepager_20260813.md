---
date: 2026-08-13
auditor: A4(W-对外材料窗口波次)
target: proposals/onepager_draft_v1.md(中文版+英文版全部事实句)
type: factcheck
scope: 名称口径 / 会议归属 / 空白表述边界 / 内部数字一致性 / 身份时间线
rule: 只核查不改稿;证据为准,搜不到即写搜不到
---

# 对外一页纸事实核查表(factcheck_onepager_20260813)

> 被核版本:`onepager_draft_v1.md`(2026-08-13 起草)。核查手段:arXiv/PMLR/ACL Anthology 实时抓取 + 本仓实测(EvoAgent、mindbridge)+ 内部档案对照(SEARCH_BOUNDARY、COLLISION_AUDIT_V2、proposal-notes、T5)。
> **总计:FAIL 1 条(名称口径,涉 6 处改动点)、WARN 2 条、其余 PASS。**

---

## 一、裁定摘要

### 1.1 名称口径裁定(最高优先)★

**事实认定(2026-08-13 实查)**:

- arXiv:2508.00500 当前页面标题为 **"ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction"**,页面头部带 ACM camera-ready 会议标注:**Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26), October 12–16, 2026, Munich, Germany**。即:论文已更名 **ProbGuard** 并获 **ASE 2026** 录用。证据:https://arxiv.org/abs/2508.00500(实时抓取,2026-08-13)。
- 旧名 **Pro2Guard** 为该论文 v1/v2 时期名称(v1 副标题 "…via Probabilistic Model Checking",v2 "…via Probabilistic Prediction",arXiv HTML 历史版本可见:https://arxiv.org/html/2508.00500v2)。
- 官方代码仓库**仍名** `haoyuwang99/Pro2Guard`,README 仍引用旧题(https://github.com/haoyuwang99/Pro2Guard)。
- 作者不变:Haoyu Wang、Christopher M. Poskitt、Jiali Wei(XJTU)、Jun Sun——**SMU Jun Sun 组**,v1 撰写说明第 5 条的"两个 Sun"警示方向仍正确。
- 结论:CHANGELOG 军情"Pro2Guard 更名 ProbGuard 获 ASE 2026"**属实**;v1 撰写说明第 6 条("FOCUS.md 内部写法 ProbGuard 即论文正式名 Pro2Guard,对外一律用正式名 [Pro2Guard]")**已过时且方向恰好写反**——现行正式名是 ProbGuard,FOCUS.md 的写法反而是对的。判 **FAIL**。

**裁定建议(最稳写法)**:对外一律以 **ProbGuard 为主名**,首次出现括注旧名与录用信息,此后直接用 ProbGuard:

- 中文:**"ProbGuard(原名 Pro2Guard,ASE 2026,arXiv:2508.00500)"**,第二次起写 "ProbGuard"。
- 英文:**"ProbGuard (formerly Pro2Guard; ASE 2026, arXiv:2508.00500)"**,第二次起写 "ProbGuard"。

理由:① 一页纸的使用时点是 2026-09 进组,ASE 2026 于 10 月开会,课题组届时看到的最新 arXiv 页、会议日程、正式版论文都叫 ProbGuard——以旧名为主的写法(如 "Pro2Guard(现名 ProbGuard)")到 10 月会后立刻显得信息滞后;② 2025-08 至 2026 年上半年的第三方引用与官方代码仓库仍用 Pro2Guard,括注旧名一次即可消除"你说的 ProbGuard 是不是那个 Pro2Guard"的沟通摩擦,同时展示军情追踪到位;③ 括注 arXiv 号锚定唯一身份,规避一切重名/更名风险。口头被问复现计划时可补一句"代码仓库还挂在旧名 Pro2Guard 下"。

### 1.2 必须修改项清单

| # | 位置 | 现状 | 改法 |
|---|---|---|---|
| M1 | 撰写说明第 6 条 | "对外一律用正式名 Pro2Guard" | 改写为:"论文已更名 ProbGuard 并获 ASE 2026(2026-08-13 核实,arXiv:2508.00500);对外以 ProbGuard 为主名,首次出现括注原名 Pro2Guard 与 ASE 2026;代码仓库仍名 Pro2Guard" |
| M2 | 中文版 §三 "现有概率护盾工作(Pro2Guard、ShieldAgent)" | 用旧名 | "现有概率护盾工作(ProbGuard,原名 Pro2Guard、ASE 2026;ShieldAgent)" |
| M3 | 中文版 §四 "跑通 Pro2Guard 与 ReGA 的公开实现" | 用旧名 | "跑通 ProbGuard 与 ReGA 的公开实现"(首次出现处已括注旧名) |
| M4 | 英文版 "existing shield pipelines (Pro2Guard, ShieldAgent)" | 用旧名 | "existing shield pipelines (ProbGuard, formerly Pro2Guard; ShieldAgent)" |
| M5 | 英文版 "run the public implementations of Pro2Guard and ReGA" | 用旧名 | "run the public implementations of ProbGuard and ReGA" |
| M6 | 撰写说明第 5 条人名警示 | "Pro2Guard 出自 SMU Jun Sun 组" | 同步更名:"ProbGuard(原 Pro2Guard)出自 SMU Jun Sun 组"(警示内容本身经核属实,保留) |

建议连带(WARN 级,见明细 C1/C2):评测域表述补"自动驾驶";空白句"同类工作"显式化为"带概率保证的同类护盾工作"。

---

## 二、核查明细表

判定口径:PASS=证据支持,可外发;WARN=不算错但有被追问翻车面,建议修;FAIL=与证据冲突,必须改。

### A. 名称口径

| 条目 | v1 原句(摘) | 判定 | 证据 | 修正建议 |
|---|---|---|---|---|
| A1 arXiv:2508.00500 正式名 | 撰写说明第 6 条:"'ProbGuard'即论文正式名 Pro2Guard…对外一律用正式名" | **FAIL** | arXiv 实时页标题 "ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction" + ASE '26 camera-ready 头(https://arxiv.org/abs/2508.00500);GitHub 仓库仍名 Pro2Guard | 按 §1.1 裁定改 M1–M6 |
| A2 该论文作者归属 | 撰写说明第 5 条:"Pro2Guard 出自 SMU Jun Sun 组;与 PKU Meng Sun 是两个人" | PASS(名称需连带更新) | arXiv 页作者:Haoyu Wang/C.M. Poskitt/Jun Sun(SMU)+ Jiali Wei(XJTU);ReGA 作者 Meng Sun(PKU,通讯)——确系两人 | 执行 M6 |

### B. 会议/发表归属(正文出现的)

| 条目 | v1 原句(摘) | 判定 | 证据 | 修正建议 |
|---|---|---|---|---|
| B1 ReGA | §四:"跑通 Pro2Guard 与 ReGA 的公开实现"(正文未标会议;内部基准:FSE 2026,arXiv:2506.01770,DOI 10.1145/3808177) | PASS | arXiv 实时页(https://arxiv.org/abs/2506.01770):"ReGA: Model-Based Safeguard for LLMs via Representation-Guided Abstraction",页面标注 DOI 10.1145/3808177、PACMSE Vol.3、fse26main(即 FSE 2026);作者 Zeming Wei/Chengcan Wu/Meng Sun(PKU) | 无需改;口头可称"FSE 2026(PACMSE)" |
| B2 ShieldAgent | §三:"(Pro2Guard、ShieldAgent)"(内部基准:ICML 2025,PMLR v267 chen25ae) | PASS | PMLR 实时页(https://proceedings.mlr.press/v267/chen25ae.html):42nd ICML,PMLR 267:8313-8344,2025,Chen/Kang/Li;名称未变 | 无需改 |
| B3 INTIMA | §三:"实证研究(INTIMA;…)";§四:"INTIMA 行为分类学…12–16 个…谓词"(内部基准:arXiv:2508.09998) | PASS | arXiv 实时页(https://arxiv.org/abs/2508.09998):"INTIMA: A Benchmark for Human-AI Companionship Behavior",Kaffee/Pistilli/Jernite;摘要明确 "taxonomy of 31 behaviors across four categories and 368 targeted prompts"——内部口径"31 类/368 prompt"同步得证;页面未见会议归属标注 | 无需改;正文"行为分类学改写为 12–16 个谓词"是自己的计划句,与 31 类源分类学不冲突 |
| B4 MIT/OpenAI 四周 RCT | §三:"(INTIMA;MIT/OpenAI 四周 RCT)"(内部基准:arXiv:2503.17473) | PASS | arXiv 实时页(https://arxiv.org/abs/2503.17473):"How AI and Human Behaviors Shape Psychosocial Effects of **Extended** Chatbot Use: A Longitudinal Randomized Controlled Study";作者 MIT Media Lab(Fang/Liu/Danry/Lee/Chan/Pataranutaporn/Maes)+ OpenAI(Phang/Lampe/Ahmad/Agarwal);摘要确认 four-week RCT、n=981、>300k messages——"MIT/OpenAI 四周 RCT"表述准确 | 无需改;注意现版标题多了 "Extended" 一词,引用全称时以页面为准 |
| B5 ProbGuard 评测域 | §三:"评测域集中在具身与 web 场景";英文 "evaluated in embodied and web domains" | **WARN**(C1 详述) | ProbGuard 摘要:"two safety-critical domains: autonomous driving and embodied household agents"——具身之外还有自动驾驶;web 属 ShieldAgent(6 个 web 环境,PMLR 页摘要) | 中文改"评测域集中在具身、自动驾驶与 web 场景";英文 "embodied, autonomous-driving, and web domains" |

### C. 空白表述边界

| 条目 | v1 原句(摘) | 判定 | 证据 | 修正建议 |
|---|---|---|---|---|
| C1 评测域概括 | 同 B5 | **WARN** | 同 B5 | 同 B5(被追问"Pro2Guard 不是还做了自动驾驶吗"时,漏写会显得没读过论文) |
| C2 域空白句 | §三:"在我 2026 年 8 月的调研中未见长期交互域的同类工作";英文 "as of my August 2026 survey I found no comparable work in the long-term interaction domain" | **WARN**(表述成立,建议收窄一词) | ① 合规性:带检索时点限定("2026 年 8 月的调研中"),无 SEARCH_BOUNDARY 禁语(全网无人做/全球唯一),符合有界口径;② COLLISION_AUDIT_V2 全部 16 条证据均为 PN/conformance/编排/工具门控线,无一是"长期交互域概率护盾"(最近者 #12 ToolGate 为工具执行门控、在审,#8 为 MCP×PN,均非本域);watchlist 12 条同样无本域条目;③ 独立复搜(2026-08-13):检得 GitHub 仓库 **SIIHA**(HUEI-JYUN-DEBBY-YEH/siiha-safety-guardrail,"runtime governance for emotionally vulnerable human-AI interactions…long-term interaction drift")——**规则式治理(constitutional rules/response modifiers),自称实验性,无 DTMC/概率模型检验/PAC 保证**,不构成"概率护盾同类工作"的反例,但已是"长期交互域运行时护栏"的边缘先例 | 把"同类工作"显式锚定到概率保证上:中文"未见**将概率模型检验护盾用于**长期交互域的同类工作"或"未见长期交互域**带概率保证的**同类护盾工作";英文 "no comparable **probabilistic-shielding** work in the long-term interaction domain"。SIIHA 建议登记进 radar watchlist(本文件不代登,遗留项 L6) |

### D. 内部数字一致性(本仓 2026-08-13 实测)

| 条目 | v1 原句(摘) | 判定 | 证据 | 修正建议 |
|---|---|---|---|---|
| D1 EvoAgent 行数/文件数 | 中"约 8,800 行 Python"/英 "~8,800 lines";撰写说明"44 个 Python 文件约 8,800 行(不含 .git/output)" | PASS | 实测(`/mnt/d/MyResearch/EvoAgent`,排除 output):**44 个 .py 文件,8,824 行**(gitignore 口径与全量口径结果一致);"约 8,800"成立,中英一致 | 无需改 |
| D2 EvoAgent 测试数 | 中"43 个单元测试"/英 "43 unit tests" | PASS | 实测 `tests/` 下 `def test_` 计 **43** 个;中英一致 | 无需改 |
| D3 MindBridge 微调数据 | 中"2,400 条合成心理问答"/英 "2,400 synthetic counseling QA instructions" | PASS | 实测 `mindbridge/psychqa_synthetic.jsonl/psychqa_synthetic.jsonl` 计 **2,400 行**;中英一致 | 无需改 |
| D4 MindBridge 模型 | 中"Qwen2.5-7B…量化为 q4_k_m GGUF 经 Ollama 本地部署"/英同;撰写说明"约 4.7 GB" | PASS(带单位注) | 实测文件 `mindbridge-qwen2.5-7b-ft-q4_k_m.gguf`,**4,683,073,536 字节 = 4.68 GB(十进制)= 4.4 GiB**;"约 4.7 GB"按十进制成立(正文未写体积,仅撰写说明) | 无需改;若口头报体积,建议说"约 4.7 GB(即 4.4 GiB)"防较真 |
| D5 MindBridge 5-agent 与评测 | 中"事件驱动 5-agent 协作 runtime,动态路由混合检索(向量 + BM25),含 Recall@K/MRR/NDCG 评测"/英同 | PASS | `mindbridge-py/README.md` 实证:五个 Agent(Coordinator/Understanding/Safety/Context/Response)事件驱动黑板协作;Chroma 向量 + BM25 融合检索;评测含 Recall@K、Precision@K、MRR、NDCG@K、HitRate;中英一致 | 无需改 |
| D6 平台量级 | 中"持续运行数月,沉淀数千轮…纵向交互日志"/英 "months of continuous operation…thousands of turns" | PASS(内部口径) | 与 proposal-notes 统一脱敏原则、T5 §M2("数千轮纵向")口径一致;中英一致。**实数本次未复核**(量级表述,无平台数据库读取,见遗留项 L7) | 无需改 |
| D7 XES/GraphML 双出口 | 中"同源双出口,经 PM4Py 与 networkx 读取验证"/英同 | PASS(措辞合规) | 撰写说明第 7 条已按 039 波审计(Gate R0 FAIL)自限为"互操作事实";正文两版均未越界称"实验/研究结果";中英一致 | 无需改;口头同样只说"读取验证通过",不说"评测过" |

### E. 身份与时间线

| 条目 | v1 原句(摘) | 判定 | 证据 | 修正建议 |
|---|---|---|---|---|
| E1 进组时点 | 中"将于 2026 年 9 月进入[课题组]"/英 "joining [lab] in September 2026" | PASS | 中英一致;与任务背景(9 月进组)一致 | 无需改 |
| E2 身份口径 | 正文用占位符[身份表述]/[status];撰写说明第 2 条:"本科生,2026-09 进组时为大三…勿写成研究生" | PASS | 中英两版均为占位符,填充口径已在撰写说明锁定(含 2026-08-13 身份勘误) | 发前按第 2 条填"本科生/undergraduate",删撰写说明 |
| E3 近期计划时间轴 | 中"①复现打底(9–10 月)②域建模 v0(10–11 月)③12 月前…短文"/英 "(1) Sep–Oct (2) Oct–Nov (3) Before December" | PASS | 三段节点中英逐一对应;与 T5 §9("2026-12 前 workshop/arXiv 占位")一致 | 无需改 |
| E4 伦理边界句 | 中"不做真人实验,评测采用模拟用户…自有数据仅用于模型学习"/英同 | PASS | 与 T5 §5(W4 门禁③)逐句对应;中英一致 | 无需改 |

---

## 三、"仅口头引用风险"附表

正文未点名、但 proposal-notes 在列且用户面谈可能引用的条目(引用前以本表为准):

| 条目 | 内部写法 | 核查结果 | 判定 | 口头引用建议 |
|---|---|---|---|---|
| AgentSpec | "AgentSpec(ICSE 2026),arXiv:2503.18666" | arXiv 实时页(https://arxiv.org/abs/2503.18666)带 camera-ready 头:**48th ICSE(ICSE '26),2026-04-12~18,里约热内卢**;作者 Haoyu Wang/Poskitt/Jun Sun(SMU)。注:页面标题渲染为 "\tool:…"(LaTeX 宏未展开的渲染瑕疵),正式名 AgentSpec 无疑(GitHub 与第三方引用一致) | PASS | 可称"AgentSpec,ICSE 2026";它与 ProbGuard 同出 SMU Jun Sun 组,口头别张冠李戴到 PKU Meng Sun |
| EmoAgent | "EmoAgent(EMNLP 2025),arXiv:2504.09689" | ACL Anthology 实证(https://aclanthology.org/2025.emnlp-main.594/):**EMNLP 2025 主会**(非 Findings),苏州,2025-11,pp.11741–11756,DOI 10.18653/v1/2025.emnlp-main.594 | PASS | 可称"EmoAgent,EMNLP 2025 main";其 EmoGuard 组件在 T5 叙事中是基线 |
| INTIMA 的"31 类/368 prompt" | proposal-notes/T5:"31 类行为分类学""368 prompt" | 摘要原文:"a taxonomy of 31 behaviors across four categories and 368 targeted prompts" | PASS | 口头引用数字安全;正文只写了"行为分类学",不必带数 |
| RCT 的 "n=981" | T5:"n=981" | 摘要原文:"four-week randomized controlled experiment (n=981, >300k messages)" | PASS | 口头引用安全 |
| SIIHA(新发现) | 内部无记录 | GitHub 个人实验仓(https://github.com/HUEI-JYUN-DEBBY-YEH/siiha-safety-guardrail):长期情感交互的规则式 runtime governance,无论文、无概率保证 | 提示 | 若口头把空白句说宽成"没人在长期交互域做护栏"会被此类仓库反例;**始终把空白限定在"带概率保证的护盾"上** |
| ProMAS / conformance-shield OSS(CHANGELOG 军情提及) | radar delta:"ProMAS 已占 MAS 主动预测、OSS 已有 0★ conformance-shield 原型" | 本次未核读 radar delta 原文(非必读面) | 提示 | 同上:空白句只说"长期交互域概率护盾";若说宽成"没人做 agent 越界预测/预测式护栏"会撞 ProMAS 与 ProbGuard 本身 |

---

## 四、遗留项(网搜无法确认或超出本次范围,标注给用户)

- **L1 ProbGuard 副标题两说**:arXiv 实时页为 "ProbGuard: **Proactive Runtime Monitoring** for LLM Agent Safety **via Probabilistic Prediction**";部分索引源(DOI 解析/学术缓存)显示 "ProbGuard: **Probabilistic Runtime Monitoring** for LLM Agent Safety"。系统名 ProbGuard 与 ASE 2026 双源一致,不影响一页纸(只用系统名);**引用全称前请点开 arXiv 页确认当前版本副标题**。
- **L2 ASE 2026 官方接收列表未直接核到**:本裁定依据为 arXiv camera-ready 页的 ACM 会议头(ASE '26,慕尼黑,2026-10-12~16),属强证据;如需绝对稳妥,会前可在 ASE 2026 官网 accepted papers 页复核一次。
- **L3 MIT/OpenAI RCT 正式发表 venue**:arXiv 页未见期刊/会议标注,本次搜索亦未见;口头称"MIT/OpenAI 的四周 RCT(arXiv 预印本)"最稳。
- **L4 INTIMA 会议归属**:页面未标注 venue,本次未检得;维持只写 arXiv 号的现口径即可。
- **L5 proposal-notes 其余文献未逐条网核**(超出指定六条):Badings JAIR 2023、dtControl、Position paper(ICML 2025)、DiverseGuide(ICFEM 2025)、NeMo Guardrails、RvLLM、Agent-C、Ctrl-G、OCC(Synthese 2009)、Verified Detection(arXiv:2606.17182)、CoAgent、SagaLLM(VLDB 2025)、CRDT(OOPSLA 2017)。口头引用任何一条的会议归属前,建议按本表方法点验一次。
- **L6 SIIHA 建议登记 radar watchlist**:本文件按任务约束不改任何其他文件,登记动作留给 watchlist 辖区窗口。
- **L7 平台"数月/数千轮"实数**:内部既定量级口径,本次未做平台数据库实数复核;对外为量级表述、风险低,如需精确数需用户授权后另测。

---

*核查完毕。本文件为唯一产出;未修改 onepager_draft_v1.md 及任何其他文件,未登 CHANGELOG。*
