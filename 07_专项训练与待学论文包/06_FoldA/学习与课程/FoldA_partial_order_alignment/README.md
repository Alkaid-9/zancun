# FoldA + Siddiqui — 偏序 alignment 双论文档案(T2 检查层技术内核)

> 拆解定位:T2 提案将这对论文标注为"**技术内核最强现有件,算法拟复用而非重造**"(T2 §7 近邻表)。本档案为 S01–S04 深度拆解,重点公式与最优性证明。
> 拆解日期:2026-08-13 ｜ 状态:**S01–S04 v1 完成**;S05/S06(复现)待复现窗

---

## 论文卡 A:FoldA

- **题名**:FoldA: Computing Partial-Order Alignments Using Directed Net Unfoldings
- **作者**:Douwe Geurtjens、Xixi Lu(乌得勒支大学 Utrecht University)——**注意:Xixi Lu 正是 2014 年偏序 conformance 开山文(Lu/Fahland/van der Aalst,BPM Workshops,LNBIP 202)的一作**,本文是其偏序诊断议程十年后的算法层补完
- **venue**:**BPM 2025**(第 23 届国际业务流程管理会议,Seville,2025-08-31/09-05),**LNCS 16044,pp. 126–143**,Springer(2026-08-13 经 Springer 卷目录页与 researchr 记录核实)
- **原文**:[arXiv:2506.08627](https://arxiv.org/abs/2506.08627)(HTML 全文含全部定义/定理/证明/评测表,2026-08-13 实见)
- **代码**:github.com/DouweGeurtjens/unfolding-alignments(Zenodo DOI 10.5281/zenodo.15552463;链接取自论文正文,仓库未实地打开)
- **一句话**:把"模型×轨迹同步积网"直接做**代价导向的有向 Petri 网展开**(而非探索可达图),第一个到达终止 marking 的配置即为**最优偏序 alignment**——一步产出并发保真的对齐,附正确性/最优性定理(Thm 4.1)与启发式可采性证明(Thm 4.3);代价是运行时间普遍慢于 A*,但排队状态数普遍更少。

## 论文卡 B:Siddiqui / van der Aalst / Schuster

- **题名**:Computing Alignments for Partially-ordered Traces Through Petri Net Unfoldings
- **作者**:Ariba Siddiqui、Wil M. P. van der Aalst、Daniel Schuster(通讯)(RWTH Aachen,PADS 组)
- **venue**:**PETRI NETS 2025**(第 46 届 Application and Theory of Petri Nets and Concurrency,Paris,2025-06-22/27),**LNCS 15714,pp. 411–432**,Springer(2026-08-13 经 researchr 记录与 Springer 章节 DOI 10.1007/978-3-031-94634-9_20 的搜索结果确认)
- **⚠ 勘误(供 T2 引用时更正)**:T2 提案 §7 近邻表把两文合写为"FoldA / Siddiqui(BPM 2025 / arXiv:2504.00550)",易误读为 Siddiqui 也是 BPM 2025——实际 **Siddiqui 发表于 PETRI NETS 2025(LNCS 15714)**,FoldA 才是 BPM 2025(LNCS 16044)。矩阵附注"dblp 记录 [需验证]"与 T2 §4 步骤 3 的"[需验证]"经本档案核实,均可解除。
- **原文**:[arXiv:2504.00550](https://arxiv.org/abs/2504.00550)(HTML 全文含定义/算法/附录充分性证明,2026-08-13 实见)
- **代码**:github.com/ariba-work/cortado(集成进 Cortado 工具)、github.com/ariba-work/classic-pa(~~Lu et al. 2014 经典两步法的对照实现;链接取自论文正文,仓库未实地打开~~〔08-22 已核:仓库存活;其 README 自述 "Classic Partial Alignments based on ILP-based A* algorithm",未提 Lu/两步法——"Lu 2014 两步法对照实现"系我方方法级归类,仓描述宜作"ILP-based A* 经典实现"〕)
- **一句话**:面向**天然偏序轨迹(p-trace)**的一步式 unfolding alignment:p-trace→trace net→扩展同步积网(加目标变迁 \(t^*\))→ \(ERV[\triangleleft_c]\)/\(ERV[\triangleleft_h]\) 展开→最优 alignment run→分解为 u-alignment(带对齐函数的双偏序),并给出**缺失/多余事件与依赖**的四象限偏差诊断和 chevron 可视化;附 \(\triangleleft_c\) 充分序的完整证明(Thm 0.B.1)。

## 两文关系(FoldA §2 自述,已核原文)

- **独立同时**:FoldA 思路源于 Geurtjens 2024 年硕士论文,投稿在 Siddiqui arXiv 版可见之前;两文互为独立发现。
- **FoldA 自称的两点差异**:① Siddiqui 未显式指出"经典方法因忽略 move 间依赖差异而**根本无法保证偏序最优**"这一动机问题(FoldA 用 Fig 1 反例讲透);② FoldA 评测面广得多(485 个含选择/并发/循环的合成模型 + 13 个真实 log-模型对 [IM+Split Miner] + 6 个基准集,vs Siddiqui 仅并行分支无循环的合成树 + 1 个真实日志 [仅 IM])。
- **互补分工(本档案判读)**:FoldA 给了更硬的实验学与更明确的问题陈述;Siddiqui 给了更严格的充分序证明(Thm 0.B.1)、p-trace 原生输入、偏差四象限分类与工具落地(Cortado)。**T2 复用应取并集**:算法骨架与证明体系以 Siddiqui 的 \(\triangleleft_c\)/\(\triangleleft_h\) 为准(tie-break 确定性可复算),问题动机与评测协议学 FoldA,偏差分类接 Siddiqui。

---

## 在 T2 管线中的位置:第 3 步"检查层"的技术底座

T2 四步管线(T2 §4):日志层(EvoAgent 双出口)→ 发现层(IM→sound WF-net + correlation_id 恢复偏序)→ **检查层** → 偏差三分类与形式保证。本对论文精确落位在**检查层**:

> T2 §4-3 原文:"安全策略 PN(人工规约+发现模型精化)与轨迹在同步积网上做 A\* 最优 alignment;**对偏序轨迹用 PN 展开做偏序对齐(2025 已有非 agent 技术底座)**,agent 场景无人做。"

具体承接关系:

| T2 需求 | 由本对论文提供 | 缺口(T2 的增量) |
|---|---|---|
| 偏序轨迹 ↔ 策略 PN 的最优 alignment | 同步积 + 有向展开 + 充分序/cut-off(两文算法主体) | 输入偏序来自 correlation_id/消息因果而非时间戳(Siddiqui Def 1 需改造) |
| 最优性保证(sound/complete 检出) | FoldA Thm 4.1(有效性/完备性/最优性/终止)+ Siddiqui Thm 0.B.1(充分序) | 保证需重述为"相对安全性质 PN 可表达偏差"(T2 §4-4b) |
| 三类偏差 + 最小证据 | Siddiqui §3.4 缺失/多余 × 事件/依赖四象限;最优配置本身 = 最小代价解释 | 偏差命名方向要翻转(见 04 §5.2);tie-break 需确定性化才"可复算" |
| 并发/循环鲁棒性 | Siddiqui 实验:并发度 70% 时 unfolding 显著占优;FoldA 支持循环与无界 easy sound 网 | LLM-MAS 轨迹的活动标签噪声、循环+选择混合结构的性能风险 |

T2 收窄贡献句的"宽松最近邻 FoldA/Siddiqui(3/4 要素)缺 LLM-MAS 场景与安全性质网语义"(T2 §1)与本档案精读结论一致:两文均为**业务过程、通用参照模型、离线**设定,无 agent 语义、无安全性质网、无"证据最小性"叙事——差异化空间实在。

---

## 核心产出文件

| 文件 | 内容 |
|------|------|
| `01_QUESTIONS.md` | 读前五问+读后回答:痛点/复杂度/与全序 alignment 差异/公式直觉/可质疑假设 |
| `03_PAPER_READ.md` | 双文精读:形式定义链/展开与"折叠"机制/两套算法逐行/复杂度/评测/局限,含两文对照表 |
| `04_DERIVATION.md` | 代价函数与最优性逐步推导(Dijkstra 不变式/cut-off 安全性/启发式一致性缺口)+ 偏序 vs 全序语义差异形式化 + **T2 复用改造点**(直接用/要改造/不复用三清单+偏差映射表) |
| `GLOSSARY.md` | 30 个术语:alignment 系/展开系/算法系/评测系 |

## 关键发现(S01–S04)

1. **"偏序最优 ≠ 全序最优的偏序化"是这条线的存在理由**:代价函数对 move 顺序不敏感(只看多重集),等代价的全序 alignment 可诱导**不同的依赖结构**,经典两步法(Lu et al. 2014:A\* 选一条再展开)任取其一,可能返回依赖诊断更差的偏序 alignment(FoldA Fig 1 反例)。unfolding 直接在配置(=偏序 run)空间搜索,绕过此缺陷。
2. **最优性保证的机械结构完全可迁移**:非负可加代价 + 充分序(well-founded / ⊂-单调 / 扩展保序)+ cut-off ⇒ "第一个弹出的目标事件即最优"(Dijkstra 不变式);加 marking-equation 启发式后为半充分序(Bonet et al.),FoldA Thm 4.3 的证明文本有一处"admissible vs consistent"的跳步,marking-equation 启发式实际满足一致性,结论无恙(推导见 04 §3.4)。
3. **性能画像**:unfolding 赢在**排队状态数**(FoldA:Dijkstra 最多多排 11.8 万%)与**高并发/高噪声域**(Siddiqui:并发 70% 时最优);输在**绝对时间**(A\* 普遍快 71–99%)与**长尾超时**(FoldA 在 BPIC17/ITL prCm6 上大量超时;可能扩展计算是组合瓶颈)。**T2 应做混合调度**:轨迹并发宽度小 → 经典 A\*,宽度大 → unfolding。
4. **两文各有一处原文瑕疵**(已核,引用时避雷):FoldA Def 6(3) 漏写标签相等条件(照抄会禁止合法选择结构);Siddiqui §3.4 第 2 类偏差("undesired")的文字段落是第 1 类的复制粘贴笔误,以其形式化关系式为准。FoldA 正文 328/500、697/1000 与 Table 2 的 679 不一致(疑笔误)。
5. **对 T2 最值钱的暗门**:FoldA 结论明确说"展开保留 move 间依赖,使得**未来可设计更高级的代价函数**"——T2 的安全加权代价(强制步骤 model move 重罚、越权 log move 分级)恰好插进这个官方声明的空位;Siddiqui 的依赖偏差(missing/undesired dependencies)恰好是 T2 第③类"序/并发违例"的现成形式化。

---

## 目录结构

```
FoldA_partial_order_alignment/
├─ README.md          ← 本文件(双论文卡 + T2 定位)
├─ 01_QUESTIONS.md    ← S01 产出
├─ 03_PAPER_READ.md   ← S03 产出
├─ 04_DERIVATION.md   ← S04 产出(含 T2 复用改造点)
└─ GLOSSARY.md        ← 术语表
```

**信息来源约定(链接实见情况)**:
- 公式、定义、定理、证明、评测数字均以两篇 arXiv HTML 全文为准(arXiv:2506.08627 与 arXiv:2504.00550,2026-08-13 抓取实见);
- venue/卷号/页码经 Springer BPM 2025 卷目录页(link.springer.com/book/10.1007/978-3-032-02867-9)与 researchr 两条记录(GeurtjensL25、SiddiquiAS25)、Springer 章节 DOI(10.1007/978-3-031-94634-9_20)的搜索结果内容核实;
- **深度受限标注**:两文图形(FoldA Fig 1–19、Siddiqui Fig 1–11)在 HTML 转文本中仅存图注与正文转述,图内 Petri 网细节不可见,涉及处均以正文文字为准;FoldA Algorithm 1 伪代码在 HTML 中行序有乱,已按正文叙述复原意图并标注;GitHub 仓库与 Springer 正式版 PDF 未实地打开(正式版与 arXiv 版若有出入,以正式版为准,此处未能比对)。

---

**最后更新**:2026-08-13
