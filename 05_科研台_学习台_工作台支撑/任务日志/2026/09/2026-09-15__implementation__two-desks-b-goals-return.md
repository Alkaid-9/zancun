---
id: TASK-20260915-004
title: 两台首批 B 目标要求与研究学习往返施工
date: 2026-09-15
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 托管会话未提供可确认的有效 effort；交互式分批实施，不运行无人值守任务
  launch: 当前交互式会话
type: implementation
status: completed_with_open_gates
area: research-desk
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/FIRST_BUILD_PLAN.md
  - progress/decisions/two-desks-delta-20260914/B_CONTRACT_PROPOSAL.md
---

# 目标与授权

用户在 A 交付、用户复验仍开放的说明之后明确要求“B启动”。本次采用 B_CONTRACT_PROPOSAL 的窄约定实施 B1／B2，按 FIRST_BUILD_PLAN 的 B-01–10 验收。允许带 A／C03 用户复验开放项推进 B，但不代签 AC03-12，不把本次合成试验等同学习效果验证。总并发最多 2，子代理仅只读检索／核验。

# 开工基线与写域

- 应用独立仓 `/mnt/d/MyResearch/research-desk`，main，HEAD `d53d188faff8e64ae9d22d92dd1eeab1b8309b84`。A 的 app.js／styles.css 与 A 脚本／验收目录是已完成但未提交的前序改动，完整保留；B 差分从本次 before 快照起算。
- 写域：`app/research_service.py`、`app/research_desk.py`、`app/static/app.js`、必要的 styles.css／index.html；B 专用测试与验收资料。优先复用 record_store，不迁移 schema。
- B 界面函数分置 `app/static/b.js`，由 index.html 在 app.js 前加载；仍是原生 JS，不引入框架。app.js 只保留既有工作区的接入点。
- 首轮发现 `_insert_view` 漏存已有 return_context；本批需要在 `record_store.py` 的 JSON 构造中补该字段，无表结构变化／旧库迁移；改前已加入 before 快照。
- 独立根：`acceptance/b-TASK-20260915-004/`，content／data／exports／runtime／logs 分离，只用合成 DEMO；端口候选 127.0.0.1:8878，启动前核空闲。
- MAS 仅本任务、索引本任务行、必要的后续执行路由；不修改真实库、默认配置、registry、课程、答案、sealed、一苇渡江任务或其他窗口改动。不安装依赖、不 commit／push／部署。
- 任务号由 8899 中央 allocator 签发；solver 环境预检通过。

# 当前状态

B1／B2 有界实现完成，`CONTROLLER-TECH-PASS / USER-TRIAL-OPEN / INDEPENDENT-REVIEW-OPEN`。目标三档、共享知识、个人尝试／反馈、研究学习分支往返、独立研究判断及显式版本导出已贯通。不是完整多层网络或课程内容全部建设完成。

# 合同与证据

[集中回执](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/RECEIPT.md)；[实际窄合同](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md)；[复验与试用](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/RUN_CHECKS.md)。

- 最终 B 浏览器 27/27（run-05）；A 回归 38/38（a-regression/run-02）；C03 回归 22/22（c03-final/run-01）。全部独立 DEMO，不继承旧通过数。
- 后端 28/28（原有22＋B6），JS语法／应用diff空白／B scoped patch reverse check通过；源码差分与before快照集中保存。未执行实际撤回。
- 主线程复查修复 v2 旧关系端点版本／草稿引用枚举，并补目标与知识的只读历史入口。旧Feedback未定版本保持未知；未迁移真实库。
- C03 同库二跑因夹具叠加关系而失败；保留现场，使用新合成根完整重跑22/22。失败与处置均在回执的FAILURES链接登记，未改旧断言。
- 只读代理连接中断／429，无独立审查证据。最高并发限制保持，不将主线程自查写成独立复核。
- 两仓HEAD未变、无本轮暂存／commit／push／部署；测试服务已停止，8878收尾无监听。A原有改动保留。

# 尚未完成与下一步

B-01–10主线程功能验收完成。下一步为用户最短路径试用与体验反馈；A／C03 AC03-12、B真实试用、独立复核仍开放。完整C06／多层网络、课程内容、考纲采集、科研实验、真实库接线及部署均未开展，不自动开下一包。

# 风险与回滚

返程恢复的是原身份与阅读上下文，不回滚后来版本；新记录的引用版本固定，个人表现与研究判断独立。未知章目、旧记录未固定版本、缺少原文快照均如实显示。需要新 schema 或超出单次分支往返时先停下单列差异。撤回仅对 B 相对 before 的改动，不删除 A 或真实数据。

## Amendment

- 2026-09-15：恢复注入曾因外层cwd报wrong_repo；读取本会话binding，切到指定MAS仓复验为VERIFIED并重开正本后继续。恢复绑定仍为本任务“目标与授权”。
- 收尾把设计入口从“B未授权”更新为本任务与实际回执；共享索引只改本任务行，保留其他窗口内容与CRLF，不更新无关生成视图。
- INDEX 经既有 ledger CAS 单行写入并回读通过，仍为纯 CRLF；写后核验值 `1e3bdca33c49bff924d48865f495ece0cccd94caec650b012d2a5c6fd81afb12`。该值只用于本次共享登记并发校验，不是源码质量或来源完整性证明；后续他窗写入后应重新读取。
