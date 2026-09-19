# C03用户体验返修回执

日期：2026-09-11。任务：`TASK-20260911-003`。状态：`CONTROLLER-REPAIR-PASS / USER-ACCEPTANCE-OPEN`。

## 用户判定与范围

用户没有签署`USER-ACCEPTED`。C00–C03技术包仍为4/4，C04–C07未启动。本任务只返修用户实际体验指出的前三项：非工作簿来源错误渲染、专题成员关系回流缺失、同端点边与标签重叠；AC03-12继续开放。

用户验收数据库原样保留了两条同名问题、`prerequisite / personal_hypothesis`正式关系、挂起与继续点。开工前使用SQLite一致快照保存到应用证据根`acceptance/c03-repair-20260911-task003/evidence/user-repro.sqlite3`。

## 修复

- 非工作簿`registered_asset`改走资产来源读取并显示摘要、整份来源定位和原件路径；不再拼接工作簿字段，也不再永久显示“正在读取原段”。
- Topic作为图中心时，把`attrs.topic_ref`指向该Topic的工作区成员纳入专题作用域；关系任一端属于该作用域即可进入Topic投影。成员自身作为中心时仍保持一跳查询，不引入递归图语言。
- 同端点正式边与待确认边按稳定通道分线；图内使用短编号标记，图外图例逐行显示正式／待确认状态、关系类型和端点，避免长文字压在线上。SVG边与编号记录`data-edge-id`供回流验收定位。

## 控制器复验

- 完整unittest：22/22 OK，其中新增Topic关联工作区任意成员关系测试。
- `check-links`：2432 assets，0 errors，0 warnings。
- 新空数据根C03 Playwright：22/22 passed；新增非工作簿终态、同端点编号不重叠、图例可读、任意专题成员关系返回可见五项断言。
- 用户复现数据库快照只读复验：7/7 passed；真实`obj_4032adbd3d994e079f4acc690688bb51`关系返回Topic后可见，Method标签框不重叠，来源无`undefined`或永久加载，快照哈希前后不变。
- 当前8873数据库只读在线烟测：8/8 passed；服务返回200，编号图例与关系回流可见，烟测前后当前数据库文件哈希一致。该哈希仅证明本次烟测没有写入，不代表数据库回到交付前状态。

应用证据根：`/mnt/d/MyResearch/research-desk/acceptance/c03-repair-20260911-task003/`。关键报告：`test6-runtime/c03-browser-report.json`、`repro-runtime/user-repro-recheck.json`、`live-runtime/live-readonly-smoke.json`、`changes.patch`；最终截图为`test6-runtime/c03-desktop.png`、`test6-runtime/c03-mobile-390.png`与`live-runtime/method-parallel-edges-final.png`，来源终态截图保留在`repro-runtime/registered-asset-source-fixed.png`。

## 开放项

- 问题4：2432资产入口仍是截断到前300项、无检索的原生下拉框。
- 问题5：首次保存缺少提交中状态和明确成功回执，快速重复点击可能产生重复记录。
- 上述两项不在本次1–3返修范围；用户复验前三项后再决定是否进入下一次C03返修。AC03-12保持`USER-OPEN`。

当前体验入口仍为`http://127.0.0.1:8873`，配置与数据库路径不变。未迁移真实数据，未启动C04–C07，未push/deploy；科研台应用仍无独立Git版本。
