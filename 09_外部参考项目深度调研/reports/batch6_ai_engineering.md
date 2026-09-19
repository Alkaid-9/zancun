# Batch 6 · AI Engineering 从零精通原版与中文生态深度调研报告

- **任务编号**：`TASK-20260919-REF-B6`
- **审查范围**：
  - 上游原版：`rohitg00/ai-engineering-from-scratch`（5.5万 Star，MIT）
  - 中文衍生版：`fancyboi999/ai-engineering-from-scratch-zh`（1086 Star，MIT）
- **核心任务**：
  - 核实两者血缘与代码同步性；
  - 评估 20 阶段 523 课的内容硬核度；
  - 探索其内置的 Claude Code 交互式导师技能体系（`start-learning`、`learn-mcp`、`learn-agent-skills`）。
- **证据存证**：原始元数据见 `receipts/BATCH_METADATA_RECEIPT.json`，目录树与完整 README 已落盘至 `receipts/`。

---

## 1. 上游原版：rohitg00/ai-engineering-from-scratch

```yaml
id: REF-20260919-027
repo: rohitg00/ai-engineering-from-scratch
branch: main
stars: 55003
license: MIT
depth_achieved: L2/L3-MECHANISM
primary_slot: learning-desk
safety_tier: SAFE-READONLY (开源教科书与代码工坊)
disposal_recommendation: BORROW-PRINCIPLE (上游权威底座)
```

### 1.1 基础画像与核心定位
- **定位**：当前 GitHub 上最全面、最具系统性的全栈 AI 工程师自学实战体系（“Learn it. Build it. Ship it for others”）。
- **规模与体量**：**20 个阶段，523 节独立实验课，约 342 小时实战**，跨 Python、TypeScript、Rust、Julia 四种语言。
- **教学哲学**：拒绝只看不动的技术博客阅读，每一节课都要求交付一个可运行、可复用的软件资产（Prompt、Skill、Agent 循环、MCP Server）。

### 1.2 课程 20 阶段知识树拆解（核心亮点）
- **Phase 00~05（底层与工程基建）**：环境搭建、线性代数/微积分工程直觉、自动微分引擎手写、CUDA/异构算子手写；
- **Phase 06~10（模型体系）**：从零手写 Transformer、Attention 变体、分词器（Tokenizer）、预训练与 SFT/DPO 微调；
- **Phase 11~13（LLM 工程与工具协议）**：提示词工程、生产级 RAG 架构、**Model Context Protocol (MCP) 全生命周期实战、Agent Skills 编写规范**；
- **Phase 14~16（智能体与高阶编排）**：Agent Loop 核心循环手写、多智能体协同、评测与防漂移门禁；
- **Phase 17~20（生产部署与评估）**：推理加速、模型量化（vLLM/llama.cpp）、安全对齐、红蓝对抗。

---

## 2. 中文衍生版：fancyboi999/ai-engineering-from-scratch-zh

```yaml
id: REF-20260919-028
repo: fancyboi999/ai-engineering-from-scratch-zh
branch: main
stars: 1086
license: MIT
depth_achieved: L2/L3-MECHANISM & AGENT-SKILL
primary_slot: learning-desk (团队首选学习资料) / workbench (导师技能集成)
safety_tier: SAFE-READONLY (本地交互教学)
disposal_recommendation: ADAPT-DESIGN / ADOPT-SKILL (重点采纳)
```

### 2.1 基础画像与血缘关系
- **定位**：上游 `rohitg00/ai-engineering-from-scratch` 的官方授权简体中文全量本地化衍生项目。
- **血缘查验**：通过 CI 流水线（`node site/build.js --check`）强约束 523 课课数与上游严格对齐，代码示例与阶段拓扑完全同步。

### 2.2 本地化增量与工业级体验升级
1. **全站高质量地道中文**：523 节课、83 条术语表、测验题与 Mermaid 流程图全部人工中文化并保留核心英文术语。
2. **3Blue1Brown 风格动画讲解视频**：将复杂的数学推导与网络反向传播制作成无真人可视化短视频。
3. **Claude Code 原生 AI 导师交互生态（重大价值亮点）**：
   - 运行 `npx skills add fancyboi999/ai-engineering-from-scratch-zh`，可一键向当前 Claude Code / Codex 注入系统级教学 Skill：
     - `/start-learning`：交互式定位导师，评估开发者背景，生成个性化 `LEARNING.md` 学习进度契约；
     - `/learn`：单课动手教学，流式阅读指定课程，分步推导代码；
     - `/learn-mcp`：17 课 MCP 协议专属导师，逐课生成 `MCP-LEARNING.md` 存证；
     - `/learn-agent-skills`：9 课 Agent Skill 研发专项导师，生成 `AGENT-SKILLS-LEARNING.md`；
     - `/check-understanding <phase>`：8 道实战测评题，自动批改并反馈薄弱环节。

---

## 3. 业务场景映射与双仓分工建议

- **槽位匹配**：**学习台 (Learning Desk) 权威教材底座 & 智能体导师 Skill 库**。
- **直击痛点**：
  - 团队进组新人通常对大模型工程（从 Tokenizer 到 Agent 循环再到 MCP 工具）缺乏系统性直觉；
  - 该项目不仅是一本书，而且提供了**内嵌进 Claude Code 的实战私教**，通过生成本地进度清单（`LEARNING.md`），保证每一次学习都有代码存证和测试输出。
- **分工定位**：
  - **日常查阅与交互学习**：全面以 `fancyboi999/ai-engineering-from-scratch-zh` 为主界面（无语言摩擦，有网页端 `aieng-zh.cn` 和动画配套）；
  - **规范对齐与国际版本**：保留 `rohitg00/ai-engineering-from-scratch` 作为 Git Submodule 或底层对照权威。
- **处置建议**：**采纳导师技能 / 转化设计为学习台骨架 (ADAPT-DESIGN / ADOPT-SKILL)**。

---

## 4. Batch 6 综合对照表

| 仓库 | 角色 | 语言 | 核心亮点 | 推荐操作 |
|---|---|---|---|---|
| **rohitg00/ai-engineering-from-scratch** | 国际上游权威 | 英文 | 523 课 20 阶段工业级全栈 AI 工程师动手课程 | **BORROW** (权威对照) |
| **fancyboi999/ai-engineering-from-scratch-zh** | 中文深度本地化 | 简体中文 | 全中文 + 动画视频 + Claude Code 原生 6 大交互式导师技能 | **ADOPT / ADAPT** (直接引入学习台) |
