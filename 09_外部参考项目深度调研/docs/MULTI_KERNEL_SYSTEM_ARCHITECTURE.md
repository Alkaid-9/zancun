# 四核驱动统一系统架构方案与工程分工说明书
## Multi-Kernel Agent System Architecture (MKASA)

- **编制日期**：2026-09-19
- **归档路径**：`09_外部参考项目深度调研/docs/MULTI_KERNEL_SYSTEM_ARCHITECTURE.md`
- **设计目标**：将 2026-09 外部调研提纯的四大硬核项目（Prime-Agent, Moraine-Home, OpenViking, LoopX）深度融合，构建一套专为鲁组学术科研（并发 Bug 挖掘、Petri 网形式化建模）与“科研台/学习台/工作台”支撑的生产级高自主、强类型、零虚标统一控制底座。

---

## 一、架构总览与拓扑设计

MKASA（四核架构）彻底摒弃业界将大模型与未受保护的文件系统、无状态单轮 Prompt 粗暴拼装的脆弱范式，构建了自顶向下的四层防御与驱动模型：

```
                    ┌────────────────────────────────────────────────────────┐
                    │               用户人机协同与顶层交互界面               │
                    │         (Claude Code / Web PWA / CLI Dashboard)        │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                                ▼
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. 调度执行内核 (Scheduling Kernel · 提纯自 Prime-Agent)                                  │
│    - RLM (Recursive Language Model) REPL 变量化控制流                                     │
│    - 子代理沙箱化函数调用 (Subagent as Function Call)                                     │
│    - 持续微调 Harness 轨迹留痕 (Trajectory & Heartbeat)                                   │
└───────────────────────┬─────────────────────────────────────────────────┬──────────────────┘
                        │                                                 │
                        ▼                                                 ▼
┌─────────────────────────────────────────────────┐ ┌────────────────────────────────────────────────┐
│ 2. 记忆治理内核 (Memory Kernel · 提纯自 Moraine)│ │ 3. 上下文文件系统 (Context FS · 提纯自 OpenViking)│
│    - 双时态半开区间: [valid_from, valid_to)      │ │    - viking:// POSIX 风格语义虚拟目录树         │
│    - 绝对保守抽取式去重 (Extractive Deduplication)│ │    - L0(摘要)/L1(大纲字典)/L2(定理全文) 分级装配 │
│    - Self-Core 严格字符预算投影                  │ │    - 跨线程异步解耦信号量 (MinimalAsyncSemaphore) │
│    - SHA-256 密码学可逆决策账本与回滚           │ │    - AGPL-3.0 协议隔离安全边界                  │
└───────────────────────┬─────────────────────────┘ └─────────────────┬──────────────────────────────┘
                        │                                             │
                        └───────────────────────┬─────────────────────┘
                                                │
                                                ▼
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│ 4. 控制平面与安全内核 (Control Plane & Security Kernel · 提纯自 LoopX)                     │
│    - CAS (Compare-And-Swap) 乐观并发任务租约栅栏 (Task Lease Fence & Epoch)                │
│    - 细粒度写作用域 (Write Scopes) 前缀与 Glob 通配排他重叠检测                           │
│    - 四态任务生命周期 (Pending -> Current -> Delivered / Not_Required)                     │
│    - 最低交付门槛 (Outcome Floor): 强制要求 产物 + 定向测试 + 状态回写                      │
│    - 确定性 PreToolUse 策略门禁: Fail-Closed 阻断, 越界写防御与高危 Bash 熔断              │
└───────────────────────────────────────────────┬────────────────────────────────────────────┘
                                                │ 原子写入 / 磁盘文件持久化
                                                ▼
                    ┌────────────────────────────────────────────────────────┐
                    │                    真实物理工作空间                    │
                    │ (05_科研台/src, ACTIVE_GOAL_STATE.md, task-leases/*.json)│
                    └────────────────────────────────────────────────────────┘
```

---

## 二、四大内核职责与接口规约

### 1. 调度执行内核（Scheduling Kernel）
- **核心定位**：任务计算与复杂推理中枢。
- **技术突破**：
  - 将中间步骤完全变量化（如 `$var = call_subagent(...)`），不将数百行中间冗余文本拼接进下一轮 Prompt，避免上下文雪崩；
  - 维护 REPL 执行环境，执行失败支持基于变量状态的回溯重试。
- **接口输出契约**：
  ```json
  {
    "execution_id": "exec_20260919_001",
    "status": "success",
    "variables": { "target_petri_net": "net_model_v1", "deadlock_detected": true },
    "token_spent": 1420,
    "trajectory_receipt": "sha256:abc..."
  }
  ```

### 2. 记忆治理内核（Memory Governance Kernel）
- **核心定位**：长程事实、科研偏好与伴侣情感的终身免幻觉持久化。
- **技术突破**：
  - **双时态切分**：将事实物理成立时间与系统记账时间分离，历史变更事实软失效但不物理删除；
  - **非改写式去重**：坚决禁止 LLM 模糊改写记忆，仅在字面完全一致或完全字面蕴含（`subsumed_verbatim`）时合并；
  - **Self-Core 投影**：对核心身份与不可违背原则设置硬字数预算（如 400 字符），超出硬截断并预警。
- **核心文件映射**：`prototypes/minimal_moraine_kernel.py`

### 3. 上下文文件系统内核（Context FS Kernel）
- **核心定位**：20+ 页学术长论文与形式化证明的自适应加载底座。
- **技术突破**：
  - 论文按虚拟路径组织（如 `viking://papers/concurrency/edge_im_2020.pdf/l1`）；
  - 先以 L0 摘要广度定位（~100 tokens），再以 L1 提纲构建符号空间（~1.5k tokens），仅对高相关具体定理段（Score $\ge 0.85$）动态挂载 L2 全文；
  - 保证在严苛的 Token 预算（如单次提示词中仅留 180~2000 tokens 给背景上下文）下，数学证明上下文永不断裂。
- **核心文件映射**：`prototypes/minimal_openviking_kernel.py`

### 4. 控制平面与安全内核（Control Plane & Security Kernel）
- **核心定位**：多 Agent 并发隔离、跨窗口状态接力与物理安全门禁。
- **技术突破**：
  - **CAS 租约栅栏**：多 Agent 同时领任务时，凭 `(version, lease_epoch, idempotency_key)` 抢占写锁，支持幂等重放与租约转移；
  - **细粒度写作用域**：允许 Agent-A 写 `05_科研台/src/*` 的同时，Agent-B 写 `09_外部参考/docs/*`，只有当作用域发生 Glob 冲突时才排他；
  - **Outcome Floor 最低交付硬门槛**：没有真实产物路径、定向测试通过输出与状态回写指纹，禁止将任务标记为已完成；
  - **PreToolUse 策略拦截**：越权写文件与破坏性 Bash（`rm -rf`, `git reset --hard` 等）物理不可执行。
- **核心文件映射**：`prototypes/minimal_loopx_kernel.py`

---

## 三、文件组织结构与模块分工方案

```
05_科研台_学习台_工作台支撑/ (或未来集成根目录)
├── core/                                    # 四核算法纯原生层 (零依赖)
│   ├── scheduling/                          # 调度执行核 (Prime-Agent)
│   │   ├── repl_interpreter.py              # 变量化 REPL 执行引擎
│   │   └── subagent_harness.py              # 子代理沙箱调度
│   ├── memory/                              # 记忆治理核 (Moraine)
│   │   ├── temporal_engine.py               # 双时态半开区间计算
│   │   ├── extractive_dedup.py              # 保守抽取式去重
│   │   └── decision_ledger.py               # 密码学可逆账本
│   ├── context_fs/                          # 虚拟文件系统核 (OpenViking)
│   │   ├── semantic_tree.py                 # viking:// POSIX 语义树
│   │   ├── tiered_assembler.py              # L0/L1/L2 分级动态装配器
│   │   └── async_scheduler.py               # 跨线程解耦信号量
│   └── control_plane/                       # 控制平面与门禁核 (LoopX)
│       ├── task_lease_engine.py             # CAS 租约栅栏与代际推进
│       ├── write_scope_matcher.py           # 细粒度写范围 Glob 冲突排他
│       └── outcome_floor_gate.py            # 最低交付门槛验收状态机
│
├── interfaces/                              # 外部驱动与宿主挂载面
│   ├── claude_hooks/                        # Claude Code 原生 Hooks
│   │   ├── hooks.json                       # PreToolUse 注册描述
│   │   └── goal_policy_gate.py              # 拦截越界写与高危命令
│   └── mcp_servers/                         # MCP 标准化服务适配器
│       ├── memory_mcp.py                    # 记忆增删改查标准 MCP
│       └── task_lease_mcp.py                # 任务认领与租约持有 MCP
│
└── blueprints/                              # 业务场景契约定义 (JSON Schema)
    ├── academic_papers_contract.json        # 鲁组 10 篇并发论文分级挂载契约
    ├── companion_memory_contract.json       # 张重熙伴侣双时态契约
    └── task_delivery_contract.json          # 工作台任务交接与交付凭据契约
```

---

## 四、三大台（科研台 / 学习台 / 工作台）物理职责分工方案

| 业务台槽位 | 核心承载功能 | 赋能内核与模块 | 输入产物与职责边界 |
|---|---|---|---|
| **科研台 (Research Desk)** | 鲁组并发论文检索、形式化定理分析、Petri 网验证与死锁重现 | **Context FS 核** + **Scheduling 核** | 维护 `viking://papers/` 目录；对 10 篇论文提取 L0/L1/L2；驱动并发漏洞挖掘 Agent。 |
| **学习台 (Learning Desk)** | 进组新人培训体系、AI 工程实训、MCP 标准规范与符号主义本体论 | **Scheduling 核** (教学 Skill) + **Context FS 核** | 挂载 523 课从零精通课程体系；提供交互式教学引导，隔离学习产物与生产代码。 |
| **工作台 (Workbench)** | 日常多 Agent 任务流水线、跨窗口交接管理（`TASK-20260918-005`）与系统维护 | **Control Plane 核** + **Memory 核** | 管理 `task-leases/` 与任务状态机；执行 Outcome Floor 严格验收；维护跨窗口交接收据。 |
| **生活向伴侣专区 (Cyber-Companion)** | 张重熙伴侣长程情感对话、记忆沉淀与事实修正 | **Memory 核** (双时态) | 物理隔离在 `Workspace/Personal/`；执行双时态清洗与 CPU 本地向量检索，保障绝对隐私。 |
