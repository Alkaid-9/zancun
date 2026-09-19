# C00-C03 使用说明

本轮用户体验配置：`/mnt/d/MyResearch/research-desk/acceptance/c03-20260911-sol-c03-113925/user-acceptance/config.user.json`，服务仅监听 `127.0.0.1:8873`。

```bash
/home/alkaid/miniconda3/envs/solver/bin/python /mnt/d/MyResearch/research-desk/app/research_desk.py \
  --config /mnt/d/MyResearch/research-desk/acceptance/c03-20260911-sol-c03-113925/user-acceptance/config.user.json serve
```

打开 `http://127.0.0.1:8873`。该隔离沙箱最初预置一个`EdgeIM 贯穿主题`和一个`EdgeIM 体验工作区`；用户实际体验已经在其中留下新问题、正式关系与继续点，所以它不再是初始空白/干净数据库，但仍不写入真实用户数据库。

首页进入“继续”后选“从资料开始”，从登记目录选择来源；工作簿来源再选择 cell/range。Map 入口显示全局八层与缺口。P1 工作区继续点、来源回链、尝试/反馈和导出路径保持原流程。

完整往返：`HOME → Map/GLOBAL → 打开或创建 EdgeIM 贯穿主题 → Knowledge/Method/Genealogy → 从专题来源开始工作 → 新建或加入工作区 → 保存关系 → 返回原专题`。专题进入工作区会保存 `topic_ref`、来源、中心和选中项；挂起后从 HOME 的“挂起”筛选继续，重启服务仍可返回原专题。Map 会显示每层来源/对象计数、覆盖日期与范围、动作和缺口，领域尺度与来源波次独立列出；EdgeIM 按已登记来源复用已有 Topic，避免重复空 Topic。

并发修改或旧 revision 会显示冲突并保留用户输入；不要静默重试。备份使用 SQLite 一致快照，恢复到新 data 根后检查对象、revision、workspace/view、关系、提案和 return_context，不覆盖当前数据根。验收浏览器报告为 `runtime/c03-browser-report.json`，包含服务启动/停止事件和 8873 端口路径。

本轮记录写入 `data/desk.sqlite3`，导出写入 `exports/`，runtime/logs 可重建。用 SQLite 一致快照备份到新目录后再恢复，不能覆盖原数据根。未接入模型，DEMO 提案必须标明 `proposer=demo`。用户实际验收仍开放。

首次技术复核为check-links 2432/0/0、unittest 21/21、C03 Playwright 17/17。用户体验指出三项问题后，`TASK-20260911-003`限定返修最终复核为unittest 22/22、check-links 2432/0/0、新空根C03 Playwright 22/22、用户复现快照7/7、当前8873只读在线烟测8/8；返修回执见`../../c03-repair/TASK-20260911-003/RECEIPT.md`。当前仍需用户复验，AC03-12未关闭。已知开放项：来源选择仍截断前300项且无检索；保存期间缺少提交中状态与明确成功回执，快速重复点击可能产生重复记录。
