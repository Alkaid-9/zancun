---
id: TASK-20260912-002
title: v0.3 与 Astra v0.1 场景稿比较就绪度评估
date: 2026-09-12
runtime:
  model: Fable 5
  effort: max
  effort_source: 会话内 /model 设定
  launch: Claude Code CLI
type: research
status: design_only
area: research-desk
project: none
todo_ids: [RD-2]
owners:
  - user
  - fable
related:
  - progress/decisions/2026-09-12__research__knowledge-network-v0.3-vs-astra-comparison-readiness.md
  - progress/decisions/2026-09-11__research__knowledge-network-architecture-v0.3-scenarios.md
  - progress/decisions/2026-09-11__research__knowledge-network-scenarios-astra-v0.1.md
---

# 目标与最终结果

用户问"这两条其实还没想好怎么严格应用，你觉得呢？目前你觉得能写这一稿了吗"，指向两件事：(a) v0.3 与 Astra v0.1 的比较稿是否就绪，(b) 失败数据分类规则是否就绪。已重读两份场景稿原文（非按摘要转述）给出差异化判断，并落盘评估稿；(b) 由用户"感觉有一个纠错本之后才好做这种分类"的判断解决，已在同日 [TASK-20260912-001](2026-09-12__learning__correction-notebooks-and-growth.md) 落盘，本任务不重复。

# 修改内容

- 新建[比较就绪度评估稿](../../../decisions/2026-09-12__research__knowledge-network-v0.3-vs-astra-comparison-readiness.md)：核对 Astra §7 九问逐条原文，确认六到七条已有独立收敛的共同结论（点名三条证据最扎实：SourceRef 网页锚点缺口、指导库需正式关系而非标签、暂不新造 Event 平台），两到三条仍是真实分歧（轻量观察是否拆类型、v0.3 场景A 比 Astra 场景A 单薄且未做反转测试、两稿反例检验严谨度不对等）。
- 明确指出第7节完整比较表现在写会等于替用户在未冻结方案间拍板，非比较本身，故不代为拍板，只交出评估结果与选项。
- 任务号中央领取：TASK-20260912-002（`POST /api/next-task-id` 返回，此前一次因端点 404 触发过 curl 重试，第二次请求成功）。

# 验收与证据

| 项目 | 标准与结果 |
|---|---|
| 引用可溯 | 每条判断均标注取自哪份稿的哪一节原文，非转述摘要 |
| 不越权拍板 | 明确列出仍需用户裁定的选项，未替用户选定第7节最终版本 |
| 与纠错本任务的关系 | §4 显式关联 TASK-20260912-001，指出两处判断结构相同（轻量观察拆分与失败分类都要等真实案例），不重复展开 |

# 当前状态、尚未完成与下一步

第7节完整比较表未写，等用户对 §2 三点分歧裁定顺序（先补 v0.3 场景A 反转测试，还是先接受"轻量观察暂缓拆分类型"继续挂起）。CROSSWINDOW.md 跨窗登记仍是未偿debt，本任务未处理。

# 风险、回滚与拓展

未改 CONTRACTS.md/DATA_CONTRACT.md、未改 C00-C03 代码、未commit/push。撤回只需删除本任务稿与对应登记行，不影响其他窗口内容。
