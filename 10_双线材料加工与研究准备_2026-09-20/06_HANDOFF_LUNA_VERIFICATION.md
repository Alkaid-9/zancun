# JINZU_MASTER_V2 · 06_HANDOFF_LUNA_VERIFICATION

**版本**：初版
**日期**：2026-09-21
**状态**：DISPATCH-READY / EXECUTION-NOT-STARTED
**执行者**：Luna
**派发者/验收者**：主控（本仓当前会话）

---

## 0. 这份交接文档解决什么

05_CROSSCHECK_GPT_ROUND2.md 第五节记录了一批来自 ChatGPT 讨论（非论文原文）的二手技术细节，标注为"未核实"，明确要求"使用前必须对照论文原文确认""在核实之前，不要把这张表写入 00–04 任何一份文件的正文"。

本文档把其中两项具体核对任务正式派发给 **Luna**：

1. PetriBench 的 2×2 任务分类法 + PCA 解释力数字（91.7%→78.9%）。
2. ContrAgent 的 tool-call predicate 词表。

第三项决定（"三合一 toy"是否立项）**不在本次派发范围**——已由主控直接处理，见 04_BRIDGE_LU_SUN_OPENAI.md 新增的 B5 节，不需要读论文核实，因此不占用 Luna 的读文时间。

---

## 1. 角色与边界（沿用本仓既有 worker 纪律）

Luna 是**只读核验 worker**，不是判断者：

- 只读指定 PDF 的指定/相关章节，不联网检索、不查引用扩展、不读本仓其他文件、不猜测。
- 不判断 novelty、不判断"这个发现是否重要"、不判断 PASS/OWNED/VERIFIED 之类的仓库状态标签——这些由主控在收到回执后另行处理。
- 不写本仓任何文件。回执以对话/输出形式交回，由主控逐条核对后手工写入 03_PAPER_TO_CAPABILITY_PIPELINE.md 与 05_CROSSCHECK_GPT_ROUND2.md。
- 每条结论标注 `SOURCE FACT`（原文明确写的）/ `RECONSTRUCTION`（原文没有这个说法，是转述者重新组织的）/ `HYPOTHESIS`（推测）/ `UNKNOWN`（没找到或无法确认）。
- 首行只能是 `complete` / `partial` / `blocked`；结尾列出未覆盖范围和不确定性，不能因为"大部分对上了"就整体宣称 complete。
- 如果发现 GPT 转述与原文不一致，**两边都要给出原文定位**（页/节/表/图号），不能只说"不一致"而不给证据。

---

## 2. 输入文件（身份已冻结，来自 07_第二轮研究动态_三论文拆解与JINZU应用计划.md，未变化）

| source_id | 本地路径 | 题名 | 版本 | SHA-256 |
|---|---|---|---|---|
| R2_PETRIBENCH | `/mnt/d/Alkaid/Downloads/2609.19883v1.pdf` | *PetriBench: Benchmarking LLM Reasoning over Dynamic State Spaces* | arXiv:2609.19883v1, 2026-09-17 | `989f94fb791597ecaf66b234829f141ae17dc5d60a3dc6f87e126cdc41b16a91` |
| R2_CONTRAGENT | `/mnt/d/Alkaid/Downloads/2609.18128v1.pdf` | *Symbolic Temporal Supervision of LLM Agents Using Contracts* | arXiv:2609.18128v1, 2026-09-16 | `b338efa71c6ae3843200345024967b60ef2d3cc40a806b52c77b41e1864269e3` |

**第一步动作**：打开文件前先核对 SHA-256，与上表不一致立即停止并报告，不要假设"应该是同一篇"就继续。

---

## 3. 核对任务 A：PetriBench 的 2×2 任务分类法 + PCA 数字

**被核对的原始转述**（逐字取自用户转发的 GPT 讨论，不是本仓已有材料）：

> 论文设计了一套非常干净的二维 taxonomy：
>
> |            | Finite horizon      | Infinite horizon       |
> | ---------- | ------------------- | ----------------------- |
> | **Local**  | Minimum Token Steps | L0 / L4 Liveness        |
> | **Global** | Reachable Markings  | Deadlock / Boundedness  |
>
> ……作者用 PCA 也观察到第一主成分解释度从 Easy 的 91.7% 降到 Hard 的 78.9%。

**需要回答的问题**：

1. 论文原文是否真的用这个 2×2（local/global × finite/infinite）结构组织六个任务？如果是，对应的表/图/章节号是什么？
2. 本仓其他文件（07/08）已经写"Petri 网的六个标准任务"——请确认这 2×2 网格里六个具体任务名称（Minimum Token Steps / Reachable Markings / L0 Liveness / L4 Liveness / Deadlock / Boundedness）与论文原文的任务命名逐一对应，还是转述者做了合并/改名/遗漏（例如论文是否还提到 livelock 或其他未被这张表覆盖的任务）？
3. "第一主成分解释度从 91.7%（Easy）降到 78.9%（Hard）"这句话，原文是否有这两个具体数字？出现在哪个表/图？衡量的对象到底是什么（模型分数的方差、还是别的什么变量）？"Easy"和"Hard"在原文里是不是这样命名的难度档位？
4. 这个 PCA 发现在原文里对应的结论句是什么（原句摘录）？转述"随着难度增加，model-specific reasoning profile 开始分化"这句话是转述者的解读还是论文自己的措辞？

**输出**：每个问题一条结论，标 SOURCE FACT/RECONSTRUCTION/HYPOTHESIS/UNKNOWN，附原文页码/表号/图号和关键原句摘录。

---

## 4. 核对任务 B：ContrAgent 的 predicate 词表

**被核对的原始转述**：

> 然后把每个 event 转成 checkable predicates，例如：
> ```
> Call(tool)
> ArgHas(...)
> OutHas(...)
> Match(...)
> Flow(source, sink)
> Perm(...)
> Cnt(tool)
> Tok
> Depth
> Num(...)
> ```

**需要回答的问题**：

1. 论文原文是否确实定义了这十个谓词？逐一确认名称、参数（arity）、精确语义是否与上面列出的一致。
2. 是否有遗漏（原文还定义了别的谓词但转述没提到）或合并（转述把原文两个不同谓词写成了一个）？
3. 这些谓词在原文中出现的章节/定义号是什么？
4. 这套谓词与本仓 03_PAPER_TO_CAPABILITY_PIPELINE.md 已经写的 ContrAgent event 分解（`proposal/accepted_call/return/effect/END`）是同一层还是不同层——即谓词是描述"事件类型"还是描述"用于组装 A/G contract 的原子条件"？（这是判断两者是否冲突还是互补的关键，不能只看名字像不像。）

**输出**：同上，每条标 SOURCE FACT/RECONSTRUCTION/HYPOTHESIS/UNKNOWN，附原文定位。

---

## 5. 顺带任务（同一份 PDF 已经打开，顺手做，不额外派发）

03_PAPER_TO_CAPABILITY_PIPELINE.md 里两篇论文的 `identity_manifest` 目前 `authors` 和 `page_count` 两个字段仍是"待填"（`paper_id`/`title`/`version`/`hash` 已经在 07 文件中确认，不需要重复核实）。请在核对任务 A/B 过程中顺手补：

| source_id | authors（待填） | page_count（待填） |
|---|---|---|
| R2_PETRIBENCH | ? | ? |
| R2_CONTRAGENT | ? | ? |

这不是本次派发的核心任务，如果时间不够可以跳过，跳过要明确写"未做"而不是留空不说明。

---

## 6. 停止条件

- PDF 打不开、页数异常、SHA-256 不匹配 → 立即报告 `blocked`，不要用记忆或推测替代。
- 任务 A/B 中任何一条转述在原文中完全找不到对应内容 → 标 `UNKNOWN`，不要因为"大概意思差不多"就标 `SOURCE FACT` 或强行找一个不太贴切的段落当依据。
- 不因为发现转述有误就扩大核对范围去重新解读整篇论文的其他部分——只回答第 3、4 节列出的具体问题。

---

## 7. 回执交回后的去向（不需要 Luna 处理，仅供主控自己对照）

- 任务 A、B 的回执 → 更新 05_CROSSCHECK_GPT_ROUND2.md 第五节（把"未核实"改为已核实的结论，或记录"核实后发现转述有误"的具体差异）。
- 若核实通过 → 允许把 2×2 taxonomy 写入 03_PAPER_TO_CAPABILITY_PIPELINE.md 的 PetriBench P1 Mechanism Sheet；predicate 词表写入 ContrAgent 的 P1 Mechanism Sheet。核实前，两者都不得进入 00–04 正文（05 文件第五节原有的限制不变）。
- 顺带任务的 authors/page_count → 更新 03 文件对应 `identity_manifest` 表格。
