---
id: TASK-20260916-006
title: 进组材料全景盘点+研究方法论基建盘点：存盘落档（现状+方案+标准线），发现BR-1逾期未查等4项拍板缺口
date: 2026-09-16
runtime:
  model: Fable 5
  effort: high
  effort_source: 4路独立Explore子代理实地核查(研究地图/团队谱系/bridge跨领域比对/OpenReview+错题集+工业界追踪)+主控直接文件核查(简历/OE1/T5/proposal-notes死链)
  launch: Claude Code CLI（用户交互会话，非无人值守）
type: research
status: done
area: progress/audits;progress/decisions
project: jinzu-sprint
todo_ids: []
owners:
  - user
related:
  - progress/projects/jinzu-sprint.md
  - progress/projects/lu-side.md
  - progress/decisions/2026-08-31__research__bridge-research-and-teardown-status.md
  - progress/decisions/2026-09-06__research__lu-sun-intersection-matrix-and-group-entry-reframe.md
  - progress/handoff/2026-08-24__research__br1-nsfc-check-card.md
note: 领号时curl中央发号器返回TASK-20260916-006；紧接TASK-20260916-005，无跳号问题，本次为全新正常领号
---

# 目标

用户连续两轮追问"进组全景状态"（先问进组材料消费面，追问研究方法论基建：知识图谱/菌丝网/科研地图/团队脉络/领域全景/跨领域方法论比对/OpenReview追踪/错题集/工业界追踪）。本任务对两轮追问的全部发现做正式存盘，同时为每个缺口配一份解决方案与"什么算做完"的标准线，并把需要用户拍板的决策项正式挂入 `PENDING.md`。

# 最终结果

**存盘完成。核心发现：进组材料线上有一个逾期16天从未执行的检索动作（BR-1），研究方法论基建呈现"两块真骨头（研究地图/错题集）+ 一块主动冻结的空壳子（bridge/）+ 三块一次性未成持续机制（团队谱系/OpenReview追踪/工业界追踪）+ 两个明确缺口（字面知识图谱数据结构/鲁组线学术全景）"的格局。**

## 进组材料消费面（jinzu-sprint）

1. 简历一页纸（`resume_onepage.md`）：内容详实，占位符未填，属纯信息填空不需设计。
2. OE-1致鲁老师邮件v4：正文已定稿（约460字，≤500达标），但走A/B分支依赖的**BR-1（NSFC放榜复查）操作卡窗口是8-25~8-31，今天09-16，检索从未被执行**——不是查了没结果，是从未开始；且邮件原定投递窗口"9月1-15日"已经过期。这是本次盘点发现的最紧迫单点。
3. T5提案：`draft-complete/offline-assets-ready/backend-hold`是既定分期设计（2027 H1才启动正式实验），不算遗漏。
4. **发现真实死链**：`jinzu-sprint.md`§5指针"`companion-survey/14_academic/proposal-notes.md`"与T5提案内部引用"`casual/companion-survey/14_academic/proposal-notes.md`"两个路径互相矛盾，全仓搜索（含worktrees排除）均未命中实体文件——不擅自处理，记录待用户核实。

## 研究方法论基建

- **真实建成**：研究地图五层结构（L0全域38篇+L1鲁孙两侧各300+行详实版图+L2交叉带矩阵收敛出"过程感知的LLM-MAS安全"空白）；错题集`MISTAKE_LOG.md`（09-03过滤器/采样器混淆真实事故完整记录，非设计文档）。
- **设计完成、内容从未填充、主动冻结**：`bridge/`跨领域方法论比对五个核心文件均为07-25骨架，CONCEPT_MATRIX.md 22个问号至今未填；08-31决策档明确降级但未说清是否彻底停填，处于"没人正式判死也没人在推"的悬空态。
- **一次性事件、未成持续机制**：团队谱系（孙猛五时期谱系DRAFT未定稿，鲁法明侧只有单篇41KB无分期结构）；OpenReview追踪（BR-7"5条隐藏ID"核验挂账未做，无常态扫描机制）；工业界追踪（8-12/13一次性扫描，多标"需验证"未闭合，未持续更新）。
- **明确缺口**：字面意义知识图谱数据结构不存在（现有是Markdown文档，语义覆盖但非图结构）；鲁组线没有对标孙组phase0规模的学术型八大知识块全景研报。

# 修改内容

- 新建 `progress/audits/2026/09/2026-09-16__jinzu-and-research-infra-landscape/LANDSCAPE_AND_PROPOSALS.md`：完整盘点+每项解决方案+标准线，明确标注"方案未经拍板，落盘为存档目的"。
- 编辑 `progress/decisions/PENDING.md`：CAS保护新增4项决策（`DEC-OE1-WINDOW-SLIP`/`DEC-BRIDGE-DORMANT-OR-ARCHIVE`/`DEC-PROPOSAL-NOTES-PATH`/`DEC-SCHOLAR-ALERT-SETUP`）。
- 本条目：新建task log；`INDEX.md`用`ledger_edit.py`保形插入。
- 未修改任何正本内容（研究地图、bridge/、简历、OE1邮件、T5提案均只读核查，未改一字）。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 4路独立Explore核查均为实地读取而非转述 | 子代理报告需附具体文件路径+内容摘要，非仅列文件名 | PASS | 4份子代理报告均含文件路径+行数/字节数+内容概括 |
| BR-1逾期判断有依据 | 操作卡明确窗口8-25~08-31，非主观臆测 | PASS | `progress/handoff/2026-08-24__research__br1-nsfc-check-card.md` |
| proposal-notes.md死链非误判 | 全仓find两种路径变体均零命中 | PASS | `find ... -iname "proposal-notes.md"` 排除worktrees后零命中 |
| PENDING.md写入CAS保护 | `--expect-sha256`校验通过，写后复验哈希 | PASS | 见"当前状态"节 |
| INDEX.md写入CAS保护 | 同上 | PASS | 见"当前状态"节 |
| 报告文档无乱码字节 | grep "�" | PASS | 编辑后复扫0命中 |

# 当前状态

`LANDSCAPE_AND_PROPOSALS.md`已落盘；`PENDING.md`新增4项决策已CAS保护写入并复验；本task log已登记INDEX。全部为记录/建议性质，未执行任何实际修复或改动（proposal-notes.md死链未修、BR-1检索未代查、bridge/未归档）——这些都在文档里明确列为待用户裁定或建议下一步执行的动作，不在本任务范围内擅自处理。

# 尚未完成

- BR-1检索本身（10分钟公开网页查询，AI可代查但结论仍需用户确认裁定A/B分支）——建议下一个窗口第一件事执行。
- 4项PENDING决策等用户表态。
- proposal-notes.md死链的实际去向核实（可能在仓外，需要用户确认）。

# 下一步

1. 若用户下一句话即授权，可立即执行BR-1检索（不需要登录态，纯公开网页查询）。
2. 等用户对4项PENDING决策表态后，按对应解决方案节执行。
3. 孙猛团队谱系DRAFT审阅——已有明确归属（`progress/decisions/2026-09-06__research__lu-sun-intersection-matrix-and-group-entry-reframe.md`），本任务只是重申，不新增待办。

# 可拓展方向

- 本次发现的"操作卡写了明确窗口但从未被任何窗口消费执行"这一模式（BR-1）可能不是孤例——建议下次全局审计时专门扫一遍所有带`[窗口:日期~日期]`标注的操作卡，检查是否还有类似的"设计完成但从未执行且已过期"的挂账项。

# 风险与回滚

- 风险：无。本任务只做记录与建议，未修改任何正本内容，未执行任何不可逆动作。
- 回滚：如需回滚，删除本task log对应INDEX行、删除PENDING.md新增的4行、删除新建的LANDSCAPE_AND_PROPOSALS.md文件即可完全恢复到任务前状态。

# 文件和产物

- `progress/audits/2026/09/2026-09-16__jinzu-and-research-infra-landscape/LANDSCAPE_AND_PROPOSALS.md`（新建）
- `progress/decisions/PENDING.md`（编辑，+4行）
- 本文件
