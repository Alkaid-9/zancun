# Source Register

## 证据标签

| 标签 | 含义 |
|---|---|
| `PRIMARY` | 本地原始 PDF 直接陈述、公式、算法、表或图 |
| `AUTHOR-FRAMING` | 论文作者对前作、机制或结果的解释；只证明作者这样写 |
| `IMPLEMENTATION-EVIDENCE` | 固定版本源码或运行行为；不自动等于论文语义 |
| `TEARDOWN-NAV` | 拆解件导航、复算或批评；必须回原始 PDF |
| `USER-INFERENCE` | 学习者依据已列证据作出的可反驳推理 |
| `COURSE-FIXTURE` | 课程冻结的 synthetic 题面数据或公理；只用于训练/验收，不是论文证据 |
| `SOURCE-OPEN` | 当前来源不足，不能补成确定答案 |

来源标签与 claim verdict 是两套字段，不得混用。claim verdict 固定为：
`DIRECT`（直接观察）、`DERIVED`（可复算推导）、`PROXY`（间接支持）、
`CONFLICT`（内部不一致）或 `UNSUPPORTED`（现有证据不支持）。

## 冻结输入

| paper | 路径 | SHA-256 | 页数/页码 | teardown 导航 | 关键边界 |
|---|---|---|---|---|---|
| EdgeIM | `research/papers_lu/EdgeIM-2025-ICWS.pdf` | `e9dd5280e87c77b039341868abc050ac49dd38f2813d764d79d910c26795e299` | 7 physical；印刷 404-410 | `teardown-joint-20260813/07_EDGEIM.md`、`07b_EDGEIM_kg_critique.md` | bridge teardown 目录不含 EdgeIM 拆解 |
| sigRank | `research/papers_lu/sigRank-2026-TSC.pdf` | `e20cac7b2b1c562b12342d07f33b5621e50dcdb15f2dc7ea42fb6da632c09800` | 13 physical；印刷 1606 起 | `teardown-bridge-20260904/10_SIGRANK*.md`、`10b_SIGRANK_kg_critique.md` | prose Step 1-4，不是正式 Algorithm |
| Ground Truth | `research/papers_lu/Sommers-2025-ProcessScience.pdf` | `59cf748494a4f5f9393c0e9082a7cbb368e24148a5de6708ba9aa4e305db6603` | 30 physical | `12_SOMMERS*.md`、`12b_SOMMERS_kg_critique.md` | Sommers 没有做 EdgeIM 实验 |
| CrossEdgeIM | `research/papers_lu/CrossEdgeIM-2026-IoTMag.pdf` | `ac7ec167a89cd726381ae451b96280e44d49951f55481049209414654f311803` | 6 physical；印刷 55-60 | `11_CROSSEDGEIM*.md`、`11b_CROSSEDGEIM_kg_critique.md` | 本地文件 proof/final 身份未闭合 |

补充实现环境：本机 PM4Py `2.7.23.6`。它只能支撑明确版本下的实现观察；EdgeIM PDF 没有公开其
PM4Py 版本、调用参数或代码，因此不能把本机输出写成 EdgeIM 原实现行为。

## 已知来源纠错

1. EdgeIM v3 合同的 source-input 段只写了 `teardown-bridge-20260904/`；EdgeIM 自身拆解实际在
   `teardown-joint-20260813/`。本目录按真实路径取证，合同原件不在施工阶段回写。
2. sigRank PDF Table III 的 ETMC4200/LogRank 是 `186804.32`，旧拆解中的 `84306.16` 不采用。
3. sigRank PDF Table II 的 trainingLog1/hybrid/5% 是 `0.915`，不是 `0.8875`。
4. sigRank PDF Table II 的 trainingLog7/IMi/5% 是 `0.5662`，不是 `0.3662`。
5. CrossEdgeIM 作者为 Xuan Su、Cong Liu、Qingtian Zeng、Jinglin Zhang、Long Cheng；鲁法明不在作者中。

## 引用纪律

- 每个答案写 PDF physical page + section/table/figure；印刷页可作为补充。
- 表格数字发生冲突时直接看 PDF 图像，不以拆解转录覆盖 PDF。
- related work 对前作的评价默认是 `AUTHOR-FRAMING`；未打开前作不能下独立 novelty verdict。
- “未报告”不等于“为假”；“架构上可能减少”不等于“已测量减少”。
- 每条 claim 同时填一个 source label 和一个 claim verdict；例如论文表格数字可为
  `PRIMARY + DIRECT`，作者由该数字推出的因果解释可能是 `AUTHOR-FRAMING + PROXY`。
