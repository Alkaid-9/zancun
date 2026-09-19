---
id: TASK-20260905-004
title: 独立科研台三源材料改进方案与阶段0语义合同
date: 2026-09-05
runtime:
  model: Codex GPT-6
  effort: n/a
  effort_source: 当前托管会话未暴露可审计 reasoning-effort 字段
  launch: API-hosted Codex
type: research
status: completed_with_open_gates
area: research-desk
project: jinzu-sprint
todo_ids: []
owners:
  - user
  - codex
related:
  - progress/decisions/2026-09-05__research__independent-research-desk-design-alignment.md
  - progress/decisions/2026-09-05__research__research-desk-three-source-improvement-proposal.md
  - progress/decisions/2026-09-05__research__research-desk-stage0-semantic-contract.md
  - /mnt/d/Alkaid/Desktop/工作簿1.xlsx
  - /mnt/d/Edge下载/研究操作符与横向迁移案例册.md
  - /mnt/d/Edge下载/科研学习与训练体系-v0.1.md
---

# 目标

纠正三份材料的任务归属，并把它们用于改进独立科研台的对象模型、证据链、操作符、学习记录和渐进式实施路线。

# 最终结果

已完成三份材料的只读盘点和范围纠偏。工作簿归入原始摘录收件箱；操作符案例册归入 Operator/TransferCard 候选库；科研学习体系归入 LearningSession、能力观察和复测协议。已新增三源材料改进提案和阶段 0 语义合同，仍为设计提案，未实现科研台、导入器、同步或技术栈。

# 修改内容

- 追加科研台架构对齐检查点 §10，明确三份材料不属于 EdgeIM 题面、答案或 PASS 证据。
- 新建三源材料改进提案：对象层、拓扑、界面路线、P0 主链、阶段 0–5 和回滚门。
- 新建阶段 0 语义合同：manifest 字段、导入粒度、稳定 ID、状态机、P0 候选问题和阶段验收。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 三源读取 | 文件、表结构、章节结构和内容角色已核对 | PASS | 三份输入只读命令输出；提案 §2 |
| 输入快照 | 路径、SHA-256、版本冲突记录 | PASS | 阶段 0 合同 §1 |
| 归属纠偏 | 不把摘录/操作符/训练体系直接当 EdgeIM 答案 | PASS | 对齐检查点 §10 |
| 对象边界 | raw/research/learning/index 四层分开 | PASS | 提案 §3.1；合同 §2 |
| 稳定 ID | 不依赖移动路径或 UI 排序 | PASS | 合同 §3 |
| 状态边界 | candidate、confirmed、UNKNOWN 和复测分轴 | PASS | 合同 §4 |
| P0 闭环 | 已提出但尚未冻结的真实问题与主链 | PROPOSED | 合同 §5 |
| 实现范围 | 未写导入器、数据库、UI、同步或工作台运行时 | PASS | git status 与本日志 |

# 当前状态

`completed_with_open_gates / DESIGN-ONLY`。材料和设计提案已存档；阶段 0 仍等待用户确认 P0 问题、manifest 字段、ID 和状态词。

# 尚未完成

- 未建立只读来源库或 `sources.manifest` 正式产物。
- 未导入工作簿摘录、操作符卡或训练体系为正式研究对象。
- 未实现科研台 UI、数据库、搜索、Map、Comparison 或桥接适配器。
- 工作台、Obsidian、Reviva 和 EdgeIM 学习包均未因本任务获得运行时或题面改动。

# 下一步

1. 用户确认阶段 0 语义合同和 P0 候选问题。
2. 仅在确认后建立三源只读 manifest 与 source index。
3. 通过一个 Excerpt → Note → Claim candidate → Evidence link 的小闭环验收可回链性。

# 可拓展方向

- 阶段 1：来源库和 provenance 浏览。
- 阶段 2：研究对象与 Evidence/Review Inbox。
- 阶段 3：Operator、TransferCard 与 LearningSession。
- 阶段 4：Map、Comparison、Team Timeline。
- 阶段 5：WorkBench、Obsidian、Reviva 的文件优先桥接。

# 风险与回滚

- 风险：三源内容被扁平化为无来源知识表。控制：保留 source_id、locator、哈希和状态转换。
- 风险：AI 候选关系被当事实。控制：候选层和 Review Inbox，禁止自动提升。
- 风险：科研台复制工作台任务状态。控制：执行事实仍归工作台，科研台只保存链接和 Evidence 回链。
- 回滚：删除新增设计/日志文件并移除对应登记；不删除三个原始输入、不改 EdgeIM 学习包、不改工作台事实。

# 文件和产物

- `progress/decisions/2026-09-05__research__independent-research-desk-design-alignment.md`
- `progress/decisions/2026-09-05__research__research-desk-three-source-improvement-proposal.md`
- `progress/decisions/2026-09-05__research__research-desk-stage0-semantic-contract.md`

