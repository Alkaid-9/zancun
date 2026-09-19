# P1 使用说明

P1 使用现有 Python HTTP 服务、原生 HTML/CSS/JS 和 B1a SQLite。当前已验收的隔离配置是：

`/mnt/d/MyResearch/research-desk/acceptance/p1-20260910-sol/config/config.p1.final-12.json`

## 启动与停止

在前台启动 loopback 服务：

```sh
/home/alkaid/miniconda3/envs/solver/bin/python /mnt/d/MyResearch/research-desk/app/research_desk.py --config /mnt/d/MyResearch/research-desk/acceptance/p1-20260910-sol/config/config.p1.final-12.json serve
```

访问 `http://127.0.0.1:8881/`。前台使用时以 `Ctrl-C` 停止该命令；不要停止 8899 或其他服务。本次交付时 8881 没有监听进程。

final-12 数据是验收 DEMO 数据，不是真实用户库。真实日常配置仍是未修改的 `/mnt/d/MyResearch/research-desk/config.local.json`；本包没有执行迁移。

## HOME 与继续

HOME 显示 record store 中的全部工作区，按聚合活动时间降序、同刻 workspace ID 升序。活动时间取 workspace、其全部 View、以及 `attrs.object_refs` 中现存对象的最大 `updated_at`。摘要 View 取最新 `updated_at`，同刻 ID 升序。

可按标题过滤，或切换“全部／挂起”。“资料继续入口”打开旧 continue 卡和 workbook 媒体；侧栏旧导航仍可使用，点击“继续”返回 P1。

从 HOME 点击“继续工作”时，如果工作区是 suspended，页面会显式保存 active 后再打开。仅 GET workspace 或 GET list 不改变状态。

## 新建、来源与成员

“随手记录”允许只填一句正文，不要求项目、任务、课程或来源。“从资料开始”输入 workbook 资产 ID 和单元格／范围：

- `asset:workbook1:sheet:01` + `R6`
- `asset:workbook1:sheet:12` + `A14:A43`

页面显示抽取文字、完整 anchor 和可复制的 Windows 原件路径；保存的 `source_refs` 使用接口返回的真实 `source_id`、`revision_id` 和 anchor。选择“用此来源记录”后必须明确选择“新建工作区”或“加入已有工作区”。加入已有工作区会在一个 SQLite 事务里创建对象、加入 `workspace.attrs.object_refs` 和当前 `View.members`，并设为 selected；不会再新建 workspace。Sheet18 的 worksheet member 是 `xl/worksheets/sheet12.xml`，不能按表名猜文件名。

来源接口以 registry 中 `asset.workbook_detail.sheet_index` 定位既有抽取 JSON，并要求 locator、registry 和抽取中的 `sheet_index/name/sheet_id/member` 全部一致。任一字段缺失、非法或映射漂移返回 `400 invalid_request`，不会换用同名工作表或重新解析原工作簿。

工作区的成员下拉框使用 View.selected，完整对象 ID 显示在下方。若 workspace 引用了已不存在的对象，页面在“缺失成员 ID”中明列该 ID，同时继续显示其他现存对象；不会自动删引用。

“通用／学习／科研”只切换观察角度及右侧用途说明，不改变 workspace/object ID、正文、成员或来源，也不产生评分、研究判断或任务路由。“新尝试”和“记反馈”使用页面内表单；操作者与帮助条件可选填，feedback 必须显式选择本工作区的 attempt。

## 保存、历史与挂起

“保存草稿”只保存当前 textarea。保存成功后当前 revision 随响应更新；服务失联或 409 时 textarea 不清空，也不自动重试。

当前正文有未保存更改时，切换成员或返回 HOME 会出现“保存后继续／丢弃更改／留下继续编辑”。“随手记录／从资料开始”的捕获页返回 HOME 也提供对应三选。尚未成功保存的输入不承诺跨关页恢复。

对象 409 时页面并列提示服务器当前正文，并提供“采用服务器修订作为重试基线”。该按钮只更新重试基线，不提交正文；用户检查／合并 textarea 后必须再次点击“保存草稿”。

“历史”列出修订按钮；点击旧 revision 只在状态区读取旧正文，不覆盖 textarea 或当前版本。

“保存并挂起”的固定顺序是：

1. 当前正文有变化时先保存正文。
2. 保存当前 View 的 selected 和用户填写的“继续点”。
3. 保存 workspace 的 suspended 状态。

只有三步都成功才返回 HOME 并显示“已挂起”。如果正文成功而 View 或 workspace 失败，页面明确显示“正文已保存，挂起未完成”，保留 textarea、selected、继续点和成员。View/workspace 冲突各有显式采用服务器 revision 的按钮，仍需用户再次点击“保存并挂起”。

新建流程按阶段报告失败：对象已保存但 workspace 创建失败时只重试 workspace；workspace 已创建但后续打开失败时只重试打开，不重复创建 workspace。

## 导出与下载

“选择并导出”不再要求输入 ID：

- 至少勾选一个正文对象。
- 需要继续点时另勾“包含工作区继续点”。
- 显式勾选 JSON 和／或 Markdown。

“导出前省略的引用 ID”会在生成前列出未选 workspace 成员和所选对象指向但未选的对象。导出不会递归加入未选正文。点击“生成导出”后，页面显示具体的“下载 JSON／Markdown”链接；不会自动下载、上传或回导。

下载路由格式：

`/api/research/exports/{export_id}/download?format=markdown`

无效 export ID／格式返回 400，格式合法但文件不存在返回 404；有效文件为 attachment，`uploaded` 始终是 `false`。导出是生成时快照，后续编辑不改变旧文件。

## 浏览器验收命令

最终 P1 命令如下，使用 Playwright 自带 Chromium launch 模式，并由脚本只管理给定配置的服务：

```sh
/home/alkaid/miniconda3/envs/solver/bin/python /mnt/d/MyResearch/research-desk/app/tests/browser_check.py --browser-mode launch --p1 --base-url http://127.0.0.1:8881 --service-config /mnt/d/MyResearch/research-desk/acceptance/p1-20260910-sol/config/config.p1.final-12.json --output /mnt/d/MyResearch/research-desk/acceptance/p1-20260910-sol/final-validation-12/runtime --report-name p1-final-browser-check.json
```

该 P1 分支要求配置指向空的新数据根；上面的 final-12 已运行并含证据，不应原地重跑来制造“空库”结果。负向映射验证会在输出目录内创建隔离 catalog 副本并管理短时服务，不写正式 registry/抽取。需要复验时，新建另一个显式隔离配置和目录，保留 final-12。

最终完整 legacy 命令：

```sh
/home/alkaid/miniconda3/envs/solver/bin/python /mnt/d/MyResearch/research-desk/app/tests/browser_check.py --browser-mode launch --base-url http://127.0.0.1:8881 --service-config /mnt/d/MyResearch/research-desk/acceptance/p1-20260910-sol/config/config.p1.final-12.json --output /mnt/d/MyResearch/research-desk/acceptance/p1-20260910-sol/final-validation-12/legacy-runtime --report-name legacy-final-browser-check.json
```

CDP 兼容模式仍保留：不传 `--browser-mode` 时默认 `cdp`，也可显式传 `--browser-mode cdp --cdp-url http://127.0.0.1:9223`。P1 最终重启场景要求 launch 模式。

## 权威路径

- 源码：`/mnt/d/MyResearch/research-desk/app/{record_store.py,research_service.py,research_desk.py}` 与 `app/static/{index.html,app.js,styles.css}`。
- 浏览器脚本：`/mnt/d/MyResearch/research-desk/app/tests/browser_check.py`。
- 当前配置：`.../acceptance/p1-20260910-sol/config/config.p1.final-12.json`。
- 当前数据：`.../acceptance/p1-20260910-sol/final-validation-12/data/desk.sqlite3`。
- 当前导出：`.../acceptance/p1-20260910-sol/final-validation-12/exports/`。
- 当前报告与截图：`.../final-validation-12/runtime/` 和 `.../final-validation-12/legacy-runtime/`；负向映射副本在 `runtime/mapping-drift/`。
- 完整证据清单：`.../acceptance/p1-20260910-sol/EVIDENCE.md`。
- 原始基线与差异：`.../acceptance/p1-20260910-sol/before/`、`.../acceptance/p1-20260910-sol/changes.patch`。

P1 不提供 P2/P3、B2、3D、完整拖拽关系、桌面壳、部署、上传、导入、账号同步或真实资料迁移。
