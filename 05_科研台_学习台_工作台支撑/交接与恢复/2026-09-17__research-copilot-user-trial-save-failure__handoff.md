# 科研驾驶舱 G0 后首次用户试用：保存未发生

日期：2026-09-17。关联任务：`TASK-20260916-009`（G0已收口）、`TASK-20260915-017`（隔离用户试用现场）。状态：`USER-TRIAL-RED / SAVE-NOT-REQUESTED / ROOT-CAUSE-OPEN / PAUSED`。

## 0. 一句话结论

用户打开8878隔离DEMO后明确反馈“没有保存”。服务日志显示本次交互只有GET，没有任何POST／PUT，因此只能确认“保存请求没有到达后端”，不能称已保存、用户操作错误、后端写入失败或已定位根因。P1a仍不启动。

## 1. 当前现场

- URL：`http://127.0.0.1:8878`，2026-09-17现场探测HTTP 200。
- 进程：PID 8705，自2026-09-16 22:29:13运行。
- 命令：`/home/alkaid/miniconda3/envs/solver/bin/python app/research_desk.py --config acceptance/user-trial-TASK-20260915-017/config.demo.json serve`。
- 数据：`acceptance/user-trial-TASK-20260915-017/data/desk.sqlite3`存在；这只说明隔离数据库文件存在，不证明用户本次输入已写入。
- Git：试用目录下`data/`未跟踪；不得把运行数据称为已Git采收或完整备份。
- 服务日志：用户操作时可见首页、静态文件、catalog、workspaces、map、goals、knowledge等GET；未见POST／PUT保存请求。

## 2. 已做与未做

已做：核8878监听、HTTP、PID、启动配置、试用目录、服务日志和Git状态；确认保存请求未到后端。

未做：没有读取或改写真实数据库；没有删除／迁移隔离库；没有重启服务；没有修改前端或后端；没有代用户重复提交；没有用自动测试冒充用户路径；没有判断是按钮未触发、前端校验、页面状态、浏览器缓存、交互误解还是其他原因。

## 3. 下次第一动作

1. 先向用户取得失败时所在页面、所点按钮、页面提示及一张截图；不要让用户从头盲试整套流程。
2. 在同一隔离配置复现那一条精确路径，同时观察浏览器console/network和服务日志。
3. 若按钮没有发请求，定位前端状态／事件路径；若发出请求但日志仍无记录，检查浏览器地址、缓存和请求目标；若后端收到请求，再检查响应与数据库写入。
4. 根因明确后另领修复任务，先写最小复现和验收标准，再修改应用；修复后由用户只重试失败步骤。

## 4. 验收标准

- 点击明确保存命令后出现一次可辨识POST／PUT及成功响应；失败时页面必须显示原因且输入保留。
- 页面给出保存成功对象ID／revision或等价可回读身份；刷新页面后能从同一隔离库重新找到。
- 不重复创建、不覆盖旧版本、不把前端提示当数据库证据。
- 用户重试原失败步骤并明确确认保存行为可理解、结果可找到，才可把该路径从RED改为USER-OBSERVED-PASS。

## 5. 边界与恢复

G0仍为`COMPLETE_WITH_OPEN_GATES`；本次RED属于G0后的用户试用门，不推翻事实／语义冻结，也不允许绕过问题直接施工P1a。保持8878现场和`data/desk.sqlite3`不动；不要reset、clean、删除未跟踪data或覆盖server.log。没有明确修复授权前，只做只读诊断和交接。

恢复时依次阅读本页、[G0交接](2026-09-17__research-copilot-cockpit-g0__handoff.md)及试用现场`/mnt/d/MyResearch/research-desk/acceptance/user-trial-TASK-20260915-017/README.md`。
