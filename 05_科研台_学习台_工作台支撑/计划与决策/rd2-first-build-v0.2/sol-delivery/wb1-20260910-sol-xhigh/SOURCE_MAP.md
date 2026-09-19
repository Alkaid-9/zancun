# WB-1 真实来源映射：Sheet1 / Sheet18

状态：`complete`（文档包）；应用接线状态：`not implemented`。

## 1. 先给结论

本包从原工作簿独立解析显示表、关系表、单元格和 drawing，再与现有导出、资产登记和导航代码对照。六个选段的真实状态均为：

`原工作表存在且已逐格复核 -> JSON/Markdown 已完整提取这些单元格 -> 学习入口和全局搜索可找到表级资产 -> 尚未进入具体 P2/P3 工作区、知识/方法关系或真实使用回执`

因此，`extracted`、资产 ID、导航可见和关键词可搜索都不能写成“已融进学习/科研流程”。两个表的资产记录均为 `adapted=false`、`used=false`，科研指导库和继续点也都没有引用这两个 asset ID。

来源身份映射经 `xl/workbook.xml` 和 `xl/_rels/workbook.xml.rels` 解析，不按名称猜文件：

| 显示顺序 | 显示表名 | OOXML sheetId | relationship | 实际 worksheet | 资产 ID |
|---|---|---|---|---|---|
| 1 | Sheet1 | 1 | rId1 | `xl/worksheets/sheet1.xml` | `asset:workbook1:sheet:01` |
| 12 | Sheet18 | 18 | rId12 | `xl/worksheets/sheet12.xml` | `asset:workbook1:sheet:12` |

原件只读：`/mnt/d/Alkaid/Desktop/工作簿1.xlsx`。现有导出只读：`/mnt/d/MyResearch/research-desk/content/intake/workbook1/sheets/`。

## 2. 六段逐项链路

### S1-1：学术人际网络

- 原工作表：`Sheet1!S3`，短摘录：“建一张‘学术人际网络图’”。身份是作者给出的**方法/产品想法**，不是已核实的学术关系。
- 导出内容：`sheet-01.json` 保留 `S3`、值、类型；`sheet-01.md:29` 保留相同单元格和值；本包直接比较原件与 JSON，结果 `MATCH=True`。
- 导航入口：资产归入“学习与能力”，全局搜索“学术人际网络图”可命中 `asset:workbook1:sheet:01`；点开只显示表级元数据和复制 Windows 路径，没有 `S3` 正文预览、单元格直达或 P2 入口。
- 学习/科研用途提案：在 P2 的“团队/谱系”视角建立**待确认**的关系候选；每条边须带论文、作者页或用户观察等 basis。适合从一篇论文横向看团队与合作，不能由合作直接推断资源交换或研究动机。
- 当前状态/未知：仅提取、登记、可搜索；没有具体工作区、正式关系、用户确认或使用回执。未知项是关系真实性、来源范围和用户是否要采用这一视角。

### S1-2：纵向/同期分析

- 原工作表：`Sheet1!R6`，短摘录：“hv-analysis [论文小主题]（纵向研究追时间深度，横横截面研究追同期广度，最后交汇出判断。）”。原文中的“横横截面”照录。身份是**prompt/方法笔记**，本包未执行该 prompt。
- 导出内容：`sheet-01.json` 保留 `R6`；`sheet-01.md:34` 保留相同锚点和值；原件与 JSON 直接比较为 `MATCH=True`。
- 导航入口：在“学习与能力”表级资产或全局搜索 `hv-analysis` 可找到；仍只能到 Sheet1 资产卡，不能从结果直达 `R6`、P2 或原 Excel 单元格。
- 学习/科研用途提案：从某个真实论文问题进入 P2，分别建立“纵向谱系”和“同期比较”两个操作视角，记录已查范围、未查范围和依据；最后的判断仍是用户草稿。`L0/L1/L2` 只表示领域尺度，与“全局/专题/工作区”入口正交；进入 P2 不等于进入 L1 或 L2。
- 当前状态/未知：没有搜索计划、关联论文、覆盖记录或结论；未知项是专题中心、领域尺度、时间窗、同期比较集合及判断标准。

### S1-3：保存即时理解

- 原工作表：`Sheet1!S19`，短摘录：“即时的理解和感觉……读完之后，几十分钟内，马上写下来”。身份是作者的**经验/建议**，不是用户已经采用的学习规范。
- 导出内容：`sheet-01.json` 保留 `S19`；`sheet-01.md:46` 保留相同锚点和值；原件与 JSON 直接比较为 `MATCH=True`。
- 导航入口：搜索“即时的理解”可命中 Sheet1 表级资产，但当前界面没有自由记录、版本或工作区动作。
- 学习/科研用途提案：在 P3 为一篇具体论文保存 `original_reaction` 草稿，后来解释另建 revision/对象，不覆盖第一反应。适合读后快速捕获疑问、反例或方法联想。
- 当前状态/未知：没有用户草稿、论文引用、时间或反馈；不得据此写“已掌握”或提升能力状态。

### S18-1：手绘标注法

- 原工作表：`Sheet18!A14:A43`。短摘录包括 `A14`“方法一：手绘标注法（适合精读）”、`A21` 的标注 prompt，以及 `A31:A37` 对“AI 二手理解”和保留原文的解释。身份是**作者经验 + prompt + 未核理论解释**；本包不执行 prompt，也不采信“引导注意力”或学习效果为已证事实。
- 导出内容：`sheet-12.json` 与 `sheet-12.md:14-30` 保留这些单元格；直接抽查 `A14/A15/A17/A19/A21/A24/A26/A29/A31/A33/A35/A37/A43` 均 `MATCH=True`。
- 导航入口：在“学习与能力”或搜索“手绘标注法”可命中 `asset:workbook1:sheet:12`；没有段落预览、图片回链、P3 方法卡或实际试用记录。
- 学习/科研用途提案：在 P3 建一个**待确认的方法候选**，对用户选定的一页论文保存“原页引用、AI 标注稿、用户重画/解释、发现的错误与反馈”四个分离位置。适合精读单页公式或图表；是否提高理解须由真实任务反馈决定。
- 当前状态/未知：Sheet18 在 OOXML 中没有 drawing；`A17` 的 `image.png` 和 `A45` 的“图片”只是文字占位，实际图片不可从本工作簿恢复。故本段只能保留占位单元格位置，不能声称图片已保留。

### S18-2：分屏工作流

- 原工作表：`Sheet18!A48:A64`，短摘录为 `A48`“方法二：分屏工作流”、`A49`“左屏放原始 PDF，右屏开 Gemini 或 NotebookLM”、`A51`“不要来回切”。身份是**作者工作流经验**；`A60` 的“23 分钟”是未给出处的引用性主张。
- 导出内容：`sheet-12.json` 与 `sheet-12.md:32-42` 保留本段；直接抽查 `A48/A49/A51/A53/A55/A56/A60/A62/A64` 均 `MATCH=True`。
- 导航入口：搜索“分屏工作流”可命中 Sheet18 表级资产；界面当前不保存窗口布局或将来源与个人草稿并排。
- 学习/科研用途提案：P3 可把论文原文、助手草稿和用户笔记并列显示；这里只是工作区布局/偏好，不生成语义关系。适合需要反复核对原段落的阅读；实际效率与注意力影响待个人试用。
- 当前状态/未知：无实际工作区、布局、计时或反馈；`A53` 同样只是 `image.png` 文字，没有可保留的嵌入图。

### S18-3：区分创新、背景、假设的提示词

- 原工作表：`Sheet18!A78:A102`。短摘录包括 `A93`“核心创新点在哪、铺垫性背景在哪、哪些是作者的假设而不是结论”，以及 `A98:A102` 的四项提示词。身份是**prompt/方法观点**，不是对任一论文的已完成分析。
- 导出内容：`sheet-12.json` 与 `sheet-12.md:49-64` 保留本段；直接抽查 `A78/A83/A86/A93/A98:A102` 均 `MATCH=True`。
- 导航入口：搜索“哪些是作者的假设”可命中 Sheet18 表级资产；当前没有把提示词作为指导条目挂到论文工作区，也没有用户结果。
- 学习/科研用途提案：在 P3 把它改编为“原文定位 -> 论证链 -> 技术细节 -> 可疑假设 -> 用户复述/质疑”的可选方法模板，所有助手输出标 `assistant_draft` 并要求回链论文页码。适合首次精读或准备讨论；输出准确性、论文适配性和用户是否内化均未知。
- 当前状态/未知：仅可搜索。没有方法对象、关联论文、尝试、反馈、正式关系或使用回执。

## 3. 图片与原位置核对

| 表 | 原件事实 | 导出/登记 | 导航 | 学习工作区 |
|---|---|---|---|---|
| Sheet1 | 一个 `twoCellAnchor`，`xl/drawings/drawing1.xml` 关联 `xl/media/image1.png`；零基 from `(16,25)`、to `(31,64)`，即从 `Q26` 到 `AF65` | 二进制保存在 `content/intake/workbook1/media/image1.png`；coverage 保存起点 `Q26` 和 media member | 首页“工作簿原图”及“学习与能力”中的媒体资产可预览 | 未与 S1-1/S1-2/S1-3、论文工作区或方法对象建立关系；只是图片实体和放置起点已登记 |
| Sheet18 | `xl/worksheets/sheet12.xml` 没有 drawing relationship；只有 `A17/A53/A72` 的 `image.png` 与 `A45/A122` 的“图片”文本 | JSON/Markdown 保留文字占位，`drawing_members=[]`；没有对应媒体二进制 | 可按文字搜索表级资产，不能预览不存在的图 | 图片内容及其原始来源未覆盖；不得把占位文字升级成“图片已保留” |

Sheet1 导出目前只在 placement 台账中保存锚点起始单元格，未把完整 `Q26:AF65` 区间作为可回到原位置的 SourceRef；这是后续字段缺口，不在本轮改数据。

## 4. 三组语义必须分存

1. `L0/L1/L2`：领域尺度。它描述正在看多大的知识/研究范围。
2. `global/topic/workspace`：操作入口。它描述用户从哪里进入、正在做什么；P2 不自动等于 L1/L2，P3 也不自动等于 L2。
3. `View.positions/pinned`：拖拽与固定位置，只影响布局。
4. `goal_member`：目标归属，是明确的 typed relation；从目标移除不删除对象。
5. 其他 `Relation`：正式语义关系，有端点、类型、依据和 decision_ref；画线或拖动都不能自动创建。

AI 提案接受时，必须在同一确认结果里保存 `Proposal.state=accepted`、可见 `Decision` 和正式关系/正式变更，并一起返回引用；选“稍后”时正式关系不存在。此要求与现有 `DATA_CONTRACT.md:55-56,79-80` 一致，但尚无实现。

## 5. 对 DATA_CONTRACT 的五项局部补齐

1. **精确 SourceRef**：把 `anchor` 定型为可辨别的联合结构，至少覆盖 `sheet_name`、`sheet_id`、`worksheet_member`、`cell`/`range`；图片另含 `drawing_member`、`media_member`、`from_cell`、`to_cell`。解析必须沿 workbook relationship，不能用显示名推 XML。
2. **融合阶段与回执**：在资产覆盖之外记录 `nav_reachable`、`workspace_ref`、`knowledge_or_method_ref`、`attempt_ref`、`usage_receipt_ref`。只有后四者存在时，才能分别声称接入工作区、关联知识/方法、已试用；搜索命中不等于融合。
3. **尺度与入口分离**：View 增加独立的 `domain_scale`（L0/L1/L2/unknown）和 `entry_kind`（global/topic/workspace），均允许未选；不得用一个 `scope` 字段暗含两者映射。
4. **三动作分离交互**：拖动只写 View layout；“加入目标”显式写/撤回 `goal_member`；“建立语义关系”显式选择类型与依据后写 Relation。三个动作分别保存、分别撤销、分别显示状态。
5. **提案确认的原子可见结果**：保留现有 Decision + Proposal + Relation 同事务合同，并在界面一次返回三者引用；导出同时带提案状态与正式关系。SQLite + Markdown/JSON 导出、原资料原位是待审建议，本轮没有建库、迁移或改写任何资料。

## 6. 证据定位

- 导出：`/mnt/d/MyResearch/research-desk/content/intake/workbook1/sheets/sheet-01.md:29`、`:34`、`:46`；`sheet-12.md:14`、`:32`、`:49`。
- 表/图片映射：`/mnt/d/MyResearch/research-desk/content/intake/workbook1/coverage.json:18`、`:155`、`:238`、`:688`。
- 资产状态：`/mnt/d/MyResearch/research-desk/content/registry/assets.json:24707`、`:24739`、`:25331`、`:25363`。
- 导航事实：`/mnt/d/MyResearch/research-desk/app/static/app.js:27`、`:87`、`:119`、`:195`、`:334`、`:371`。
- 设计边界：`README.md:59`、`:85`、`:110`；`DATA_CONTRACT.md:32`、`:42`、`:55`、`:79`。
