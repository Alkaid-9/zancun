complete

# C00-C03 接收主控技术验收

日期：2026-09-11。对象：`TASK-20260911-002` / `20260911-sol-c03-113925`。

结论：接收主控独立重放通过，第一波状态为 `CONTROLLER-ACCEPTED / USER-ACCEPTANCE-OPEN`。AC03-12 只能由用户实际使用关闭；本结论不代表 RD-2、七图、工业资料、学习台或科研台整体完成。

主控复跑：

- solver 门禁：`Environment OK: solver`，解释器 `/home/alkaid/miniconda3/envs/solver/bin/python`。
- 完整 unittest：21/21 OK。
- 本轮 `config.build.json` 链接检查：2432 assets，0 errors，0 warnings。
- C03 Playwright：17/17 passed；覆盖 GLOBAL 字段、三投影、pending 边、换中心返回、专题来源进入新建和已有工作区、人工关系、草稿线、挂起重启、返回原专题、桌面和 390px 布局。
- 差异证据：相对 2026-09-10 P1 before 的 `changes.patch` 共 2243 行。

证据入口：应用 `acceptance/c03-20260911-sol-c03-113925/evidence.json`、`runtime/c03-browser-report.json`；干净用户沙箱只读烟测为 `user-acceptance/runtime/user-acceptance-smoke.json`；Sol 回执为同目录 `RECEIPT.md`。

边界：原配置、registry、真实资料和真实记录库未改；验收只写隔离根。C04-C07与X-*未启动。主控验收时未commit、push、deploy；其后用户只授权提交MAS仓内文档与证据，科研台应用源码仍没有独立Git版本，未push/deploy。

用户体验入口：使用 `user-acceptance/config.user.json` 启动或继续访问 `http://127.0.0.1:8873`，走 `HOME -> Map -> EdgeIM 贯穿主题 -> 来源 -> EdgeIM 体验工作区 -> 返回原专题`，记录找不到、不自然、术语不清或预期差异。干净沙箱只读烟测已通过且数据库哈希前后不变；AC03-12 仍只能由用户实际使用关闭。

## 用户体验与限定返修 Amendment

用户实际体验后明确不签`USER-ACCEPTED`，总状态保持`CONTROLLER-ACCEPTED / USER-ACCEPTANCE-OPEN`。用户数据库已经写入两条同名问题、一条`prerequisite / personal_hypothesis`正式关系和继续点；上段“数据库哈希前后不变”只描述返修前那次只读烟测，不能描述当前数据库内容。

用户重新打开AC03-04和AC03-10，并指出非工作簿来源错误显示。`TASK-20260911-003`仅修这三项，控制器最终复验为unittest 22/22、check-links 2432/0/0、新空根C03 Playwright 22/22、用户复现快照7/7、当前8873只读在线烟测8/8。AC03-04/10现在为`CONTROLLER-REPAIR-PASS / USER-RECHECK-OPEN`；来源列表截断无检索和保存提交态/重复点击仍开放。返修回执见`../../c03-repair/TASK-20260911-003/RECEIPT.md`。
