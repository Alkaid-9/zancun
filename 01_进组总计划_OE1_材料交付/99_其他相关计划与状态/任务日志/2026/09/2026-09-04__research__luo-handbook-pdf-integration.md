---
id: TASK-20260904-003
title: Luo 博士生科研入门辅导 PDF 直读与三源科研体系适配
date: 2026-09-04
runtime:
  model: Codex main window
  effort: max
  effort_source: current session harness
  launch: Codex API workspace
type: research
status: completed_with_open_gates
area: bridge/learning
project: lu-edgeim-bridge
todo_ids: []
owners:
  - codex-main-window
related:
  - research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/B2b_luo_handbook_pdf_reading.md
  - research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/B2_supervisor_skills_handbook_methods.md
  - research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/B3_research_growth_index.md
  - research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/B4_research_system_v0_PROPOSED.md
  - /mnt/d/MyResearch/research_growth/方法论/科研体系三源整合_20260904.md
---

# 目标

直接读取用户给定的 `D:\Edge下载\博士生科研入门辅导.pdf`，包含图像页面的结构性视觉核对；准确区分讲者经验、原文事实和待验证内容；把可迁移机制接入已有的 Supervisor-Skills、pengsida 与当前 OS 的适配层。

# 最终结果

PDF 70 页已完成文本抽取和代表性页面视觉核对。用户下载件与 Supervisor-Skills 仓内同名 PDF 字节一致（两件各 17,411,724 bytes），因此没有复制第二份源件。新证据读本 `B2b_luo_handbook_pdf_reading.md` 已落盘；个人整合入口 `research_growth/方法论/科研体系三源整合_20260904.md` 已落盘并在 README/SKILL_INDEX 导航；B2/B3/B4 追加了 `TASK-20260904-003` amendment；现行 `learning/methodology/RESEARCH_METHODOLOGY.md` 增加了入口指针。OS 冻结文件、训练包、主 MANIFEST 和 TODO 均未改。状态仍为 `completed_with_open_gates`：外部事实/图内细节核验、L0–L5 正式采纳和公开许可仍需单独门。

# 修改内容

- 新增 PDF 证据读本：页码地图、选题/阅读/写作/审稿主张、图像可读性、三源交叉表、排除口径和许可边界。
- 新增个人三源整合卡：明确 Luo PDF（导航）、Supervisor-Skills（提问/检查）、pengsida（实验/调试）、OS（事实/ownership/验收）的分工，以及六步用户先做流程。
- 更新 `research_growth/README.md` 和 `research_growth/方法论/SKILL_INDEX.md`，提供整合卡入口。
- 更新 B2：将 PDF 从“未读”改为“已读/图像限制”，追加 M 组件适配说明；不增加重复 M 编号。
- 更新 B3：追加 research_growth 入口和三源角色说明。
- 更新 B4：追加 proposal-only 挂载表；维持 36 个既有适配组件计数和 `PROPOSED` 状态。
- 更新 `learning/methodology/RESEARCH_METHODOLOGY.md`：加入整合卡短指针和 OS 优先级声明。
- 新增本任务日志；待主控按当前 INDEX 行格式登记。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 源件身份 | 用户给定 PDF 与仓内源件可对齐 | PASS | `cmp` 返回 0；`pdfinfo` 70 页、960×540 pt、未加密 |
| 文本覆盖 | 读完 PDF 文本层并形成页码地图 | PASS | B2b §1–§2；`pdftotext -layout` 抽取 |
| 图像读取 | 代表性图页直接渲染目视核对 | PASS-WITH-LIMITS | B2b §0、§3；p.6/11/16/20/30/36/42/50/53/57/61/68/69 |
| claim ceiling | 经验数字、截图小字、外部链接不升级为事实 | PASS | B2b §3、§6；整合卡 §5 |
| 三源交叉 | 每条新增机制可指向 SS/pengsida/OS 现有位置 | PASS | B2b §4；整合卡 §1–§4 |
| 用户 ownership | 不生成用户能力、G0/T0 或研究完成结论 | PASS | B2b §5、§8；OS 未改 |
| 导航可达 | 个人整合卡有 README/SKILL_INDEX/方法论入口 | PASS | `research_growth/README.md`、`方法论/SKILL_INDEX.md`、`learning/methodology/RESEARCH_METHODOLOGY.md` |
| 工作树纪律 | 不覆盖他窗已有修改、不提交 | PASS | 当前 nested HEAD `da66308`；本任务未执行 git add/commit/push |
| 收尾复核 | 链接、纯 CRLF 登记、无尾空格、源件身份与冻结范围 | PASS | `ledger_edit.py --check`：INDEX 纯 CRLF，sha256 `20c49b25…`; `cmp` 返回 0；OS/TODO 无 diff |

# 当前状态

- 证据层已读并入索引；个人方法库已有可直接使用的适配卡。
- `learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md` 保持原样；B4 仍是 proposal，不是权威。
- `external/Supervisor-Skills` 与 `external/learning_research` 未修改；其原始仓库身份和许可仍以各自仓库为准。
- 任务涉及两个 Git 工作树：MAS nested repo 与独立 `research_growth` repo；两边均保留未提交状态，未声称已入库/已推送。

# 尚未完成

- Luo PDF 中示例论文/年份、政策链接、时间线、速度对比、接受率和截图微小标签未逐项联网或回到原论文核验。
- `pengsida_pdfs/*.pdf` 五份原件和 Notion 六页仍按 B1/B4 标记为未读或待核，不被本 PDF 读取替代。
- B4 的 L0–L5 是否写入冻结 OS、CC BY-NC-SA 改编署名位置、05 章张力等用户决策门仍开放。
- 未更新 `progress/TODO.md`，因为本任务没有新增用户授权的登记项；未更新 memory，因为本任务未获得显式 memory 写入请求。

# 下一步

1. 用户用整合卡完成一篇论文的 paper note 或一次小实验，再以 prediction/变体/冷启动验收是否真正有用。
2. 若要公开整合卡，先确定 CC BY-NC-SA 署名与改编声明，再另开许可/发布门。
3. 需要事实核验时，逐项回到 PDF 所列原论文、官方 venue 页面或作者仓，而不是把讲义数字直接搬入账本。

# 可拓展方向

- 将整合卡的纸面字段按当前 frozen slice 做一张最小 paper-note 适配表（需单独批准，避免重复模板）。
- 对未读 pengsida PDF 做同样的原件核对；不能用本任务结果替代。
- 在真实用户作答产生证据后，再决定哪些问题进入训练包题面或方法卡。

# 风险与回滚

- 风险：个人整合卡是受 CC BY-NC-SA 来源影响的改编摘要；公开分发前必须补署名、许可证链接和改编说明。
- 风险：把讲义的经验性比例/时间/接受率写成硬规则会造成 claim 越级；已在 B2b 和整合卡中显式排除。
- 风险：现有 B2/B3/B4 是前一窗 evidence/proposal 文件，后续若有人重写需保留本 amendment；不要用整文件覆盖。
- 回滚：删除本任务新证据读本、整合卡及其导航/指针 amendment，并将本任务 INDEX 行反向替换；不触碰原始 PDF、外部仓和冻结 OS。

# 文件和产物

- `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/B2b_luo_handbook_pdf_reading.md`
- `/mnt/d/MyResearch/research_growth/方法论/科研体系三源整合_20260904.md`
- `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/B2_supervisor_skills_handbook_methods.md`
- `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/B3_research_growth_index.md`
- `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-04__research-system/B4_research_system_v0_PROPOSED.md`
- `learning/methodology/RESEARCH_METHODOLOGY.md`

## Amendment

2026-09-04：本日志记录 PDF 直读与三源适配；收尾复核时将 B3 的证据读本占位路径改为仓内真实相对路径，并把整合卡中“现有 OS 的 L0–L5”纠正为“B4 proposal 挂载标签”；未执行 commit/push。若后续用户批准 L0–L5 或公开发布，另立决策/发布任务，不回写本日志的历史结果。
