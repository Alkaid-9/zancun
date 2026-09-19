# Sol P1 实施任务书：保存、找到并继续学习／科研工作区

状态：IMPLEMENTED / CONTROLLER-PASS / USER-ACCEPTANCE-OPEN。本文件保留原实施合同；最终证据见[实施回执](sol-delivery/p1-20260910-sol/RECEIPT.md)、[主控验收](sol-delivery/p1-20260910-sol/CONTROLLER_ACCEPTANCE.md)及[使用说明](sol-delivery/p1-20260910-sol/USAGE.md)。
归属：RD-2 / TASK-20260910-001设计续段。记录：2026-09-11 UTC / 09-10 America/Los_Angeles。

## 0. 接到本文件后直接执行

用户授权主规划窗口：“做，然后我拿去给sol执行”。用户把本文件交给Sol并要求执行时，即按这里限定的P1范围实现代码、做隔离验证、交回执；不再交一轮等待批准的总体方案。主规划窗口只交文档，没有启动实施。

目标链：**来源或一句自由记录 → 草稿 → 尝试／反馈 → 挂起 → 关闭页面及重启验证服务 → 从界面找到并继续 → 手动下载所选记录。**

承载：现有本地网页，Python HTTP服务＋原生HTML/CSS/JS＋B1a SQLite。不换栈、不先装桌面壳；长期桌面形态保留后续选择。P1完成不等于完整Map、菌丝网络或共同画布完成。

最短阅读：本页 → [总体方案](README.md) §4–6 → [B1a主控验收](../rd2-first-build-v0.2/sol-delivery/b1a-20260910-sol-xhigh/CONTROLLER_ACCEPTANCE.md) → 按修改点读源码。WB-1只读[SOURCE_MAP](../rd2-first-build-v0.2/sol-delivery/wb1-20260910-sol-xhigh/SOURCE_MAP.md)的身份表与S1-2/S18-1；[比较表](../rd2-first-build-v0.2/sol-delivery/COMPARISON.md)保留另一份独立映射的地位。不重扫工作簿、不重查外部参考仓。

| 权威位置 | 用途／规划窗口核到的事实 |
|---|---|
| `/mnt/d/MyResearch/MAS_Safety_Project` | 规划与交接的独立Git仓；本轮HEAD为`b76ccafcf350ce70922fb827d35981142caa76c1` |
| `/mnt/d/MyResearch/research-desk` | 应用目录，仍被外层Git忽略、没有独立Git仓；外层HEAD不能证明应用版本 |
| `app/research_service.py` | 对象142起、工作区264起、View310起、选择导出330起；字段以源码为准 |
| `app/record_store.py` | SQLite对象、revision、View与事务；已有`list_object_revisions` |
| `app/research_desk.py` | `research_get`、POST/PUT、`load_catalog`、`serve`与静态路由 |
| `app/static/{index.html,app.js,styles.css}` | 原导航主要请求`/api/catalog`；`renderHome/openAsset`为接入点 |
| `app/tests/{test_research_records.py,test_research_desk.py,browser_check.py}` | 现有后端和浏览器核验入口；旧浏览器脚本未覆盖P1 |

B1a历史主控回执报告17项后端测试通过；本规划窗口未重跑。Sol开工核定这些文件当前状态即可；局部差异写回执，不覆盖其他窗口修改。

## 1. 产品边界

1. HOME与工作台首页合并；学习／科研／通用事务是领域分类，已安排／等我处理／执行或等待／候选是协调状态，分别显示。P1只接真实“继续工作”列表，完整协调面在P2对接，不填假任务。
2. 工作台保留任务、依赖、验收、资源、版本、重跑与恢复职责。阅读、手推、草稿直接进行，需要排期、委派或资源协调才经过调度。P1不接真实派发。
3. 同一次活动及产物可同时支持学习评价与研究认识，切换观察角度不复制对象、不强制单选归属。P1允许在共用草稿中分别记录，正式评价模型后续做。
4. 科研继续覆盖探索、问题形成、团队与工业路线、方法比较、公开失败与草稿、研究议程。P1记录页不替代原Map八层／七图。
5. 自由记录只需正文或来源，不强制项目、课程、标签、关系、task_id或日期。AI关系／待办／标记仍先提案；本包不接模型自动写入。
6. 人的作答、AI示范和合成演示分清；不生成掌握分／研究通过状态，不改资产`used/adapted`。索引可见、运行成功都不等于本人掌握或实际采用。

## 2. 页面和动作

```text
HOME [随手记录] [从资料开始] [最近工作区 / 挂起工作区]
                           ↓
工作区 标题 [通用 / 学习角度 / 科研角度] 已保存／尚未保存
┌──────────────┬────────────────────────┬───────────────────┐
│ 问题 / 草稿   │ 原段（锚点） | 编辑正文 │ 来源、帮助条件     │
│ 尝试与反馈    │ [保存] [新尝试] [反馈] │ 历史 / 继续点      │
├──────────────┴────────────────────────┴───────────────────┤
│ [保存并挂起] [继续工作] [选择并导出] [返回HOME]             │
└──────────────────────────────────────────────────────────┘
```

| 动作 | 必须出现的结果 |
|---|---|
| 随手记录 | 一句无分类文字能保存并进入工作区；无来源也合法；空正文且无来源时说明需要内容 |
| 从资产开始 | 选择新建或已有工作区，保留准确来源及锚点；新建沿既有Workspace＋初始View事务 |
| 保存／新尝试 | 修改正文增加revision；新attempt有独立ID；帮助条件与操作者可选填，不替用户填写独立作答 |
| 记反馈 | 明确选择本工作区的一次attempt，显示被反馈内容，不按最近时间猜对象 |
| 切观察角度 | workspace/object ID、正文、选中项和来源保留；侧栏用途变化，不做任务路由 |
| 历史 | 列修订并只读打开旧正文，可返回当前版；查看不触发覆盖 |
| 保存并挂起 | 正文、View继续点与workspace状态都成功才显示“已挂起” |
| 继续 | HOME发现并打开，恢复选中、来源与继续点；主动继续才设active，GET不写状态 |
| 导出 | 显式勾选对象／工作区继续点及JSON/Markdown，生成后点击下载；不上传、不回导 |

保留原资产搜索、指导库来源／场景双入口和画布“规划中”真实状态。P1是列表与编辑区；完整拖拽、正式关系和共同画布后续实现。

## 3. 记录约定

沿用现有Object/Workspace/View及开放attrs字段，不迁库、不建立万能控制回路schema：

- `workspace.attrs.object_refs`为内容成员权威列表，保留center_object_ref；View.members是显示子集，selected为成员或null。
- `workspace.attrs.p1.status`为active/suspended，历史缺值按active展示，不批量补写。
- `workspace.attrs.p1.perspective`为neutral/learning/research，仅记当前观察角度；历史缺值按neutral展示。
- `view.resume_note/selected`记继续点与当前对象；保留positions/pinned/collapsed等既有字段，不冒称拖拽已实现。
- 新question/note/attempt/feedback用既有kind/body_md/author/source_refs/attrs。反馈沿attrs.attempt_ref；尝试可用attrs.question_ref指向工作区内问题、可选attrs.assistance文字记帮助条件。
- 合成记录用attrs.demo=true与可见DEMO，author填实际操作者或demo。默认human不构成本人独立作答证据。

更新attrs须合并原字段并提交expected_revision，不能只写p1而覆盖其他字段。P1界面与新增成员接口保证成员存在、选中项属于成员；现有B1a通用View接口未保证这点，不能假设已有。历史缺失引用显示具体ID并允许打开其余内容，不擅自删引用或批量修真实数据。

## 4. 接口合同

标为新增的路由均为本包实现任务，不是现状。现有400 invalid_request／404 missing／409 revision_conflict语义保留。

| 接口 | 合同 |
|---|---|
| 现有POST objects、GET/PUT objects/{id} | `/api/research`前缀；PUT携expected_revision，GET可带revision=N |
| 现有POST workspaces、GET workspaces/{id} | 保留原响应；GET返回workspace和views，不是发现列表 |
| 现有GET/PUT views/{id} | PUT携expected_revision；entry_kind仍是global/topic/workspace，不能塞learning进去 |
| **新增**`GET /api/research/workspaces` | 返回`{items:[...],total:N}`。项含workspace_id/title/status/perspective/updated_at/source_refs/view_id/selected/resume_note；无View时对应字段null并显示缺口 |
| **新增**`GET /api/research/objects/{id}/revisions` | 调list_object_revisions，返回`{object_id,revisions:[{revision,updated_at,author,revision_note}]}`，revision降序；正文沿已有GET取 |
| **新增**`POST /api/research/workspaces/{id}/entries` | 在单事务中创建内容、加入工作区成员和当前View；详见下文 |
| **新增**`GET /api/research/sources/workbook?asset_id=...&cell=R6` | cell与range=A14:A43二选一，从已有单表抽取返回asset_id/source_id/revision_id/anchor/cells；详见§5 |
| 现有`POST /api/research/exports` | 保留selected_refs/formats及uploaded:false，files增加download_url；保留path兼容，但界面不用磁盘路径充当下载链接 |
| **新增**`GET /api/research/exports/{export_id}/download?format=markdown` | 按服务生成的export_id和json/markdown读取配置export_root中的文件，返回attachment和正确MIME；缺文件404、无效ID/格式400，不接受磁盘路径参数 |

列表范围：当前配置record库中的全部workspace；P1一次返回，前端做标题及全部／挂起过滤。不扫原始资料、不混入catalog.continue静态卡；旧卡在“资料继续入口”单独保留。排序为updated_at降序、workspace_id升序。时间取workspace、所属views、object_refs引用的现存内容的最大updated_at；不用空workspace修订模拟最近活动。摘要View取最新updated_at、id升序的一个。空列表给开始入口，不制造演示用户数据。

entries请求示例（尖括号字段用实际值）：

```json
{
  "expected_workspace_revision": 1,
  "view_id": "<本工作区的view ID>",
  "expected_view_revision": 1,
  "object": {
    "kind": "attempt", "body_md": "DEMO：不是用户作答", "author": "demo",
    "source_refs": [], "attrs": {"demo": true, "assistance": "合成验收示例"}
  }
}
```

在单一SQLite事务中检查workspace/view revision和归属，沿既有合同创建对象，追加workspace.attrs.object_refs及view.members，设置view.selected，保存各自修订。feedback的attempt_ref须为本工作区attempt；question_ref如填写须为本工作区问题。返回201 `{object,workspace,view}`及最新revision；任一步失败都不留下半条内容或半次关联。409返回冲突资源、当前与提交内容，用户处理后显式重提。只为该流程提取必要事务辅助方法，不重写RecordStore、不造通用事务框架；不能连续三次HTTP写入后笼统显示保存成功。

可先用既有接口创建空工作区及初始View，再用entries保存第一条自由记录。单独保存现有正文仍用对象PUT，无需重写成员；一次保存从成功回执更新界面的revision。

## 5. 来源定位

| 用例 | 已核身份 | P1验收 |
|---|---|---|
| 主流程 | asset:workbook1:sheet:01 / Sheet1 / sheet_id `1` / xl/worksheets/sheet1.xml / R6 | 显示R6原文和定位，从这里记录；恢复能打开相同原段 |
| 映射回归 | asset:workbook1:sheet:12 / Sheet18 / sheet_id `18` / xl/worksheets/sheet12.xml / A14:A43 | 显示区间文本；不猜sheet18.xml，A17的image.png仍是文字 |

原件`/mnt/d/Alkaid/Desktop/工作簿1.xlsx`、抽取和registry只读。catalog.workbook只有表元数据、无cells；asset.workbook_detail也排除了cells，两资产preview_locator为空。新增接口沿登记的sheet_index/member，读`content_root/intake/workbook1/sheets/sheet-01.json`或sheet-12.json等已有抽取，核对name/sheet_id/member一致，取指定cell/range；不重新解析全工作簿。

SourceRef保存真实source_id，可附asset_id/revision_id；anchor.kind用workbook_cell或workbook_range，含sheet_name/sheet_id/worksheet_member及cell或range。asset_id不能冒充source_id。cells沿原JSON的cell/value等字段；合法空格显示“该位置无非空文本”，非法单元格格式400、资产不存在404；映射不一致明确报错。

“回原段”承诺网页显示准确抽取文本、完整位置和可复制Windows路径，不承诺操控Excel选中格。真实图片沿已有媒体入口保留锚点，P1不新增图片空间编辑器／PDF解析器。源prompt只展示；原文、解释、草稿可区分，用户内容不作为HTML或脚本执行。

## 6. 保存失败、冲突与导出

网络错误或409时保留编辑框，显示失败步骤并提供复制草稿；不自动重试、清空或接受服务器版本。未保存时切对象／返回HOME，让用户选择保存、丢弃或留下。尚未保存的输入不承诺浏览器关闭／断电后恢复，可先复制带走；关页重开验收用已成功保存的记录。

对象409并列“我未保存的内容／服务器当前版”，用户保留草稿或手工合并后，才用最新revision重提。查看冲突不自动覆盖。View/workspace冲突保留继续点与选择意图；未加载成功前不把默认空members写回。正文保存成功而View/挂起状态失败时，显示“正文已保存，挂起未完成”，不虚报全成功。来源失效显示缺口，不换成同名资料。

导出不默认全选：选择对象，需要继续点时另勾workspace。现有export不递归带出其成员正文；生成前显示正文选择及仅作为引用的ID，未选正文不进包。反馈引用未选attempt时注明正文未随包附带，不自动扩大范围。下载为生成时快照，之后编辑不改变文件。Markdown窄屏可读；无上传／回导／同步／手机账号连接。

## 7. 写域、版本证据与隔离配置

应用写域（相对research-desk）：

- app/static/index.html、app.js、styles.css；必要时新增一个workspace.js并补显式静态路由。
- app/research_service.py、record_store.py、research_desk.py，仅本包接口和保存／片段读取。
- 扩展既有app/tests/browser_check.py覆盖P1实际操作；后端运行现有测试并按§9记录行为核验，不另建测试平台或泛化测试层。
- `acceptance/p1-<实际窗口标识>/`内的config.p1.json、data/、exports/、runtime/、logs/、before/、changes.patch与验收证据。日志仅本次既有服务输出，不新增生产遥测。

Sol文档写域：`/mnt/d/MyResearch/MAS_Safety_Project/progress/decisions/three-desks-v0.1/sol-delivery/p1-<实际窗口标识>/`。只交自己的文档，不改本文／上位规划／他窗回执／共享TODO、INDEX、CROSSWINDOW。共享登记由主控后续依据回执合并。

目前应用不受独立Git管理：改前逐个保存本包既有源码到before，记录新增文件，交可读changes.patch，作为差异与局部回退输入；不复制真实数据库／资料。若接手时已成为独立仓，用该仓基线与scoped diff替代并说明。不能以外层空git diff证明应用未改；不git init、不改ignore、不commit/push。

沿config.local.json现有字段生成本次config.p1.json；content_root、allowed_roots等原来源设置沿用只读。research_data_root、research_export_root、runtime_root、log_root分别指向本次验收目录的对应子目录，host明确127.0.0.1，port取空闲本地端口并记录。原config.local.json不改，真实记录不拷入验收库，应用参数不用环境变量隐藏注入。启动只用专用配置。

不安装、迁移、整理全库、改模型／机器配置、连接账号／Tunnel、实施TaskQuay／M4或服务器。必要短时本地验证服务已在包内，不能停别人的服务；演示库标DEMO，真实source_ref只引用、不执行源prompt。

## 8. 步骤、分工与停止条件

| 步骤 | 工作 | 阶段产物 |
|---|---|---|
| S0 | 核根目录／身份／写域／局部基线，solver门禁，保存改前源码与隔离配置 | 回执基线和文件清单 |
| S1 | 列表、历史、原子entries、源段、下载接口 | 接口及行为核验；既有后端测试实有结果 |
| S2 | HOME发现、编辑／尝试／反馈、历史／冲突、挂起恢复、下载 | 可操作本地网页 |
| S3 | 按§9走两种来源、双标签页冲突、关页及重启服务后继续、桌面／窄屏 | 验收JSON、截图和导出样例 |
| S4 | 写使用／维护说明、差异和剩余项，停止自己启动的短时服务 | RECEIPT、USAGE、changes.patch，交回即停 |

并发≤2，含主窗口。用户交给独立Sol窗口实施；只读子代理不因拿到任务书就有代码写权。Sol自验明示“单执行者自评”；独立核验释放执行位后由另一个人／窗口顺序做。不要求启动其他模型，不以任务名冒充模型身份。

遇局部阻碍交已完成部分与最小缺口：环境门禁失败停Python相关动作；缺浏览器将该验收列not-tested，继续其他实现／文档；源映射矛盾停对应来源；同一文件有并发修改停该文件。新依赖／配置字段／真实迁移／外部权限超出本包，不擅自做。既有授权的可逆步骤不用反复询问。不因P1完成进入P2/P3/B2/3D/桌面／部署。

## 9. 验收矩阵

| 编号 | 操作和通过条件 |
|---|---|
| A01 自由捕获 | 不填项目／任务／课程／分类，一句DEMO正文可保存，原资料未改 |
| A02 来源 | Sheet1!R6正文、source_id、完整anchor一致，重开回同段，未执行源prompt |
| A03 映射 | Sheet18!A14:A43来自sheet12.xml，image.png是文字 |
| A04 共用 | 切学习／科研／通用保持workspace/object ID、正文及选中；无自动评分或研究判断 |
| A05 成员 | 新attempt/feedback加入成员；反馈指向本工作区所选attempt；重开仍在 |
| A06 原子性 | 旧workspace或view revision调用entries得409；对象／成员／View无部分写入，原输入保留 |
| A07 接续 | 成功保存正文／选中／继续点并挂起，关页且重启隔离服务后从HOME挂起列表继续，不手记ID |
| A08 发现 | 两个工作区，更新成员草稿或继续点后排序正确；空列表、标题／挂起过滤可用 |
| A09 历史 | 改草稿后前后revision及旧正文可查，查看旧版不改当前内容 |
| A10 对象409 | 双标签页甲先保存、乙冲突，乙输入保留；用户合并才重提，旧内容仍有历史 |
| A11 View409 | 双页改选中／继续点发生冲突，不清空members、不覆盖新继续点，明确保存不完整 |
| A12 下载 | 只选一个对象及workspace继续点，浏览器下载JSON/MD；未选正文不在包，缺正文引用说明可见，uploaded=false |
| A13 下载合同 | 有效但不存在export ID为404，无效格式／ID为400，attachment正确，内容为生成时快照 |
| A14 旧功能 | 资产导航、搜索、指导双入口、媒体、旧继续卡保持可用；不改登记数量迁就测试 |
| A15 存储 | 演示只写隔离record库，原资料／registry／真实SQLite／原配置未写；发现列表独立于资产索引 |
| A16 可用性 | 桌面完成全链，窄屏表单和按钮可操作、MD可读；服务失联保留当前输入并明确未保存 |

旧导航“A11浏览器20项”不是本表A11；旧截图、源码审阅不替代本包实际浏览器操作。新增验收仅覆盖上表已声明的行为，不扩展成测试平台、遥测或无关代码护栏。

先在MAS目录用solver环境运行`bash tools/scripts/require_solver_env.sh`，明确解释器为`/home/alkaid/miniconda3/envs/solver/bin/python`。之后在应用目录执行（尖括号用实际参数替换）：

```sh
/home/alkaid/miniconda3/envs/solver/bin/python -m unittest discover -s app/tests -p 'test_*.py' -v
/home/alkaid/miniconda3/envs/solver/bin/python app/research_desk.py --config <config.p1.json绝对路径> check-links
/home/alkaid/miniconda3/envs/solver/bin/python app/research_desk.py --config <config.p1.json绝对路径> serve
```

serve用可管理的后台／会话方式启动，记自己的PID／端口，不阻塞主流程、不碰8899。先确认已有浏览器／CDP可用，不擅装或改机器配置。旧脚本通过CDP连接，参数如下：

```sh
/home/alkaid/miniconda3/envs/solver/bin/python app/tests/browser_check.py --base-url http://127.0.0.1:<本次端口> --cdp-url http://127.0.0.1:<实际CDP端口> --output <本次验收目录绝对路径>
```

为写入型P1场景增加显式选项（如--p1），只对隔离服务执行；保留旧导航模式，USAGE记录最后命令。其他已有浏览器工具可完成同等实测并留证，不强制换CDP；缺浏览器报partial，HTTP探针不能标浏览器通过。check-links只核既有引用，不跑scan/workbook/build；记录独立性按存储读写边界检查并说明验证方式，无需重扫全盘。

## 10. 产物与回执

Sol文档目录只需两份：

- **RECEIPT.md**：首行complete/partial/blocked；实际身份及未知、时间、仓与基线、逐文件改动、数据配置位置、接口差异、A01–A16 passed/failed/not-tested及证据路径、命令／退出码、自评或独立、未完成、风险／局部回退／下一步。
- **USAGE.md**：用实有绝对路径／端口说明启动停止、页面入口、保存、历史、挂起恢复、下载、409处理；列源码、权威数据、导出与运行日志位置。回退只回本包源码，不删新用户记录；演示也先保留，不清理他窗目录。

应用验收目录留browser-check.json、桌面／窄屏截图、选择导出样例、必要HTTP行为结果、changes.patch和改前源码。只存必要证据，不复制长终端日志、私人材料或新建checksum manifest；示例用DEMO、真实原段注明来源。

complete只表示本包实现和约定自验完成；独立复核、用户实际使用分别列明。必需项not-tested时为partial；不将自验改名为独立通过。资料全量融合、完整Map／画布、真实派发、学习测量、桌面／服务器仍属后续。

交回即停，不自动改共享台账、commit/push或接下一包；主控按回执复核后再决定后续范围。
