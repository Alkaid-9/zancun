---
id: TASK-20260917-004
title: 两台全景进展盘点存档 + 两份参考清单交付
date: 2026-09-17
runtime:
  model: Fable 5
  effort: max
  effort_source: 会话内声明（Claude Code 系统提示 model 段）
  launch: Claude Code CLI（用户交互会话）
type: audit
status: done
area: research-desk
project: research-desk
todo_ids: []
owners:
  - user
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
  - research/tracebridge_full_spectrum_20260830/00_control/BRIDGE_TOOL_REFERENCE_CATALOG_20260831.md
  - progress/handoff/2026-09-17__research-copilot-user-trial-save-failure__handoff.md
  - progress/handoff/2026-09-17__research-copilot-cockpit-g0__handoff.md
  - progress/decisions/three-desks-v0.1/README.md
  - progress/decisions/two-desks-delta-20260914/README.md
---

# 目标

用户要求"给我看看实际的全景进展"——对科研台/学习台从三台(09-10)到两台(09-14)的设计演进、代码落地、驾驶舱事件、外部参考清单四条线现状做一次贴磁盘证据的核验汇总，并产出可视化交付物；随后用户追加要求把两份参考清单原文摆出来，本次一并存档。

# 最终结果

已完成核验并交付一份本地 HTML 可视化全景图（`D:\Alkaid\Desktop\两台全景进展_20260917.html`，因会话认证方式（`ANTHROPIC_AUTH_TOKEN`）挡住 claude.ai 登录、Artifact 云端发布失败，改为本地文件交付，内嵌字体与两张 SVG 机制图，离线可看）；随后在对话中原文列出两份参考清单（两台线 13 项 + Bridge 线 24 仓）供用户直接查看，不改动任一原文件。

# 修改内容

- 无任何项目文件被修改（本任务是只读核验 + 新增交付物 + 登记面收尾）。
- 新增：`/tmp/two-desks-panorama.html` → 复制至 `D:\Alkaid\Desktop\两台全景进展_20260917.html`（不在任一 git 仓库内，纯本地交付物）。
- 本 task log 与 `task_logs/INDEX.md` 一行为本次唯一新增登记面写入。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 09-10 四点校正是否回改 | 逐句核对文档原文含校正表述 | PASS | `three-desks-v0.1/WORKBENCH.md`/`README.md`/`LEARNING.md` 原文引用，见上一轮会话子代理核验 + 本轮 mtime 复核（09-11 07:21 后无实质修改） |
| A/B/N3 测试数字是否属实 | 与 `research-desk` 仓 RECEIPT.md 原文 JSON 逐条比对 | PASS | `acceptance/{a-TASK-20260915-002,b-TASK-20260915-004,n3-TASK-20260915-013}/RECEIPT.md`：38/38、28/28、27/27、20/20、22/22 均命中 |
| 驾驶舱 G0 冻结是否触碰应用代码 | 5 个冻结 commit 的 diff 文件列表 | PASS（零触碰） | `git show --stat` 5 个 commit（`7b545c6`/`695e0e3`/`2d7815e`/`e21c7e6`/`c85bba4`）均只改 `two-desks-delta-20260914/**` 与 `progress/handoff|task_logs` 下文档 |
| 驾驶舱试用失败现状 | 与最新 handoff 一致 | PASS | `2026-09-17__research-copilot-user-trial-save-failure__handoff.md`：`USER-TRIAL-RED / SAVE-NOT-REQUESTED / ROOT-CAUSE-OPEN / PAUSED`，服务日志只见 GET |
| Bridge 线×两台线是否重叠 | 24 仓 vs 13 项逐条比对 | PASS（零重叠，上一轮会话已核） | 本轮重读两份原文档确认结论未变 |
| Bridge 线×RE-30(47项) 是否重叠 | — | **未核实**，本轮未新增核查 | 明确标注为开放缺口，不在本次范围内处理 |
| 项目卡挂号 | `PROJECTS.md` 健康检查 | 发现新缺口 | `research-desk` 相关 task log 的 `project` 字段全部报 `UNKNOWN_LOG_PROJECT`（09-15 起至本次共 14+ 条），项目卡注册表未建该卡 |
| 交付物结构自检 | HTML 语法/主题令牌/字体嵌入完整性 | PASS | 本地 Python 脚本核对：section/svg/figure 标签配对、无残留占位符、`:root`/媒体查询/`[data-theme]` 三层令牌齐备、body 背景显式取 token、无 `<!doctype/html/head/body>`（符合 Artifact 片段规范） |

# 当前状态

- 全景交付物已在用户本机桌面（`D:\Alkaid\Desktop\两台全景进展_20260917.html`），未纳入任何仓库版本控制，纯本地查看用途。
- 两份参考清单原文已在对话内完整摘录给用户，原始文件未改动。
- 项目层面事实状态无变化：两台代码仍是 `CONTROLLER-TECH-PASS / USER-TRIAL-OPEN`；驾驶舱仍 `USER-TRIAL-RED`；四条参考清单账本仍互相独立、Bridge×RE-30 仍未核对。

# 尚未完成

- Bridge 线(25仓/24仓统一后)与 RE-30(47项现行权威账本)之间的交集核对——上一轮子代理未完成，本轮未处理，仍是唯一悬空的"未核实"关系。
- R04/R05 两个"OpenScience"身份仍未钉死，阻塞条件是用户提供原始材料来源（链接/视频/转述来源）。
- `research-desk` 项目卡缺口未处理（是否现在建卡，留用户决定）。

# 下一步

1. 用户已表示：从两份参考清单里选一到两个作为"底座"，开始搭建自己的两台架构，并想先讨论架构本身为什么一直不清晰——这是下一轮的主题，本任务不代为拍板选型或出架构方案，只完成本轮盘点存档。
2. 若用户后续要求，可对 Tier A 五个候选（obsidian-NotEMD/LearnGraph/Remit/ai-project-os/open-science）之一做更深的机制拆解，作为架构讨论的输入。

# 可拓展方向

- 是否需要给 Bridge 线×RE-30 单独开一个核对任务。
- 是否需要一份跨四条参考线的统一路由索引（[[external-tool-reference-lists-fragmentation-20260917]] 已建议但未拍板）。

# 风险与回滚

- 无系统状态改动，无回滚需求。唯一新增文件在用户本机桌面，用户可自行删除，不影响任何仓库。

# 文件和产物

- `D:\Alkaid\Desktop\两台全景进展_20260917.html`（本机桌面，非仓库内文件）
- 本 task log

## Amendment

（无）

### 2026-09-17 — 用途讨论续档：两轮生长、个人主线与工业关注

- 记录者：后续 Codex 主线程（系统标识 GPT-6；推理档位未提供）。本附记不追改上述 Fable 窗口 runtime 或历史盘点回执；任务 `done` 仅表示盘点与本次续档完成，不表示架构已通过或施工完成。
- 用户继续明确：以论文长第一轮，学习过程中积累第二轮种子，学完再展开；之后论文成为长期网络中可重激活的节点。网络涵盖知识、问题、团队、领域、跨域方法、成果/代码/评审追踪、失败复盘和个人错题；提高工业界关注权重，同时保留自己的主线及鲁到孙的发展路径。
- 将完整原话、用途解释与开放问题追加至 [用途提案 §7](../../../decisions/2026-09-17__research__two-desks-purpose-redefinition-proposal.md)，并在文件顶部增加恢复指针。文档仍为提案，不覆盖冻结合同。
- 本轮直接核对：09-14 暂定内容版图已要求多层结构与跨层关系；09-11 场景 v0.3 已收窄 `maturity/growth_mode`；WORKBENCH.md 已保留协调内核与独立交付验收职责。因此纠正“菌丝网仅为谱系”“只是一张图多视角”“职责分层就保证仓库不冲突”等过度推论。
- 未开展上游最新代码核验，不宣称 NotEMD/LearnGraph 已满足底座要求；鲁×孙交集矩阵仍按原文的待审草稿使用，未升级为已核研究事实。
- 验收：追加后回读用户原话与状态边界；原 task log 正文保留；INDEX 仅补本行续档与下一步，沿用 `ledger_edit.py` 保持 CRLF 并核对未触及字节。未改 TODO/lines/PENDING 等生成源，无需重新生成视图；未运行软件/科研测试，无代码或实验变化。
- 尚未完成：主线定稿、底座采用方式、多层数据契约和施工安排。下一步以“论文两轮生长”和“工业问题反向进入”两条完整活动检验候选方案。
- 回滚：只撤销本次提案顶部指针、§7、本附记及 INDEX 对应追加说明；不动既有盘点、其他窗口内容或既有验收状态。未 commit/push。
