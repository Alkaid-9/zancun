# 进组训练与三台：维护与恢复手册

日期：2026-09-15。TASK-20260915-012首次编制。范围：现有三仓及当前A/B/隔离WP0的维护接续；下述操作需相应任务授权，不由手册存在自动执行。

TASK-019更新：A/B b54ea71、N3 c86f6d1、新隔离试用0b3a541已提交；当前恢复及归档欠账见[最新总交接](../handoff/2026-09-15__desks-window-current__handoff.md)。N2/N3现场未全量纳入Git，不能用代码checkout代替数据库/原件备份。

## 1. 每次维护先定仓库、数据和写域

| 仓库/位置 | 维护职责 | 当前注意事项 |
|---|---|---|
| `/mnt/d/MyResearch/MAS_Safety_Project` | 任务、设计、交接、学习合同 | 共享脏树；不要手写生成的NOW/STATUS等视图 |
| `/mnt/d/MyResearch/research-desk` | 应用源码、DEMO配置与验收 | 已独立Git；代码已提交，历史A/B合同回执/运行数据仍有未跟踪项，不能只备份HEAD |
| `/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901` | WP0隔离实现及Lot证据 | 包含旧复合改动，不可整树merge/stage；外部门未闭 |

每仓用显式`git -C`核root、branch、HEAD、status和staged路径。再读所选包的实际合同/回执及before。源码、配置、原件、对象库、派生索引、导出、临时日志分别定位，不用文件夹名推断权威。

原应用[MAINTENANCE](/mnt/d/MyResearch/research-desk/MAINTENANCE.md:75)仍有“尚未独立Git”旧说明，已被当前Git事实取代；其“runtime/logs可删除”不能不看真实配置就照做。本手册明确：配置把记录库放在runtime下面时，它仍是重要数据，不可当缓存清理。本次不改旧手册、不执行任何删除。

## 2. 环境、启动和停止

项目Python先通过MAS的`bash tools/scripts/require_solver_env.sh`，显式解释器为`/home/alkaid/miniconda3/envs/solver/bin/python`，不能在base装包。可直接使用[使用手册§2](lu-onboarding-and-desks-user-guide.md#2-查看当前合成demo)的显式solver预检命令。

科研台用指定配置启动，主机保持回环。8878只是B历史端口，不是永久空闲保证；先ss核监听，若冲突查PID/配置，不能终止其他窗口进程。本轮未常驻服务、未安装依赖、未部署。

WP0/8899按[原交接外部门](../handoff/2026-09-01__workbench-v2-wp0-codex-execution__handoff.md:84)处理，记录原PID/版本后才可受控重启。M4默认warn不因“要上线”改enforce。端口可见/HTTP响应/应用版本加载是三件事；观察矛盾时保留原观察并定向复查。

停止只针对自己启动的前台服务Ctrl+C或已核身份的进程；不要批量kill Python，不把“窗口存档”理解为关闭所有服务。

## 3. 新试用/复验现场

1. 选择本次任务独有且尚不存在的验收目录，位于应用`acceptance/`下，不覆盖A/B原验收根。
2. 参考原B配置结构，用apply_patch建立新的显式配置；content使用获准来源，data/exports/runtime/logs分别指向新根；检查没有混入真实config.local.json或真实registry。
3. 若要完整B/C03机器复验，按原RUN_CHECKS准备各自合成来源/夹具，不能只改output却复用会堆关系的旧C03库。
4. 新现场准备及命令写入实施任务后再运行。报告保留配置路径、源码版本/工作树差分、开始/结束、结果、失败和处理；不要把历史run目录当临时目录覆盖。

TASK-017已建立[新隔离试用](/mnt/d/MyResearch/research-desk/acceptance/user-trial-TASK-20260915-017/README.md)，本次TASK-019未再新建现场或测试。以后真实学习资料接入须指定材料与正式数据根，并与DEMO隔离；不能直接给DEMO改名后当个人正本。

## 4. 按包复验

最新命令：[N2 RUN_CHECKS](/mnt/d/MyResearch/research-desk/acceptance/n2-TASK-20260915-013/RUN_CHECKS.md)、[N3 RUN_CHECKS](/mnt/d/MyResearch/research-desk/acceptance/n3-TASK-20260915-013/RUN_CHECKS.md)。N3最终为final-v2/run-01专项20/20、final-regression-b2的27/27、final-regression-a的38/38、final-regression-c03的22/22。所有这些根已使用，不覆盖；旧RED也保留。原browser main会SystemExit，顺序启动须分别调用或只消费成功退出，检查三份报告真实存在，不凭批次exit=0报全绿。

返回链接必须使用生成时对应的配置和对象库；Git不包含对象库时，在新根重新生成合成夹具并使用新ID。端口保持本机回环，平板联网、真库加载、WP0自动桥与部署不在此包。只回滚N3源码hunk不删除note或数据库；已有note作为普通记录仍可读。

权威命令来自[B RUN_CHECKS](/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/RUN_CHECKS.md)。B/A/C03使用相同历史端口，依次运行，不并行抢占。`run-05`、`a-regression/run-02`、`c03-final/run-01`均为已用报告名，不复用。

允许的静态/后端检查示例（在应用仓、正确环境和相关测试授权下）：

```sh
/home/alkaid/miniconda3/envs/solver/bin/python -m unittest discover -s app/tests -p 'test*.py' -v
node --check app/static/app.js
node --check app/static/b.js
git diff --check
git apply --reverse --check acceptance/b-TASK-20260915-004/B_SCOPED.patch
```

最后一条只检查补丁能否反向匹配，不执行撤销；后来改动导致失败就核hunk，不能强行还原。B回归要包括A/C03、版本导出、旧未知记录、桌面/窄屏；机器通过后用户体验门仍开放。

WP0按原Lot/总验收命令重跑，不能把A/B测试或09-01历史138/490通过数充当新验收。新功能摘录按EXR-01–10，跨台桥按获准窄合同；本手册不另造整套代码级护栏或无限检查。

## 5. 数据备份与恢复

先读取实际配置，列明：研究对象库及相关文件、content/registry中的人工数据、必要原附件、导出根、继续点/版本；再决定备份范围。只保存Git、Markdown导出或assets派生索引不能恢复完整工作现场。

- 科研对象SQLite是重要持久数据；在获准备份任务中用SQLite一致快照机制，或受控停写后保留必要数据库文件集，不能运行中只随手复制主db而忽略WAL。
- WP0的SQLite是由任务日志重建的派生索引；仍先核日志/事件等权威来源存在，不能把科研对象库当同类派生物。
- 恢复先到新目录验证对象、历史、关系、反馈、继续点和附件引用；验证通过后是否切换配置另行确认。不覆盖现有真库作为第一次恢复测试。
- 备份目的地/范围未约定时先提出，不新增定时备份服务或默认全盘哈希工作流。已有哈希仅沿原来源完整性/共享CAS用途使用，不重新生成全库manifest。

当前本包只提供维护步骤，没有执行备份/恢复；不声称全部本地资料已有可恢复副本。

## 6. 限定提交和共享登记

1. 新任务通过8899中央allocator领号，失败时才按仓库协议使用兜底；不目测抢号。只有task ID响应成功不能证明整个服务健康。
2. 用任务日志记录实际工作，INDEX只加/改本任务行。两INDEX遵守既有行尾和CAS，冲突重新读后重算，不整文件覆盖。
3. 先检查暂存区为空或仅有自己明确拥有的内容。自有文件按路径stage；共享INDEX从HEAD构造只含自有行的cached patch，工作树其他行不改。操作前后核实际diff，发现他窗staged项即停止提交并协调。
4. 提交前列allowlist、审staged diff/空白；提交后查commit tree和staged区。不要git add -A、commit -a、reset、stash、clean或归一化共享行尾。
5. 应用A/B按before/patch与新差分审阅采收，不能从HEAD全差分猜B所有权。WP0必须先过原异构审/接受/采收门，普通commit许可不豁免这些条件。
6. 提交成功不等于push或部署；push仍单独授权。不把别人的未提交学习答案打包进文档commit。

本轮未改TODO/line源数据，故不为存档触发全量生成；生成视图不手改。若以后修改这些源，依AGENTS运行生成器并限定核结果，不能以“刷新进度”为由采收无关输出。

## 7. 故障与回滚

| 情况 | 动作 |
|---|---|
| 新窗口恢复wrong_repo | 读取本会话binding的repo/task/entry，显式切到对应根验证并重开正本；不按cwd猜任务 |
| 429或代理连接失败 | 保存未查范围，主线程继续不依赖项；独立审保持OPEN，不无限重试 |
| 保存冲突/来源缺失 | 保留输入与旧身份，查看实际版本；不悄悄改成同名对象/最新版 |
| 浏览器测试失败而后端通过 | 按浏览器失败定位，不拿后端绿灯覆盖；用新隔离根复验 |
| Git出现新增他窗改动 | 刷新归属清单，仅动自己的hunk；不清理或强行提交 |
| 想撤回本次文档包 | 找本任务实际commit，核后续引用，再审阅式撤回自有七文档/三路由增量；不逆转上游决定 |
| 想撤回A/B或WP0 | 依原before/patch/合同逐hunk处理，保留前序A和他窗代码；没有授权不执行 |

## 8. 日常维护的最小记录

每次收尾只需更新实际发生变化的任务/回执和当前入口：本次做了什么、检查了什么、还欠什么、下一动作、commit/push/runtime各自状态。历史失败与当时依据保留，不能把旧回执改成今天状态。新增设计回写架构/合同，重复操作方法回写本手册；工作日志不变成第二本手册。
