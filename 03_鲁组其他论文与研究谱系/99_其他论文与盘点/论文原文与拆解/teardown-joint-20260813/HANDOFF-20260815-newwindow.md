---
date: 2026-08-15
time: 22:5x UTC+8
type: cross-window-handoff
status: 主战役+收口已完成；三波后续增量（R改进重审/L框架补齐/F鲁×孙融合）15 路 Agent 在途，交接给新窗口收口
authoritative_entry: true
supersedes_for_resume: CHECKPOINT-20260815.md（主战役收口档，仍有效，本档是其后的增量波交接）
architecture: _launch/LAUNCH_PACKAGE_20260815.md（全 Agent ID 与写域矩阵）
no_commit: true
---

# 新窗口交接档 · 付费墙三篇战役的三波后续增量

> **▶ 2026-08-15 23:42 窗口2 完整存档**：`_archive_window2_20260815/README.md`（状态权威）。进度：R 7/7、F 4/4、L 1/4、ROADMAP ✅、SYN-A/C 在途。本档 §3/§4 规格仍权威；SYN 重发规格见档案包 `HANDOFF.md`。

> **🧊 2026-08-15 22:57 用户令冻结**：本窗不再发射新 Agent、不改已有产物。在途子 Agent 无法强制终止，会自行跑完并**追加**落盘（写域隔离、no-commit，不破坏已有物）。**冻结点快照**：R 波 5/7 落盘（缺 R1/R3）、L 波 0/4、F 波 0/4。晚落的文件＝加分项，新窗口重新 `ls` 即采纳；真缺的按 §3 重发。

## 0. 新窗口开局三步（照做）

1. **读四件**：本档 → `_launch/LAUNCH_PACKAGE_20260815.md`（Agent ID＋写域矩阵）→ `09_FAMILY_SYNTHESIS_V2.md`（七篇最新总览）→ `README.md` §四（战役全景）。主战役怎么打完的看 `CHECKPOINT-20260815.md`。
2. **盘点在途波产出**（本档 §2 有清单）：
   ```
   ls _review_20260815/ fusion_sun_20260815/ ; ls 0?b_*sixpoint*.md
   ```
   对照 §2 的"预期文件"表，落盘的=该 Agent 已完成；缺的=仍在跑或已阵亡。
3. **缺的按 §3 规格重发**（本会话 Agent 的完成通知新窗口收不到，但产物落磁盘，所以只认文件不认通知）；全落齐后做 §4 的三张合成表交用户。

## 1. 已完成（只读，勿重做）

- **主战役**：SBPN/EdgeIM/MHP 三篇拆解（`06/07/08`＋`06b/07b/08b`）、复现三 PASS（`repro/{sbpn,edgeim,mhp}/`）、bridge 三卡（`bridge/`）、综合 V2（`09`）、教学包（`teaching_paywall3/`）、四审计（`_audit_paywall3/G1-G4`）。
- **收口**：G 波 P0×2+P1×5+W1 全修；README §四、`99_USER_TODO_20260815.md`、`CHECKPOINT-20260815.md`、MANIFEST/PLAYBOOK/CROSSWINDOW 登记。
- **文献**：付费墙三篇已入档 `../{SBPN-2024-InfSci,EdgeIM-2025-ICWS,MHP-Seg-2025-CCPE}.pdf`；六+一篇全文 txt 在 `_launch/pdftxt/`（含旧四篇 SBTPN/PNULOCK/UAF/SEGLOCK＋SBTPN_supp，L 波已提取）。

## 2. 在途三波与预期文件（截至 22:5x 落盘状态）

写域全部隔离，互不相交；三波都是"只产报告/新增卡，不改任何已完成产物与旧卡 01-05"。

### R 波 · 改进空间重审（7 路，报告落 `_review_20260815/`）
性质＝质量上限审（非符合性审计，G 波已做完）。每报告格式：改进项【改进点/为什么值得/怎么做/成本/优先级 A-B-C】＋总评 top3。

| Agent | 对象 | 预期文件 | 落盘? |
|---|---|---|---|
| R1 | SBPN 拆解深度 | `R1_SBPN_teardown.md` | ✅ 已落 |
| R2 | EdgeIM 拆解＋复现回流 | `R2_EDGEIM_teardown.md` | ✅ 已落 |
| R3 | MHP 拆解＋规则回流 | `R3_MHP_teardown.md` | ✅ 已落 |
| R4 | 三篇复现升级路径评估 | `R4_repro_upgrade.md` | ✅ 已落 |
| R5 | bridge 命题盲区＋独立排序 | `R5_bridge_blindspot.md` | ✅ 已落 |
| R6 | 综合 V2＋教学包实战性 | `R6_synthesis_teaching.md` | ✅ 已落 |
| R7 | 旧四卡受新证据冲击 | `R7_legacy_cards_recheck.md` | ✅ 已落 |

### L 波 · 旧四篇框架补齐（4 路，新增卡落主目录）
性质＝给旧四篇（08-13 的 8 层卡）补用户完整框架（6 点第一性原理＋张力结构＋知识图谱＋批判四审视）；与旧卡互补（同一事实引用旧卡不复写），novelty 切割独立核原文。

| Agent | 对象 | 预期文件 | 落盘? |
|---|---|---|---|
| L1 | SBTPN（对照 06 切割 novelty 首发权） | `01b_SBTPN_sixpoint_kg_critique.md` | ✅ 已落（08-22 补齐波） |
| L2 | PNULock（含重模型剩余价值） | `02b_PNULOCK_sixpoint_kg_critique.md` | ✅ 已落（08-22 补齐波） |
| L3 | UAF（双图分工 insight 判定） | `03b_UAF_sixpoint_kg_critique.md` | ✅ 已落 |
| L4 | SegLock（组内路线之争张力） | `04b_SEGLOCK_sixpoint_kg_critique.md` | ✅ 已落（08-22 补齐波） |

### F 波 · 鲁×孙融合探路（4 路，报告落 `fusion_sun_20260815/`）
性质＝论证鲁组方法×孙侧 LLM-agent 安全的融合可行性；**硬门槛＝真实在研先例＋OpenReview 拒稿取证（forum id 必须真实可核，拒因真实摘录不得杜撰）**；**全程防御性框架，禁攻击生成/传播放大**。

| Agent | 融合轴 | 预期文件 | 落盘? |
|---|---|---|---|
| FA | 概率模型检验（SBPN/SBTPN×ProbGuard DTMC/PRISM） | `FA_probabilistic_modelchecking.md` | ✅ 已落 |
| FB | 一致性监测（EdgeIM/conformance×AgentSpec/ReGA） | `FB_conformance_monitoring.md` | ✅ 已落 |
| FC | 并发验证（PNULock/MHP/UAF×MAS 并发安全） | `FC_concurrency_mas.md` | ✅ 已落 |
| FD | OpenReview 拒稿取证专员（跨轴避雷地图） | `FD_openreview_forensics.md` | ✅ 已落 |

> 全 Agent ID 见 `_launch/LAUNCH_PACKAGE_20260815.md` 的 R/L/F 波表（新会话大概率无法 resume 旧 ID，缺的直接按 §3 重发新 Agent）。

## 3. 缺失 Agent 重发规格（新窗口用；输入路径均相对本目录）

公共约束：简体中文；公式纯文本禁 LaTeX；数字带 [PDF p.X] 页锚；三道安全门（不编造/不过度承诺/全覆盖）；只写自己那一个输出文件；旧卡 01-05 与已完成产物只读；不 commit。原文在 `_launch/pdftxt/`，原 PDF 在 `../`。

- **R 波**：对被审对象做"质量上限审"（不是查对错，G 波已做）。R1/R3 审 `06/08`＋`06b/08b` 拆解深度与批判盲点；R4 审 `repro/` 三包的复现升级路径（不实跑）；R5 审 `bridge/` 三卡命题盲区（重点：跨篇组合命题如 D1+D2 闭环有没有人认领＋三 bridge 独立排序）；R6 审 `09`＋`teaching_paywall3/`（谱系证据强度＋18 题与真实使用对齐度）；R7 审旧四卡 01-05 在新证据（06/07/08）下的受冲击点。输出格式见 §2 R 波说明。
- **L 波**：给对应旧论文按完整框架产补齐卡，与旧卡互补。L1=SBTPN（切割与 SBPN 06 的 novelty 首发权，引 06 卡 §9）；L2=PNULock（加"重模型剩余价值"推演）；L3=UAF（判定"双图分工"是否真 insight）；L4=SegLock（组内路线之争张力＋"够用就好"裁剪哲学）。结构：一 6 点第一性原理／二 张力结构／三 知识图谱／四 批判四审视。
- **F 波**：见 §2 F 波性质。名称雷区：Jun Sun（SMU，ProbGuard/AgentSpec）≠孙猛（PKU，ReGA）≠ Meng Sun（PKU），必标明。孙侧资产在 `../../sun/phase1/papers/`。FD 是重点，专攻 OpenReview 拒稿取证，可参考 `../../map/W4_rejection_intel/` 既有拒稿元分析。

## 4. 全落齐后要交付用户的东西（本会话已承诺）

1. **改进空间总表**：汇总 R1-R7，按 A/B/C 优先级排出"值得马上做的改进"清单（带成本），让用户拍板做哪些。
2. **七篇框架补齐确认**：L1-L4 落盘后，七篇拆解标准统一（每篇主拆卡＋框架分析卡），更新 README §四与 `09` 的文件清单。
3. **鲁×孙融合可行性＋OpenReview 避雷地图**：合成 FA-FD，给出三融合轴可行性档位排序＋OpenReview 拒因模式排行＋对 T2/T4/T5 的避雷建议。合成可另开一个 Agent 或主窗自己做。
4. **学习梯队**：用户已拍板「要」；`STUDY_ROADMAP.md` 于 23:22 落盘（S＝SBPN/PNULock/UAF）。

## 5. 用户侧待办（不阻塞，见 `99_USER_TODO_20260815.md`）

④教学开考（新旧两套教学包）＋ra30 EX-04 精读＋T4/T2/T3 提案差量拍板＋OE1 素材（8-25 死线）。这些是只有用户能做的，别代做。

## 6. Git 与写域终态

顶层仓 `M FOCUS.md`/`M WINDOW_PLAYBOOK.md`/`M CROSSWINDOW.md`；MAS 子库大量他窗历史改动＋本战役新增文件，**全程未 commit**，新窗口不得替用户决定提交/回滚/清理。本战役写域仅限 `papers_lu/teardown-joint-20260813/**`＋`../MANIFEST.md`＋顶层三档的对应行。

## 7. 恢复口令

> 接手付费墙三篇战役后续波：先读 `HANDOFF-20260815-newwindow.md`＋`_launch/LAUNCH_PACKAGE_20260815.md`，`ls` 盘点 `_review_20260815/`＋`fusion_sun_20260815/`＋`0?b_*sixpoint*.md` 落盘情况，缺的按本档 §3 重发，全齐后做 §4 三张合成表交用户。旧卡与已完成产物只读，不 commit。
