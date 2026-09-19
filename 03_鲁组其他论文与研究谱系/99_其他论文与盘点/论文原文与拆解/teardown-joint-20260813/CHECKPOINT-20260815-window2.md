---
date: 2026-08-15
time: 23:40 UTC+8（上次全量存档 23:16；本档为进度刷新）
type: window-checkpoint（窗口2工作存档＝总结+日志+架构+计划+手册）
window: 窗口2（付费墙三篇战役后续波收口窗，23:03 接手）
line: P批1 · 鲁组论文拆解线（papers_lu）· 付费墙三篇战役（SBPN/EdgeIM/MHP）· 后续三波增量（R 改进重审 / L 框架补齐 / F 鲁×孙融合）＋ROADMAP＋SYN
upstream: HANDOFF-20260815-newwindow.md（窗口1→本窗交接档）；主战役收口档 CHECKPOINT-20260815.md
no_commit: true
status: 2026-08-22 01:2x 补齐波收口刷新——L 4/4、SYN-A/SYN-C 已落、T-B 完成；G 级独立审计进行中（报告将落 `_audit_finishing_20260821/`）。下行为 23:42 历史快照，不回填
---

# 窗口2存档 · 付费墙三篇后续波收口窗（23:03 起）

> **23:42 完整档案包**：`_archive_window2_20260815/README.md`（总结/日志/进度/所属线/架构/文件/计划/使用/维护/交接，分档可溯源）。本单档保留作快照索引，细节以档案包为准。

## 0. 本档是什么、给谁读

- **本档**＝窗口2 的完整工作存档：总结、日志、已完成/未完成、架构分工、后续计划、使用与维护手册。断线后凭本档＋磁盘文件可完整恢复。
- **读者路径**：接手人先读本档 §7（下一步）＋§4（在途表）；要背景再读 §1；要操作细节读 §8/§9。
- **本档不取代**：`HANDOFF-20260815-newwindow.md`（窗口1 交接档，含 §3 重发规格与 §4 交付定义——仍然权威）；`CHECKPOINT-20260815.md`（主战役怎么打完的）。

## 1. 所属线与上游脉络（追根溯源）

1. **主战役**（窗口1，18:2x–22:3x）：付费墙三篇 SBPN/EdgeIM/MHP 拆解＋批判＋复现三 PASS＋bridge 三卡＋综合 V2＋教学包＋四审计＋修复收口。已 100% 关窗，恢复档 `CHECKPOINT-20260815.md`，架构档 `_launch/LAUNCH_PACKAGE_20260815.md`。
2. **三波增量**（窗口1，22:4x–22:5x 用户令追加）：R 改进重审 7 路、L 旧四篇框架补齐 4 路、F 鲁×孙融合 4 路，共 15 路。
3. **冻结与交接**（窗口1，22:57）：用户令冻结；窗口1 写 `HANDOFF-20260815-newwindow.md` 后被强行中断（Ctrl+C），其未落盘子 Agent 全部阵亡。
4. **本窗＝窗口2**（23:03 起）：凭恢复口令接手，盘点→重发→（现在）存档。

## 2. 窗口2 工作日志（可溯源时间线）

| 时刻 | 动作 | 证据/落点 |
|---|---|---|
| 23:03 | 接手：读 HANDOFF 全文＋盘点三写域 | 盘点结果：R 6/7（R1 晚落已到，缺 R3）、L 0/4、F 0/4 |
| 23:03 | 读 `_launch/LAUNCH_PACKAGE_20260815.md` 取原始规格与写域矩阵 | 判定：旧会话强断→9 路阵亡，按 HANDOFF §3 重发 |
| 23:04 | **重发 9 路后台 Agent**（R3、L1-L4、FA-FD），提示词按 HANDOFF §3 规格自包含 | 新 ID 见 LAUNCH_PACKAGE「重发记录」节 |
| 23:05 | 更新 HANDOFF §2：R1 标 ✅；LAUNCH_PACKAGE 增「重发记录」表（9 ID） | 两文件对应行 |
| 23:09 | 用户拍板「要」STUDY_ROADMAP → **发第 10 路 ROADMAP Agent** | ID 08e61a6d…，登记进重发记录表 |
| 23:15 | 用户令「快存档」 | 本档＋CROSSWINDOW 登记行 |
| 23:16 | 存档前快照（见 §4 表） | ls 实测 |
| 23:18 | FA/FB/FC 三路落盘 | `fusion_sun_20260815/{FA,FB,FC}_*.md` |
| 23:22 | ROADMAP 落盘（用户拍板「要」） | `STUDY_ROADMAP.md`（S＝SBPN/PNULock/UAF） |
| 23:31 | R3 落盘 → R 波 7/7 齐 → 发 SYN-A | `_review_20260815/R3_MHP_teardown.md`；SYN-A=`d74b3888-d081-4dc5-b40b-b6e0a4367c14` |
| 23:32 | L3 落盘 | `03b_UAF_sixpoint_kg_critique.md` |
| 23:34 | FD 落盘 → F 波 4/4 齐 → 发 SYN-C | `fusion_sun_20260815/FD_openreview_forensics.md`；SYN-C=`ae79ad40-2521-4b93-8ec5-b54c0f3111a8` |
| 23:40 | 用户令「存档进度」 | 本档刷新＋HANDOFF §2 勾选＋CROSSWINDOW 窗口2 行 |
| 23:42 | 用户令完整窗口存档（总结/日志/架构/计划/手册分档） | `_archive_window2_20260815/**` 11 件 |

## 3. 已完成（本窗）

- 接手盘点完成，落盘真相与 HANDOFF 冻结快照差异已核（R1 晚落＝加分项，已采纳标 ✅）。
- 缺失 9 路全部按规格重发＋ROADMAP 1 路新发；R 波齐后发 SYN-A、F 波齐后发 SYN-C。ID 全部登记（`_launch/LAUNCH_PACKAGE_20260815.md` 重发记录节）。
- 已回收：R 7/7、F 4/4、L3、ROADMAP。
- HANDOFF 快照行、LAUNCH_PACKAGE 登记、本存档、CROSSWINDOW 登记。
- 约束遵守：零 commit；旧卡 01-05、已完成产物零改动。

## 4. 落盘与在途（23:40 快照，ls 实测）

**计数**：R 7/7 · F 4/4 · L 1/4 · ROADMAP 1/1 · 合成表 0/3（T-A/T-C 在途，T-B 等 L 齐）。

**原 10 路重发＋后续 2 路合成**：

| Agent | 产出（相对本目录） | 23:16 落盘? | 新 ID（resume 用） |
|---|---|---|---|
| R3 | `_review_20260815/R3_MHP_teardown.md` | ✅ 23:31 落（R 波 7/7 齐） | a20b8010-43da-4f3c-85c4-c05882900702 |
| L1 | `01b_SBTPN_sixpoint_kg_critique.md` | ⬜ | eabdf685-bb34-4bbf-8a3b-04f568a372cf |
| L2 | `02b_PNULOCK_sixpoint_kg_critique.md` | ⬜ | f5e70086-3f8c-4647-b7da-0856e17cf958 |
| L3 | `03b_UAF_sixpoint_kg_critique.md` | ✅ 23:32 落（双图＝真分工假对等） | b55f67b1-afb9-4d20-bf35-03afd83cf9d3 |
| L4 | `04b_SEGLOCK_sixpoint_kg_critique.md` | ⬜ | 952e3d7c-b7f4-4b52-894a-dff6d8a8812a |
| FA | `fusion_sun_20260815/FA_probabilistic_modelchecking.md` | ✅ 23:18 落（可开题·附条件） | c9288cfb-f8ce-498a-b812-5fa016c20f2b |
| FB | `fusion_sun_20260815/FB_conformance_monitoring.md` | ✅ 23:18 落（可开题·T2 运行时出口） | c48bad79-7b08-4c97-a889-607510563877 |
| FC | `fusion_sun_20260815/FC_concurrency_mas.md` | ✅ 23:18 落（分轴三档） | 7a2f4ec5-6fee-4978-9cf8-d583da83d4a8 |
| FD | `fusion_sun_20260815/FD_openreview_forensics.md` | ✅ 23:34 落（21 案例/29 核验链接/9 类拒因；F 波 4/4 齐） | 4300725d-977d-483f-9edd-58da575f96e6 |
| ROADMAP | `STUDY_ROADMAP.md` | ✅ 23:22 落（S＝SBPN/PNULock/UAF；总预算 53-68h） | 08e61a6d-3b41-481e-b65b-0921b7d29504 |
| SYN-A | `_review_20260815/00_SUMMARY.md` | ⬜ 23:31 发 | d74b3888-d081-4dc5-b40b-b6e0a4367c14 |
| SYN-C | `fusion_sun_20260815/00_SYNTHESIS.md` | ⬜ 23:34 发 | ae79ad40-2521-4b93-8ec5-b54c0f3111a8 |

**本窗欠的交付**：T-A（等 SYN-A）· T-B（等 L1/L2/L4 后核结构＋改 README §四/09 清单）· T-C（等 SYN-C）。规格见 §7。

**用户已拍板**：STUDY_ROADMAP＝要（已落）。**未拍板**：改进总表做哪些、融合轴是否开题、W4 两处接收记录是否改（VIRF＝ICLR 2026 Poster；GuardAgent＝ICML 2025；本窗只登记不代改）、`99_USER_TODO` 四项。

## 5. 设计与架构方案（本窗沿用＋新增）

**总架构**（沿用窗口1，见 LAUNCH_PACKAGE）：主窗＝协调/盘点/重发/合成/登记，不产内容；内容全部由单写域子 Agent 产出。
**核心设计原则**：
1. **写域隔离**：每 Agent 只写唯一一个文件/目录，矩阵见 §4 表，两两不相交 → 任何时刻中断都不产生半成品冲突。
2. **只认文件不认通知**：跨会话收不到旧窗 Agent 通知，落盘文件是唯一真相源 → 盘点用 ls 而非记忆。
3. **只增不改**：在途波只新增文件；旧卡 01-05、06-09、repro/bridge/teaching/audit 全部只读终态。
4. **no-commit**：全程不 git commit，提交权在用户。
5. **自包含提示词**：重发的 Agent 提示词内嵌全部路径/约束/特命，不依赖会话记忆 → 本窗再断，凭 §4 表＋HANDOFF §3 可第三次重发。
6. **安全门**：不编造（F 波链接/forum id 必须真实）、不过度承诺、防御性框架（F 波禁攻击内容）、名称雷区（Jun Sun≠孙猛≠Meng Sun）。

**分工方案**：R 波＝质量上限审（对已 PASS 产物挑改进）；L 波＝旧四篇补 6 点框架＋张力＋图谱＋四审视卡（0Xb 命名）；F 波＝鲁×孙融合三轴论证＋OpenReview 拒稿取证；ROADMAP＝七篇 S/A/B 学习梯队。

## 6. 文件索引（本战役全景，按用途）

- **入口**：`HANDOFF-20260815-newwindow.md`（交接权威）→ 本档（窗口2 状态）→ `_launch/LAUNCH_PACKAGE_20260815.md`（架构+全 ID）→ `CHECKPOINT-20260815.md`(主战役)。
- **拆解卡**：旧四 `01-04_*.md`＋补齐卡 `03b` 已落、`01b/02b/04b` 在途；新三 `06/07/08`＋`06b/07b/08b`；综合 `05`(旧)、`09_FAMILY_SYNTHESIS_V2.md`(现行)。学习路线 `STUDY_ROADMAP.md` 已落。
- **复现**：`repro/{sbpn,edgeim,mhp}/`（三 PASS）；**bridge**：`bridge/`三卡；**教学**：`teaching/`(旧四) `teaching_paywall3/`(新三)；**审计**：`_audit_paywall3/G1-G4`。
- **在途产出区**：`_review_20260815/`（R 波）、`fusion_sun_20260815/`（F 波）、主目录 `0Xb_*`＋`STUDY_ROADMAP.md`。
- **原文**：`_launch/pdftxt/*.txt`（8 件）＋`../*.pdf`。
- **登记面**：`../MANIFEST.md`、仓顶 `FOCUS.md`/`WINDOW_PLAYBOOK.md`/`CROSSWINDOW.md`。
- **用户侧待办**：`99_USER_TODO_20260815.md`（教学开考/EX-04/提案差量/OE1，8-25 死线——AI 不代做）。

## 7. 接下来的 Plan（本窗或接手窗执行）

1. **等落盘**（23:40 仍缺）：L1/L2/L4、SYN-A、SYN-C。晚落直接采纳；某路超 ~40 分钟无文件 → 按 HANDOFF §3 重发（L）或按本档 §4 原提示词重发（SYN）。L1/L2/L4 已跑约 36 分钟，接近警戒。
2. **三张合成表**（HANDOFF §4）：
   - **T-A** `_review_20260815/00_SUMMARY.md`：R 齐，SYN-A 在途。
   - **T-B** L 齐后核四大节＋更新 README §四与 `09` 清单（加 0Xb 四行）。尚未发 Agent。
   - **T-C** `fusion_sun_20260815/00_SYNTHESIS.md`：F 齐，SYN-C 在途。
3. **交付后登记**：HANDOFF §2 全表打 ✅、CROSSWINDOW 加收口行、本档 status。
4. **用户拍板项**（AI 不推进）：改进总表做哪些；融合轴是否开题；W4 两处接收记录是否改；`99_USER_TODO` 四项。

## 8. 使用手册（怎么用这套东西）

- **盘点命令**（在本目录）：`ls _review_20260815/ fusion_sun_20260815/ ; ls 0?b_*sixpoint*.md STUDY_ROADMAP.md`，对照 §4 表即知进度。
- **新窗口接手口令**：接手付费墙三篇后续波：读 `CHECKPOINT-20260815-window2.md`（窗口2 存档）§4/§7，ls 盘点在途 10 路落盘，缺的按 `HANDOFF-20260815-newwindow.md` §3 重发，全齐后按 §7.2 做三张合成表。旧产物只读，不 commit。
- **读产物顺序**（用户）：R 波先读 `_review_20260815/` 各报告末尾 top3 → 三张合成表（做完后）→ 按合成表拍板。学习路径读 `STUDY_ROADMAP.md`（落盘后）。
- **resume**：各 Agent ID 见 §4 表（同会话内有效）；跨会话失效则重发，提示词规格＝HANDOFF §3。

## 9. 维护手册（改动纪律）

- **可写白名单**：`_review_20260815/**`、`fusion_sun_20260815/**`、主目录新增 `0Xb_*`/`STUDY_ROADMAP.md`/合成表两件；登记行可改 HANDOFF §2 勾选、LAUNCH_PACKAGE 登记节、README §四清单、09 文件清单、CROSSWINDOW/MANIFEST 增行、本档 status。**其余一切只读**（尤其 01-05 旧卡、06-09、repro/bridge/teaching/audit、99_USER_TODO）。
- **冲突规则**：撞写域以先落盘者为准，后到并入增补节（沿用 LAUNCH_PACKAGE 停止规则）。
- **快照纪律**：任何人改 HANDOFF/本档的落盘快照必须附时间戳，不回填历史行。
- **git**：仓顶 `M FOCUS.md`/`M WINDOW_PLAYBOOK.md`（他窗历史改动）＋MAS 子库大量未 commit 改动——**不得替用户 commit/回滚/清理**。
- **安全红线**：F 波产物若发现杜撰链接/forum id（G4 式抽查核链），该条目整条作废并在合成表标注；不修原报告。
