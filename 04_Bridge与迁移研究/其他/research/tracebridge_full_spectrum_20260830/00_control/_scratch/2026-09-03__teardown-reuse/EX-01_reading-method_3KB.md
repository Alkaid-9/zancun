# EX-01 读法附页 · 三个知识库里只跟"读一篇算法论文"有关的那几条

## A4 一页执行法（2026-09-04，先用这一节）

三个本地来源只提供阅读动作和追问框架，不替学习者判断论文：

| 来源 | 当前本地路径 | 本页只取什么 | 不取什么 |
|---|---|---|---|
| Supervisor-Skills | `/mnt/d/MyResearch/external/Supervisor-Skills/`（核对时 HEAD `aff5de9e...`） | 逐条核查 AI 内容、核心判断由学习者完成、先问问题再看方法 | 自动评分、结论、顶会话术 |
| learning_research / pengsida 访谈 | `/mnt/d/MyResearch/external/learning_research/`（核对时 HEAD `a737e3f...`），访谈在 `pengsida_pdfs/` | 小例子、复现、反复阅读与主动验证 | 把名人经验当成当前论文证据 |
| research_growth | `/mnt/d/MyResearch/research_growth/`（核对时 HEAD `22ace3d...`） | 问题驱动阅读、出处记录、讲给别人听 | 旧领域模板、旧路线和预填判断 |

执行链只有五步，每步必须留下一个可检查产物：

1. **预测**：不开论文，为每个 G0 问号写 `我猜什么 | 为什么 | 什么文字会推翻我`。产物是带时间的 `PREDICTION`，猜错不扣分，也不回改。
2. **定位**：先按 `EX-01_reading-kit.md` 找印刷页/PDF 页/章节/算法行，再回 PDF 原件。TXT 只搜关键词。产物是 `问题 -> 页码 -> 行或图表标记`，找不到就记 `UNKNOWN`。
3. **证据标签**：把“看见的文字”和“自己的推论”拆成两句，分别标 `PAPER-TEXT / USER-INFERENCE / AGENT-SUMMARY / UNKNOWN`。产物是每句可追到页码；AI 提供的坐标仍需本人复核。
4. **反证**：为当前解释写一个竞争解释，并问“如果竞争解释为真，输入/更新/输出或实验表里应看到什么”。产物是一条可判对错的反证检查，不是新的结论。
5. **脱稿**：关掉 PDF、TXT、本页和所有 AI 对话，重写 G0 五问；再重新打开 PDF 查错。G0 note 落盘以后，拆解材料只用于逐句对照：`自己的句子 | 原文 | 拆解句 | 一致/冲突/仍 UNKNOWN`。

这五步与 Learning-Research OS 的边界一致：看到材料只是 `SEEN`；提交可检查 note 才是 `SUBMITTED`；通过冻结验收才是 `PASS`；到期冷启动仍能独立完成才是 `RETAINED`。三库来源最多解释“为什么这样读”，不能把任何 G0 判断升级成 `PAPER-TEXT`。

**写者 / 时间**：主窗 b270bae5（训练包出题窗），2026-09-04 02:1x。**层级**：evidence。
**跨窗提示**：科研体系通宵窗（TASK-20260904-001）的 RUNSTATE 泳道 B5 计划写的就是这个路径，依赖它的 B1–B3。本文先落盘，只覆盖第 1 站用得上的几条；B5 若跑，请**读后合并**而不是覆盖——它的 B1/B2（`../2026-09-04__research-system/`）是更全的组件审计，本文只是站内摘要。

**来源**：`external/Supervisor-Skills`（HEAD aff5de9）、`external/learning_research` + `pengsida_pdfs/`（HEAD a737e3f）、`research_growth/摘录文档/pengsida_learning_research/`
**裁定依据**：`00_control/BRIDGE_RESEARCH_LEARNING_REUSE_AUDIT.md:113`（learning_research = REFERENCE-ONLY）、`:132`（Supervisor-Skills 只作导师提问，不作裁判）
**用法**：这页不是新读法，是给 `EX-01_reading-kit.md` 那 12 个停靠点找"为什么这么读"的出处。每条一句话 + 指到原文行号，读第 1 站前扫一遍即可，不要花超过 10 分钟。
**没写进来的**：三库里关于选题、写作、投稿、画图、找导师的内容——这一站用不上，以后需要再回去翻。

## 1. 先做再读、读了要重做（对应 4.2 段 0 和段 2）

- 跑之前先写预测，读完再对——这是 OS §10 的规矩，三库里最接近的是 Schulman："reimplementing existing work (where the desired level of performance is known)" 比做原创反馈快得多（`pengsida_pdfs/John_Schulman.txt:271-275`）。对你而言"已知答案"就是论文十条例子和 Fig. 1(b) 的 6。
- Schulman 同段：复现给的理解比"passively reading"深（`:272-273`）。这就是为什么第 1 站要求把十条例子按两种顺序**手跑** Algorithm 1，而不是读懂就过。
- 周志华："读不懂的先跳过去，多读几遍"（`Zhihua_Zhou.txt:124`）。用在停靠点 11：Algorithm 3 的递归看不懂就写 UNKNOWN，别停在那儿。

## 2. 小例子（对应 §1.2 微例子、停靠点 1–2）

- Freeman："the simplest toy model that captures the main idea… you can figure out what will work by thinking it through with your toy model"（`Bill_Freeman.txt:38-40, 51-52`）。EX-00 六条 trace、论文十条 trace 就是这个 toy；第 7 站的合成日志也是从它长出来的。
- 李武军讲本科生科研：先让学生"读懂论文的…实现过程，有些算法需要进行数学推导"（`Wujun_Li.txt:409, 531-538`），再"实现几个前沿的方法"（`:645`）。第 1 站读、第 5a 站裸写，就是这个顺序。（这份 txt 是双栏 PDF 抽取、两栏行交错，行号只能定位到附近几行，引文以原 PDF 为准。）

## 3. 每句话要能指到出处（对应 §5 四个标签、停靠点 12）

- Supervisor-Skills 行为准则第 3 条：AI 生成的内容"学生必须逐条核查其准确性"；第 2 条：核心结论"必须由学生/导师完成并完全理解"（`handbook/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md:24, 23`）。这就是 `AGENT-SUMMARY` 标签存在的理由：agent 给的页码地图是线索，判定以 PDF 为准（README §4 开头那句）。
- 同一文件第 4 条：不得编造引用（`:25`）。对你的 G0 note 意味着：页码写不出来的句子不能打 `PAPER-TEXT`。

历史结论段已移入 `_sealed`，G0 后按题面授权打开。
