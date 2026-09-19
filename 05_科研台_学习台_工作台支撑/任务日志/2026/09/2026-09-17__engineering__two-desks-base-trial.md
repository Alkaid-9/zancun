---
id: TASK-20260917-005
title: NotEMD与LearnGraph底座串接试用
date: 2026-09-17
runtime:
  model: GPT-6
  effort: UNKNOWN
  effort_source: 当前系统未提供推理档位；交互式有界试用
  launch: Codex 当前交互会话
type: engineering
status: completed_with_open_gates
area: research-desk
project: research-desk
todo_ids: []
owners:
  - user
related:
  - progress/decisions/2026-09-17__research__two-desks-purpose-redefinition-proposal.md
  - progress/task_logs/2026/09/2026-09-17__research__two-desks-panorama-and-reference-list-review.md
---

# 目标与授权

用户选中 object/view 职责框架后要求“要不我们先试试缝起来，然后先用着？”，并追加“然后再往我们的架构里去调”。本任务先恢复并串接可实际使用的参考底座，之后根据试用缺口逐步适配；不把此前的四类职责自动扩大为四个仓库的采用或完整重构。

# 当前范围

- NotEMD 与 LearnGraph 的独立本地试用，首个材料沿用正在讨论的 EdgeIM 论文。
- 在专用试用目录保存材料、学习入口和研究问题种子，验证跨工具关联与保存恢复。
- 保留原论文、真实库、既有8878试用服务及其他窗口写域；不提交或部署。
- 模型服务选择已向用户异步询问；先完成不依赖模型的准备，不自行选用新的付费服务或复制无关应用凭据。
- 一个只读子代理检查 LearnGraph API/路由与启动路径；主线程检查 NotEMD、运行环境并独占所有写入。

# 已知基线

- LearnGraph 本地提交：`a3e4c87160727293c79880d4aeea6dfa132d49fd`，工作树未见改动；运行快照在 `LearnGraph-runtime-20260830/runtime-state.tar.zst`。
- MAS vault 的 NotEMD `1.9.7` 插件文件存在，但 `community-plugins.json` 与插件 `data.json` 不存在；没有当前启用/模型配置证据。
- 现有科研台8878监听仍在；本任务不复用其真实记录存储。
- task_id 由中央发号接口取得，非手工编号。

# 验收目标

1. LearnGraph 本地页面与 API 可用，可重新打开已保存的试用材料和记录。
2. 同一材料能从笔记进入学习，并把新问题或学习记录带回持久笔记；明确自动接通与手动步骤。
3. NotEMD 插件在专用 vault 就绪；模型连接与AI处理结果须独立验证，未完成不得称全链通过。
4. 提供明确启动、停止、试用入口、已知限制与下一步；用户真实使用门保持开放。

# 尚未完成

运行恢复与基本桥接交互验证已完成；模型配置/AI功能、非空学习对话导出、GitHub远端创建/私有性核验/推送与真实用户试用仍开放。以末尾验收附记为最新状态。

# 风险与回滚

新增试用目录与本任务日志/索引为本轮写域；停止本轮进程后可撤回新增试用目录。正式架构和旧验收状态不因试用改写。

## Amendment

待本轮进展追加。

### 2026-09-17 — Github资料层与本地运行恢复检查点

- 用户追加“资料同步要不用github吧”“Obsidian的同步好贵”，随后明确选择新建：“新建吧？复用的架构不清晰”。建议新私有资料仓名称 `research-garden`（学习与研究园地）；用户另提出明天整理 `/mnt/d/MyResearch`。后者先记录整理清单，不立即移动旧项目。
- 新试用根：`/mnt/d/MyResearch/two-desks-trial-20260917`；资料 vault：其下 `materials/`，已初始化独立 `main` Git 仓；`README.md` 保存试用入口、同步边界和明日整理清单。
- 可重建运行缓存：`/home/alkaid/.cache/two-desks-trial-20260917/learngraph`。原持久快照保留。最初NTFS恢复过慢已中止，已删除本轮未完成副本；历史 `LearnGraph-runtime-20260830.incomplete-rsync` 不属于本轮清理写域，未动。
- `trial.py` 从 `trial.json` 读取参数，控制本轮 API/Web 进程；数据和本地密钥在试用根 `state/`，不进入资料仓。状态：18880 health=200，18881 Web=200；3.11解释器与 FastAPI/Uvicorn 导入通过。现有8878未改。
- 真实接口确认 Markdown 与 PDF 可本地解析；demo登录成功；远程模型及固定回答demo provider均未启用。模型服务选择仍等待用户。
- 新增 Obsidian 薄连接插件：材料上传并保留来源链接、人工问题种子写入本地与 LearnGraph memory、记忆/会话按版本导出 Markdown。尚在实际交互核验中，不能仅凭代码宣称全链通过。
- 独立 Obsidian profile 已打开正确专用 vault；19222用于本轮本机交互验证。GitHub SSH核验身份为 `Alkaid-9`，但未检测到 `gh`、GitHub API token或credential helper；已异步请用户创建 `Alkaid-9/research-garden` 私有空仓。远端创建/隐私验证/推送均未完成。
- 资料仓忽略 NotEMD程序与配置、连接插件本机数据、数据库、环境文件、密钥、窗口状态。原论文只复制，原MAS vault设置未改。
- 恢复游标：试用根 README → trial.json/trial.py → 本log最后追加。下一步完成 Obsidian 真操作与 LearnGraph 浏览器保存/重开核验，再更新回执；模型与远端建仓仍是外部输入，不据此伪造完成。

### 2026-09-17 — 本地串接收尾，模型与远端仍开放

- 结论：`LOCAL-BRIDGE-TECH-PASS / MODEL-OPEN / GITHUB-REMOTE-OPEN / USER-TRIAL-OPEN`。完整回执：`/mnt/d/MyResearch/two-desks-trial-20260917/ACCEPTANCE.md`，使用与恢复入口同目录README。
- 实际Obsidian加载NotEMD与连接插件，并导入EdgeIM；LearnGraph保存为 `c07afe78-c4f0-4c48-812c-45ad2500ec8f`，本地对应object `a19aa516-f53a-447c-b924-51aabc84f75d`。后端解析21个内容块，来源链接保留。
- 浏览器发现上游PDF预览错误 `Cannot convert object to primitive value`；定位 `frontend/src/components/resources/document-previewers.tsx:35` 的动态import模块转换，运行副本一行改为 `workerUrl.default`。持久补丁放试用根 `patches/pdf-worker-default.patch`，恢复快照时自动应用；原源码仓未改。浏览器复验7页PDF、首屏像素与视觉检查通过。
- 实际Modal生成明确标注的验证种子，保存到笔记与memory，再导出Markdown；重复导出保留已有文件编辑。验证样例移至试用根 `state/acceptance/generated-verification-notes/`，两个测试memory软删除，不登记个人能力或真实研究结果。
- 18880/18881服务停止重启后，原材料与indexed状态保持。Windows启动器已运行；专用Obsidian和浏览器可用，验证用19222调试端口已关闭。原8878服务未动。
- 独立资料仓 `materials/` 的main初始提交：`2ba7995`；明确选择7个文件提交，工作树干净。远端设为 `git@github.com:Alkaid-9/research-garden.git`，但查询返回Repository not found；未push、未宣称私有远端或云端同步已完成。MAS与外层仓未commit。
- 仍开放：用户选择模型服务（不在聊天里收密钥）；用户建立GitHub私有空仓后核实并push；非空对话导出与真实学习试用。没有模型调用或假模型回答，不宣称NotEMD抽取/学习图谱生成已通过。
- 明日整理请求已落在试用根README的清单：先盘点Git身份、运行者、恢复入口和引用，再讨论正式项目/资料/参考源码/缓存/快照分区；本轮不搬旧项目。
