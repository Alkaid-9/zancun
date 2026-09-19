# 科研台施工蓝图 v0.1

> 2026-09-10 用户已选择 B／A／B／B／C。导航首版范围、Sol分工与验收以[执行方案](2026-09-10__research__research-desk-navigation-sol-execution-plan.md)为准；[Sol接手入口](2026-09-10__research__SOL_START_HERE.md)。此更新确认首版取舍，不表示整套历史蓝图已采纳或软件已运行。

日期：2026-09-08  
状态：BLUEPRINT / DESIGN-READY / IMPLEMENTATION NOT STARTED  
关联：TASK-20260908-002、RD-1  
依据：[解耦架构 v0.3](2026-09-08__research__research-system-decoupled-design-v0.3.md)、[Research Graph／Canvas 需求 v0.4](2026-09-08__research__research-canvas-graph-requirements-v0.4.md)、[学习科研体系运行方案](../audits/2026/09/2026-09-08__research-inventory/09_学习科研体系运行方案与新讨论整合.md)

本蓝图定义施工顺序和验收边界，不表示已经创建新仓、迁移资料、安装服务或批准服务器部署。

## 1. 施工目标

科研台是学习与科研内容的主入口，回答：

- 正在研究什么，为什么研究；
- 哪些来源支持当前理解；
- 知识、方法、问题、证据和任务如何相连；
- 用户本人、人机编排和 Agent 执行分别留下了什么证据；
- 哪些内容可以继续学习、进入研究、挂起或复查。

工作台负责盘点、协调和发起执行请求；CLI、Claude Code、Codex、TaskQuay 和项目仓负责具体执行。科研台不复制工作台的 Git、命令和运行目录。

## 2. 物理解耦

首版按职责建立六个可独立迁移的区域：

```
research-desk-app       UI、协议、适配器、索引器
research-knowledge     来源、学习记录、研究记录、Map 裁定、菌丝关系
research-projects       每个研究项目的代码、实验合同和产物
workbench-app           任务、日程、执行请求、回执
research-logs           追加式执行／应用／服务器日志索引
research-runtime        SQLite/FTS、缓存、队列和服务器私有配置
```

`MAS_Safety_Project` 保持历史工程与正式台账的权威，不在本阶段直接改造成新科研台。新区域先可在本机以分离目录验证，最终是否拆成远端仓由实际使用和权限需求决定。

## 3. 不再压缩的对象

以前容易被压成几个节点的内容，在施工时分别保留：

1. **Map Estate**：完整科研地图，包括八层需求、L0/L1/L2、W1–W7、matrices、radar、surveys、oss_landscape、proposals、来源池和七个学习／成长视角。
2. **Map Registry**：为既有 Map 资产分配稳定 ID、记录来源、版本、层级和维护状态。
3. **Graph**：正式语义关系和证据，不等于画布布局。
4. **Canvas**：布局、分组、折叠、拖拽、协作轨迹；可以有多个视图。
5. **Mycelium**：跨任务线的可复用连接、类比、谱系、反例和下一问题；不是百科全书。
6. **Learning/Research Guidance Library**：方法论和训练入口；先作为来源分层与调用适配器接入，不直接变成自动评分器。
7. **Logs**：研究证据、决策交接、执行事件、服务器运行事件分层保存。
8. **Capability**：Personal、Orchestration、Human–AI system 三层分开记录。

## 4. 拓扑

```
Map Estate ──> Map Registry ──> Graph Adapter ──> Canvas Views
                                      │                 │
                                      │                 └─ 人／Agent 协作提案
                                      │
                                      ├─ Mycelium relations
                                      ├─ Track/Task tree
                                      └─ Research agenda
                                      │
                                      └─ accepted execution request ──> Workbench
                                                                            │
                                                                            └─ CLI/CC/Codex/TaskQuay
                                                                            │
                                                                            └─ run receipt ──> Evidence/Artifact
```

唯一事实对象由稳定 ID 标识。画布位置、颜色和折叠状态是视图数据；正式关系、任务状态、来源和证据回到内容库。工作台回执只通过 `run_id`、`evidence_id` 和产物引用回链。

## 5. 内容库最小模型

每个对象至少有 `id`、`kind`、`title`、`revision`、`created_at`、`status`。跨库引用只用稳定 ID和相对引用，不写绝对路径。

首批对象：

- `source`：论文、讲义、会话、网页、代码版本；
- `learning_session`、`observation`、`research_question`；
- `track`、`task`、`subtask`、`todo`；
- `concept`、`method`、`evidence`、`artifact`；
- `mycelium_card`、`discussion_branch`、`person/team`；
- `map_asset`、`map_decision`、`proposal`。

工作状态、本人能力证据、研究判断是三个独立状态轴。AI 摘要、用户原话、原文摘录、代码结果和人工核验不能混为同一种来源。

## 6. Map 与画布施工

### 6.1 Map Registry

第一阶段只读扫描 W1–W7 及配套目录，为每个地图资产登记：

```yaml
id: mapasset:w6-craft:method-card-001
estate: W6_craft
kind: map_asset
source_ref: file:research/map/W6_craft/...
layer: methodology
status: observed
supersedes: null
```

Registry 不改变原地图文件。冲突、重复、来源不明和历史推断进入 `map_decision`，由用户确认后才提升为正式关系。

### 6.2 三种板

- Track Board：任务线→任务→子任务→论文／概念／执行动作。
- Mycelium Board：一个问题为中心，展开跨线方法、文献、反例、证据、类比和研究候选。
- Collaboration Board：人和 Agent 放卡片、开讨论分支、提待办，保留提案、修改和拒绝轨迹。

画布支持拖拽、连线、分组、折叠、筛选、快照、撤销／重做和局部导出。普通连线先是草稿，确认边类型后才成为 `supports`、`prerequisite_for`、`extends`、`contradicts`、`blocks` 等正式关系。

## 7. 科研指导库接入（施工附录入口）

以下四行是早期来源分工摘要；完整六层目录及pengsida跨层映射以指导库融合规格为准：

| 层 | 主要来源 | 在科研台的落点 |
|---|---|---|
| 导航 | Luo PDF 等研究入门材料 | 问题卡、What/Why/How/So What、广度到深度 |
| 提问与审查 | Supervisor-Skills、导师经验材料 | 反问清单、假设检查、图表和论证检查 |
| 实验与调试 | pengsida／research_growth 的实验与 debug 方法 | prediction、toy、good/failure case、一次只改一处 |
| 事实与所有权约束 | Learning–Research OS、来源登记和冷启动 | provenance、claim ceiling、用户先做、能力证据 |

首版按上下文调用并记录来源。详细字段、来源去重、学习／协作研究／执行三种模式、系统性科研与成果继承，见[科研指导库融合规格 v0.1](2026-09-08__research__guidance-library-integration-spec-v0.1.md)。这份适配草案已写，尚未进行实际使用和应用接入。指导库不能因作为“方法适配层”而丢掉 pengsida 跨阅读／创新／实践／写作／协作的完整经验库、W6 领域实践、研究议程、成果系列、复用及下一问题。

## 8. AI 与权限

索引、标题、别名和来源定位可以自动生成。语义关系、任务线归属、待办、特殊标记、研究状态和能力判断必须先形成 proposal，用户接受后写入正式记录。提案保留依据、解释、置信度排序值、修改／拒绝原因和回滚入口。

## 9. 工作台桥接

“安排执行”只创建一个执行请求，字段包括问题、输入来源、允许写域、预期产物、停止条件和验收方式。工作台回传 `run_id`、版本、命令摘要、测试、结果／失败和产物路径。执行成功不自动推出个人能力掌握或研究结论成立。

TaskQuay 先作为工作台侧连接器，在独立沙盒中完成真实委派闭环；扩大目录、远程隧道和手机账号接入另设决策门。

## 10. 编辑器和操作入口

当前建议：

- Cursor Desktop：主要用于浏览、跨文件搜索和代码审查，授权范围限制在 app／协议／适配器代码仓；
- VSCode：保留为通用编辑和调试后备，不先做大规模定制；
- CLI、Claude Code、Codex：执行和自动化的主入口；
- 外部画布（飞书／Miro）：只做 P0 交互试验，导出必须带稳定 ID；不成为第二真相源；
- MarginNote：继续承担 PDF 精读，不承担图谱和任务状态管理。

只有当 Cursor 的索引、隐私排除、WSL 路径或审查回链形成可重复痛点，才加工 VSCode 或开发专用扩展。

## 11. 施工阶段与验收

### P0：协议与小样本

选 EdgeIM 一篇论文、一条真实学习记录、一个开放观察和一张任务树；手工建立 source／task／concept／evidence 四类对象，验证稳定 ID、相对引用、关闭重开和导出。

### P1：Map Registry 与指导库适配

只读接入 W1–W7 的资产；建立指导库来源层、调用阶段和一页操作卡；验证不复制大文件、来源可回溯、提案可接受／拒绝。

### P2：画布试验

在飞书和 Miro 各做一张 Track Board 与一张 Mycelium Board，比较拖拽、连线、折叠、导出、恢复和协作摩擦。选择依据是实际残余问题，不预设自建。

### P3：科研台最小应用

实现保存／重开／中文搜索／索引重建／局部视图；普通文件为权威，SQLite 为派生索引。

### P4：工作台回链

从任务卡创建一个低风险执行请求，接收回执并将 evidence/artifact 回链；不复制运行目录。

### P5：迁移与服务器

本地快照可恢复、权限和备份策略确定、恢复演练通过后，才迁移更多资料或部署服务器。

最低验收不是“页面能打开”，而是：一个对象可从来源到画布、从画布到任务、从任务到执行回执，再回到证据；关闭重开和索引重建不丢关系；拒绝的 AI 提案不污染正式图；用户能力与系统产出仍分层显示。

## 12. 当前开放门

这些不阻塞蓝图成稿，但在对应阶段前必须决定：

- RD-G1：科研指导库来源分层、调用路由与能力边界已形成规格草案；来源逐项适配、三条配方样例、实际试用及应用接入仍待做；
- RD-G2：独立目录／仓库的最终命名及哪些资料首批迁移；
- RD-G3：飞书与 Miro 的首轮样本和导出格式；
- RD-G4：Cursor 审查范围、VSCode 是否需要定制；
- RD-G5：服务器同步对象、访问者、备份频率和成本上限；
- TQ-1：TaskQuay 沙盒委派与远程接入是否分开推进。

本蓝图先作为施工总图；任何代码、迁移、外部连接和服务器动作都要在对应阶段形成单独任务和回执。
 
