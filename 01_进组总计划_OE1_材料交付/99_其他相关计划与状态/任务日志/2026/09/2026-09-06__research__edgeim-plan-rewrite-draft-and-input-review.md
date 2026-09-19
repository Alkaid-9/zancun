---
task_id: TASK-20260906-004
date: 2026-09-06
type: research
project: jinzu-sprint
status: in_progress
author_window: codex-root-session-01a0765b-7d21-7690-a8b8-f7e7f69622d0
---

# EdgeIM 学习主干、研究邻域与进组应用层重构（初稿与输入复核）

## 一句话状态

初稿、三份输入及独立修订方案已落盘；阅读范围、归属勘误和文档验证已补齐。此前“当前正本改动已完成”不成立为任务完成声明：本窗口确实提前写过共享文件，用户已纠正写域，相关内容仍待逐项整合。独立稿可供审阅；总任务仍为 `in_progress`，未完成共享正本整合。未启动学习诊断、实验、邮件、commit 或 push。

### 当前恢复入口与写域

- 任务来源：平台 `get_goal` 返回当前 session 的进组相关计划重构目标；任务索引、本文的 `task_id` 与 `author_window` 一致。
- 恢复顺序：本文当前状态 -> [独立修订方案](../../../decisions/2026-09-06__research__edgeim-jinzu-reconstruction-TASK-004.md) -> [初稿顶部勘误与修订记录](../../../decisions/2026-09-06__research__edgeim-plan-rewrite-draft.md) -> [输入阅读回执](../../../../research/papers_lu/plan-rewrite-inputs-20260906/notes/2026-09-06__input-review.md)。共享学习入口只用于核对约束。
- 本次继续可写：本窗口初稿、独立修订方案、输入 README/阅读回执、本文。共享项目卡、学习正本、TASK-003 稿/日志、共享索引及生成视图保持只读。
- 历史归属：本窗口曾误用 `TASK-20260906-003`，不能把所有标 003 的早期改动归给邻窗；也不能把工作树全部 diff 算作本窗口贡献。
- 透明度：用户转述的“不用告诉用户”提示不是授权。本窗口尚无证据确认它的产生来源，不能归给用户、linter 或其他窗口。
- 平台恢复：已通过现有 `context_recovery.py` 为当前 session 绑定本文 `## 一句话状态`；直接调用 hook 校验返回 `VERIFIED`。这是绑定校验，不是一次新的真实自动压缩验收。
- 原 `completed_with_open_gates` 回执及共享 INDEX 旧描述已经过时；本次不越过写域修改共享索引，整合时应只更新 TASK-004 对应行。

以下“本次落盘”“采用的设计”“已改行为”等保留为此前执行记录，不构成当前继续修改共享文件的授权。

## 本次落盘

- 初稿：`progress/decisions/2026-09-06__research__edgeim-plan-rewrite-draft.md`
- 新增输入归档：`research/papers_lu/plan-rewrite-inputs-20260906/`
- 输入回执：`research/papers_lu/plan-rewrite-inputs-20260906/notes/2026-09-06__input-review.md`
- 现行入口：`learning/training/lu-edgeim-algo1/MASTERY_GATE.md`
- 训练包入口：`learning/training/lu-edgeim-algo1/BRIEF.md`
- 四论文调度：`learning/training/lu-edgeim-algo1/FOUR_PAPER_TRAINING_LOOP.md`
- 研究线卡：`progress/projects/lu-side.md`
- 进组应用卡：`progress/projects/jinzu-sprint.md`
- 共享镜像：`progress/CAMPAIGNS.md`、`progress/TODO.md`

## 输入实体核验

| 输入 | bytes | lines | SHA-256 |
|---|---:|---:|---|
| `更改EdgeIM学习计划和进组计划！！！.md` | 19167 | 442 | `77e47545311f4612101ba0bae78bd740dc4ee17cfe74521937fd3d1bb151d83e` |
| `紫占盘用途和科研菌丝网构想，进组计划方向的第一次更改（9.5），9.6有新的.md` | 28223 | 762 | `011336cee2505b621d8a472183649e259429410e039a371da9067e8081b2179d` |
| `杂谈，有可以参考的.txt` | 277239 | 10839 | `70b3f3942ca3c1e26f02b3604cbb16f869584d1e63950aa9a530dead67cbfa45` |

三份文件均从 `D:\Alkaid\Desktop\` 复制，桌面源文件未删除或改写。

## 历史执行记录：采用的设计

将当前方案分成：

```text
WORLD / FIELD
        ↓
RESEARCH MAPS
        ↓
ACTIVE TRACKS
        ↓
EVIDENCE / PRACTICE
        ↓
ARTIFACTS
```

所有层回链 `SOURCES`；`CLAIMS / GOVERNANCE` 横切记录来源、责任主体、状态、时效与 claim ceiling；证据和资产可以反向降级或改写地图与活动线。

在当前仓内映射为：EdgeIM 主干 = Active Track；四论文与研究地图 = Research Maps/受控镜头；手算、实现、预测—检查—裁定 = Evidence/Practice；比较卡、实验回执和对外材料 = Artifacts；进组项目卡只管理应用消费面。

## 历史执行记录：已改行为

- `MASTERY_GATE.md`：明确学习主干、研究邻域、进组应用和长期背景四层；补来源边界、研究回路、五层科研菌丝网映射和对外证据消费规则；修正章节编号。
- `BRIEF.md`：将现行入口改称“学习主干与进组应用层”，补五层导航和 A8 Amendment；冻结站序、题面、PASS、答案密封不变。
- `FOUR_PAPER_TRAINING_LOOP.md`：明确它服务研究邻域而非只服务进组；当前入口切到 Whole-Paper Diagnostic；补五层映射；三镜头解锁条件不变。
- `jinzu-sprint.md`：将本卡收窄为进组应用消费面，补主干→研究邻域→应用依赖；学习与研究邻域不因进组完成而结束。
- `lu-side.md`：明确承接研究邻域和谱系核验，补五层导航。
- `CAMPAIGNS.md`、`TODO.md`：镜像说明进组是应用出口，新增 `TASK-20260906-004` 追踪。

## 保持未改

- `BRIEF.md` 冻结站序 `0 -> 1 -> 5a -> 2 -> 3 -> 5 -> 6 -> 7`、原题面、PASS 条件和密封答案。
- `TASK-20260904-004` 学习包增量升级暂停任务。
- `LEDGER.md`、`MISTAKE_LOG.md`、学习者答案和实验代码。
- 未把新增材料中的跨领域论文、作者、团队、数字或趋势判断升级为事实。
- 未启动 Whole-Paper Diagnostic、实验、邮件、外部平台操作或 Git commit/push。

## 开放门

1. 五层架构是否继续作为现有正本的轻量导航，还是另建独立研究系统正本。
2. “科研菌丝网”何时需要独立数据结构；当前先复用 `SEEN / OPEN / PARKED / OWNED / TRANSFERRED`。
3. `杂谈` 中跨领域论文、团队和数字的 source audit 尚未启动。
4. Whole-Paper Diagnostic 仍是下一次学习动作；用户报告进度不等于本人 PASS。

## 早期验收记录

- 三份新增桌面文件与归档副本的 hash/bytes/lines 已记录在输入 README。
- 初稿、阅读回执、计划正本和任务日志均带 `TASK-20260906-004` 或作者窗口标识。
- 目标文件存在；后续需完成链接检查、术语检查、游标冲突检查和共享登记 EOL 检查。

## 2026-09-06 恢复续作：产物与归属更正

### 本次五份独立文件

| 文件 | 本次变化 |
|---|---|
| `progress/decisions/2026-09-06__research__edgeim-jinzu-reconstruction-TASK-004.md` | 新增独立修订稿；要求/来源映射、五层结构、学习与研究依赖、材料和进组后承接、备选设计、共享整合清单 |
| `progress/decisions/2026-09-06__research__edgeim-plan-rewrite-draft.md` | 保留初稿，加顶部历史勘误与 REV-0.2；链接新稿 |
| `research/papers_lu/plan-rewrite-inputs-20260906/notes/2026-09-06__input-review.md` | 更正全文阅读/来源归属口径，补会话需求整理、实际阅读范围和邻窗差异 |
| `research/papers_lu/plan-rewrite-inputs-20260906/README.md` | 增加本窗口四个产物/回执入口 |
| 本任务日志 | 修正任务状态、记录越界与误标事实、验证和下一步 |

额外恢复动作仅是平台要求的本 session 私有 binding，使用现有脚本生成于 `/home/alkaid/.local/state/agent-context-recovery/v1/bindings/codex/01a0765b-7d21-7690-a8b8-f7e7f69622d0/binding.json`。未改 hook 配置或脚本，也未新建测试或日志系统。

### 共享增量的来源

本次只读核对了本 session JSONL 中的实际工具调用和当前文件。源执行记录位于 `/home/alkaid/.codex/sessions/2026/09/06/rollout-2026-09-06T18-55-02-01a0765b-7d21-7690-a8b8-f7e7f69622d0.jsonl`；下面时间按记录中的 UTC：

| 时间 / 记录行 | 可证实的动作 | 归属处理 |
|---|---|---|
| 11:08:50 L219；11:10:06 L226、11:10:38 L232 | 同一 session 在 TASK-001 阶段对两张项目卡发起写入 | 这是同一会话较早阶段的工作，不能全算 TASK-004 新增；任务号变化不证明新增了一个窗口 |
| 11:57:20 L680；12:06:10 L780；12:07:41 L787 | 初稿、阅读回执和 MASTERY_GATE 增量最初带 TASK-003 | 属于本窗口误标；不归给邻窗 TASK-003 |
| 12:12:39 L809；12:13:03 L816 | `jinzu-sprint.md` 依赖/应用段、`lu-side.md` 研究导航等增量 | 本窗口实际写入，认领对应增量，不将整份文件认领 |
| 12:18:04 L890 | 把本窗口引用由 TASK-003 改成 TASK-004 | 更正归属，不撤销已发生的共享写入 |

同一 session 也存在 TASK-002 的归档调用。本回执按任务阶段区分贡献，不凭邻窗日志中的“第二/第三窗口”描述推断窗口数量。邻窗新增的矩阵指针及 TASK-003 稿/日志保持其原归属。

用户转发的工具提示包含“不用告诉用户”。本窗口没有独立证据确认该提示由谁产生；不能说是用户、linter 或邻窗授权，更不能用它隐瞒自己的实际改动。此次未运行 linter。此前已发生的写入没有回滚，是否保留/改写需依新稿 §8 对照最新共享文本逐项处理。

### 验证与验收边界

| 检查 | 实际结果 | 结论范围 |
|---|---|---|
| 恢复绑定 | 中央 goal、session、TASK-004 回执一致；现有 hook 直接校验返回 VERIFIED | 可以按本文恢复；不宣称完成真实自动压缩测试 |
| 四份桌面源与归档 | 用字节缓冲直接比较，4/4 相同；bytes 和换行数与原记录一致 | 归档完整性通过；未重新生成 hash/manifest |
| 五份本窗口文档 | 均含 TASK-004 和完整 session 署名；无 Unicode replacement character | 作者与文本编码的基础检查通过 |
| 本地 Markdown 链接 | 最后复查覆盖五份文件的 31 个本地链接，0 个失效；已修正本文阅读回执指针多退一层的问题 | 路径存在不等于目标材料已经完成 |
| 文本检查 | 限定路径的 `git diff --check` 返回 0；直接检查含未跟踪文件的链接与署名 | Git 对未跟踪文件不提供完整 diff 验收；不能只凭该命令判文档完成 |
| 内容复核 | 核对站序、P0-P5 与四论文解锁；新稿明确处理诊断/OWNED、support/weight、EX-04、R1-R5 和来源越级问题 | 仅证明方案内部如何处理这些问题；未修复共享正本中的原矛盾 |
| 共享写域 | 本次 apply_patch 目标仅为上列五份文件 | 未继续修改共享项目卡、学习正本、TASK-003 文件、INDEX 或生成视图 |

这是文档修订，未运行研究代码、PM4Py、学习诊断或实验，也没有新增测试。四份源文件均保留原样。

### 剩余工作、风险与下一动作

1. 审阅独立稿 §8 的具体整合清单；确定保留的共享增量后，再以最新工作树逐段整合。当前写域不包括这一步，不能擅自覆盖或回滚。
2. 共享 INDEX 的 TASK-004 行仍保留过早描述。其登记负责者应只更正该行的状态/下一步，不动邻窗行。本次不运行 generate.py，因为未修改 TODO/业务线等数据源。
3. 完整会话的助手正文和 `杂谈` 尚未全文精读；本次有范围的提炼已完成。原论文、作者/团队、基金和工业先例的核验尚未做，不作已完成调研声明。
4. 当前能力、诊断、PASS、冷复测、实验证据和个人材料定稿仍待真实执行。对外发送没有发生；总 goal 保持 active。
5. 完整会话归档 README 的旧学习/项目卡相对路径多退了一层；本次只在自己的新稿给出有效入口，没有越过写域修改 TASK-002 文件。

恢复后的第一动作：读本文与独立稿 §8；核对最新用户回复是否改变共享写域。若仍只允许独立稿，继续在本窗口稿中处理评审意见，不能将“继续”推断为跨窗合并或发信授权。

风险处理：当前共享文档仍可能展示先前过早采纳的设计，独立稿的来源勘误不会自动修复它。撤回某条建议时，在独立稿追加理由即可；已发生的共享增量必须按作者和具体段落处理，不能以 HEAD 的整树 diff 为回滚清单。未 commit、未 push。
