---
id: TASK-20260917-006
title: 进组学习包盘点与资料库整理
date: 2026-09-17
runtime:
  model: GPT-6
  effort: UNKNOWN
  effort_source: 系统未提供推理档位；当前交互式有界文件整理
  launch: Codex 当前交互会话
type: setup
status: done
area: learning
project: jinzu-sprint
todo_ids: []
owners:
  - user
related:
  - progress/projects/jinzu-sprint.md
  - progress/projects/teaching-prefab.md
  - progress/decisions/2026-09-13__research__four-paper-full-ownership-v3-sol-execution-contract.md
---

# 目标与授权

用户当前直接要求：“可以了。现在 立刻 整理一下进组的目前的所有学习包放进去”。用户此前要求施工前说明详细方案与架构。本任务先核对既有学习包和具体导入映射，在现有 Obsidian 资料库中整理学习入口；不借此批准新的架构或恢复其他施工任务。

# 恢复入口

- 当前会话：`codex / 01a0af78-69be-7dc1-b2c8-787650d7d319`。
- 本任务由用户当前指令新建，中央发号器签发 `TASK-20260917-006`，不从自动摘要推定旧任务授权。
- 先读本文，再读 `progress/projects/jinzu-sprint.md` §7、四论文 v3 合同 §1.3、`ownership-v3/BUILD_STATUS.md`、09-15 三缺口补修交接和 `progress/projects/teaching-prefab.md`。
- 目标资料库：`/mnt/d/MyResearch/two-desks-trial-20260917/materials`。具体导入方案在清单完成后说明；LearnGraph 批量导入尚不在已明确范围内。
- 写域限本任务文档、所属 INDEX 行和具体确认后的资料库新增内容；源课程、作答、Ledger、密封答案和架构正本不改。

# 当前状态

已完成资料库整理并推送新 Obsidian 仓库。导入 286 份来源文件，新增六个站点导航页及总入口、来源说明、逐文件清单和引用检查；未调用模型或批量导入 LearnGraph。

# 验收与边界

- 区分当前路线、备课资产和历史版本；课程建成不代表用户掌握或自动解锁。
- 密封答案、未见测验和考官材料只盘点路径，不读取正文或进入普通检索库。
- 导入时保留来源与原目录关系，核对引用和复制结果，不覆盖用户原文件。
- 不 commit/push，不整理其他 MyResearch 项目，不读取或复制模型密钥。

# 下一步

用户可在 Obsidian 首页打开“进组学习包总入口”，从当前 EX-05 或其他既有学习包继续。旧资料中的历史失效路径见 LINK_CHECK.md；批量建课、三台架构调整和 MyResearch 全目录整理不属于本次结果。

## Amendment

### 2026-09-17 — 导入与 Git 同步完成

- 用户补充“git也同步一下”，并明确追问“我们同步的是那个新的ob仓库吧”；已确认唯一同步对象是 `Alkaid-9/Research-Garden`，不是 MAS 原仓库。
- 主线程向用户说明四类材料布局、原目录复制关系、密封隔离和按需送入 LearnGraph 的接入方式后，执行本次明确要求的资料整理；没有新增三台架构或数据库设计。
- 目标：`/mnt/d/MyResearch/two-desks-trial-20260917/materials/learning/group-entry/`；原文件未移动或修改。按源工作树实际内容复制，未声称其等于某个纯净提交。
- 内容：EdgeIM 八站和四论文 ownership-v3、四个专项训练包、P批六包、EmoAgent 补充工作册、EvoAgent Phase 1、鲁组旧联卷及基础模块、配套论文与方法材料。
- 当前入口按 jinzu-sprint §7 和 v3合同 §1.3 指向六项恢复包及 EX-05；D2 不重新作为当前前置。保留课程建设与本人能力的区别、09-15补修开放项、历史包标记。
- 复制前后直接字节核对通过；286份最终来源文件有源路径/目标/大小/时间记录。初核286份后补入两份公开读前材料，并在推送前排除两个额外考试编排文件；排除发生在本地提交改写阶段，未推送被排除文件。
- 新总入口与原文清单的文件链接检查通过；为六个历史站点文件名补导航，修复14处引用（含两个读前文件）。原资料仍有87处已记录的库外/密封/历史失效或非标准引用，不能声称所有旧链接通过。
- 密封、考官、正式考试文件未进入最终 Git 树；已有本人作答保留。未改变学习 Ledger 或掌握状态。常见令牌/私钥模式扫描未发现命中文件，不代表通用秘密审计。
- Git：SSH 访问指定新仓成功，初始远端无 refs；未认证 GitHub API 返回404。设置 exact remote `git@github.com:Alkaid-9/Research-Garden.git`，只暂存资料库 README 与 group-entry，未暂存运行状态或模型配置。
- 本轮资料提交 `f2e6a482ad83b0ae4c375ebcb23b9215b3cbd8d0`；`git push -u origin main` 成功，新建远端 main。资料仓状态 `main...origin/main`，工作树干净；远端 refs 另行复验。
- MAS 仅写本任务日志与所属 INDEX 行，未 commit/push；旧 MyResearch 全目录、LearnGraph源码/数据库与服务均未变。
- 回退范围限新资料仓本轮提交；源课程仍在原路径，不能用回退覆盖后续用户学习记录。
- 收尾复验：`git ls-remote origin refs/heads/main` 返回 `f2e6a482ad83b0ae4c375ebcb23b9215b3cbd8d0`，与本地 HEAD 相同。INDEX 写后与收尾 `--check` 均为纯 CRLF / 326行，收据 `8630047cc8861dcb4b97f2237e3278280b9f7761d44be4a87f657065cf9a17e4` 一致。
