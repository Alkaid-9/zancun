complete

# RD-2 B1a 数据闭环执行回执

日期：2026-09-10（America/Los_Angeles）。任务包：RD-2 B1a。

## 身份、输入与边界

- 显式启动选择：`gpt-5.6-sol` + `xhigh`。
- 执行身份：本轮唯一 Codex 主代理；未派生子代理。
- 外层仓库根：`/mnt/d/MyResearch`；开工 HEAD 与用户指定基线一致：`e757493236ebdb1fd1cc114417eed093e0435e79`。
- 外层仓开工时既有脏文件只有 `CROSSWINDOW.md`、`GUARDRAILS.md`、`WINDOW_PLAYBOOK.md`；本轮未修改。
- 唯一回执所在的 `MAS_Safety_Project` 是独立嵌套仓，收尾 HEAD 为 `da66308fb34abb8f93c40be07de119231914c7e2`，已有大量其他窗口脏改；本轮在该仓的写入仅为本回执。`research-desk` 不属于该内仓，并被外层仓忽略。
- 读取范围限于用户指定的 AGENTS/实施合同/WB-1 回执，以及 `research-desk` 的现有 app、配置和测试；未重读全库或私人材料。
- 未执行 `git add`、commit、push、stash、reset、clean；未安装、升级或联网获取依赖。

## 变更与产物

代码与配置：

- `/mnt/d/MyResearch/research-desk/app/record_store.py`（新）：显式数据根导出 `desk.sqlite3`（`:90`）；对象/视图当前态和不可变 revision 快照（`:111`、`:120`、`:128`、`:137`）；公开单库事务边界（`:160`）；对象/视图乐观并发（`:283`、`:443`）；工作区和初始 view 同事务（`:372`）。
- `/mnt/d/MyResearch/research-desk/app/research_service.py`（新）：显式数据/导出根（`:95`）；自由对象、Attempt/Feedback 合同（`:108`、`:118`）；对象修订（`:147`）；独立工作区（`:240`）；挂起视图（`:286`）；选择式 JSON/Markdown 导出（`:306`、`:361`）。
- `/mnt/d/MyResearch/research-desk/app/research_desk.py`（小改）：只在 `/api/research/` 下增加对象、工作区、视图和导出 JSON 路由（`:1063`、`:1156`、`:1177`）；旧 `do_GET` 分支保留（`:1086`）；服务由配置构造（`:1207`）。
- `/mnt/d/MyResearch/research-desk/app/tests/test_research_records.py`（新）：C01/C02/C03/C04/C08、挂起、导出、显式路径和本地 HTTP 验收（`:35`、`:46`、`:65`、`:107`、`:126`、`:159`、`:189`、`:245`、`:300`）。
- `/mnt/d/MyResearch/research-desk/config.example.json:18`、`/mnt/d/MyResearch/research-desk/config.local.json:15`：只增加 `research_data_root` 与 `research_export_root`，未改其他配置值。

合成演示产物：

- SQLite：`/mnt/d/MyResearch/research-desk/runtime/rd2-demo/desk.sqlite3`。
- JSON：`/mnt/d/MyResearch/research-desk/runtime/rd2-demo/exports/export_e2bebd096f5347d198379ec888f3e686.json`。
- Markdown：`/mnt/d/MyResearch/research-desk/runtime/rd2-demo/exports/export_e2bebd096f5347d198379ec888f3e686.md`。
- 演示内容全部明确标为 `DEMO` / `DEMO_SYNTHETIC`：1 question、1 attempt、1 feedback、1 workspace、1 view；question r2、view r2。Feedback 的 `attempt_ref` 指向演示 Attempt。
- 演示对象 ID：question `obj_e35f9f09a3c14744a5a57603ea21838d`；attempt `obj_267ee2a51f974c60966abefcc8065efe`；feedback `obj_9b57a90535314f35971cdaeafc6a3f23`；workspace `obj_72adc45b52614d4aba05c3162cb0ad12`；view `view_34ede8b9892642ce8b7ea0f5815b4825`。

## 验收结果

| 项目 | 结果 | 证据 |
|---|---|---|
| C01 一句无分类疑问 | passed（执行者自验） | 仅 `body_md` 可生成稳定 ID/r1；关闭并重建 store 后内容相同；测试 `test_research_records.py:35` |
| C02 独立工作区 | passed（执行者自验） | 无论文/项目/中心对象可同事务创建 workspace + initial view；工作区可继续修订；`:46` |
| C03 D1/A1/F1 与后来解释 | passed（执行者自验） | Attempt/Feedback 为明确 kind；Feedback 校验具体 Attempt；D1 r1 与 r2 均可读；`:65` |
| C04 旧 revision 并发 | passed（执行者自验） | stale PUT 返回 409；载荷同时含 `current/current_revision` 与完整 `submitted`；当前内容未被覆盖；`:107`、`:300` |
| 挂起恢复 | passed（执行者自验） | selected/collapsed/positions/pinned/resume_note/domain_scale/entry_kind/draft_edges 保存到 view r2，重开恢复；布局更新未增加 Object；`:126` |
| C08 资产重扫隔离 | passed（执行者自验） | 临时旧 content 扫描后独立 SQLite Object 原样可读；`:189` |
| 手动导出边界 | passed（执行者自验） | 只导出显式 `selected_refs`；JSON/Markdown 均生成于显式 export root；未选对象不存在于包中；`uploaded=false`；`:159` |
| HTTP 合同 | passed（执行者自验） | 真实本地 `ThreadingHTTPServer` 覆盖旧 `/api/catalog` 和新路由；合同错误/不存在/冲突分别 400/404/409；`:300` |
| 后续原子确认可扩展性 | passed（设计边界自验） | 新记录在同一 SQLite；`RecordStore.transaction()` 提供单库显式事务，未来可在一个事务加入 Proposal + Decision Object + Relation；本包没有伪造这些接口或表 |

## 命令与结果

- solver 初检：未激活环境时门禁明确拒绝；随后显式 `conda activate solver`，`require_solver_env.sh` 返回 `Environment OK`，解释器为 `/home/alkaid/miniconda3/envs/solver/bin/python`（Python 3.10.19）。此后所有项目 Python 命令均重复执行该门禁并使用显式解释器。
- 首次 `python -m unittest -v app.tests.test_research_records` 被 solver 中同名第三方 `site-packages/app.py` 截获，进入 Nougat/Albumentations 后失败；未进入项目测试、未改依赖。改用文件入口及 discovery 后通过。
- 最终全量：`python -m unittest discover -s app/tests -p 'test_*.py' -v` -> `Ran 15 tests ... OK`（现有 5 + 新增 10）。
- `research_desk.py --config config.local.json check-links` -> `ok=true`、0 errors、0 warnings、2432 assets。
- 演示 SQLite `PRAGMA integrity_check` -> `ok`；4 objects、5 object revisions、1 view、2 view revisions；kind 分布为 attempt/feedback/question/workspace 各 1。
- AST/配置解析 -> `AST_OK=4 JSON_OK=2`。
- 外层根仓 `git diff --check` 无输出；六个改动文本逐文件 `git diff --no-index --check /dev/null <path>` 无空白错误。`research-desk` 被外层仓忽略，普通 tracked diff 不会展示其代码，因此没有把空 diff 冒充变更证据。
- MAS 内仓全局 `git diff --check` 被既有 `progress/task_logs/INDEX.md` 尾随空格阻塞；本轮没有修改该禁写文件。对本回执单独执行 `git diff --no-index --check /dev/null RECEIPT.md` 无空白错误。
- 旧 `content/registry/*.json` 与 `content/records/{reviews,continue,guidance,proposals,coverage}.json` 九个文件前后 SHA-256 全部一致；静态前端三个文件时间戳仍为本轮开工前，未修改。

## 明确未做

- 未做 B1b 前端、任何 `static` 修改、B2 关系地图、Proposal/Decision/Relation 接口、3D、真实数据迁移、导入、自动上传、网络、安装、部署或共享台账。
- `IMPLEMENTATION.md` 把用户界面上的手动导出归于 B1b；本包只交可复用的选择式导出服务与 `/api/research/exports` JSON 合同，没有增加导出按钮或前端行为。
- 未修改旧 JSON 记录、registry、原 Excel、MAS TODO/INDEX/CHANGELOG/task logs、其他既有脏文件或模型配置。
- 未启动持久服务器；HTTP 只在临时测试服务器上验证，避免向授权外日志目录写入运行日志。
- 本回执为同一执行者自验，不冒充独立核验或用户日常使用验收。

## 回退

1. 先保留当前 JSON/Markdown 演示导出；演示根没有真实用户内容。
2. 删除本包两个新模块和新测试，并从 `research_desk.py` 移除本包 imports、`/api/research/` 路由及服务构造。
3. 从两个配置文件只移除 `research_data_root`、`research_export_root` 两项。
4. 若不再需要合成冒烟数据，可删除整个 `/mnt/d/MyResearch/research-desk/runtime/rd2-demo/`；不要把此步骤用于未来真实记录。
5. 本轮无 commit 可回退；不要用 reset/clean 处理共享工作树。
