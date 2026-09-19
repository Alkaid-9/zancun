---
id: TASK-20260915-015
title: ownership-v3 三缺口+早期教学债合并为优先级队列（J2）
date: 2026-09-15
runtime:
  model: Fable 5
  effort: high
  effort_source: 合并前逐条核对三份来源文档的行号锚点，发现并修正两处引用偏差
  launch: Claude Code CLI（用户交互会话，非无人值守）
type: research
status: design_only
area: learning/training/lu-edgeim-algo1
project: lu-side
todo_ids: []
owners:
  - user
related:
  - progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md
  - progress/decisions/2026-09-14__research__multilayer-content-map-provisional-baseline.md
  - progress/decisions/two-desks-delta-20260914/REFERENCE_EVALUATION.md
  - progress/decisions/2026-09-15__research__lu-onboarding-supplement-next-plan.md
  - progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md
---

# 目标

执行[进组补充计划](../../../decisions/2026-09-15__research__lu-onboarding-supplement-next-plan.md) §3 J2步骤：把三缺口交接（`TASK-20260915-007`）和已独立核对确认仍未关闭的5项早期教学债（完整IM/过程树/Petri net/soundness链、30分钟连续追问、跨四篇D2、QA总表一致、EX-05真实卡点）合并为一张有优先级结构的队列，每项标目标文件/负责人/来源/验收/停止条件；不重写全课程，不裁定任何未决事项。

# 最终结果

新建`progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md`，含8项队列条目（3项来自三缺口交接，5项来自早期教学债）和一张依赖关系图。合并过程中发现并修正了自己起草时的两处引用偏差：缺口2/缺口3最初引用交接文档的行号（59/72）实际落在表格标题行而非各自小节标题，核对交接文档`## §4`下`### 缺口2`/`### 缺口3`实际起始行（55/68）后已订正为准确锚点。其余引用（早期基线:48/55、参考评估:57-61）逐条核对原文内容与行号一致，未发现新的偏差。

# 修改内容

- 新建 `progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md`：8项队列+依赖图+4条验收标准（Q-AC1~Q-AC4）+边界声明。
- 本条目：新建本任务日志；`progress/task_logs/INDEX.md` 待用 `ledger_edit.py` 保形插入。
- 未修改任何已冻结正本、未修改`ownership-v3/`内任何文件、未裁定队列中任一项的阻塞（方案A/B表态、`TASK-20260906-004`状态冲突）。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 队列8项均有目标文件/负责人/来源三项 | 逐行核对表格完整性 | PASS | 队列文档§2表格8行，"待定"项如实标注而非留空 |
| 引用行号准确 | 对照三份来源文档实际行内容 | PASS（发现2处偏差并订正） | 交接文档`grep -n "^### 缺口"`确认缺口2=55行、缺口3=68行（非最初误引的59/72）；早期基线48/55行、参考评估57-61行经`sed -n`核对内容吻合 |
| 依赖图不虚构顺序 | 只标注来源文档明确写出的硬依赖 | PASS | §3依赖图仅含4条边（#3←用户裁定、#2←用户表态、#7←#1、#6←#4），均可在来源文档中找到对应文字依据 |
| 文档无乱码字节 | grep "�" 全文扫描 | PASS | 扫描结果0命中 |
| 纯LF无CRLF混杂 | python3哈希探测 | PASS | CRLF=0, LF=47 |

# 当前状态

J2已完成到"队列已存在且结构完整"的程度。队列本身是设计产物（`DESIGN-ONLY / NOT-EXECUTED`），不代表任何一项缺口/债务的实际补修已经开始或完成——队列中#1（独立QA）此前已有部分抽样进展（见`TASK-20260915-007`），其余7项均未开始实际补修工作，这是队列文档如实反映的现状，不是本任务遗漏。

# 尚未完成

- 队列8项本身的实际补修：全部未开始或部分开始（仅#1有前序进展）。
- 队列中3项客观阻塞仍待用户处理：#2/#3的方案表态与状态冲突裁定（与此前`TASK-20260915-007`记录的阻塞相同，未重复裁定）。
- #7（QA总表一致）"谁来改`BUILD_STATUS.md`本身"这一问题——`TASK-20260915-007`可拓展方向中已提出但未解决，本次队列文档只是重申依赖关系，未新增解法。

# 下一步

1. 若用户对#2方案A/B或#3状态冲突表态，对应项可解除阻塞进入实际执行。
2. #1（独立QA）可不依赖任何用户裁定继续推进——直接推进B-EVAL/CrossEdgeIM P0-P3剩余抽样是当前唯一"无阻塞可继续"的实质性技术工作。
3. #8（EX-05真实卡点）本质需要用户本人学习动作，AI只能提供脚手架，不应等同于"AI可以独立推进的下一步"。

# 可拓展方向

- 队列文档目前是静态Markdown表格；如果后续迭代频繁（比如v3合同再升级到v4），可考虑像两张路由卡一样标注"最后核对v3合同版本"字段，避免队列本身又变成新的过期权威。此想法与`TASK-20260915-014`可拓展方向中提出的"路由卡单一来源生成"思路相关，但本次不实施，仅记录。

# 风险与回滚

- 风险：队列的"待定"负责人字段（#2/#5/#6/#7）如果长期不填，容易被后续窗口默认为"没人管"而搁置；缓解手段是队列本身已明确标注这些是"待定"而非"无主"，下次窗口应主动询问而非默认跳过。
- 回滚：新建单文件，删除即可完全回滚，不影响其他已有文档。

# 文件和产物

- `progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md`（新建）
- 本文件
