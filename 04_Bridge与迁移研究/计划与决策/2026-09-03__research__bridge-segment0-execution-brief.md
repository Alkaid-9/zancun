# Segment 0 执行作业书

**Date**: 2026-09-03 Asia/Taipei
**Task**: `TASK-20260830-004` / Segment 0
**Parent**: `progress/decisions/2026-09-03__research__bridge-lu-execution-plan-v1.0.md`
**Status**: `READY-TO-DISPATCH`
**Executor**: Codex 主窗 + ≤3 parallel agents（总并发 ≤4）
**Duration**: 1–2 天
**Gate**: 四表完成 → 主窗口审阅 → 用户明确确认 → v1.0 升级 `EXECUTION-SPEC-FROZEN` → 进入段 1

---

## 0. 目标

段 0 不是"开始研究"，而是把 v1.0 从 APPROVED 推进到 EXECUTION-SPEC-FROZEN。

**四项交付物**（段 0 不写实验代码、不运行实验）：

本段不重新评估 R1 是否值得做，只冻结其可执行规格。R1 的主对象是采样策略在匹配预算下保留了什么；下游过程发现仅作为后果检查。主实验默认只选一类扰动，另留一类备用，不扩展为多噪声或全链路比较。

| # | 交付物 | 写域 | 冻结条件 |
|---|---|---|---|
| T1 | 核心论文核对表 | `_scratch/seg0/T1_paper_verification.md` | 每篇：DOI/全文/实现/关键细节缺失 四栏全填 |
| T2 | 操作化 Measurement Contract | `_scratch/seg0/T2_measurement_contract.md` | 5 项各有：数学定义 + toy example + 边界 + 代码字段 + 作废条件 |
| T3 | CORE / ADJACENT dependency graph | `_scratch/seg0/T3_core_adjacent.md` | 每个知识点标 CORE/ADJACENT + 理由 |
| T4 | 时间倒排与降级表 | `_scratch/seg0/T4_reverse_schedule.md` | 可用小时 → gate 小时 → buffer → 降级触发线 |

写域：`research/tracebridge_full_spectrum_20260830/00_control/_scratch/seg0/`

---

## 1. 依赖图（DAG）

```
                    ┌─── A1 (文献身份核实) ──────────────────────┐
                    │                                            │
 DISPATCH ──────────┼─── A2 (EdgeIM 结构化精读) ────┐            │
                    │                               ├──→ B1 (Measurement Contract 草案)
                    ├─── A3 (PM4Py IM API 能力盘点) ┘            │
                    │                                            │
                    └─── A4 (日历/课程/小时预算审计) ─────────────┼──→ C1 (时间倒排)
                                                                 │
                         B1 ──→ B2 (CORE/ADJACENT 草案)          │
                         A2 ──→ B3 (扰动类型选择建议)            │
                                                                 │
                         B1 + B2 + B3 ──→ C2 (四表冻结 gate) ───┘
```

**关键路径**：A2 → B1 → B2 → C2

---

## 2. 串并行方案

### Wave 1 — 三路并行（Day 1 上午）

 A1–A3 无依赖并行发射；A4 由主窗口在回收后完成，不占用额外并发槽位。

| Slot | ID | 任务 | 输入 | 产出 | 写域 |
|---|---|---|---|---|---|
| Main | — | Dispatch + 等回 | v1.0 | — | — |
| Agent 1 | A1 | 文献身份 + 源可用性核实 | v1.0 §5.1 固定文献清单 | T1 草案：每篇 × (身份/全文状态/实现状态/关键缺失) | `seg0/T1_paper_verification.md` |
| Agent 2 | A2 | EdgeIM 原文结构化精读 | EdgeIM PDF 或提取 Markdown | 7-field paper note 草案 + 三阶段技术摘要 + 未公开细节清单 | `seg0/A2_edgeim_paper_note_draft.md` |
| Agent 3 | A3 | PM4Py IM/IMf API 能力盘点 | PM4Py 文档 + 源码 | API inventory（IM 参数、输入输出、fitness/precision 计算函数、版本） | `seg0/A3_pm4py_api_inventory.md` |
| Main（A1/A2/A3 回收后） | A4 | 日历小时预算 | 09-03 → 09-25 日历、课程表、已知维护任务 | 可用深度/低强度/后台小时 + 课程冲突表 | `seg0/A4_calendar_budget.md` |

**每个 Agent 的 prompt 顶部必须含**：

```
URL cap: arxiv.org, github.com, pm4py.fit.fraunhofer.de, novaresearch.unl.pt, link.springer.com, pypi.org
word cap: ≤ 1500 字
time cap: ≤ 15 分钟
done_when: 对应表/草案完整，无 [TODO] 占位
tool cap: forbidden_sed_heredoc; 不写实验代码; 不改 v1.0; 不 commit
```

---

### Wave 1 回收 + 主窗口审阅（Day 1 中午）

主窗口做：

1. 核对 A1 输出：哪些全文已在盘、哪些需要授权下载、哪些实现确认不存在
2. 审阅 A2 paper note：标注"用户必须自己重读的部分"（ownership 要求）
3. 审阅 A3 API inventory：确认 IM 作为 primary downstream 的 API 可行性
4. 审阅 A4 日历：与用户确认课程安排

**Gate W1**：A1–A3 回收并经主窗口审阅；随后主窗口完成 A4 → 进入 Wave 2。每条事实标注来源事实 / 本地文件事实 / Agent 推断 / 待用户决定。

---

### Wave 2 — 两路并行（Day 1 下午 或 Day 2 上午）

| Slot | ID | 任务 | 依赖 | 产出 | 写域 |
|---|---|---|---|---|---|
| Main | — | 审阅 B 输出 + 做决策 | — | — | — |
| Agent 1 | B1 | Measurement Contract 草案 | A2 (paper note) + A3 (API) | 5 项各含：数学定义、分子/分母、toy example (≤10 traces)、边界情况、代码字段名、作废条件 | `seg0/T2_measurement_contract.md` |
| Agent 2 | B3 | 扰动类型选择建议 | A2 (未公开细节清单) | 推荐 1–2 类主实验扰动 + 理由 + 其余候选 | `seg0/B3_perturbation_recommendation.md` |

B2 (CORE/ADJACENT) 不在此波：它依赖 B1 的 measurement contract 方向，需要 B1 审阅后才能起草。

---

### Wave 2 回收 + 主窗口审阅

主窗口做：

1. 审阅 B1 measurement contract：逐项检查数学定义是否可执行、toy example 是否说得通、边界是否覆盖
2. 审阅 B3 扰动推荐：决定主实验用哪 1–2 类
3. 如有问题，退回 B1 修改（同一 agent 续跑，不另起）

**Gate W2**：B1 measurement contract、主扰动选择和 primary downstream 均明确；状态只能为 PASS、RETURN 或 BLOCKED。PASS 才进入 Wave 3。

---

### Wave 3 — 两路并行（Day 2）

| Slot | ID | 任务 | 依赖 | 产出 | 写域 |
|---|---|---|---|---|---|
| Main | — | 最终审阅 + 冻结 | — | — | — |
| Agent 1 | B2 | CORE / ADJACENT dependency graph | B1 (frozen contract) + A2 (paper note) | 知识链每节点标 CORE/ADJACENT + 理由 + 对 R1 的必要性评级 | `seg0/T3_core_adjacent.md` |
| Agent 2 | C1 | 时间倒排 | A4 (calendar) + B1 (contract) + v1.0 §9 | 各段 gate 最低小时 + 最坏缓冲 + 降级触发线 + 09-20 可行性判定 | `seg0/T4_reverse_schedule.md` |

---

### Wave 3 回收 → 冻结 Gate（主窗口 + 用户）

| 检查项 | 通过条件 |
|---|---|
| T1 论文核对表 | 固定文献实体均填完，全文状态明确（可读/提取文本/受限/缺失） |
| T2 Measurement Contract | 5 项均有数学定义 + toy + 边界 + 代码字段 |
| T3 CORE / ADJACENT | 每节点标注完毕，执行门生效 |
| T4 时间倒排 | 09-20 判定为 FEASIBLE（或降级方案已列） |
| 主实验扰动类型 | 已选定 1–2 类 |
| Primary downstream | IM 已确认可行 |

全过后由主窗口提交用户确认；用户明确批准后，才将 v1.0 status 升级为 **`EXECUTION-SPEC-FROZEN`**。该状态不等于已授权公开、发邮件或运行实验。

---

## 3. Agent 写域隔离

```
research/tracebridge_full_spectrum_20260830/00_control/_scratch/seg0/
├── T1_paper_verification.md        ← A1 写
├── A2_edgeim_paper_note_draft.md   ← A2 写（用户后续必须自己重读）
├── A3_pm4py_api_inventory.md       ← A3 写
├── A4_calendar_budget.md           ← A4 写
├── T2_measurement_contract.md      ← B1 写
├── B3_perturbation_recommendation.md ← B3 写
├── T3_core_adjacent.md             ← B2 写
└── T4_reverse_schedule.md          ← C1 写
```

每个 agent 只写自己的文件。主窗口审阅时可在同目录写 `_review_*.md`。不触碰 v1.0、00_control 其他文件、progress 面、TODO、INDEX。

---

## 4. 不做清单

- 不写实验代码
- 不建公开仓库
- 不安装依赖或运行第三方代码
- 不修改 v1.0 结构（只在段 0 结束时改 Status 一行）
- 不下载超授权范围资料（EdgeIM PDF 如果不在盘上，先报告缺失，等用户授权）
- 不 commit / push

---

## 5. 失败分支

| 场景 | 动作 |
|---|---|
| EdgeIM PDF 确实不在盘上 | A2 改用已有提取文本 `07_EDGEIM.md`；T1 标记 PDF 缺失待用户补 |
| sigRank 全文无法合法取得 | T1 标记；主实验 baseline 改为"无 sigRank 实现"，只留 random + frequency-aware |
| 09-20 倒排判定 NOT FEASIBLE | C1 输出降级方案；用户决定是否采纳 |
| Measurement contract 某项无法定义 | B1 标记 BLOCKED + 理由；主窗口决定是否退回 R1 scope |

---

## 6. 恢复入口

- 本文件 + v1.0
- 如果中途断开：读本文件 §2 判断当前在哪个 Wave → 从对应 Gate 继续
- 四表写域固定在 `_scratch/seg0/`，回收时从该目录读
