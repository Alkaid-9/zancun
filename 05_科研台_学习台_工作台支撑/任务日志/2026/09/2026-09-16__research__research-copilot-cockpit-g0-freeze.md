---
id: TASK-20260916-009
title: 科研驾驶舱G0当前事实与语义冻结
date: 2026-09-16
type: research
status: completed_with_open_gates
area: research-desk / workbench-v2 / reference-integration
project: research-desk
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md
  - progress/handoff/2026-09-16__research-copilot-cockpit-plan__handoff.md
---

# 授权与边界

用户授权：“直接做，一个阶段一个阶段commit”。本任务先提交已验收的TASK-008设计基线，再只执行方案G0：刷新三仓事实、钉实际B合同、建立需求与权威矩阵、冻结跨仓新鲜度和非原子读取语义。

默认决策按上一轮提案执行：R11维持`IDENTITY-OPEN / SCREENSHOT-ONLY`；暂不注册永久`research-desk` slug。G0不修改应用代码、真实数据库、Skills、WP0隔离树、课程、sealed、答案或生成视图，不启动P1a／P1b或P2-P7。

# 阶段

1. `S0`：TASK-008设计基线限定commit。
2. `G0-A`：MAS、research-desk、WP0身份、工作树、服务与开放门刷新。
3. `G0-B`：实际B合同、当前实现／测试及恢复载体对账。
4. `G0-C`：截图需求→用户动作→对象→正本→消费者→门矩阵。
5. `G0-D`：跨仓新鲜度、非原子读取、失败显示和停止条件冻结。
6. `G0-E`：主控验收、独立只读复核、恢复入口和限定commit。

# 当前状态

`S0 COMMITTED / G0 COMPLETE_WITH_OPEN_GATES / SCOPED-READONLY-PASS`。任何产品施工和新的运行试用仍未开始。

- `S0`：TASK-008设计基线已限定提交为`c85bba4401b616ced1ed33ad965abc2a7fba20e1`；9个归属路径，未夹带R12或TASK-009。
- `G0-A`：三仓身份、index/worktree、8899／8878／8873服务观察和开放门已写入[当前冻结件](../../../decisions/two-desks-delta-20260914/RESEARCH_COPILOT_G0_FREEZE.md)。结论只到事实快照，不宣称WP0加载、用户接受或独立审关闭。
- `G0-B`：实际B合同哈希与未跟踪状态、应用`b54ea71→c86f6d1→0b3a541`提交链、旧patch当前reverse-check失败原因和恢复载体已对账。当前限定单测6/6通过；历史浏览器／回归数未冒充本轮重跑。首次错误unittest模块入口触发第三方`app.py`导入失败，改用既有discover入口后通过；未改依赖。
- `G0-C`：R11项目台、证据、路线、Idea、文献、蓝图、章节、图表、审查、导出、Skills、Codex入口和顶部计数已逐项映射到用户动作、现有对象、唯一正本、消费者、状态及进入／退出门。`EXISTING/PARTIAL/DESIGN-ONLY/MISSING/UNKNOWN/N-A`口径冻结，未把Skill名称或文件存在升级为产品能力。
- `G0-D`：来源戳、构建前后双读、`CURRENT/STALE/NON-ATOMIC/UNKNOWN/ERROR/N-A`、失败显示、硬停止和重建规则已冻结。时间阈值不单独决定新鲜度；R12增量水位线只作后续参考，本阶段未新增同步服务。
- 阶段提交链：G0-A=`7b545c6`，G0-B=`695e0e3`，G0-C=`2d7815e`，G0-D=`e21c7e6`。G0-E整改以`e21c7e6`为base_commit，最终身份由本阶段限定commit固定；不是仍停在S0的`c85bba4`。
- `G0-E`独立只读首轮复核返回1 BLOCKER、6 MUST-FIX、1 LIMITED；主要问题为来源戳未覆盖消费字节、N-A与MISSING混用、运行状态单值化、矩阵复合状态、测试／服务证据坐标不足、证据脊柱开放项未裁决及R11顺序表述。当前正在整改，未签G0完成。

第四轮复核最终为`SCOPED-READONLY PASS`：前三轮发现已全部处置，无剩余BLOCKER／MUST-FIX／新增LIMITED。该复核不等于异构审、外部审、运行验收或用户接受。G0主控验收、开放门裁决和恢复入口已收口；产品施工、真实用户试用、合同／历史证据采收、WP0原门和push均未执行。

# 验收、回滚与下一步

- 验收：G0-A至G0-E各阶段分别形成限定commit；当前事实、B合同、权威矩阵、A/C/B内容身份协议、失败语义、开放项和四轮复核可从冻结件及回执复查。
- 回滚：仅撤对应阶段文档commit；不reset、stash、clean，不删除应用验收现场、数据库、用户产物或他窗修改。
- 下一步：先按现有隔离DEMO做一次5-10分钟真实用户路径观察。只有用户另行授权后才启动P1a；P1b及P2-P7继续关闭。
- 恢复入口：[2026-09-17 G0交接](../../../handoff/2026-09-17__research-copilot-cockpit-g0__handoff.md)。

# 收口后用户试用观察

2026-09-17用户首次尝试8878隔离DEMO后反馈“没有保存”。定向检查确认当时服务日志只有GET、没有POST／PUT；数据库文件存在不能证明本次输入已写入。当前结论为`USER-TRIAL-RED / SAVE-NOT-REQUESTED / ROOT-CAUSE-OPEN`，根因可能位于页面路径、按钮／前端状态、浏览器请求或交互理解，尚未复现，不归责用户也不虚报后端失败。已写[专项交接](../../../handoff/2026-09-17__research-copilot-user-trial-save-failure__handoff.md)；P1a继续关闭，下一步先取得失败页面／按钮／提示／截图并复现精确路径。

2026-09-17用户追加 `marikagura/agent-stack-notes` 并要求纳入参考清单。已按固定远端 HEAD `e17d0a8edff0b01d340c385d936b5ecaca5e8178` 登记为R12，证据范围限于README和三篇教程的只读方法评估；未运行关联实现、未审完整文献地图、未判定采用。该增量只写工作树，未混入当前暂存的TASK-008设计基线。
