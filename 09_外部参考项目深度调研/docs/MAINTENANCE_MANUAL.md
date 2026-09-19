# 多核驱动系统维护手册与故障排查指南 (Maintenance & Troubleshooting Manual)

- **适用对象**：系统维护工程师、工作台主控 Agent 与安全审计员
- **归档路径**：`09_外部参考项目深度调研/docs/MAINTENANCE_MANUAL.md`
- **核心目标**：保障四核驱动架构长期稳定运行，固化红蓝对抗排查出的暗坑防御规约，提供确定性的故障排查与自愈 SOP。

---

## 一、架构红蓝对抗安全防护铁律（Anti-Pattern Defense Rules）

依据对 Prime-Agent、Moraine-Home、OpenViking、LoopX 四仓的逐行源码审计结果，系统运维必须恪守以下 5 项防御铁律：

### 铁律 1：严禁依赖单层 Python 字符串匹配做操作系统级安全沙箱
- **源码陷阱定位**：`loopx/claude_goal_mode/hooks/goal_policy.py:63-66`
- **风险描述**：仅对字面量 `rm -rf` 进行子串扫描，易被 `base64 -d | sh`、环境变量别名或多空格分隔绕过。
- **运维规范**：
  1. Claude Code 运行的操作系统账号严禁赋予 `sudo` 无密权限；
  2. 高风险任务（如运行未受信任的代码微调）必须在 Docker 隔离沙箱或独立工作目录中执行；
  3. PreToolUse 钩子仅作为第一道防手滑护栏，底层安全由操作系统用户权限闭环。

### 铁律 2：长程任务必须挂载心跳自动续约（Heartbeat Auto-Renew）
- **源码陷阱定位**：`loopx/control_plane/work_items/task_lease.py:53-54`（默认 TTL 2700 秒）
- **风险描述**：执行长时任务（如大型测试跑 1 小时）中途租约自然过期，后入 Agent 抢占租约修改同名文件，引发幽灵并发写碰撞。
- **运维规范**：
  1. 任何预期执行时间 $> 30$ 分钟的任务，必须在后台启动异步续约协程，每 15 分钟调用一次 `engine.renew(expected_version=...)`；
  2. 任务执行完成后，必须在 `finally` 块中显式执行 `engine.release(...)`，严禁让锁悬挂至 TTL 自然到期。

### 铁律 3：生产环境全面绝育 `handoff_mode: "legacy"` 双轨兼容模式
- **源码陷阱定位**：`loopx/control_plane/todos/handoff_mode.py:6-9`
- **风险描述**：`legacy` 模式允许 Markdown 前言的 `claimed_by` 与磁盘 JSON 租约并存，官方代码承认该设计会产生脑裂。
- **运维规范**：
  1. 所有工作台目标的 `ACTIVE_GOAL_STATE.md` 前言中，**必须显式声明 `handoff_mode: hard_lease`**；
  2. 运维巡检脚本定时扫描 `.task-leases/` 目录，若发现未持租约但标记领取的 Todo，强制触发报警并重置为 `pending`。

### 铁律 4：向量与语义提取模块严禁在主事件循环中同步冷加载
- **源码陷阱定位**：`moraine/search.py`（FastEmbed 初次加载权重需 3~8 秒）
- **风险描述**：多线程环境下若多个 Agent 同时触发冷启动，会导致主进程 GIL 锁死并引发 HTTP 请求超时。
- **运维规范**：
  1. 采用单例延迟加载模式，并在初始化阶段加互斥锁（`threading.Lock`）；
  2. 生产环境中推荐将文本切片与向量提取下沉为独立守护进程，主交互界面仅通过标准接口通信。

### 铁律 5：OpenViking 16k 字符截断陷阱防御
- **源码陷阱定位**：`openviking/parsers/text.py:85`（硬编码 `chunk_size = 16384`）
- **风险描述**：20+ 页数学证明与长形式化定理（如 Petri 网可达树矩阵）若跨越 16k 边界，会被生硬切碎导致语义断裂。
- **运维规范**：
  1. 针对学术论文解析，严禁依赖简单字符计数分块；
  2. 强制使用 AST 或 Markdown 标题层级（`## Definition`, `## Theorem`）作为硬性语义保护边界，在章节内部保持完整。

---

## 二、常见故障排查矩阵（Troubleshooting Matrix）

| 故障现象 / 错误代码 | 底层触发原因 | 应急排查命令 | 标准修复与自愈 SOP |
|---|---|---|---|
| **`version_mismatch` (CAS 乐观锁冲突)** | 其他 Agent 已修改了该任务租约，或当前 Agent 使用了陈旧版本号 | `python3 -c "from minimal_loopx_kernel import engine; print(engine.leases['TODO_ID'].to_dict())"` | 重新调用 `inspect` 读取最新 `version`；若任务确由他人持有，主动排队或放弃认领。 |
| **`write_scope_conflict` (写范围冲突)** | 试图修改的文件路径与另一正在执行的任务的写作用域发生重叠 | 检查当前所有活跃租约的 `write_scopes` 列表 | 检查是否作用域配置过于宽泛（如配置了 `*`）；将写范围缩小到具体子模块路径后重试。 |
| **`Outcome Floor missing` (拒绝交付)** | 交付任务时缺失产物路径、测试通过证明或状态写回哈希 | 检查 `contract.deliver_task` 的三个必填参数是否为空 | 执行单元测试（如 `pytest`），获取真实测试日志输出与 Git Commit 哈希，填充后再行提交。 |
| **PreToolUse 报 `outside authorized write_scopes`** | Agent 试图通过 `Edit`/`Write` 修改超出自身租约范围的文件 | 查看工具调用的 `file_path` 参数与任务租约的作用域配置 | 严禁越权修改！若确需修改全局共享配置，应先向系统申请扩大作用域，或交由协调 Agent 统一修改。 |
| **租约死锁 / 孤儿租约（Orphan Lease）** | Agent 进程异常崩溃（如 OOM 或网络断开），导致租约未正常 release | 检查租约文件的 `expires_at` 与当前系统时间对比 | 若 `now >= expires_at`，引擎将自动判定为失效；若需紧急恢复，运维人员可使用管理员凭证强制调用 `release`。 |

---

## 三、租约与持久化文件清理规范

1. **临时锁目录巡检**：
   - 租约文件物理存放于 `.task-leases/`；
   - 每周一凌晨由定时任务清理状态为 `released` 或过期超过 7 天的历史 JSON 收据，归档至 `task-leases/archive/`。
2. **Git 仓库健康守护**：
   - 任何第三方克隆的外部仓库一律存放在受 `.gitignore` 保护的临时目录（如 `receipts/repos/`）；
   - 严禁将数万行第三方 Node_modules 或 `.git` 子目录直接提交到主工作台 Git 树中。
