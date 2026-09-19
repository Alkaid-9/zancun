# 训练包 lu-edgeim-algo1 · 零基础到拥有 EdgeIM Algorithm 1

**Date**: 2026-09-03（大纲冻结日）
**Type**: 训练包开箱档（learning 层，不是第二权威源：研究决策在 `progress/decisions/`，本包只管"练"）
**受约束于**: `learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md`（下称 OS）
**对应研究面**: `progress/decisions/2026-09-03__research__bridge-segment0-execution-brief-v1.1.md`（PROPOSED）的 G0 / T0 由本包第 0–1 站产出
**大纲版本**: v1（2026-09-03 用户「先存档目前大纲，避免后续漂移」）。改动只许在文末 Amendment 追加，且受 OS §16 约束：一周内不大改，每次周复盘最多动 1–2 个变量。

**当前入口**：先读 [START_HERE.md](./START_HERE.md)，再按唯一站序进入当前 README。论文定位见 [PAPER_MAP.md](./PAPER_MAP.md)，跨站卡只从 [CONNECTIONS.md](./CONNECTIONS.md) 按站解锁；七图入口和统一研究笔记由 START_HERE 集中导航。历史正文保留，冲突处以文末最新 Amendment 为准。

**现行学习主干与进组应用层**：整篇 ownership、Whole-Paper Diagnostic、双线程节奏和月底滚动窗口以 [MASTERY_GATE.md](./MASTERY_GATE.md) 为准；进组准备只是建立在学习主干和研究邻域之上的应用出口，不定义整个学习目标。用户报告实际执行已过 EX-03；下一次学习动作是先做 15 题诊断，不机械重做 EX-00，也不因磁盘密封答案存在而自动记为 PASS。

**研究系统映射（2026-09-06）**：`WORLD / FIELD -> RESEARCH MAPS -> ACTIVE TRACKS -> EVIDENCE / PRACTICE -> ARTIFACTS` 作为导航结构，所有层回链 `SOURCES`；`CLAIMS / GOVERNANCE` 横切记录来源、责任主体、状态和 claim ceiling。该映射不新增站点、不改变原题面或 PASS。

---

## 0. 这个包为什么存在

2026-09-03 白天，R1（EdgeIM sampling mechanism audit）从计划到代码全由 agent 完成，
用户没有在纸上跑过一次 Algorithm 1。结果把一个无参数的一遍过滤器当成了 fixed-K 采样器，
当天全部实验数字作废（`research/edgeim_sampling_audit/STATUS.md`）。

按 OS §7，核心算法和论文 reasoning 是"必须长在本人身上"的两项。本包就是把这两项补回来。
**规划放最后一站**——今天规划部分本来是做得最好的，坏的是对象层。

## 1. 起点与前置

- 起点：过程挖掘零基础。不需要先学 Petri 网、不需要先学 pm4py。
- 数学前置：集合、子集、有序对。数三范围内。
- 数据结构前置：排序 + 一遍扫描维护集合。正是考研数据结构内容。
- 每站开工前按 OS §4B 写 PASS 条件（本包已预写，**赛后不得降低**）。

## 2. 六站大纲（冻结）

| 站 | 学什么 | 时间盒 | 产出 | PASS 条件（冻结） | 对应研究面 |
|---|---|---|---|---|---|
| **0** | 事件日志 / case / trace / activity；`(S, E, R)` 三集合；Algorithm 1 手跑两遍（正序、乱序） | 一晚 2–3h | `EX-00/` 手算稿 | 空白纸脱稿：写出 Algorithm 1 的输入、维护的状态、保留判据、终止、输出；说清"为什么它没有 K"；两种 CaseID 顺序下保留集合不同且能解释为什么 | G0 五问之 1、2；关闭 Mistake Log #1 |
| **1** | DFG 与边频次；过滤前后频次对比；带问题读原文 Stage 1 | 一晚 2–3h | `EX-01/` + `_scratch/seg0/G0_user_paper_note.md`（用户写） | 手画两张 DFG（原始 vs D′）并说出哪些边次数变了；paper note 五问全答，第 3 问（频次在 D′ 重算还是原始带过来）有 `PAPER-TEXT` 页码依据或明确 `UNKNOWN`；每条陈述标 PAPER-TEXT / USER-INFERENCE / UNKNOWN | G0 完成；T0 可裁 |
| **2** | Inductive Miner 直觉（四种切）；pm4py 跑同一日志对照；IMf `noise_threshold` 是什么 | 3–4h | `EX-02/` | 在 EX-00 日志的 DFG 上手切出过程树；用 pm4py 跑出模型并指出与手切的异同；用一句话说清 noise_threshold 按什么砍边、为什么第 1 站的频次塌平会让它失效 | 邻接圈建图 |
| **3** | 噪声与"非法"：oracle 是什么；手插一个事件看 R 多出什么；噪声占比计数题 | 2h | `EX-03/` | 手插一个非法事件后正确写出新增的 r；解释为什么"现有字母表插非法位置"在 Algorithm 1 下首次必留；完成一页手算：D′ 噪声占比 vs 随机采样噪声率 | B3 primary 为何作废；G0 note 附页 |
| **4** | 测量在测什么：OS §15 六问审 `_withdrawn/T2` | 2h | `EX-04/` | 独立写出六问答案，第 3 问 Identification 自己指出 T2 测的对象与 Algorithm 1 的差异（不看 STATUS.md / v1.1） | informative failure 的 credit assignment 由本人完成 |
| **5** | 代码：自己写 Algorithm 1（~15 行）；对照 `_features`；在 10 个 universe 上跑证伪测试；按 OS §11 逐个接管生成器层 | 4–6h | `EX-05/` 自写实现 + 运行记录 | 裸机先写出能跑的实现，再看 `pilot.py`；能预测 `1.000` 塌不塌并说出理由；对 `build_universe` / `classify_trace` 各答出 representation、改一个条件的影响 | 今天数字的证伪；生成器层是否归本人 |
| **6** | 规划：T0 裁定 → T2' / T3' / T4' | 由 v1.1 定 | v1.1 §2–3 交付物 | 由 v1.1 门制度判定 | 规划有对象可依 |

合计约 15–20h，在 T4 容量模型（115h）内；进组已改月底，09-20 冻结日不动。

**顺序不可调换**：第 5 站（代码）在第 4 站之后，第 6 站（规划）在最后。这是 OS §7「裸机先手 → AI 辅助 → 关答案重做 → 冷启动复测」在本包的具体化。

## 3. AI 在本包的角色（OS §7）

**做**：出题；给定义与一个跟练习不同的微例子；判对错；追问 1–2 层；给反例、改条件、出变体；环境与 API 问题；核对原文页码。
**不做**：不写 paper note；不写 Algorithm 1 实现（第 5 站你写完前不给）；不替你填六问；不替你裁 T0。
**答案密封**：每站参考答案在 `_sealed/`，做完再开。开了再做不算 PASS，记 hint 级。

## 4. 记账（OS §4）

- **A. Hard Evidence Ledger**：每站 PASS 后在 `learning/training/LEDGER.md` 加一行（日期 | 包/EX | 用时 | hint 级 | 自评 | AI 评 | 暴露弱点 | 铸/磨卡）。**只在 PASS 后写。**
- **B. Active Check List**：就是上表的 PASS 条件列。每日 1–2 站，不多开。
- **C. Mistake Log**：`MISTAKE_LOG.md`（本目录）。#1 已登记为 OPEN，关闭条件在第 0 站。
- 当天没 PASS 也没暴露新错 → 在 LEDGER 记一行 `NO-HARD-OUTPUT`（OS §3），不写长复盘。

## 5. 冷启动复测（OS §5）

第 0 站 PASS 后 D+2、D+7 各一次：空白纸重写判据、给一份新的 5 条 trace 预测保留集合。
第 5 站 PASS 后 D+3：不看代码说出 `build_universe` 的 representation。
复测不过 → 该能力从 Ledger 标 `RE-OPEN`，不删历史。

## 6. 防漂移

- 本文件是唯一大纲。任何新窗口先读这里，不从对话摘要重建大纲。
- 想加站、删站、换顺序 → 写进 Amendment，标日期，等周复盘。
- 想"顺手先把代码写了" → 违反 §2 顺序，记 Mistake Log 候选。
- 想"这站太简单跳过" → 不跳；用 PASS 条件验，通过就快，验不算跳。
- agent 后台产出（文献核验、API 版本核对等）只是输入（OS §8），不进 Ledger。

## 7. 站点文件约定

```
lu-edgeim-algo1/
├── BRIEF.md          ← 本档
├── MISTAKE_LOG.md    ← 错误账本（本包）
├── EX-00/ … EX-05/   ← 每站：README.md（题面）+ 你的手算/代码
└── _sealed/          ← 参考答案，做完再开
```

---

## Amendment

（追加制。格式：日期 | 改了什么 | 为什么 | 依据 OS 哪条）

**A1 · 2026-09-03 晚 | 采纳独立审稿人（`_scratch/2026-09-03__independent-continuation-review__scratch.md` §3）七条，用户「可以改动，其他的都同意」 | 大纲 v1 落盘当晚、任何一站开始前的一次性修正，不算 §16 的"一周内大改" | OS §7、§17、§10 ③**

| 项 | v1 | A1 之后 |
|---|---|---|
| 新增 **5a 站** | — | 第 1 站之后立即裸写 Algorithm 1（~1h，纸上写完再敲），PASS=在 EX-00 六条上跑出与手算一致的保留集合。理由：OS §17 要尽早有"自有实现进入可测状态"的 hard output |
| 第 4 站 | 六问审 `_withdrawn/T2`（2h） | **砍**。credit assignment 压成 Mistake Log #1 的亲手填写，并入第 0 站收尾（30 min） |
| 第 2 站 | 3–4h | **5–6h**，拆 2a 手切 / 2b pm4py 首装首跑（本机 2.7.23.6） |
| 第 3 站 PASS | "D′ 噪声占比 vs 随机采样"手算 | 改为：推出 \|D′\| 的上界（用 \|S\|+\|E\|+\|R\|），并用**原文自己的例子**（十条四变体）手算过滤前后边权变化 |
| 第 5 站主体 | 证伪 `1.000` | 改为**不变量测试**：自写实现在 D 与 D′ 上断言 S/E/R 相等；`1.000` 塌不塌只作 30 min 附录 |
| 第 1 站 PASS | 五问全答 | 允许对"Stage 3 是否使用权重"答 UNKNOWN |
| 新增 **第 7 站：实验** | — | pre-prediction → 合成日志（+ 可选 Sepsis）→ IM/IMf on D vs D′ → verdict。OS §10 ③ 的落点；主对照是 **D 本身**，随机等量只作次级控制 |
| 总时长 | 15–20h | **22–28h** |

顺序 A1 后：0 → 1 → 5a → 2 → 3 → 5 → 6 → 7。§2「顺序不可调换」对新顺序继续生效。
T0 的四选项裁定仍在第 1 站之后；用户 09-03 表示同意审稿人"B 为地板、C 为唯一研究问题"的方向，正式裁定待 G0 note 完成。

**A2 · 2026-09-04 上午 | 第 0 站题面由 Sol 版（v0）换为 Fable 版（v2，`EX-00/README.md`）；v0 题面 + 用户作答 + 批改原样归档 `EX-00/_v0_sol/`，v0 密封归 `_sealed/_v0_sol/`（三件 sha256 前 12 位 bde310271e55 / a37c4285e6c9 / 80534f28667b，搬前搬后一致）；v0 追问 A–E 作废 | 用户 09-04「不用管 sol 出的题啊，那个我觉得不太好用，所以是想让你从头再出」 | OS §7（出题归 AI）；§1 PASS 条件原文不变；§5 冷复测日期不变（D+2 = 09-05，日志已密封 `_sealed/EX-00_retest_D2.md`）；hint 级记账沿用 `_v0_sol/GRADING.md` 口径（用户已见 Sol 批改中的状态 / 更新 / 输出 / 无 K 四句）**

| 项 | v0（Sol） | v2（Fable） |
|---|---|---|
| 练习日志 | 六条 A–F（现称 L1，第 1 / 5a 站继续用） | 新日志 L0（a–e 五活动六案例，含重复 trace、被拼盖 trace、重复相邻对、新起点四种性质）；L1 在 §5 作桥保留 |
| 考法 | 背判据 + 追问五空 | 逐 case 状态表（正序 + 逆序）、预测先于运行、改一个条件、与"程序乙（有 K）"对照、脱稿 |
| 密封 | `_sealed/_v0_sol/EX-00_answer.md` | `_sealed/EX-00_answer.md`（数字由参考实现实跑 + 720 序全枚举）+ `_sealed/EX-00_retest_D2.md` |
| 时长 | 一晚 | 一晚 2–3h（不变） |

**A3 · 2026-09-04 下午 | `EX-01/README.md` §2、`EX-03/README.md` 任务 1 两处"EX-00 那六条/EX-00 答案"改称"L1（EX-00 §5 桥接日志）"；无数字、无判据改动 | A2 把 EX-00 主日志换成 L0 后，这两处旧指针仍叫六条 A–F 日志"EX-00"，与 v2 的 L0（R=7）撞名，核对时容易看错成 R=8 | 纯引用勘误，不改 PASS 条件、不改站序、不属于 §16 "一周内大改"**

**A4 · 2026-09-05 | 用户批准“外围重排、地基不动”的双层计划差分 | 新形成的鲁法明研究谱系和 `Execution -> Structure -> Intervention` operator 改变本包完成后的研究出口，但不能抢跑 Algorithm 1 ownership | 决策档 `progress/decisions/2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md`**

- 本包冻结站序 `0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7`、题面和 PASS 条件全部不变。
- `EX-00 -> EX-01 -> EX-05a` 定义为 P0 地基；当前唯一游标仍是 EX-00 v2 §6 脱稿。
- EX-05a 后才解锁鲁法明谱系 citation audit；EX-05 后才做 DFR-equivalence sampling / EdgeIM / sigRank 横向比较；EX-06 后才填首张 Transfer Card；EX-07 PASS 且 Transfer Card=`PROMOTE` 后才允许一个 toy research test。
- 谱系档、AI 地图和 related-work 拆解只作输入，不计入本包 Ledger，不替代用户脱稿、反例或冷启动证据。
- 进组日期按 2026-09-03 用户更新理解为“9 月底、精确日期待定”；旧 `09-10` 不再作为压缩本站序的依据。

**A5 · 2026-09-05 | 用户纠正“不是四篇里只学 EdgeIM，另外三篇放着”，批准一主干三镜头的穿插式训练结构 | TASK-20260905-002 | 调度正本=`FOUR_PAPER_TRAINING_LOOP.md`**

- EdgeIM 仍是唯一主干和 ownership 对象；另外三篇不是平均精读，也不是统一后置。
- sigRank 是横向 sparring partner：EX-01 后短开一次 selection philosophy，EX-05 后做完整 fair comparison。
- Sommers Ground Truth Approach 是实验/证据方法论：EX-06 后读框架，EX-07 设计前必须产 world contract。
- CrossEdgeIM 是纵向 genealogy：EX-06 后重建 predecessor → residual → redesign → new residual；Transfer Card 阶段可再开 interaction-semantics residual。
- 四个镜头都不改变原站序和 PASS 条件，也不因“读过拆解件”计入 Ledger。

**A6 · 2026-09-05 | `TASK-20260904-004` 按用户“零基础、只做增量、提高可读性和信息密度、借 EdgeIM 长科研能力”的要求升级教学接口 | 不删原题、不重排路线；集中提交；把跨论文与跨领域问题放到受控卡或停放枝 | OS §4、§5、§7、§8、§10、§17**

本次只增加教学与证据接口。A1-A5、原题、历史说明和冻结 PASS 全部保留；当前唯一站序仍是：

```text
0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7
```

| 站 | 核心产物不变 | 本轮只增加什么 | 解锁后的研究动作 |
|---|---|---|---|
| 0 | 两种次序状态表与脱稿解释 | 当前对象、状态、输出的零基础入口 | 比较日志缩减方法；检查 `K`、顺序与保证是否属于原问题 |
| 1 | 三张 DFG、逐边次数、G0 note | 先区分事件位置、相邻对出现次数和不同边类型 | 审计 support/weight、下游读取项和异领域迁移上限 |
| 5a | 本人实现与两种顺序输出 | Python 对象与最小 system-reading 映射 | 区分实现错误和算法本身的顺序影响 |
| 2 | 手切过程树、PM4Py 对照、阈值解释 | 先 sequence，再 choice/parallel/loop；Petri net 正式定义暂缓 | 追踪日志、图、weight 分别在哪一步被读取 |
| 3 | 噪声例、上界、原文例子的权重变化 | 合法性 x 新颖性两轴先修 | 把“像 bug”改成竞争解释、最小反例与 closure 状态 |
| 5 | 不变量测试与生成器接管 | 测试词汇和四类证据边界 | 一条绿灯最多支持什么，怎样让反例真正改写 claim |
| 6 | T0、Measurement Contract、范围与时间线 | 缩写、四方 credit、claim-evidence 表 | 从测量缺口提出可被打脸的问题，不把架构推论写成实测 |
| 7 | 冻结预测、可复跑输出与 verdict | 全称猜想、观察检查、外部效度 | 写 falsifier、适用范围和更新后的 claim ceiling |

统一执行合同：

1. 新概念按“为什么需要 -> 2-4 个对象的无关微例 -> 正式定义且解释每个符号 -> 亲手操作 -> 接回 EdgeIM 上下游 -> 研究追问”出现；不再假设学习者懂 process tree、Petri net、测试术语或研究缩写。
2. `CONNECT` 在核心题后集中提交，但不提高原 PASS；`EXTEND` 可选，不做不影响 PASS。公开 [CONNECTIONS.md](./CONNECTIONS.md) 只列解锁点，具体卡由对应站核心题完成后授权。
3. 旧证据可用“路径 + 标题”引用并重新核对；预测、脱稿、冷启动和题面要求的本人修改必须产生新证据。AI 讲解、Agent 产物或答案暴露只记 `SEEN` 和 exposure，不自动成为能力证据。
4. 七图不是新课程。主干仍是 EdgeIM，当前小视窗只有 `weighted DFG -> 为什么描边不够 -> cut -> sequence cut`；每个节点只选 2-4 个自然枝。知识枝状态与站点验收状态分开，升级仅允许 Dependency、Repeated recurrence 或 Research leverage。
5. 系统阅读最低要求是 data flow、state before/update/after、algorithm step -> code anchor 和 observed behavior；源码注释量不算理解。每条主张和怀疑使用 [RESEARCH_NOTE_TEMPLATE.md](./RESEARCH_NOTE_TEMPLATE.md) 的 Evidence audit、Evidence closure 与 Research hooks；证明义务必须注明 implementation、model 或 abstraction。
6. EX-02 的公开核心仍是 `D + 正序 D'` 在六个阈值下共 12 棵树；逆序六棵只作 `EXTEND`。EX-07 的“任何 D”保留为全称猜想：一个反例可证伪，有限测试通过只能写“在已测范围内未被证伪”；trace replay 或给定日志 fitness 不等于模型语言等价。
7. CrossEdgeIM 的作者、三层数据流和 interaction limitation 已按主来源登记；它的正式 genealogy 仍按 A5 在 EX-06 后才解锁。“EdgeIM 的正式直接后继”、DES、formal verification、runtime assurance 与一般 MAS safety 均保持 `USER-RECONSTRUCTION / UNKNOWN`；后四者还要等具体 property、representation 和验证任务出现。流程合规不自动等于安全。

批改仍按 [START_HERE.md](./START_HERE.md#一次交一整站反馈一次说清) 的整批矩阵执行。研究树只帮助选下一动作，不替学习者填答案、改 Ledger、关闭 Mistake Log 或判定 `OWNED / TRANSFERRED / PASS / RETAINED`。

**A7 · 2026-09-06 | EdgeIM Mastery Gate v2.1 接入现行入口 | 用户要求围绕桌面框架重构学习计划和进组计划；执行档为 `learning/training/lu-edgeim-algo1/MASTERY_GATE.md`**

- 原站题面、站序 `0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7`、PASS 条件、答案密封和四论文镜头解锁点全部保留。
- `EX-04/` 不补建独立站；测量与证据边界改由 Whole-Paper Diagnostic 的缺口选择、EX-06 和 EX-07 承接。
- 用户报告实际执行已过 EX-03；这不是磁盘密封答案或 AI 讲解的替代证据。下一动作是 `MASTERY_GATE.md` §4.2 的 15 题诊断，完成前不新增站点、不开始实验。
- 进组准备按 2026-09-06 起的 W0→W4 滚动窗口推进，月底为软边界；精确日期确认后只压缩窗口，不跳过诊断、证据边界和冷启动复测。

**A8 · 2026-09-06 | 完整会话与新增桌面材料复核后的层级分离 | `TASK-20260906-004` | 计划重构初稿与输入回执见 `progress/decisions/2026-09-06__research__edgeim-plan-rewrite-draft.md`、`research/papers_lu/plan-rewrite-inputs-20260906/`**

- EdgeIM 学习主干、受控研究邻域和进组应用层分开记账；进组不是整个学习系统的目标。
- 用户提出的五层科研菌丝网作为导航设计输入；来源/责任/状态由 `CLAIMS / GOVERNANCE` 横切约束，失败证据可反向降级研究分枝。
- 新增材料中的跨领域论文、团队和数字继续标为待核验，不进入站点 PASS、Ledger 或对外事实表。

**A9 · 2026-09-15 | 09-20/09-25 日历日期脱钩，改为条件触发 | 用户拍板「09-20 本身要往后挪一点」，选定「脱钩日历，改成条件触发」 | 依据：`progress/decisions/2026-09-03__research__bridge-lu-execution-plan-v1.0.md` §13（同步修订，本条与之互为对照）**

- 本行第 103 行"总时长 15–20h → 22–28h"是 09-12 四论文全升 5/5 拍板后的既有事实，本次不改这一行；本次改的是这个新工作量与 `bridge-lu-execution-plan-v1.0.md` 原定 09-20/09-25 日历日期之间一直悬空未决的冲突（该冲突由 `progress/decisions/2026-09-12__research__four-paper-full-ownership-design-for-sol.md` §6 首次指出，三天未获用户表态）。
- `09-20 核心技术闭环冻结` / `09-25 对外包检查` 两个日历日期作废，改为条件触发：`ownership-v3/` 四个 EdgeIM 桥接模块 `B-S2`/`B-S3A`/`B-S3B`/`B-EVAL` 的用户能力状态全部到达 `PASS`（`ownership-v3/BUILD_STATUS.md` 资产轴之外、独立的用户能力轴）即视为核心闭环达成；`09-25` 窗口起点随之改为触发日，窗口本身长度不变。
- `B-DEFENSE` 与三篇镜头论文（sigRank/Ground Truth/CrossEdgeIM 各自 P0-P3）的全文 ownership 不计入本次触发条件，继续按长期四篇 5/5 目标推进，不受此次冻结点变动加速或延后。
- 本条不改变、不豁免站序、PASS 条件、密封答案、Ledger 记账或冷启动复测的既有规则；也不把资产轴的 `BUILT/QA-PASS` 与用户能力轴的 `PASS` 混用作触发依据——详见 `bridge-lu-execution-plan-v1.0.md` §13 第 4 条。
- 待办（本次不动）：`progress/projects/lu-side.md`、`progress/projects/jinzu-sprint.md` 两张路由卡的 `last_verified`（停在 2026-09-05）和 DDL 表尚未反映 `ownership-v3/` 落地与本次触发条件变更，需单独一轮更新。
