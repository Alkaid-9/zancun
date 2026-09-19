---
id: TASK-20260915-002
title: 两台首批 A 来源检索与首次保存反馈施工
date: 2026-09-15
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 托管会话未提供可确认的有效 effort；有界交互式实施，不启动无人值守任务
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
---

# 目标与授权

用户明确要求“施工A”。执行 FIRST_BUILD_PLAN 的 A1 来源检索、A2 首次保存反馈及 A-01–09 对应验收；不执行 B，不关闭 C03 用户验收，不修改课程、真实库、registry 或一苇渡江采集任务。总并发最高 2，子代理只读核验。

# 开工基线与写域

- 应用仓 `/mnt/d/MyResearch/research-desk`，main，HEAD `d53d188faff8e64ae9d22d92dd1eeab1b8309b84`，开工工作树干净。
- 预计源码写域：`app/static/app.js`，确需状态样式时修改 `app/static/styles.css`；本批专用浏览器验收放 `app/tests/a_browser_check.py`，沿既有 Playwright，无新测试平台。
- 隔离验收根：`research-desk/acceptance/a-TASK-20260915-002/`；仅构造 DEMO 来源与记录，content／data／exports／runtime／logs 分开。端口候选 127.0.0.1:8877，启动前核空闲；不复用旧验收库。
- 规划仓仅写本任务记录、必要回执路由及共享索引本任务行。中央 allocator 实际签发 TASK-20260915-002；solver 预检通过。未授权 commit／push／部署。

# 当前状态

A 实施和主线程隔离机器验收完成：`A-TECH-PASS / USER-RECHECK-OPEN / INDEPENDENT-REVIEW-NOT-AVAILABLE`。不是两台全包完成；B 未批准、未执行，C03 的 AC03-12 仍开放。源码未暂存／commit／push，测试服务已关闭，未部署。

集中交付：[A 回执、实跑命令、失败修复与试用入口](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/RECEIPT.md)。运行时仅改 app.js、styles.css；新增 A 验收脚本与本任务 DEMO 根，没有服务接口或数据库 schema 差分。

# 验收与证据

- [最终 A 浏览器报告](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/run-07/a-browser-report.json)：38/38，A-01–09，326 个合成登记资产／324 个可选来源，覆盖第 321 项、同名不同集合、工作簿、重复点击、明确拒绝、分阶段重试及写入后丢响应。无真实 registry 扫描。
- [最终 C03 浏览器报告](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/c03-final/evidence/c03-browser-report.json)：22/22，新建隔离 c03-final 数据根，含专题往返、服务重启、桌面／窄屏；不引用旧结果。
- [后端测试实际输出](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/backend-tests.txt)：现有 unittest 22/22；solver 预检、JS 语法、应用 diff 空白检查通过。
- [源码 scoped diff](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/changes.patch)、[新增验收脚本差分](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/a-browser-check.patch)及截图见回执。首轮窄屏溢出、测试回调／端口探针／Playwright 清理问题均记录，不把中间失败报为通过。
- 主线程完成验收。只读代理 `/root/a_source_save_review` stream disconnected，未产出独立证据，不重试派发。总并发不超过 2。

# 尚未完成与下一步

下一步是用户按回执的短路线试用 A，并处置 C03 既有使用反馈。B 仍需单独批准其合同及继续范围；本任务不替用户接受两台全包。来源检索限当前加载的可选登记资产；未落库草稿只保留在当前页面会话，不承诺刷新恢复／跨客户端 exactly-once。

# 风险与回滚

不改默认配置、真实来源、旧数据库；只启动并关闭本任务创建的服务进程。必要撤回仅针对本任务源码差异，不 reset 整仓、不清空验收目录。应用与规划分别报告工作树、提交、运行和用户验收状态。

## Amendment

### 2026-09-15 恢复及收尾

- 压缩后报告 `wrong_repo`；实际绑定仍为本会话 `01a09aa5-24c1-7233-868b-7426b5d94476` → 本任务 → MAS 正本。重读绑定、任务、FIRST_BUILD_PLAN 与两仓 Git 身份；用显式 MAS cwd 校验得到 `CONTEXT_RECOVERY_STATUS=VERIFIED` 后继续。未从外层 `/mnt/d/myresearch` 推断任务或覆盖绑定。
- 应用 HEAD 仍为 `d53d188faff8e64ae9d22d92dd1eeab1b8309b84`，仅本任务运行时两文件和新增脚本／验收资产；index 无暂存。MAS 其他窗口的已改／未跟踪文件均保留。
- A 最终 run-07 及 C03-final 所创建进程均已停止；最终 `ss -ltn '( sport = :8877 )'` 无监听。
- 共享索引仅更新本任务行；使用 ledger_edit 的 CAS／原生 CRLF 保形写法。读前值 `f8e76a1c3da8c4684177c557b0a9930a5b417b7360998dfab284883126602139`；写后 `e44b9e5ad2174d56f887c80cf7abaa362f23b261d5001a9254bea0b10075bbde`，`VERIFY-OK`，再次 `--check` 值相同、299 行均为 CRLF。没有覆盖本轮期间新增的其他任务。
