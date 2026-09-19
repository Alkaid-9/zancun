Author: Fable 5 main window (TASK-20260904-001)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# MANIFEST 附录 · 桥线 T1 三篇 PDF 落盘登记（2026-09-04）

> 主 `MANIFEST.md` 是 08-12 文献获取 Agent 的产物（6+1 篇），本附录只登记 09-03 新落盘的三件，**不改主表**。三件均出现在桥线执行计划 v1.0 :155-156 与 `_scratch/seg0/_withdrawn/T1_paper_verification.md` P2–P4；T1 表当时的结论是"官方记录 open access，本地未找到 PDF"。09-03 17:50 三件同时落盘，**由谁、从哪里下载没有记录** → 来源栏一律 `[需核实]`，等用户补一句。

| # | 题录 | 本地文件 | 页数 | SHA-256 | 原件内印的 DOI | 来源 |
|---|---|---|---|---|---|---|
| P2 | **sigRank**: Su, Liu, Zhang, Zeng, Mo, Cheng. "Toward Efficient Support for Business Process Event Log Sampling". *IEEE Trans. Services Computing* 19(2):1606–1618, Mar/Apr 2026 | `sigRank-2026-TSC.pdf`（4.4 MB，2026-09-03 17:50） | 13（印刷 1606–1618） | `e20cac7b2b1c562b12342d07f33b5621e50dcdb15f2dc7ea42fb6da632c09800` | `10.1109/TSC.2026.3665370`（TXT:71；PDF Subject 字段同） | `[需核实]`；T1 表记 RUN/UNL 机构库 OA 记录 |
| P3 | **CrossEdgeIM**: Su, Liu, Zeng, Zhang, Cheng. "CrossEdgeIM: An Edge-Based Approach for Interactive Robotic Behavior Model Discovery". *IEEE Internet of Things Magazine*, 2026（proof 版，栏目 "Edge AI for Internet of Robotic Things"） | `CrossEdgeIM-2026-IoTMag.pdf`（1.2 MB，2026-09-03 17:50） | 6 | `ac7ec167a89cd726381ae451b96280e44d49951f55481049209414654f311803` | `10.1109/MIOT.2025.3625047`（TXT:68，抽取截断为 `362504`，末位按 T1 表补齐 `[需验证]`） | `[需核实]`；PDF 标题元数据为 `MIOTliu-3625047_proof.pdf` → 作者校样，非最终排印版 `[推断]`；卷期页码未定 |
| P4 | **Sommers**: Sommers, Sidorova, van Dongen. "A ground truth approach for assessing process mining techniques". *Process Science* 2:1, 2025（Springer, Open Access） | `Sommers-2025-ProcessScience.pdf`（3.9 MB，2026-09-03 17:50） | 30 | `59cf748494a4f5f9393c0e9082a7cbb368e24148a5de6708ba9aa4e305db6603` | `10.1007/s44311-025-00006-8`（TXT:2；PDF Subject 字段同） | `[需核实]`；Springer OA（CC 许可具体条款见原件末页，未逐字核） |

## 判型证据

三件 `pdfinfo` 均正常解析（Creator/Producer 为 LaTeX+Distiller / Arbortext+LiveCycle / InDesign+Adobe PDF Library），`pdftotext -layout` 分别得 711 / 387 / 1434 行，分页符 13 / 6 / 30 个，与页数一致 → 均为真 PDF，非 HTML 壳页。

## 与主表的关系

- 主表第 5 行 EdgeIM（`e9dd5280…`）是三件的"母论文"（P1，必要）；三件在 T1 表里分别是辅助 / 背景 / 必要辅助，**不改变主表 6+1 的口径**。
- 三件的拆解产物在同目录 `teardown-bridge-20260904/`，`_launch/pdftxt/` 下的 TXT 为 `pdftotext -layout` 抽取，只作定位，判定以 PDF 原件为准。

## 待用户

- 补三件的下载来源（一句话即可：校园网 IEEE Xplore / 机构库 / Springer 官网 / 作者提供），补完把 `[需核实]` 改掉。
- 是否把本附录并入主 `MANIFEST.md`（主表是 08-12 历史产物，并入等于改历史档，需口令）。
