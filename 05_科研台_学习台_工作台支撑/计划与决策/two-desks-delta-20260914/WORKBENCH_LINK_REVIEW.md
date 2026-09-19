# 工作台接续的接口核验（TASK-20260915-013）

日期：2026-09-15。范围：旧共享服务与WP0隔离实现的Task字段/接口及人工回链边界。来源：只读子代理`/root/workbench_link_readonly`终态complete；主线程定向回查共享http.py与隔离loader/writer/events关键符号。未跑WP0测试、未探测live版本、未审进组/课程/sealed。

## 已确认的边界

1. Task十字段没有一等`origin_ref/request_id/artifacts`；`acceptance`可记验收文本，`current`可放恢复指针。隔离[loader.py:17](/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901/tools/dashboard/taskstore/loader.py:17)列`TASK_FIELDS`；[writer.py:189](/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901/tools/dashboard/taskstore/writer.py:189)拒绝unknown fields。不能手加frontmatter后说是受支持接口。
2. [events.py:17](/mnt/d/MyResearch/MAS_Safety_Project-wb2-wp0-20260901/tools/dashboard/taskstore/events.py:17)有artifact_linked，但payload宽松不等于完整schema冻结。跨台origin/request映射仍是[WORKBENCH提案](../three-desks-v0.1/WORKBENCH.md:50)。
3. 共享[http.py:160](/mnt/d/MyResearch/MAS_Safety_Project/tools/dashboard/service/http.py:160)可读/progress/**；[http.py:232](/mnt/d/MyResearch/MAS_Safety_Project/tools/dashboard/service/http.py:232)旧POST /api/task调用update_todo_task，不是Task日志写入器。
4. 隔离实现只有GET /api/tasks.json和GET /api/task/<id>.json；无taskstore HTTP写端点，GET不重建派生DB。当前共享源码没有这些Task GET，不能从allocator能签号推断WP0已经加载。
5. WP0精确采收/异构审/用户接受/服务加载门仍见[原交接§3](../../handoff/2026-09-01__workbench-v2-wp0-codex-execution__handoff.md:84)。不得整体复制http.py，隔离树含旧复合改动；普通commit许可不取消这些门。

## 可推进与不可假称

在不改WP0、不重启8899前，可以使用既有Task正文/CURRENT/EVENTS文本及科研台普通记录保留原问题、任务、产物和验收的明确双向引用；这是人工接续，不是自动调度/自动回传，也不是新schema。若增加应用入口，必须说明只做导航/引用，不代替任务权威或推造HTTP写接口。

本核验提供N3实施范围证据，不等于WP0异构审、A/B独立代码审、用户试用或live验收。下一步：先完成N2应用checkpoint，再对人工接续的实际入口/返回需求制定并实施最小差异；自动接驳必须另过原门。

## 未查面

代理未重读Git/各Lot回执、未联网/探测运行态或执行测试；主线程的当前Git/端口观察记录在TASK-013，不能由静态文件推出服务部署状态。独立结果只覆盖以上字段/接口/权限问题。

## N3源码追加审查（同一只读代理，有效终态complete）

N2提交b54ea71后，代理只读审查N3的app.js新函数、b.js的initialBody预填、N3合同及16/16报告，发现两项：

1. 主问题：p1SaveBody用p1ReplaceObject替换数组中的对象（app.js约1318行），但工作区按钮闭包仍捕获原selected（约1452行），直接生成时revision可能仍是r1而真实保存已到r2。必须在生成时重取当前对象，不能靠首轮测试通过关闭。
2. 次问题：继续点只更新p1.resumeIntent，交接refresh原来只绑任务/产物输入；面板打开后改继续点再复制可能取旧值。复制/保存前需重新生成。

代理未见自动派发/Task schema变化、错身份回退、原正文被N3改写等额外违约；但没有运行测试、没有审A/B全包或WP0。主线程将两发现转成定向回归并保存RED/最终结果，修复状态以N3回执为准；本节不是提前签PASS。

## 修复终审与证据闭环

第一轮RED 2/3复现保存后旧revision；重取当前record/view/workspace，并在copy/save前刷新继续点后18/18。后续静态审又发现面板打开后再改正文仍能复制；第二RED 6/7复现。refresh集中检查脏稿，清空无效包、返回false，copy/save立即停止后，最终final-v2为20/20。

同一代理最后有效终态complete，静态核见三发现均收敛，未见新合同阻断：app.js:1482脏稿门、1488当前身份、1490继续点、1497复制/保存门；manual_workbench_check.py:90覆盖面板后二次编辑。主线程沿源码抽查并亲自运行，修后B27/27、A38/38、C0322/22、后端28/28。准确报告与失败现场见[N3回执](/mnt/d/MyResearch/research-desk/acceptance/n3-TASK-20260915-013/RECEIPT.md)。

结论仅SCOPED-STATIC-REVIEW-PASS；代理没有亲自启服务或运行测试，不等于WP0异构验收、A/B完整代码审或真实用户接受。接口核验时的旧“下一步先做N2”由TASK-013当前进度取代，不改原静态依据。
