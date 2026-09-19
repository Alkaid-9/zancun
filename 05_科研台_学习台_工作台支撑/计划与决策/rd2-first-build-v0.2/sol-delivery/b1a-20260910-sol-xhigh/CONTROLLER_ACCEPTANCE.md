complete

# RD-2 B1a 主控独立验收

日期：2026-09-10（America/Los_Angeles）。验收对象：同目录 `RECEIPT.md`
所列 B1a 实现。结论：**CONTROLLER-PASS / B1a COMPLETE**。

## 恢复与边界

- 已重开 `SOL_START_HERE.md`、施工包 `README.md`、`IMPLEMENTATION.md`、
  `DATA_CONTRACT.md` 与执行回执，再按当前磁盘事实验收。
- 外层仓库 HEAD 仍为 `e757493236ebdb1fd1cc114417eed093e0435e79`；
  `research-desk` 被外层仓忽略，普通 Git diff 不能作为其变更证据。
- MAS 嵌套仓当前 HEAD 为 `08c9e947710e44b9240335b75e27efd882925be9`，
  已从执行回执记录的 `da66308f` 前进三个无关提交；B1a 回执与施工包仍是
  当前工作树中的新增文件。本验收没有改动或回退其他窗口内容。
- 未授权也未执行 B1b、B2、3D、真实数据迁移、导入、上传、安装、部署、
  commit、push 或共享 TODO/INDEX/CHANGELOG/task-log 修改。

## 主控抽查与修正

逐行抽查 `record_store.py`、`research_service.py`、HTTP 路由、配置与测试后，
确认对象/视图使用不可变修订快照；工作区与初始 view 同事务创建；旧 revision
冲突返回当前内容和提交内容；布局、领域尺度、操作入口与草稿线分开保存；旧资产
扫描不写 SQLite；导出只处理显式选择并固定 `uploaded=false`。

独立探针发现并在 B1a 原范围内修正两项合同缺口：

1. 同值对象/视图保存原会增加空 revision。现由 `record_store.py:298`、`:461`
   在事务和 revision 检查之后返回当前快照，不生成空历史。
2. `source_refs.anchor=null` 原会写入数据库。现由 `research_service.py:67` 起要求
   非空 anchor kind；workbook cell/range/image 还必须携带显示表名、sheet ID、
   实际 worksheet member 及对应单元格/区间/图片定位字段，避免由 Sheet18 错推
   `sheet18.xml`。

对应回归测试位于 `app/tests/test_research_records.py:245`、`:267`。执行回执保留
为 Sol 原始自验记录，没有回写其当时的 15-test 结果。

## 独立验收结果

| 项目 | 结果 |
|---|---|
| solver 环境门禁 | passed；Python 3.10.19，解释器为 `/home/alkaid/miniconda3/envs/solver/bin/python` |
| 全量后端测试 | passed；17 tests，包含既有 5 项 |
| C01/C02/C03/C04/C08 | passed |
| 挂起恢复与布局/语义分离 | passed |
| 同值保存不增空 revision | passed |
| 来源锚点最小合同及 Sheet18 实际 XML 定位 | passed |
| 手动、选择式 JSON/Markdown 导出服务 | passed |
| HTTP 旧 GET 与新 400/404/409 合同 | passed |
| `check-links` | passed；2432 assets，0 errors，0 warnings |
| SQLite | passed；`integrity_check=ok`，外键检查无结果 |
| 合成演示根 | passed；4 objects / 5 object revisions / 1 view / 2 view revisions |
| 常驻服务 | 未启动；验收后无 `research_desk.py ... serve` 进程 |

演示 SQLite 与两种导出均只含 `DEMO` / `DEMO_SYNTHETIC` 内容；question、
attempt、feedback、workspace 和 view 引用闭合，Feedback 指向具体 Attempt。
原资产仍在原位且只读。

## 结论与下一门

B1a 数据闭环按已授权范围封板，可作为 B1b 的前置。这里的“完成”只指后端数据、
服务和 HTTP 合同：当前恢复仍依赖调用方持有对象 ID，尚无工作区界面或真实用户日常
使用回执。B1b 需另行明确授权，并在界面验收中证明新记录可被发现、关闭后可发现并
继续，而不能只以按 ID 的 API 读取代替用户可找回。
