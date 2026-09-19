# Batch 4 · 工程、推理底座与前沿效能工具组深度调研报告

- **任务编号**：`TASK-20260919-REF-B4`
- **审查范围**：9 个工程、推理底座与前沿效能工具仓
  1. `lyogavin/airllm`（单卡超大模型分层流式推理）
  2. `AlexsJones/llmfit`（本地硬件规格与模型承载力评估 CLI/TUI）
  3. `modular/modular`（Modular 平台、MAX 推理引擎与 Mojo 语言）
  4. `simstudioai/sim`（多智能体可视化构建与部署协作工作台）
  5. `microsoft/AirSim`（基于 UE/Unity 的自动驾驶仿真平台，历史老仓）
  6. `ayghri/i-have-adhd`（Claude Code 抑制废话与高能动性输出约束技能）
  7. `huangruiteng/loopx`（长程智能体跨窗口状态控制平面与循环工程）
  8. `tt-a1i/archify`（架构与工作流交互式动态渲染 Agent Skill）
  9. `omacom/omarchy`（DHH 定制化 Agentic Linux 操作系统发行版）
- **执行规范**：严格执行 `00_深度调研SOP与工程规范.md`（5 Caps 纪律、源码除魅、业务槽位精准靶向）
- **证据存证**：原始元数据见 `receipts/BATCH_METADATA_RECEIPT.json`，目录树与完整 README 已落盘至 `receipts/`。

---

## 1. lyogavin/airllm（单卡超大模型分层流式推理）

```yaml
id: REF-20260919-012
repo: lyogavin/airllm
branch: main
stars: 34550
license: Apache-2.0
depth_achieved: L2/L3-MECHANISM
primary_slot: infra
safety_tier: SAFE-READONLY (本地推理脚本)
disposal_recommendation: ADAPT-DESIGN / TRIAL-CANDIDATE
```

### 1.1 基础画像与核心机制
- **定位**：通过**分层加载与流式计算（Layer-wise Streaming Inference）**，使 70B 大模型能在单张 4GB 显存显卡上运行，乃至在 12GB 显存上运行 DeepSeek-V3 (671B)。
- **核心机制**：
  - 传统推理要求将所有权重一次性加载进显存；
  - AirLLM 仅在 GPU 显存中常驻当前计算层（Layer），通过磁盘/内存映射（mmap）与流水线预取（Prefetching），在计算第 $N$ 层时预取第 $N+1$ 层，计算完毕立即释放；
  - 牺牲吞吐时间换取极端显存利用率（适合学术验证、微调、单批次离线长程分析）。
- **业务场景映射**：
  - **槽位**：**底层工程基建 (Infra)**。
  - **对齐业务**：若未来需要在本地私有机器上对特定开源大模型（如 Qwen-72B、DeepSeek）进行离线批量文献分析或静态代码推理，而受限于单卡显存，AirLLM 是最低成本的兜底方案。
- **处置建议**：**转化设计 / 备选试用 (ADAPT-DESIGN / TRIAL-CANDIDATE)**。

---

## 2. AlexsJones/llmfit（本地硬件规格与模型适配评估器）

```yaml
id: REF-20260919-013
repo: AlexsJones/llmfit
branch: main
stars: 36816
license: MIT
depth_achieved: L2-MECHANISM
primary_slot: infra
safety_tier: SAFE-READONLY (无特权只读 CLI)
disposal_recommendation: BORROW-PRINCIPLE
```

### 2.1 基础画像与核心机制
- **定位**：用 Rust 编写的高性能硬件探查与本地模型承载力评估 CLI/TUI 工具。
- **核心机制**：
  - 自动扫描 CPU、物理内存、NVIDIA CUDA/AMD ROCm/Apple Silicon 显存带宽与架构；
  - 内置主流开源模型参数矩阵（上下文窗口、GGUF/AWQ/EXL2 量化位宽对显存的需求公式）；
  - 输出打分表，精准告知本机能以多少 tok/s 跑哪种量化级别的开源模型。
- **业务场景映射**：
  - **槽位**：**底层工程基建 (Infra)**。
  - **对齐业务**：在团队配置新研发机器或学生本地环境时，作为基线硬件测评工具，杜绝盲目下载几十 GB 模型后显存溢出（OOM）。
- **处置建议**：**借鉴原则 (BORROW-PRINCIPLE)**。

---

## 3. modular/modular（Modular 平台、MAX 与 Mojo）

```yaml
id: REF-20260919-014
repo: modular/modular
branch: main
stars: 29820
license: Apache-2.0 with LLVM Exceptions (部分模块为 Community License)
depth_achieved: L1-IDENTITY / L2-MECHANISM
primary_slot: infra
safety_tier: SAFE-READONLY
disposal_recommendation: SHELVE (当前阶段过重，保持观望)
```

### 3.1 基础画像与除魅
- **定位**：LLVM 之父 Chris Lattner 创立的高性能 AI 编译器与运行底座，包含 Mojo 编程语言和 MAX 加速引擎。
- **除魅结论**：属于极底层的异构硬件编译生态（AI 基础软件级别）。对于我们目前的“科研台/工作台/长程智能体编排”而言，层级过深，短时间内无法对我们的 Agent 工作流产生直接生产力增益。
- **处置建议**：**暂缓搁置 (SHELVE)**。列入长期技术雷达，但当前不投入精力集成。

---

## 4. simstudioai/sim（多智能体可视化协作工作台）

```yaml
id: REF-20260919-015
repo: simstudioai/sim
branch: main
stars: 29674
license: Apache-2.0
depth_achieved: L2-MECHANISM
primary_slot: workbench
safety_tier: SAFE-READONLY (Docker 本地部署)
disposal_recommendation: BORROW-PRINCIPLE
```

### 4.1 基础画像与核心机制
- **定位**：用于构建、部署和监控 AI Agent 的全栈可视化协作工作台。
- **核心架构**：
  - 左侧为多轮交互与 Agent 状态会话，右侧为可视化工作流画布（Visual Workflow Builder）；
  - 内置统一的表格（Tables - 结构化数据）、文件（Files - 团队资料）、知识库（Knowledge - 语义检索）；
  - 支持全量 Docker Compose 本地一键部署。
- **业务场景映射与可偷师资产**：
  - **槽位**：**工作台 (Workbench) 交互架构与数据流参考**。
  - **可复用设计**：其将“结构化表格（如任务账本）”与“非结构化知识库（如论文库）”在同一 UI 内无缝喂给 Agent 的数据管理模型，值得我们的工作台前端深度参考。
- **处置建议**：**借鉴原则 (BORROW-PRINCIPLE)**。

---

## 5. microsoft/AirSim（UE/Unity 自动驾驶与无人机仿真平台）

```yaml
id: REF-20260919-016
repo: microsoft/AirSim
branch: main
stars: 18498
license: MIT (历史)
status: ARCHIVED / DEPRECATED (微软已于 2022 年底停止维护原仓)
depth_achieved: L1-IDENTITY
primary_slot: unrelated
safety_tier: SAFE-READONLY
disposal_recommendation: SHELVE (彻底排除)
```

### 5.1 基础画像与除魅
- **定位**：微软在 2017 年发布的基于虚幻引擎的无人机/自动驾驶物理仿真器。
- **事实查验**：微软官方已正式关闭并归档该项目，全面转向封闭商业云服务 Project AirSim。且其研究领域为**端到端机器人物理控制与计算机视觉仿真**。
- **结论**：与大语言模型、软件工程智能体、科研分析工作流**完全无关**。
- **处置建议**：**暂缓搁置 / 彻底排除 (SHELVE)**。

---

## 6. ayghri/i-have-adhd（Claude Code 抑制废话与高能动性输出技能）

```yaml
id: REF-20260919-017
repo: ayghri/i-have-adhd
branch: main
stars: 48420
license: MIT
depth_achieved: L2/L3-MECHANISM
primary_slot: infra / workbench (交互纪律规约)
safety_tier: SAFE-READONLY (纯 Prompt/Skill 契约)
disposal_recommendation: BORROW-PRINCIPLE / ADOPT-SKILL
```

### 6.1 基础画像与核心机制
- **定位**：面向 Claude Code 等代码智能体的系统级 Prompt/Skill，彻底消灭 AI 回答中的废话套话。
- **十条铁律（The 10 Rules）**：
  1. 行动先行（Lead with the next action）；
  2. 多步任务严格带序号（Number multi-step tasks）；
  3. 结尾必须是一个具体且明确的下一步（End with one concrete next step）；
  4. 严禁展开无意义的发散枝节（Suppress tangents）；
  5. 每轮显式重申当前状态（Restate state every turn）；
  6. 给出精确的时间估计（Specific time estimates in minutes）；
  7. 进展显性化（Make wins visible）；
  8. 实事求是暴露错误（Matter-of-fact errors）；
  9. 清单上限封顶 5 项（Cap lists to 5 items）；
  10. **零开场白，零总结复述，零客套结尾（No preamble. No recap. No closers）**。
- **业务场景映射与价值**：
  - **槽位**：**工作台交互规范与 Agent 提示词协议**。
  - **对齐痛点**：多 Agent 长程执行时，往往被模型客套的“很高兴为您解答”、“希望能帮到您”消耗大量 Token 并造成上下文污染。其 10 条铁律与我们的工程 SOP 天然契合！
- **处置建议**：**采纳为常用规范 (ADOPT-SKILL / BORROW-PRINCIPLE)**。

---

## 7. huangruiteng/loopx（长程智能体跨窗口状态控制平面）

```yaml
id: REF-20260919-018
repo: huangruiteng/loopx
branch: main
stars: 5896
license: Apache-2.0
depth_achieved: L2/L3-MECHANISM & ARCHITECTURE
primary_slot: workbench / infra (底座级核心参考)
safety_tier: SAFE-READONLY (本地优先控制面)
disposal_recommendation: ADAPT-DESIGN (重大架构参考)
```

### 7.1 基础画像与核心机制
- **定位**：面向长程智能体（Long-horizon Agents）的**开放、跨厂商、有状态控制平面（Stateful Control Plane）**。
- **核心哲学**：
  - Agent 单次对话可以解决单点问题，但长程复杂工程任务无法仅靠单窗口完成；
  - **Harness（如 Claude Code/Codex）负责执行有边界的动作，LoopX 负责维持长周期跨窗口状态**；
  - 核心状态包括：目标树（Objectives）、门禁验收（Gates）、任务清单（Todos）、存证回执（Evidence）、配额开销（Quota）、跨轮交接（Handoffs）。
- **架构亮点**：
  - **Local-first**：状态全部本地持久化，断点随时续接；
  - **Turn Authority 与 Message 隔离**：明确区分人类管理者的拍板授权与智能体的执行边界；
  - 提供 Personal Workspace 仪表盘（`loopx dashboard`）。
- **业务场景映射**：
  - **槽位**：**工作台 (Workbench) 与两台长程交接设计最高价值架构参考**！
  - **深度共鸣**：我们当前正在践行的 `TASK-20260918-005` 跨窗口 handoff、AC 验收门禁、收据存证（Receipts），在 LoopX 中得到了完整的系统级抽象！
- **处置建议**：**转化设计 (ADAPT-DESIGN)**。

---

## 8. tt-a1i/archify（架构与工作流交互式动态渲染 Skill）

```yaml
id: REF-20260919-019
repo: tt-a1i/archify
branch: main
stars: 67113
license: MIT
depth_achieved: L2-MECHANISM
primary_slot: workbench / research-desk
safety_tier: SAFE-READONLY (纯本地静态生成)
disposal_recommendation: BORROW-PRINCIPLE
```

### 8.1 基础画像与核心机制
- **定位**：面向 Cursor、Claude Code 的架构与工作流高保真图表渲染 Agent Skill。
- **核心机制**：
  - Agent 只需输出强类型的 JSON IR（中间表示）；
  - Archify 确定性地将其编译为自包含的交互式 HTML/SVG；
  - 独创 **Before / Delta / After 架构 Diff 对比**，清晰呈现系统架构在重构前后的节点增删与路由变化；
  - 原生支持交互式链路追踪（Upstream/Downstream reach trace）。
- **业务场景映射**：
  - **槽位**：**两台架构演变可视化与科研论文技术路线图呈现**。
  - **价值**：比传统的静态 Mermaid 图表具备更强大的交互性和语义对比能力。
- **处置建议**：**借鉴原则 (BORROW-PRINCIPLE)**。

---

## 9. omacom/omarchy（DHH 定制化 Agentic Linux 发行版）

```yaml
id: REF-20260919-020
repo: omacom/omarchy
branch: quattro
stars: 41978
license: MIT
depth_achieved: L1-IDENTITY / L2-MECHANISM
primary_slot: infra
safety_tier: SAFE-READONLY
disposal_recommendation: BORROW-PRINCIPLE (理念借鉴)
```

### 9.1 基础画像与除魅
- **定位**：Ruby on Rails 创始人 DHH 主导的基于 Arch Linux 的定制发行版，专为以 Agent/AI 为中心的工作流打造。
- **核心内容**：预装并高度调优 Neovim、Kitty、Wayland、统一剪贴板历史、全局 AI 热键与 TUI 工具链。
- **业务场景映射**：
  - **槽位**：**底层开发环境与终端美化参考**。
  - **结论**：我们运行在 WSL2 / Ubuntu 环境下，无需推翻重装操作系统；但其对于终端热键绑定、CLI 与 AI 剪贴板无缝联动的配置逻辑值得参考。
- **处置建议**：**借鉴原则 (BORROW-PRINCIPLE)**。

---

## 10. Batch 4 综合横向矩阵表

| 仓库 | 核心定位 | 技术栈 | 对应业务槽位 | 核心可复用价值 | 处置裁定 |
|---|---|---|---|---|---|
| **lyogavin/airllm** | 单卡显存流式加载超大模型 | Python / mmap | 底层基建 | 4GB~12GB 显存运行 70B/671B 模型的保底机制 | **ADAPT / TRIAL** |
| **AlexsJones/llmfit** | 硬件检测与模型适配评分器 | Rust / TUI | 底层基建 | 研发机器硬件基准测量与量化模型承载力评估 | **BORROW** |
| **modular/modular** | MAX 引擎与 Mojo 语言 | C++ / Mojo | 底层编译器 | 异构编译底层，当前过重 | **SHELVE** |
| **simstudioai/sim** | 多智能体可视化协作画布 | Next.js / Docker | 工作台 | 表格/文件/知识库统一喂入 Agent 的前端交互 | **BORROW** |
| **microsoft/AirSim** | 自动驾驶 UE/Unity 仿真 | C++ (已废弃) | 无关历史仓 | 微软已废弃的物理控制仿真器，与 AI 无关 | **SHELVE** |
| **ayghri/i-have-adhd** | 高能动性/防废话输出规范 | Skill / Prompt | 工作台交互规约 | 10 条高压紧凑输出规约，大幅降低 Token 浪费 | **ADOPT / BORROW** |
| **huangruiteng/loopx** | 长程智能体有状态控制面 | TS / Python | 工作台底座 | 跨窗口目标维持、门禁验收、交接证据链架构 | **ADAPT** (重点吸收) |
| **tt-a1i/archify** | 强类型架构图与 Diff 渲染 | Node.js / HTML | 工作台/科研台 | 架构 Before/Delta/After 对比与交互链路展示 | **BORROW** |
| **omacom/omarchy** | DHH 定制 Agentic Linux | Arch Linux / Shell | 开发环境 | 终端、TUI 与 AI 深度绑定的桌面环境配置范式 | **BORROW** |
