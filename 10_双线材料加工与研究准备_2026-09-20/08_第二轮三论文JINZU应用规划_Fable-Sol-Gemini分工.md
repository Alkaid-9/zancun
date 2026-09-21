# 第二轮三论文 JINZU 应用规划与模型分工

**状态**：PLAN / READY FOR WAVE 0 FREEZE  
**日期**：2026-09-20  
**审计基准**：`RESEARCH_AGENT_CONSTRAINT_v1.0.md` + `GEMINI_WORKER_CONTRACT.md` + 2026-09-20 红队审计教训

---

## 0. 三论文身份冻结

所有后续工作必须基于这个表的事实，任何身份错配立即停工。

| source_id | 本地文件 | PDF 首页标题 | arXiv ID | 版本日期 | SHA-256 | 状态 |
|-----------|---------|-----------|---------|---------|---------|------|
| R2_STRING_DIAGRAMS | `/mnt/d/Alkaid/Downloads/2609.20478v1.pdf` | *String Diagrams for Process Mining* | 2609.20478v1 | 2026-09-17 | `9011e7d...` | ✓ VERIFIED |
| R2_CONTRAGENT | `/mnt/d/Alkaid/Downloads/2609.18128v1.pdf` | *Symbolic Temporal Supervision of LLM Agents Using Contracts* | 2609.18128v1 | 2026-09-16 | `b338efa...` | ✓ VERIFIED |
| R2_PETRIBENCH | `/mnt/d/Alkaid/Downloads/2609.19883v1.pdf` | *PetriBench: Benchmarking LLM Reasoning over Dynamic State Spaces* | 2609.19883v1 | 2026-09-17 | `989f94f...` | ✓ VERIFIED |

**重要**：三篇均为未经同行评审的 arXiv 预印本。所有机制、数字、贡献都按"此论文宣称"处理，不按已定论使用。

---

## 1. JINZU 路线中的位置

### R2_STRING_DIAGRAMS → T2 跨表示语义层

**问题**：EdgeIM 发现流程网后，怎么比较另一种记号法的发现结果？两个网的"相同"指什么——trace 相同？并发结构相同？对象交互序列相同？

**本论文的贡献**：
- 定义装饰 cospan (decorated cospans, Def 4) 和 cospan-algebra signatures (Def 6) 作为过程图的标准表示。
- 证明 signature equality ⟹ trace equivalence（严格细于）；signature inclusion ⟹ trace inclusion（反向不成立）。
- 恢复研究：对象中心的事件日志 + 流程网发现 = discovered causal net signature ⊂ discovered Petri net signature（严格包含）。

**与 EdgeIM 的关系**：EdgeIM 产出的 Petri 网在这个框架下有一个 signature；如果用对象中心输入重新发现，会得到一个更细的 causal net signature。这提供了事后审计钩子（"发现结果为什么不一样"）和���较尺度定义（"我们要保留的 sameness 是什么"）。

**最小可用产物**：
- `sameness_ladder.md`：五层sameness从弱到强（trace equivalence < concurrent-structure equivalence < signature equality）；每层一个"相同但下层不同"的反例对。
- 一句话：signature equality vs trace equivalence 方向的逻辑证明梗概（不要全文重复定理 4.1–4.4，只标源页）。

**上限声明**：
- 本论文不说"发现"能自动产出正确的 signature，只说当你有了两个网（用什么方法发现的），怎么比它们的 signature。
- 不支持对象数量、消息顺序、时间窗口等复杂约束——那超出本论文的形式化范围。
- 这是 CONNECT 材料候选（用于 EX-05 后"并发不同也能 trace 一样"这个反例），不改变 EX-05 本身。

---

### R2_CONTRAGENT → T3-lite 运行时可观测与合约监视

**问题**：给 Agent 写"做不了这个"的规则，怎样既能阻止坏动作（online），又能事后打分（offline）？前端系统有哪些盲点？

**本论文的贡献**：
- 合约 C = (A, G) 是两个 ALTLf 公式（有限轨迹上的线性时序逻辑）。
- 编译成一个 DFA，同一个 DFA 既用来：
  - **Online**：每当 Agent 发起工具调用，DFA 检查约束，违反则阻止。
  - **Offline**：给定完整轨迹（tool-call-1, return-1, tool-call-2, return-2, ...），DFA 重放一遍，输出"通过/违反"。
- 四个基准测试 (SOPBench, AgentDojo, R-Judge, τ²-bench) 展示安全提升（32%→98%）和开销（≤+0.135s）。

**信任边界**：DFA 假设以下被忠实观测和报告：
- **Tool interface**：Agent 发起什么工具调用、什么参数（通过 MCP/API 层观测）。
- **Return value**：工具返回什么数据。
- **Event counter / context**：有多少次调用、目前什么上下文状态。

**盲点（论文明确说不覆盖）**：
- 自由文本语义安全（Agent 在 prompt 里说"忽略这个规则"——DFA 看不懂自然语言）。
- 意图安全（Agent 真实想做什么，不只是表面工具调用序列）。
- 观测完整性（Return value 是否诚实、API 层是否被绕过）。

**最小可用产物**：
- `predicate_blindspot_pairs.json`：至少两个混淆对。形式：两条轨迹 T1, T2，在所有已声明谓词（e.g., "called Write"、"return value is JSON"）上取值相同，但业务风险不同（e.g., T1 写了敏感路径，T2 没有，但都是"调用了 Write"）。说明为什么 DFA 必然给两个相同 verdict，以及这说明了观测谓词不足。
- 一句话清单：谓词假设、A/G 合约的信息上限、什么情形下 DFA 无法区分。

**上限声明**：
- 只证明"给定已声明谓词，阻止约束之外的轨迹"，不证明"已声明谓词本身足以覆盖安全"。
- 不支持状态机之外的 AI 决策（Agent 学到的偏见、推理失败、隐形目标）。
- 本论文的 "Limitations" §明确说"free-form semantic harms need separate check"。

---

### R2_PETRIBENCH → 评价线的 exact-oracle 基准

**问题**：如何设计一个 LLM 推理基准，避免模型靠"语言统计"而非真逻辑得高分？

**本论文的贡献**：
- 六个任务族（Reachable Markings, Liveness, Deadlock, Boundedness 等）。
- **Property-preserving 生成**：生成器产出一个 Petri 网，用 TINA solver 计算真值，模型只看题面。
- **错误分类**：四个模型 (Claude Opus 5 / Sonnet 5 / Haiku 4.5 / GPT-5.6 Sol / Gemini 3.8 Flash / Grok 等) 在每个任务上的失败都被分类（Token-step 不够、Transition semantics 错、Behavior search 不完整 etc）。
- **难度生成**：Easy/Medium/Hard 按网大小和复杂度生成；Hard 任务上准确度显著下降，说明难度有效。

**与 JINZU 的关系**：作为 T2/Petri-net 基础的评价方法范本。我们能复用这套"生成器→真值→分类"的框架来评价我们的 Petri 网发现和验证。

**最小可用产物**：
- `exact_oracle_eval_protocol.md`：冻结一个有限时域任务（e.g., reachability on nets ≤10 places）和一个无限时域任务（e.g., liveness），定义 Petri 网生成、TINA solver 调用、错误分类表（不重新分类，引用论文的分类体系）、通过/失败标准。
- 不需要真跑，只交协议和一个手工例子。

**上限声明**：
- 高分只支持"给定形式表示后的状态空间推理"，**不支持**：
  - 日志到模型恢复的建模能力。
  - 真实系统验证。
  - 通用程序验证能力（不在 Petri 网范围内）。
- 这是"No Free Checker"（推理的形式基础）之后的事，不是一个通用 LLM 能力测试。

---

## 2. 昨晚教训转成本轮阻断门

| 已发生的问题 | 本轮强制动作 | 阻断条件 |
|-----------|-----------|---------|
| 真实论文被串成另一条研究线 | 每条机制必须指向 PDF 页、章节、定义/定理号 | 题名、对象、符号与原文不符立即停 |
| 虚构论文名与假年份进入计划 | 所有命名实体只来自原件；无法回源写 UNKNOWN | 出现无坐标的题名、数字、仓库名 |
| 硬编的 "passed" 字符串被当证据 | 机制、算法、代码运行声明都附真实 command/log/exit | 仅有"看起来对"没有真实日志则拒收 |
| 同一模型家族红蓝互审放大错误 | 复核只产生待核问题；独立 oracle 或主控二次打开原文 | 仅凭第二个同族模型同意就升级状态 |
| 事后才发现遗漏 | 交付前从摘要/贡献/正文/结论反向覆盖每条 claim | 主要贡献或局限没有去向即拒 |

---

## 3. Fable / Sol / Gemini 分工与任务包

### 3.1 模型岗位定义

| 模型 | 岗位 | 本轮角色 | 输出形式 | 不得做 |
|------|------|--------|--------|--------|
| **Sol** (GPT-5.6) | 主拆一手证据 | 逐篇独立核定理/定义/算法、四基准、局限与 JINZU 接口 | DRAFT（每篇一次终态） | 写仓、融合三篇、用摘要代替全文、宣布复现或选题成立 |
| **Fable** (Claude，即我) | 教学与综合 | 消费 Sol 证据包后，产三张"对象→状态→规则→反例"教学卡 + 练习空白 | EVIDENCED（回源后） | 代写用户答案、拍 PASS/OWNED、自行补论文事实、打开 EX-06/sealed |
| **Gemini 3.8 Flash** | 固定快照的字段抽取 | 每篇最多两个微包：身份/贡献原句，表格/局限/仓库字段 | DRAFT（仅提取） | 读主仓、读完整作答、工具/网络/写入、机制裁决、方向综合、novelty 判定 |
| **主控 M**（用户） | 唯一验收与写权 | 冻结三个哈希，逐条回源 Sol/Gemini 产出，实现最小反例，写入计划产物 | VERIFIED（经二阶段核验） | 用模型互相同意代替原文、用标签代替真实运行 |

**当前 Gemini 状态**：`CONTROL-PLANE READY / PRODUCTION HOLD`。専用入口的真实上游烟测仍未成功（最后被 `RATE_LIMIT` 止损）。因此 G-R2 包排入 `HOLD`；门禁未开时，相同字段由 Sol/Luna 或主控本地抽取，**不阻断主线**。

---

### 3.2 三份 Sol 任务包（可并行）

#### S-R2-STRING_DIAGRAMS

**输入**：`R2_STRING_DIAGRAMS` PDF 全文（33 页）  
**约束**：
- 只答题，不写仓。
- 单一会话，返回一次。
- 如遇 pages 21–33 不可读或定理有歧义，标 PARTIAL 并说明确实卡在什么。

**问题**：
1. 四个构造定理（§4, Theorems 4.1–4.4）各说什么？（一行/定理，含页号和定理号）
2. 恢复研究（§5）怎么做的？输入什么日志，比较哪些记号法，结果怎么说 causal-net-signature 与 Petri-net-signature 的关系？
3. 跨记号对等（§6）对 Petri net / causal net / process tree / BPMN 各说什么？
4. 相关工作（§7）与哪些名字论文/框架比较？本论文的差异是什么（一句话/论文）？
5. 代码仓库：论文有没有给 "proc-posets" 或其他工件的真实 URL？如果有，原文在哪一页，怎么说的？如果没有，说"NOT FOUND"并解释找过哪些地方（正文/References/Appendices）。

**交付格式** (SD_P1_DRAFT)：
- **Claim Table**（页号 + 定理号 + 一行声明）
- **Symbol Table**（pages 21–33 中的新记号，不重复 Defs 4/6/7/14）
- **方向清单**（equality/inclusion/equivalence 的逻辑方向；反向不成立处有反例或原文边界）
- **恢复研究例子**（从 §5 一个实际例子，引用页/图号）
- **Repository URL**（URL + 页号，或 "NOT FOUND，搜索范围：正文、References、Appendices"）

**失败条件**：
- Pages 21–33 无法读取或定理号无法定位。
- 用摘要或通用知识代替全文主线。
- 方向混淆（把单向定理写成充要条件）。

---

#### S-R2-CONTRAGENT

**输入**：`R2_CONTRAGENT` PDF 全文（13 页）  
**约束**：同 S-R2-STRING_DIAGRAMS。

**问题**：
1. DFA 同时支持 online enforcement 和 offline scoring，数据流怎么走？tool-call event 怎么变成 AP (atomic proposition)，轨迹怎么形成，DFA 怎么消费？（逐步，含页号）
2. 定义 State / AP / ALTLf / Assume-Guarantee (A,G) / DFA 五个核心概念，各给一行定义和源处。
3. 四个基准（名字、headline 数字、表号）。数字逐一定位，不要四舍五入，原文怎么写就怎么写。
4. 至少一个"盲点对"：两条轨迹在所有已声明谓词上相同，但业务风险不同；说明 DFA 为何必然同等对待。
5. 论文有没有公开代码仓库链接？原文在哪里，怎么说的？无则说 "NOT FOUND"。
6. Limitations 段明确说 DFA 不能覆盖什么？完整引用那一段（不要摘选）。

**交付格式** (CA_P1_DRAFT)：
- **Data Flow Diagram**（工具调用 → AP → DFA 状态 → 阻止/评分，含页号）
- **概念表**（State/AP/ALTLf/A-G/DFA，每个一行 + 页号 + 定义号）
- **基准审计**（基准名、headline 数字原文、Table 号和页号）
- **盲点反例**（两条具体轨迹、共同谓词值、不同风险、为什么 DFA 无法区分）
- **代码仓库**（链接 + 页号，或 NOT FOUND）
- **Limitations 原文**（verbatim 或精确释义，带页号）

**失败条件**：
- 基准表数字不精确。
- DFA 机制描述混淆"阻止"和"评分"两种用法。
- Limitations 段无法定位。

---

#### S-R2-PETRIBENCH

**输入**：`R2_PETRIBENCH` PDF 全文（67 页）  
**约束**：同 S-R2-STRING_DIAGRAMS。

**问题**：
1. 六个任务族分别叫什么？（逐一，页号）
2. "Property-preserving generation" 怎么做？生成器产什么，TINA solver 干什么，模型只看什么？（数据流，页号）
3. 错误分类体系有几类？各叫什么？（完整列表，页号）
4. 四个基准（论文说的 benchmark，不是学术会议）：名字、benchmark 结果数字、错误分布、Table 号。
5. 难度生成（Easy/Medium/Hard）：按什么参数生成？三个难度的准确度分别是多少？（逐行，含数字原文和页号）
6. 论文有没有发布 benchmark suite、生成器代码、solver 脚本？哪一页说的？链接是什么（如果有）？

**交付格式** (PB_P1_DRAFT)：
- **任务矩阵**（六族 × 四基准，核心结果逐项定位）
- **生成与评价流**（生成器 → TINA → 分类，含页号）
- **错误分类表**（名称、定义、出现频率）
- **难度分布**（Easy/Medium/Hard 参数和准确度数字）
- **Artifact 声明**（发布了什么、在哪里、链接是什么，或 NOT FOUND）

**失败条件**：
- 错误分类无法完整列出。
- 难度参数混淆（size/complexity/depth 各是什么）。
- 数字自己补或四舍五入。

---

### 3.3 Fable（我）的综合与教学任务

**依赖**：Sol 三包均返回且 M 已逐条回源接收。

**任务**：为每一篇产一张"零基础教学卡"，一对完整例子，一个空白练习。

#### F-R2-STRING_DIAGRAMS：Sameness 的阶梯

**输入**：M 已接收的 String Diagrams 事实表（定理、signature 定义、equality/inclusion 方向）

**教学目标**：学习者从"S/E/R 保持"（EX-05 已学）走到"trace 与并发结构不同时的 sameness"（新反例）。

**产出**：
1. **教学卡**：一页，标题"Signature vs Trace：并发看起来一样也能画得不一样"
   - 三层概念梗概（Trace ⊂ Signature ⊂ Execution structure）
   - 一对学习者能自己验证的反例（两个网，相同 trace，不同并发）
   - 与 EdgeIM 发现的关系（一句话：发现 A 和发现 B 的 signature 怎么比）
2. **完整例子**：一个 Petri 网分解成 causal net，标注 signature；一个独立发现的结果，指出 signature 怎么包含关系。（不给答案，但给问题）
3. **空白练习**（CONNECT 候选）：给定两个网的 trace 相同的反例，学习者指出 signature 怎么不同。

**禁止**：
- 改变 EX-05 本身或其 rubric。
- 给正式题的答案。
- 引入论文没有的记号或概念。

---

#### F-R2-CONTRAGENT：从工具调用到合约状态

**输入**：M 已接收的 ContrAgent 事实表（DFA/online/offline、盲点对、信任边界）

**教学目标**：从"工具调用序列"讲到"DFA 状态与 verdict"，明确"什么时候 DFA 无法区分"。

**产出**：
1. **教学卡**：一页，标题"DFA 的眼睛和看不见的地方"
   - 工具调用 → AP → DFA 转移（三步，每步一张微图）
   - 盲点对案例（两条调用序列，表面一样，风险不同，为什么 DFA 误判）
   - 三个信任边界清单（观测的、假设的、未假设的）
2. **完整例子**：一个真实的不安全轨迹（e.g. 试图 overwrite critical file），DFA 如何阻止；一个"看起来坏"但不违反合约的轨迹，说明谓词的局限。
3. **空白练习**：给定一个新的盲点对描述，学习者标出哪个谓词补充就能区分。

**禁止**：
- 宣布"DFA 解决了 Agent 安全"（论文明说不能）。
- 混淆 online/offline 两种用法。
- 编造合约例子。

---

#### F-R2-PETRIBENCH：有限与无限推理的分层

**输入**：M 已接收的 PetriBench 事实表（六任务、错误分类、难度）

**教学目标**：用一道有限题和一道无限题讲清"exact oracle"与错误分层的关系。

**产出**：
1. **教学卡**：一页，标题"有限和无限的推理不一样"
   - 两个任务对比（e.g., Reachability「有限」vs Liveness「无限」，各什么意思）
   - 错误分类表（做错通常因为什么——Token 不够？逻辑错？状态转移不懂？）
   - 与"通用推理基准"的差异（"这不是测 LLM 通用聪慧，是测 formal reasoning in Petri nets"）
2. **完整例子**：一个简单 Petri 网的 reachability 题（答对给手推过程；答错指出错误类型）。一个 liveness 题，提示怎么从"似乎没死"推到"绝对不死"。
3. **空白练习**：两道题的参考解与作答区分离（学习者先自己做，再看参考）；错误分类表供查。

**禁止**：
- 把参考结果放进学习者的起始文件。
- 用答案长度评分（是推理，不是文字量）。
- 夸大"推理能力"——这只测"给定形式、推理状态空间"。

---

### 3.4 Gemini 微包（当前 HOLD，不启动真实会话）

**当前门禁**：Gemini 专用入口的真实上游烟测仍未成功（2026-09-20 最后分类为 `RATE_LIMIT`，止损）。

**模板仅供参考**，待门禁通过后启动：

| 任务 ID | 输入快照 | 单一问题 | 交付 | 验收 | 禁止 | 后备 |
|--------|--------|--------|------|------|------|------|
| G-R2-SD | SD 首页 + §4 定理陈述页 + §5 恢复研究例子页 | 这些页上分别说了什么题录、定理陈述、案例关键数字？ | DRAFT 表 (claim/field/value/location/quote) | G01-G03 逐字段回源；最多 20 分钟 / 1 次修正 | 工具/网络/写入；机制裁决 | Sol 或主控本地抽取 |
| G-R2-CA | CA 首页 + DFA 表 + 基准结果表页 | 这些页上的概念、评测数字、作者声明分别是什么？ | DRAFT 表 | G01-G03 + 数值必须带坐标 | 顺着引用扩展检索；宣布方法有效 | Sol 或主控本地抽取 |
| G-R2-PB | PB 首页 + 任务表 + 难度分析 + 限制声明页 | 六任务、难度参数、错误分类、论文不声称什么？ | DRAFT 表 | G01-G03 + 任务名与数字逐项定位 | 评判推理能力；填补找不到的链接 | Sol 或主控本地抽取 |

---

## 4. 执行波次与停止条件

### Wave 0：身份冻结与基线登记（M 执行，前置）
- 重读 HEAD/status。
- 记录三个 PDF 的 SHA-256 和落地路径。
- 建立三份空 claim ledger（摘要 / 贡献 / 正文 / 结论段入口）。
- **停止条件**：任何一个哈希不符或文件不可读。

### Wave 1：Sol 三包独立执行（可并行）
- S-R2-SD（String Diagrams）
- S-R2-CA（ContrAgent）
- S-R2-PB（PetriBench）

**执行顺序**：如并发资源紧张，按 ContrAgent → PetriBench → String Diagrams 的调度顺序串行（不是优先级，只是队列）。

**单包规则**：新会话、单一问题、一次终态返回（PARTIAL 可接受，表示真实卡点；多次修正则停）。

### Wave 2：M 主审（前置 Fable）
- 对每份 Sol 产出逐条抽查：
  - 身份（论文题目、作者、年份正确吗？）
  - 一个核心形式对象（定理号、定义号与原文一致吗？）
  - 一个主要结果（数字原文怎么说的？是否引用精确？）
  - 一个局限（论文自己怎么说不能做什么？）
  - 所有拟进 JINZU 的句子（机制是否真的在原文出现，方向是否正确？）
- **发现一处关键错误就扩大抽查同类主张**。
- **通过标准**：所有主张能回到 PDF 页号、无身份混淆、数字精确、方向清晰。

### Wave 3：Fable 教学卡（仅用 M 已接收的事实）
- 三张教学卡（String Diagrams / ContrAgent / PetriBench），均基于 Wave 2 的已验收事实。
- String Diagrams 反例可与 EX-05 结合（CONNECT 候选）。
- 其余两张进学习队列，待后续评估。

### Wave G：Gemini 微包（当前 HOLD）
- 预留，不启动真实会话。
- 门禁条件：Gemini 专用入口取得一次真实、合法快照成功回执。
- 启动后每包最多 3 个输入、20 分钟、1 次定点修正。
- 任一伪造坐标或自升状态，整包拒收，关闭本轮 Gemini。

### Wave 4：反向覆盖与交付（M 执行）
- 核查每篇的摘要、贡献段、正文主要结果、定理、局限、artifact 声明是否都有去向（接收/拒绝/未核）。
- 产三张研究卡（概念→推导→接口→上限）。
- 产三份最小产物规格（sameness_ladder / predicate_blindspot_pairs / exact_oracle_eval_protocol）。
- 产 JINZU 桥接矩阵（三篇→T2/T3-lite/评价，各贡献什么、不贡献什么）。

---

## 5. 验收检查表（R2-Q 系列）

| ID | 检查项 | 通过条件 | 失败处置 |
|----|--------|---------|---------|
| R2-Q01 | 身份映射 | 三个文件名、题名、arXiv ID、版本、SHA-256 一一对应；无歧义 | 身份错配拒收，停止下游 |
| R2-Q02 | 主张覆盖 | 每篇的摘要/贡献/正文/结论段所有主张并集进 ledger；每条有 locator | 缺页号拒收；主张漏落扩大抽查 |
| R2-Q03 | 逻辑方向 | Equality/inclusion、assumption/guarantee、finite/infinite 精确；反向不成立处有反例 | 混淆单双向拒收；方向反转整篇留证据化 |
| R2-Q04 | 应用边界 | 每条 JINZU 建议标 SOURCE FACT / RECONSTRUCTION / HYPOTHESIS / UNKNOWN；写不能推出什么 | 无边界标注拒收；过度宣称删去 |
| R2-Q05 | 最小产物 | 三规格各有输入、输出、oracle/反例、失败条件、运行状态；未跑标 NOT_RUN | 伪造日志拒收；只文本可接收但标 NOT_RUN |
| R2-Q06 | 学习隔离 | 不代写 EX-05/EX-06，不拍 PASS/OWNED，不改 Ledger；仅 SD 反例作 CONNECT 候选 | 越界拒收;文件回滚，不让模型自改 |
| R2-Q07 | 模型分权 | Sol 主拆、Fable 教学、Gemini 抽取、M 验收无混用；异构复核非同族自审 | 混用或同族互审，两份隔离重做 |
| R2-Q08 | 反向覆盖 | 三篇全部主要贡献、限制和 artifact 声明各有"接收/拒绝/未核"去向；无不解释遗漏 | 遗漏贡献拒收，整篇重核 |

---

## 6. 对外可用上限与声明

**本轮对 JINZU 的最高可用表述**：

> 已能把三篇新论文（String Diagrams for Process Mining、ContrAgent、PetriBench）分别放入 JINZU 路线的三个位置：
> - **String Diagrams** → T2 跨表示语义（sameness 定义与比较）
> - **ContrAgent** → T3-lite 运行时合约监视（DFA 双模式与信任边界）
> - **PetriBench** → 评价线的 exact-oracle 基准（生成→真值→分类）
> 
> 并产出三份最小产物的**规格**（未实装）和三张**教学卡**（待验收）。

**不得声称的**：
- ❌ "已掌握三篇论文"（只拆了定义/主要定理/局限，不是全文覆盖）
- ❌ "已复现论文的贡献"（规格和教学卡不等于运行）
- ❌ "已证明新方向成立"（这是跨论文的应用假设，不是论文本身的贡献）
- ❌ "已形成安全方法"（ContrAgent 的 limitations 明确说不能覆盖语义安全）

**待后续**：
- 实装三份规格（sameness_ladder / predicate_blindspot_pairs / exact_oracle_eval_protocol）。
- 让用户解释三篇对 JINZU 的具体价值（而不是我们代解释）。
- 用真实例子（EdgeIM 发现结果、真实 Agent 轨迹、简单 Petri 网）验证三篇的适用边界。

---

## 7. 时间与资源约束

- **Sol 三包**：各目标 15–30 分钟单包，最多一次修正；总不超过 90 分钟。
- **Fable 教学卡**：三张各 30–40 分钟；总不超过 2 小时（含 M 回源检查）。
- **Gemini 微包**：每包 20 分钟硬停；当前 HOLD，不消耗时间。
- **M 主审与交付**：另计，不与 A 线 260 分钟竞争。

---

## 8. 文件归档与版本控制

**新增写域**：
```
10_双线材料加工与研究准备_2026-09-20/
├── 00_control/
│   ├── R2_baseline.json          # 身份冻结与哈希
│   ├── R2_claim_ledgers.tsv      # 三份空 ledger
│   └── R2_execution_log.md       # 波次进度
├── B_papers/
│   ├── string_diagrams/
│   │   ├── SD_P1_DRAFT.md
│   │   └── sameness_ladder.md
│   ├── contragent/
│   │   ├── CA_P1_DRAFT.md
│   │   └── predicate_blindspot_pairs.json
│   └── petribench/
│       ├── PB_P1_DRAFT.md
│       └── exact_oracle_eval_protocol.md
├── research/
│   ├── F_R2_STRING_DIAGRAMS_teaching.md
│   ├── F_R2_CONTRAGENT_teaching.md
│   ├── F_R2_PETRIBENCH_teaching.md
│   └── R2_JINZU_integration_matrix.md
└── manifest.json                  # 交付物清单、hash、限制
```

**不修改**：
- `01_两天执行合同.md` 及所有 01_xxx 内容。
- `02_逐篇施工与专项验收.md` 及所有 A 线文件。
- 原 MAS 仓（`/mnt/d/MyResearch/MAS_Safety_Project`）。
- 邮件、简历、主要承诺。

**分支与提交**：
- 当前工作树在 `audit/redteam-external-ref-2026-09-20` 分支。
- 本计划的中间产出（Sol 包、主审笔记、教学卡初稿）不提交 main；只在主控最终验收后，由主控决定何时、怎样并入计划性交付。

---

## 9. 后续决策项（留给用户）

1. **Gemini 烟测**：何时重试 Gemini 专用入口的真实上游烟测？当前选项：(a) 等 24 小时冷却后重试；(b) 跳过 Wave G，用 Sol/Luna 补；(c) 向 Anthropic 诊断。
2. **三教学卡的用途**：是否立即纳入后续课程（EX-06 / 新模块）？还是先收集三个月反馈后再定位？
3. **规格实装优先级**：三份规格中哪一个先实装？或是并行？

---

**状态**：READY FOR WAVE 0 FREEZE  
**下一步**：等主控确认身份与基线 → 派 Sol 三包 → 我逐条回源 → 产教学卡。

