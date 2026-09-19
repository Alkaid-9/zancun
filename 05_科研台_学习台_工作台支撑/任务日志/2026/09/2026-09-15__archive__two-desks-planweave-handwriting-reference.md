---
id: TASK-20260915-008
title: 两台三次输入统一参考清单与后续施工备注
date: 2026-09-15
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 托管会话未提供可确认的有效effort；交互式文档存档与只读核验
  launch: 当前交互式会话
type: archive
status: completed_with_open_gates
area: research-desk
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
  - progress/decisions/two-desks-delta-20260914/FIRST_BUILD_PLAN.md
---

# 目标

用户要求将PlanWeave评估存档并加入下一步施工方案作备注参考，同时询问平板／电脑使用享做笔记承担部分学习是否合适；后续追加工具／方法清单与TreeTalk迁移地址，最新明确要求三次输入先统一存档。本任务只存档、接方案路由和提供建议，不安装或接入任一外部软件，不启动试点／自动执行，不改课程、真实库或应用。

# 最终结果

三次输入集中于REFERENCE_NOTES_20260915.md这一份正本，§0共R01–R10十项：PlanWeave／视频、工程经验、学习方法、两款OpenScience、OrbitStart、ThoughtDAG、TreeTalkGPT、TreeTalk-Obsidian、享做。保留PlanWeave原有固定版本评估，补四个仓库的固定提交与有界阅读范围；两款TreeTalk并存，旧库停止维护与错误发布警告单列。OpenScience身份缺失、享做真实设备未测与外部声明均不冒充已验证事实。

同日用户续补ownership-v3执行交接，新增内部资料I01（清单§9）。当前合计11项：10项外部工具／方法＋1项内部施工交接；仍为一份参考内容正本，不复制源交接或改动其授权／状态。

# 修改内容

- 新增REFERENCE_NOTES_20260915.md，统一三次输入，固定已核项目来源提交并保存边界与待核项；只归档必要摘要与来源入口，未镜像视频、仓库或安装包。
- FIRST_BUILD_PLAN新增§9后续参考；README增加当前续作入口，不重写历史授权与A／B回执。
- 本任务与共享INDEX本任务行；不修改TODO／生成视图／外部配置／应用源码。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 用户授权边界 | 存档和参考不升级为安装／执行 | 主线程文档核对通过 | 参考备注§1、§5、§8；无应用写入或软件执行 |
| 来源可追溯 | PlanWeave固定提交、源码语义与未实跑声明明确 | 存档口径通过，非全源码审计 | 参考备注§2、§4、§7；新增四仓库固定引用与阅读范围 |
| 享做能力口径 | 厂商说明与设备／导出未测分开 | 口径通过，实际行为未测 | App Store id1642325772及备注§6 |
| 三次输入覆盖 | R01–R10齐全，两款TreeTalk分开，OpenScience不猜身份 | 10项及关键入口检查通过 | 统一清单§0、§7；Node一次性文档检查 |
| 方案双向接线 | README／首批方案可到备注且能返回 | 4文件、41个本地链接目标通过 | 来源目标存在性、§9目标标题、乱码／冲突标记／行尾空白检查；非外网全链接扫描 |
| 共享登记 | allocator签号，单行CAS，CRLF保留 | VERIFY-OK，其他索引字节保留 | 8899签发TASK-20260915-008；ledger_edit.py写后及--check通过 |

# 当前状态

本轮统一清单、施工备注、恢复入口与任务登记已完成；外部工具正式采用、身份补充和真实设备试用仍开放，不影响“参考存档”这一授权范围交付。无软件运行、安装、真实数据接入、commit或push。最高并发2，本轮由主线程处理文档和只读核对，未派发子代理。

# 尚未完成

- PlanWeave正式选型、试点与实测：不在本轮授权内，保持候选参考。
- 享做平板系统、同步／套餐、导出及备份恢复：待用户信息与真实设备试用。
- 两款OpenScience的唯一项目地址待用户补充；各候选完整源码、供应链、实际数据流和兼容性未审。旧TreeTalkGPT仍作设计参考，不推荐警告中的v0.2.3安装包。
- 两台此前的用户试用、独立复核、完整内容／多层网建设：本任务不代签、不改变状态。

# 下一步

1. 本轮按用户最新要求在统一归档后结束，不继续展开选型；后续施工先读唯一清单，按实际缺口借鉴，不把任一工具变成两台开工硬前置。
2. 若之后批准比较或试用，再补OpenScience地址、享做设备组合，选择一个小过程核回链与导出；不要先搬全库或开发同步接口。

# 可拓展方向

若用户批准，再分别建立PlanWeave隔离试点与手写产物接入小任务；不合并成整体平台重构。

# 风险与回滚

共享树已有他窗改动；只修改上述文档与本任务索引行。撤回时按本任务新增段／文件处理，不重置仓库或覆盖旧计划。评审轮数耗尽与真正通过必须分开，第三方同步不可冒充独立备份。

# 文件和产物

- progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
- progress/decisions/two-desks-delta-20260914/FIRST_BUILD_PLAN.md §9
- progress/decisions/two-desks-delta-20260914/README.md 后续参考指针
- 本任务和progress/task_logs/INDEX.md本任务行

## Amendment

### 2026-09-15：恢复核对与追加清单

- 恢复提示为`CONFLICT / wrong_repo`；实际启动位置是父仓库`/mnt/d/MyResearch`，文档工作仓库经`git rev-parse`确认是`/mnt/d/MyResearch/MAS_Safety_Project`，HEAD=`f9f42db39be4286e6275ffbeb636ffae53e1f23e`。
- 正式续作前重读本任务、两台方案README、FIRST_BUILD_PLAN及参考备注；README记载会话`01a09aa5-24c1-7233-868b-7426b5d94476`，与当前恢复标识相同。按文档绑定恢复本任务，不从父仓库cwd或自动摘要推定工作；未更改平台的恢复配置或伪造其状态。
- 用户最后两条补充：保留TreeTalkGPT并加入TreeTalk-Obsidian；三次输入合并一份参考清单。两条均已纳入，不延伸为安装／选型授权。
- 本轮无子代理，既有子代理错误状态不作独立核验证据；主线程直接核对远端引用、README和许可。一次只读抓取脚本因括号语法错误在联网前退出，修正后成功；无安装或仓库状态变更。
- 收尾：solver预检通过；4份文档检查通过。共享INDEX只新增本任务一行，程序断言删去该新增行后与写前内容逐字节一致；写后纯CRLF、bare-LF=0，CAS回读`VERIFY-OK`，末次登记SHA=`56796081a70d707317c878ff56bf48596ac6a58fea823793a5e37570960d3ef7`。该SHA仅用于既有共享登记并发核对，不是新设质量门；他窗续写后应重读，不把本值当未来恒定状态。
- 本任务只形成一份参考内容正本；另三份文档是方案指针／任务回执，共享INDEX是单行登记。未修改应用、课程、sealed、一苇渡江采集域或其他窗口内容；未运行应用测试，不宣称独立评审或用户试用通过。

### 2026-09-15：内部施工交接I01补录

- 用户转交TASK-20260915-007的ownership-v3执行交接及TASK-20260915-005方案摘要并说“还有这个”；按前一轮统一存档范围处理，不解读为补修批准。
- 已完整阅读两份原文；只读核对v3合同§8.1与AC-01–AC-10、Transfer Card枚举源段，以及TASK-20260906-004日志／INDEX状态。未重跑pdftotext、未检查sealed、不为原审查结论代签。
- 清单I01记录进展／未做／触发条件，明确B-S3B坐标抽样≠整体教学通过、AC-07仍待审、方案“已选定”与“待批准”的文字差异需恢复时核清。源文件和TASK-004／005／007索引行均未修改；本任务仍是参考归档完成，不是三缺口施工完成。
- 同步更新本任务方案入口、README指针和INDEX本任务行；4份文档、46个本地链接目标、I01新标题锚点、10项外部＋1项内部覆盖及空白／乱码检查通过。INDEX单行CAS回读`VERIFY-OK`，程序确认其他行字节保留；纯CRLF、bare-LF=0，写后SHA=`7e47258b426f6ec93e54f16ebbfda54562e4384fe90fa95c8bdb9d61e847520f`。未运行应用测试、未commit/push。
