# T3 提案：跨会话/跨 agent 长期记忆的完整性建模与 use-after-poison 值流检测

> 起草：T-FLOW ｜ 2026-08-12 ｜ 挂载：bridge 课题 T3（D 报告 Bridge 候选 2）× 孙侧 M④ 缺口 × 鲁侧 D2（UAF+VFG）
> **范围声明**：本提案为防御与完整性视角，目标是让跨会话记忆的来源、传播、错误使用**可审计、可检测**。对抗性文献（AgentPoison 等）仅作威胁对象与评测语料引用；不构造、不推演任何投毒或利用方法。

## 1. 问题与缺口

LLM agent 的长期记忆（MemGPT/Mem0/A-MEM 类）跨会话持久化、跨 agent 共享。一旦某条记忆被污染，其后续读取会在无关会话中静默影响决策——防御侧现状三缺口（均有当日核实证据）：
① 唯一形式化防线 TMA-NM（arXiv:2606.24322）走"写时来源绑定权限 + IFC 强制"路线，且其威胁模型**明确将 cross-agent shared memory 排除在范围外**，调用边界采用粗粒度污点（参数取最大不可信级），自认值级细粒度传播是未来工作；② 孙组 Securing MAS（arXiv:2510.19420，ICML 2026）用带符号 DAG 反向传播归因恶意 agent，但无记忆生命周期语义、DAG 假设覆盖不了循环协作（SUN_SIDE_MAP §3 M④："记忆完整性缺跨 agent 来源链统一模型"）；③ D 报告红蓝海矩阵确认"记忆投毒数据流检测路线"零命中（🟢格）。

## 2. 核心概念迁移：UAF def-use 链 ↔ 记忆写入-读取链

**同构点**：(a) def↔write（记忆写入/派生），use↔read+act（检索并进入决策）；UAF 判定 = "失效点之后存在对同一对象的 use 可达"，use-after-poison 判定 = "污染点之后存在对同一记忆（及其派生物）的读取可达"，二者都是值流图上的源-汇可达性查询；(b) 指针别名 ↔ 记忆派生同源（摘要、改写后仍承载同一来源），都造成"同一值多个名字"；(c) 多线程并发访问堆对象 ↔ 多 agent 并发读写共享记忆，happens-before/MHP 分析可整体迁移，鲁组 D2 用 PN 承载因果约束（vs Canary 纯 SMT）恰好适配 agent 事件的偏序语义；(d) A-MEM 的 memory evolution（新记忆触发旧记忆改写）↔ 强更新/弱更新问题。
**不同处（诚实边界）**：(i) free 是显式程序事件，"污染"无显式失效事件——判定被参数化为"给定污染源假设 S 的前向可达使用集"，S 由 provenance 来源分级给出候选，而非由检测器断言；(ii) 指针别名靠静态分析近似，记忆的"语义别名"（模型内部释义产生的隐式派生）不可静态推断，须由可信 harness 插桩把派生边变成**系统观测**（假设 H1，与 TMA-NM 的 A1 来源标注神谕对称——这也正面回应其 T1 定理"内容/可延展 lineage 不健全"：我们的边不从内容推断，故不被洗白通道抹除）；(iii) UAF 是内存安全违例，use-after-poison 是完整性违例，sink 须按后果分级（回答/工具调用/资金类操作）。

## 3. 研究问题

- **RQ1（建模）**：跨会话/跨 agent 记忆读写事件能否统一为"记忆值流图 MVFG"（节点=SSA 式版本化记忆条目事件，边=检索/派生/跨 agent 共享/演化改写），使 use-after-poison 可表达为源-汇可达性？
- **RQ2（检测增量）**：MVFG（版本化+PN 偏序过滤不可行交错）相对普通污点分析与内容检测，在精度/召回上是否有显著增量？
- **RQ3（可审计性）**：能否用 PN 展开对检出实例做确定性重演，输出最小污染传播链作为可复算审计证据（鲁组 D2 反例回放，主流预测式检测未覆盖）？
- **RQ4（互补边界）**：相对 TMA-NM 类预防式强制，检测式值流在其范围外（跨 agent 共享、过度污染导致的 utility 损失）提供多少互补量？

## 4. 方法

- **M1 记忆事件模式**：定义 write/derive/retrieve/act 四类事件+（origin, scope, t, act_class）元数据（沿用 2606.24322 已发表词汇，保证可对接），衔接 8-09 设计档 ProcessEventSchema-v0；在 EvoAgent harness 与开源记忆框架（Mem0/A-MEM）上插桩采集。
- **M2 MVFG 构建**：记忆条目按写入/改写版本化（处理 memory evolution 的强/弱更新）；检索命中与生成依赖由 harness 记录为显式边；跨 agent 边来自共享存储与消息。
- **M3 检测**：provenance 来源分级 → 污染源假设 S → 前向可达 use 集；多 agent 并发段用 PN 偏序（happens-before）剪除不可行路径以降误报；迁移鲁组 UAF+VFG 工具链（包云霞/王小宇线）。
- **M4 审计重演**：对每个告警用 PN 展开回放最小传播链（写入→派生→跨会话检索→sink），供人工复核与根因归档。

## 5. 数据与评测（存在性均已逐条核实）

- EvoAgent 共享记忆读写 trace（自有平台；污染 ground truth 用**故障注入式良性标记数据**——无害占位内容+已知标签，属测试学 fault seeding，不构造攻击）。
- MEM-INV-Bench：TMA-NM 论文正文确认已释出（GitHub+HuggingFace），跨防御×威胁×模型，带标签 [链接在 2606.24322 内，落地时二次核验]。
- AgentPoison（arXiv:2407.12784，NeurIPS 2024）公开数据集：仅作已发表威胁语料复用其标注。
- 多会话对话底座：LoCoMo（arXiv:2402.17753，≤35 会话）、LongMemEval（arXiv:2410.10813，多会话推理/知识更新）提供真实跨会话读写负载（本身无污染标签，作良性背景流量）。

## 6. 基线

① 内容检测（嵌入异常/LLM-as-judge/困惑度）；② 预防式强制 TMA-NM（度量互补而非压倒）；③ 普通污点分析（无版本化、无偏序、边界全污染）；④ provenance-only 谱系跟踪（MemLineage，~~[需验证：仅经 2606.24322 引文得知，未独立核实]~~）。

> **（联动回填 2026-08-13）基线④两处更新**（据 `research/sun/phase1/papers/MemLineage_2605/05_T3_INTERFACE.md` §4.2）：①[需验证] 摘除——MemLineage（arXiv:2605.14421）已于 08-13 全文核实并完成拆解（`research/sun/phase1/papers/MemLineage_2605/`）；②"provenance-only 谱系跟踪"表述不准——它带 M6 双层门禁与 Repair-and-Retry，超出纯谱系跟踪。修订表述建议："④ provenance 门禁（MemLineage）：取其血缘传播子系统作检测器使用（M6 门禁置记录模式，trust≥2 视为告警），度量精度/召回与 MVFG 对比；预期差异来源：Coarse 归因过度标注（精度下界）、LmSelfEval 压权 fail-open（召回缺口）——两者正是'打分边 vs 观测边'的可测化。"原文字保留备考。

## 7. 与最近邻差异

| 工作 | 路线 | 本提案差异 |
|---|---|---|
| TMA-NM（2606.24322） | 写时权限绑定+IFC 强制，预防式 | 检测/审计式；覆盖其自弃的跨 agent 共享记忆；值级细粒度（其列为 future work）；给影响面与审计链而非拒绝动作 |
| Securing MAS（2510.19420） | 坏输出反向归因，signed DAG | 前向值流+记忆生命周期语义；PN 偏序覆盖循环/并发协作 |
| Bollig（2605.20923） | 因果偏序 RV，MSC 风格 | 对象是记忆数据流非消息时序；带值流图与重演 |
| AgentPoison（2407.12784） | 红队评测（攻击侧） | 仅作威胁对象；本提案纯防御 |
| MemLineage（2605.14421）**（联动回填 2026-08-13，据 `research/sun/phase1/papers/MemLineage_2605/05_T3_INTERFACE.md` §4.1；审稿人检索 "agent memory provenance" 首撞之作，不列即硬伤）** | 条目级密码学 provenance+血缘门禁：per-principal Ed25519 + RFC 6962 Merkle log + 写时加权派生 DAG，max-of-strong-edges 传播（Thm 1 Untrusted-Path Persistence），敏感动作门拒绝不可信祖先授权；预防式强制 | 检测/审计式，正交可叠（其保标签真实，本提案保传播可见）；其派生边=写时归因打分，自证父边缺失/边权稀释/多跳衰减三类 fail-open（其 §6.6），本提案 H1 边=harness 系统观测、无权重门槛；其无 act 事件与跨 agent 并发语义（单 host 单存储），MVFG 覆盖检索→决策值流与 PN 偏序；其输出 allow/deny 审计事件，本提案输出影响面+最小传播链重演证据 |

## 8. Kill criteria

- K1：若基线③普通污点分析在两套数据上 F1 与 MVFG 差距 <5pt 且误报率可接受 → 版本化/偏序/值流无增量，降级为标签传播工程，撤 T3。
- K2：若 H1 插桩假设在主流记忆框架上覆盖 <60% 派生事件（模型内部隐式派生占主导）→ 值流边不可观测，课题不成立。
- K3：若 TMA-NM 类强制在跨 agent 场景被其后续工作补齐且零漏报零 utility 损失 → 互补空间消失。

## 9. 风险与缓解

- 语义别名漏报（无显式派生边的模型内改写）：加嵌入相似弱边做敏感性分析，报告漏报上界。
- 审稿人以 T1 定理质疑 lineage 路线：正文明示 H1 系统观测假设与"检测≠授权"的目标区分。
- EvoAgent trace 代表性不足：以 LoCoMo/LongMemEval 负载回放补真实分布。
- 撞车风险：Bollig 组或 TMA-NM 后续扩展跨 agent → 按 W2 §4 时钟，2026-12 前以 workshop/arXiv 占位。

## 10. 参考（均当日经 arxiv.org 核实存在）

- Securing MAS（NCB）：https://arxiv.org/abs/2510.19420
- TMA-NM：https://arxiv.org/abs/2606.24322
- LoCoMo：https://arxiv.org/abs/2402.17753 ｜ LongMemEval：https://arxiv.org/abs/2410.10813
- AgentPoison：https://arxiv.org/abs/2407.12784 ｜ A-MEM：https://arxiv.org/abs/2502.12110
- AgentWorm：https://arxiv.org/abs/2603.15727 ｜ Bollig 偏序 RV：https://arxiv.org/abs/2605.20923（二者经 D 报告 8-12 验证）
- 本地：LU_SIDE_MAP.md（D2）、SUN_SIDE_MAP.md（M④）、D_fm_x_mas_redblue.md（Bridge 候选 2）
