---
id: TASK-20260915-007
title: ownership-v3 三缺口方案订正+缺口1部分执行+交接文档落盘
date: 2026-09-15
runtime:
  model: Fable 5
  effort: high
  effort_source: 会话内多轮独立核验深度（pdftotext逐页核对+git log溯源+跨文档追溯）
  launch: Claude Code CLI（用户交互会话，非无人值守）
type: research
status: in_progress
area: learning/training/lu-edgeim-algo1
project: lu-side
todo_ids: []
owners:
  - user
related:
  - progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md
  - progress/task_logs/2026/09/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md
  - progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md
  - progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md
  - learning/training/lu-edgeim-algo1/ownership-v3/BUILD_STATUS.md
---

# 目标

响应用户"现在做"指令，把上一任务（`TASK-20260915-005`）交付的三缺口方案从"方案"推进到"执行"：(1) 订正方案文档自身发现的两处错误；(2) 实际执行缺口1（独立QA）的抽样核对；(3) 应用户"先存一份交接文档"的要求，把当前进度、后续步骤、检查点、验收标准、测试方案完整落盘，而不是继续无边界地往下抽样。

# 最终结果

三项均有实质进展但均未完全收尾：

1. **方案文档订正**：发现并修正了 `2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md` 中两处自身错误——缺口1/缺口2建议的新文件路径原稿误写入 `ownership-v3/` 目录内部，违反 v3 合同 §8.1 "Sol第一阶段唯一写域"（已订正到该目录外）；缺口2标注的"Transfer Card判定枚举待查"阻塞经进一步溯源到 `2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md` §P4/P5 后确认已解除（枚举=`DROP/PARK/PROMOTE`，配套模板 `research_growth/方法论/TRANSFER_CARD_TEMPLATE.md` 真实存在）。两处订正均以 Amendment 形式追加，未静默改写原文。
2. **缺口1部分执行**：用 `pdftotext` 逐页提取 EdgeIM 原始 PDF，核对 B-S3B 模块声称的三处论文坐标（p.3 Definition 5、p.5 Algorithm 3 lines 9-23、p.6 soundness 叙述），三处全部精确核对通过。B-EVAL 的范围声称（pp.5-7）和 CrossEdgeIM P0-P3 的目录/哈希也做了初步核对，但两者的任务内容可执行性尚未深入核对。同时发现一处可能影响最终验收结论的问题：`BUILD_STATUS.md` 自报 AC-07 PASS，但抽样发现该 AC 涉及的"consumer 明确"实际只是字段预填、未见真正消费（正是缺口2的技术根源），这处发现已记入交接档待纳入最终 `CONTROLLER_ACCEPTANCE.md`。
3. **交接文档落盘**：新建 `progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md`，按用户明确要求的六项（计划/步骤/检查/评审/验收标准/测试方案）逐项对应组织内容；同时发现并如实记录一处新的前置阻塞——`TASK-20260906-004` 在 `INDEX.md` 与自身 task log 之间存在状态冲突（`completed_with_open_gates` vs `in_progress`），v3合同§8.1明文要求这个冲突必须先解决才能做共享正本接线，直接影响缺口3方案A的可执行性；已如实上报，未擅自裁定。

# 修改内容

- `progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md`：追加 Amendment A1，订正两处路径错误、解除枚举阻塞标注、新增缺口3前置阻塞记录；§5决策面表格三行同步更新。
- 新建 `progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md`：完整交接文档，含三缺口执行步骤表、AC-01~AC-10逐条抽样判定、测试方案模板、未完成项触发条件表。
- `progress/handoff/INDEX.md`：用 `ledger_edit.py` 保形插入一行最新交接记录（CAS校验通过，sha256 `3a25d85...` → `e8d9ae7...`）。
- 本条目：新建本任务日志；`progress/task_logs/INDEX.md` 待用 `ledger_edit.py` 保形插入（见下方登记步骤）。
- 未修改 `ownership-v3/` 任何文件（Sol独占写域）；未修改任何已冻结正本；未裁定 `TASK-20260906-004` 状态冲突。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| B-S3B三处坐标核对方法可信 | 直接pdftotext提取原始PDF逐字比对，非读课程材料转述 | PASS | `pdftotext -f 3/5/6 -l 3/5/6`输出逐字包含"Definition 5. (Petri Nets)"/"Algorithm 3: Feature-Preserving Sampling"（第9-23行为递归函数体）/"To ensure model soundness, EdgeIM employs more invisible transitions" |
| 方案文档路径订正有据 | v3合同§8.1原文核对 | PASS | 合同文件312-318行："Sol 第一阶段只写：`learning/training/lu-edgeim-algo1/ownership-v3/`" |
| 枚举阻塞解除有据 | 溯源到BRIEF.md A4引用的源头文档 | PASS | `2026-09-05__research__lu-learning-lineage-transfer-plan-delta.md`§P4原文"只能得到DROP/PARK/PROMOTE之一" |
| TASK-20260906-004状态冲突真实存在 | INDEX与自身日志frontmatter对比 | PASS | `INDEX.md:41`记`completed_with_open_gates`；日志frontmatter记`status: in_progress`；合同437行本身也明文记录此冲突 |
| 交接文档六项要求逐一对应 | 用户原话六项（计划/步骤/检查/评审/验收标准/测试方案） | PASS | 交接档§3有逐项对照表 |
| handoff INDEX保形写入 | ledger_edit.py CAS保护 | PASS | 写后sha256=`e8d9ae7f26207f4193276f9bc214f48e2a03b8f1ecc8f5d86b06678155db1c48`，VERIFY-OK |
| task_id中央领号 | POST获取非目测自增 | PASS | 本任务号`TASK-20260915-007`；此前误用一次`TASK-20260915-006`（见Amendment） |

# 当前状态

三缺口方案的错误已订正，缺口1的抽样核对启动并有一个模块（B-S3B）完整通过，交接文档已完整落盘可支持随时中断续接。缺口1的B-EVAL/CrossEdgeIM P0-P3剩余抽样、缺口2的桥接文档撰写、缺口3的正式写入均未开始，均在交接档§4/§7列出明确的触发条件和下一步。用户"针对整体的进一步优化方案"这一更大范围的要求，本次仍只按三个已知缺口处理，未去猜测是否有更大范围诉求——这一点已在交接档§8明确标注为待澄清项，不是本任务遗漏，是主动留白。

# 尚未完成

- 缺口1：B-EVAL六项任务可执行性核对、CrossEdgeIM P0-P3四阶段内容可执行性核对、最终`CONTROLLER_ACCEPTANCE.md`产出（路径已定：`progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/`，目录已建但文件未写）。
- 缺口2：用户尚未对方案A表态；`TRANSFER_CARD_BRIDGE.md`未撰写。
- 缺口3：`TASK-20260906-004`状态冲突尚未获用户裁定；正式写入CrossEdgeIM P0-P3 README需要下一次Sol施工窗口。
- "整体优化方案"的范围澄清（三缺口是否等于全部，还是还有更大范围诉求）——尚未获用户回应。

# 下一步

1. 用户对交接档§7/§8表态后按对应触发条件继续。
2. 若继续缺口1：直接套用交接档§6测试方案模板覆盖剩余范围，产出`CONTROLLER_ACCEPTANCE.md`。
3. 若用户澄清§8范围且诉求大于三缺口：需要重新规划，不在本任务范围内直接扩大执行。

# 可拓展方向

- 交接档§5发现的"AC-07自报PASS可能过于宽松"这一处，如果最终验收判定为需要改判，`BUILD_STATUS.md`本身要不要同步更新是��个需要用户决定的问题（改自报文件属于touch `ownership-v3/`内部文件，即便由主控做也需谨慎——严格说这可能仍算触碰Sol写域，需要下次讨论由谁、以什么方式做这处更正）。

# 风险与回滚

- 风险：交接文档本身篇幅较大，如果后续窗口只读摘要不读原文，可能重复本次已解决的枚举/路径问题。缓解：交接档§1明确列出"不要重新分析三缺口是什么"，且Amendment记录清晰可查。
- 回滚：本任务只新增文件+两处保形插入，删除新建文件和还原两处INDEX插入行即可完全回滚。

# 文件和产物

- `progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md`（追加Amendment）
- `progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md`（新建）
- `progress/handoff/INDEX.md`（保形插入一行）
- 本文件

## Amendment

**A1（本次记录内）**：执行过程中曾误用中央allocator返回的`TASK-20260915-006`（在核对完B-S3B模块前领取，因中断未使用），最终登记以`TASK-20260915-007`为准；`006`号视为已发出未使用的正常空号，不回收也不重复登记，符合协议本身"发出即占用，不回收"的设计。
