---
task_id: TASK-20260918-005（中央领号 2026-09-18，:8899 在线签发；本文件暂存桌面未归档进仓库，见 §7）
date: 2026-09-18
type: handoff（跨窗口交接）
status: 本窗口工作已完成并落盘，交接文档本身因用户要求暂存桌面
owner: 用户
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
  - progress/task_logs/2026/09/2026-09-18__archive__workbench-research-desk-plugin-reference-batch.md（TASK-20260918-002）
  - progress/task_logs/2026/09/2026-09-18__research__two-desks-plugin-mechanism-deep-scan.md（TASK-20260918-004）
  - progress/decisions/2026-09-17__research__two-desks-purpose-redefinition-proposal.md
  - 2026-09-18__新增28条GitHub链接登记.md（同目录，本窗口另一件未完成登记）
---

## §0 · TL;DR（≤80字符）

两台参考清单R13-R15共16项已整合入库；考研台架构问题待拍板；28条新链接仅桌面登记未分类。

## §1 · 本窗口完整时间线（供追溯，非必读）

本窗口跨越至少两次自动压缩，实际发生顺序：

1. 用户先问"科研台/学习台进度"，多个只读子代理溯源三台设计原话、代码实施映射、G0-P7驾驶舱状态、OpenScience身份重叠核查、全项目参考清单去重盘查——这部分是纯调研，未产生写盘变更。
2. 用户贴一批社媒帖转述的Obsidian插件名（11项，无原始链接）+ 用户自选的确切链接批（14项，按考研/工作台/科研三分类），明确要求"存一下是工作台参考和科研台参考"。落地为 `TASK-20260918-002`：R13（社媒帖批，WebSearch按名核实身份）+ R14（用户确切链接批，13项非重复）追加进 `REFERENCE_NOTES_20260915.md` §7.8，§0编号从13项→15项（R01-R14+I01）。
3. 用户说"写一下这个窗口的交接文档"——这是**当前仍未完成的原始请求**，见下方§2。
4. 交接文档撰写被新指令打断：用户要求多Agent并行调研这批新增参考项目"能用在哪个台"，同时提出一个全新未拍板的架构问题——**是否新增"考研台"**。用户先要求"先给我确认一下范围、产出预期产物、各项标准、验收标准"，方案经一轮自我批判后用户拍板"没有了，改一下计划然后直接跑"。
5. 又追加两个考研对比链接（Pkmer-Math、Math-And-English-Library），要求与R14的Lazy-Kaoyan-Library、R13的obsidian_math、已独立深查的`virtualxiaoman/kaoyan`（`TASK-20260911-007`）放一起比较。
6. 6个`general-purpose`子代理并行核查了合计26个GitHub URL（R13全部11项+R14非重复13项+新增2项），5 caps约束（URL/字数/时间/工具/done_when）全部遵守，无超时无缺项。落地为`TASK-20260918-004`：结果整合进`REFERENCE_NOTES_20260915.md`新增§7.9（7个子节），§0编号15项→16项（R01-R15+I01）。
7. 用户重新问"现在的进度？"——本窗口据此重新核对磁盘状态并汇报（详见§2）。
8. 用户开始整理文件夹，把 `/mnt/d/MyResearch` 往新建的 `/mnt/d/Workspace` 迁移；同时贴出28条新GitHub链接（微软系列教程/Agent工具/若干同名不同项目），要求先不动应用改动、这次所有产出先放桌面。已落一份纯登记文件（未分类未核实），见 `2026-09-18__新增28条GitHub链接登记.md`。
9. 本文件——用户最初"写一下这个窗口的交接文档"这个请求，现在补上。

## §2 · 已完成（对照证据，均可复核）

| 项目 | 状态 | 证据 |
|---|---|---|
| R13（社媒帖转述批，11项）身份核实 | 完成 | `REFERENCE_NOTES_20260915.md` §7.8.1；10/11按名WebSearch找到高置信匹配 |
| R14（用户确切链接批，13项非重复）分类登记 | 完成 | 同文件 §7.8.2，按用户原始三分类（考研/工作台/科研）呈现，未擅自改判 |
| R15（26个URL机制层深查）核心内容/工作流/能不能用得上 | 完成 | 同文件 §7.9（§7.9.1-§7.9.7 七个子节）；`TASK-20260918-004` |
| 考研对比组四维对比表 | 完成 | §7.9.1：obsidian_math / Pkmer-Math / Math-And-English-Library / Lazy-Kaoyan-Library 四项+kaoyan引用（不重读），按内容定位/血缘痕迹/三段式工作流/版权来源四列比较 |
| 关键发现：Lazy-Kaoyan-Library血缘声明 | 完成并落盘 | 该仓明确声明"灵感来源于Math-And-English-Library和Pkmer-Math"，自建"AI+OCR转录→思维导图+AI对话→Dataview+Templater模版驱动"三段式工作流；后两者本身均为纯静态笔记无工作流；此三段式与已深查的`virtualxiaoman/kaoyan`三段式（人工记录+Python统计+外部AI批改）目标相似但实现路径完全独立、互不知晓——同一问题两种独立收敛解法 |
| 共享登记面写入 | 完成 | `progress/TODO.md`：RD-3（R13/R14登记）、RD-4（R15机制层深查）、RD-5（"是否新增考研台"架构问题挂项）三行，均用`ledger_edit.py` CAS哈希保护写入，VERIFY-OK；`progress/task_logs/INDEX.md`新增`TASK-20260918-002`、`TASK-20260918-004`两行 |
| task log | 完成 | `2026-09-18__archive__workbench-research-desk-plugin-reference-batch.md`（002）+ `2026-09-18__research__two-desks-plugin-mechanism-deep-scan.md`（004），均含完整验收与证据表、Amendment哈希记录 |
| 看板视图重新生成 | 完成 | `python3 tools/scripts/generate.py` 已重跑，`STATUS/NOW/PROJECT_HOME/WEEK/DAILY/dashboard/*` 已反映新TODO行；生成器警告（撞号`TASK-20260821-001`、几个陈旧campaign）均为历史已知问题，非本窗口引入 |
| 文件编码完整性 | 完成（过程中3次发现并修复） | `REFERENCE_NOTES_20260915.md`与`TASK-20260918-004`task log在撰写中各混入过复制粘贴导致的U+FFFD替换字符，均已定位修复，当前复验0残留 |
| 28条新链接原文留痕 | 完成（仅登记，未分类未核实） | `2026-09-18__新增28条GitHub链接登记.md`（桌面），未进`TODO.md`（记账线未定） |
| respond-in-chinese-preference记忆 | 完成 | `~/.claude/projects/-mnt-d-MyResearch/memory/respond-in-chinese-preference.md` + `MEMORY.md`索引行均已确认存在 |
| 外层仓库`GUARDRAILS.md`/`WINDOW_PLAYBOOK.md`未提交改动溯源 | 完成——**结论：非异常，无需处理，勿重复调查** | `git log -1`显示两文件最后一次commit分别是`50d731c`(2026-08-23)和`7b13459`(2026-08-24)；当前未提交diff经核对：`GUARDRAILS.md`增量正是文件内自带的"2026-09-03 amendment"（§5.1运行时身份留痕）与"2026-09-08 amendment"（§8，原文写明用户"一一看过了，全部修改"已授权）；`WINDOW_PLAYBOOK.md`增量是P批1死线从"09-10进组"同步为"9月底进组"，与`CLAUDE.md`用户信息栏"2026-09-03用户统一改月底"完全对应。两处均为早于本窗口、已获用户授权的存量改动，只是十几天来没人commit，不是任何窗口的新编辑；本窗口全程未对这两个文件做过任何Edit/Write |
| `two-desks-trial-20260917`/`research-desk`只读现状核实 | 完成（只读，未操作） | `two-desks-trial-20260917`本身**没有**独立`.git`，是外层`/mnt/d/MyResearch`仓库的一部分（remote指向`my-cockpit`）；其`materials/`子目录是独立仓已推送到`Alkaid-9/Research-Garden`（本地HEAD与远端一致）；三个服务端口18880/18881/8878经`curl`探测均不可达（返回000），与用户"昨晚试了下，就这样"的说法一致。`research-desk`（不同目录）**有**自己独立的`.git`，commit历史`0b3a541`→`c86f6d1`→`b54ea71`→`d53d188`，含大量未跟踪的acceptance测试截图/日志（`acceptance/a-TASK-20260915-002/`等），无remote配置 |
| `myresearch-b9` peer session广播机制说明 | 完成（供后续窗口参考） | `ListAgents`确认存在一个独立同级Claude Code会话`myresearch-b9`（非本会话子代理），它自己在跑batch1-batch6一批子代理；这些子代理的`idle_notification`空闲心跳会以`<teammate-message teammate_id="..." color="...">`格式广播到本会话。这类消息**不是**给本会话的实质工作请求，只是状态通知，与本会话工作完全独立；用户曾中断过一条这样的通知，实际未丢失任何工作 |

## §3 · 未完成 / 待用户拍板（不代为判断）

1. **是否新增"考研台"**——用户在派发`TASK-20260918-004`时提出，属全新未拍板架构问题，已按铁律8单独挂`TODO.md` RD-5行。§7.9.1的考研对比表可作决策输入，但不代替拍板。与09-17的`two-desks-purpose-redefinition-proposal.md`（学习台/科研台/工作台槽位重定义提案，PROPOSED未采纳）是**两个独立问题**：一个问"既有槽位怎么重定义"，一个问"要不要加第四个槽位"。
2. **26项"能不能用得上"字段未做处置判断**——borrowing/转化设计/隔离试用/正式接入/暂存不采用五选一，本次刻意不做，等用户或后续任务决定。
3. **28条新贴GitHub链接完全未处理**——已在桌面纯登记（原文+肉眼分组，未核实未分类），归属哪条记账线（External旧账本/RE-30/Bridge线/两台线，均不贴合；或需单独开线）未定；是否WebSearch核实也未定。
4. **`research/map/*RESTRUCTURING_20260917*`**——一个与既有v0.2/v0.3菌丝网设计零交叉引用的第二套知识图谱设计，此前窗口已发现但从未处理，本窗口同样未处理。
5. **Bridge线×RE-30参考清单重叠**——两条独立记账线的24仓/47仓交集从未正式核对，此前调研只是发现问题未解决。
6. **R04/R05 OpenScience身份**——两处独立记录因互不知道对方而重复"身份待补"，此前调研发现三个候选真实仓库（ai4s-research/synthetic-sciences/aipoch三家open-science，star数均与原声称的"2.1k"不符），未收敛判定。
7. **多窗口`TODO.md`/`task_logs/INDEX.md`未提交积压**——本窗口写入前后，这两个文件在`git status`里一直是`M`（他窗口遗留），本窗口未reset/未覆盖，只做单行追加；是否提交，不在本窗口权限内判断。
8. **workspace重组进行中**——用户当前正把`/mnt/d/MyResearch`往新建的`/mnt/d/Workspace`迁移（已见`Toolbox`/`claude-code-remote`/`新建文件夹`落位），此前`docs/workspace-reorganization-20260918/README.md`记录的计划状态是`PROPOSED_NOT_MOVED`——**这个状态现在已经是过期的**，实际移动已经在发生。下一个窗口打开时，`/mnt/d/MyResearch`这个路径本身是否还存在、是否已经改名或整体挪位，需要先核实，不能假定路径不变。

## §6 · 新窗口第一动作 / 必读

1. **先确认`/mnt/d/MyResearch`路径是否还在原位**——用户正在手动重组到`/mnt/d/Workspace`，可能仍在进行中或已完成一部分；本文件与28条链接登记文件目前都在`D:\Alkaid\Desktop`，尚未随重组移动，也尚未归档进仓库。
2. 若要续接两台参考清单工作：读`REFERENCE_NOTES_20260915.md` §7.9（本窗口新增，R01-R15+I01共16项现状）+ `TODO.md` RD-4/RD-5两行。
3. 若要处理28条新链接：读桌面`2026-09-18__新增28条GitHub链接登记.md`，先问用户想归哪条记账线，不要自己新开第五条。
4. 若要处理"是否新增考研台"：这是用户的架构决策，不由AI代为判断；只在用户主动问起时提供§7.9.1对比表作参考。
5. 本文件与其配套的28链接登记文件目前**只在桌面，不在仓库**——如果用户示意"可以归档了"，需要：把两份文件正式移入`progress/handoff/`与合适位置、在`progress/handoff/INDEX.md` §1追加路由行（用`ledger_edit.py`，非直接改写）、`TASK-20260918-005`这个已领但未消费的号在那时候才正式使用。

## §7 · 禁止越界

- 不代用户判断是否新增"考研台"，不代做28条链接的分类/记账线归属。
- 不主动移动/整理`/mnt/d/MyResearch`或`/mnt/d/Workspace`任何文件——用户在手动进行，AI不插手，除非明确被要求。
- 不把本窗口的两份桌面产出自作主张移进仓库——用户明确说"这次全部产出先放桌面"。
- 不重跑R13/R14/R15的调研（已完成且已验证一致，重跑是浪费）。
- 不擅自处理`research/map/*RESTRUCTURING_20260917*`与既有设计的调和、Bridge×RE-30重叠、R04/R05身份——这些都是已知缺口，等用户指派。

## §8 · 完成判据

本窗口的两条任务线判定如下：
- **任务线B（26项参考机制层整合）**：已100%完成，可复核（见§2表格），无需进一步动作除非用户要处置判断。
- **任务线A（交接文档）**：本文件即完成态，但**归档动作**（移入仓库+INDEX路由行）明确未做，等用户示意重组完成或单独授权。

## §9 · 主控默认问句（用户没拍路径时主动问）

- "28条新链接想放进哪条记账线，还是先不管？"
- "考研台这个架构问题，现在想拍板，还是先放着？"
- "workspace重组完成了吗？我要不要把桌面这两份文件挪回仓库？"

## §-1 · 复核记录

| 维度 | 结果 | 备注 |
|---|---|---|
| L0-1 零 `/tmp/` 路径 | ✅ | 全文无 `/tmp/` 引用 |
| L1-1 交接档本身存在 | ✅ | 本文件 |
| L1-2 关联决策档存在 | ✅ | `REFERENCE_NOTES_20260915.md`、`two-desks-purpose-redefinition-proposal.md` 均已存在 |
| L1-3 关联task_logs存在 | ✅ | `TASK-20260918-002`、`TASK-20260918-004` |
| L2-1 每件task有触发条件 | ✅ | §3各条均注明触发来源 |
| L2-2 无语义重叠的in_progress/pending | ✅ | RD-4（已完成的调研）与RD-5（待拍板的架构问题）明确区分，不重叠 |
| L2-3 completed任务有description总结 | ✅ | §2表格逐项带证据 |
| L3-1 本会话用户护栏全落memory | ✅ | 中文回复偏好、增量输出偏好均已落盘（见MEMORY.md索引） |
| L3-2 不重复立已有护栏 | ✅ | 未新增重复memory |
| L4-1 memory链接用`[[name]]`格式 | ✅（本文件未直接引用memory文件，格式要求不适用） | — |
| L4-2 关键决策档交叉引用 | ✅ | 见frontmatter `related` 字段 |
| L4-3 §0 TL;DR ≤80字符 | ✅ | 40字符 |

**特殊说明**：本次是唯一一次交接文档未能完成"归档进仓库+INDEX路由"这一步，原因是用户明确指示本轮产出先放桌面（配合其正在进行的workspace重组）。这是刻意的、用户授权的偏离，不是遗漏。

**本文件写作过程中的一次自我修正**（诚实记录，非隐瞒）：撰写初稿时曾把`GUARDRAILS.md`/`WINDOW_PLAYBOOK.md`的未提交diff描述为"疑似其他窗口的新编辑"；重新核对`git log -1 -- <file>`与diff具体内容后发现判断有误——两处改动都能在文件自身文本里找到对应的、早已获用户批准的amendment记录（日期分别是2026-09-03/09-08和09-03），只是迟迟没commit，不是新发生的事。已在§2表格更正为准确结论，不带着错误的"异常"标签移交下一个窗口。
