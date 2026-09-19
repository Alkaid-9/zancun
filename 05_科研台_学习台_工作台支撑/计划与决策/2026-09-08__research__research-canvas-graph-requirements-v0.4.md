# Research Graph／Canvas 需求规格 v0.4

日期：2026-09-08。关联：TASK-20260908-002、RD-1。状态：**REQUIREMENTS FROZEN FOR PILOT / IMPLEMENTATION NOT STARTED**。

用户已确认三项取舍：

1. 先用飞书／Miro 验证画布交互，再决定是否自建画布；
2. 索引可自动生成，关系／待办／特殊标记先由 AI 提案、用户确认；
3. 画布创建执行请求，工作台回传状态和结果。

本稿把科研台中的 Map、菌丝网络、任务线、任务卡、人—Agent 共同画布和工作台联动定义为一等工作面。它补充并修订[解耦架构 v0.3](2026-09-08__research__research-system-decoupled-design-v0.3.md)；不立即创建新应用、接入飞书／Miro、迁移资料或启动 TaskQuay。

## 1.1 完整科研 Map 的范围不能被画布模型压缩

上一版功能图只展示了“Graph 节点和关系”，没有展示现有科研 Map 的全部资产。这里明确：**Map 是完整的科研地图项目，不是几个论文节点，也不是菌丝网络的简化别名。**画布是访问和操作 Map 的一种空间界面，不能替代 Map 的范围、来源和层级。

现有 Map 至少包含：

| 范围 | 内容 |
|---|---|
| 8 层需求 | 分区图、脉络图、团队图、成果横向对比、困难清单、动向雷达、SOP／taste、领域工程实践 |
| L0／L1／L2 金字塔 | L0 全域分区，L1 细分方向与团队，L2 交叉带、竞争和候选问题 |
| W1–W7 波次 | 鲁侧三版图、孙侧版图、统一总图、拒稿情报、W5 数据化、W6 craft、W7 companion |
| 配套资产 | matrices、radar、surveys、oss_landscape、proposals、来源池和维护记录 |
| 七个学习／成长视角 | Knowledge、Method Landscape、Idea Genealogy、Transfer、Competency、Identity & Fit、Trajectory |
| 工作区资产图 | `/wbmap` 的跨仓资产定位；它与科研 Map 关联，但不替代科研事实和谱系 |

新系统的正确关系是：`Map Estate`（现有完整地图资产）→ `Map Registry／Graph Adapter`（稳定 ID、来源和关系索引）→ `Canvas Views`（任务图、谱系图、菌丝图、研究议程图等）。适配器只读接入旧地图并添加明确裁定，不把 W1–W7、矩阵、雷达、综述库、开源图和提案库合并成一张失去出处的大图。

## 1. 产品目标

科研台要同时支持两种思考：

- **树状展开**：从一条长期任务线拆到任务、子任务、论文、章节、概念和具体动作；
- **菌丝连接**：把不同任务线、论文、方法、反例、工具、证据和研究问题横向连接。

用户可以在画布上拖拽模块、分组、折叠、建立连接、添加备注和调整布局；AI 可以在旁边整理和提出连接；工作台可以接收选定任务的执行请求。空间位置始终是视图状态，正式关系必须有类型和来源。

## 2. 四个互相连接的产品面

| 工作面 | 中心对象 | 可做的动作 | 权威归属 |
|---|---|---|---|
| Graph | 节点、任务线、语义关系 | 建立／确认／撤回关系，查看证据 | `research-graph` |
| Canvas | 画布、布局、卡片、分区 | 拖拽、连线、折叠、快照、局部导出 | `research-canvas` |
| AI workspace | 提案、索引、标记、待办候选 | 批量整理、解释依据、接受／修改／拒绝 | 提案记录；正式结果回 Graph／records |
| Workbench bridge | 执行请求、日程、回执 | 安排任务、查看状态、打开结果 | 工作台／项目仓；科研台只保引用 |

一个对象只能有一个稳定 ID；多个画布通过 ID 引用它。画布不能成为第二套事实库。

## 3. 节点、边与任务线

### 3.1 节点类型

首批支持：`track`（任务线）、`task`、`subtask`、`paper`、`chapter`、`concept`、`method`、`question`、`evidence`、`artifact`、`todo`、`discussion_branch`、`person/team`。节点只保存自己的标题、状态、摘要和引用；长正文回到内容库或项目仓。

### 3.2 边类型

| 边 | 用途 | 是否默认需要依据 |
|---|---|---:|
| `contains` | 任务线包含任务，任务包含子任务 | 否，但需用户建立或接受 |
| `belongs_to_track` | 任务／卡属于哪条任务线 | 否，用户确认 |
| `prerequisite_for` | 一个概念／任务是另一个动作的前置 | 是 |
| `supports`／`contradicts` | 证据支持／反驳具体主张 | 是 |
| `derived_from` | 卡片或讨论由来源／会话产生 | 是 |
| `extends`／`alternative_to` | 方法、论文或设计的谱系／替代 | 是 |
| `blocks`／`unblocks` | 当前任务被什么阻塞或解除 | 是 |
| `reused_in` | 旧概念、代码或协议被实际复用 | 是，需实际使用证据 |
| `scheduled_as` | 画布任务对应工作台执行请求 | 是，带请求 ID |

视觉上的普通连线不自动产生语义边；用户可以先画草稿线，确认后选择边类型。

### 3.3 任务线模型

```yaml
id: track:edgeim-root
kind: track
title: EdgeIM 基础主线
status: active
goal: 建立全文 ownership 与表示方法基础
parent_track: null
task_refs: [task:edgeim-stage3, task:edgeim-full-paper]
next_task: task:edgeim-stage3
```

任务卡示意：

```yaml
id: task:edgeim-stage3
kind: task
title: Stage 3 cut 与递归
status: doing
track_refs: [track:edgeim-root]
source_refs: [src:edgeim-icws-2025]
blocked_by: [concept:recursion-input-output]
execution_request: null
```

一个任务可以属于多条任务线，但必须明确主线与辅助线；不因拖到某个画布就自动改变归属。

## 4. 画布交互与板类型

首版画布至少有三种板：

1. **Track Board**：以任务线为根，展开任务树、依赖和进度。
2. **Mycelium Board**：以一个问题或概念为中心，显示跨线论文、方法、反例、证据和研究候选。
3. **Collaboration Board**：人和 Agent 共同放置卡片、讨论分支、方案和待办，保留提案与修改轨迹。

通用交互：新建节点、拖拽移动、框选／分组、连线、选择边类型、折叠／展开、筛选状态、撤销／重做、版本快照、导出当前局部。布局数据与 Graph 边分开保存，导出时同时带节点 ID、边 ID 和来源。

任务卡旁边的工作区显示：当前状态、所属任务线、阻塞项、来源、下一步、AI 提案、执行请求和最近回执。日程安排属于工作台，不在画布内复制一套日历。

## 5. AI 提案与协作规则

### 5.1 可自动执行

- 对选定范围建立全文索引、标题、别名和来源定位；
- 更新索引版本和“未索引／索引失败”标记；
- 根据用户指定的字段生成搜索候选，不写正式关系。

### 5.2 必须提案后确认

- 新建或修改语义关系；
- 把卡片归入任务线、改变主线；
- 创建、关闭、延期或重新激活 TODO；
- 添加“阻塞、重复、待核、重要”等特殊标记；
- 改变研究状态、能力判断或来源身份。

提案必须包含：`proposal_id`、提案者、目标对象、操作、依据来源、解释、置信度（仅作排序，不是事实概率）和回滚方式。用户可逐条接受、批量接受、修改或拒绝；拒绝也保留原因，不从原记录删除。

### 5.3 讨论分支与挂起

一段对话先保存原文或明确标为摘要，再由 AI 提出 `discussion_branch` 分类：T／F／R／E、关联任务线、当前问题、待办候选和建议复查日期。用户确认后才进入正式 TODO 或关系。挂起卡必须保存挂起原因、恢复条件、下一次提醒和原始上下文。

## 6. 工作台联动协议

画布上的“安排执行”按钮创建一个请求，不复制整张卡：

```yaml
request_id: exec-request:2026-09-08-001
source_card_id: task:edgeim-stage3
question_id: q:edgeim-stage3
project_id: project:edgeim-training
input_refs: [src:edgeim-icws-2025]
allowed_write_domain: project-worktree-only
expected_outputs: [mechanism-note, scoped-test-result]
stop_conditions: [完成一个最小例子后停止]
acceptance: [用户能解释输入输出, 结果可回到来源]
status: requested
```

工作台回传：`run_id`、项目仓版本、实际动作摘要、状态、结果／失败、测试、产物链接和用户验收记录。科研台只更新对应 Evidence、Artifact 和任务显示，不接管工作台的 Git、命令和测试状态。TaskQuay 属于工作台连接器，仍先在独立沙盒完成闭环。

## 7. 飞书／Miro 验证方式

先不把任一产品定为真相源。用同一份小样本分别建立一张 EdgeIM Track Board 和一张 Mycelium Board，比较：

- 手写／拖拽／连线是否顺手；
- 一个新节点进入画布需要多少步骤；
- 任务卡能否清楚回到来源和任务线；
- Agent 能否读取指定范围并返回可审提案；
- 结果能否导出为带 ID 的 Markdown／JSON；
- 从画布创建执行请求并收到回执是否有额外重复劳动；
- 换设备、离线或网络不稳时能否继续工作。

飞书更适合作为多设备工作空间候选，Miro 更适合作为空间推理画布候选；这是待验证的产品假设，不是本稿的事实结论。MarginNote 继续承担 PDF 精读，不承担共同画布。

## 8. 验收场景

### A：手动画出一条任务枝

用户创建“EdgeIM 基础主线”，拖入论文、Stage 3 任务和递归概念，建立 `contains`、`belongs_to_track`、`prerequisite_for`；关闭再打开后布局和语义边都保留，搜索任务 ID 能定位原卡。

### B：菌丝横向连接与 AI 提案

用户把“DFG”连接到 Duplicate Task、对象中心和一个反例卡；Agent 对一段新讨论提出“可能属于 F、需要补图关系、生成一个待办”的三项提案；用户只接受其中一项，正式图中只有被接受的关系，原讨论和拒绝原因仍可追溯。

### C：共同画布到工作台

用户在任务卡点击“安排执行”，填写项目、写域、输入、停止条件和验收标准；工作台收到唯一请求，回传 `run_id`、版本和结果；科研台显示状态和结果链接，不把执行成功自动显示成能力已掌握或研究结论成立。

### D：挂起与恢复

用户把一条分支标记为挂起并设恢复条件；到期提醒只产生待处理事件，不自动重开研究状态；用户点击恢复后回到原卡、原讨论和下一步。

## 9. 实施顺序

1. **P0 适配试验**：飞书／Miro 各做同一小样本，记录交互摩擦和导出能力；不迁移全部资产。
2. **P1 语义协议**：在普通文件中落地节点、边、任务线、提案和执行请求 schema；先人工维护。
3. **P2 画布桥接**：把外部画布导出映射回稳定 ID，建立接受／拒绝提案流程。
4. **P3 工作台回链**：实现执行请求和回执显示；先接一个沙盒或低风险项目。
5. **P4 自建判断**：只有外部工具在手动连接、导出、权限或协作方面出现稳定 residual，才评估自建画布。

本稿通过需求审阅后，下一份实施任务应包含一个可撤销的样本板、导出文件和三项验收回执。没有通过 P0／P1，不创建独立画布仓或迁移全部科研资产。
