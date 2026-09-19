---
id: TASK-20260917-001
title: 进组包拓展执行总合同与W0事实权限冻结
date: 2026-09-17
type: research
status: in_progress
area: jinzu / research-infrastructure / three-desks
project: jinzu-sprint
owners:
  - Codex controller
related:
  - progress/decisions/2026-09-17__research__jinzu-extension-master-execution-contract.md
  - progress/decisions/2026-09-17__research__jinzu-extension-wave0-receipt.md
---

# 授权与目标

用户授权“现在写，写了就直接开始执行”。本任务把进组包的研究方法论拓展统一为 W0-W7 总合同，并立即执行 W0；不把合同、静态资产、技术通过、用户接受和持续运行混为一谈。

# 已执行

1. 重新绑定接入审计、RD-2施工／验收、驾驶舱方案、执行计划、TASK-009并发边界、OE-1最新交接及TASK-017试用入口。
2. 核对 MAS、research-desk、WP0 隔离树身份、HEAD、工作树与现有 staged 集合。
3. 核对 TASK-017 服务：127.0.0.1:8878、PID 8705、HTTP 200；未重启服务。
4. 只读核对试用 SQLite：objects/views/object_revisions/view_revisions 均为0，维持 `USER-ACTION-OPEN`。
5. 写入总合同和 W0 回执，冻结 R01-R10、W0-W7、验收、写域、停止条件及发布门。

# 当前状态

`W0-CONTROLLER-COMPLETE / AC-W0-01..08-PASSED / USER-ACTION-OPEN / W1-READY`。

本任务继续保持 `in_progress`：W0 的登记与最终复验完成后，下一执行游标是 W1 有界九月刷新；W2-W7 仍按合同门禁，不因总合同存在而自动启动。

# W1增量

1. 冻结2026-08-15至09-17的三路范围、证据等级、来源政策、写域和AC-W1-01..07。
2. 以总并发4执行IND-1、RS-A、RS-B三路只读调查；IND-1与RS-B complete，RS-A partial。
3. 主控抽查工业官方文档及MHP／AgentLTL两条新增引用，归档三路报告和合成页。
4. 工业动机句修正为`partial`；确认两条严格九月新增引用和多项此前漏扫邻居；未升级为“全球没有”或“新颖性已证明”。
5. 因RS-A缺逐项URL矩阵、bridge余项和BPM/ICPM完整接收面，W1保持partial，SURVEY_LEDGER／CHANGELOG未提前更新。
6. W1执行期间其他窗口将MAS HEAD从`306cc2b`推进到`e21c7e6`并清空原暂存集合；本窗口未执行add/reset/commit。TASK-001文件与INDEX已在新HEAD下复读，跨时段仓库快照标`NON-ATOMIC`。

当前游标：`W0-COMPLETE / W1-PARTIAL / RS-A-RECOVERY-NEXT / USER-ACTION-OPEN / W2-W7-GATED`。

# 边界

- 未修改 TASK-009 文件、现有 staged 集合、应用代码、真实数据库、课程作答、sealed、TODO/PENDING或生成视图。
- 未执行 commit、采收、加载、部署、push、邮件发送、订阅或其他外部动作。
- 用户试用、个人证据、邮件个人字段和研究采用只能由用户完成或确认。
