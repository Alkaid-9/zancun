# 维护手册 - ownership-v3三缺口补修窗口档案与状态治理

> 面向：维护者、主协调Agent、独立复核Agent
> 原则：历史可审计、当前可定位、未来不冒充已完成

## 1 权威层级（冲突时回原始证据追加纠正，不覆写历史）

1. 磁盘原始PDF（`research/papers_lu/`）——任何坐标声称的最终真相来源。
2. v3合同（`progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md`）——写域边界、诊断阶段定义的权威。
3. 三缺口方案文档（含Amendment历史）——方案演进的权威，含批准状态。
4. `CONTROLLER_ACCEPTANCE.md`——独立QA坐标层判定的权威。
5. `teaching-debt-priority-queue.md`——补修优先级与依赖关系的权威。
6. `progress/task_logs/INDEX.md`——所有task_id状态的共享登记权威。
7. 本归档包——窗口过程记录，**不覆盖以上任何一层**，只提供"当时的快照"。

**冲突处理**：若本归档包的描述与上述1-6层任何一层的当前内容不一致（比如`CONTROLLER_ACCEPTANCE.md`后来又被更新了），以当前磁盘内容为准，本归档包保留作历史记录，不回改。

## 2 追加式维护规则

- 本归档包6件文件一旦生成，**后续窗口不得直接编辑**，只能在同目录新增日期化的后续包（比如`2026-09-16__ownership-v3-window-archive-02/`）。
- `CONTROLLER_ACCEPTANCE.md`、`teaching-debt-priority-queue.md`、三缺口方案文档三份"活文档"允许持续追加（Amendment/新增小节），但不允许删除已有历史记录段落。
- `INDEX.md`只能用`ledger_edit.py`编辑，不允许整文件重写。

## 3 状态词典（引用runbook §5，本线专有态补充）

| 状态词 | 含义 |
|---|---|
| `DRAFT / AWAITING-USER-APPROVAL` | 方案已写完，未获批准执行 |
| `PARTIAL-CONTROLLER-PASS（坐标层）` | 独立QA只做了部分模块的坐标层核验（本窗口前半段状态，已被下方状态取代） |
| `CONTROLLER-PASS-WITH-ONE-FAIL（坐标层，8/8已核）` | 独立QA坐标层已覆盖全部8个抽样模块，其中1个FAIL（本窗口当前状态） |
| `completed_with_open_gates` | task日志/INDEX状态：主要工作完成但有已知未关闭的门 |
| `in_progress` | 任务仍在进行，未完成 |
| `done` | 任务本身（如一次状态裁定）已完整完成 |

## 4 新工作包登记模板

若后续窗口要继续处理Ground Truth错误/缺口2/缺口3，新task log应包含：
```
related:
  - progress/handoff/2026-09-15__ownership-v3-window-archive/WINDOW-HANDOFF-20260915.md
  - progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md
```
并在"目标"段明确引用本归档包§3对应的入口编号（A/B/C/D）。

## 5 基线与哈希维护

- `INDEX.md`当前哈希（本归档包生成时刻）：`8a061edb8b73ce8dc64fdd2c02cfe189cf4352e0651d1cc410a675a3fcb21a7a`（314行，纯CRLF）。**这个哈希会随其他并发窗口的追加而很快过期**，使用前必须重新跑`ledger_edit.py progress/task_logs/INDEX.md --check`获取当前值，不能直接信任本手册记录的值。
- 本归档包6件文件+manifest的sha256见`WINDOW-ARCHIVE-MANIFEST-20260915.sha256`，这个哈希不会过期（除非文件被篡改）。

## 6 脏工作区维护

见`WINDOW-HANDOFF-20260915.md` §6。核心原则：commit前用`git diff --stat`确认变更范围只包含本窗口应负责的文件，不要把其他并发窗口在途的`GUARDRAILS.md`/`WINDOW_PLAYBOOK.md`改动一起打包进同一个commit。

## 7 多Agent维护纪律

- 并行子代理只做只读核验时，不需要`isolation: worktree`（无文件写入冲突风险）。
- 每个子代理prompt必须包含4 caps（本窗口5个子代理全部遵守），且要求"具体证据（grep命中原文片段+行号）"而非允许模糊断言，这是保证并行核验质量的关键约束，后续窗口复用此模式时不应省略。
- 交叉核验型子代理（如B-S3A核验时被告知B-S3B的既有结论）需要在prompt中明确标注"背景信息"性质，避免与真正独立盲核的子代理混淆职责。

## 8 文档一致性检查

后续维护者定期（比如每次Sol施工窗口结束后）应跑一次：
```bash
grep -rn "PARTIAL-CONTROLLER-PASS" progress/  # 应该已经没有引用，若有说明某处描述过时未同步
grep -rn "completed_with_open_gates" progress/task_logs/INDEX.md | grep "TASK-20260906-004"  # 应该查无结果，若有说明状态被意外改回
```
若发现旧状态词残留在应该已更新的地方，按"追加纠正"处理，不静默覆盖。

## 9 本线专有维护规则

- CrossEdgeIM论文作者非鲁法明——任何涉及CrossEdgeIM的维护动作都不得引入"鲁法明署名论文"这类错误归因表述。
- 四篇论文F-measure数字不可直接并表——维护`CONTROLLER_ACCEPTANCE.md`或类似汇总文档时，任何跨论文的数字对比都要检查是否违反此规则。

## 关闭和重新打开条件

**本归档包关闭**（不再是"当前"参考）的条件：Ground Truth错误已修复且重新核验PASS、缺口2/3执行完成、`BUILD_STATUS.md`一致性问题已裁定处理——四项全部满足后，下一窗口应生成新的收官归档包并在其中声明"本包supersede OWNERSHIP-V3-WINDOW-20260915-01"。

**重新打开**条件：若发现本包记录的任何裁定（尤其TASK-20260906-004状态裁定）依据的原始证据后来被证明有误，应在对应权威文档追加纠正记录，并在本包同目录追加一份`CORRECTION-<日期>.md`说明，不回改本包正文。
