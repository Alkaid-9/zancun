# 两台参考融入：第一轮需求对账与机制比较结果

日期：2026-09-15。任务：`TASK-20260915-010`。状态：`BOUNDED-FIRST-PASS / DESIGN-CANDIDATES / NO-INSTALL-OR-ADOPTION`。

> 续评更新：TASK-011已完成§9限定发送链核验，并形成[原段摘录窄合同提案](SOURCE_EXCERPT_PROPOSAL.md)。TASK-010及下文“本轮”仍指首轮；两轮均为静态核验／设计，不是软件实测。用户随后授权及时commit，第一批文档已存于`ac87186`；历史“未commit”保留其当时时点，未授权push。

依据：[详细计划与标准](REFERENCE_INTEGRATION_PLAN.md)、[唯一参考清单](REFERENCE_NOTES_20260915.md)、[本轮任务与检查](../../task_logs/2026/09/2026-09-15__research__reference-evaluation-first-pass.md)。用户已明确“继续推进／直接做／做”，本轮执行需求对账、只读机制与关键源码比较、结果落盘；不是再次只交计划，也不是软件接入授权。

## 1. 本轮结论与证据上限

**优先转化“带来源的摘录与回跳”；保留两台已有的版本、单次补学往返和选择导出。** PlanWeave先借鉴需求覆盖与执行／评审分开的做法；不新建第二任务正本。暂不把任一对话软件当多层知识网底座，不引入自动来源写回、模型调用、同步或新调度系统。

本轮有三项决定性发现：

1. ThoughtDAG的图上下文组装后还会插入记忆块；图上所选内容不等于完整模型输入。折叠、归档、导出也有不同语义。
2. TreeTalk-Obsidian的整树沉淀会尝试回写来源笔记，且回写错误被捕获；导出成功不能证明所有回链写入成功。单条回答保存与带来源摘录又是不同路径。
3. TreeTalkGPT固定提交的维护者订正说明明确否定旧`v0.2.3`作为所述迁移成功的证据；原交互思路仍保留，但本轮不能把当前库视为可直接接入的有效实现。

证据区分：外部README／订正说明＝维护者声明；关键函数＝本轮静态源码观察；A/B通过数＝既有回执记载，**本轮未重跑**；本件的场景推演＝纸面比较，**不是实测**。没有用户真实试用、独立复审或教学效果证明。源码引用固定提交，身份／许可继续由唯一清单登记，不建立第二候选库。

| 原计划阶段 | 本轮实际进展 | 未完成部分 |
|---|---|---|
| 1 需求对账 | 完成有界对账，11项均有处置；原教学遗留单列 | 不是全应用审计、全课程QA或官方考纲核验 |
| 2 机制／实现比较 | R07/08/09完成同场景静态首轮；R01/02完成任务检查场景首轮 | 模型各发送通道、导入事务／恢复、可信历史客户端等未查面保留；整个深评阶段不标全完 |
| 3 真实小样 | 未执行 | 真实材料、享做设备／版本与实际使用观察待补 |
| 4 融入决定 | 已形成原则借鉴与最小设计提案、反例和退出条件 | 无真实试用，不作正式采用决定 |
| 5–6 试点／施工 | 未执行／未授权 | 安装、真实资料、应用改动与部署分别确认 |

## 2. 两台需求与现有能力对账

应用核对基线为`research-desk`的`d53d188faff8e64ae9d22d92dd1eeab1b8309b84`加既有A/B未提交工作树；下面的本地源码坐标指该工作树，不能称这些功能已包含在HEAD提交。规划仓为`MAS_Safety_Project@f9f42db39be4286e6275ffbeb636ffae53e1f23e`。本轮未改应用、课程或真实库。

| 需求 | 已有／缺口判定与依据 | 对参考的取舍 |
|---|---|---|
| 完整来源集合检索、首次保存状态 | 已有A有界实现；[A回执§1–3](/mnt/d/MyResearch/research-desk/acceptance/a-TASK-20260915-002/RECEIPT.md:9)记录38/38及用户复验开放 | R02/R06不能把此项重新算作外部工具带来的增量；先用既有入口 |
| 同知识、不同目标的最低／正常／长期要求 | 已有B窄合同；[CONTRACT_DELTA:9](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md:9)分离goal、requirement、个人证据 | R03/R10只改善学习动作；不把参考阅读深度或手写量当本人达标 |
| 原尝试、帮助、反馈、研究判断及所引用版本 | 已有B记录语义；[合同:12](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md:12) | 不复制一套聊天评分系统；外部回答不是独立作答或研究证据 |
| 研究问题→补学→返回 | 已有单次往返；[bWorkspaceTools/bReturn](/mnt/d/MyResearch/research-desk/app/static/b.js:308)保留原身份及当时／当前区别；合同不允许嵌套branch_origin | R07/09可提供更细摘录定位；复杂嵌套另案，不重建已通路径 |
| 普通文本／PDF精确原段回跳 | **部分满足**：[_source_refs](/mnt/d/MyResearch/research-desk/app/research_service.py:73)可校验text_excerpt行字段，但[p1SourcePanel](/mnt/d/MyResearch/research-desk/app/static/app.js:1259)主要区分工作簿定位与整份来源；[b.js:325](/mnt/d/MyResearch/research-desk/app/static/b.js:325)对非工作簿显示原段未定位 | R09摘录及身份回跳是具体增量候选；不能因字段可存就声称UI已支持PDF页／任意原段 |
| 选定版本导出与外部引用缺口 | 已有[bExportPanel](/mnt/d/MyResearch/research-desk/app/static/b.js:370)及[导出合同](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md:32)；未含原文件／历史字节 | 保留现有v2；R07不能把普通Markdown包装成完整备份，R09不能隐式扩写来源 |
| 多层知识／科研网、跨层依据与影响复核 | **尚未建齐**，不在B1/B2完成范围；[设计入口:50](/mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/two-desks-delta-20260914/README.md:50)及B合同明确边界 | 借鉴对话层，不用对话父子、WikiLink或任务依赖替代知识／证据／指导实践层 |
| 明确本次模型输入、回放请求及隐私流向 | 本轮没有确认两台已有这项完整能力，A/B合同也不承诺；当前不接模型 | R07仅转化为后续设计要求；不为比较参考先建模型代理、请求日志或摘要hash平台 |
| 跨端手写、导出、备份与回链 | 享做厂商多端声明已登记；用户设备与实际行为**未知** | R10先留人工可读导出与原件引用路线；不假称已接入或同步可靠 |
| 环境、启动、日志、交付检查 | 已有solver预检、配置加载、链接检查、HTTP日志与A/B独立验收根，详见§5 | R02适合统一操作入口；不从“工程化”倒推出必须Docker／CI／通用trace |

四科仍为数三、英一、统计学、数据结构；2027年9月中旬结束积累，2027年12月初试。近期鲁侧，后续孙侧／工业OAI仅作阶段导向。不加入经济学、默认小模型课程、猜测预算或自动排期。普通探索不必先建任务或立即回流EdgeIM。

### 2.1 I01与早期课程遗留不能互相覆盖

本表对账的是**内容工作的待核／待修范围**，不是替课程重新验收。本轮只读公开文件与交接，没有读取sealed、重算数字或改学习状态。

| 遗留 | 本轮依据与当前判定 | 后续关闭需要什么 |
|---|---|---|
| I01独立QA | [交接:45](/mnt/d/MyResearch/MAS_Safety_Project/progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md:45)记录B-S3B三坐标通过，B-EVAL/CrossEdgeIM仅部分；正式回执仍列未开始 | 实际内容／验收逐项证据及审查者、过程、详细回执；本轮不复签抽样PASS |
| I01研究出口 | [交接:59](/mnt/d/MyResearch/MAS_Safety_Project/progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md:59)已查DROP/PARK/PROMOTE，桥接正文／交叉检查未完成 | 原任务核清授权后接Transfer Card消费者；不替用户作具体判定 |
| I01跨论文接线 | [交接:72](/mnt/d/MyResearch/MAS_Safety_Project/progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md:72)记录具体锚点及写域阻塞；本轮回查INDEX与TASK-20260906-004日志，状态仍不一致 | 原任务协调状态与写域，再接具体来源；本任务不修改该行或Sol写域 |
| 完整IM→过程树→Petri net→soundness教学 | [早期基线:48](../2026-09-14__research__multilayer-content-map-provisional-baseline.md:48)列为缺口；当前[B-S3B README:10](/mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/ownership-v3/edgeim/B-S3B/README.md:10)列补充层与来源边界，未由本轮证明完整教学兑现 | 有来源的解释、示范、渐进练习与不同结构验收；核坐标或标SOURCE-OPEN不能单独关闭 |
| 四篇各30分钟连续追问 | 早期基线明确D1总计30分钟不等于连续追问30分钟；本轮公开Markdown限定检索未找到新增计时安排 | 对应题面／追问脚本、独立计时、评分、记录与重做；未查sealed，不能把公开检索扩大为全包不存在证明 |
| 跨四篇D2 | 早期基线列执行资产缺口；当前公开START_HERE仍只提D1/D2执行时机，本轮未核见新的闭环证据 | 四论文跨篇题面、评分及记录入口；模块D+2/D+7不能替代 |
| QA总表、模块回执、共享入口一致 | 总表仍写BUILT/QA-PASS；I01仍保留AC-07消费者／回写待审；没有本轮独立关闭证据 | 按真实审查结果统一状态并链详细回执；既有QA-PENDING与新总表的时点关系需裁明 |
| EX-05真实卡点、三篇教学展开与App/CLI交接 | [早期基线:55](../2026-09-14__research__multilayer-content-map-provisional-baseline.md:55)保留未教先用、AI代码归属与遗漏联动等问题 | 用户真实小过程验证必要前置与返回点，不是更多表格／导出功能；学习效果保持开放 |

I01原件同时含“方案A已选定”与“等待批准”，独立性也有不同表述。本件记录差异而不选择有利句子当授权；单一commit本身不能证明是否独立审查。

## 3. ThoughtDAG与两个TreeTalk：同场景比较

纸面输入：问题Q引用材料r1的一小段；开补学分支K，再有一条无关分支U；排除U、导出Q/K、将来源改为r2，再返回旧问题。此为自拟无敏感DEMO描述，**没有创建对话或发送请求**。

| 动作 | R07 ThoughtDAG | R08 TreeTalkGPT | R09 TreeTalk-Obsidian | 两台应保留的区别 |
|---|---|---|---|---|
| 从原段追问 | 上下文组装能加入branchContext，并记录来源类别 | 用户介绍有框选追问；当前可信实现未核到 | 摘录payload含conversation/node/message；v2可带anchor并渲染来源链接 | 原文摘录、来源身份、提问和回答分开；不自动形成知识前置边 |
| 排除U | 折叠只是显示；归档节点在已查组装路径不贡献正文；引用深度还有独立控制 | 未确认，不能以演示介绍推断 | deposit状态排除节点会递归排除后代；投影用于沉淀范围 | 明确这是显示、下次输入还是导出动作；不因排除而删除原证据 |
| 送入模型 | 材料／引用／主线组装后，streaming还可能插入memory块，再调用llmCallStream | 发送实现未核 | 本轮只查沉淀／回链，未追到模型发送路径 | 不能依据图或导出内容宣布“模型只看到了这些” |
| 导出Q/K | JSON备份路径内联附件并带nodes/edges/events；Markdown路径只列附件名称、branchContext截前120字符 | 无可信当前导出实现结论 | 单回答只显式写标题＋回答正文；整树按投影导出并尝试改来源笔记 | 导出范围与完整备份分开；任何来源写回另行授权 |
| r1变r2／来源消失 | 上游指纹用于变化提示；不等于真伪判定或旧请求全文快照 | 未查 | 回链处理先找活动对话、再找历史，失败返回missing；不保证来源永久存在 | 当时／当前／缺失分开；不悄悄用r2替代r1，不据变化自动推翻结论 |
| 回到Q并研究判断 | 对话上下文可重新连接；本轮未验证研究／能力双评价 | 仅保留交互参考 | 对话回链可参考，但WikiLink不具备本地研究关系的全部语义 | 复用B单次往返，研究判断另写；不把AI回答或学习通过自动升格研究结论 |

### 3.1 R07的关键实现证据

固定版本见清单R07。本轮沿以下链路核对：

- [graph.ts:80–123](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/src/lib/graph.ts#L80)：`partitionContext`区分结构主线、materials和cross-link references；引用深度为quote/full，不能把所有边当同一关系。
- [context-builder.ts:285–349](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/src/store/context-builder.ts#L285)：已查路径跳过archived正文；折叠不裁剪；组装材料、引用、主线、选段及角色。这里只证明客户端组装规则。
- [streaming.ts:211–228](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/src/store/streaming.ts#L211)：普通生成在buildContext之后调用`memoryContextBlock`并插入messages；特定stepKind/digest例外。注释明确记忆不进入上游staleness指纹，故记忆改变不一定触发该过时提示。
- [streaming.ts:276–295](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/src/store/streaming.ts#L276)：调用`llmCallStream`，onDispatch记录摘要、数量、通道等元数据，**不是请求全文存档**；该回调错误被捕获。未继续审完API层、各provider、重试／图片替换、工具／agent通道，也没有抓取真实请求。
- [export.ts:42–69](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/src/lib/export.ts#L42)与[253–287](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/src/lib/export.ts#L253)：JSON和Markdown不是等价导出；前者的源码意图是自包含画布，恢复成功仍需实测；后者不能承担精确请求重放或附件备份。

处置：借鉴“可解释的输入选择”和“多种边各有职责”，不移植其运行时、不默认增加hash工作流／遥测。若将来实际接模型，需明确预览覆盖的系统提示、记忆、工具与附件处理，不能只显示图节点。

### 3.2 R09的关键实现证据

- [excerpt-drag.ts:204–228](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/knowledge/excerpt-drag.ts#L204)：`renderExcerptCallout`输出摘录文字和带conversationId/nodeId/messageId的链接，v2增加编码anchor。
- [source-link-handler.ts:28–73](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/navigation/source-link-handler.ts#L28)：校验身份／anchor，`openActive`或`openHistory`成功才返回opened，否则missing。本轮未审其所有UI适配器，不能保证每个锚点都高亮正确。
- [state.ts:55–73](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/relationship-graph/state.ts#L55)与[model.ts:201–218](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/relationship-graph/model.ts#L201)：前者写depositGraphState，后者生成includedNodeIds及允许边；这支持“控制沉淀范围”，不足以证明“同样排除模型输入”。
- [capture-service.ts:569–585](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/knowledge/capture-service.ts#L569)：单条assistant回答保存路径只额外写标题及message.content；不自动加结构化来源。回答原文偶然已有链接，也不能当该路径保证。
- [capture-service.ts:594–635](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/knowledge/capture-service.ts#L594)与[512–549](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/knowledge/capture-service.ts#L512)：整树沉淀按投影写文件，然后`updateSourceNotes`可能`vault.write`来源笔记；该函数捕获错误而不令导出失败。不能称整树导出只写目标文件夹，也不能据返回路径宣布回写全部完成。

处置：优先转化带身份的摘录回跳；本地先只写新产物及引用，不照搬来源笔记隐式写回。没有要求用户迁入Obsidian；本轮未测试私有历史永久删除、移动端或Vault迁移。

### 3.3 R08的有界结论

[PROJECT_SOURCE.md:18–25](https://github.com/safasffa111/TreeTalkGPT/blob/6b15e5bc428c36302e00069ed23036911e91a252/PROJECT_SOURCE.md#L18)是维护者对错误发布的说明；[47–49](https://github.com/safasffa111/TreeTalkGPT/blob/6b15e5bc428c36302e00069ed23036911e91a252/PROJECT_SOURCE.md#L47)明确旧backend/frontend等被移除，不能作为修正发行版的有效来源。这些是**来源订正声明**，不是本轮对ZIP、签名或迁移的实测。

保留用户所给问题树、框选追问、返回与知识引用的交互方向；本轮未定位可信历史构建，故不进入安装或实现移植候选。恢复评估的条件是找到可追溯的具体源码／发行来源并核对应关系，不是仓库更新时间“很新”。

## 4. R01：PlanWeave任务检查场景与取舍

纸面场景：一个获准的小包完成实现，评审要求修改；轮数耗尽、429或中断时，怎样回到既有任务正本？本轮没有创建PlanWeave包或启动Agent。

| 检查 | 已见证据 | 对我们意味着什么 |
|---|---|---|
| 原需求到执行块与消费者 | [plan-importer:53–84](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/skills/plan-importer/SKILL.md#L53)要求来源列表、目标覆盖、对象从创建到消费及失败路径 | 借鉴成下一批任务包检查，不靠任务数或“文件已建”认定交付；外部skill仅作为文档阅读，未安装／执行 |
| completed但未通过 | [reviewSubmission.ts:696–730](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/packages/runtime/src/taskManager/reviewSubmission.ts#L696)在轮数耗尽时返回completed＋needs_changes＋max_cycles_reached；[664–693](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/packages/runtime/src/taskManager/reviewSubmission.ts#L664)是passed分支 | 外部运行停止与本地验收分别记录。任何连接器只见completed就把任务转绿，都不符合本地需求 |
| 并发与写域 | [claimScheduler.ts:155–173](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/packages/runtime/src/taskManager/claimScheduler.ts#L155)按maxConcurrent减在途block计算容量；[importer:112–114](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/skills/plan-importer/SKILL.md#L112)说sharedResources只是提示 | 运行时在途block数不是本会话总人数；主控＋一个只读核验位仍为上限，不能把maxConcurrent=2当两个额外子代理；资源提示不替代写域与CAS |
| 导入说明差异 | [中文README:139–146](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/readme/README.zh-CN.md#L139)写draft校验／preview／import；[importer:29–51](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/skills/plan-importer/SKILL.md#L29)仍描述CLI返回路径后直接编辑包 | 这是同版文档路径差异，不据此断言哪个实现坏了；实际导入、覆盖、事务恢复需以后针对选定路径审源码／实测 |
| Git与恢复责任 | [DEVELOPMENT:39–41](https://github.com/GaosCode/PlanWeave/blob/21ea024eb23bd35d88f5183c9a2622d624ea5185/DEVELOPMENT.md#L39)声明不拥有Git分支/worktree/合并 | 本地任务授权、共享树、采收和最终验收继续由原机制负责，不同时引入TaskQuay与PlanWeave双调度 |

429与中断恢复在本轮只形成验收要求，未沿runtime完整重放。不能说PlanWeave能消除429、保证恢复不重复写入，或已通过本地独立评审。

**无需安装的可行方案**：下一批仍使用现有任务日志＋实际CONTRACT_DELTA＋集中回执；每项仅补齐原需求、输入／版本、写域、动作、消费者／产物、检查、失败后的继续点。现成字段够用，不再建立空模板库。应用技术状态、独立审查、用户试用分别写。只有实际任务暴露手工维护负担，才考虑单一只读小包的PlanWeave隔离试点。

## 5. R02：工程方法在两台的实际增量

| 检查面 | 当前可定位能力 | 不足／最小建议 |
|---|---|---|
| 环境与启动 | MAS的[AGENTS:13](/mnt/d/MyResearch/MAS_Safety_Project/AGENTS.md:13)规定solver预检；应用[load_config:66](/mnt/d/MyResearch/research-desk/app/research_desk.py:66)检查schema、loopback及root身份；[serve:1394](/mnt/d/MyResearch/research-desk/app/research_desk.py:1394)按显式配置启动 | 不新增环境管理平台；下一批操作页直接链原环境要求与所用配置，分清DEMO／真实库 |
| 来源与失败可见性 | [check_links:908](/mnt/d/MyResearch/research-desk/app/research_desk.py:908)检查已登记资产、引用、预览等；[HTTP日志:1390](/mnt/d/MyResearch/research-desk/app/research_desk.py:1390)及serve日志输出已存在 | 检查范围不是全盘内容质量；HTTP日志不是完整执行追踪。本轮未运行check-links或服务，不能报当前运行健康 |
| 隔离、复验与继续 | [B RUN_CHECKS:3](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/RUN_CHECKS.md:3)已有端口、环境、独立DEMO、依次复验及不覆盖旧结果说明；[50–72](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/RUN_CHECKS.md:50)有试用和恢复路径 | 无需复制doctor/CI整套系统。优先在新任务入口准确引用这些说明，不把旧run路径当可覆盖临时文件 |

工程评论的价值落实为“正确入口＋显式环境／写域＋可见结果＋可恢复回执”。Docker Desktop、Anaconda Navigator、JupyterLab、CI/CD、DevSecOps并不是一个必须一起装的包；当前没有证据支持因这条评论引入它们。OrbitStart的统一入口也需与现有页面／快捷方式比较后再决定。

## 6. 11项参考的本轮处置

“借鉴／转化”指评估结论与设计建议，不等于修改了课程、接入了软件或冻结新合同。

| ID | 本轮深度及处置 | 收益、限制与继续条件 |
|---|---|---|
| R01 PlanWeave | 机制＋评审／并发关键源码；**借鉴原则，软件暂缓** | 用原需求→消费者→验收检查下一批小包；导入事务／恢复和实际收益未核，不造第二任务正本 |
| R02 工程经验 | 与本地配置／日志／检查／回执静态对照；**借鉴原则** | 改善执行说明的精确引用；不增加无具体需求的基础设施 |
| R03 类比／复述／提问 | 用户材料＋既有教学缺口；**转为教学样板建议** | 先问已有基础，讲清类比适用与失效，再本人解释和独立变式；AI再回答不是事实核验，流畅复述不算独立掌握 |
| R04 OpenScience A | **身份待补／暂存** | 缺唯一地址，不猜项目；仅阻塞自身事实核验 |
| R05 OpenScience B | **身份待补／暂存** | 与A独立定位；“完全本地”和环境内置均未独立验证 |
| R06 OrbitStart | 继承固定README／许可有界核对，本轮未深审源码；**入口原则参考，软件暂缓** | 有实际切换负担再比较；脚本启动、Markdown写回与打开网页分开，未访问网盘 |
| R07 ThoughtDAG | 上下文→生成调用边界、两类导出关键源码；**转化设计** | 保留输入选择的可解释性；记忆／工具／provider链未全核，无实际请求证据，不移植运行时 |
| R08 TreeTalkGPT | README与PROJECT_SOURCE订正；**保留交互参考，停止当前安装候选** | 不删除用户参考；需可信历史源码／发行对应证据后再评实现 |
| R09 TreeTalk-Obsidian | 摘录／身份回跳／投影／写回源码；**优先转化摘录回链设计** | 不照搬隐式来源写回，不把单回答导出当来源保真备份，不强制Obsidian |
| R10 享做 | 继承厂商说明，设备与行为未知；**人工导出候选，试用待条件** | 先一页真实学习，再检查电脑可读、符号／笔迹、独立备份；稳定页链接未知，不开发同步 |
| I01 三缺口交接 | 本地合同／交接与旧遗留对账；**交回原内容任务** | 内容、独立QA、授权冲突分别处理，不被新工具评估关闭 |

## 7. 最小融入提案及反例验收

以下是本轮给出的具体设计成果。只推荐先审阅提案一；其余保留各自触发条件，不一次开四个施工包。

### 提案一：先做带身份的原段摘录与返回（优先）

范围：先选当前可读取、非保护的普通文本来源，解决“能保存出处但回不到原段”的局部缺口；不同时支持任意PDF、网页、享做深链接。先沿现有SourceRef／Revision核对能否表达，确有差异才写窄CONTRACT_DELTA，不预先冻结新schema。

候选动作：选中一段→看见并确认来源身份／当时版本／摘录文字→创建自己的新记录→补学或提问→返回该段。来源原文件保持只读；用户转述与原文摘录标明区别。摘录只是局部快照，不等于完整原件或论文结论成立。

影响位置候选：`app/static/app.js`的p1SourcePanel与来源记录入口，`app/static/b.js`的branch_origin消费；确需补字段校验时才涉及`app/research_service.py`。当前只是定位，**本轮未修改**。

拟验收：

- 同名来源仍能按资产身份分辨；重复段落不能悄悄选第一个作为原段。
- 材料r1变r2后同时说明当时摘录与当前可读取文本；未保存历史全文就明确不可复现。
- 无稳定锚点／来源缺失时显示未定位／缺失，保留摘录与出处，不假跳成功。
- 返回继续使用B原问题／视图版本规则，不覆盖后来正文，不自动新增supports／PASS。
- 只导出新记录时，列明未包含的外部来源；不偷偷写回原笔记。

无软件改造的比较基线：现有记录正文保留短摘录＋原路径／已知位置＋版本限制，人工打开原文件；若真实使用没有明显减少定位负担，维持此方式。试点回退为停止新入口、保留已保存记录及来源引用；具体patch回退应由未来任务定义，不恢复整个HEAD。

### 提案二：模型输入、可见画布、沉淀与知识关系各自明确（结构前置）

下一版涉及对话功能的合同必须回答四个不同问题：看见哪些内容；下次实际送入哪些内容；这次导出哪些内容；哪些关系获得研究依据。层内／跨层关系仍按自身语义解释，不是给同一张图换四个过滤器。

反例：隐藏U但它仍在请求里；沉淀排除U但它仍参与模型上下文；原段r1更改却用当前r2冒充旧依据；仅凭聊天父子就生成知识前置。四种情况应能解释或拒绝错误宣称，不能靠“回答看起来没用U”判断输入。未来获准接模型才检查最终发送边界及附加记忆／工具内容；本轮不为此创建自动记录或后台服务。

### 提案三：下一批执行包沿原正本做需求—消费者—验收对账（方法）

直接复用现有合同与回执：每项要求有执行动作、真正消费其产物的入口与可观察检查；已有技术验收、独立复核、真实用户试用分开。引用R01的状态反例，不接PlanWeave runtime。

反例：completed但review=needs_changes；文档只预填consumer而下游不使用；429无回执却标独立通过；A/B回归通过却把D2改完成。任一出现都不能关闭相应验收。失败只更新本任务待做／继续点，不改课程判定或别窗状态。无新执行平台也可完整执行此做法。

### 提案四：享做承载部分原始学习，学习台只收必要证据（设备就绪后）

候选路径：用户选一页当前鲁侧或四科学习→保留原笔迹与帮助条件→电脑可读导出→引用到已有attempt→反馈后另留重做，不覆盖原尝试。无需每页建节点，不要求先有科研问题；有研究价值的疑问再进入科研台。

拟验收：公式／图和页序可核、原作答仍在、OCR不冒充原件、导出可在离开软件后读取、独立备份可恢复。没有稳定页链接就使用明确文件／页号并注明限制。未提供平板系统／软件版本及真实小样前不判兼容或用户可用；同步与备份分别检查，不上传sealed或私人材料。

## 8. 收口、未查面与下一动作

本轮交付是集中评估结果，不是全参考深评完成：未运行任何上游应用／测试、模型请求、安装命令或研究实验；未迁移资料、修改应用／课程／sealed、commit／push。两台旧技术回执未重跑，不用历史通过数冒充本轮测试。

已按计划核对11项覆盖、关键源码与结论对应、原教学遗留未误关、链接／文件状态和本任务登记；实际文档检查结果见[任务记录](../../task_logs/2026/09/2026-09-15__research__reference-evaluation-first-pass.md)。本轮由主线程静态核对与自查；前序子代理连接失败不能充当独立证据，本轮不再重复派发。

下一步优先审阅提案一的范围；应用施工需单独确认该窄增量，再沿A/B合同建立实施回执。只读评估可继续核R01实际导入／恢复链或R07/R09的发送边界，但应由拟采用的机制决定是否值得继续，不无限扫全库。OpenScience地址、享做设备／版本、真实小样只阻塞对应项目。课程遗留返回I01和原内容任务，本件不裁定它们的授权与状态。

## 9. TASK-011续评：实际调用边界与摘录合同

### 9.1 ThoughtDAG：onDispatch不是网络字节／服务端后续上下文的完整证明

沿R07同一固定提交补读[api.ts:225–329](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/src/lib/api.ts#L225)：

- `245–247`：桌面Agent路径在onDispatch之后委托agentCallStream；该事件不证明Agent自身工具、会话或system上下文的全部内容。
- `249–269`：图片可先经imagesForModel选择；浏览器直连和代理路径分别调用onDispatch，再交directLlmStream／proxyStream。`279–305`还存在特定条件下去图片重试，因此一次用户提问不必只对应一次发送。
- `309–327`：浏览器到代理的实际JSON还含searchEngine、providers、harness等配置字段；onDispatch只覆盖其声明的消息／图片／模型／工具开关。不能称摘要覆盖HTTP完整请求，也不能证明代理到供应商没有附加内容。
- [streaming.ts:19–48](https://github.com/chenxiachan/thoughtdag/blob/3c57d429f83946498fce06d8e2a579c99f102e1e/src/store/streaming.ts#L19)定义了供图卡使用的另一次摘要llmCall；本轮只确认该函数存在和输入，没有审完所有调用触发点，不能声称每次问答都必定触发摘要调用。

结论加强为：正式接入前必须按实际选用通道区分“图上下文、客户端发给代理的内容、代理／Agent继续处理、辅助调用”。本轮不查凭据、不跑模型、不抓真实会话；未审服务端、direct provider实现及所有Agent路径，不能宣布全链隐私或回放通过。也不为两台新增请求遥测／hash平台。

### 9.2 TreeTalk-Obsidian：发送与沉淀不同，full模式也有预算处理

沿R09固定提交核对：

- [main.ts:873–997](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/main.ts#L873)：发送前冻结笔记上下文，失败提示本次未发送；当前这条入口设置contextMode为full，非Pi路径调用compileContextPlan，把messages传给ExecutionRequest。不是从沉淀Markdown逆推请求。
- [context-engine.ts:558–602](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/domain/context-engine.ts#L558)：沿会话路径组装消息和systemPrompt；[1538–1591](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/domain/context-engine.ts#L1538)在full分支仍调用笔记图正文预算／分配逻辑，返回noteContextTrimmed和用量差异。故名称full不保证所有关联笔记全文原样送出。
- [legacy-execution-engine.ts:158–173](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/execution/legacy-execution-engine.ts#L158)将contextMessages等交adapter.buildRequest，随后stream；本轮停在该适配边界，未核所有provider序列化、Pi工具或网络实况。
- 读到的compileContextPlan文件中没有depositGraphState引用，且首轮已见沉淀由独立投影控制；结合实际调用链，可以确认**已查路径不能把排除沉淀当排除模型输入**。这不是对所有插件模式的穷尽性证明。
- [main.ts:1482–1512](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/main.ts#L1482)在找到活动／历史来源后选节点并发布highlight；[selection-anchor.ts:103–155](https://github.com/safasffa111/TreeTalk-Obsidian/blob/09de5a6ea424a4ed32af0555c95540fa42bb806d/src/domain/selection-anchor.ts#L103)先核旧位置，再按quote、前后文和距离选候选，特定歧义返回unresolved。虽然创建anchor保存contentHash，所读resolve函数没有用它核整段历史版本；resolved不能当“原始版本已重现”。DOM渲染／滚动效果未实测。

补读context-builder.ts只作为类型及历史实现参考；实际main调用的是context-engine.ts，**未用旧buildProviderContext函数替代当前发送路径的证据**。

### 9.3 转化成两台的具体合同差异

[SOURCE_EXCERPT_PROPOSAL.md](SOURCE_EXCERPT_PROPOSAL.md)已给出：首批UTF-8文本整行区间、旧text_excerpt兼容、原摘录与本人正文分开、来源版本未知规则、窄读取接口、三写路径、避免来源缓存串段、多来源显式选择、当时片段／当前原位核对、v2选择导出、EXR-01–10及逐步施工／退出方案。

本地新增发现是`p1SourceKey`没有文本行区间／来源版本，而非只缺视觉按钮；`sources/asset`返回登记摘要，也不能给该摘要直接安上原文件行号。因此首批先按原位比较，不照搬TreeTalk启发式重定位，不新建完整来源快照库。当前仍为可审阅提案，未修改应用或创建测试数据。

R01实际导入／恢复、R06脚本与写回、R08可信历史实现、R04/R05身份、R10真实设备及用户试用仍开放。现有证据已足以提出该窄增量，不要求读完全部工具再决定；源码续评与独立复审也不是同一件事。
