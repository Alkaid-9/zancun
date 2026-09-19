---
id: TASK-20260916-008
title: 科研项目驾驶舱参考整合方案复核与恢复绑定
date: 2026-09-16
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 托管会话未提供可核实effort；仅交互式有界文档工作
  launch: 用户交互续作
type: research
status: completed_with_open_gates
area: research-desk / workbench-v2 / reference-integration
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
  - progress/decisions/two-desks-delta-20260914/REFERENCE_INTEGRATION_PLAN.md
  - progress/decisions/two-desks-delta-20260914/RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md
  - progress/decisions/two-desks-delta-20260914/_review/20260916_cockpit-review-controller-reconciliation.md
  - progress/handoff/2026-09-16__research-copilot-cockpit-plan__handoff.md
---

# 目标

用户提供“科研副导师 / AI Research Copilot”截图，询问现有系统是否具备其项目台、资料证据、研究路线、Idea评估、文献调研、论文蓝图、章节写作、图表整稿、投稿审查、Skills、导出和Codex入口，并要求把它与此前统一参考清单一起参考；随后要求先构造详细计划、执行步骤、检查、评审、验收标准、划分标准和测试方案，最终以“继续”批准方案落盘。

本任务只交付设计与路由，不修改应用、真实数据、Skills、WP0隔离树或课程，不运行测试／服务／模型，不安装、部署或push。

恢复绑定：会话`01a0aa0a-203a-7290-b7c8-be62c8f1f896`于2026-09-16经用户两次“ok了，继续”明确恢复本线。中央发号器8899不可达，按共享INDEX兜底协议通读当日登记号后取最大值+1，并用`ledger_edit.py`＋CAS登记`TASK-20260916-008`。原草稿号`TASK-20260916-004`已被INDEX明确判为未消费跳号，不能继续沿用。

# 最终结果

新增并复核[科研项目驾驶舱详细方案](../../../decisions/two-desks-delta-20260914/RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md)，把截图八阶段限定为现有正本的派生用户旅程，定义权威分工、参考处置、证据深度、五门状态向量、严重度、G0-P7工作包、八阶段进入／产物／退出合同、检查评审链、测试矩阵、包级与整体完成标准、写域和回退。截图作为R11登记，但保持`IDENTITY-OPEN / SCREENSHOT-ONLY`；没有把可见界面当实际功能或安装授权。

独立评论提出A-E五点后，主控回到实际B合同、research-desk代码、WP-S设计和CURRENT生成链逐项核验。结果为：A／C／E成立但需收窄；B的“仍依赖未冻结提案”前提不成立，真实缺口是未显式钉住已落地但未跟踪的实际合同；D路线成立，但只有Markdown渲染壳成本低，可信跨仓聚合仍需G0数据适配。对账全文见[主控复核回执](../../../decisions/two-desks-delta-20260914/_review/20260916_cockpit-review-controller-reconciliation.md)。

# 修改内容

- 新增本任务计划正本和任务记录。
- 在统一参考清单登记R11，更新当前总数；TASK-010历史“11项”仍保留其当时时点。
- 在两台方案README增加TASK-008当前设计入口。
- 新增主控复核对账和可恢复handoff，原独立评论不改写。
- 共享INDEX只增加TASK-008一行，使用`ledger_edit.py`与CAS保持纯CRLF；不修改其余窗口行。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 范围 | 只有文档与路由，无代码／运行／安装 | 通过 | scoped Git status／diff；应用与真实数据未改 |
| 权威边界 | 科研、学习、任务、Skill、采用分别有唯一正本 | 通过主线程设计检查 | 方案§2 |
| 划分标准 | 处置、深度、门向量、严重度可判定 | 通过主线程设计检查 | 方案§3 |
| 执行方案 | G0-P7均有步骤、依赖、完成条件 | 通过主线程设计检查 | 方案§5 |
| 阶段合同 | 八阶段均有进入、产物、退出及现有能力 | 通过主线程设计检查 | 方案§4 |
| 检查评审验收 | 自测、主控、独立、用户及运行事实分开 | 通过主线程设计检查 | 方案§6/§8 |
| 测试 | 合同、集成、负例、权限、恢复、UI、DEMO、真实试用、回归齐全 | 通过主线程设计检查 | 方案§7 |
| 来源上限 | R11无链接时不宣称身份、实现或可用性 | 通过 | 清单R11及方案页首 |
| 复核对账 | A-E逐项有一手证据、采纳／修正／未决明确 | 主控证据复核完成 | 对账回执 |
| 链接／格式／索引 | 本批本地链接、UTF-8、空白、EOL与INDEX CAS | 通过 | 下列收口复验回执 |

# 收口复验（2026-09-16）

- 恢复绑定与仓库身份：会话、方案、对账、任务日志、handoff和两份INDEX均指向`TASK-20260916-008`；MAS为`master@306cc2b3172c3504c23be913a97f518a707ea217`，相对本地`origin/master`为`+21/-0`，Git index为空。
- 文档机械检查：8份设计链文档均可严格按UTF-8解码；共113个Markdown链接，其中82个本地链接的目标和锚点全部存在；替换字符、冲突标记、尾随空白和未闭合代码围栏均为0。
- 差分与登记面：限定tracked路径按`cr-at-eol`口径执行`git diff --check`通过。task INDEX以`ledger_edit.py`＋CAS只替换008行，保持纯CRLF，写后SHA-256为`72d112525335a2a59d71f5b43519c759212b732fbe9b09e398608867cb8fb6bf`；handoff INDEX保持纯LF，SHA-256为`3f3b5f83c1e3692393196fbacaacc49cf0308fcfd1918aa50b66490b8b558fe4`。
- 语义覆盖检查：R01-R11与I01、八阶段、G0-P7、PLAN-C01-C08、A-E裁定和五门分层均齐；`research-desk`项目卡注册表仍无该slug，未擅自注册。
- 跨仓开放门复核：research-desk仍为`main@0b3a54178e4ec58fb96eb8570101c44d94ac5687`；实际B合同和回执仍未跟踪，应用源码限定路径无差分。该事实不影响本设计任务收口，但继续阻止把B合同称为稳定采收。
- 未运行应用测试、服务、生成器、模型或真实数据库；未commit、push、部署或刷新生成视图。原独立评论保留原文，主控对账另层记录纠正，不静默改写历史。

# 当前状态

本设计任务已按`completed_with_open_gates`收口并完成A-E主控对账，但任何应用施工、外部试用、模型调用、真实资料使用、WP0接驳、部署或push均未授权。当前产品仍是A/B与人工N3已有技术checkpoint、试用和独立复核开放；EXR、C04-C07、WP0自动桥及R11身份仍开放。

# 尚未完成

- R11原始链接、作者、版本、许可与实际功能未核。
- `project: research-desk`不是已注册slug；是否立卡具有不可逆命名后果，仍待用户决定，当前保留`UNKNOWN_LOG_PROJECT`诊断。
- 实际B `CONTRACT_DELTA.md`虽与已提交代码一致，但其合同／回执仍未跟踪，稳定恢复门未闭。
- G0需求矩阵和当前事实刷新尚未作为独立执行任务启动。
- P1a／P1b及P2-P7均未施工、未测试或用户接受。
- 当前有fresh-context只读评论和主控证据对账，但不是组织外部审计、完整异构审或用户接受。

# 下一步

1. 用户补R11来源，或明确只按截图UI参考。
2. 用户决定是否注册`research-desk`项目slug；未拍板前不为消除诊断而立卡。
3. 另领任务执行G0；先刷新三仓、钉实际B合同与开放门，再形成可审阅需求矩阵。
4. 在任何新代码开工前，先完成现有隔离DEMO的5-10分钟真实使用观察。
5. 另行批准后才制作P1a静态验证件；真实阅读证明减负后再决定P1b交互页。
6. P2、P3、P4及WP0原线分别授权，不由本方案自动解锁。

# 可拓展方向

- 将第一垂直切片限定为课题卡→Idea评估→文献调研→论文蓝图。
- 后续根据真实使用再决定章节、图表、审查和正式投稿包是否需要产品化。

# 风险与回滚

- 最大风险是截图驱动出第四套正本、八步自动变绿或用Skill运行代签研究质量；方案以唯一正本和五门向量阻断。
- R11身份未知，只保留截图可见观察；取得来源后再做固定版本核验。
- 任务身份曾错误沿用已作废的004号；已迁移到008，生成视图在专门刷新前可能仍显示旧号，禁止手改生成物。
- 回滚只撤本任务新增文件及本任务在三个路由面的限定hunk，不reset/stash/clean或触碰其他窗口改动。

# 文件和产物

- `progress/decisions/two-desks-delta-20260914/RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md`
- `progress/decisions/two-desks-delta-20260914/_review/20260916_cockpit-review-controller-reconciliation.md`
- `progress/decisions/two-desks-delta-20260914/_review/20260916_fable5-independent-review.md`
- `progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md`
- `progress/decisions/two-desks-delta-20260914/README.md`
- `progress/handoff/2026-09-16__research-copilot-cockpit-plan__handoff.md`
- `progress/handoff/INDEX.md`
- `progress/task_logs/2026/09/2026-09-16__research__research-copilot-reference-integration-plan.md`
- `progress/task_logs/INDEX.md`
