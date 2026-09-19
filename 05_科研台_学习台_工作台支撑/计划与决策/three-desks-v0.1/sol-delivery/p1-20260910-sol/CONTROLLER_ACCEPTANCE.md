# RD-2 P1 controller acceptance

结论：**CONTROLLER-PASS（保留用户实际使用门）**。

主控在 `/mnt/d/MyResearch/research-desk/acceptance/p1-20260910-sol/controller-validation-2/` 使用全新隔离 SQLite、导出根和 `127.0.0.1:8882`，独立重放当前源码：

- P1 浏览器链 120/120；Legacy 25/25。
- 后端单测 17/17；Python 编译、JS 语法和 2432 项链接检查通过。
- SQLite `integrity_check=ok`，无外键违规；原 `config.local.json` 与基线逐字节一致。
- 直接检查桌面与 390px 移动端四张截图，无溢出、截断、重叠或旧区域泄漏。
- `8882` 已停止，匹配配置的服务进程不存在。

主控重点复核并通过此前未获证明的项目：重启后 Sheet1!R6 原文、完整 anchor 与 Windows 路径；来源加入已有工作区且不新增 workspace；捕获页和工作区未保存正文的保存/丢弃/留下；attempt operator/assistance；三种用途侧栏；对象已保存、workspace 创建失败与 workspace 已创建、打开失败的分阶段诚实状态。

边界：本结论是本地技术验收，不是用户实际使用验收；未 harvest、commit、push、deploy，未接真实数据，未授权 P2/P3/B2/3D。当前工作树有大量他窗修改，后续只能按 `before/` 与 `changes.patch` 做本包范围处理。
