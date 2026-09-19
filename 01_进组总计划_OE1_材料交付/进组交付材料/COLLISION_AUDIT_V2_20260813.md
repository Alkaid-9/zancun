---
task_id: TASK-20260813-021
date: 2026-08-13
type: collision-audit
status: done
version: v2
supersedes_scope: 扩充（不推翻）research/experiments/t2_fusion1_sprint_20260812/08_COLLISION_AUDIT.md（v1，六篇）
evidence:
  - progress/handoff/2026-08-13__bridge-map-fusion__map-gap-search-report.md   # TASK-013 补搜报告
  - progress/audits/2026/08/2026-08-13__audit__bridge-7agent-verification/     # TASK-021 七路回执
---

# 碰撞审计 v2（2026-08-13）

> v1（039 波）审了 SAP ABM、AgentLTL、STEAD、AgentSpec、ProbGuard、Bollig CPL 六篇。
> 本 v2 纳入 08-12 晚补搜三近邻 + 08-13 七路验收波全部新命中，共 **16 条**，并对
> T1 / T2 / T5(bridge) 三提案与 GRAND_MAP 口径给出重裁。逐条证据可溯至上方两个来源档。

## §1 证据清单与逐条裁决

| # | 对象 | 身份（核验后） | 它做了什么 | 对地图 | 对提案 |
|---|---|---|---|---|---|
| 1 | **arXiv 2003.07291**（Mecheraoui/Carrasquel/Lomazova） | CEUR Vol-2795:34-45（MACSPro 2020，非 PNSE）；仅 v1；被引 4，无 LLM 接续 | Nested PN × MAS 事件日志 × 组合式 conformance；定理=**全序**轨迹**布尔完美拟合**的组件分解等价；无 alignment/无最优性/无偏差证据/无实现 | P1 | **T2 必引**；分解定理证明结构与 T2 分解引理有撞车风险，写作时显式对比"完美拟合分解 vs 最优 alignment+最小证据" |
| 2 | **FoldA**（Geurtjens & Lu，BPM 2025, LNCS 16044 / arXiv 2506.08627） | 确证 | 偏序轨迹 × PN unfolding × **离线最优 alignment** + 偏差可视化 | P1 | **T2 技术内核最强现有件（宽松 3/4 要素）**；T2 的算法层大概率复用而非重造，必引并把贡献重心压到"安全性质网语义 + LLM-MAS 偏序日志构造 + 证据最小性" |
| 3 | **Siddiqui/van der Aalst/Schuster**（arXiv 2504.00550，Cortado 实现） | 确证 | 同上路线（unfolding alignment，工具级） | P1 | 同 #2，必引 |
| 4 | **LAMAS**（PNSE'26，CEUR Vol-4236，汉堡 Köhler-Bußmeier/Moldt 学派） | 确证（08-13 补搜新发现） | 组织模型 guardrail + **过程挖掘自动发现组织模型 + 运行时监控**，正面进入 LLM-MAS | **P0**（汉堡学派入场，PN×LLM-MAS 学术占位） | T2：其不做 alignment 级 conformance，核心仍空；T1/T5 叙事须让位其组织模型语义；必引 |
| 5 | **PetriFlow**（joshuaisaact/petri-flow） | 确证：10★/MIT/push 2026-03-21/无论文；tests+engine+CLI+示例俱全；与 netgrif/petriflow、Juhás 语言双消歧 | 声明式安全规则编译为 PN tool gate，编译期穷举可达状态（196 states 案例），运行时预防门禁 | **P0**（"活跃仓 0"作废） | T2：预防门禁 vs 离线诊断，方向错位；工程动机段必引 |
| 6 | **agentic-nets**（alexejsailer，BSL 1.1，Zenodo 10.5281/zenodo.18743372） | 确证（08-13 新发现） | agent 运行在 typed-transition PN 内，权限/内存边界=net 定义，token 可回放 | **P0**（第二个活跃仓；与 #5 构成"外置门控 vs 网内运行时"双路线） | 同 #5 |
| 7 | **HASH / Petrinaut**（hash.ai 博客 2026-02-18） | 确证（08-13 新发现） | 工业公司用 PN 编排可形式验证的多 agent 工作流（human approval 前置），开源编辑器 Petrinaut | **P0**（"工业界无人做"作废） | 工程动机段必引 |
| 8 | **Byzantine MCP Router**（wdulz，HN 47415812） | 确证（08-13 新发现） | 扩展 PN（抑制弧）保证 MCP human-in-the-loop 问责、防 agentic worm | P1 | T5(bridge)：MCP×PN 已有社区实现，T5 的"协议 PN 验证"叙事收窄 |
| 9 | **TB-CSPN**（Borghoff/Bottoni/Pareschi，Future Internet 17(8):363；无 arXiv 版） | 确证；开源 tb-cspn-poc（MIT）；同组 ≥4 项后续=活跃组 | CPN 做 agentic AI 协调；LLM 限于语义处理、编排确定化；liveness/deadlock-freedom 可验证 | **P0**（占"CPN×agentic AI 协调"位） | T2/T5：事前构造正确路线，与事后轨迹审计互补；必引 |
| 10 | **TB-CSPN 硬件篇**（arXiv:2607.02376） | 确证；**概念文，无 FPGA 原型/无实证**（自述） | 协调语义映射 FPGA 原语（同步/授权屏障/有界协调） | P1（radar 原"仅关键词命中"系误判，勘误） | 无直接冲突；"硬件强制"面留空可作远期差异点 |
| 11 | **Daszczuk**（Springer LNNS，10.1007/978-3-032-27927-9_7，2026-01） | 确证（08-13 新发现） | PN 验证分布式集成模型中 LLM agent 同步 | P1 | 邻域学术又一例，动机段引 |
| 12 | **ToolGate**（OpenReview 在审 BRHv9AUhhD） | 在审匿名稿（08-13 接口重试新发现） | 符号状态+Hoare 契约的 LLM 工具执行运行时门控与验证 | P1 | **对 T2 威胁=高**：与 T2 仅差 PN/事件日志一维；进 watchlist 月度盯防 |
| 13 | **Agent Behavior Mining**（arXiv 2606.20669） | 确证 | LLM-MAS 推理/工具轨迹→XES 式日志 + 策略偏差检测（常规 PM，无 PN 性质/无最优 alignment） | P1 | **对 T2 动机新颖性最大威胁**；必引并对比"有保证的 alignment vs 启发式偏差检测" |
| 14 | **TRAC / Formal Methods Meet LLMs**（arXiv 2605.16198，FAccT 2026） | 确证 | LTL 规范+离线审计+在线监控+可解释 witness+soundness 证明 | P1 | LTL 线占"显式性质+离线审计+证据"位；T2 必引并论证 PN 载体的增量（并发语义/偏序/结构证据） |
| 15 | **AgentLTL**（arXiv 2607.02599）与 **AgentRFC**（arXiv 2603.23801，TLA+） | 确证（v1 已审 AgentLTL，此处更新语境） | FO-LTL 程序性合规评分；agent 协议 conformance testing（TLA+） | P1 | AgentRFC 占"agent 协议安全+conformance"命名位 → **T5(bridge) 承压加剧**；两者均必引 |
| 16 | **SAP ABM 升级**（BPM 2026 主会接收，LinkedIn 双帖佐证） | 确证 | （v1 已审）agent 行为挖掘：discovery+conformance+缺失/插入偏差 | P1 | T2 提案"纯描述性"表述作废（本 v2 落实修订）；对比基线首选 |

> ⚠️ **#16 证据冲突登记（2026-08-13 20:5x）**：039 波（TASK-039）与补搜报告（TASK-013）判 ABM"实做 discovery+conformance+缺失/插入偏差"；但深挖波 A5 路同日全文核读（`research/map/matrices/conformance-lane-comparison.md` ABM 行）判"纯描述性治理，无 conformance/alignment、无形式保证"。两窗结论**相互矛盾**，可能源于"conformance"一词口径不同（偏差挖掘 vs alignment 级检查）。**T2 写作引用 ABM 前必须重开原文逐节裁决**（涉及 T2 对比基线的措辞与 R2 格式权风险）。在裁决前，两种表述都不得单方采信；"纯描述性"禁令暂缓为"待重裁"。

**检索噪声源（登记防误判）**：Anthropic "Petri"（对齐审计 agent，与 PN 无关）、HF petri-dish 类、dblp "Meng Sun 0001"（同名语音研究者）、netgrif/petriflow（低代码语言）。

## §2 三提案重裁

### T2（conformance + 形式保证）——**存活，贡献重写为四要素合取**

- 新贡献句（提案本体已同步落入）：**"面向异步 LLM 多智能体系统的偏序轨迹/事件日志，以显式安全性质 Petri 网（WF-net 类）为规范载体，做离线最优 alignment 一致性检查，并输出最小可复算偏差证据的端到端方法。"**
- 严格口径零命中维持（16 条中无一同时覆盖 ≥3/4 要素）；宽松最近者 FoldA/Siddiqui（3/4，缺 LLM-MAS 场景与性质网语义）。
- 引用义务（写作必引 12 项）：#1、#2、#3、#4、#9、#5、#6、#7、#13、#14、#15（两篇）、#16；另加煤电 conformance（TASK-013 报告 §4）。
- 禁止表述（沿 v1 并扩充）："全网无人做/全球唯一"；"13 条零命中"全称句（改为"在已扫面与日期内，四要素合取零命中，边界见 SEARCH_BOUNDARY"）；"SAP ABM 纯描述性"。

### T1+T4（传播/隔离）——**收窄口径下存活**

- "PN 尚未用于 agent 对象"旧判断作废（#4/#6/#9 都以 agent 为对象）；T1 差异点收窄为"**故障传播的影响可达集/最小隔离集计算**"（协调编排类工作 #6/#9 不做传播分析），SBPN/SBTPN 概率时序推断（T4）暂无撞车。

### T5(bridge)（MCP/A2A 协议 PN 验证）——**降级为观察+改名候补**

- #8（Byzantine MCP Router 社区实现）+ #15（AgentRFC 占协议 conformance 命名位）双重挤压；维持 GRAND_MAP"观察"状态并加"承压"注记，暂不投入；与 W7 companion 提案的 T5 编号冲突由消歧横幅处理（DEC-T5-NUMBERING 待拍）。

### GRAND_MAP 口径修订（本 v2 授权的原文改动）

- §6"F④/F⑤/F⑥×P⑥ 整片未被占据"→ 收窄为"**编排/门控/组织侧已被占（见本审计 #4-#9），'带最优性保证的事后 alignment 审计'子格仍空**"。
- §8"PN×agent 论文 0 / 活跃仓 0"→ 作废，改指本审计 §1。
- 三条收窄口径成立（顶会主 track 零条目 / 观测性厂商无形式 conformance / FPGA 仅概念），作为新占位表述。

## §3 radar watchlist 新增（12 条，月度复核）

TB-CSPN 组（含 Guarded Swarms 线）、HASH/Petrinaut、PetriFlow、agentic-nets、Byzantine MCP Router、LAMAS/汉堡学派、FoldA/偏序 alignment 线（Lu 组+RWTH）、ToolGate（在审）、Agent Behavior Mining、AgentLTL、AgentRFC、TRAC/FAccT 线。作者面执行三重过滤（消歧 ID+题目词+合作者）。**5 条 OpenReview 隐藏 ID 待用户登录核验后回填本表。**
