# 段 0 第一轮可复用件 · 处置台账

**Date**: 2026-09-03 晚
**Scope**: `_scratch/seg0/` 未撤回的六份 + `pilot.py` 组件 + 计划/作业书条款。每件写：现状核实 → 已做 → 剩下谁做。
**层级**: evidence 层。不改任何原件（原件保持产出时原样，处置意见只写在这里）。

| # | 件 | 现状核实（2026-09-03 晚） | 已做 | 剩下 · 责任人 |
|---|---|---|---|---|
| 1 | `A3_pm4py_api_inventory.md` | 版本疑点属实：文档镜像写 2.2.30/2.2.32；**本机已装 `pm4py 2.7.23.6`，PyPI 最新 2.7.23.8**。API 名（`discover_petri_net_inductive` / `noise_threshold` / replay_fitness / precision）在 2.7 系仍存在，但 A3 :57 自己说明未核本机 | 版本核清（本行） | 是否 pin 2.7.23.6 · **用户**（一句话即可）；训练包 EX-02 用本机版本跑对照 · 主窗 |
| 2 | `A4_calendar_budget.md` | 仍缺用户课表，其余可用 | — | 补课表 · **用户**（T4' 之前任何时候） |
| 3 | `B3_perturbation_recommendation.md` | backup（相邻交换）+ 排除清单可用；primary（现有字母表插非法位置）在 Algorithm 1 下首次必留，作废 | v1.1 §9 已写替换方向 | 新 primary 待 T0；候选=不制造新 DFG 边的扰动（时间戳粗化等）· T0 后 |
| 4 | `T4_reverse_schedule.md` | 容量模型 96h+20%=115h、四门 T4-A~D 可用。:23「14 calendar days」与窗口 09-04→09-20（17 天）矛盾属实；:62 INVALID-BUDGET 行受 T2 污染。**进组改月底后 09-20 冻结日不变**，本表不因日期改动重排 | 矛盾登记（本行） | 分项工时随 T0 重排成 T4' · T0 后 |
| 5 | `A2_edgeim_paper_note_draft.md` | :6「本地无 PDF」为假（`papers_lu/EdgeIM-2025-ICWS.pdf` 在）。§5 九条未验证 + §9「不足以授权代码」是当天唯一说对了的 flag | 不改原件；本行登记 :6 为假 | 只作定位底稿。理解层由用户在 EX-01 自写 `G0_user_paper_note.md` |
| 6 | `pilot.py` 生成器/oracle 层（`ModelSpec` `_derive_seed` `classify_trace` `_insertion_candidates` `build_universe` `_features` 指标与校验） | 代码未变；STATUS.md 已列行号 | — | **不动代码**。归属判定在训练包 EX-05：用户先裸写 Algorithm 1，再按 OS §11 逐个接管；接管不了的按遗物处理 |
| 7 | 计划 v1.0 §1.3/1.4/6.2/6.6/7/9/10/11 | 继续有效 | v1.1 §9 已列 | 作废条款（§4.1–4.3/6.1/6.4/6.5）须随 C-069 正式记录 · **用户批** |
| 8 | 作业书 v1.0 骨架（DAG/写域/caps/不做清单） | 有效，v1.1 继承 | — | — |
| 9 | 三份 results 报告的判断（六因子清单 / 冷审计 findings / scoped exploratory 定级） | 判断成立，数字不可引 | STATUS.md 已写 | 取证材料，不改 |

## 不在复用范围但常被误以为可用

- `edgeim_sampling_audit/results/*.json` 全部数字
- `sample_coverage` / `_valid_budget` / `run_pilot`
- `_withdrawn/` 内任何结论（T1 的检索结论、T2 的五单位、T3 的 CORE 表）

## 当晚已清掉的一笔

`learning/` 下曾有两份自称 `OS v0.1 FROZEN` 的文件；晚间核查只剩 08:37 那份 17,302 B，17:37 的压缩版已不在盘上（非本窗所删）。权威源歧义消失。
