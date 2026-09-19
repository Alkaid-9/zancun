# 2026-09-17 全部进度与进组学习包总交接

日期：2026-09-17。任务：`TASK-20260917-007`。状态：`RECOVERABLE / FULL-SCOPE-SNAPSHOT / PROJECTS-PARTIAL / ARCHIVE-DONE`。

本档回答用户连续两次校正后的要求：先“存档当前进度”，再明确为“全部的进度”，并追问进组相关的包是否完整。这里的“全部”覆盖：2026-09-17 全部任务、全部已发现的进组学习包、OE-1 与进组交付、鲁侧到孙侧及工业界方向、Bridge 研究学习复用，以及支撑这些工作的科研台／学习台／工作台和新 Obsidian 资料仓。Kaggle、考研等无关项目不纳入本档。

## 0. 恢复入口与阅读顺序

新窗口按以下顺序恢复，不从聊天摘要猜当前任务：

1. 先读本档 §1、§3、§4、§8；
2. 当前学习动作读 `progress/projects/jinzu-sprint.md` §7 和四论文 v3 合同 §1.3；
3. 当前资料入口打开 `/mnt/d/MyResearch/two-desks-trial-20260917/materials/learning/group-entry/README.md`；
4. 三台产品状态读 `progress/handoff/2026-09-17__research-desk-workbench-global__handoff.md`；
5. 进组研究拓展读 TASK-001 总合同与 W1 回执；
6. OE-1 只在用户选择分支并补齐个人字段后继续，不由恢复者代填或发送。

恢复边界：课程文件存在不等于用户掌握；课程资产 `QA-PASS` 不等于用户 `PASS`；技术服务 HTTP 200 不等于用户验收；总合同存在不等于 W2-W7 已启动。

## 1. 一句话全局结论

今天已经把三件大事接起来了：第一，三台架构从“几个平级容器”收敛到共享 object／source、多 view 判断和独立任务执行层的方向；第二，NotEMD＋LearnGraph 已形成可运行的本地试用路径，并由新 Obsidian Git 仓承载资料；第三，现有进组学习包已按当前主线、专项训练、待学备课和历史复习整理进该仓并推送。

项目仍远未“全部完成”：EdgeIM 当前六项恢复包未做完；ownership-v3 课程已建但 rubric 未冻结、用户能力未验收；P 批六包和 EmoAgent 尚未正式开考；ra26／ra28 是 Agent 先行后的逆向训练债；ra2716／ra30 未闭；OE-1 未选择和发送；进组拓展 W1 只完成一部分；三台旧科研驾驶舱仍有保存 RED，NotEMD AI 抽取和真实 LearnGraph 学习也未验收。

## 2. 2026-09-17 全部任务线

| 任务 | 窗口／性质 | 已完成 | 当前状态与开放门 |
|---|---|---|---|
| `TASK-20260917-001` 进组包拓展 W0-W7 | 其他 controller 窗口 | 总合同、W0 AC-01..08、W1 的 IND-1 与 RS-B | `W0-COMPLETE / W1-PARTIAL / RS-A-RECOVERY-NEXT / USER-ACTION-OPEN / W2-W7-GATED`；缺 URL 矩阵、Bridge 余项及 BPM/ICPM 接收面；未 commit/push |
| `TASK-20260917-002` 三台／工作台／驾驶舱全局交接 | 其他 controller 归档窗 | 全局分层、已做／未做、Git／服务和恢复顺序 | `PARTIAL-PRODUCT / USER-TRIAL-RED / WORKBENCH-AUTO-OPEN / COCKPIT-G0-COMPLETE`；日志和 handoff 存在，但此前漏挂两个 INDEX，本任务补路由 |
| `TASK-20260917-004` 两台全景与参考清单 | Claude Code／Fable 窗口 | 本地 HTML 全景、两台 13 项＋Bridge 24 仓清单、历史测试数字及 G0 零应用代码触碰核验 | Bridge×RE-30 未核；R04/R05 身份未钉死；`research-desk` 项目卡缺失 |
| `TASK-20260917-005` NotEMD＋LearnGraph 串接试用 | 较早 GPT-6 交互窗；日志无 session id | EdgeIM 上传解析、PDF 预览补丁、问题种子往返、导出保形、重启恢复、新 vault 初始提交 | GitHub 门已被 TASK-006 后续关闭；仍缺 NotEMD/远程模型实测、真实非空学习对话、用户试用和正式架构适配 |
| `TASK-20260917-006` 全部进组学习包入新 vault | 当前 Codex 会话前一任务 | 286 份源文件、6 个站点导航、总入口／来源清单／引用检查；提交并 push `f2e6a48` | 旧材料仍有 87 项库外／密封／历史失效引用；未批量导入 LearnGraph；未整理整个 MyResearch |
| `TASK-20260917-007` 本总存档 | 当前 Codex 会话 | 对账上述任务、全部进组包、Git、服务、开放门与恢复顺序 | 本任务只归档和修复路由；不改变课程能力、产品状态或其他窗口施工 |

窗口责任不能混写：TASK-001／002／004 的成果是磁盘上其他窗口的事实；TASK-006 和本任务有当前 Codex session 明确绑定。TASK-005 的日志只证明较早 GPT-6 交互工作，不能仅凭模型名证明和当前根会话同一。

## 3. 架构与两台底座当前结论

### 3.1 用途框架

- 科研台：回答“世界已知什么、证据怎样连接、我的研究判断怎样变化”；承载知识图谱、菌丝网、科研地图、团队脉络、方法谱系、工业信号和失败经验等观察面。
- 学习台：回答“我是否真正掌握”；承载目标、尝试、反馈、提示暴露、掌握证据、冷复测和迁移。
- 工作台：协调已选择行动的负责人、优先级、依赖、状态、验收与恢复；任务完成不自动升级研究结论或掌握状态。
- 科研与学习共享 material/object/source，但保留不同 view；工作台评价 task，而不是第三套内容对象。

### 3.2 两轮生长与长期方向

第一轮可围绕论文生成概念、来源和初始关系；学习过程中积累第二轮种子，再长出问题、方法、团队、工业、开源、失败与后续成果网络。论文之后只是可重激活节点，不永久占据中心。

长期方向提案是保持个人主线，近期承接鲁侧训练，未来兼顾孙侧形式化／可信 AI 能力，并提高工业采用、成本、延迟、可靠性、评测、部署、开源维护和失败经验的可见度。方向尚未冻结为具体选题、界面或数据结构。

### 3.3 当前底座分工

- NotEMD：两台共用的阅读、笔记、概念候选、wiki-link 和来源组织底座；既可服务具体学习，也可服务科研网络。
- LearnGraph：学习目标、材料关联、尝试／反馈／掌握／下一步的参考底座。
- 原科研菌丝网、工作台任务层和完整科研观察面尚未被这两个仓库替代。
- 当前策略是“先串接使用，再按真实使用缺口向自身架构调整”；并未决定整仓长期采用，也未冻结最终多层数据结构。

## 4. 全部进组相关包与真实状态

### 4.1 当前学习主线

| 包 | 状态 | 当前动作／边界 |
|---|---|---|
| EdgeIM 八站 | `CURRENT / EX-05` | 路线为 `EX-00→EX-01→EX-05a→EX-02→EX-03→EX-05→EX-06→EX-07`。先完成 v3 合同 §1.3 六项恢复包，再继续 EX-05；旧十五题现为最终 D2，不是当前前置 |
| ownership-v3：EdgeIM B-S2／B-S3A／B-S3B／B-EVAL／B-DEFENSE | `ASSET BUILT / LEARNING PENDING` | 课程资产 `BUILT / QA-PASS`，rubric `NOT-FROZEN`；来源开放项和 09-15 三缺口仍存在；不写用户能力状态 |
| ownership-v3：sigRank／Ground Truth／CrossEdgeIM P0-P3 | `ASSET BUILT / LEARNING PENDING` | sigRank 含已记录 errata；Ground Truth 与 CrossEdgeIM 有来源／复现实参缺口；CrossEdgeIM 不是鲁法明署名论文 |

EdgeIM 当前六项恢复包：补 EX-01 G0 五问；补 C00/C01/C05a/C02 CONNECT；补 L-S1 对照；补 EX-02 `SR-__` 和 EX-03 `EC-__`；每站补全文回接句；按 rubric 复核后才能追加 Ledger。任何一项都不能由导入文件或 AI 代签。

### 4.2 四个专项训练包

| 包 | 状态 | 事实边界 |
|---|---|---|
| ra26 EvoAgent trace→PM4Py | `HISTORY PRODUCT COMPLETE / USER REVERSE-TRAINING PENDING` | toy、报告与对照实验由 Agent 先行；用户仍需按逆向训练入口 review、抽查、复算，不得包装成本人独立完成 |
| ra2716 导师画像与谱系 | `PENDING` | 当前应走 EX-01R 证据审计；旧 EX-01 不追认 PASS；与 OE-1 一样受用户本人核对门约束 |
| ra28 MindBridge | `HISTORY / REVERSE-REVIEW PENDING` | Agent 先行完成部分事件导出与日志；Ledger 明记“降级→逆向训练”，用户 review 未闭 |
| ra30 记忆架构＋Petri 网 | `PENDING` | EX-01→03 需用户顺序完成；EX-04 受至少一篇目标 SBPN 原文精读及 file＋定义编号前置约束 |

### 4.3 预制待学／待考包

| 包 | 当前状态 |
|---|---|
| P 批六包：ProbGuard、AgentSpec、FoldA、鲁组 PN 四篇联卷、INTIMA、Anchor | 预制和审计 6/6 已完成；正式教学仍 `TEACHING-AWAITING-USER`，不能按资产完成推导用户掌握 |
| EmoAgent | 第七个教学母版／公开工作册已收录；正式教学仍属于 0/7 待用户 |
| SBPN／EdgeIM／MHP teaching_paywall3 | 历史联卷，18 题仍需本人完成；不替代当前 EdgeIM 八站＋ownership-v3 |

新 vault 只收学习者可读工作册、公开材料、错题模板和论文导航；密封答案、主考流程、正式口试材料没有进入普通检索库。

### 4.4 历史复习与方法库存

- EvoAgent Phase 1：历史学习地图和复习包；地图是导航，不证明 Phase 2、实现掌握或研究迁移已经完成。
- 鲁组七篇旧路线：保留复习和谱系价值；旧日期、十一周安排和旧进组假设不是当前游标。
- 通用基础模块：2026-05 的数学建模、博弈论、论文阅读、写作、科研方法和知识图谱库存；多处仍为概览／部分／旧路径，只作参考。
- Learning–Research OS：可作为 ownership、冷复测、先手作答和证据纪律的方法总则，不是具体课程。

### 4.5 Bridge 研究学习复用

Bridge 的研究学习复用审计已完成，但没有一项 `REUSE-AS-IS`。用户先做、分级提示、能力账本、论文拆解、闭卷／迁移、知识依赖图和成品深审都只能 `REUSE-WITH-ADAPTER`；旧的 Agent 代做后逆向训练不能作为当前对外发送依据。

L0 事实与范围 → L1 导师式提问 → L2 用户先做 → L3 分级反馈 → L4 所有权验收 → L5 证据与交付的组合骨架仍是 `PROPOSAL-SEED / UNAPPROVED`。具体模块、mentor contract、评分、日程、工具、freshness 与执行预算均未批准；Bridge 255 项来源库也不是现成课程包。

### 4.6 进组应用、OE-1 与 W0-W7 拓展

- jinzu-sprint 是学习和研究证据的下游应用面：收口 pitch、简历三件套、T5 和 OE-1；不能吞掉上游学习主线。
- OE-1 已有 α／β 两稿，BR-1 仅部分确认；仍等用户选择分支、填写 F1-F5 和决定投递。没有发送邮件。
- 进组包研究方法拓展：W0 完成；W1 部分；RS-A 是下一恢复点；W2-W7 受门禁。用户试用和个人证据只能由用户产生或确认。

## 5. 新 Obsidian／Research-Garden 实况

本地 vault：`/mnt/d/MyResearch/two-desks-trial-20260917/materials`。总入口：`learning/group-entry/README.md`。

- 286 份来源文件、6 个站点导航、来源说明、逐文件清单和链接检查已落盘。
- 资料仓 `main@f2e6a482ad83b0ae4c375ebcb23b9215b3cbd8d0`，上游 `origin/main`，ahead/behind 为 0/0，工作树和 index 干净。
- 远端：`git@github.com:Alkaid-9/Research-Garden.git`；`git ls-remote` 的 main 与本地 HEAD 相同。
- 此仓保存可阅读资料和导出，不保存 LearnGraph 数据库、运行缓存、模型密钥或 NotEMD 本机配置。
- 原 MAS 课程没有被移动；vault 中是 2026-09-17 的学习者快照。后续编辑不会自动回写原课程。
- 原资料仍记录 87 处库外、密封、历史失效或非标准引用；新总入口自身链接已检查，不能宣称全部旧引用健康。

## 6. 当前运行与 Git 状态

### 6.1 服务

| 服务 | 当前检查 | 含义 |
|---|---|---|
| 旧科研台 `127.0.0.1:8878` | HTTP 200 | 服务在线；保存路径仍是 `USER-TRIAL-RED / SAVE-NOT-REQUESTED / ROOT-CAUSE-OPEN` |
| LearnGraph API `127.0.0.1:18880/api/v1/health` | HTTP 200 | 本地试用 API 在线 |
| LearnGraph Web `127.0.0.1:18881` | HTTP 200 | 页面在线 |

在线只证明本次探测成功；不证明 NotEMD AI 抽取、真实学习对话或用户接受通过。

### 6.2 MAS 仓

- `master@479dc5b174026d10566b90123ef7c6bd542e560a`；相对本地已知 `origin/master` ahead 28，未 fetch，不能据此声称远端最新。
- 工作树包含大量其他窗口和用户修改、删除及未跟踪文件；本存档不清理、不暂存、不 reset、不把这些改动归为本任务。
- 今天 TASK-001 的合同／回执、用途提案、TASK-002 全局交接、OE-1 handoff 及多份日志仍是未跟踪实体；本任务新增的总 handoff／log 也保持未提交。
- 本任务只修改自己的 log、总 handoff 与两个共享 INDEX 的精确行；不 commit/push MAS。

## 7. 完成、部分完成、未开始的边界

### 已完成

- 2026-09-17 全部相关任务和进组包的证据化盘点；
- object／view 用途框架、两轮生长、工业权重和两底座分工已形成可讨论提案；
- NotEMD＋LearnGraph 本地可运行串接及 EdgeIM 技术路径验证；
- 全部现有进组学习包整理到新 Obsidian vault；
- Research-Garden 首次远端推送和 main 一致性复验；
- 本档、TASK-007 日志和恢复路由建立；TASK-002 漏挂 INDEX 路由补齐。

### 部分完成

- 三台产品：有运行切片和历史技术验收，但用户保存 RED、独立审、历史采收、完整多层网络与自动工作台桥仍开着；
- 进组研究拓展：W0 完成，W1 部分；
- ownership-v3：资产建成，学习和真正 ownership 未完成；
- OE-1：方案备好，个人字段和投递未完成；
- 学习资料引用：新入口可用，旧路径债仍有记录。

### 未开始／未获验收

- 用户真实 NotEMD 概念抽取和 LearnGraph 非空学习会话；
- 将试用底座正式重构成最终三台架构；
- P 批六包／EmoAgent 正式开考；
- ra26／ra28 逆向训练闭环、ra2716 EX-01R、ra30 EX-01→04；
- W2-W7、Bridge 组合骨架采用、完整工业跟踪自动化；
- 整理整个 `/mnt/d/MyResearch`；
- MAS 本批次 commit/push。

## 8. 推荐恢复顺序

以下顺序只说明依赖，不替用户做决定：

1. 学习线上，从六项恢复包继续，并回到 EX-05；这是当前唯一正式学习游标。
2. 底座线上，用一轮真实 NotEMD 阅读＋LearnGraph 学习验证保存、导出和问题种子，再决定架构适配。
3. 进组拓展线上，恢复 W1 的 RS-A，关闭 AC-W1-07 后再判断 W2。
4. OE-1 线上，用户选择 α／β并补 F1-F5 后，才形成可投递正本；发送必须由用户明确决定。
5. 三台旧产品线上，先精确复现并修正 8878 保存路径，再启动驾驶舱 P1a。
6. 待真实使用暴露结构问题后，再冻结三台界面、关系模型、菌丝网数据结构、工作台接法和正式仓布局。

## 9. 验收与未覆盖范围

- 本档由主线程复读关键权威文件，并用一个只读子代理独立盘点；子代理没有改文件或读取密封正文。
- 对 Research-Garden 核对了 HEAD、upstream、clean 状态和远端 main；对服务核对了 8878、18880 health 和 18881。
- 没有读取 `_sealed`、answer key、examiner 或正式口试正文；只按路径和公开说明登记边界。
- 没有 fetch MAS 远端，没有重跑全部历史测试，也没有视觉重开桌面 HTML。
- 本档是恢复快照，不重新授予产品、课程或个人能力 PASS。

## 10. 本次写入与回滚

- 新增本总 handoff；
- 新增 TASK-007 task log；
- 在 task log INDEX 登记 TASK-002 漏行和 TASK-007；
- 在 handoff INDEX 登记 TASK-002 全局交接和本总交接；
- 未修改课程、作答、Ledger、应用、数据库、服务、Research-Garden 或其他项目文件。

若仅撤销本存档，删除 TASK-007 log／handoff，并精确撤回本次增加的 INDEX 行；TASK-002 原始 log／handoff 和所有项目事实仍保留。
