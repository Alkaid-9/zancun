# 对象、关系、布局和保存合同（待审）

2026-09-10 · v0.2-DRAFT。下面字段与接口是给实现者评审的候选，不是现有应用能力。演示数据见 [sample.json](sample.json)。

## 1. 权威边界和存储建议

原论文、讲义、Obsidian笔记、旧Map仍在原位，各自是其正文来源。新对象/个人草稿/决定/关系集中保存；资产扫描器只生成索引。新对象引用旧asset_id，另带来源锚点；移动原件导致引用失效时显示“需重新定位”，不能靠同名自动认领另一个文件。

**建议修订v0.1：新编辑数据使用本地SQLite，正文为Markdown字符串，JSON作为交换包，Markdown作为导出。** 理由：接受提案要同时更新提案、决定与关系；SQLite事务比自建多文件提交机制更直接，可使用现有Python标准库。此为待审选择，本轮不创建数据库、不改配置。

替代方案仍是Markdown/JSON文件权威，便于外部编辑；若选它，须先确定跨文件确认、并发冲突及恢复合同，不能悄悄用多个覆盖写声称原子提交。导出文件不能与数据库同时被宣称为自动双向同步的唯一正文。

| 内容 | 候选落点 | 维护方式 |
|---|---|---|
| 代码、脱敏样例 | 独立research-desk代码范围 | 小范围版本管理；分仓待定 |
| 原资产 | 各原资料库/项目仓 | 只读引用，本批不迁移 |
| 新对象、关系、可见修订、布局 | 用户单独指定的数据根中的desk.sqlite3 | 应用统一读写；原文不是缓存 |
| 人机可见讨论/失败/决定 | 上述研究记录 | 不按运行日志轮转；不索取模型隐藏思维 |
| 运行日志/缓存 | 独立运行数据根 | 不成为科研内容权威，本批不新增日志平台 |
| 手机/其他账号文件包 | 用户主动导出的指定目录 | 自包含清单、选中内容、继续点；无自动上传 |

路径需在现有配置中显式指定，不能硬编码到MAS或shell环境变量。实际机器路径、备份落点和代码Git范围在开工选择中固定。

## 2. 最小模型

| 实体 | 最小字段/含义 |
|---|---|
| Object | id、kind、title、body_md、revision、author、source_refs、attrs；标题可自动取首行 |
| SourceRef | source_id、anchor（可辨别联合，按kind分流：workbook_cell/workbook_range覆盖sheet_name、sheet_id、worksheet_member、cell或range；workbook_image另覆盖drawing_member、media_member、from_cell、to_cell；解析须沿workbook relationship定位实际XML成员，不由显示表名或编号推断）；真实旧资产由来源绑定解析；示例只用demo来源 |
| Workspace | 本质是Object(kind=workspace)，attrs记录关注范围/对象引用；继续点见视图状态 |
| Attempt/Feedback | Object子类；feedback.attrs.attempt_ref明确对应哪次尝试；归因可unknown |
| Relation | id、from、to、type、basis_refs、decision_ref、revision；正式语义独立于布局 |
| Proposal | id、operation、payload、basis_refs、target_revisions、state、decision_ref；pending/accepted/rejected |
| Decision | 作为Object保存可见决定/解释与操作者；接受后关联正式产物 |
| View | id、scope_refs、members、mode、positions、pinned、collapsed、selected、resume_note、revision |
| Revision | 对象的明确保存/决定快照与更正说明，不记录每次按键 |

> **2026-09-10 amendment（依据 WB-1 两份独立交付共同诊断，见 `sol-delivery/COMPARISON.md`）**：原`anchor`仅为单点字符串，无法表示"表内区间"（如图片锚点`Q26:AF65`）与"嵌入图片"两类不同来源，也未要求沿workbook relationship解析实际XML成员——真实核对时（Sheet18显示表名与底层sheetId/rId不一致）暴露这一缺口。上方SourceRef行已改为按kind分流的联合结构。此前产物（`sample.json`及两份WB-1 WALKTHROUGH.md中的示例JSON）仍用旧扁平写法，本次未回填，读者遇到不一致以本表结构为准。此修订只改设计契约文字，不涉及应用代码（当前无写入实现）。

全局稳定ID由系统生成；示例使用DEMO前缀。kind首批只实现问题、笔记、概念、演示资料、方法、目标、工作区、尝试、反馈、决定与TODO所需行为；团队/产品/论文等后续类型可引用，不能为每种kind先造一套复杂模块。

正式边候选：references、prerequisite、method_analogy、historical_influence、complements、goal_member、feedback_on、result_of。正式不等于“学术结论为真”：边的证据状态仍可为用户联想/待核/来源支持。用户可以正式保存“这是我的未验证联想”，不得把它显示成既定因果。

树的展开路线属于view；真实学习依赖/目标归属属于typed relation；无类型草稿线属于view.draft_edges。拖动不创建关系，所属视图也不自动等于所属goal。学习依赖可能多父节点；每次展开必须可回到前一个中心，不强制把网裁成单父目录。

## 3. 2D/3D和个人状态

同一View语义范围可有2D和3D布局快照，key为view_id+renderer。共享对象选择，分别保存位置/缩放/相机；3D相机字段在选定渲染器后细化。未知坐标不编成知识高度。用户固定位置和未固定自动布局分开。

能力不由Object数量、AI操作次数或已读状态推算。个人表现记录需指定任务、帮助条件、本人可见产物、反馈依据与时间；首批只保存描述，不运行自动mastery投影。研究结论、任务执行状态、来源核验、个人表现是四个不同字段域。

## 4. 保存与确认

1. 自由捕获仅要求非空正文或一个引用，生成Object r1。不要求来源完整、goal或分类。
2. 保存带expected_revision；保存成功返回新revision。旧版本冲突返回当前revision和可比较内容，保留当前编辑草稿，由用户处理。
3. 人手建立关系需要明确类型/端点；依据可说明“个人联想，待验证”。不是所有关系都必须先找到论文。
4. AI索引更新可以自动；关系、待办、标记、归属均产生pending提案。接受在一笔事务内保存Decision、正式变更及Proposal accepted；拒绝保留其依据与决定。
5. 重复提交同一已接受提案返回既有决定及产物引用，不创建第二条边；过期target_revisions需重新比较，不默默改目标。
6. 修改解释新增revision；反馈指向具体尝试；删除视图成员只改membership，撤回正式关系保留历史。硬删除/全面同步策略不在首批。
7. 挂起保存选择、展开、位置和可选继续说明；没有变更不生成空历史。重建索引不写人工记录域。

## 5. 候选API与可审请求

新路由放在`/api/research/`，与现有asset预览路径分开；尚未实现。所有写接口只写新数据根，不让原件预览参数成为任意文件写路径。

| 动作 | 候选接口 | 输入/输出合同 |
|---|---|---|
| 自由保存 | POST /objects | body_md或source_refs→id/revision |
| 读对象 | GET /objects/{id} | 当前内容、来源与历史入口 |
| 改对象 | PUT /objects/{id} | expected_revision+明确字段→新revision或409 |
| 新建工作区 | POST /workspaces | 可选中心对象→workspace和初始view；同一事务 |
| 读/存视图 | GET/PUT /views/{id} | view revision+布局/当前选择；不顺带改语义边 |
| 人工建立关系 | POST /relations | 端点、类型、依据→relation id |
| 创建候选 | POST /proposals | 白名单operation+payload+basis；不接受任意shell或文件补丁 |
| 审提案 | POST /proposals/{id}/decision | expected_revision、目标版本、接受/拒绝、可选说明 |
| 专题图/邻居 | GET /graph | view或center、边类型、展开范围→共同节点边+覆盖信息 |
| 导出选中范围 | POST /exports | selected_refs、包含原件与否→导出清单/内容；不发送网络 |

自由保存示例：`{"kind":"question","body_md":"保留边能还原次数吗？"}`；服务生成ID而非要求用户准备JSON。

接受P1示例：`{"expected_revision":1,"action":"accept","target_revisions":{"DEMO-Q1":1,"DEMO-M1":1},"note":"保留为待验证的方法类比"}`。
响应：`{"proposal_id":"DEMO-P1","state":"accepted","decision_ref":"DEMO-D2","relation_ref":"DEMO-R4","revision":2}`。sample.json保存的是**接受前**状态，不包含伪造的已执行回执。

400=合同不合法；404=目标不存在；409=版本冲突。来源缺失可保存疑问或草稿，不能把“证据不足”当作自由捕获错误。错误恢复保留用户已输入内容；不在本设计增加泛化重试、遥测或后台任务平台。

## 6. 导出和日常维护

导出包含版本、选中对象、引用闭包或明确外部引用、提案状态、相关过程、继续点；私有原件是否包含由用户选择。手机可直接读Markdown，JSON用于后续导入。导入先给差异，再确认；同ID不同revision不得静默覆盖。

重新索引只刷新自动资产层；来源链接坏了显示待重新定位。待审关系、静置分支与疑似过期来源集中供主动整理，不默认产生日程催促。维护以一次真实使用后的摩擦为依据：找不到、无法接续、重复填写、错误关系分别记入改进项；不先引入完整评分/日志系统。
