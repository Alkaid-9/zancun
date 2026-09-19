---
id: TASK-20260911-003
title: RD-2 C03用户体验返修
date: 2026-09-11
runtime:
  model: Codex
  effort: UNKNOWN
  effort_source: hosted session; no SKU evidence
  launch: Codex shared workspace
type: research
status: completed_with_open_gates
area: research-desk
project: research-desk
todo_ids: []
owners:
  - codex-controller
related:
  - progress/decisions/rd2-construction-v0.3/ACCEPTANCE.md
  - progress/decisions/rd2-construction-v0.3/sol-delivery/20260911-sol-c03-113925/CONTROLLER_REVIEW.md
---

# 目标

根据用户对C00–C03干净沙箱的实际体验，仅返修C03的三个阻断问题：非工作簿来源显示undefined与永久加载、专题内任意成员之间的新关系返回专题后不可见、同端点正式边和待确认边标签重叠。保持`CONTROLLER-ACCEPTED / USER-ACCEPTANCE-OPEN`，不关闭AC03-12，不启动C04–C07。

# 最终结果

限定返修1–3已完成并通过控制器复验。AC03-04与AC03-10从用户报告的失败状态修到`CONTROLLER-REPAIR-PASS / USER-RECHECK-OPEN`；AC03-12继续开放。问题4（2432资产截断下拉无检索）和问题5（保存期间缺少提交态与明确回执，可重复提交）登记为范围外开放项。

# 修改内容

- `app/static/app.js`：区分registered_asset与工作簿来源，终止非工作簿水合状态；Topic图平行边分通道，以编号标记配合图外图例，并增加edge id。
- `app/research_service.py`：Topic中心图纳入关联工作区成员及其关系。
- `app/tests/test_research_records.py`与`c03_browser_check.py`：增加任意成员关系回流、来源终态和平行标签断言。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 非工作簿来源 | 不出现undefined或永久“正在读取原段” | passed | 用户复现快照与8873在线只读复验 |
| 专题任意成员关系 | 新记录连接专题内任意节点，返回专题后记录与正式关系可见 | passed | 新空根22/22与用户关系`obj_4032...`回流 |
| 平行边标签 | 同端点正式/待确认边及标签不重叠 | passed | Method标签框实测分离；桌面与390px通过 |
| 完整回归 | 后端、链接与C03路径通过 | passed | unittest 22/22；check-links 2432/0/0；C03 Playwright 22/22；8873只读在线烟测8/8 |
| 用户验收状态 | 保持USER-ACCEPTANCE-OPEN | passed | 返修回执；未代签AC03-12 |

# 当前状态

原`user-acceptance`数据库保留用户复现现场；返修测试只写新的隔离数据根。127.0.0.1:8873已加载修复后代码并继续使用原验收数据库，返回200。

# 尚未完成

- 用户复验问题1–3并决定是否关闭对应体验问题。
- 问题4–5仍需独立C03返修范围与验收。

# 下一步

1. 用户从当前8873重复`Topic→来源→工作区→任意成员关系→返回Topic`，确认体验结果。

# 可拓展方向

- C03后继可单独处理来源检索和保存提交态，不能夹带进入本次问题1–3补丁。

# 风险与回滚

- 不覆盖用户复现数据库；源码回滚使用本任务`before/`快照和差异补丁。

# 文件和产物

- `/mnt/d/MyResearch/research-desk/acceptance/c03-repair-20260911-task003/`
- `progress/decisions/rd2-construction-v0.3/c03-repair/TASK-20260911-003/RECEIPT.md`
