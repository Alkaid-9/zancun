# A0 当前游标

状态：`CURRENT-EVIDENCE-RECONCILED / NO-PASS-DECISION`

## R1

- 正式题面：[EX-01 README](../../../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-01/README.md)，五问在第 219–236 行。
- 指定提交：`/mnt/d/MyResearch/MAS_Safety_Project/research/tracebridge_full_spectrum_20260830/00_control/_scratch/seg0/G0_user_paper_note.md`
- 现状：未在 zancun 和 MAS 权威范围找到指定稿；EX-01 作答中已有 DFG、任务 4 和读前预测 WIP，不重做。
- 暴露：第 3 问已见 Sol 提示；它只能做 PDF 来源核实，不算独立发现。
- D1 动作：先找仓外本人稿；若没有，只建五问空框，30 分钟到点留断点。

## EX-05

| 对象 | 当前证据 | 当前裁定 |
|---|---|---|
| [`test_invariants.py`](../../../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-05/test_invariants.py) | `:8-20` 有一版 `full_features`；`:40-76` 有 10 seeds 正/逆序主体 | 已做但未验收 |
| 预测/观察 | `:30-32` 对 p3 同时写了“高”和“低” | `CONFLICT`，须由本人分开预测与运行后观察 |
| 函数重定义 | `test_invariants.py:79-92` 又定义一次 `full_features`，但字符串语义不同且当前未调用 | `CONFLICT`，不自动删除 |
| [`own.py`](../../../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-05/own.py) | `:93-99` 有固定 seed 随机顺序和断言 | 探索稿，不是题面指定正式交件 |
| [`takeover.md`](../../../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-05/takeover.md) | zancun 文件为 0 字节 | `MISSING`，不代写 |
| EX-05 PASS | 未按冻结 rubric 验收 | `UNKNOWN / NOT-DECIDED` |

详细差分见 [CURRENT_STATE.tsv](CURRENT_STATE.tsv)。

## EX-06

- [公开门禁页](../../../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-06/README-EX06.md)：G0 note 已落盘，且 EX-02、EX-03、EX-05 PASS。
- 当前：G0 未找到；EX-03 的 2026-09-12 checkpoint 是 `USER-REPORTED / NOT PASS`；EX-05 PASS 未裁定。
- 裁定：`LOCKED`。不打开受控 C06，不生成 T0 答案。
