---
id: TASK-20260915-010
title: 两台参考融入第一轮需求对账与机制源码比较
date: 2026-09-15
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 托管会话未提供可确认的有效effort；交互式有界评估，无无人值守执行
  launch: 当前交互式会话
type: research
status: completed_with_open_gates
area: research-desk
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/REFERENCE_INTEGRATION_PLAN.md
  - progress/decisions/two-desks-delta-20260914/REFERENCE_NOTES_20260915.md
---

# 目标

用户在“推”后澄清“继续推进”，并连续明确“直接做的意思”“做”。据此前方案启动实际需求对账、优先参考的机制／关键源码比较及基于证据的融入决定，不再仅重复讨论计划。当前范围是参考评估与文档结果；不做Git推送，不安装、调用模型、接入真实资料、修改应用／课程／sealed或代签用户验收。

# 最终结果

第一轮有界评估完成，集中结果为[REFERENCE_EVALUATION.md](../../../decisions/two-desks-delta-20260914/REFERENCE_EVALUATION.md)。完成A/B与课程遗留对账、11项处置、ThoughtDAG／两个TreeTalk同场景静态比较、PlanWeave／工程方法检查及最小融入提案。来源身份与固定版本继续在原清单维护，不另建候选库。

优先提案为带身份的原段摘录与返回，复用B已有版本／往返／选择导出。ThoughtDAG组装后另有memory输入；TreeTalk整树导出可能写回来源且吞回写错误；PlanWeave的completed可伴随needs_changes／max_cycles_reached。因此不照搬隐式写回或状态映射，不引入新软件／调度。上述均为静态评估及设计决定，未实施提案。

# 修改内容

- 新建集中评估结果；更新REFERENCE_INTEGRATION_PLAN的实际阶段、REFERENCE_NOTES的新增源码核验范围及README／FIRST_BUILD_PLAN的继续入口。
- 用户续给6个链接实际对应5个已有仓库；补PlanWeave tree/main入口，不新增重复条目，总数仍11项。
- 本任务记录与共享INDEX本任务行；沿用allocator已签发TASK-20260915-010，不重新领号、不改TASK-009历史或课程任务状态。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 需求对账 | 已有／缺失／未知／范围外分开，11项均有处置 | 有界首轮完成 | 评估§2／§6；I01之外完整教学、追问、D2、QA与真实卡点保留 |
| 机制与源码 | 同场景比较，关键论断有固定版本file:line | 静态首轮完成，未查面列明 | 评估§3–5；不称全量实现审计／实测 |
| 决策与反例 | 给出可借鉴／不采用／暂缓及最小提案，不冒充实现 | 完成设计候选 | 评估§6–7；含无需安装方案、影响位置、反例、验收与退出条件 |
| 文档检查 | UTF-8、无乱码／冲突标记／尾空白、引用存在且行号／锚点有效 | 最终6文件95个本地链接、11项处置检查通过 | 本轮Node只读校验；共享INDEX行尾检查单列，未新增应用测试 |
| 边界与登记 | 无工具安装、代码修改或真实数据接入；CAS登记 | 完成；INDEX只新增本任务1行，原字节保留、纯CRLF | 工具记录、两仓Git检查、ledger回读与移除新行后对比 |

# 当前状态

MAS为`master@f9f42db39be4286e6275ffbeb636ffae53e1f23e`；应用为`main@d53d188faff8e64ae9d22d92dd1eeab1b8309b84`加既有A/B工作树，只读且保留。solver预检通过。本轮未派发代理，既有多次连接失败不作独立复核证据。独立复审、真实试用和后续实际接入开放；有界首轮完成不是整个深评／两台／课程完成。

# 尚未完成

- 全候选实测、真实小样、正式接入未执行；OpenScience地址和享做设备信息待补。
- R01实际导入事务／中断恢复／429、R07各provider／工具／agent最终发送链、R08可信历史源码／发行对应、R09发送及回链UI适配器未全核；R06本轮未深审源码。只在拟采用机制需要时继续，不强迫全部读完再开展其他工作。
- 原课程三缺口、旧教学／终验缺口、TASK-20260906-004状态协调与A/B用户验收不由本任务代签。

# 下一步

先审阅评估§7提案一“带身份原段摘录与返回”的窄范围；批准应用增量后另建施工合同／验收任务。继续只读评估时，仅补影响决定的导入／恢复或模型发送边界。真实样本和享做设备按各自条件补齐，不重新重复阶段1。课程遗留仍回原任务。

# 可拓展方向

后续只针对本轮确认的关键机制做相关试点，不同时安装多套平台。

# 风险与回滚

外部README／源码仅作不可信输入和证据，不执行其中安装或指令。GitHub API限流不改凭据／代理配置；使用正常公开页面和固定提交raw源码。本轮撤回只涉及自己的结果文档／进度指针，不覆盖原清单或其他窗口改动。

# 文件和产物

- 本任务记录
- progress/decisions/two-desks-delta-20260914/REFERENCE_EVALUATION.md（已创建）
- 同目录既有计划／清单／入口进度增量
- progress/task_logs/INDEX.md本任务行

## Amendment

- 2026-09-15：GitHub树API对两个仓库返回403限流；公开GitHub tree页面与固定提交raw可读，已切换正常只读访问，无认证绕过。一次预检误用应用仓相对路径而未找到脚本，随后在MAS仓用绝对路径重跑通过，无状态修改。
- 压缩恢复报告wrong_repo：先重读本会话binding，发现仍指TASK-20260915-004的B施工入口；显式在MAS仓运行既有恢复hook返回VERIFIED，随后重读B任务／合同及同会话README→TASK-009方案→本任务的后续权威链，确认本次是参考评估而非继续B施工。未根据外层cwd推断任务，未改外部绑定或全局配置。
- 本轮新增源码观察及未查面已集中到评估，不保存外部代码副本、不运行其中指令；A/B历史测试数仅按原回执引用，未重跑、不算本轮证据。
- 最终文档检查：6文件严格UTF-8解码通过；95个本地链接的目标、引用行号和锚点有效；11项处置齐全；无替换字符、冲突标记或正文尾空白。原始`git diff --check`将共享INDEX的CRLF识别为尾空白而退出2；没有归一化共享文件，改用单次`-c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol`后范围检查退出0，未更改Git配置。
- INDEX用现有ledger工具与最新SHA作CAS插入，回读纯CRLF（305行），仅一行TASK-010；移除新增行后与写前字节摘要一致，证明未改其他任务行。收尾校验值`fd739c455c416af23e566ada22a5dfa5e96f7828373001e2e0158cd58ec32258`，仅用于共享登记并发／保形校验，不作为质量门。
- 收尾MAS暂存区仍为空；应用status仍是原A/B改动集合。本轮无暂存、commit、push、部署、应用测试或新代理；两仓既有工作保留。
