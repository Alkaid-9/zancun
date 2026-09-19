# Batch 1 · 科研与科学智能 Agent 核心组深度调研报告

- **任务编号**：`TASK-20260919-REF-B1`
- **审查范围**：`google-deepmind/science-skills`、`K-Dense-AI/scientific-agent-skills`、`PrimeIntellect-ai/prime-agent`、`TauricResearch/TradingAgents`
- **执行规范**：严格执行 `00_深度调研SOP与工程规范.md`（5 Caps 纪律、源码除魅、业务槽位精准靶向）
- **证据存证**：原始元数据见 `receipts/BATCH_METADATA_RECEIPT.json`，目录树与完整 README 已落盘至 `receipts/`。

---

## 1. google-deepmind/science-skills

```yaml
id: REF-20260919-001
repo: google-deepmind/science-skills
branch: main
commit: 111423Z (2026-09-19)
license: Apache-2.0
stars: 3095
depth_achieved: L2-MECHANISM
primary_slot: research-desk
safety_tier: SAFE-READONLY (部分Skill需第三方API_KEY)
disposal_recommendation: BORROW-PRINCIPLE
```

### 1.1 基础画像与环境基建
- **官方地址**：`https://github.com/google-deepmind/science-skills`
- **定位**：Google DeepMind 官方开源的 Agentic Scientific Workflows 技能库（支持 Google Antigravity、Claude Code、Gemini CLI 等标准 Agent）。
- **运行环境与门槛**：Python ≥ 3.10，依赖轻量包管理器 `uv`，无需重型 GPU 即可运行；每个 Skill 均配有独立的 `scripts/` 与说明。
- **协议合规**：代码为 Apache-2.0，文档为 CC-BY 4.0，引用第三方数据源（如 UniProt、ClinVar）受各自开源条款约束，无商业或传染风险。

### 1.2 核心架构与工作流机制
- **输入**：自然语言科学查询、文献查询条件（arXiv/BioRxiv/PubMed/OpenAlex 检索式）、基因与蛋白质序列标识符。
- **处理链路**：
  1. 采用标准的 Anthropic/Claude Code Agent 规范（每个目录含 `SKILL.md` + YAML frontmatter + `scripts/`）；
  2. 包含 40+ 独立科学技能模块，其中不仅涵盖生信，还包含通用科研基础设施：
     - `literature_search_arxiv` / `biorxiv` / `europepmc` / `openalex` / `pubmed_database`：结构化学术文献检索；
     - `workflow_skill_creator`：元技能，专门负责让 Agent 自动把长链科研操作封装成新 Skill。
- **产出**：结构化学术检索结果、API 调用回执、经验证的蛋白质/基因组分析报告。

### 1.3 源码除魅与纸老虎检验
- **自研算法 vs Prompt 包装**：本项目是纯正的 **Agent Tools / Skills 协议实现**。它不宣称自己是“全自主通用科学家”，而是扎扎实实将 30+ 专业科学数据库的 REST API 封装成了标准的 Agent 调用契约。
- **自主性真实度**：单步 Skill 机制明确，没有死循环风险；依赖 `uv` 进行运行时虚拟环境隔离。
- **示例真实度**：README 提供的 API 契约均经过官方测试，非静态 Mock。

### 1.4 数据流、安全与隐私审查
- **通信目标**：主要是公开学术数据库 API（arXiv、OpenAlex、PubMed、UniProt 等），除 `AlphaGenome` 和 `OpenAlex` 需要配置 API Key 外，大部分检索可直接匿名访问。
- **写域安全**：只读查询为主，本地只写临时缓存，不存在越权遍历或覆盖宿主工作区风险。

### 1.5 业务场景映射与可偷师资产
- **槽位匹配**：**科研台 (Research Desk) - 学术文献检索与验证工具链**。
- **对齐业务**：
  - 在鲁组并发分析与系统论文追踪中，`literature_search_arxiv` 和 `literature_search_openalex` 提供了极其优雅、紧凑的 Python 检索脚本。
  - `workflow_skill_creator` 的 `SKILL.md` 模板，是教 Agent “如何把多步繁琐命令打包为可复用技能”的标准规范。
- **可直接剪切复用的代码资产**：
  - 直接提取 `skills/literature_search_arxiv/` 与 `skills/literature_search_openalex/` 下的检索契约与 Python 脚本，作为本地 Claude Code 的现成自定义 Skill。

### 1.6 局限性与反例
- 生物信息学比重偏大（占 70% 左右），对计算机系统、形式化方法、并发漏洞等非生信领域的专门算法工具较少。

### 1.7 五选一处置建议
- **处置结论**：**借鉴原则 (BORROW-PRINCIPLE)**
- **行动**：提取其文献检索类（arXiv / OpenAlex）与 `workflow_skill_creator` 的 Skill 结构，沉淀入本地工作台，不克隆全包。

---

## 2. K-Dense-AI/scientific-agent-skills

```yaml
id: REF-20260919-002
repo: K-Dense-AI/scientific-agent-skills
branch: main
commit: 45581 stars (高活跃)
license: MIT
depth_achieved: L2-MECHANISM
primary_slot: research-desk / infra
safety_tier: SAFE-READONLY
disposal_recommendation: BORROW-PRINCIPLE
```

### 2.1 基础画像与环境基建
- **官方地址**：`https://github.com/K-Dense-AI/scientific-agent-skills`
- **定位**：社区构建的“AI 科学家技能库”，内含 166 个涵盖数学、物理、天文学、生物、文献学的专门技能。
- **协议与依赖**：MIT 许可证。依赖 Python 生态（Astropy, BioPython, Scanpy 等）。

### 2.2 核心架构与工作流机制
- **输入**：领域计算任务指令、文献搜索关键词。
- **处理链路**：扁平化包含 166 个 Skill 目录，每一个目录为一个独立任务域，均配有输入参数 schema 和对应的 Python CLI 执行脚本。
- **产出**：计算结果、文献元数据、格式转换文件。

### 2.3 源码除魅与纸老虎检验
- **除魅结论**：166 个技能中，约 40% 是直接调用现成开源 Python 库（如 `astropy`、`anndata`、`biopython`）的薄层包装器（Wrapper），另外 30% 是针对第三方 API 的请求器。
- **宣称水分**：README 宣称“Turn any AI agent into an AI Scientist”，实际是“工具箱大全”，真正的科研假设生成、验证与实验设计仍需由核心 Agent（如 Claude/GPT）自己驱动。

### 2.4 数据流与安全性
- 多数为本地脚本，部分依赖外部学术 API。无自建云端中转，隐私风险低。

### 2.5 业务场景映射与可偷师资产
- **槽位匹配**：**底层工程工具库 (Infra & Skills)**。
- **可复用资产**：
  - `bgpt-paper-search`：文献多源抓取逻辑；
  - `analytical-method-validation`：实验数据对照与验证评估的标准流程模版。

### 2.6 五选一处置建议
- **处置结论**：**借鉴原则 (BORROW-PRINCIPLE)**。需要用到特定数学/分析技能时再按需抽取单个 Skill。

---

## 3. PrimeIntellect-ai/prime-agent

```yaml
id: REF-20260919-003
repo: PrimeIntellect-ai/prime-agent
branch: main
commit: 21051 stars (arXiv: 2608.23552 / 2605.09998)
license: MIT
depth_achieved: L2/L3-MECHANISM & ARCHITECTURE
primary_slot: workbench / research-desk (底座架构级参考)
safety_tier: REQUIRES-API-KEY (支持自定义本地模型端点)
disposal_recommendation: ADAPT-DESIGN
```

### 3.1 基础画像与环境基建
- **官方地址**：`https://github.com/PrimeIntellect-ai/prime-agent`
- **定位**：开源长期自主研发与长程任务 Agent 控制台，基于 **RLM (Recursive Language Model)** 与 **Continual Harness** 双核心。
- **学术背书**：配有两篇权威预印本论文（arXiv:2608.23552 和 arXiv:2605.09998）。
- **运行环境**：Python 3.10+，后台常驻 Daemon 架构，支持客户端断开重连。

### 3.2 核心架构与工作流机制（高度启发性）
- **核心创新 1：RLM (Recursive Language Model)**
  - 传统 Agent 把上下文当历史日志拼字符串，而 RLM 把**上下文视为内存变量 (`prompt-as-a-variable`)**；
  - 在持久 Python REPL 中，递归子代理（Subagent）被直接视为普通函数调用：`rlm.spawn(prompt, subagent_type) -> result`，子代理直接返回结构化内存对象，不再靠聊天窗口转述！
- **核心创新 2：Continual Harness（可持续演进的支架）**
  - 系统由“不可变基础 System Prompt”与“可动态更新的外部补充状态（Harness）”构成；
  - 提供 `/refine` 命令：基于当轮对话的实际失败与反思，生成微小的、有证据支持的持久化记忆微调；
  - 具备严格的快照机制（Snapshot & Rollback），避免 Prompt 漂移损坏。

### 3.3 源码除魅与纸老虎检验
- **真实度**：这是**真正的系统级工程突破**，不是玩具 Demo。它解决了多 Agent 协作时“主窗口上下文被子代理废话刷爆”的根本顽疾（子代理运行在隔离 REPL 栈中，输出直接赋给变量）。
- **自主性**：后台 Daemon 保持长程任务心跳，即使终端关闭，后台任务继续推进并写入事件日志。

### 3.4 数据流与隐私
- 原生支持自定义 OpenAI-compatible API 端点（可无缝接入本地 vLLM/Ollama 或私有代理）。
- 支持完全本地存储会话状态与记忆快照。

### 3.5 业务场景映射与可偷师资产
- **槽位匹配**：**工作台 (Workbench) 与科研台 (Research Desk) 底座架构设计最高价值参考**！
- **对齐痛点**：
  - 我们此前在两台设计中反复讨论的“多 Agent 并发跑完后主控如何无污染聚合”、“记忆如何增量演进而不会污染基础规范”，Prime Agent 给出了最优雅的工业界解答！
- **可偷师资产**：
  1. `rlm.spawn` 的函数式调用与变量回传协议；
  2. `/refine` 演进机制与快照回滚设计。

### 3.6 五选一处置建议
- **处置结论**：**转化设计 (ADAPT-DESIGN)**
- **行动**：强烈建议将 Prime Agent 的 RLM 变量化子代理通信机制与 Continual Harness 回滚设计，融入我们科研台/工作台下一阶段的内核改造中！

---

## 4. TauricResearch/TradingAgents

```yaml
id: REF-20260919-004
repo: TauricResearch/TradingAgents
branch: main
commit: 107551 stars (v0.5.0, 2026-09)
license: Apache-2.0
depth_achieved: L2-MECHANISM
primary_slot: workbench
safety_tier: REQUIRES-API-KEY
disposal_recommendation: BORROW-PRINCIPLE
```

### 4.1 基础画像与环境基建
- **官方地址**：`https://github.com/TauricResearch/TradingAgents`
- **定位**：多智能体金融分析与交易框架（10万+ Star 顶流开源项目，技术报告 arXiv:2412.20138 / arXiv:2509.11420）。
- **技术栈**：Python 3.10+，基于 LangGraph 构建的多角色状态机，支持 Docker 部署。

### 4.2 核心架构与工作流机制
- **角色分工明确**：
  - Research Manager（调研调度） -> Sentiment Analyst（情绪面） -> Fundamental Analyst（基本面） -> Trader（交易执行提案） -> Risk/Portfolio Manager（风控门禁审查）。
- **工作流链路**：
  - 严格的点对点时间一致性（Point-in-time Integrity，杜绝用未来数据预测过去）；
  - 基于 LangGraph Checkpoint 的可中断/可恢复状态机机制。

### 4.3 源码除魅与纸老虎检验
- **除魅结论**：虽然业务是金融量化交易，但其**多 Agent 审批流与风控门禁（Risk Gate）**是货真价实的工程代码。
- **风控门禁机制**：Trader 角色提出任何买卖决策，必须通过独立的 Risk Manager 审查指标才能放行，这与我们主控中的 `AC 验收门禁` 机制完全同构。

### 4.4 业务场景映射与可偷师资产
- **槽位匹配**：**工作台 (Workbench) - 多 Agent 异构协作与风控门禁设计**。
- **可直接复用资产**：
  - 学习其 `Risk Manager` 否决机制：当执行 Agent（如编写代码/生成分析）提交产物时，由独立的审查 Agent 执行 Checklist，若不满足条件强制回退并削减重试预算（LLM retry budget）。

### 4.5 五选一处置建议
- **处置结论**：**借鉴原则 (BORROW-PRINCIPLE)**
- **行动**：提取其多角色异构校验与 LangGraph 状态机 Checkpoint 恢复机制，不引入金融业务逻辑。

---

## 5. Batch 1 综合横向矩阵与结论

| 仓库 | 定位核心 | 代码硬核度 | 对应槽位 | 关键可偷师资产 | 处置裁定 |
|---|---|---|---|---|---|
| **google-deepmind/science-skills** | GDM 官方科研技能包 (40+ Skills) | 工业级协议规范 | 科研台 (文献工具) | arXiv/OpenAlex 检索 Skill 结构与元 Skill 模板 | **BORROW** (借鉴) |
| **K-Dense-AI/scientific-agent-skills** | 166 领域科学工具包装库 | 工具包装/薄层调用 | 底层工程库 | 实验验证流程模板与多源抓取脚本 | **BORROW** (借鉴) |
| **PrimeIntellect-ai/prime-agent** | RLM 递归 Agent + 持续微调 Harness | 极高 (学术+系统突破) | 工作台/两台底座 | 上下文变量化 (`prompt-as-variable`) + 记忆无损回滚 | **ADAPT** (转化设计) |
| **TauricResearch/TradingAgents** | 多 Agent 协作与风控门禁状态机 | 高度成熟的状态机 | 工作台 (门禁控制) | 独立审查 Agent 强制拦截与断点恢复机制 | **BORROW** (借鉴) |
