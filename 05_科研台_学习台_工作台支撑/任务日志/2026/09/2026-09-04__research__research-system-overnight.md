---
id: TASK-20260904-001
title: 科研体系通宵窗：三库整理 + 桥线三篇论文拆解（无人值守自跑）
date: 2026-09-04
runtime:
  model: "Fable 5 (claude-fable-5-1[1M])"
  effort: max
  effort_source: "本会话 /model 输出「saved as your default … with max effort」+ 本轮 harness reasoning_effort=max 标记"
  launch: "Claude Code CLI (WSL)，/goal 设定 + Stop hook 守门"
type: research
status: completed_with_open_gates
area: bridge/learning
project: lu-edgeim-bridge
todo_ids: []
owners:
  - fable-main-window
related:
  - progress/task_logs/2026/09/2026-09-03__archive__codex-guardrail-and-bridge-pause.md
  - research/tracebridge_full_spectrum_20260830/00_control/BRIDGE_RESEARCH_LEARNING_REUSE_AUDIT.md
  - research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__overnight-research-system__RUNSTATE.md
---

## 目标

用户 2026-09-03 深夜口令：「这个窗口就做科研体系那边的东西吧——整理三个科研学习资料仓库，然后拆解几篇我们要用的论文……今晚直接跑完……注意自检，还要有超时重连和 429 之后的重连，整个定时检测」，并以 `/goal` 设为本窗目标。

范围（按盘面证据划定，不是按记忆）：

- **A 论文拆解**：桥线 T1 论文集里尚未拆解的三篇——`research/papers_lu/sigRank-2026-TSC.pdf`、`CrossEdgeIM-2026-IoTMag.pdf`、`Sommers-2025-ProcessScience.pdf`（依据 `_scratch/seg0/_withdrawn/T1_paper_verification.md` P2–P4 与执行计划 v1.0 :155-156）。EdgeIM 本身已有 `teardown-joint-20260813/07_EDGEIM.md`，且 Algorithm 1 是用户训练包的对象，**本窗不碰**。
- **B 三库整理**：`external/learning_research`（pengsida）、`external/Supervisor-Skills`、`research_growth`。08-31 复用审计已裁 META-CORE-A/B 与组件级 REUSE-WITH-ADAPTER；本窗**沿用不重审**，只补三件盘面缺的东西：pengsida 首轮组件审计、Supervisor-Skills handbook 方法抽取表、research_growth 导航索引；再合成一份 **PROPOSED** 的「科研体系 v0」索引（提案，不是权威；OS v0.1 FROZEN 不动）。
- **C 运行纪律**：≤2 并发子代理、4 caps + tool cap、429/超时重试、分段落盘、RUNSTATE 检查点、每单元自检。

## 边界（开工前钉死）

- 不碰训练包 `learning/training/lu-edgeim-algo1/`、EX-01、seg0、G0-T0（另一窗在做）。
- 子代理只读三库与 PDF；不给 G0 五问的答案；不写 bridge 卡 :27 那个结论。
- 所有产出落 evidence 层（`research/papers_lu/teardown-bridge-20260904/`、`00_control/_scratch/`、三库审计附录）；决策面（OS、REUSE_AUDIT 主文、BRIEF）不改。
- TODO/INDEX 只经 `ledger_edit.py`；不 commit、不 push。

## 最终结果

**完成（00:34–05:5x，无人值守，主窗 + 13 次子代理派发，≤2 并发）**：

- **A 论文拆解**：三篇全部拆完并各配一份独立视角 KG+批判，外加一份三篇合成注记，共 13 件落 `research/papers_lu/teardown-bridge-20260904/`。sigRank 5 件（p1/p2/表格回填/合并件/10b）；CrossEdgeIM 2 件（11 为 PARTIAL：Fig. 1/Fig. 3 图内数字未视觉判读；11b）；Sommers 4 件（p1/p2/合并件含主窗交叉核对块/12b）；合成件 13（§4 列 21 条交叉核对后仍存疑项，★ 三条最要紧）。另 MANIFEST 附录登记三 PDF 的 sha256/页数/DOI，来源 `[需核实]`。
- **B 三库整理**：B1 pengsida 首轮组件审计、B2 Supervisor-Skills handbook 方法抽取表、B3 research_growth 导航索引、B4 科研体系 v0 索引（**PROPOSED**，§6 列拍板项）四件落 `00_control/_scratch/2026-09-04__research-system/`。08-31 复用审计裁决沿用未重审。B5（三库→第 1 站读法）被训练包窗 b270bae5 先写，本窗 TaskStop 未写，零碰撞。
- **C 运行纪律**：RUNSTATE 检查点 85+ 行事件日志；cron 心跳每 15 分钟；每单元自检（头三行/章节/锚点计数/禁用词/G0 与 EdgeIM 泄漏扫描/2–3 处页码对 TXT 分页抽查）。

**未完成 / 开着的门**（详见"当前状态"）：TODO 三行等口令；三 PDF 来源待用户补；CrossEdgeIM 两图与 Sommers Table 3/Fig. 12 的图内数字未判读；B4 §6 拍板项；附录是否并入主 MANIFEST。

**三处铁律 1 意义上的原文内部矛盾（三篇都有，拆解件已标 `[⚠️矛盾]`）**：sigRank Table III ETMC4200 84306 ms vs Fig. 6 读数 ≈180k、正文"10/12 vs LogRank"三种计数都复算不出；Sommers p.10 "Skipping (BI1)" vs Table 2 BI3、p.28 "No datasets were generated" vs p.18 gitlab 链接、摘要 "quantitatively" vs 结论 "qualitative"；CrossEdgeIM IM 基线 ECyM 全落 10004–10009 疑饱和值。

## 修改内容

全部为**新增文件**，未改任何既有文件（决策面 OS/REUSE_AUDIT/BRIEF/主 MANIFEST/训练包/seg0 均未动）：

| 落点 | 文件 | 说明 |
|---|---|---|
| `research/papers_lu/teardown-bridge-20260904/` | `10_SIGRANK.md`（合并，含 errata 5 条）、`10_SIGRANK_p1.md`、`10_SIGRANK_p2.md`、`10_SIGRANK_p2_tables.md`、`10b_SIGRANK_kg_critique.md` | sigRank TSC 2026 |
| 同上 | `11_CROSSEDGEIM.md`（PARTIAL）、`11b_CROSSEDGEIM_kg_critique.md` | CrossEdgeIM IoT Mag 2026 校样 |
| 同上 | `12_SOMMERS.md`（合并，含交叉核对块）、`12_SOMMERS_p1.md`、`12_SOMMERS_p2.md`、`12b_SOMMERS_kg_critique.md` | Sommers Process Science 2025 |
| 同上 | `13_BRIDGE_SYNTHESIS_20260904.md`、`MANIFEST_ADDENDUM_20260904.md`、`_launch/pdftxt/{SIGRANK,CROSSEDGEIM,SOMMERS}.txt` | 合成 / 登记附录 / 定位用文本层 |
| `00_control/_scratch/2026-09-04__research-system/` | `B1_pengsida_component_audit.md`、`B2_supervisor_skills_handbook_methods.md`、`B3_research_growth_index.md`、`B4_research_system_v0_PROPOSED.md`、`C3_todo_lines_PENDING.md` | 三库整理 + 待口令的 TODO 三行 |
| `00_control/_scratch/` | `2026-09-04__overnight-research-system__RUNSTATE.md` | 检查点 + 事件日志 |
| `progress/task_logs/` | 本日志 + `INDEX.md` 一行（插入 sha c986cb7f→6b87ad0b；收尾改状态，见验收） | 登记面，经 ledger_edit.py CAS |

## 验收与证据

- **产出清单与哈希**：18 件 md 的字节/行数/sha256 前 8 位在 RUNSTATE"收尾清单"；关键件：10_SIGRANK 96b96ce0、11_CROSSEDGEIM 825e6aea、12_SOMMERS 599d9ef1、13 合成 2ecb7330、B4 70dfa7c7。
- **每件自检**（RUNSTATE 单元表"自检"列）：头三行固定；章节齐全；`[PDF p.N]` 锚点密度 63–247/件；禁用词（显然/毫无疑问/必然/一定是）13 件零命中；G0 五问词表与"迁移坑/失真"零命中；EdgeIM 处只有原句英引 + "见 §IV.B 用户自读"指针；每件 2–3 处页码锚点对 `pdftotext -layout` 分页抽查命中。
- **独立视角一致率**：sigRank 10↔10b 三点一致（top-N 单位冲突、0.5/0.5 无消融、m≪n 口径）；CrossEdgeIM 11↔11b 三点一致（单基线、模拟数据、[8] 仅 p.1 一处）；Sommers p1/p2↔12b 两点一致（BI 编号错位、p.28 数据声明矛盾）+ 12b 新增摘要/结论矛盾（合成件 §5 表）。
- **B 泳道**：裁定词全在 08-31 词表内（B1 RWA 13/RO 8/REJECT 1/RAI 1；B2 RWA 17/RO 6/REJECT 1）；B4 头四行含 `Status: PROPOSED`，10 处 `[建议]`。
- **运行纪律证据**：子代理 13 次派发，3 次上游错误（520×1、429×2 起跑即死）+ 3 次"回执前被 429 但文件已落盘"，0 次产出丢失；A3p2 三次尝试（尝试 1 在 p.25–27 循环重读 60 分钟无产出 → 尝试 3 加"每页 ≤2 次 + 两段式写盘"16 分钟完成）。
- **未做的验收**：无网络，合成件 §4 的三条 ★ 存疑（ProM 代码 / gitlab 仓 / TASE 仓）未能关闭；图内数字全部标 `[图读数]`/`[图读数不清]` 未做二次判读。

## 当前状态

- **已完成**：A1–A4、A5、B1–B4、C1、C2、C4、C5；B5 SUPERSEDED-BY-OTHER-WINDOW。
- **等用户口令（登记面 / 决策面）**：
  1. TODO 三行（`C3_todo_lines_PENDING.md`，已 dry-run，含逐行 CAS 命令）。
  2. 三 PDF 下载来源一句话 → 改掉附录 `[需核实]`；附录是否并入主 `MANIFEST.md`（08-12 历史档，需口令）。
  3. B4 §6 拍板项：L0–L5 骨架采否、Supervisor-Skills CC BY-NC-SA 署名层级、handbook 05 章张力、六篇高手经验 txt 重抽、AI 导出件移出。
  4. EX-01 读法附页合并（训练包窗 b270bae5 的文件 + B4 §3 的 25 条待合并清单）由训练包窗决定。
  5. commit（整目录 `??`）——本窗不 commit、不 push。
- **等条件（有网 / 人工看图）**：合成件 §4 ★ 三条；11_CROSSEDGEIM Fig. 1/3；12_SOMMERS Table 3 二次判读、Fig. 12 横轴；10_SIGRANK Fig. 6(i) vs Table III。
- **下一步建议（不决策）**：用户按合成件 §6 读序自读三篇；先读 Sommers（必要辅助），再 sigRank，CrossEdgeIM 只读 §9/总评。
- **回滚**：全部产出为新增文件；删除 `teardown-bridge-20260904/`、`_scratch/2026-09-04__research-system/`、`_scratch/2026-09-04__overnight-research-system__RUNSTATE.md` 与本日志即回滚；INDEX 行经 `ledger_edit.py --replace` 反向。
