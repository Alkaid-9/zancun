---
id: TASK-20260918-004
title: 工作台/科研台/考研插件参考机制层深查（R15，26项URL）
date: 2026-09-18
runtime:
  model: Fable 5[1M]
  effort: max
  effort_source: ~/.claude/settings.json effortLevel=xhigh
  launch: Claude Code 交互会话
type: research
status: done
area: research-desk / workbench / kaoyan-candidate
project: research-desk
todo_ids: []
owners:
  - user
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
  - progress/decisions/two-desks-delta-20260914/REFERENCE_INTEGRATION_PLAN.md
  - progress/task_logs/2026/09/2026-09-18__archive__workbench-research-desk-plugin-reference-batch.md
  - progress/audits/2026/09/2026-09-11__kaoyan-deep-review/REPORT.md
  - progress/decisions/2026-09-17__research__two-desks-purpose-redefinition-proposal.md
---

# 目标

`TASK-20260918-002`（R13/R14）只做了"按名称核身份"层级的调研。用户随后要求：①把两个新增考研链接（Pkmer-Math、Math-And-English-Library）与 R14 的 Lazy-Kaoyan-Library、R13 的 obsidian_math、已独立深查的 `virtualxiaoman/kaoyan` 放一起比较；②对 R13/R14 全部项目升级到"机制层"（核心内容/工作流/能不能用得上），不预设槽位归类；③同时提出一个全新的、未拍板的架构问题——是否要新增"考研台"。用户明确要求先出计划、确认范围产出验收标准后再执行（"先给我确认一下范围、产出预期产物、各项标准、验收标准""先别发直接开始"），方案经一轮自我批判后由用户拍板"没有了，改一下计划然后直接跑"。

本任务边界：只做"定位→机制"两档只读调研（对齐 `REFERENCE_INTEGRATION_PLAN.md` §2.2），不做"实现/实测"深度，不做处置判断（借鉴/转化设计/隔离试用/正式接入/暂存不采用五选一），不判断是否新增"考研台"。

# 最终结果

6 个 `general-purpose` 子代理并行核查了 26 个 GitHub URL（R13 全部 11 项 + R14 非重复 13 项 + 新增 2 项，已核对无遗漏无重复计数），全部在派发的 5 caps 约束内按时足量交付，无超时缺项、无"读不到"字段。结果已整合进 `REFERENCE_NOTES_20260915.md` 新增 §7.9（含 §7.9.1–7.9.7 七个子节），§0 总表新增 R15 一行。

关键发现：Lazy-Kaoyan-Library 明确声明"灵感来源于 Math-And-English-Library 和 Pkmer-Math"，且自带一套"AI+OCR转录→思维导图+AI对话→Dataview+Templater模版驱动"的三段式工作流；这套工作流是它在两个"血缘对象"基础上自己另加的（后两者本身都是纯静态笔记，没有任何工作流），与已深查的 `virtualxiaoman/kaoyan` 三段式（人工记录+Python统计+外部AI批改）目标相似但实现路径完全独立，双方互不知晓/互不借鉴，可视为同一问题的两种收敛解法。

# 修改内容

- `REFERENCE_NOTES_20260915.md` §0：编号统计从 15 项更新为 16 项，新增 R15 一行。
- 同文件新增 §7.9（R15 机制层深查，含 7 个子节：考研对比组含 5 项对比表 + vault模板/任务管理/仪表盘/嵌入绘图/科研AI-agent 五个技术分组表 + 边界与未决）。
- 本 task log 与 INDEX.md/TODO.md 对应行（见 Amendment）。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 不新开平行清单 | 追加进已有 R01-R14 正本而非新建文件 | 通过 | 仅 Edit 了 `REFERENCE_NOTES_20260915.md`，未 Write 新文件 |
| 6 批子代理均遵守 5 caps | URL/字数/时间/工具/done_when 全部显式给出且被遵守 | 通过 | 逐一核对 transcript 中 6 个 Agent 调用的 prompt 全文；6 批全部在 12 分钟 time cap 内交付，无超时、无"读不到"字段 |
| 整合内容与子代理原始输出一致，非转述失真 | 逐字段比对 | 通过 | 从 session transcript（`18294e79-...jsonl`）按 `tool_use_id` 精确提取 6 批最终 `teammate-message`（非 idle_notification）原始文本，与写入 §7.9 的表格逐项核对一致 |
| 不做处置判断、不代拍"考研台"问题 | §7.9 正文与 §7.9.7 明确声明边界 | 通过 | §7.9.7 第 3、4 条 |
| 考研对比组含 kaoyan 引用不重查 | 不重新读取已深查的 kaoyan | 通过 | §7.9.1 表格 kaoyan 行标注"引用 `TASK-20260911-007`，不重读" |
| 26 个 URL 与既有 R13/R14 重叠核对 | 用集合比对确认无遗漏无重复计数 | 通过 | `comm` 命令核对：26 项中 24 项已在 R13/R14 出现，2 项（Pkmer-Math/Math-And-English-Library）为真正新增 |
| 共享登记面用 ledger_edit.py 保形写入 | TODO.md/INDEX.md 不整文件重写 | 通过 | 见下方 Amendment |
| 铁律8：用户单发内容必列 TODO（含"是否新增考研台"架构问题） | 在 TODO.md 单独一行挂项 | 通过 | 见下方 Amendment |
| 文件编码完整性 | 无替换字符（U+FFFD）等复制粘贴损坏 | 通过（发现后修复） | 写入后发现 7 处 U+FFFD，逐一定位并对照原始 batch 素材修复，复验 0 残留 |

# 当前状态

`REFERENCE_NOTES_20260915.md` 现含 R01-R15 + I01 共 16 项外部参考登记，仍是 `ARCHIVED / REFERENCE-ONLY / NO-ADOPTION-OR-RUN-AUTHORIZATION`——本次只做机制层调研，未安装任何插件、未选型、未修改 NotEMD/LearnGraph 试用范围、未对是否新增"考研台"这一架构问题做任何裁定。

# 尚未完成

- 26 项均未进入"实现/实测"深度（未读源码、未装、未跑），若后续要真实试用需另立任务并固定版本号。
- "能不能用得上"栏是并列候选池，未做互斥优先级排序或五选一处置判断，等用户或后续任务决定。
- "是否新增考研台"仍是完全开放的架构问题，本任务不代为拍板，只在 TODO 挂项登记。
- R13 中提到的多个同名/相邻仓（Research OS 系、Editing Toolbar 双仓、Apex Dashboard 双仓等）的血缘关系仍未核实，本次沿用 R13 阶段的"未核实项"边界，未新增核实动作。
- `two-desks-purpose-redefinition-proposal.md`（09-17，槽位重定义提案）尚待用户拍板；本次 §7.9 的"能不能用得上"字段刻意不套用该提案的四槽位框架，两份文档目前是平行未合流状态，若提案获批，可能需要回头用新槽位框架重新读一遍本次 26 项的"能用得上"字段。

# 下一步

1. 用户如果要对"是否新增考研台"拍板，可直接参照 §7.9.1 的考研对比表和"值得点出的发现"段做决策输入，不需要重新调研。
2. 若确认新增考研台或对某几项做真实试用，参照 `REFERENCE_INTEGRATION_PLAN.md` §2.2 升级到"实现"层（固定版本号、只读源码核对，不批量安装）。
3. 若 `two-desks-purpose-redefinition-proposal.md` 获批，需要重新审视本次"能不能用得上"字段是否需要按新槽位框架重新组织（不是重新调研，是重新归类既有事实）。

# 可拓展方向

- 本次"5 caps"派发协议（在此前"4 caps"基础上新增 tool cap）在 6 批全部无超时无失败的情况下验证有效，可作为后续同类"读 README 做机制层分类"任务的默认派发模板。
- §7.9.1 考研对比组的四维对比表格式（内容定位/血缘痕迹/三段式工作流/版权来源）可复用于未来出现的同类"多个相似定位项目需要横向比较"场景。

# 风险与回滚

仅追加内容到既有 decisions 文档 + 新增一份 task log + 两条共享登记面行；未删除任何既有内容。回滚：`git diff` 定位本次追加的 §7.9 与 §0 R15 行变更，可整体 revert 该文件的本次 diff hunk；INDEX.md/TODO.md 新增行可用 `ledger_edit.py --replace` 单行撤回。

# 文件和产物

- `progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md`（本次编辑，新增 §7.9 + §0 R15 行）
- 本文件
- `progress/task_logs/INDEX.md`（新增一行，见 Amendment）
- `progress/TODO.md`（新增两行，见 Amendment）

## Amendment

### 2026-09-18 — 收尾回执

- `progress/task_logs/INDEX.md`：`ledger_edit.py --insert-after` 在 `TASK-20260918-002` 行后插入本任务行，CAS 前置哈希 `3e1996f0041a945cabb35306dc275f9b2b91f553bbe449a3933b7984e28b9a7f`，写入回读 VERIFY-OK，落盘后复验哈希 `a35479b654acc40f1606a5a047b11094ecc059e94ce3e78032ec76977e1d10fa`，纯 CRLF 330 行（较写入前 329 行 +1，符合预期）。
- `progress/TODO.md` 分两次写入：
  1. `--insert-before "RD-1 · 科研台导航首版与后续解耦建设"` 插入 `RD-4`（本任务调研结果登记），CAS 前置哈希 `75a1d1facfd3fdc3d8f27ca2c767a829e3b5a7b326891b9eb585002d8f5f01b8`，写入回读 VERIFY-OK，落盘后复验哈希 `7524bb7520ad964849d633bb48efcb4a9d91316b6604781f78fd131d82fc423a`，纯 LF 835 行（较写入前 834 行 +1）。
  2. `--insert-after "RD-4 · 工作台/科研台/考研插件参考机制层深查"` 插入 `RD-5`（"是否新增考研台"架构问题，遵循铁律8单独挂项，不代为拍板），CAS 前置哈希取上一步复验结果 `7524bb7520ad964849d633bb48efcb4a9d91316b6604781f78fd131d82fc423a`，写入回读 VERIFY-OK，落盘后复验哈希 `b065cecd8ca434974d733300965f67bb6010ed2236bfca98113791498b0320cc`，纯 LF 836 行（较写入前 835 行 +1）。
- 三次写入均未触发行尾混杂拒绝，未使用 `--normalize`，说明未与其他窗口的并发写产生冲突；每次写入前均先 `--check` 核对 CAS 前置哈希与预期一致才执行。
- `REFERENCE_NOTES_20260915.md` 与本 task log 在首次落盘后各发现复制粘贴混入的 U+FFFD 替换字符（前者 7 处、后者 9 处），均已逐一定位并对照原始子代理输出素材修复；本 task log 撰写本条 Amendment 时又混入 2 处新的 U+FFFD（同类复制粘贴问题），一并修复。两份文件当前复验均为 0 残留，最终写盘状态干净，但过程本身说明复制长段中文文本进 Edit/Write 参数时该问题会反复出现，后续同类操作宜写完即用 `content.count(chr(0xFFFD))` 复查一遍。
- `git status --short` 在写入前确认 `progress/TODO.md`、`progress/task_logs/INDEX.md` 均已是他窗口遗留的 `M`（此前累计的多窗口未提交积压，非本任务引入）；本次追加内容前未 reset 或覆盖既有改动，只在原有基础上单行插入。本次未 commit、未 push。
