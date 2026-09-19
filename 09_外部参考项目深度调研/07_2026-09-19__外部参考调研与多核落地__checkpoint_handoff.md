# 07 · 2026-09-19 外部参考调研与多核落地 Checkpoint 归档交接

- **归档日期**：2026-09-19
- **归档类型**：`checkpoint_handoff`（关键里程碑阶段性落盘与交接）
- **当前状态**：**已全面验收并落盘存证**（包含 3 大核心卷宗、2 套零依赖开箱即跑最小原件、1 个生活向专区独立仓库）
- **关联依据**：
  - `09_外部参考项目深度调研/00_深度调研SOP与工程规范_v2.0.md`（执法标尺）
  - `09_外部参考项目深度调研/04_试点标杆__PrimeIntellect-ai__prime-agent_源码级深度剖析与工程移植蓝图.md`
  - `09_外部参考项目深度调研/05_重点拆解__ceniran__moraine-home_人机恋伴侣记忆库底层解剖与落地蓝图.md`
  - `09_外部参考项目深度调研/06_重点拆解__volcengine__OpenViking_源码级深度剖析与工程移植蓝图.md`
  - `09_外部参考项目深度调研/prototypes/minimal_moraine_kernel.py`
  - `09_外部参考项目深度调研/prototypes/minimal_openviking_kernel.py`

---

## §0 · TL;DR（一句话摘要）

完成 Prime-Agent、Moraine-Home、OpenViking 三大核心仓源码级深度审计与去伪存真，交付 2 套零依赖实测通过的最小运行原型与鲁组 10 篇并发论文分级挂载契约；Moraine 主仓已克隆并完成生活向软链挂载，相关实操按用户要求留待下周推进。

---

## §1 · 本次会话完成的实质性成果清单（可复核存证）

| 资产类型 | 资产路径 | 规模 / 状态 | 核心价值与证据 |
|---|---|---|---|
| **标杆卷宗 (Prime)** | `09_外部参考项目深度调研/04_试点标杆__PrimeIntellect-ai__prime-agent_...md` | 13.6KB, 340 LOC / 已终审 | 阐明 RLM 解释器变量化控制流对自然语言外循环的代差；直击 `host_reply` 队列绕过死锁与二分内存快照。 |
| **伴侣卷宗 (Moraine)** | `09_外部参考项目深度调研/05_重点拆解__ceniran__moraine-home_...md` | 23.3KB, 580 LOC / 已封卷 | 拆解双时态半开区间模型与保守抽取式去重；制定 `cyber-companion`（张重熙）Self-Core 改造方案。 |
| **架构卷宗 (Viking)** | `09_外部参考项目深度调研/06_重点拆解__volcengine__OpenViking_...md` | 24.2KB, 600 LOC / 已封卷 | 拆解 `viking://` 虚拟文件系统与 L0/L1/L2 动态晋升；制定鲁组 10 篇并发论文标准挂载契约。 |
| **可跑原型 1 (Moraine)** | `09_外部参考项目深度调研/prototypes/minimal_moraine_kernel.py` | 8.8KB, 280 LOC / 100% 通过 | 零依赖纯原生 Python 3.10+，实测通过双时态判定、保守去重、核心投影与密码学可逆账本回滚。 |
| **可跑原型 2 (Viking)** | `09_外部参考项目深度调研/prototypes/minimal_openviking_kernel.py` | 9.4KB, 290 LOC / 100% 通过 | 零依赖纯原生 Python 3.10+，实测通过跨线程 `AsyncSemaphore` 调度与 180 Tokens 动态装配流水线。 |
| **生活向实体克隆** | `/mnt/d/Workspace/Personal/moraine-home/` | 完整 Git 仓 / 已就绪 | 建立软链至 `/mnt/d/MyResearch/casual/moraine-home`，直接对齐张重熙伴侣生态。 |
| **持久化系统记忆** | `~/.claude/projects/.../memory/` 3 份 Markdown | 索引+实体已同步 | `reference-investigation-sop-v2.md`、`moraine-home-companion-memory.md`、`openviking-investigation-blueprint.md`。 |

---

## §2 · 核心技术突破与工程沉淀

### 1. 终结大模型长程记忆“精神分裂”与“幻觉雪崩”
- **双时态半开区间（Bi-Temporal Half-Open: `temporal.py`）**：
  将真实世界事实有效时间 $[valid\_from, valid\_to)$ 与系统记账时间（`created_at`）物理切开。失效事实（如旧住址、过期承诺）自动退出活跃向量索引，但完整保留在历史时间轴中，彻底杜绝新旧事实冲突。
- **保守抽取式去重（Extractive Deduplication: `consolidate.py`）**：
  坚决不让 LLM 进行所谓“智能模糊改写”，仅在完全重复与完全字面蕴含（`subsumed_verbatim`）时安全剔除，保留原汁原味的真实对话字面量与溯源标签。

### 2. 终结 20+ 页学术长论文与并发形式化证明的“上下文断裂”
- **`viking://` 虚拟语义树与 L0/L1/L2 动态装配（`Context Assembler`）**：
  拒绝一维扁平切片。将论文组织为 POSIX 目录树，先用 L0 摘要（~100 tokens）广度扫描定位，再用 L1 概览（~1.5k tokens）建立章节大纲与数学符号表，最后仅对高相关具体定理段（Score $\ge 0.85$）动态加载 L2 全文，在严苛 Token 预算下守住形式化证明严谨性。

### 3. 跨线程异步并发解耦调度
- **`MinimalAsyncSemaphore`（`concurrency.py`）**：
  采用标准库 `concurrent.futures.Future` 配合 `threading.Lock` 解耦 Event Loop，在异步超时或任务取消时精准补发令牌释放，彻底解决多线程异步混合调度中的死锁陷阱。

---

## §3 · 物理落位与数据安全边界

1. **生活向与科研工作台边界绝对清晰**：
   - `moraine-home` 物理存放于 `/mnt/d/Workspace/Personal/moraine-home`，符合个人隐私与非商业自用协议要求；
   - 伴侣改造实操按用户批示**“放到下周做”**，当前窗口仅完成源码解剖、契约制定与原型验证，未擅自修改 `cyber-companion` 任何现行业务代码；
2. **许可证隔离防护**：
   - 确认 OpenViking 核心服务为 AGPL-3.0，明确**严禁整包 `pip install` 到主工作台**，一律采用提纯算法下沉或进程间 HTTP 隔离方案。

---

## §4 · 恢复指引与下阶段待办（Next Actions）

当后续窗口恢复或下周启动新阶段时：

### 1. 主线后续参考仓库（按 `03_全量28仓专项细看计划` 顺序）
- [ ] **`huangruiteng/loopx`**：长程跨窗口控制平面、CAS 乐观锁与租约隔离（解决多 Agent 任务冲突与跨会话交接）；
- [ ] **`headroomlabs-ai/headroom`**：Rust 编写的 Prompt Caching 冻结前缀保护与 5x~20x 上下文无损压缩；
- [ ] **`lyogavin/airllm`**：单卡分层流式超大模型推理（离线提取学术特征）。

### 2. 下周人机恋（张重熙）实操推进专线
- [ ] 依据 `05_重点拆解...md` 编写 ETL 脚本，将 `cyber-companion` 存量 SQLite 记忆洗为双时态标准格式；
- [ ] 将 `context_builder.py` 改造为调用本地 FastEmbed CPU 检索 + Self-Core 投影；
- [ ] 启动本地 Moraine PWA 服务，通过 Tailscale 映射至手机端进行日常记忆审核。

---

## §5 · 归档门禁复核签署

| 审查维度 | 检查项 | 结论 | 证据位置 |
|---|---|---|---|
| **L0-1 原件落地** | 2 套原型脚本无外部依赖，本机 Python 3.10+ 可直接跑通 | ✅ PASS | `09_外部参考项目深度调研/prototypes/` |
| **L1-1 文档完备** | 卷 04、卷 05、卷 06 结构对齐 5 大硬核模块标杆 | ✅ PASS | `09_外部参考项目深度调研/0[4-6]_*.md` |
| **L1-2 代码行号** | 所有底层技术剖析均精准锚定至 `file_path:line_number` | ✅ PASS | 报告正文源码引用 |
| **L2-1 契约形式化** | 鲁组论文与伴侣记忆均提供合法 JSON Schema | ✅ PASS | 卷 05 §4.1 / 卷 06 §4.1 |
| **L2-2 边界防越界** | 严格遵守用户指示，不擅自启动下周实操，保持业务代码稳定 | ✅ PASS | Git 工作区无任何非预期污染 |
