# Four-Paper Shared Artifacts

本文件只定义接口。下列表在课程建设阶段保持空白；只有学习者完成相应 P3/桥接任务后才能回写，并必须链接本人证据。

## Mechanism Map

| paper/module | object | input | state before | update | state after/output | consumer | preserved | lost/open | source | learner evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ |

## Sampling / Selection Matrix

| method | selection unit | objective/surrogate | budget policy | input/output interface | state/cost | downstream consumer | preserved/lost | matched interface/cost | claim ceiling | learner evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ |

禁止直接并表 sigRank、EdgeIM、CrossEdgeIM 的 F-measure。比较前先固定 evaluation referent、miner、日志、预算、参数和指标实现。

## World & Evidence Contract

固定链：

`M0 --BI--> M^S --RI--> M^L --simulate(theta,seed)--> L' --project(q)--> D_obs --sample(S)--> D' --consume(g)--> result`

来源边界：`M0 -> M^S -> M^L -> L'` 是 Sommers 论文框架；`project(q) -> D_obs -> sample(S) -> D'`
是本课程为 EdgeIM 迁移新增的实验后缀，不得写成 Sommers 原文步骤。evaluator 可保留独立 oracle sidecar，
sampler 只能消费去除 oracle 字段后的 `D_obs`。

| field | frozen value | source/owner | OPEN condition |
|---|---|---|---|
| world/source/version | ______ | ______ | ______ |
| `M0/M^S/M^L` identifiers | ______ | ______ | ______ |
| BI/RI operators and order | ______ | ______ | ______ |
| simulation parameters/seed/scale | ______ | ______ | ______ |
| oracle provenance | ______ | ______ | ______ |
| learner/sampler-visible projection | ______ | ______ | ______ |
| sampler version/order/hash/budget | ______ | ______ | ______ |
| downstream consumer/version/params | ______ | ______ | ______ |
| evaluation target and metric | ______ | ______ | ______ |
| prediction/falsifier | ______ | learner | ______ |
| raw output and claim ceiling | ______ | learner/evaluator | ______ |

采样是生成后的第三类 intervention，不能改名为 behavioral deviation 或 recording error；sampler 不得看到 oracle tags。

## Genealogy & Residual Card

| predecessor | bottleneck | redesign | new residual | source label/coordinate | authorship boundary | migration boundary | downstream consumer | claim ceiling | learner evidence |
|---|---|---|---|---|---|---|---|---|---|
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | Transfer Card / B-DEFENSE | ______ | ______ |

CrossEdgeIM 行必须明确：“CrossEdgeIM 不是鲁法明署名论文”。作者重叠不等于导师署名、实验室组织关系或独立 novelty 证据。

## 回写门

1. 回写前有 `pretest -> redo -> holdout` 证据。
2. 每行至少一个 primary-source coordinate。
3. 冲突和 UNKNOWN 不得删掉。
4. 回写只改变共享理解，不自动改变用户 PASS/OWNED。
