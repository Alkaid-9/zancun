---
title: 科研体系通宵窗交接快照（TASK-20260904-001）
date: 2026-09-04 06:00 +0800
source: Fable 5 主窗通宵跑（00:34–05:5x）
authority: RUNSTATE @ research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__overnight-research-system__RUNSTATE.md
---

# 交接快照 — 科研体系通宵窗

**用户进度**：已回电脑前  
**状态**：TASK-20260904-001 `completed_with_open_gates`（INDEX sha f2a32b6f）  
**未 commit**：所有新文件都是 `??` 状态

---

## 🎯 产出总览（18 件）

### 泳道 A — 桥线三篇拆解（13 件）

```
research/papers_lu/teardown-bridge-20260904/
├── 10_SIGRANK.md                    # 合并件（61 KB，errata 5 条）✓
├── 10_SIGRANK_p1/p2/表格/10b_*.md   # 部件 4 + 独立批判 ✓
├── 11_CROSSEDGEIM.md                # PARTIAL（图内数字缺）✓
├── 11b_CROSSEDGEIM_kg_critique.md   # 独立批判 ✓
├── 12_SOMMERS.md                    # 合并件（55 KB，§4/5 间插交叉核对块）✓
├── 12_SOMMERS_p1/p2/12b_*.md        # 部件 3 + 独立批判 ✓
├── 13_BRIDGE_SYNTHESIS_20260904.md  # 合成件：§4 21 条存疑 + §6 读序 ✓
├── 14_VISUAL_READINGS_20260904.md   # 图不可读标注 ✓
└── MANIFEST_ADDENDUM_20260904.md    # 三 PDF 登记（来源 [需核实]）✓
```

**三篇硬约束守住**（13 件全扫）：
- ✅ 零 G0 五问答案
- ✅ EdgeIM 处仅原句英引 + "见 §IV.B 用户自读" 指针
- ✅ 零写 bridge 卡 :27 结论（采样后边权失真）

### 泳道 B — 三库整理（4 件）

```
research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/
├── B1_pengsida_component_audit.md                  # 组件审计（RWA 13/RO 8/REJECT 1）✓
├── B2_supervisor_skills_handbook_methods.md       # 方法抽取表（RWA 17/RO 6）+ 5 条 open ✓
├── B3_research_growth_index.md                    # 导航索引（3 条 open）✓
├── B4_research_system_v0_PROPOSED.md              # 体系 v0 PROPOSED（§6 拍板 5 项）✓
└── C3_todo_lines_PENDING.md                       # TODO 三行（dry-run 过，待口令）✓
```

**B5（三库→第 1 站读法）**：由训练包窗 b270bae5 先写（EX-01_reading-method_3KB.md），零碰撞。

### 登记与验收（C1–C5）

- C1 合并：sigRank 62 KB + Sommers 56 KB ✓
- C2 逐件自检：18 件全检，禁用词/G0 词/EdgeIM 泄露零命中 ✓
- C3 TODO 三行：dry-run 过，正文在 C3_todo_lines_PENDING.md（等口令）
- C4 task log 收尾 + INDEX CAS 改状：sha 6b87ad0b → f2a32b6f ✓
- C5 memory 更新 ✓

---

## 📍 三篇论文内部矛盾一览

**引用数字前必读**：`13_BRIDGE_SYNTHESIS_20260904.md` §4 存疑表（21 条）

### sigRank TSC 2026
- **Table III 时间 84306 ms vs Fig.6 读数 ~180k** → 疑似实现层数值/图读数不清
- **"10/12 优于 LogRank"** 三种计数规则都复算不了 → 可能是归一化或表述不清
- Table I–III 全是图像嵌入，格内数字都是视觉判读 `[图读数]`

### CrossEdgeIM IoT Mag 2026（校样版）
- **IM 基线 ECyM 全落 10004–10009** → 疑饱和值，Complexity 对比只由 ECaM 驱动 `[需验证]`
- **数据标签"机器人日志"** + "#Dep." 列 → 疑为医疗跨科室日志改标签 `[需验证]`
- Fig. 1/Fig. 3 图内数字未判读 `[PARTIAL]`

### Sommers Process Science 2025
- **BI 编号不一致**：正文 BI1 vs Table 2 BI3 → 按 Table 为准
- **p.28 "No datasets" vs p.18 gitlab 链接** → 前后不一
- **摘要"quantitatively" vs 结论"qualitative"** → 用词矛盾

---

## 🔗 三库实际用法（研究体系 v0 里）

### Supervisor-Skills（https://github.com/HKUSTDial/Supervisor-Skills）

**用上的**：
1. 审稿四喜四厌（1.1）→ 反转成**读论文追问表**
2. Intro 六段 + 论文思考模板（3.2–3.3）→ 空表，用户填 + AI 判
3. 符号表/自造例子/不看图重画（3.5）→ 手跑前检查清单
4. 案例剖析法（6.1–6.3）→ Flowchart 表映射原文的拆解套路

**冲突 / 未用**：
- 05 章 Vibe Research 心法（"AI 能做就不人工做"）→ 与用户 OS 直接冲突 ← **§5 拍板项**
- idea 能力匹配、顶会门槛 → 口径太 DB，用户当下不适用
- 绘图三范式 → 内容少，当下无任务

**许可**（CC BY-NC-SA 4.0，Yuyu Luo + contributors）：
- 摘出来的任何模板都是改编 → 需署名 + 非商业 + 相同方式共享
- 若 research_growth 日后公开 → **NC 条款需用户确认**

### pengsida learning_research + research_growth

**角色分工**（B4 §3 读法清单）：
- **Supervisor-Skills** = 方法论 baseline（读论文和想 idea 的追问框架）
- **pengsida** = 实例库（值得学的东西）
- **research_growth** = 用户定制（已读论文的做法档 + 与 SS/pengsida 的映射）

**目标用法**：用户边读论文边填 SS 的空表，research_growth 记"这篇怎么用 SS 的框架"。

---

## 🎛️ 用户决策门（五项，无法 AI 自主）

### 1. TODO 三行（铁律 8 新挂项）

**位置**：`C3_todo_lines_PENDING.md`

**三行内容**：
- 工作台三仓（Reviva / ebbingflow / LearnGraph）link/clone/fetch 状态核实
- 桥线三篇拆解完成度核实
- 三库整理（B1–B4）产出落 research_growth

**状态**：dry-run 通过，待你说"挂"才经 `ledger_edit.py` 写入 `progress/TODO.md`

**为什么需要你口令**：TODO 是共享登记面，/goal 授权("整理三库+拆解三篇")不覆盖"新挂项"。

### 2. 三 PDF 来源补充

**位置**：`MANIFEST_ADDENDUM_20260904.md` 三行

三行都标 `[需核实]`，需补充：
- P2 sigRank → IEEE Xplore / 机构库 / 校园网 / 作者提供？
- P3 CrossEdgeIM → （校样版，来源？）
- P4 Sommers → Springer OA 还是其他？

**一句话 × 3 即可**。

### 3. 附录并入决定

**问**：主 `MANIFEST.md` 是 08-12 历史档案（6+1 篇），附录是新加（3 篇）。并进主表吗？

**风险**：并进等于改历史档案，需单独口令。

### 4. B4 §6 五项拍板

**位置**：`B4_research_system_v0_PROPOSED.md` §6（第 1–5 条，各标 `[建议]`）

**拍板项**：
1. L0–L5 骨架采纳否
2. Supervisor-Skills CC BY-NC-SA 署名层级（改编署名写哪层）← **许可相关**
3. handbook 05 章心法与 OS 的张力（采哪一侧）
4. 六篇高手经验 txt 重抽规划（共享还是私有）
5. AI 导出件（导图）移出否

### 5. Commit 全量

**文件**：全是新增 `??` 状态

```bash
git add research/papers_lu/teardown-bridge-20260904/ \
        research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__* \
        progress/task_logs/2026/09/2026-09-04__*

git commit -m "TASK-20260904-001 科研体系通宵窗：三库整理+桥线三篇拆解完成…"
```

---

## 🔄 断点续跑（RUNSTATE 权威）

**authority 文件**：
```
research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__overnight-research-system__RUNSTATE.md
```

**用途**：
- 泳道 A/B/C 单元表 + 自检结果
- 事件日志（13 次派发、3 次错误、2 次 SendMessage 续跑详细记录）
- 收尾清单（每件 sha256 前 8 位）
- 若需续接其他任务，以此文件为准

**硬约束开工清单**：
- [ ] 读 RUNSTATE（盘面权威）
- [ ] 读 task log frontmatter（status/边界/开着的门）
- [ ] 读 C3_todo_lines_PENDING.md（待口令的三行）
- [ ] 读 B4 §6（拍板 5 项）
- [ ] 读 13_BRIDGE_SYNTHESIS_20260904.md §6（读序）

---

## 📊 训练包窗的关联产出

**都在 `learning/training/lu-edgeim-algo1/` 下**（不混 bridge 产出）：

| 站 | 题面 | 密封答案 | 批改 | 备注 |
|---|---|---|---|---|
| EX-00 | ✓ | ✓ | **NOT PASS YET**（差 5 空） | Sol 泄答→hint 级；#1 CLOSED 推 09-05 冷复测 |
| EX-01 | ✓ | ✓ | — | 读法附页 `EX-01_reading-method_3KB.md` 已落盘 |
| 其他 6 站 | ✓ | ✓ | — | 题面密封齐全 |

**待口令**（训练包窗）：TODO/INDEX/task log 登记、commit、LearnGraph 复核、Sepsis 下载。

---

## 🛠️ 技术亮点

### 子代理失败模式与解药

已记入 memory `subagent-channel-constraints.md` 09-04 追加段：

1. **"completed 但无文件"** → SendMessage 续跑（省 PDF 重读）
2. **卡在图表循环重读** → 派单硬写"每页最多 2 次" → 16 分钟完成（vs 60 分钟 0 产出）
3. **两段式写盘** → 先骨架（可回收）+ 再最终版（被 429 杀不全丢）
4. **429 是网关级** → 与并发无关；7 分钟退避后重发即过

### 过程质量数据

- **总 13 次派发**，≤2 并发
- **三次上游错误**（520×1、起跑即 429×2）
- **三次被 429 杀回执**（产出零丢失）
- **一次走错目录**（cwd 漂移，已复核清理）
- **产出 18 件全自检通过**

---

## 📝 提醒

### 千万别碰
- `learning/training/` 路径（训练包窗在用）
- `_scratch/seg0/` 路径（训练包窗在用）
- bridge 卡 `teardown-joint-20260813/bridge/EDGEIM_T2_bridge.md:27` 那个结论

### 来源待三核
- 三 PDF 下载来源（附录 `[需核实]`）
- 17 MB handbook PDF 未读（B2:108 标 `[需验证]`）
- pengsida_pdfs 五份 + 六 txt 的同源性（B4 §3 row 3 `[需验证]`）

### 许可要留心
- CC BY-NC-SA 4.0（Supervisor-Skills）→ 若 research_growth 公开需确认 NC 条款
- 08-31 REUSE_AUDIT 的署名/改编层级规则（§4 row 6、§2.3 `:97-107`）

---

**恢复入口**：RUNSTATE + task log + C3_todo_lines_PENDING.md + B4 §6

**下一步选项**：
- A. 批准五项拍板 → 我写 TODO/commit/汇总
- B. 查看 13_BRIDGE_SYNTHESIS.md §4 存疑表详情 → 决定信不信哪些数字
- C. 回到训练包窗协作 EX-01+ → 我等支援信号
