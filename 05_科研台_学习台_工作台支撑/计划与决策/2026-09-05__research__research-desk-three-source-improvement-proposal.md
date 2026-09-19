# 独立科研台：三源材料改进提案

**Date**：2026-09-05  
**Status**：`PROPOSED / NOT-FROZEN / DESIGN-ONLY`  
**Parent**：[独立科研台架构对齐检查点](2026-09-05__research__independent-research-desk-design-alignment.md)  
**范围**：用工作簿、研究操作符案例册和科研学习训练体系，补强独立科研台的对象模型、证据链、学习记录和界面路线。  
**当前边界**：不实现应用、不定技术栈、不修改工作台运行时、不把外部材料直接当成事实或答案。

## 1. 纠偏结论

三份材料分别回答三个问题：

1. **我收集了什么、当时怎么想？** —— 工作簿。
2. **我可以借用哪些研究动作，迁移时哪里会失效？** —— 操作符与横向迁移案例册。
3. **怎样把理解、操作、反馈、复测和能力变化记录下来？** —— 科研学习与训练体系。

因此它们是科研台的三种输入，不是同一层的知识。科研台需要保留原文和上下文，同时允许它们通过明确的转换进入研究对象：

```text
原始材料
  -> 摘录/观察
  -> 研究问题或候选 Claim
  -> Evidence 审核
  -> Map / Comparison / Decision
  -> 工作台任务或学习任务
  -> 结果与复测回链
```

其中 `候选`、`假说`、`UNKNOWN` 和 `已核对` 必须是不同状态。导入、抽取或 AI 建议不会自动完成状态提升。

## 2. 三源盘点与导入粒度

### 2.1 工作簿：原始摘录收件箱

本次只读检查得到以下盘面事实：

- 文件为 8,458,455 bytes，修改时间为 `2026-09-05 16:50:21 +0800`。
- 工作簿有 18 个可见工作表，没有发现隐藏工作表、公式、批注或定义名称。
- `Sheet1` 有 20 列，首行包含作者、单位、时间、题目、研究目的、贡献、方法、结果、局限、idea、novelty、感想、链接、文件、代码、备注、主题相关度和类型等字段；后部还有关于作者团队、论文河流、纵向/横向分析、读者与研究脉络的摘录。
- 其余工作表主要是单列长文本摘录；主题覆盖论文写作、科研问题、会议复盘、AI 使用、研究方向、组会表达、时间/精力/心智管理等。`Sheet7` 有 5 个显式网页链接；`Sheet14` 只有一个 GitHub URL；多个工作表含图片对象。

导入时不把一行或一个单元格直接变成 `Claim`。第一阶段只建立：

```text
WorkbookSnapshot
  -> SheetRecord
  -> CellExcerpt(sheet, coordinate, raw_text)
  -> UserNote(optional)
  -> CandidateTag(optional)
```

每个 `CellExcerpt` 至少带 `source_file_id`、工作簿 SHA-256、工作表名、单元格坐标、原始文本、导入时间和导入批次。原始文件保持可重新读取，结构化索引可以删除并重建。

### 2.2 操作符案例册：动作与迁移边界

案例册的最小可调用单位是操作符卡，而不是论文摘要。当前包括 8 张 `OP` 卡，四篇论文在主干训练中的角色，以及按“输入—关系—用途—保证—证据—成本”排列的 Agent 案例矩阵。

科研台应把它们拆成以下对象：

```text
Operator
  - operator_id
  - name / trigger_question
  - source_refs[]
  - original_mechanism
  - borrowable_action
  - non_transfer_boundary
  - minimum_check
  - evidence_ceiling

TransferCard
  - transfer_id
  - source_operator_id
  - target_object
  - shared_structure
  - mismatch[]
  - required_observation[]
  - prediction_or_obligation
  - minimum_check
  - evidence_state
  - reopen_condition
```

操作符可以被多个问题、论文和学习会话引用；迁移卡必须保存“不能对应什么”和“什么证据仍缺”，否则地图会把类比误显示为结论。

### 2.3 训练体系：学习与成长记录协议

训练体系正文标题为 `v0.3`，虽然文件名仍是 `v0.1`。它提出七张图、学习/探索/研究三个循环，以及调度状态、能力表现、证据状态三条分轴。科研台吸收的是记录协议，不把七张图实现成七套互相复制的数据库。

每次学习或研究会话只保存一条主记录，并由视图引用：

```text
LearningSession
  - session_id / date / object_refs[]
  - question / prerequisite
  - initial_prediction
  - action_or_operator
  - learner_artifact
  - feedback_refs[]
  - correction_or_update
  - delayed_retest
  - scheduling_state
  - capability_observation
  - evidence_state
  - next_action / reopen_condition
```

这样可以把“看过摘录”“能解释”“能亲手操作”“能改条件”“能迁移”分开，也能把一次失败与后续更新连起来。

## 3. 目标拓扑

科研台独立运行，拥有研究对象和证据关系；工作台拥有执行事实。三份材料先进入科研台的原始与候选层，经过用户确认或证据闭合后才进入稳定研究记录。

```text
                         ┌──────────────────────────┐
                         │ External sources         │
                         │ PDF / Web / Git / BibTeX │
                         └────────────┬─────────────┘
                                      │ capture + receipt
┌──────────────────────┐              ▼
│ Local material layer  │      ┌──────────────────────────┐
│ xlsx / md / pdf       │─────▶│ Independent Research Desk│
└──────────────────────┘      │                          │
                              │  Source & Excerpt         │
                              │  Paper / Note / Claim     │
                              │  Evidence & Review Inbox  │
                              │  Map / Comparison / Team  │
                              │  Operator / TransferCard  │
                              │  LearningSession          │
                              └──────────┬───────────────┘
                                         │ one-way promotion / deep link
                              ┌──────────▼───────────────┐
                              │ Workbench                  │
                              │ Task / Session / Git / Test│
                              │ Result / Delivery evidence │
                              └────────────────────────────┘

       Obsidian / Reviva
       Markdown / PDF / JSON / BibTeX
              ▲              │
              └── export/import adapter ──┘
```

### 3.1 权威归属

| 层 | 权威事实 | 可重建内容 |
| --- | --- | --- |
| 原始材料层 | PDF、网页快照、Markdown、BibTeX、工作簿及其哈希 | 不可由索引替代 |
| 科研记录层 | Question、Paper、Note、Claim、Evidence、Person、Team、Method、Relation、TransferCard | 正文与结构化关系需可导出 |
| 学习记录层 | LearningSession、学习者产物、反馈、复测和能力观察 | 七张图、能力摘要和轨迹视图 |
| 执行事实层 | Workbench Task、CLI/Agent session、Git、测试、实验结果和交付物 | 不由科研台复制 |
| 派生索引层 | 全文索引、关系图布局、统计、搜索缓存 | 删除后可重建 |

## 4. 最小对象模型

科研台的第一版对象不追求覆盖所有研究生活动，只需要支撑一条可回链主链：

```text
Question
  -> Source / Paper
  -> Excerpt / Note
  -> Claim
  -> Evidence
  -> Relation / Map view
  -> Comparison
  -> Decision / Experiment
  -> Workbench Task
```

对象共用稳定 ID，例如 `paper:edgeim-2025`、`excerpt:workbook1-sheet1-s12`、`claim:edgeim-c014`、`operator:op-05`、`transfer:edgeim-agent-001`。对象正文必须能指向原始文件、页码、单元格或运行回执。

关系至少带：`relation_type`、`source_refs[]`、`source_version`、`created_by`、`created_at`、`confidence`、`status`、`valid_time` 和 `revision`。状态建议为：

```text
candidate -> confirmed
          -> disputed
          -> rejected
          -> archived
```

人物、团队和机构关系另带关系类型与有效时间；论文合作、机构隶属、机制类比和个人推测不能共用一条无类型边。

## 5. 具体界面路线

第一版采用对象中心的三栏工作面，页面数量随阶段增长；不是先造一个巨型仪表盘。

### 5.1 收件箱 / 来源库（P0）

- 左栏：来源文件、工作簿工作表、PDF 和 Markdown。
- 中栏：原文、单元格摘录或 PDF 页面；保留原始位置。
- 右栏：创建 `Excerpt`、添加个人 Note、标记“候选问题/候选 Claim/待核来源”，显示哈希与导入批次。

验收重点：用户能看见“这句话来自哪个文件的哪里”，且重新导入不会静默覆盖既有摘录。

### 5.2 研究对象面（P0）

从一个来源进入 `Paper` 或 `Question` 后，中心显示对象正文与笔记；右侧显示证据、未决项、相关操作符和下一动作。AI 只生成候选摘要、实体或关系，必须经过收件箱审阅。

### 5.3 Evidence / Review Inbox（P0）

集中显示：待确认 Claim、来源版本冲突、AI 候选关系、同步冲突、缺少页码/单元格锚点的记录。每项提供 `confirm / narrow / dispute / reject / park`，并记录谁作出决定及依据。

### 5.4 Map（P1）

同一对象层切换 Knowledge、Method、Idea Genealogy、Transfer、Competency、Identity/Fit、Trajectory 七个视图。边的颜色或形状表达关系类型和证据状态，不能只表达“相似程度”。点击边必须回到来源或研究记录。

### 5.5 Operator Bench 与 Transfer Card（P1）

先选一个问题或对象，再选择一个操作符。界面显示触发问题、最小练习、不能照搬之处、证据上限和重启条件；完成后生成一张 TransferCard 草稿，而不是直接修改稳定 Map。

### 5.6 Comparison / Team Timeline（P1/P2）

横向比较的每个单元格都存 `claim`、测量、来源和量纲；论文自报、个人复算、推论和 UNKNOWN 分开。团队页把人物、机构、论文和有效时间分层，不能用推测关系填满时间线。

## 6. P0 真实使用流程

第一条真实闭环用一个具体问题验证，而不是同时做完整地图、自动搜索和团队图谱：

```text
导入一份来源（工作簿摘录或 EdgeIM PDF）
  -> 选定一个 Question
  -> 保存带位置的 Excerpt / Note
  -> 写一条带证据上限的 Claim
  -> 绑定一个 Evidence
  -> 选择一个 Operator
  -> 写 TransferCard：对应、不对应、预测、最小检查
  -> 在一个 Map 视图中显示关系
  -> 需要执行时生成 Workbench Task
  -> 把执行结果、版本和测试回链为 Evidence
  -> 延迟复测并更新 LearningSession
```

P0 的通过条件：科研台在工作台未启动时仍能打开、阅读、搜索和导出；一个对象能从来源走到 Note、Claim、Evidence、一个 Map 关系和一个导出文件；任何稳定关系都能回到来源或明确标为推论/假说/UNKNOWN。

## 7. 一步一步的实施路线

### 阶段 0：语义冻结与材料快照

**产物**：三源 manifest、输入哈希、字段词典、状态词典、对象 ID 规则。  
**检查**：文件名与正文版本冲突被记录；工作簿单元格锚点规则可复现；不产生正式 Claim。  
**停止条件**：任何字段的权威归属不清，先停在设计，不开始导入。

### 阶段 1：只读导入与 provenance 浏览

**产物**：来源库、工作簿 Sheet/Cell 浏览、Markdown 章节浏览、PDF 来源登记。  
**检查**：原始文件不被改写；同一来源可重复导入并发现版本差异；每个摘录可回到坐标或页码。  
**不做**：自动实体合并、自动建图、向量库锁定。

### 阶段 2：研究对象与证据链

**产物**：Question、Paper、Note、Claim、Evidence、Review Inbox；稳定 ID 与版本记录。  
**检查**：候选与确认分开；Claim 没有证据时显示缺口；导出 Markdown/JSON 后能恢复对象关系。

### 阶段 3：操作符与学习记录

**产物**：Operator、TransferCard、LearningSession；七图从主记录派生。  
**检查**：每张迁移卡包含不对应之处和最小检查；学习会话能记录先手预测、反馈、修正和延迟复测；不能把看过材料写成能力 PASS。

### 阶段 4：Map、Comparison、Team

**产物**：知识/方法/迁移/谱系等视图，比较矩阵和团队时间线。  
**检查**：同一关系不维护多份副本；关系类型、时间和证据状态可筛选；比较单元格保留量纲和来源。

### 阶段 5：三个桥接适配器

**产物**：

- `source file -> research desk index`；
- `research decision / experiment -> workbench task`；
- `workbench result -> evidence link`；
- Markdown/PDF/BibTeX/JSON 与 Obsidian/Reviva 的导入、导出和深链接。

**检查**：P0 不做任意字段实时双向覆盖；冲突进入 Review Inbox；桥接失败不会删除来源或覆盖研究记录。

## 8. 当前明确不纳入 P0

- 完整自动网页搜索和自动研究雷达。
- 复杂多人协作权限和实时协同编辑。
- 把 Obsidian 或 Reviva 的内部数据库作为科研台真相源。
- 自动推断人物关系、导师意图、论文新颖性或研究潜力评分。
- 用一次摘录、一次回答或一次迁移卡给能力或研究身份定论。
- 将操作符案例册中的所有论文同时变成必读任务。

## 9. 验收与回滚

阶段验收必须分别回答：

1. 原始材料是否保持不变并可重新定位？
2. 研究记录是否有稳定 ID、版本和来源？
3. 候选、确认、争议、拒绝和 UNKNOWN 是否没有混淆？
4. 研究台是否能脱离工作台完成阅读、搜索和导出？
5. 进入工作台的任务是否带着问题、范围、证据要求和回链？
6. 执行结果是否能回到产生它的问题和来源？
7. 删除派生索引后是否能从原始记录重建？

任何阶段不通过时，只回滚派生索引或候选记录，不删除原始材料、已确认研究记录或工作台执行事实。每次阶段结束要保存 manifest、验证命令、未决问题和下一步入口。

## 10. 下一步

下一步只做**阶段 0 的设计确认**：冻结三源 manifest 字段、对象 ID 规则、状态词和 P0 的一个真实问题。确认后再建立只读来源库；在此之前不写导入器、不改工作台、不接 Obsidian/Reviva 私有 API。

本提案与 EdgeIM 学习包的关系是：EdgeIM 可作为 P0 的一条真实研究闭环样例，但三份材料的归属是科研台的输入层；它们不会自动修改 EdgeIM 原题、答案、PASS 或学习者证据。
