# Batch 3 · 疑似同名不同项目对照与排查深度调研报告

- **任务编号**：`TASK-20260919-REF-B3`
- **审查范围**：
  - 对照组 1：`paperclipai/paperclip` vs `thoughtbot/paperclip`
  - 对照组 2：`headroomlabs-ai/headroom` vs `WickyNilliams/headroom.js`
- **核心任务**：彻底查清两组“同名项目”的技术真相、血缘关系，排除历史干扰项，确立有效工具的接入边界。
- **证据存证**：原始元数据与完整 README/Tree 已落盘至 `receipts/`。

---

## 1. 第一对照组：Paperclip 对比审查

### 1.1 thoughtbot/paperclip（排除项：已废弃的经典 Rails 插件）
```yaml
id: REF-20260919-008
repo: thoughtbot/paperclip
branch: master
license: NOASSERTION (Thoughtbot Custom)
stars: 9014
status: DEPRECATED (2018 年官方停止维护)
disposal_recommendation: SHELVE (历史无关项，彻底排除)
```
- **真相与除魅**：这是 Ruby on Rails 社区十年前最著名的文件上传附件管理 Gem 包。官方在 2018 年已正式宣布废弃（`closing-the-trombone`），全面让位于 Rails 原生的 `ActiveStorage`。
- **结论**：与现代 AI、LLM、Agent **毫无任何关系**，纯属同名巧合。必须从任何当前记账线中彻底剔除，不再投入任何精力。

---

### 1.2 paperclipai/paperclip（有效项：多 Agent 企业协作编排平台）
```yaml
id: REF-20260919-009
repo: paperclipai/paperclip
branch: master
license: MIT
stars: 81038
depth_achieved: L2-MECHANISM
primary_slot: workbench
safety_tier: SAFE-READONLY (本地 Web 管理器)
disposal_recommendation: BORROW-PRINCIPLE
```
- **定位**：面向 AI Agent 团队的组织化调度管理后台（“If OpenClaw is an employee, Paperclip is the company”）。
- **架构机制**：
  - 基于 Node.js + React 构建的多 Agent 管理控制台；
  - 核心抽象层：目标设定（Goals） -> 角色招募（Agents/Roles） -> 预算与治理审批（Budgets/Governance） -> 执行监控；
  - 提供可视化的组织架构图、Agent 任务卡板和模型 Token 成本实时审计。
- **源码除魅与真实度**：
  - 本项目是真实度很高的多 Agent 组织管理 UI 封装，适合管理多模型（OpenAI, Anthropic, 自定义端点）；
  - 但其定位于“商业公司运行（Run a business）”，目标和任务层级较重（含 CEO/CTO 模拟），对个人学术研究来说略显庞大。
- **业务槽位与可偷师资产**：
  - **槽位**：**工作台 (Workbench) 预算与 Agent 治理**。
  - **可复用资产**：其对多 Agent 的 **Token 消耗预算硬限制（Budget Control）** 和 **任务状态看板（Task Status Board）** 的数据结构设计非常干净，可以直接作为两台工作台的成本监控参考。
- **处置建议**：**借鉴原则 (BORROW-PRINCIPLE)**。

---

## 2. 第二对照组：Headroom 对比审查

### 2.1 WickyNilliams/headroom.js（排除项：纯前端网页滚动特效库）
```yaml
id: REF-20260919-010
repo: WickyNilliams/headroom.js
branch: master
license: MIT
stars: 10841
status: UNRELATED (前端 DOM 动画小工具)
disposal_recommendation: SHELVE (前端旧库，彻底排除)
```
- **真相与除魅**：这是一个拥有 10 年历史的纯前端原生 JavaScript 库，唯一功能是在用户向下滚动页面时隐藏导航栏（Header），向上滚动时重新显示。
- **结论**：纯属同名，与 LLM 上下文和 Agent 研发**完全无关**，彻底淘汰。

---

### 2.2 headroomlabs-ai/headroom（重大价值项：本地 Agent 上下文无损压缩层）
```yaml
id: REF-20260919-011
repo: headroomlabs-ai/headroom
branch: main
license: Apache-2.0
stars: 73016
depth_achieved: L2/L3-MECHANISM
primary_slot: infra / research-desk / learning-desk (底层降本加速神级组件)
safety_tier: SAFE-READONLY (完全本地端运行)
disposal_recommendation: ADAPT-DESIGN / ISOLATED-TRIAL (强烈建议重点关注)
```

### 2.2.1 基础画像与核心定位
- **官方地址**：`https://github.com/headroomlabs-ai/headroom`
- **定位**：专门为 AI Coding / Research Agent 打造的**本地上下文实时压缩层（Context Compression Layer）**。
- **核心声明**：在工具输出、超大日志、文件内容、RAG 分块到达大模型之前，在本地将其无损/语义压缩 5x 至 20x，且**不向外发送任何提示词或文件内容**（基于本地小型模型 `kompress-v2-base` 驱动）。

### 2.2.2 核心架构与多种接入形态
1. **Python / TS 库模式**：在代码中直接调用 `compress(messages)`。
2. **本地代理模式 (Proxy)**：`headroom proxy --port 8787`，自动拦截并压缩所有经由代理发送给模型的 Tool outputs 与上下文。
3. **Agent 一键封装 (Agent Wrap)**：原生支持 `headroom wrap claude`、`codex`、`cursor`、`aider` 等几乎所有主流 CLI 工具。
4. **标准 MCP 服务**：对外提供 `headroom_compress`、`headroom_retrieve`、`headroom_stats` 三大 MCP 工具。

### 2.2.3 源码除魅与纸老虎检验
- **真实度**：这是当前 AI 工程界**最顶级的底层基础设施之一**。它不是粗暴地按字符截断，而是通过训练专有的小型局部压缩模型，保留错误堆栈中的 `FATAL`、关键行号、语法定义，剔除大量无意义的重复空格、冗余中间日志和模版文字。
- **安全性**：完全在本地机器运行，不上传任何隐私或研究数据，完美契合我们对科研数据本地性的严苛要求。

### 2.2.4 业务场景映射与价值
- **槽位匹配**：**底层工程基建 (Infra) & 两台文献/长上下文处理**。
- **直击痛点**：
  - 鲁组论文全文往往上万字，以前读一篇论文直接把上下文撑满或导致 429；
  - 运行自动化测试或代码静态分析时，上千行的终端输出会导致巨额 Token 消耗。
  - 接入 Headroom 可以让我们的单次调用成本直接下降 60%-80%，同时大幅减少上下文触顶导致的遗忘。
- **处置建议**：**转化设计 / 隔离试用 (ADAPT-DESIGN / ISOLATED-TRIAL)**。

---

## 3. Batch 3 同名对照排查总结表

| 项目名称 | 所属领域 | 真实技术栈 | 是否我们要找的目标 | 处置裁定 |
|---|---|---|---|---|
| **thoughtbot/paperclip** | Ruby on Rails 文件上传 | Ruby (已废弃) | ❌ 彻底无关 | **SHELVE** (排除) |
| **paperclipai/paperclip** | 多 Agent 团队组织编排 | Node.js + React | ✅ 组织管理参考 | **BORROW** (借鉴预算/看板) |
| **WickyNilliams/headroom.js** | 网页顶部导航栏特效 | 原生 JavaScript | ❌ 彻底无关 | **SHELVE** (排除) |
| **headroomlabs-ai/headroom** | 本地 Agent 上下文压缩 | Python/Rust/MCP | ⭐ **超高价值底层基建** | **ADAPT / TRIAL** (重点吸收) |
