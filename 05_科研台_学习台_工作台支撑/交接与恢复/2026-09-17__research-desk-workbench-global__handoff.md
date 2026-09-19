# 科研台、学习台、工作台与驾驶舱：全局总交接

日期：2026-09-17。任务：`TASK-20260917-002`。状态：`RECOVERABLE / PARTIAL-PRODUCT / USER-TRIAL-RED / WORKBENCH-AUTO-OPEN / COCKPIT-G0-COMPLETE`。

## 0. 全局结论

当前不是“全做完”，也不是“只有方案”。科研台／学习台已有可运行的C00-C03、A、B和N3人工接续切片，代码已提交；工作台WP0在隔离复合树达到历史TECH／CONTROLLER-PASS，但异构审、用户接受、精确采收和8899加载未完成；科研驾驶舱只完成G0事实与语义冻结，没有制作P1a页面。首次真实短试用暴露“保存请求未发出”RED，当前优先级高于新增界面。

## 1. 系统分层与唯一正本

| 层 | 职责 | 当前正本 | 当前上限 |
|---|---|---|---|
| 科研台 research-desk | 来源、问题、对象／版本、关系、研究工作区、研究判断 | `/mnt/d/MyResearch/research-desk`及其对象库／应用提交 | 有界功能可运行；完整科研网络、C04-C07和真实使用未完成 |
| 学习台能力面 | 目标要求、帮助条件、Attempt／Feedback、复测与个人证据 | research-desk B对象＋课程原合同 | B切片已实现；不能由DEMO或任务完成代签本人掌握 |
| 工作台 workbench-v2 | 任务、授权、依赖、CURRENT／EVENTS、评审、接受与运行事实 | MAS task logs／EVENTS／dashboard；WP0隔离树 | N3人工接续可用；自动桥仍关闭 |
| 科研驾驶舱 | 只读聚合项目、证据、阶段、开放门和下一步 | G0冻结件与驾驶舱方案 | G0完成；P1a/P1b及P2-P7未施工 |
| Skills | Skill身份、许可、输入输出和单次运行回执 | WP-S未来manifest／运行回执 | 方案点名不等于身份已核；有效运行回执源MISSING |

驾驶舱不是第四套对象库；科研台、学习台和工作台之间共享引用，不共享一个模糊PASS。

## 2. 已完成

### 2.1 科研台／学习台

- C00-C03已有来源、对象／Revision、工作区／View、关系、草稿、Attempt／Feedback、挂起、导出和专题往返底座；C03历史修复为`CONTROLLER-REPAIR-PASS / USER-RECHECK-OPEN`。
- A来源切片：来源集合选择／检索、首次保存反馈与失败恢复；代码与后续N2结果已采收到research-desk。
- B学习研究往返：goal、requirement、attempt、feedback、research_judgment、branch_origin及v2显式版本导出；应用提交链`b54ea71→c86f6d1→0b3a541`。
- N2限定复验历史结果：B 27/27、A 38/38、C03 22/22、后端28/28；这些是历史运行证据，不冒充本轮全量重跑。
- N3人工工作台接续：任务／产物普通引用、workspace/view/record身份返回、普通note保存，专项20/20；状态为`MANUAL-ONLY`。
- TASK-017两份合成来源、隔离配置和试用说明已提交；8878隔离服务当前可访问。

### 2.2 工作台

- 现有dashboard-v3／task logs／CURRENT／EVENTS继续是任务事实面。
- WP0 Lot A-E在隔离工作树历史达到：taskstore聚合138 passed、dashboard 490 passed、legacy 49 passed/1 skipped、golden 9/9及117/117字节一致；M4默认仍为warn。
- WP0实现包含任务读取／写回、事件先行、SQLite派生索引、漂移报告、M4写门和两个只读Task GET端点；这些仍是隔离树技术成果，不是主仓已加载功能。

### 2.3 驾驶舱与参考

- TASK-008设计基线提交`c85bba4`。
- G0-A至G0-E分阶段提交：`7b545c6`、`695e0e3`、`2d7815e`、`e21c7e6`、`6b21800`。
- G0已冻结三仓事实、实际B合同依赖、需求／权威矩阵、四类判定门＋正交运行事实、A/C/B内容身份、新鲜度和失败语义；四轮同谱系只读复核最终`SCOPED-READONLY PASS`。
- 统一参考清单现为R01-R12＋I01；R12 `agent-stack-notes@e17d0a8`只作方法参考，未接入关联实现。

## 3. 部分完成或未完成

| 项目 | 当前状态 | 尚缺什么 |
|---|---|---|
| 科研台真实使用 | `USER-TRIAL-RED` | 首次短试用没有发出POST／PUT保存请求；根因未定位，用户未接受 |
| A/B独立QA | `OPEN` | 旧代理429／中断无有效终态；需固定revision的小范围独立审及发现闭环 |
| B合同恢复 | `PRESENT-UNTRACKED` | `acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md`及相关回执未精确采收 |
| C04-C07 | `DESIGNED / NOT-DELIVERED` | 搜索、指导库、学习回流、失败／成果继承分别实施与验收 |
| EXR原段摘录 | `CONTRACT-ONLY` | EXR-01–10未施工；PDF/OCR和模糊锚点不在首批 |
| 完整多层网络 | `PARTIAL` | 容器和局部关系存在，真实内容、跨层语义、反转测试和长期使用未完成 |
| 工作台N3 | `MANUAL-ONLY` | 自动派发、状态回传、去重和失败恢复没有接入 |
| WP0 | `TECH/CONTROLLER-PASS / EXTERNAL-GATES-OPEN` | 异构审、用户accepted、精确所有权采收、commit/merge、8899 loaded revision、push |
| 工作台WP1+ | `NOT-STARTED` | WP0外部门关闭后才可FINAL化和施工 |
| 驾驶舱P1a | `NOT-STARTED` | 先修并完成真实最短路径观察，再单独授权静态验证件 |
| 驾驶舱P1b/P2-P7 | `NOT-STARTED` | 分别依赖P1a价值验证、合同与单包授权 |
| Skill运行计数 | `MISSING` | manifest、许可处理及有效单次运行回执合同／来源 |
| 历史证据采收 | `OPEN` | A/B合同回执、历史验收现场和其他未跟踪实体须按归属逐项分类采收 |
| 部署与远端 | `NOT-DONE` | 没有产品部署；本线没有push授权 |

## 4. 当前RED：保存没有发生

2026-09-17用户在`http://127.0.0.1:8878`首次短试用后反馈“没有保存”。现场核验：服务HTTP 200，PID 8705使用`acceptance/user-trial-TASK-20260915-017/config.demo.json`；日志只有GET，没有POST／PUT。只能判定`SAVE-NOT-REQUESTED / ROOT-CAUSE-OPEN`，不能归责用户、声称后端写入失败或把数据库文件存在当保存证据。

专项证据见[保存失败交接](2026-09-17__research-copilot-user-trial-save-failure__handoff.md)。该RED阻断P1a优先级：先修实际主路径，再做聚合页面。

## 5. Git、服务与恢复载体

| 面 | 当前已知身份 | 恢复注意 |
|---|---|---|
| MAS | `master@479dc5b`之后由本总交接形成限定文档增量；共享树仍有大量他窗修改 | index应保持空；只提交本任务路径／hunk；未fetch，不据ahead数判断远端最新 |
| research-desk | `main@0b3a54178e4ec58fb96eb8570101c44d94ac5687`；tracked代码干净，acceptance/data有未跟踪现场 | 无remote；不要clean或删除8878隔离data／log |
| WP0隔离树 | `codex/wb2-wp0-20260901-root@02da69bfd54f5a2fdfb70b6ae085c1178bfea43e`；33 tracked change、17 untracked入口的复合树 | 禁整树stage／cherry-pick；先按原回执逐hunk核归属 |
| 8878 | research-desk隔离DEMO，HTTP 200，PID 8705 | 当前故障现场；不重启、不清库，除非修复任务明确要求 |
| 8899 | `/api/version`可答，schema 4 | `service-up`不等于WP0已加载；loaded revision仍UNKNOWN |

运行数据、SQLite、日志和截图并非都由Git恢复。禁止把真实答案、sealed、无关数据库或完整会话加入Git来凑“全量存档”。

## 6. 接下来严格顺序

1. **修复用户主路径RED。** 取得失败页面／按钮／提示／截图，在同一8878隔离现场复现console、network和服务日志；冻结最小复现后另领修复任务。
2. **修复后只重试失败步骤。** 必须看到POST／PUT成功响应、对象ID／revision、刷新后可回读，并由用户确认结果能找到。
3. **完成A/B有界独立复核。** 固定`0b3a541`及实际合同范围，按file:line审权威、版本、冲突、失败和导出；不以机器测试代签。
4. **决定历史采收。** 先采B合同／回执等高价值恢复载体，再分类历史运行数据；不整树打包。
5. **再决定P1a。** 只有真实路径可用且用户认为聚合能减负，才另行授权只读静态驾驶舱；无收益就停放。
6. **WP0走原治理线。** 异构审→用户接受→精确采收／commit→受控8899加载复验；不得由驾驶舱或N3绕过。
7. **其余包分别授权。** EXR、C04-C07、P2-P7、WP1+各自有合同、测试、独立审和用户门，不批量开工。

## 7. 全局验收标准

- 科研台主路径：保存请求真实到达、响应成功、身份可回读、失败保留输入、用户确认操作可理解。
- 研究与学习语义：研究判断、个人能力、技术测试、独立评审和用户接受互不代签。
- 工作台：任务唯一、授权明确、事件可恢复、重复操作不重复派发、loaded revision可证明。
- 驾驶舱：只读、不建第二状态库；每个显示值回到对象revision、task/event内容身份或运行回执。
- 采收：归属清楚、限定commit、运行数据另行备份；不把未跟踪文件存在写成稳定恢复。
- 完整产品：至少一个真实非保护项目端到端走通，BLOCKER为零，独立审和用户接受按范围关闭；部署、push另行记录。

## 8. 新窗口第一动作

先读本页，再读保存失败交接、G0冻结件和WP0原交接。随后只读刷新三个Git根、index/worktree、8878日志和8899 version。第一项施工只能是8878保存路径的精确复现；不要先做P1a、自动桥、C04-C07或批量证据采收。

边界：不reset、clean、stash、整树stage；不改真实库、课程、sealed、答案或生成视图；不部署、不push；用户观察和接受不能代填。
