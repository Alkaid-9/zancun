# WB-1 交付回执

状态：`complete`（有界文档包完成；应用运行验收保留 `partial`）。

## 输入与读取范围

- 入口：`progress/decisions/rd2-first-build-v0.2/SOL_START_HERE.md`。
- 规范：同目录 `README.md`、`WORKBOOK_INTEGRATION.md`、`DATA_CONTRACT.md`；项目约束：`AGENTS.md`。
- 原件只读：`/mnt/d/Alkaid/Desktop/工作簿1.xlsx`，实际读取显示 Sheet1 与 Sheet18；沿 workbook relationship 识别 Sheet18 对应 `xl/worksheets/sheet12.xml`。
- 登记只读：`research-desk/content/registry/assets.json` 的 `asset:workbook1:sheet:01` 与 `asset:workbook1:sheet:12`。
- 使用 solver 环境完成读取；未安装依赖，未执行原表 prompt、宏、外链或网络工具。

## 产物

- `SOURCE_MAP.md`：6 段真实单元格/范围，来源身份、用途提案、状态/未知与 P2/P3 动作；逐项区分原表、导出/资产登记、导航、学习科研用途。
- `WALKTHROUGH.md`：从 Sheet1!R6 到 P2/P3、草稿/反馈、挂起并返回原位置的走查；另含 Sheet18 prompt 引用走查，明确原文/改编/用户空位。
- `RECEIPT.md`：本回执与逐项验收。

## 验收逐项状态

| 项目 | 状态 | 证据 |
|---|---|---|
| 来源正确、Sheet18 使用 ID12/XML sheet12 | PASS | `SOURCE_MAP.md`；登记 `assets.json:25331-25342` |
| 原文身份与用途分开，关系/提案标待确认 | PASS | `SOURCE_MAP.md` 各段及末节 |
| 可从来源进入 P2/P3 并返回 | PARTIAL（文档走查，未运行应用） | `WALKTHROUGH.md` 第 1-5 步 |
| 不虚构学习、能力、反馈或 PASS | PASS | `WALKTHROUGH.md` 用户填写区；本回执 |
| 仅两表最多 6 段，未批量制造卡片 | PASS | `SOURCE_MAP.md` 6 段；范围声明 |
| 变更可追溯且仅写本交付目录 | PASS | 本目录三文件；未改原件、索引、应用或共享文档 |
| 图片与原位置/可搜索边界明确 | PASS | `SOURCE_MAP.md` Sheet18 A17/A53/A72 说明 |
| L0/L1/L2、入口、位置/归属/语义关系不混同 | PASS | `SOURCE_MAP.md` 末节；`WALKTHROUGH.md` 第 5 步 |
| 提案状态与正式关系共同保存、SQLite 建议不迁移 | PASS（建议记录） | `SOURCE_MAP.md` 末节；未创建数据库 |

## 未做、未覆盖与不确定性

未处理其余 16 表、全文语义融合、图片 OCR/逐图核对、外链/网络核验、实际应用代码、拖拽/3D、真实用户作答和使用回执。Sheet18 登记的 `Sheet12` 标签是历史标签，同时显示名是 Sheet18；本交付以 `fragment: sheet:12:Sheet18` 和 workbook relationship 为准。由于没有应用编辑能力，本回执不能宣称运行闭环通过。

## 停止条件

入口规定的停止条件未触发：原件、登记和映射均可读，未见冲突；未安装依赖、未改可写目录、未运行外部命令或 prompt。按范围完成后三件产物后停止，不自动继续代码或其他表。
