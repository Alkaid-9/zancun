# 第二轮研究动态：三论文拆解与 JINZU 应用计划

状态：**PLANNED / 增量挂载 / 未开始论文加工**。日期：2026-09-20。

本计划消费 9 月 14–20 日第二轮自动推送中的三篇预印本，把它们挂到现有 JINZU / EdgeIM / T2–T4–T3-lite 路线。它不改写 [两天执行合同](01_两天执行合同.md)的 18 项任务和 11 篇硬交，不挤占 `R1 最小缺口 + EX-05 继续`。三篇只能先进入身份冻结、主张台账、机制片段和应用候选；未经对抗性回源和最小验证，不升级为选题、复现或进组能力证据。

## 1. 先冻结真实输入

用户消息中的三条拆解内容基本准确，但 PDF 列表顺序与正文题名顺序不同。本轮以 PDF 首页和字节哈希建立唯一映射：

| source_id | 本地原件 | PDF 首页确认的题名 | 版本 | SHA-256 |
|---|---|---|---|---|
| R2_PETRIBENCH | `/mnt/d/Alkaid/Downloads/2609.19883v1.pdf` | *PetriBench: Benchmarking LLM Reasoning over Dynamic State Spaces* | arXiv:2609.19883v1, 2026-09-17 | `989f94fb791597ecaf66b234829f141ae17dc5d60a3dc6f87e126cdc41b16a91` |
| R2_CONTRAGENT | `/mnt/d/Alkaid/Downloads/2609.18128v1.pdf` | *Symbolic Temporal Supervision of LLM Agents Using Contracts* | arXiv:2609.18128v1, 2026-09-16 | `b338efa71c6ae3843200345024967b60ef2d3cc40a806b52c77b41e1864269e3` |
| R2_STRING_DIAGRAMS | `/mnt/d/Alkaid/Downloads/2609.20478v1.pdf` | *String Diagrams for Process Mining* | arXiv:2609.20478v1, 2026-09-17 | `9011e7deb9a251f99c748847ca0d06cd30bddd9ce9185f789122661efee46c6e` |

首个验收不是写摘要，而是确认 `source_id -> 文件 -> 题名 -> arXiv ID -> 任务`五者一致。任何一处错配都阻断下游拆解。

## 2. 昨晚教训转成本轮阻断门

| 已发生的问题 | 本轮强制动作 | 阻断条件 |
|---|---|---|
| 真实论文被串成另一条死锁/并发研究线 | 先冻结上表身份；每条机制必须指向 PDF 页、节、定义/定理/图表 | 题名、对象、符号或任务对不上原文 |
| 虚构论文名与假年份进入任务表 | 所有命名实体只能来自原件；无法回源则写 `UNKNOWN` | 出现无 source locator 的题名、仓库、数据集、数字 |
| 硬编的 `passed` 字符串被当作运行证据 | 运行声明必须附 command/cwd/version/exit/stdout/stderr/input hash | 没有真实命令和原始日志却宣布通过 |
| 同一模型家族的红蓝互审放大错误 | 模型复核只产生待核问题；主控独立打开原文，可机械化结论再用独立 oracle | 仅凭第二个模型说“同意”就升级状态 |
| 隔离分支和真实工作树状态在事后才核 | 执行前重读 HEAD/status/写域/输入哈希；只由主控写入 | 基线变化未登记或 worker 直接写仓 |
| 初始清单看似完整，后续逆向覆盖才发现遗漏 | 交付前从三个 PDF 的摘要/贡献/正文/结论反向对照 claim ledger | 主要贡献或局限没有去向 |

## 3. 在 JINZU 路线中的放置

### R2_STRING_DIAGRAMS：T2 主线的跨表示语义层

- 位置：`T2 process/event/conformance -> object-centric consistency -> cross-notation semantics`。
- 它改的问法：比较两个 discovery 输出前，先声明要保留的 sameness 是 trace language、并发/因果结构，还是带类型和数量的对象交互。
- 最小可用产物：`sameness_ladder.md`，加一对“traces 相同但真并发/互斥顺序选择不同”的反例，再记录 signature equality/inclusion 与 trace equality/inclusion 的逻辑方向。
- 与 EdgeIM 的关系：先作比较尺度和事后审计钩子。EdgeIM 当前路线不能因此被改写成 object-centric 方法，也不能在没有类型对象输入和转换规格时直接声称可比。
- 后续消费点：EX-05 中“S/E/R 相同不意味频次相同”之后，作为另一层“trace 相同也不意味并发结构相同”。这是 CONNECT 材料候选，不改 EX-05 PASS 标准。

### R2_CONTRAGENT：T3-lite 可观测/溯源接口和 MAS runtime assurance

- 位置：`T2 trajectory -> T3-lite observable interface -> contract monitor -> online block/offline score`。
- 真正可迁移点：同一份轨迹级合约经 DFA checker 同时用于执行前阻断和历史轨迹评分；将“监视器看到什么”显式写成 tool-call/return、context 和 counter 合同。
- 最小可用产物：`predicate_blindspot_pairs.json`，至少两对轨迹在所有已声明谓词上取值相同，但业务语义风险不同；监视器必须给同一 verdict，用来确认 abstraction 的信息上限。
- 信任边界：谓词是否覆盖真正风险、事件是否忠实观测、合约是否正确、counter/context 是否可信。这些不由 DFA 自动解决。
- 声明上限：只证明已暴露谓词上的程序性约束，不证明自由文本语义安全、意图安全、观测完整或合约库无错。

### R2_PETRIBENCH：评价线的 exact-oracle 形式推理基准

- 位置：`evaluation -> exact-oracle formal benchmark -> local/global x finite/infinite reasoning`。
- 真正可迁移点：生成器决定题目，独立 solver 产生真值，被测模型只看题面；按任务类型和错误类型报告，不用单一总分遮住能力差异。
- 最小可用产物：`exact_oracle_eval_protocol.md`，只先选一个有限时域任务和一个无限时域任务，冻结 Petri 网语义、序列化、独立 oracle、错误分类和退出标准；未得到 artifact 前只交协议。
- 与 JINZU 的关系：作为 T2/Petri-net 基础和“No Free Checker”后的评价方法训练，可支持讲清状态、firing、可达性、活性、死锁与有界性。
- 声明上限：高分只支持“给定形式表示后的状态空间推理”，不支持自然语言到模型的建模能力、日志到模型恢复、现实系统验证或通用程序验证能力。

T4 本轮不单独加任务。只有当后续从 ContrAgent 的确定性 verdict 或 PetriBench 的分类错误中产生可校准的不确定量，才进入 T4 候选；不为了“连上 T4”而人工添加概率层。

## 4. Fable / Sol / Gemini 3.8 Flash 分工

详细任务字段见 [模型任务单](07_第二轮研究动态_模型任务单.tsv)。三者都是 worker，不是写入者或状态裁判者。

| 模型 | 岗位 | 本轮任务 | 不得做 |
|---|---|---|---|
| **Sol** | 一手证据与机制主拆 | 三个隔离任务分别核定理/定义/算法、评测、局限与 JINZU 接口；返回准确 PDF 页/节/对象号 | 写仓、把三篇融成一个大方案、用摘要代替全文主线、宣布复现/选题成立 |
| **Fable** | 零基础教学转换 | 只消费主控已接受的 Sol 证据包，产出三张“对象→状态→规则→反例→JINZU 接口”教学卡，再各给一个不泄答案的空白练习 | 代写用户答案、决定 PASS/OWNED、自行补论文事实、提前打开 EX-06 或密封材料 |
| **Gemini 3.8 Flash** | 固定快照的字段抽取候选 | 每篇最多两个微包：身份/贡献原句，以及表格/局限/仓库声明字段；只读主控提供的最小快照 | 读主仓、读完整个人作答、工具/网络/写入、P1 机制裁决、方向综合、novelty、验收 |
| **主控 M** | 唯一写入和验收 | 冻结输入，逐条回源，处理冲突，实现/运行最小反例，写入计划产物并给状态 | 用模型互相同意代替原文、oracle 或真实运行 |

Gemini 当前仍是 `CONTROL-PLANE READY / PRODUCTION HOLD`：专用入口的真实上游烟测仍未成功，昨晚已因 `RATE_LIMIT` 止损。因此本文只把 G-R2 包排入 `HOLD`，不再自动重试；门禁未关闭时，相同字段由 Sol/Luna 或主控本地抽取，不阻断主线。

## 5. 执行波次和终止条件

1. **Wave 0，身份与基线**：M 重读 HEAD/status，记录三个 hash，建立空 claim ledger。此步不成功则不发包。
2. **Wave 1，Sol 三包可并行**：S-R2-SD、S-R2-CA、S-R2-PB 各用新上下文，各读一篇，各只返回一次终态结果。如并发资源与 A 线冲突，按 ContrAgent -> PetriBench -> String Diagrams 的顺序串行；这是调度顺序，不是学术价值排名。
3. **Wave 2，M 主审**：每篇至少抽查身份、一个核心形式对象、一个主结果、一个局限和所有拟进 JINZU 的句子。发现一处关键错误就扩大到同类主张。
4. **Wave 3，Fable 三张教学卡**：只使用 M 已接受的事实和原句。与 EX-05 直接相关的 sameness 反例可先做；其余两张只进未来学习队列。
5. **Wave G，Gemini 微包（HOLD）**：只在专用入口取得一次真实合法快照成功回执后启动；每包最多 3 个输入、20 分钟、1 次定点修正。任一伪造坐标或自升状态，整包拒收并关闭本轮 Gemini。
6. **Wave 4，合并与反向覆盖**：交付三张研究卡、三个最小产物规格和一张 JINZU 乔接矩阵。逐项反查三篇的摘要、贡献段、正文机制、实验/定理、局限和 artifact 声明是否都有去向。

任务遇到下列情况立即停在 `PARTIAL/BLOCKED`：PDF 版本变化；条件/量词不明；仓库或数据链接无法回源；需要读 sealed/holdout；需要安装大型框架、调用付费批处理、提交、推送或对外发布。

## 6. 验收与对外可用上限

| ID | 检查 | 通过条件 |
|---|---|---|
| R2-Q01 | 身份映射 | 三个文件名、题名、arXiv ID、日期、hash 一一对应；不再按消息顺序猜 |
| R2-Q02 | 主张覆盖 | 每篇的摘要/贡献/正文/结论主张并集均进 ledger，每条有 locator 和证据类型 |
| R2-Q03 | 语义方向 | equality/inclusion、assumption/guarantee、finite/infinite 等方向和前提精确，反向不成立处有反例或原文边界 |
| R2-Q04 | 应用边界 | 每条 JINZU 建议标 `SOURCE FACT / RECONSTRUCTION / HYPOTHESIS / UNKNOWN`，并写不能推出什么 |
| R2-Q05 | 最小产物 | 三个规格各有输入、输出、oracle/反例、失败条件、实际运行状态；没跑则明记 `NOT_RUN` |
| R2-Q06 | 学习边界 | 不代写 R1/EX-05，不改 PASS/OWNED/Ledger，不解锁 EX-06；仅 String Diagrams 反例可作 EX-05 后的 CONNECT 候选 |
| R2-Q07 | 模型分权 | Sol 主拆、Fable 教学、Gemini 抽取、M 验收没有混用；同家族复核未冒充独立真值 |
| R2-Q08 | 反向覆盖 | 三篇的全部主要贡献、限制和 artifact 声明各有“接收/拒绝/未核”去向，无不解释遗漏 |

本轮对 JINZU 的最高可用表述是：**已能把三篇新论文分别放入跨表示语义、可观测合约监视和 exact-oracle 评价三个位置，并给出可证伪的最小产物规格**。在这些产物实际实现、独立核验和由用户解释之前，不写“已掌握”、“已复现”、“已证明新方向”或“已形成安全方法”。
