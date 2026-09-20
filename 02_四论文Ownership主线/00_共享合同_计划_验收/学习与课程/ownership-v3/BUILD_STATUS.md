# Ownership v3 Build Status

**历史源仓资产状态**：`BUILT / QA-PASS`（以下 QA 记录所述时点）
**当前 zancun 快照状态**：`PUBLIC-ASSETS-PRESENT / SEALED-EXCLUDED / QA-NOT-REPLAYED-HERE`
**能力状态**：不在本文件记录
**合同**：`TASK-20260913-001` v3 Sol 施工合同
**rubric 冻结状态**：`NOT-FROZEN`（等待用户逐模块确认）

本表汇总的是历史构建与 controller QA 记录。当前仓只收公开学习材料，未收 sealed/holdout/reference/retest 正文，因此不能仅在本仓重放 AC-03/04/05/06 的完整检查。模块 `BUILD_RECEIPT` 的 `QA-PENDING` 是生成回执时状态；其后历史 controller 状态由本表记录。两者都不授予用户能力状态。

| 资产 | public | rubric | training fixture | sealed holdout/reference | D+2/D+7 | receipt | 状态 |
|---|---:|---:|---:|---:|---:|---:|---|
| 公共合同与来源登记 | yes | N/A | N/A | N/A | N/A | N/A | BUILT |
| EdgeIM B-S2 | yes | yes | yes | yes | yes | yes | BUILT |
| EdgeIM B-S3A | yes | yes | yes | yes | yes | yes | BUILT |
| EdgeIM B-S3B | yes | yes | yes | yes | yes | yes | BUILT-WITH-SOURCE-OPEN |
| EdgeIM B-EVAL | yes | yes | yes | yes | yes | yes | BUILT-WITH-SOURCE-OPEN |
| EdgeIM B-DEFENSE | yes | yes | yes | yes | yes | yes | BUILT-WITH-SOURCE-OPEN |
| sigRank P0-P3 | yes | yes | yes | yes | yes | yes | BUILT-WITH-ERRATA |
| Ground Truth P0-P3 | yes | yes | yes | yes | yes | yes | BUILT-WITH-SOURCE-OPEN |
| CrossEdgeIM P0-P3 | yes | yes | yes | yes | yes | yes | BUILT-WITH-SOURCE-OPEN |

`BUILT-WITH-SOURCE-OPEN` 表示模块文件齐全，但 rubric 禁止把缺失来源或参数补成确定事实。
在历史源仓中，`SOURCE-OPEN` 本身不阻止资产 `QA-PASS`；前提是未知项边界已冻结，且没有未关闭的 High/Medium finding。当前快照未独立复验这一前提。

## 已知开放项

1. EdgeIM 原文没有给完整 IM cut、partition、fall-through、Petri-net merge 或 soundness 构造；B-S3B 分层标源。
2. EdgeAlpha/EdgeMiner 原始论文未在本地材料中；谱系 verdict 限定为作者 framing。
3. EdgeIM 数据版本、代码、PM4Py/矿工参数、模型制品、通信与隐私测量均未公开到可复现合同。
4. sigRank teardown 有已确认的表格抄录错误；课程以 PDF 为准并把 errata 作为证据训练。
5. Ground Truth 的代码/数据版本、种子、DS2/DS3 规模与复现实参不完整。
6. CrossEdgeIM 本地 PDF 的 proof/final 身份、数据生成器、实现参数和网络/隐私测量未闭合。

## 禁止自动转换

- `BUILT` 不推出 `FROZEN`：学习前仍需用户确认 rubric。
- `QA-PASS` 不推出用户 `PASS`。
- 文件存在不推出用户 `RETAINED/OWNED`。
- 本文件不得被用作进组能力证明。

## QA 记录

- 第一轮结构检查：8 modules / 66 Markdown / 8 sealed sets，文件、链接、乱码 PASS。
- 第一轮独立语义 QA：REWORK；发现 reference 映射错误、coverage/major-claim 缺口、holdout 同构、PASS/RETAINED 混淆和冷测未冻结。
- 修订后结构检查：`ASSET-STRUCTURE-PASS modules=8 markdown=74 sealed_sets=8`；相对链接、乱码和 staged whitespace 检查通过。
- 独立技术回归：EdgeIM 与 sigRank/Ground Truth/CrossEdgeIM 均无 High/Medium finding；四篇 PDF SHA-256 与 `SOURCE_REGISTER.md` 一致。
- 合同复验：AC-02、AC-04、AC-08 定向复验 PASS；AC-03、AC-05、AC-06、AC-07、AC-09、AC-10 PASS。
- AC-01 provenance：75 个暂存路径全部位于 `ownership-v3/`，该目录无未暂存差异；仓库其他脏改动未纳入本资产提交。
- 历史源仓记录因此达到 `BUILT / QA-PASS`。当前快照只保留公开资产与该记录；这不表示 rubric 已由用户 `FROZEN`，也不改变用户的 `PASS / RETAINED / OWNED`，不写 Ledger。
