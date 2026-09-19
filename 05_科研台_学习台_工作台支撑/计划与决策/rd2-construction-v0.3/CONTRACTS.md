# RD-2 第一波对象与接口合同

状态：v0.3施工合同。已有P1合同继续有效；Sol先在CONTRACT_DELTA记录实际字段和局部调整，再实现。这里固定语义和可验收行为，不要求照抄内部函数名。

## 1. 不变量

1. 原资产只读；用户内容写入独立记录根。重扫资产不能覆盖对象、关系、决定、用途、历史或视图。
2. `asset_id`是导航资产身份，`source_id`是来源身份，`revision_id`是被引用版本；三者不互相冒充。来源引用保存稳定身份及可辨别anchor。
3. Object保存内容；Relation保存正式语义；Proposal保存未决建议；Decision保存人工处置；View保存布局、草稿线、选择和返回上下文。删除视图成员或拖动不删除Object或Relation。
4. 正式保存“个人联想，待验证”是合法的；正式只表示用户明确保存了关系，不表示命题经科学核验。
5. 所有会覆盖已有状态的写入带`expected_revision`；冲突返回当前状态与提交内容。错误时保留前端输入，不静默重试。
6. AI提案只由明确decision变成正式对象／关系／TODO／标记；接受、产物和proposal状态在一笔事务内。重复接受幂等。
7. 探索覆盖、个人学习证据、研究判断、任务运行、来源可用性各自保存，不能由另一域自动推出。

## 2. SourceRef

保留P1已实现的workbook_cell/workbook_range/workbook_image。C01增加或明确：

```json
{
  "source_id": "src:...",
  "asset_id": "asset:...",
  "revision_id": "rev:...",
  "anchor": {"kind": "registered_asset"}
}
```

`registered_asset`表示整份已登记资料。若实现文本片段，使用`text_excerpt`并保存可重复定位的行号或明确字符范围和内容版本；不能只存一段脱离位置的复制文本。第一波不必实现任意PDF页码或图片区域。来源详情以registry解析真实路径，记录库不复制原文件。

现有`_source_refs`对未知anchor仅保存、不校验。实现者须为本包新增anchor显式验证，并保持旧P1 workbook引用兼容；不接受任意磁盘路径作为SourceRef。

## 3. 关系、提案和决定

第一波可以继续用Objects表保存下列kind，无须立即新增关系表。attrs最小结构：

```json
{"kind":"relation","attrs":{"from_ref":"obj-a","to_ref":"obj-b","relation_type":"method_analogy","basis_refs":[],"state":"active"}}
{"kind":"proposal","attrs":{"operation":"add_relation","payload":{"from_ref":"obj-a","to_ref":"obj-b","relation_type":"method_analogy"},"basis_refs":[],"target_revisions":{"obj-a":1,"obj-b":2},"state":"pending"}}
{"kind":"decision","attrs":{"proposal_ref":"prop-a","action":"accept","result_refs":["rel-a"]}}
```

Relation类型白名单：`references`、`prerequisite`、`method_analogy`、`historical_influence`、`complements`、`goal_member`、`result_of`。`feedback_on`继续由既有feedback/attempt语义提供，专题图可统一投影，但不重复生成第二条事实。

Relation另外保存`epistemic_status`：`personal_hypothesis`、`source_supported`或`unknown`；默认unknown，不能根据relation_type推断。依据可空，但UI必须显示状态。withdraw是新增revision和Decision，将state改为withdrawn；不硬删。

Proposal首批operation：`add_relation`、`add_todo`、`add_marker`。本轮不接模型；DEMO提案须在界面可见地标DEMO和proposer=demo。接受和拒绝都保留proposal、依据及decision。拒绝不产生目标变更；过期target revision返回409并要求重新比较。

## 4. Topic和三尺度View

Topic是普通Object(kind=topic)，attrs至少含`academic_or_industry`、`domain_scale`及可选`parent_topic_refs`。Global/Topic不是新的正文权威；它们读取对象、关系、来源登记与View投影。

现有View必须依附workspace。第一波可为每个Topic创建一个内部workspace作为其持久视图容器，或以最小改动增加非workspace owner；两种方案必须在CONTRACT_DELTA选一项并说明：

- 是否会污染HOME“最近工作区”；
- Topic删除／撤回时对象与关系怎样保留；
- 旧P1 View怎样读取；
- 一个Topic怎样拥有多个视图而不复制成员。

内部workspace若采用，必须用明确attrs标为system view container，并从P1工作区列表排除。不能把Topic伪装成用户最近做过的学习／科研工作。

View继续保存`members`、`positions`、`collapsed`、`selected`、`resume_note`、`draft_edges`；增加`return_context`时应是稳定、可解析的对象：来源页／全局／专题、筛选、中心对象、选中项。视图模式不改变对象或关系。

## 5. 候选HTTP合同

保持`/api/research`前缀和现有400/404/409语义。路径可因现有router约束局部调整，但行为必须一致并写入CONTRACT_DELTA。

| 动作 | 候选接口 | 关键行为 |
|---|---|---|
| 从已登记资产开始 | `GET /sources/asset?asset_id=...` | 返回真实source/revision/registered_asset引用与可用预览；参数只接受登记ID |
| 新建人工关系 | `POST /relations` | 端点存在、类型合法、expected revisions匹配；返回relation r1 |
| 撤回关系 | `POST /relations/{id}/withdraw` | 写Decision和relation新revision；对象不删除 |
| 新建提案 | `POST /proposals` | 白名单operation、payload、basis、target revisions；默认pending |
| 处置提案 | `POST /proposals/{id}/decision` | accept/reject；接受事务生成唯一产物；重复调用返回已有结果 |
| 读专题邻域 | `GET /graph?center_ref=...&relation_type=...&depth=1` | 节点、正式边、覆盖与缺失；不返回pending为正式边 |
| 读专题 | `GET /topics/{id}` | Topic、View、图、来源与工作区引用；缺口显式 |
| 读全局入口 | `GET /map` | 八层、学术／工业、L0–L2、W1–W7及各入口状态；来源配置化，不硬编码成伪数据 |

若旧catalog已经提供某项信息，服务层组合即可，不复制一份新registry。Graph depth首批固定1；不实现通用图查询语言。所有写请求拒绝未知字段，提交失败不留半次写入。

## 6. 导出、备份与兼容

选择导出应包括选中对象、显式选择的关系／决定、来源引用、继续点，以及未带入正文的外部引用清单；不默认递归导出整个图。pending/rejected状态只有用户选择时进入导出，防止把提案当事实。

SQLite备份采用一致快照。恢复验收在新目录打开，不覆盖当前演示库。README/MAINTENANCE把`research_data_root`视作记录权威位置，`runtime_root`只用于可重建运行态；两者即使恰好嵌套，也不能宣称整个runtime均可删除。

旧P1对象和workbook SourceRef必须继续读。新kind在旧界面无法操作时至少可导出；USAGE写最低可读版本。sample.json及旧WB-1扁平anchor是历史样例，不能作为新接口输入权威。
