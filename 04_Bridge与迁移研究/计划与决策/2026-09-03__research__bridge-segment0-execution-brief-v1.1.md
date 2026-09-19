# Segment 0 执行作业书 v1.1

**Date**: 2026-09-03 Asia/Taipei
**Task**: `TASK-20260830-004` / Segment 0（第二轮）
**Supersedes**: `2026-09-03__research__bridge-segment0-execution-brief.md`（v1.0，10:24，保留不改）
**Parent**: `2026-09-03__research__bridge-lu-execution-plan-v1.0.md`
**Status**: `PROPOSED-DRAFT（待用户批）→ 批后 BLOCKED-ON-G0 / NOT-DISPATCHABLE`
**Gate 链**: G0（用户）→ T0 裁定（用户）→ T1'–T4' → 用户确认 → v1.0 升 `EXECUTION-SPEC-FROZEN`

> **本版生效前提（2026-09-03 晚 Sol 复审补）**：本文件由用户口令「新开一版 -v1.1」授权*写出*，
> 尚未被授权*生效*。它与规划日志两条已记录的用户决策相抵，须用户显式改判后才能启动：
>
> | 冲突 | 规划日志原文 | 本版立场 | 需用户裁定 |
> |---|---|---|---|
> | W2 已由用户冻结 | `C-043`：W2 = `FROZEN / PASS`，「不得反向修改已冻结 Measurement Contract；如确需修改，必须走 amendment log」 | T2 已移入 `_withdrawn/`（用户口令「不能用的直接归档」） | 是否以 `C-069` amendment 记「W2 冻结撤销，理由=matched-K 前提与 Algorithm 1 原文不符」 |
> | 停止新增 Gate | `C-065`：「不再新增 harness 功能、Gate、版本字段…」 | 新增 G0 / T0 / `_gate_*.md` 制度 | C-065 针对的是实现层 harness gate；G0/T0 是研究对象层门。是否视为不同类而放行 |
>
> 另：`progress/handoff/2026-09-03__bridge-r1-pilot__pause-handoff.md:44` 仍写「四表完成、W2 FROZEN/PASS」，
> 与本版及 `_withdrawn/README.md` 冲突，待同一条 amendment 一并消费。
> **在 `C-069` 落盘前，本文件不得作为任何派发的依据。**

> v1.0 的段 0 在 **44 分钟**内跑完了写着「1–2 天」的流程（10:24 派发 → 11:08 四表齐），
> 四张表里两张作废、一张半作废。v1.1 的每一处改动都指向同一件事：**让门有成本**。

---

## 0. 与 v1.0 的四处差异

| # | 改动 | 原因 | 依据 |
|---|---|---|---|
| 1 | 新增前置阻断门 **G0**：用户亲自读 Algorithm 1 并写 paper note，未过不启动任何 agent | v1.0 §63 把 paper note 派给 A2；note 由 agent 写、用户未重读，之后 T2/T3 全建在上面 | OS §7「论文 reasoning 必须长在本人身上」、§10.6 |
| 2 | **A2 降级为 fact extraction**：只交页码与逐行原文摘录，不做理解、不填七字段 | 同上。关键路径的第一个输入不能是解释 | OS §7 |
| 3 | **原件不可得 = BLOCKED**，不降级到提取文本 | v1.0 §174 预批了降级路径，于是 A1 的假阴性（PDF 误判缺失）没有触发任何升级，直接往下走 | 本轮实证 |
| 4 | **每道门必须留 `_gate_*.md`**，逐项写判定与依据；无此文件不算过门 | v1.0 的门只写「主窗口审阅」。第一轮的过门记录只存在于规划日志 `C-042`（CONDITIONAL-PASS）/`C-043`（用户 FROZEN/PASS），日志里没有逐项判定，也没有消费 `A2` §9 的「不授权」flag——用户是在没看到这条 flag 的情况下批的 | 本轮实证 |

另**删除 v1.0 §19**「本段不重新评估 R1 是否值得做，只冻结其可执行规格」——
研究对象已变，该句现在会锁死唯一出口。

---

## 1. G0｜前置阻断门（用户，不可派）

**做什么**：读 `research/papers_lu/EdgeIM-2025-ICWS.pdf` 的 Stage-1 preprocessing /
feature-preserving sampling 一节（含 Algorithm 1），写一份 paper note。

**为什么不可派**：这是 OS §7 划入「必须长在本人身上」的两项之一（另一项是核心算法）。
第一轮的失败点正在此处——**flag 都产出了，没有任何一步负责消费**：

- `A2_edgeim_paper_note_draft.md` §5 第 3 条已把「sampling unit 和终止条件」列为未验证
- 同文件 §9 明写「**not sufficient to freeze B1 or authorize code**」
- 18 分钟后 B1 照跑，产出 T2 并被记为 `FROZEN / PASS`

**note 必须回答（少一条不算过 G0）**：

1. Algorithm 1 的输入、维护的状态、保留判据、终止条件、输出各是什么
2. 它有没有预算参数？保留量由什么决定？
3. **过滤后 DFG 的边频次是在 `D′` 上重算，还是从原始日志带过来？**（← 决定 R1 还有没有）
4. Stage 1 的全局 `R` 是否带权，与 Stage 2 局部 `Ri`（原文称 weighted）是什么关系
5. 每条陈述标 `PAPER-TEXT` / `USER-INFERENCE` / `AGENT-SUMMARY` / `UNKNOWN`

**产出**：`_scratch/seg0/G0_user_paper_note.md`（用户写）
**通过条件**：五问全答，第 3 问有明确 `PAPER-TEXT` 依据（页码/段落）
**不通过**：整份作业书不启动。**不允许用 `_launch/pdftxt/EDGEIM.txt` 替代**——
那是双栏乱序抽取，可用于定位，不可用于判定。

---

## 2. T0｜研究对象裁定（用户，G0 之后）

段 0 第二轮的目标不再是「冻结 R1 的可执行规格」，而是先判定
**R1 是否仍然是一个研究对象**。G0 的答案会把它推向以下之一（不预设）：

| 选项 | 触发条件 | 后果 |
|---|---|---|
| A｜撤销 R1 | 判据确认为集合包含，且频次问题不成立 | H1 是定义的推论，无可实验内容；换对象 |
| B｜降级为有边界复现 | 想先建立 ownership 再提问 | 实现真 Algorithm 1（约 15 行，`_features` 已在），不提研究问题 |
| C｜转向频次问题 | G0 第 3 问确认频次在 `D′` 上重算 | 新问题：feature-preserving 保住边集、压平频次分布，是否使下游频次型噪声过滤失效 |
| D｜其他 | — | 用户提 |

**产出**：`_scratch/seg0/T0_object_verdict.md`（用户拍板，主窗口记录）
**这一步不派 agent。**

T0 未定之前 T1'–T4' 全部不启动——第一轮的教训就是在对象未定时先冻了规格。

---

## 3. 交付物（T0 之后）

| # | 交付物 | 写域 | 冻结条件 | 相对第一轮 |
|---|---|---|---|---|
| T1' | 文献核对表 | `seg0/T1_paper_verification_v2.md` | 每篇五栏全填：DOI / 全文状态 / 实现状态 / 关键细节缺失 / **检索命令 + 原始输出** | 第五栏为新增；旧版结论为假 |
| T2' | Measurement Contract | `seg0/T2_measurement_contract_v2.md` | 五单位各有：数学定义 + toy（≤10 traces）+ 边界 + 代码字段 + 作废条件 | **重写，不从旧版改** |
| T3' | CORE / ADJACENT | `seg0/T3_core_adjacent_v2.md` | 每节点标 CORE/ADJACENT + 理由 | 可搬旧版 §1 决策规则与 §4 ADJACENT 表 |
| T4' | 时间倒排 | `seg0/T4_reverse_schedule_v2.md` | 可用小时 → gate 小时 → buffer → 降级触发线 | 容量模型与 T4-A~D 四门沿用；分项工时随 T0 重排；修「14 天 vs 17 天」自相矛盾 |

---

## 4. 依赖图

```text
G0 (用户读原文) ──→ T0 (用户裁定对象)
                        │
                        ├──→ A1' 文献核对（agent，仅检索 + 命令留痕）
                        ├──→ A2' 原文摘录（agent，只抄不解释）
                        ├──→ A3  PM4Py API 清单 ← 沿用第一轮，仅重核版本号
                        └──→ A4  日历预算   ← 沿用第一轮，等用户补课表
                                 │
                        B1' ─────┴──→ T2'（主窗口起草，非 agent）
                        B1' ──→ B2' ──→ T3'
                        A4 + T2' ──→ C1' ──→ T4'
```

**关键路径：G0 → T0 → T2' → T3'。** 前两个都在用户身上，agent 不在关键路径上。
（v1.0 的关键路径是 A2 → B1 → B2 → C2，全是 agent。这是本版最实质的结构改动。）

---

## 5. Gate 制度（新增）

每道门由主窗口写 `_scratch/seg0/_gate_<门名>.md`，格式固定：

```text
门：<名>
时间：<起> → <止>
逐项判定：
  <检查项> | PASS / RETURN / BLOCKED | 依据（文件:行）
消费的 flag：
  <逐条列出上游文档里所有 未验证 / 待确认 / 不授权 标记，逐条写如何处理>
判定：PASS / RETURN / BLOCKED
```

**「消费的 flag」栏是这一版的核心。** 第一轮每个 agent 都正确标出了关键不确定性
（`A2` §5 九条 + §9 拒绝授权、`_withdrawn/T3` §3 第 51 行、`B3` 第 16 行），
一条都没被处理。这一栏强制把上游每个 flag 显式结清。

**无 `_gate_*.md` 不算过门。** 门的产出物写不完就是没过门——
这取代 v1.0 里没有约束力的「主窗口审阅」四个字。

---

## 6. 写域与 caps

写域：`research/tracebridge_full_spectrum_20260830/00_control/_scratch/seg0/`
每个 agent 只写自己的文件；主窗口写 `_gate_*.md` 与 `_review_*.md`。
不触碰 v1.0、v1.1、`_withdrawn/`、`00_control` 其他文件、`progress/`、TODO、INDEX。

agent prompt 顶部必须含：

```text
URL cap: <按任务给；A2' 为纯本地读取 → URL cap = 无>
word cap: ≤ 1500 字
time cap: ≤ 15 分钟
done_when: 对应表完整，无 [TODO] 占位，所有不确定项显式标 UNKNOWN
tool cap: forbidden_sed_heredoc; 不写实验代码; 不改 v1.0/v1.1; 不 commit;
          只摘录不解释（A2' 专属）
```

---

## 7. 不做清单

继承 v1.0 §4 全部六条，并加：

- 不用抽取文本替代 PDF 原件做算法判定
- 不由 agent 产出 paper note 或任何"理解层"文档
- 不在 T0 裁定前起草 measurement contract
- 不引用 `_withdrawn/` 内任何结论

---

## 8. 失败分支

| 场景 | 动作 |
|---|---|
| PDF 打不开 / 页面缺失 | **BLOCKED**，报用户，不降级到提取文本 |
| G0 第 3 问在原文中无法确定 | 记 `UNKNOWN`；T0 只能在 A / B 之间选（C 需要该答案） |
| T2' 某单位定不出来 | BLOCKED + 理由，退回 T0 重议对象 |
| 09-20 倒排判 NOT FEASIBLE | C1' 出降级方案，用户定 |
| 任一门 `_gate_*.md` 写不出来 | 该门未过；不得以「口头审过了」推进 |

---

## 9. 继承与作废

**沿用**：

- `A3_pm4py_api_inventory.md` —— 重核版本号（2.2.30/2.2.32 疑为过期文档镜像，PyPI 现行 2.7.x）
- `A4_calendar_budget.md` —— 仍等用户补课表，未关
- `A2_edgeim_paper_note_draft.md` —— 删「PDF 不在盘上」一行后作为**定位底稿**，不作为理解来源
- `B3_perturbation_recommendation.md` —— backup 与排除清单留，**primary 必换**（见下）
- `T4_reverse_schedule.md` —— 容量模型与 T4-A~D 四门留

**作废**：`_withdrawn/` 内 T1 / T2 / T3，理由见该目录 `README.md`。

**执行计划 v1.0 的作废条款**（该文件属决策面不改动，作废关系记在此处）：
§4.1–4.3（R1 设计与 H1）、§6.1（五单位表）、§6.4（匹配规模规则）、§6.5（指标池）。
v1.0 其余部分继续有效：§1.3 用户八条、§1.4 非目标、§6.2 实验闭环、§6.6 三级裁定、
§7 所有权、§9 时间盒、§10 失败分支、§11 诚实约束。
v1.0 的 Status 行仍为 `APPROVED / READY / NOT-YET-EXECUTING`，本版不改它。

**B3 primary 扰动必换的理由**：在 Algorithm 1 判据下，用现有字母表插入到非法位置
必然造出新 `r`，其首次出现必被保留——这部分是判据的直接推论。
但「因此 H1 恒真」说过头了（Sol 复审指出）：`D′` 的噪声占比是否高于随机采样，
取决于 distinct 非法边数与覆盖合法特征所需 trace 数之比，是道计数题，不是恒等式。
不需要实验，需要一页手算——这一页应进 G0 note。
替换方向见 `BRIDGE_LU_PLANNING_LOG.md` C-067（15:16）：优先加入不创造新 DFG edge 的对照。
注意这不是简单换一种扰动：对插入类噪声，「非法」与「造出新结构」在该判据下几乎同延，
可能只有属性层扰动（时间戳粗化）才是该过滤器看不见的——**这一点本身值得写进 T0**。

---

## 10. 恢复入口

- 本文件 + 执行计划 v1.0 + `learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md`
- 断线后：看 `_scratch/seg0/` 里有哪些 `_gate_*.md`，从最后一道已过的门继续
- 未见 `G0_user_paper_note.md` = 尚未开工

## Amendment

**A1 · 2026-09-03 晚 | 采纳独立审稿人 §2 四条，用户「其他的都同意」**

1. **§5 Gate 制度撤回**：不再要求每门 `_gate_*.md`（与 C-065 相抵，且是给一人项目造制度）。「消费的 flag」栏保留，改为 **T0 verdict 一节**的必填栏。§10 恢复入口相应改为：看 `G0_user_paper_note.md` / `T0_object_verdict.md` 是否存在。
2. **§1 / §8「原件不可得 = BLOCKED、不许用 TXT 判定」放宽**：PDF 在盘，问题不存在。改为：判定以 PDF 页码为准，`EDGEIM.txt` 用于定位。
3. **§3 T1' 缩表**：R1 缩到 Algorithm 1 后只依赖 EdgeIM 一篇；其余三篇降 ADJACENT 地图，T1' 成五行状态表。
4. **baseline 方向更正**：主对照是原始日志 **D 本身**（原文 zero-loss 就是相对 D 说的），随机等量采样只作次级控制。沿用的 `T4` §5 把 random-vs-coverage 列为不可降级——该行随 T4' 重排时改。
5. 新增 **实验段**：T3' 之后加 T5'（pre-prediction / 输入 / 指标 / verdict），对应训练包第 7 站。OS §10 ③ 的落点此前两份文件都没有。

T0 推荐方向（B 地板 + C 唯一研究问题）已获用户口头同意，正式裁定仍待 G0 note。
