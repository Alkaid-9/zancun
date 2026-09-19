# EdgeIM Mastery Gate 改写：错模型中断交接

- 日期：2026-09-05 晚
- 状态：`INTERRUPTED / NEEDS-REDO-WITH-CORRECT-MODEL`
- 工作区：`/mnt/d/MyResearch/MAS_Safety_Project`

## 一句话状态

用户要求"围绕一份新贴的框架文件，重写 EdgeIM 学习计划和进组准备"；本窗口已经照做并写了盘，但**用户随后指出这轮回复用错了模型**，选择新开窗口用正确模型（Fable 5，max effort）重做。旧产出不算废弃，但**不能当作"已用正确模型审过的定稿"**。

## 源头文件（权威输入，新窗口先读这个）

`D:\Alkaid\Desktop\更改EdgeIM学习计划和进组计划！！！.md`（WSL 路径 `/mnt/d/Alkaid/Desktop/更改EdgeIM学习计划和进组计划！！！.md`）

这是用户通过 `/goal` 指令贴入的完整框架原文（因超 4000 字符限制，`/goal` 本身截断了，但文件全文完整）。核心内容：

- **EdgeIM Mastery Gate 六道门**：整篇重建 / 算法手推 / 形式对象掌握 / claim-evidence 审计 / attack mode（能把论文弄坏）/ interview compression（30秒·2分钟·10分钟·30分钟追问四档）
- **学习节奏改革**：不再"一个点学完才回整篇"，改成纵向线程（当前节点深挖）+ 横向线程（每学完立刻接回整篇论文模型）双线程推进
- **新原则**："实践 scope 可以窄；认知 scope 不能窄"
- **OWNED 判定七问**（防"熟悉感冒充掌握"）：不提示能定义/换例子能算/改条件能预测/给反例能诊断/能比较替代设计/隔三天还能讲/能接回整篇论文位置
- **不打算照搬旧游标**：旧文件"当前已掌握/下一站"是过期快照，这次要做 **EdgeIM Whole-Paper Diagnostic**（整篇论文不同层级随机抽 15 道题现状重测），根据真实掉包位置重新长知识树，不是机械重做 EX-00
- **新目标定义**：不是"学完 EdgeIM"，而是"以 EdgeIM 为中心建立小而真实的 process-discovery research neighborhood"，含 sigRank / Ground Truth / CrossEdgeIM 三篇横向纵向配合，最终完成 1-2 个自己走过的比较/反例/实验闭环
- **进组面试新最低线**：EdgeIM 全文可重建 + 核心算法可手推 + 最小实现可重建 + claim 可审计 + assumption 可攻击 + 一个小研究问题跑完闭环 + 脱稿承受连续追问

配套的两份既有权威文档（本轮已读，未改动，仍然有效，新窗口可直接复用）：

- `/mnt/d/Edge下载/研究操作符与横向迁移案例册.md`（v1.0 · 2026-09-05）——具体论文/可借操作符/迁移边界
- `/mnt/d/Edge下载/科研学习与训练体系-v0.1.md`（标题内文实为 v0.3）——七图、操作符库、能力观察、导师视角框架

## 本窗口已产出、但需要新窗口用正确模型重新审的文件

`progress/decisions/2026-09-05__research__edgeim-mastery-gate-and-learning-restructure.md`

内容是本窗口（用错模型的情况下）写的一份完整 EdgeIM 学习计划重构文档，结构包含：六道门细化、双线程学习节奏、五个学习分枝（Sampling & Selection / Representation & Loss / Model Discovery & Petri Net / Evaluation & Evidence / 思想谱系与后继）、进组面试模拟题库、现状重测 15 题、OWNED 判定标准、四周冲刺计划。

**这份文件的处置方式待用户在新窗口拍板**，可能的走向：
1. 新窗口读一遍，模型正确的情况下逐段核对内容是否符合用户原意，有问题就地改
2. 整份推翻重写
3. 部分保留（比如题库、六道门细化可能没问题，只是"语气/风格/展开方式"要重做）

不确定哪种，因为用户只说"用错模型了，重写"+"新开一个会话窗口"，没有具体展开是内容问题还是纯粹模型问题（用户在 AskUserQuestion 里选的是"回答用的模型不对"，不是"内容风格不对"——所以本文件的实质内容判断本身可能没问题，只是需要用正确模型走一遍确认/重做）。

## 模型问题的技术线索（供新窗口参考，不代表已解决）

会话内先后两次 `/model` 切换：

1. 切到 `Opus 5`，回执："Set model to Opus 5 and saved as your default for new sessions"
2. 切到 `Fable 5`（max effort），回执："Set model to Fable 5 and saved as your default for new sessions with max effort"

两次回执都是"saved as default **for new sessions**"——这个措辞暗示可能只影响以后新开的会话，不一定让当前会话热切换。本窗口系统提示词显示实际运行模型是 `Opus 4.6`，与用户预期的 Fable 5 不符。**这正是用户要求"新开一个会话窗口"的原因**——新窗口大概率会正确加载 Fable 5 max effort 作为默认模型。

新窗口开启后，建议第一步就是确认当前实际生效模型（看系统提示词里的模型自述，或 `/model` 查询），确认对了再继续，避免重复踩坑。

## 不受影响、仍然有效的部分

- 用户更早贴的"张力结构分析"格式确认、07_EDGEIM.md §8 核实、EdgeIM Task3/4 复审链状态核查——这些是另一条独立线索（"EdgeIM 学习包增量升级"`TASK-20260904-004`，见另一份交接 `progress/handoff/2026-09-05__edgeim-learning-package-additive-upgrade__pause-handoff.md`），与本次"Mastery Gate 重写"是两件不同的事，互不覆盖。那条线仍然是 `PAUSED / RECOVERABLE / NO-EXECUTION-AUTHORITY`，仍需用户明确说"继续"才能恢复 Task 3/4/5/6 任何动作。
- 三份用户刚发的原始文件（Desktop 的改写框架 + Edge 下载的两份体系文档）路径确认有效，内容已在本次话总结之上。

## 新窗口第一动作建议

1. 确认当前会话实际生效模型
2. 重读 `D:\Alkaid\Desktop\更改EdgeIM学习计划和进组计划！！！.md` 全文（本交接已摘要，但新窗口应该自己重读原文，不要只信这份摘要）
3. 问用户：`progress/decisions/2026-09-05__research__edgeim-mastery-gate-and-learning-restructure.md` 这份已有产出是整份重写，还是挑着改
4. 不要默认触碰 EdgeIM 学习包增量升级那条独立的暂停任务（`TASK-20260904-004`），除非用户明确提

## 反向引用

- 无独立 INDEX 路由（本文件产出仓促，未来得及按标准流程登记 `progress/handoff/INDEX.md`；新窗口若有空可以补一行，不阻塞恢复）
