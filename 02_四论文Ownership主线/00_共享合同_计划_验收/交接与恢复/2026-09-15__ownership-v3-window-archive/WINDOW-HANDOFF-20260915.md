# 窗口交接单 - ownership-v3三缺口补修+TASK-20260906-004状态裁定+AB融合

> 交接编号：OWNERSHIP-V3-WINDOW-20260915-01｜当前停点：用户"停一下，存档！"指令后的应急归档｜适用对象：下一个处理lu-side/ownership-v3任务的窗口

## 1 先读顺序

1. `WINDOW-ARCHIVE-20260915.md` §2（当前权威状态表）——一分钟看懂全局。
2. `progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md` Amendment A3（最新决策，本窗口刚追加）。
3. `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md` §2.5和§3（Ground Truth FAIL详情，最重要的新发现）。
4. `progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md`（补修队列现状，#3已更正）。
5. 本文件其余各节。

**不要只读上述文件的摘要/标题就下结论**——尤其Amendment A3和CONTROLLER_ACCEPTANCE.md§2.5，里面有具体的坐标行号和grep证据，直接影响下一步判断。

## 2 一句话现状

三缺口方案的技术前置全部核实/解除完毕，独立QA坐标层核验100%完成（8/8模块，发现Ground Truth P0-P3有3处真实错误），但缺口2/3的实际执行动作（撰写桥接文档/写入CrossEdgeIM README）仍分别卡在"用户批准"和"Sol施工窗口"两道门上，均未打开。

## 3 下一步可选入口

| 入口 | 前置对齐项 | 阻塞条件 |
|---|---|---|
| A. 处理Ground Truth P0-P3的3处错误 | 先确认这3处是否有其他来源依据（论文补充材料/其他版本），排除"课程材料幻觉"这一更严重可能性 | 需要有人（用户或下一窗口）先做这个溯源核查；修复本身需Sol写域 |
| B. 批准并撰写`TRANSFER_CARD_BRIDGE.md` | 用户需明确说"写"（不是"融合方案听起来合理"这种间接表态） | 无技术阻塞，纯粹等用户一句话 |
| C. 移交缺口3锚点给Sol施工窗口 | 无——方案文档§4的锚点内容已经是可以直接复制使用的成品 | 需要一次真正的Sol施工窗口（本主控身份无写权限） |
| D. 裁定`BUILD_STATUS.md`由谁改、如何改 | 需要先知道A的溯源核查结果，否则裁定基础不完整 | 依赖A |

**建议顺序**（非强制）：D依赖A，B和C相互独立可随时推进，A是当前唯一还有"不确定性"（是否真的是课程材料错误）的一项，值得优先安排。

## 4 恢复前检查单

- [ ] 已读`CONTROLLER_ACCEPTANCE.md`最新版（含§2.4-2.8五模块记录，非只读旧的3模块版本）
- [ ] 已确认`progress/task_logs/INDEX.md`当前哈希（跑`ledger_edit.py progress/task_logs/INDEX.md --check`），不假设本归档包写完后哈希不再变化（其他并发窗口可能已追加新行）
- [ ] 已理解"AB融合"≠"缺口2/3已获批准执行"这条区分（Amendment A3明确区分方案层面确认与执行批准）
- [ ] 若要处理Ground Truth错误，先用`pdftotext -f 1 -l 30 -layout research/papers_lu/Sommers-2025-ProcessScience.pdf -`重新独立核验一次，不要直接信任本归档包转述的grep结果（虽然本次核验方法可信，但"不读转述、只读原文"这条纪律应对每一次新决策都重新适用）
- [ ] 若要触发Sol施工窗口，先确认`ownership-v3/`当前git状态（是否有其他窗口正在写）

## 5 当前不可变状态（只有新证据才能追加superseding）

- `TASK-20260906-004`的INDEX状态已更正为`in_progress`，这是基于其自身task log和§8整合清单原文的事实裁定，**不应被下一窗口无理由改回`completed_with_open_gates`**——除非有新证据表明该任务的"共享正本整合"（§8清单其余9项）已经真正完成。
- `CONTROLLER_ACCEPTANCE.md`记录的8个模块坐标层判定（7 PASS + 1 FAIL）是当前时刻的独立核验结果，如果`ownership-v3/`内对应文件被Sol修改过，**这些判定可能已经过时**，下一窗口使用前应先检查对应README的git log/mtime是否比本次核验（2026-09-15）更新。
- 三缺口方案文档头部仍是`DRAFT / AWAITING-USER-APPROVAL`，这个状态**没有被本窗口任何操作改变**——Amendment A3只是追加记录，不是批准声明。

## 6 已知脏工作区处理

本窗口结束时，工作区包含以下未commit的变更（均为本窗口或此前会话产生，未push）：
- `progress/task_logs/INDEX.md`（多次insert+1次replace）
- `progress/task_logs/2026/09/`下新增两份task log
- `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`
- `progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md`
- `progress/decisions/2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md`
- `progress/handoff/2026-09-15__ownership-v3-window-archive/`（本归档包）
- 会话开始时已存在的`GUARDRAILS.md`、`WINDOW_PLAYBOOK.md`的修改（**这两份文件本窗口未触碰**，属于其他并发窗口的在途工作，不应被本窗口的commit意外打包）

**处理建议**：commit时应分开处理——本窗口的变更（上述前6项）可以合并为一次commit，但`GUARDRAILS.md`/`WINDOW_PLAYBOOK.md`的改动应留给对应的窗口自己commit，避免"多窗并行amend危险"（历史教训：commit-tree树级拆分优于混合commit）。**本窗口未执行任何commit/push动作**，留给用户决定。

## 7 交接完成条件

接棒窗口应在开始新工作前，先在自己的task log或决策档中记录：
1. 已读本交接单及§1指定的先读顺序文件。
2. 对§3的四个入口选择了哪一个（或全部暂不处理），并说明理由。
3. 若选择入口A（Ground Truth错误处理），独立重新做一次核验而非直接信任本包的grep结果转述。
