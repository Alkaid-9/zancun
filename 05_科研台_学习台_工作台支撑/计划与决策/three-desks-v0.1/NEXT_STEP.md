# 下一步：用户实际体验RD-2第一波C00–C03

状态：`C00-C03-CONTROLLER-ACCEPTED / USER-ACCEPTANCE-OPEN`。

P1与RD-2第一波均已实施。C00–C03的[接收主控验收](../rd2-construction-v0.3/sol-delivery/20260911-sol-c03-113925/CONTROLLER_REVIEW.md)确认 unittest 21/21、链接检查2432资产零错误零警告、C03 Playwright 17/17；干净沙箱只读烟测也已通过。AC03-12只能由用户实际使用关闭。

C04–C07与画布、3D、工作台派发、TaskQuay、独立仓采收、桌面壳、真实迁移和部署均未启动；先收用户体验反馈。

## 1. 当前试玩入口

使用全新的用户验收沙盒，不碰原`config.local.json`、原工作簿、registry或真实SQLite：

- URL：`http://127.0.0.1:8873/`
- 配置：`/mnt/d/MyResearch/research-desk/acceptance/c03-20260911-sol-c03-113925/user-acceptance/config.user.json`
- 数据：同目录`data/desk.sqlite3`
- 导出、日志：同目录`exports/`、`logs/`

该沙盒是用户体验门的记录，不是未来正式数据位置。用户明确确认前，不把其中内容迁入真实库，不改默认配置。

## 2. 最短验收路线

1. 从 `Map` 进入 GLOBAL，打开 `EdgeIM 贯穿主题`。
2. 切换 Knowledge、Method、Genealogy，观察正式关系和待确认关系是否容易区分。
3. 点“从专题来源开始工作”，进入预置的 `EdgeIM 体验工作区`。
4. 查看来源、关系与继续点，再点“返回原专题”。
5. 反馈哪里找不到、哪一步不自然、哪些词不清楚、哪些行为与预期不同。

用户只需反馈四类信息：哪里找不到、哪一步不自然、哪些词看不懂、哪些能力与预期不同。无需重复机器检查。发现问题先记C00–C03用户验收修复项；没有用户明确选择，不开始C04。

## 3. 技术边界

当前已有来源／自由捕获、工作区、草稿、Attempt/Feedback、历史/冲突、挂起恢复、选择下载、自然资料入口、关系／提案，以及GLOBAL—TOPIC—来源—WORKSPACE回流。共同画布、完整菌丝网络、真实工作台派发、学习评价、桌面壳和服务器部署仍是后续包。

应用没有独立Git仓；C00–C03版本证据为`acceptance/c03-20260911-sol-c03-113925/before/`及`changes.patch`。用户验收结束后再决定先修问题还是启动独立仓采收；不以MAS文档提交或外层空diff作为应用源码已提交证据。
