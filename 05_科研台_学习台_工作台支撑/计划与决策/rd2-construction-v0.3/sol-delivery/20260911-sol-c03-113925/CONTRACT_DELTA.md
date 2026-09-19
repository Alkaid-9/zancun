# RD-2 C00-C03 实际合同差异

本文件对应 `TASK-20260911-002` 与验收标识 `20260911-sol-c03-113925`。实现沿用 P1 的 Object/View/Revision 存储，不增加第二套关系权威。

## C00

验收配置将 `research_data_root`、`research_export_root`、`runtime_root`、`log_root` 分别指向本轮隔离根的 `data/`、`exports/`、`runtime/`、`logs/`。原 `config.local.json` 与真实资料只读。

## C01

`GET /api/research/sources/asset?asset_id=...` 仅接受已登记资产 ID，返回 `source_id`、`revision_id`、`asset_id` 和 `anchor.kind=registered_asset`。注册资产引用必须带 `asset_id`；工作簿 cell/range 继续保留既有 `worksheet_member` 映射。

## C02

关系使用 `Object(kind=relation)`，属性为 `from_ref`、`to_ref`、`relation_type`、`basis_refs`、`epistemic_status`、`state` 和 `target_revisions`。关系类型白名单来自上位合同。`POST /api/research/relations` 支持 expected revisions；`POST /api/research/relations/{id}/withdraw` 新建 revision 与 decision。

提案使用 `Object(kind=proposal)`，`operation` 为 `add_relation`、`add_todo` 或 `add_marker`，状态初始为 pending，`proposer=demo` 可明确标记演示。`POST /api/research/proposals/{id}/decision` 在单 SQLite 事务中写入决定、产物和状态；重复处置返回原结果。

## C03

`GET /api/research/map` 返回八层、学术／工业入口、L0-L2 与 W1-W7 的来源状态及缺口。`GET /api/research/graph?center_ref=...&relation_type=...&depth=1`仅投影active relation，不把pending当正式边。普通对象为中心时保持一跳；Topic为中心时，`attrs.topic_ref`指向该Topic的工作区成员构成专题作用域，关系任一端属于作用域即可进入Topic投影，使工作区新增记录连接任意专题成员后可回流。该扩展不是递归图查询，也不创建新正文权威。

View 增加 `return_context`，验证并持久化 `origin`、`filter`、`center_ref`、`selected_ref`、`source_id`、`view_id`。

专题来源进入工作区时，`return_context` 另保存 `topic_ref`；新工作区 `attrs.topic_ref` 与 Topic.attrs.workspace_refs 同步更新，工作区提供返回原专题入口。挂起、重启和继续路径沿同一上下文恢复。

`GET /api/research/topics/{id}` 返回专题、来源、workspace 投影和 active/pending 分离的邻域图。`GET /api/research/map` 从登记 catalog 与 Object 实际组合各层 source/object count、动作和缺口，不报告伪造完成率。

提案 payload 按 operation 严格验证：`add_relation` 创建关系，`add_todo` 接受后创建 `todo`，`add_marker` 接受后创建 `marker`。终态 proposal 重放直接返回原 decision/result；仅 pending 检查端点 revision 并在过期时返回 409。关系撤回的 revision 与 Decision 在同一 SQLite 事务中写入。导出增加 `external_refs`，明确未选择但被关系引用的对象。

Map 层返回 `status`、`source_count`、`object_count`、`coverage.date/scope`、`actions` 与 `gap`；`scales` 和 `waves` 为独立带状态条目。Map 入口先复用同来源的 EdgeIM Topic，只有无匹配项时才创建。

兼容性：既有 P1 对象、View、工作簿来源、冲突和导出接口保持不变；未知字段继续显式拒绝。C04-C07 与 X-* 不在本次差异内。
