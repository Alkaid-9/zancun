complete

# P1 实施回执

日期：2026-09-11 America/Los_Angeles。

## 身份与结论边界

- 原实施会话：`01a08f32-4682-7883-8f84-4f8dfb390ca2`。控制器记录的启动选择是 `gpt-5.6-sol`、`xhigh`；会话内没有第二个运行时字段可独立证明 SKU 或 reasoning effort。
- 本轮主控会话：`01a08e23-f961-7d41-b9c1-297163953dc6`。临时总并发上限按用户要求改为 3；主控加两个只读核验位均已回收。两个核验位也无法从可见运行时元数据独立证明模型 SKU，因此不以任务名冒充模型证据。
- `complete` 表示 RD-2 P1 代码与合同 A01-A16 已通过实施自验和主控隔离复跑；用户实际使用验收仍未完成。它不表示已 commit、push、部署，亦不表示 P2/P3/B2/3D、完整 Map、共同画布或真实数据迁移完成。

## 基线、写域与隔离

- MAS 仓 HEAD：`b76ccafcf350ce70922fb827d35981142caa76c1`；外层仓 HEAD：`ab839b06849f6995da020a51972bb7929b65a37c`。两仓均有大量他窗改动，本轮未整理、回退、暂存或提交。
- 应用目录 `/mnt/d/MyResearch/research-desk` 不是独立 Git 仓。版本证据使用 `before/` 与 `changes.patch`，不以外层空 diff 代替。
- 当前实施自验：`final-validation-12/`，配置 `config/config.p1.final-12.json`，`127.0.0.1:8881`。
- 当前主控复跑：`controller-validation-2/`，配置 `config/config.p1.controller-2.json`，`127.0.0.1:8882`。
- 按本次恢复请求建立的全新 `final-validation-9/` 在 `127.0.0.1:8878` 通过 P1 120/120、Legacy 25/25；`final-validation-9-attempt-1/` 保留首次遇到非空根后立即停止的诊断。后续并发窗口产生的 `final-validation-12/` 仍是更新的当前实施证据，`final-validation-9/` 不冒充最新验收。
- 原 `config.local.json` 与 `before/config.local.json` 逐字节一致。原工作簿 SHA-256 仍为登记值 `d28ce510bfcc3cb00b1f0ee85d89a61b99d17d1df179a5dbee46c81fd9f52f34`。未安装依赖、迁库或写真实 registry/SQLite。

## 实际改动

- `app/record_store.py`：原子创建 workspace entry；发现列表按 workspace、全部 View 与现存成员聚合活动时间并稳定排序。
- `app/research_service.py`：缺失成员显式返回；workspace 列表、entry 成员/attempt/feedback 校验和选择导出合同。
- `app/research_desk.py`：P1 列表、历史、workbook cell/range、entries、下载路由；严格核对 locator、registry 与抽取映射；来源响应包含 Windows 原件路径。
- `app/static/app.js`：HOME/工作区完整流程；来源可新建或加入已有工作区；原文、完整 anchor 与路径恢复；attempt/feedback 表单；三种观察用途侧栏；未保存保存/丢弃/留下选择；创建与打开失败分阶段诚实反馈且不重复创建；冲突、挂起、历史和手动下载。
- `app/static/styles.css`：P1 状态、来源、条目、导航决策、导出与 390px 响应式布局。
- `app/static/index.html`：P1 渲染区，旧导航与详情入口保留。
- `app/tests/browser_check.py`：P1 120 项真实浏览器检查、隔离映射漂移、失败注入、重启恢复、双页冲突、下载和桌面/移动截图；Legacy 分支保留。

## A01-A16

| 编号 | 状态 | 关键证据 |
|---|---|---|
| A01 自由捕获 | PASS | 空库保存无来源正文；捕获页返回 HOME 的保存/丢弃/留下均实测。 |
| A02 来源 | PASS | Sheet1!R6 原文、真实 source/revision、完整 anchor、Windows 路径；加入已有工作区后 object_refs/View.members/selected 一致且未新建 workspace。 |
| A03 映射 | PASS | Sheet18=A14:A43=`sheet12.xml`，A17=`image.png` 文本；member、sheet_id、缺字段漂移均 400，原映射文件未变。 |
| A04 共用 | PASS | learning/research/neutral 保持 workspace/object/正文/选择，各自用途侧栏可见，无自动评分或研究判断。 |
| A05 成员 | PASS | attempt/feedback 均为成员；feedback 指向显式 attempt；operator 与 assistance 持久化。 |
| A06 原子性 | PASS | stale workspace revision 返回 409，无半对象、半成员或半 View。 |
| A07 接续 | PASS | 保存正文/选择/继续点并挂起，关闭浏览器并重启服务后从 HOME 按标题继续；R6 原文、完整 anchor、路径恢复；GET/list 不写。 |
| A08 发现 | PASS | 空列表、标题/挂起过滤、聚合活动时间、稳定排序和摘要 View 选择均通过。 |
| A09 历史 | PASS | 旧/新 revision 可查；旧正文只读打开，不覆盖当前版。 |
| A10 对象 409 | PASS | 双页冲突保留乙方输入，只在用户采用基线并再次保存后提交。 |
| A11 View 409 | PASS | 明示“正文已保存，挂起未完成”，选择/继续点/成员保留，显式重提后完成。 |
| A12 下载 | PASS | 页面显式选择对象、继续点、JSON/Markdown；省略引用预览；浏览器手动下载。 |
| A13 下载合同 | PASS | 无效 ID/格式 400、不存在 404、attachment/MIME/字节一致，快照不随后续编辑变化。 |
| A14 旧功能 | PASS | Legacy 25/25：资产导航、搜索、指导双入口、媒体、详情、规划中画布和返回 P1。 |
| A15 存储 | PASS | 两轮均为独立 DEMO SQLite；原配置、工作簿、registry/抽取未写；SQLite 完整。 |
| A16 可用性 | PASS | 1440x1000 与 390x844 无 overflow/clipping/overlap；失联保留输入且不自动重试；四张图均人工复核。 |

## 最终结果

- solver 门禁：未激活 shell 首次退出 2；显式 `conda activate solver` 后退出 0，解释器 `/home/alkaid/miniconda3/envs/solver/bin/python`。
- Python 编译与 `node --check app/static/app.js`：退出 0。
- 后端：`Ran 17 tests ... OK`。
- 实施自验：P1 `120/120`，Legacy `25/25`；`check-links` 为 2432 assets、0 error/warning；SQLite `integrity_check=ok`、无外键违规。
- 主控复跑：P1 `120/120`，Legacy `25/25`，后端 `17/17`，语法、链接、SQLite、配置和截图复核全部通过。
- `8878`、`8881`、`8882` 均已停止，匹配 final/controller 配置的服务进程不存在。

## 风险与停止

- 验收库含 DEMO、故意失效成员、摘要 View 夹具和故意损坏的 mapping-drift 副本，不得作为真实库或迁移源。
- 应用仍未由独立 Git 仓跟踪；局部回退只对照 `before/` 和 `changes.patch` 处理本包七个源码/测试文件，不删除隔离数据，不覆盖后续用户记录。
- 主控已完成技术验收；剩余门只有用户实际使用验收，以及另行授权的 harvest/commit/push/deploy。到此停止，不进入下一包。
