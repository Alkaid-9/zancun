# 09_外部参考项目深度调研 · 知识资产索引

本目录是依据 `00_深度调研SOP与工程规范.md` 对 2026-09-18 登记的 28 条前沿 GitHub 外部开源项目进行全量深度审计、源码除魅（Anti-Hype）、存证收据保存与业务槽位对齐的完整资产库。

---

## 目录结构导航

```
09_外部参考项目深度调研/
├── README.md                                # 本索引文件
├── 00_深度调研SOP与工程规范.md               # 调研工程规范 v1.0 历史底座
├── 00_深度调研SOP与工程规范_v2.0.md          # 【执法标尺】Agent执行细则版 (8步法+5项搜毒+6维锚点+12项门禁)
├── 01_2026-09-18__新增28条GitHub链接登记.md  # 原始 28 仓链接登记存证 (桌面归档)
├── 02_2026-09-18__two-desks-reference-integration__handoff.md # TASK-20260918-005 跨窗口交接存证
├── 03_全量28仓专项细看计划与定制审查标准.md  # 28 仓 7 大原型分类审讯书与一仓一标准规划
├── 04_试点标杆__PrimeIntellect-ai__prime-agent_源码级深度剖析与工程移植蓝图.md # 【终审标杆范本】5大硬核模块落地样本
├── 05_重点拆解__ceniran__moraine-home_人机恋伴侣记忆库底层解剖与落地蓝图.md # 【人机恋专项解剖】双时态记忆治理与张重熙对接蓝图
├── 06_重点拆解__volcengine__OpenViking_源码级深度剖析与工程移植蓝图.md # 【上下文数据库解剖】viking://与鲁组10篇并发论文分级加载
├── 07_2026-09-19__外部参考调研与多核落地__checkpoint_handoff.md # 【里程碑交接】阶段性全量决算与下周实操规划
├── 08_重点拆解__huangruiteng__loopx_源码级深度剖析与工程移植蓝图.md # 【长程控制面解剖】CAS乐观锁、租约栅栏与4-State契约
├── 09_2026-09-19__窗口全景工作决算与交接总结__window_summary_and_handoff.md # 【全窗口总结】工作日志、已完成/未完成、跨会话完整决算
├── MASTER_EVALUATION_MATRIX.md              # 28 仓全景总决算大矩阵与处置建议
│
├── docs/                                    # 系统架构、操作手册与维护工程规约
│   ├── MULTI_KERNEL_SYSTEM_ARCHITECTURE.md  # 四核驱动统一系统架构方案与工程分工说明书
│   ├── USER_MANUAL.md                       # 原型与多核系统操作使用手册
│   ├── MAINTENANCE_MANUAL.md                # 维护手册、红蓝对抗防御与排错指南
│   └── NEXT_PHASE_EXECUTION_PLAN.md         # 下阶段演进与下周实操路线图
│
├── prototypes/                              # 开箱即跑最小可运行原件验证库 (Zero-dependency)
│   ├── minimal_moraine_kernel.py            # Moraine 4大核心算法提纯验证脚本 (已实测100%通过)
│   ├── minimal_openviking_kernel.py         # OpenViking 虚拟文件系统、语义提取与分级装配原件 (已实测100%通过)
│   └── minimal_loopx_kernel.py              # LoopX CAS租约引擎、写范围匹配、4态契约与策略门禁原件 (已实测100%通过)
│
├── receipts/                                # 原始审计证据存证目录 (只读凭证)
│   ├── BATCH_METADATA_RECEIPT.json          # 28 仓 GitHub API 探测原始元数据汇总
│   ├── readmes/                             # 28 仓完整 README 原文落盘 (28个文件)
│   ├── trees/                               # 28 仓顶层 Git 目录结构 JSON 存证 (28个文件)
│   └── sources/                             # 重点项目核心源码文件抓取存证 (Python/Rust/TS/MJS/MD)
│
├── reports/                                 # 6 大专业分组宏观摸排调研报告
│   ├── batch1_science_agents.md             # 科学智能组 (4仓: DeepMind, K-Dense, Prime, TradingAgents)
│   ├── batch2_openviking_ecosystem.md       # OpenViking 生态 (3仓: 主仓, UI后台, Claude插件)
│   ├── batch3_name_pairs.md                 # 疑似同名项目对照 (4仓: paperclip对, headroom对)
│   ├── batch4_engineering_tools.md          # 工程与推理底座 (9仓: AirLLM, LoopX, Archify, i-have-adhd等)
│   ├── batch5_microsoft_beginners.md        # 微软教程体系 (6仓: GenAI, Agents, MCP, EdgeAI, AI等)
│   └── batch6_ai_engineering.md             # 从零精通体系 (2仓: 原版 rohitg00 vs 中文版 fancyboi999)
│
└── deep_dives/                              # 【L3 源码级硬核解剖专区】逐行源码审计与代码提纯
    ├── README.md                            # 深度审计专区索引
    ├── 01_prime_agent__rlm_kernel_and_continual_harness__source_audit.md # RLM REPL 与持续支架
    ├── 02_openviking_plugins__claude_code_native_hooks__source_audit.md # Claude Code 原生 Hooks
    ├── 03_headroom__context_compression_and_cache_control__source_audit.md # Rust 缓存边界守卫
    ├── 04_loopx__long_horizon_control_plane_and_gates__source_audit.md # 长程控制面与租约门禁
    └── 05_i_have_adhd__anti_rambling_prompt_contract__source_audit.md # 认知载荷与防废话契约
```

---

## 核心决算成果摘要

- **全量审查完成度**：**28 / 28 (100%)**
- **五选一处置分布**：
  - **转化设计 (ADAPT-DESIGN, 6 仓)**：`Prime Agent`（RLM变量化Agent）、`OpenViking`（L0/L1/L2分层加载与viking://虚拟文件系统）、`OpenViking-Plugins`（Claude Code原生Hooks）、`LoopX`（长程跨窗口控制平面）、`Headroom`（本地5x~20x上下文压缩）、`AirLLM`（单卡流式推理超大模型）。
  - **直接采纳 (ADOPT-SKILL, 2 仓)**：`ayghri/i-have-adhd`（10条防废话高能动性输出铁律）、`fancyboi999/ai-engineering-from-scratch-zh`（内置6大Claude Code专属交互式教学Skill）。
  - **借鉴原则 (BORROW-PRINCIPLE, 15 仓)**：`TradingAgents`（风控门禁拦截）、`science-skills`（arXiv/OpenAlex检索Skill）、`archify`（架构Before/Delta/After动态Diff对比）、`mcp-for-beginners`（2026-07-28规范跨语言实现）等。
  - **暂缓/排除 (SHELVE, 5 仓)**：彻底排除已废弃老仓（`thoughtbot/paperclip`, `microsoft/AirSim`）与同名无关前端库（`headroom.js`）。

详情请参阅 `MASTER_EVALUATION_MATRIX.md`。
