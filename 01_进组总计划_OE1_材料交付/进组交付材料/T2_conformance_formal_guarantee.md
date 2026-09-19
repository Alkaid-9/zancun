# T2 提案：LLM 多智能体轨迹的过程发现与带形式保证的一致性检查

> 起草：T-CONF ｜ 2026-08-12 ｜ 防御/可靠性视角，不涉攻击实现
> 输入：LU_SIDE_MAP（D3）、SUN_SIDE_MAP（§2.2/§3）、bridge C 报告、EvoAgent Fusion-0 代码
> **2026-08-13 修订（TASK-021 碰撞审计 v2）**：§1 增收窄贡献句；§2 空白证据全部改为有界口径（"13 条零命中"全称句与"SAP ABM 纯描述性"作废）；§7 增五组近邻。引用义务（12 项）与禁止表述以 `COLLISION_AUDIT_V2_20260813.md` §2 为准。

## 1 一句话主张

把 LLM-MAS 执行轨迹提升为标准事件日志，自动发现过程参照模型，对"安全策略 Petri 网 ↔ 实际轨迹"做 alignment 级一致性检查，输出三类偏差及**相对模型 sound/complete 的检出保证与最小证据**——以形式保证与描述性治理（SAP）、DTMC 状态抽象（SMU）双向错位。

**收窄贡献句（2026-08-13）**：面向**异步 LLM-MAS 的偏序轨迹/事件日志**，以**显式安全性质 Petri 网**为规范载体，做**离线最优 alignment**一致性检查，并输出**最小可复算偏差证据**的端到端组合——该四要素合取在已扫面内零命中（边界见 `../SEARCH_BOUNDARY.md`）；宽松最近邻 FoldA/Siddiqui（3/4 要素）缺 LLM-MAS 场景与安全性质网语义。

## 2 空白与证据

- **有界口径（08-13 改）**：在已扫面（arXiv/OpenAlex/DBLP/OpenReview 搜索面/GitHub 仓库级/HF/主要会议接收列表，截至 2026-08-13）内，四要素合取零命中；原"S2 检索 13 条零命中"全称句作废（当时未声明边界，且 S2 search 端点自 08-12 起 429）。检索边界与查询记录：`../SEARCH_BOUNDARY.md`。
- SAP **Agent Behavior Mining**（<https://arxiv.org/abs/2606.20669>，**BPM 2026 主会接收**）：agent 轨迹 XES 化 + discovery + conformance + 缺失/插入偏差检测（039 波核实；禁止再写"纯描述性"）——但无最优性保证、无偏序语义、无最小证据构造，差异压在保证层。
- SMU **AgentSpec**（ICSE'26，<https://arxiv.org/abs/2503.18666>）手写 DSL 规则；**ProbGuard**（ASE'26，<https://arxiv.org/abs/2508.00500>，即地图所记 Pro2Guard 之更名版）从轨迹学 DTMC+PAC——单 agent 符号状态抽象，无并发/偏序语义。
- **2020 直接先例（08-13 核原文）**：Mecheraoui/Carrasquel/Lomazova（<https://arxiv.org/abs/2003.07291>，CEUR Vol-2795:34-45）——Nested PN × MAS 事件日志的组合式 conformance，定理=**全序轨迹布尔完美拟合**的组件分解等价；无 alignment 计算、无最优性、无偏差证据、无实现，被引 4 条且无 LLM 接续。**必引并显式对比**（分解定理证明结构有撞车风险）。
- **LTL 系占位（08-13 增）**：TRAC（<https://arxiv.org/abs/2605.16198>，FAccT 2026）与 AgentLTL（<https://arxiv.org/abs/2607.02599>）占"显式性质+离线审计+可解释 witness"位（载体 LTL 非 PN、无偏序、无 alignment 最优性）；LAMAS（PNSE'26，CEUR Vol-4236，汉堡学派）以组织模型+过程挖掘发现+运行时监控进入 LLM-MAS（未做 alignment 级 conformance）。
- **工程侧（08-13 改）**：PN×agent 门控/编排活跃实现已存在——PetriFlow（10★）、agentic-nets、HASH/Petrinaut、Byzantine MCP Router（预防路线，与本提案事后审计错位）；原"GitHub 无 >10★"水位线作废。ToolGate（OpenReview 在审）为最近逼近者，持续盯防。

## 3 研究问题

- **RQ1 可发现性**：多 agent 并发/循环协作轨迹，在何种日志完备度假设下可发现 sound 且行为忠实的过程参照模型？
- **RQ2 保证型检查**：策略 PN ↔ 轨迹的最优 alignment 能否 sound/complete 地检出三类偏差并附最小证据？偏差与任务失败/安全事件是否统计关联？
- **RQ3 增益**：相对手写状态机、SQL 规则与原生 PM4Py，形式化路线在检出率/误报/证据可解释性上的增益几何？

## 4 方法（四步管线）

1. **日志层（现成）**：复用 EvoAgent Fusion-0 双出口——`process_events.py`（trace→ProcessEvent→XES）+ `interaction_graph.py`（correlation_id→交互图），事件模式与 SAP XES 扩展保持兼容（引文兼对手）。
2. **发现层**：PM4Py Inductive Miner 先产出 process tree，再按受支持的块结构语义转换为 sound workflow net；这里的 soundness 是**相对转换后模型的结构性质**，不等于该模型忠实代表真实 agent 系统。行为忠实度须另用 held-out trace fitness/precision 与外部案例检验。用 correlation_id/交互图恢复可观测的跨 agent 偏序；未观测因果关系不得补猜。
3. **检查层**：安全策略 PN（人工规约+发现模型精化）与轨迹在同步积网上做 A\* 最优 alignment；对偏序轨迹用 PN 展开做偏序对齐（2025 已有非 agent 技术底座 [需验证]，agent 场景无人做）。
4. **偏差三分类与形式保证**：
   - ①缺失偏差（model move）：强制步骤（验证/审批）被跳过；②越权偏差（log move）：策略外活动/消息出现；③序/并发违例：跨 agent 交接乱序、未同步并行写共享状态。
   - 保证内容：(a) 仅在 process-tree→WF-net 的受支持语义下声明结构 soundness；(b) 若使用精确最优 alignment、固定成本函数、完整可观测日志，能找到**相对给定策略 PN 可表达偏差**的最小代价解释——不声称覆盖策略外、不可观测或错误建模的风险；(c) 日志完备性、活动映射与策略库完备性假设显式声明。
   - 出口对接：发现模型可编译为运行时 monitor 的规格来源（接孙组 ReGA/monitoring 议程，互补非对撞）。

## 5 数据

- EvoAgent 自有多 agent 任务轨迹（管线已闭合，零新建成本）。
- 合成注入日志：向真实轨迹注入已知三类偏差作 ground truth（craft G2 惯例）。
- 公开补充：agent 安全 benchmark 日志→事件日志+参照模型（C 报告空白 4，无人做过，顺带成为数据贡献）[需验证可行性]。

## 6 基线

手写状态机检查器；SQL 规则查询；PM4Py 原生 discovery（仅描述）；PM4Py 原生 conformance（token replay/顺序 alignment，无 agent 偏序扩展）；概念对照 SAP ABM 描述性指标。

## 7 与最近邻差异

| 近邻 | 它做什么 | 我们的差异 |
|---|---|---|
| SAP ABM（arXiv:2606.20669） | agent 轨迹 XES 化+描述性治理 | alignment 级 sound/complete 保证+策略 PN 语义 |
| SMU AgentSpec/ProbGuard（2503.18666 / 2508.00500） | 手写 DSL；DTMC+PAC 概率预测，单 agent | PN 并发+偏序对齐；规格由过程发现自动获得，非手写规则或马尔可夫状态抽象 |
| 孙组 ReGA（<https://arxiv.org/abs/2506.01770>，FSE'26） | 表示引导抽象监控，单 agent | 互补：我们供其 monitor 规格来源 |
| 牛津 BPOP（<https://arxiv.org/abs/2602.02806>） | 贝叶斯恢复轨迹偏序，目标省 token | 偏序服务于安全一致性而非效率 |
| 同济刘关俊组 | PN×传统 MAS 验证 | 未入 LLM 时代；同源，合作通道>竞争 |
| Lomazova 组 2020（arXiv:2003.07291） | Nested PN×MAS 日志完美拟合的组合分解定理（全序/布尔/无实现） | 偏序轨迹+最优 alignment+最小证据+安全性质网语义；对比其布尔拟合分解 |
| FoldA / Siddiqui（FoldA=BPM 2025 LNCS 16044；Siddiqui=~~BPM 2025~~ **PETRI NETS 2025 LNCS 15714, pp.411-432**(venue 勘误·联动回填 2026-08-13,据 FoldA 拆解全文实见)） | 偏序 unfolding 最优 alignment（业务过程，非 agent） | LLM-MAS 场景+安全性质网+偏差证据最小性；算法层拟复用而非重造；两文全文已精拆(sun/phase1/papers/FoldA_partial_order_alignment/,含定理复推与八件复用清单),相关 [需验证] 均可解除 |
| TRAC / AgentLTL（FAccT 2026 / arXiv:2607.02599） | LTL 离线审计/FO-LTL 合规评分+witness | PN 并发/偏序语义+alignment 最优性+结构化最小证据 |
| LAMAS（PNSE'26，汉堡学派） | 组织模型 guardrail+PM 发现+运行时监控（LLM-MAS） | alignment 级 conformance 与最小偏差证据（其未做） |
| ToolGate（OpenReview 在审 BRHv9AUhhD） | Hoare 契约的运行时工具门控与验证 | 事后全轨迹 alignment 审计+过程模型语义（月度盯防对象） |

## 8 Kill criteria

- **K1**：发现模型与手写状态机行为等价，conformance 仅复述状态机可检偏差 → 形式化附加值不成立，降级为工程报告；不得以结构 soundness 掩盖行为忠实度不足。
- **K2**：三类偏差与任务失败/安全事件无统计关联 → 降级为日志工具论文。
- **K3**：PM4Py 输出进不了策略 PN 精化环（LU 地图 §2.5 假融合风险）→ 砍掉保证叙事。

## 9 风险与对策

- **R1（最高）**SMU 5 个月一迭代，若 ProbGuard 系并发化/多 agent 化即吞掉卖点 → 2026-12 前以 workshop 占位（ICLR VerifAI-2 / Agentic AI in the Wild），行文抢先讲透"PN 并发+PM 规格发现 ≠ DTMC 状态抽象"。
- **R2** SAP 抢格式权 → 兼容其 XES 扩展，差异化压在保证层。
- **R3** LLM 轨迹噪声/非平稳 → 偏差定义在活动/交互层而非 token 层，完备性假设显式化。
- **R4** 单平台外部效度 → 公开 benchmark 轨迹补充（§5）。

## 10 里程碑

M1-2（2026-08/09）：管线贯通+偏差注入集；M3-4（10/11）：三类偏差检出+全基线对比；M5（12）：workshop 投稿+arXiv 占位；2027：完整论文投 agent/SE 或 FM 社区（ICSE/FSE/AAMAS/CAV agent 空位，不复制鲁组现有投稿习惯）。

## 引用

- SAP Agent Behavior Mining：<https://arxiv.org/abs/2606.20669>
- AgentSpec（ICSE'26）：<https://arxiv.org/abs/2503.18666>（2026-08-12 核验）
- ProbGuard（ASE'26，DTMC+PAC，原名 Pro2Guard）：<https://arxiv.org/abs/2508.00500>（2026-08-12 核验）
- ReGA（FSE'26）：<https://arxiv.org/abs/2506.01770>
- BPOP：<https://arxiv.org/abs/2602.02806>
- （08-13 增）Lomazova 组 2020：<https://arxiv.org/abs/2003.07291>（CEUR Vol-2795）
- （08-13 增）FoldA：<https://arxiv.org/abs/2506.08627>（BPM 2025, LNCS 16044, pp.126-143）；Siddiqui/van der Aalst/Schuster：<https://arxiv.org/abs/2504.00550>（PETRI NETS 2025, LNCS 15714, pp.411-432——venue 勘误·联动回填 2026-08-13）
- （08-13 增）TRAC：<https://arxiv.org/abs/2605.16198>（FAccT 2026）；AgentLTL：<https://arxiv.org/abs/2607.02599>；LAMAS：CEUR Vol-4236（PNSE'26）
- （08-13 增）完整引用义务 12 项与工程侧对照（PetriFlow/agentic-nets/HASH/Byzantine MCP Router/ToolGate）：`COLLISION_AUDIT_V2_20260813.md` §1-§2
- 本地：LU_SIDE_MAP.md、SUN_SIDE_MAP.md、bridge_scan C 报告、EvoAgent `process_events.py`/`interaction_graph.py`
