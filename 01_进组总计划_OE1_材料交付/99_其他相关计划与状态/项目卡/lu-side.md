---
slug: lu-side
title: 鲁组线（W1_lu_side）
type: thin
sector: 重心1
line: research
status: ACTIVE
cadence: weekly
campaigns: [CMP-JINZU]
last_verified: 2026-09-15
---

# 项目卡（薄） - 鲁组线

> 本卡只做路由；治理与状态以 `research/map/W1_lu_side/` 为准。
> 所属：FOCUS 重心1 → line:research ｜ 注册：2026-08-22（TASK-20260822-005）
> **09-20 当前入口**：[进组学习当前路由](../../CURRENT_LEARNING_ROUTE.md)。本卡中的 MyResearch 路径与 09-06 行仅作历史追溯。

本线承接 EdgeIM 周围的研究邻域和鲁法明公开谱系核验；它不是 `jinzu-sprint` 的材料清单，也不把进组面试当作研究线的终点。

## 1 指向

- 地图区：`research/map/W1_lu_side/`
- TODO：`progress/TODO.md` research 分区（鲁组条目）
- 协作惯例：多窗并发时鲁线让先协议走 CROSSWINDOW 登记（08-21 有先例）

## 2 DDL 与节奏

随 2026 年 9 月底进组预期激活（精确日期待定；jinzu-sprint 卡联动）；cadence=weekly（用户令 2026-08-22）。当前 weekly 语义扩为按 mechanism 搜索，但仓内未发现独立自动扫描任务，不虚构调度状态。

## 3 里程碑镜像

- 9 月底进组后本线成为主工作环境之一；当前为预备态。
- 2026-08-22｜teardown-joint-20260813 窗口2 CLOSED-PASS（commit `dc90c0c`，G 级三路审计 PASS）；遗留 DEC-LU-U1~U5 挂 PENDING 待拍板。
- 2026-09-05｜采用 P0 EdgeIM 地基 → P1 谱系核验 → P2 深入 → P3 sampling 横比 → P4 迁移审计 → P5 最小研究；P1-P5 当前受前序门阻断｜TASK-20260905-001
- 2026-09-06｜EdgeIM 学习/进组执行接入 `learning/training/lu-edgeim-algo1/MASTERY_GATE.md` v2.1；用户报告已过 EX-03，先做 Whole-Paper Diagnostic，再按 W0→W4 进入月底滚动窗口｜TASK-20260906-001
- 2026-09-06｜按五层科研菌丝网分离研究地图、活动线、本人证据和进组应用；新增跨域论文与团队断言保持待核验｜TASK-20260906-004

## 4 在途窗口

```bash
grep "\[proj:lu-side\]" /mnt/d/MyResearch/CROSSWINDOW.md
```

## 5 当前技术门（2026-09-15 订正；09-06 原文保留于下方历史行）

**09-06 原技术门已被 09-13 v3 合同取代，不再是当前入口**：[v3合同](../../../02_四论文Ownership主线/00_共享合同_计划_验收/计划与决策/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md) §3 用 D0/D1/D2 三阶段诊断取代了 `MASTERY_GATE.md` §4.2 的十五题一次性诊断，且原文明确"不再用十五题阻塞施工"；D2（十五题的升级版、四论文全文冷诊断）被重新定位为四篇全文包完成后的**最终验收**，"不是用户当前继续 EX-05/EX-06 的前置"。

- 当前学习入口：v3合同 §1.3 的**用户恢复包**（=当前 D0，不额外再开一套整篇卷），六项具体动作：①亲自完成 EX-01 G0 五问 note；②集中补 C00/C01/C05a/C02 的 CONNECT；③补一张 L-S1 对照；④在统一 Research Note 中各补一条 EX-02 `SR-__` 和 EX-03 `EC-__`；⑤每个已学站补一句"它怎样改变我对整篇 EdgeIM 的理解"；⑥后续按冻结 rubric 复核，只有真实 PASS/冷测结果才能进入 Ledger。此恢复线不要求填七张地图、不要求做 EXTEND、不授权 AI 代写。
- 恢复包完成前：不补建 EX-04（若已存在按原节奏续接）、不启动新实验、不把四论文镜头或 AI 产物记作本人 ownership。
- 恢复包之后：沿主脊柱补齐整篇重建，再按解锁点打开 sigRank、Ground Truth 和 CrossEdgeIM；进组表达只消费已核验且有本人证据的内容。
- 研究地图入口：`WORLD / FIELD -> RESEARCH MAPS -> ACTIVE TRACKS -> EVIDENCE / PRACTICE -> ARTIFACTS`；所有层回链 `SOURCES`，由 `CLAIMS / GOVERNANCE` 记录来源、责任主体和状态。

09-06 旧文（保留作历史）：当前学习入口曾为 `learning/training/lu-edgeim-algo1/MASTERY_GATE.md` §4.2–4.3 的 15 题整篇诊断；诊断完成前不补建 EX-04、不启动新实验、不把四论文镜头或 AI 产物记作本人 ownership；诊断之后沿主脊柱补齐整篇重建，再按解锁点打开 sigRank、Ground Truth 和 CrossEdgeIM。

## 5 更新记录

- 2026-08-22｜立卡｜TASK-20260822-005
- 2026-08-24｜窗口2收口×库级清欠双任务会话归档包落盘（八件套=`progress/handoff/2026-08-24__lu-finishing-reposweep__archive/`，handoff INDEX 挂链走台账 #26）＋last_verified 刷新｜TASK-20260824-006
- 2026-09-06｜同步 EdgeIM Mastery Gate v2.1 与进组滚动窗口｜TASK-20260906-001
- 2026-09-06｜另一窗口产出孙猛团队谱系+鲁×孙交集矩阵草稿（`DRAFT/PROPOSED-AWAITING-USER-REVIEW`），指针=`progress/decisions/2026-09-06__research__lu-sun-intersection-matrix-and-group-entry-reframe.md`；不改本卡§5 当前技术门（诊断优先仍生效）｜TASK-20260906-003
- 2026-09-15｜§5 当前技术门指针从 09-06 的 15 题诊断优先，更新为 v3 合同 §1.3 的六项恢复包（D0）；`MASTERY_GATE.md` 正本未改，仅本卡路由指针接续；last_verified 刷新｜TASK-20260915-014
- 2026-09-20｜接入本仓当前学习路由，修复 v3 合同链接；先对账六项证据，不重新判用户 PASS。
