# 外部参考项目深度调研 SOP 与工程规范 (v2.0 · 机器与 Agent 执行细则版)

- **制定日期**：2026-09-19
- **版本编号**：`v2.0-MACHINE-EXECUTABLE`
- **归档路径**：`09_外部参考项目深度调研/00_深度调研SOP与工程规范_v2.0.md`
- **核心定位**：专为 Agent、Subagent 及工程审核者设计的**高精度、机械化、不可抵赖的深度勘验操作手册**。杜绝泛化总结，以源码证据、反虚标排查、客观打分锚点和鲁组业务强契约为唯一执法标准。

---

## 模块一：Agent 8 步法定执行流水线（Phase-by-Phase Protocol）

任何执行项目调研的 Agent 必须按以下 8 步顺序单向推进，缺步即判定违规：

### Step 1：实体与代码落地（Grounding）
- 必须通过 GitHub API 或本地 Clone 获取真实代码树；
- 统计项目各语言代码行数（LOC），记录固定 Commit Hash（7位+）、默认分支、开源协议声明文件路径；
- **铁律**：严禁仅凭 README 文字脑补源码，必须以磁盘上真实存在的代码为准。

### Step 2：依赖栈与入侵性审计（Dependencies & Runtime Boundary）
- 解析 `package.json` / `pyproject.toml` / `Cargo.toml` / `go.mod`；
- 统计第三方库总数，区分：
  - (a) 零依赖纯原生实现；
  - (b) 轻量工程依赖（如 `serde`, `zod`, `pydantic`）；
  - (c) 重型框架绑架（如强制依赖 LangChain, LlamaIndex, AutoGPT, Azure 闭源 SDK 等）。

### Step 3：调用链与时序追踪（Call Graph Tracing）
- 准确定位系统核心入口（CLI Main / Server Handler / Agent Loop）；
- **强制要求**：端到端追踪至少一条核心业务执行流：
  $$\text{User Input} \longrightarrow \text{Parser} \longrightarrow \text{Reasoning/Agent Loop} \longrightarrow \text{Tool Call} \longrightarrow \text{State Persistence}$$
  流转中的每一个关键节点必须精确给出 `file_path:line_number` 源码行号锚点。

### Step 4：“纸老虎”反虚标专项搜毒（Anti-Hype Interrogation）
- 执行模块二所列的 5 大排查模式，在报告中显式逐项给出验真结论与事实证据。

### Step 5：六维量化客观打分（Rubric-based Anchoring）
- 严格对照模块三的评分量规，给出 1~10 分的分值；
- **铁律**：每一个打分必须附带至少一句话的源码事实依据，禁止无依据给分。

### Step 6：鲁组科研与三台工程强契约挂载（Mounting & Asset Extraction）
- 明确指出该项目挂载到当前工作区蓝图的具体物理路径（模块四）；
- 必须提取至少 1~2 段真实可用的核心代码或提示词规约原件，并附带可运行的最小复用示例（Minimal Reproducible Snippet）。

### Step 7：反模式与暗坑预警（Failure Modes & Anti-Patterns）
- 必须列出至少 2~3 个具体失败场景，格式统一为：
  `【极端输入/边界触发条件】 -> 【底层代码缺陷】 -> 【引发崩溃/死循环/OOM/429/缓存穿透】`。

### Step 8：五选一处置裁决与 12 项 Done-When 门禁签字
- 给出最终裁决（BORROW / ADAPT / TRIAL / ADOPT / SHELVE）；
- 逐项检查模块五的 12 项验收门禁，全部打勾方可结项。

---

## 模块二：“纸老虎”反虚标 5 大排查模式（Anti-Hype Checklist）

Agent 必须在源码中执行以下排查，并在报告中显式汇报：

1. **静态假数据陷阱（Mock Data Trap）**：
   - 检查演示结果是否来自 `test/fixtures/` 或代码中硬编码的静态 JSON 字符串；真实动态请求时模型输出是否缺乏解析保护。
2. **死循环与无预算自嗨陷阱（Unbounded Loop Trap）**：
   - 全局搜索 `while True:` 或 `while(!done)`，核查是否存在最大轮次上限（Max Turns）、超时控制（Timeout）、Token 预算熔断（Token Budget Cap）及退避重试（Backoff）。
3. **薄层套壳包装陷阱（Thin Wrapper Trap）**：
   - 检查所谓“自主决策”是否全靠向 LLM 灌入巨幅 Prompt 自由发挥，核心状态机与控制流代码在全部代码量中的占比是否低于 10%。
4. **正则脆弱解析陷阱（Fragile Regex Parsing Trap）**：
   - 检查是否依赖简陋的正则表达式提取 LLM 输出中的 JSON 代码块；是否存在 AST 级别语法树容错解析机制。
5. **数据隐私与外泄排查（Silent Telemetry & Exfiltration）**：
   - 扫描网络请求模块，排查是否内置隐蔽的数据埋点（如 PostHog, Segment, Mixpanel, Sentry），确认私有科研数据是否存在未经声明的外泄风险。

---

## 模块三：六维量化客观打分标准（Scoring Rubric）

| 维度 | 1 ~ 3 分 (初级/脆弱) | 4 ~ 6 分 (中等/可用) | 7 ~ 8 分 (工业级/优秀) | 9 ~ 10 分 (突破级/顶尖) |
|---|---|---|---|---|
| **真实自主度 (Autonomy)** | 纯单轮 Prompt 包装，无重试无状态 | 简单的 `while` 循环，固定轮数，无分支回退 | 带 Checkpoint 状态机，具备动态分支规划与异常自愈 | 变量化内存隔离（RLM）、子代理函数化调用与秒级快照回滚 |
| **工程成熟度 (Maturity)** | 无测试、无类型标注、单文件混乱大脚本 | 有基础单元测试，有依赖声明，但缺少边缘覆盖 | 强类型（TS/Rust/Pyright），完整 CI 流程，解耦分层清晰 | 零正则 AST 解析、生产级异常隔离、有正式学术技术报告背书 |
| **上下文/Token 效率 (Efficiency)** | 轮轮拼接全量历史，无压缩无缓存，极易 429 | 简单滑动窗口截断（按固定轮数），易发生灾难遗忘 | 语义检索按需召回 + L0/L1 摘要按需晋升加载 | 严格保护 Prompt Caching 冻结前缀不变 + 局部小模型 5x~20x 无损压缩 |
| **可观测与控制力 (Observability)** | 黑盒输出，无日志，不可中断，费用失控 | 标准输出文本打印，有简单日志，但不可回放 | 结构化 JSONL 事件流，Token 实时看板，支持单步调试 | 独立的控制平面（Control Plane），消息可见性与执行权限物理隔离，CAS 乐观锁与租约隔离 |
| **安全与数据主权 (Security)** | 强制云端外泄，代码私有上传，写操作无沙箱限制 | 可配置本地 API，但写操作缺少边界防护 | 完全本地离线运行，严密的文件系统读写沙箱 | 形式化安全契约，零外网通信，输入防注入与输出防污染绝对闭环 |
| **鲁组科研贴合度 (Relevance)** | 与系统/并发/Petri网/两台毫无关联（如无人机仿真） | 通用技术概念，可作一般背景阅读，无直接代码借用点 | 能直接解决两台中的某一具体痛点（如文献检索、防废话规约） | 架构级核心解药（直接解决长论文上下文爆炸、长程交接中断、多 Agent 冲突） |

---

## 模块四：鲁组科研与三台工程强契约挂载点（Mount Points）

每份调研必须指明代码资产对接当前工作区的哪一个物理位置：

1. **科研台（`05_科研台_学习台_工作台支撑/`）**：
   - `research-knowledge`：用于鲁组长论文（SBTPN, EdgeIM 等）分级加载与引文图谱构建；
   - `research-runtime`：用于本地离线文献检索与学术工具链；
2. **工作台（`05_科研台_学习台_工作台支撑/`）**：
   - `workbench-app`：用于多 Agent 任务 DAG、租约锁机制、Token 预算看板；
   - `TASK-20260918-005`：用于跨会话交接（Hand-off）的不可抵赖证据链与状态保存；
3. **学习台（`01_进组总计划/`、`08_科研方法/`）**：
   - 进组新人从零精通课程体系、Claude Code 专属交互式教学导师。

---

## 模块五：机器可校验的 12 项 Done-When 验收门禁

审核 Agent 对照检查，必须 12 项全通过：
- [ ] 1. Frontmatter 元数据完整，ID、Commit、SPDX、安全评级无缺失；
- [ ] 2. 至少引用了 2 个真实的源码文件，并给出了精准到行的 `file_path:line_number` 锚点；
- [ ] 3. 绘制了完整的数据流/时序 ASCII 或 Mermaid 架构图；
- [ ] 4. 显式执行了 5 项“纸老虎”排查，并明确标记是否存在虚标；
- [ ] 5. 六维雷达评分的每一项，都必须附带至少一句话的“事实代码依据”；
- [ ] 6. 提取了至少 1 段可独立移植/复用的代码或契约原文；
- [ ] 7. 列出了至少 2 个具体输入导致失败的 Anti-Pattern 场景；
- [ ] 8. 明确给出了对接鲁组并发论文或三台施工蓝图的具体目录与机制；
- [ ] 9. 若为排除项（SHELVE），给出了排他的技术/历史司法证据；
- [ ] 10. 若为教程项，明确说明了其实验代码的硬核度与课程大纲提取建议；
- [ ] 11. 给出了确定性的五选一处置裁决；
- [ ] 12. 格式合规，全篇无空占位符（严禁 `TODO`、`待补充`、`...`）。
