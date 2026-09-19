# EX-00 · 一张表就是一个事件日志

**时间盒**：2–3 小时，一晚
**规则**：纸和笔。做完再开 `_sealed/EX-00_answer.md`。卡死超过 20 分钟可以问我，我只判对错、追问、给反例，不给答案。
**PASS 条件**（冻结，见 BRIEF §2 第 0 站）：空白纸脱稿写出 Algorithm 1 的输入 / 状态 / 保留判据 / 终止 / 输出；说清为什么它没有 K；两种顺序下的保留集合不同且能解释为什么。

---

## 第一部分 · 三个词（读，15 分钟）

过程挖掘的原材料叫**事件日志**。它就是一张表，每行一个**事件**，至少三列：

| CaseID | Activity | Timestamp |
|---|---|---|
| c1 | 提交申请 | 09:00 |
| c1 | 审核 | 09:30 |
| c2 | 提交申请 | 09:05 |
| c1 | 放款 | 10:00 |
| c2 | 拒绝 | 09:40 |

- **Case**：一次完整的业务实例。上表有两个 case：c1 和 c2。一笔贷款申请、一个病人的一次就诊、一个订单，都是 case。
- **Activity**：干了什么。上表出现了四种：提交申请、审核、放款、拒绝。所有出现过的 activity 组成**字母表**。
- **Trace**：把同一个 case 的事件按时间排好，只留 activity 名，得到一个序列。
  c1 的 trace 是 ⟨提交申请, 审核, 放款⟩，c2 的是 ⟨提交申请, 拒绝⟩。

以后我们用单字母代替 activity，一条 trace 写成 `A B D F` 这样。**日志 = 一组 trace。**

## 第二部分 · 三个集合（读 + 一个微例子，20 分钟）

EdgeIM 只看每条 trace 的三样东西：

- **S**（start）：这条 trace 的第一个 activity。
- **E**（end）：最后一个 activity。
- **R**（relation，直接跟随）：所有"紧挨着的前后对"。trace `A B D` 的 R 是 {A→B, B→D}。

对一条 trace 算出来的叫 `(Si, Ei, Ri)`；对整份日志把所有 trace 的并起来叫 `(S, E, R)`。

**微例子**（跟下面的练习不是同一份日志）：

日志：`X Y Z`、`X Z`

- trace 1：S₁={X}，E₁={Z}，R₁={X→Y, Y→Z}
- trace 2：S₂={X}，E₂={Z}，R₂={X→Z}
- 全局：S={X}，E={Z}，R={X→Y, Y→Z, X→Z}

注意 R 是**集合**：`A B A B` 里 A→B 出现两次，但 R 里只有一个 A→B。这一点先记住，第 1 站要用。

## 第三部分 · 练习日志（算，40 分钟）

字母表 {A, B, C, D, E, F}。六条 trace：

```
case1: A B D F
case2: A C D F
case3: A B D E D F
case4: A B D F
case5: A C D E D F
case6: A B C D F
```


- trace 1：S₁={A}，E₁={F}，R₁={A→B,B→D,D→F}
- trace 2：S2={A}，E2={F}，R2={A→C,C→D,D→F}
- trace 3：S3={A}，E3={F}，R3={A→B,B→D,D→E,E→D,D→F}
- trace 4：S4={A}，E4={F}，R4={A→B,B→D,D→F}
- trace 5：S5={A}，E5={F}，R5={A→C,C→D,D→E,E→D,D→F}
- trace 6：S6={A}，E6={F}，R6={A→B,B→C,C→D,D→F}

全局trace：S={A}，E={F}，R={A→B,A→C,C→D,B→D,D→E,E→D,D→F}
————少了个B→C



**任务 1**：对每条 trace 写出 `(Si, Ei, Ri)`。六行。
**任务 2**：写出全局 `(S, E, R)`。R 里应该有几条？

## 第四部分 · Algorithm 1（读 + 跑两遍，60 分钟）

这是论文 Algorithm 1 的内容（`EDGEIM.txt:269-277`，我转述，你第 1 站会自己去核原文）：

```
输入：日志 L
1. 把 L 的 case 按 ⟨CaseID, Timestamp⟩ 字典序排好，得到有序的 case 列表
2. 初始化 S ← ∅，E ← ∅，R ← ∅
3. 按顺序取每一个 case：
     算出它的 (Si, Ei, Ri)
     如果  Si ⊆ S  且  Ei ⊆ E  且  Ri ⊆ R   →  这个 case 被过滤（丢掉）
     否则                                     →  保留它，并且 S ← S ∪ Si，E ← E ∪ Ei，R ← R ∪ Ri
4. 所有 case 看完，结束
输出：保留下来的 case 组成的日志 D′
```

用人话说：一个 case 只有在**带来了以前没见过的**起点、终点或直接跟随对时，才留下来。

**任务 3**：按 case1 → case6 的顺序手跑。每一步写三样：这个 case 带来了什么新东西（或"无"）；留还是滤；跑完后的 (S, E, R)。最后写出保留了哪几个 case。


- trace 1：S₁={A}，E₁={F}，R₁={A→B,B→D,D→F}——留
- trace 2：R2={A→C,C→D}——留，且留下这些
- trace 3：R3={D→E,E→D}——留这些
- trace 4——过滤
- trace 5——过滤
- trace 6：R6={B→C}——留

- trace 6：S6={A}，E6={F}，R6={A→B,B→C,C→D,D→F}
- trace 5：R5={A→C,D→E,E→D}——留
- trace 4：R4={B→D}——留
- trace 3——过滤
- trace 2——过滤
- trace 1——过滤

1.保留的case数不一样，是同几条。
2.顺序原因？遍历？——没太看懂“是算法的哪一行造成的？”——具体的那个操作吗？
3.没看懂qwq
4.case1是顺序全量保留了，逆序直接完全过滤；case4是顺序过滤，逆序留下R4中的一个。顺序原因？因为R已经有了？

```
任务 3、4 两遍都跑对了。正序留 {1,2,3,6}，逆序留 {6,5,4}，每步带来的新东西也全对。

任务 5 逐条说：

第 1 问你写"保留的 case 数不一样，��同几条"——前半句对，后半句我没看懂：4 条和 3 条，怎么会是同几条？把两个集合并排放着看一遍，哪几个 case 两边都有？哪几个只在一边？重答。

第 2 问我问得太抽象，换个问法。伪码一共四步。第 3 步的判据是"Si ⊆ S 且 Ei ⊆ E 且 Ri ⊆ R"——这一步本身跟顺序有关系吗？没有，它只看当前 case 和当前的 (S,E,R)。那顺序是从哪一步进来的？你回去看四步，指出是第几步。
顺带做一个检查，这个检查比问题本身重要：**两遍跑完，最终的全局 (S, E, R) 一样吗？**把两遍最后的 R 各写出来比一下。

第 3 问我再说人话：这个算法从头到尾，有没有哪一步让你告诉它"我要留 3 条"或"我要留一半"？如果没有——那假设我硬要它只留 2 条，我得在四步之外加什么东西？加了之后，它还是论文里那个 Algorithm 1 吗？

第 4 问你答对了，而且"因为 R 已经有了"就是原因。再往前推一步：case1 和 case4 是一模一样的两条 trace，它们的命运却完全由什么决定？用一句话说出来。这句话就是第五部分脱稿要写的"保留哪些 case 由什么决定"。

把 1、2、3 重答，4 补那一句，然后直接进第五部分：合上所有东西，空白纸写五样。

❯ 08-13 已经拆对了——当时还没有强调这几个科研知识仓，特别是那个香港的博导的

  Thinking for 55s, running 1 shell command…
  ⎿  $ cd /mnt/d/MyResearch && grep -rl -i -E '香港|hong kong|HKUST|HKU|CUHK|PolyU|CityU|博导' --include='*.md' learning/ /home/alkaid/.claude/skills/ /mnt/d/aris_repo 2>/dev/null | grep -v _archive | head -15; echo "--- MAS learning/methodology heads:"; head -5 MAS_Safety_Project/learning/methodology/RESEA…

❯ 1. 两遍保留的 case 数量一样吗？保留的是同几条吗？
  2. 如果不一样，是算法的哪一行造成的？
  3. 这个算法里有没有一个地方让你"指定要保留多少条"？如果我想让它只留 2 条，我该改哪一行？改了以后它还是原来那个算法吗？
  4. 假设 case4 跟 case1 一模一样（它确实一样），它在两种顺序下的命运分别是什么？为什么？

  这是你写的问题啊（）
```

重答-2：
1，case数量不一样。最终的SER是一样的——我原本是想说这个。不是同几条case。顺序的是1236，逆序的是654
2，它不看顺序啊，它是判断条件，是人工规定的读取顺序和列表本身的排列影响？
3.没有哪一步说"我要留 3 条"或"我要留一半"。——加什么？（）加了就不是论文的Alg.1了吧



**任务 4**：把顺序反过来，case6 → case1，再跑一遍。同样记每一步。

**任务 5**：回答——
1. 两遍保留的 case 数量一样吗？保留的是同几条吗？
2. 如果不一样，是算法的哪一行造成的？
3. 这个算法里有没有一个地方让你"指定要保留多少条"？如果我想让它只留 2 条，我该改哪一行？改了以后它还是原来那个算法吗？
4. 假设 case4 跟 case1 一模一样（它确实一样），它在两种顺序下的命运分别是什么？为什么？

## 第五部分 · 脱稿（20 分钟，这一步决定 PASS）

合上前面所有内容，换一张空白纸，写：

- Algorithm 1 的输入是什么、扫描过程中维护的状态是什么、一个 case 被保留的判据是什么、什么时候结束、输出是什么
- 一句话：为什么这个算法没有 K
- 一句话：保留哪些 case 由什么决定

写完发我。我按 PASS 条件判，追问 1–2 层。通过 → `LEDGER.md` 记一行，`MISTAKE_LOG.md` #1 你亲手改成 CLOSED。不通过 → 记暴露的具体缺口，明天再来，PASS 条件不变。

（手写到一半发现不对，手写没法发你）
input是 case act timestamp组成的列表，即trace组成的表，日志L、
维护的状态是  Si ⊆ S  且  Ei ⊆ E  且  Ri ⊆ R
初始化之后遍历的每一个case， S ← S ∪ Si，E ← E ∪ Ei，R ← R ∪ Ri
结束是所有的trace扫描完
输出是这个日志的(S,E,R)
- 一句话：为什么这个算法没有 K——没看懂qwq，没提到K，也不太需要别的参数，不依赖
- 一句话：保留哪些 case 由什么决定——trace是都含有当前集合里没有的S、E、R中的任意一项

————————————————————————————
sol接力批作业

---------

我先主窗口批这份作业；后台只做三个本地知识库的只读取证，严格不写 G0 答案、不改训练包、不碰 Bridge 卡。三个子 Agent 与主窗口合计正好四并发。

• Started `/root/supervisor_methods`

• Started `/root/pengsida_methods`

• Started `/root/reuse_and_refs`

• Updated Plan
  └ 先响应用户当前的学习验收，同时让三个只读 Agent 核对本地科研方法知识库；附件要求的 cold audit 保持为后续正式阶段，审计报告前不改代码。
    ✔ 读取附件并重新确认 Frozen OS、v1.1 与训练包边界
    □ 批改 EX-00 当前答案并给出最小重答项
    □ 汇总三个本地知识库及工作台参考仓的只读证据，形成第 1 站读法提案
    □ 完成 edgeim_sampling_audit 第一阶段独立冷审计报告（只读）
    □ 审计完成后再决定最小修复或重写、测试与 clean rerun/revalidation

• Updated Plan
  └ EX-00 当前答案已逐项核对；下一步等待用户按最小模板重答。三个只读 Agent 正在并行核验 Supervisor-Skills、Pengsida/learning_research、research_growth 与三项工作台参考。
    ✔ 读取附件并重新确认 Frozen OS、v1.1 与训练包边界
    ✔ 批改 EX-00 当前答案并给出最小重答项
    □ 汇总三个本地知识库及工作台参考仓的只读证据，形成第 1 站读法提案
    □ 完成 edgeim_sampling_audit 第一阶段独立冷审计报告（只读）
    □ 审计完成后再决定最小修复或重写、测试与 clean rerun/revalidation

• Explored
  └ Search Hard Evidence Ledger|AI.*不能替我长|artifact and claim verdicts|scoped receipts|parallel in MEMORY.md

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

• 对，刚才是我把两个层次混在一起了：

  - case0 是我临时加的热身题；
  - Claude 的正式 EX-00 从 case1 到 case6 开始。

  以后以 /mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/EX-00/README.md 为唯一题面，不再平行加题。Claude 的题面现在是完整的；密封答案已生成，但先不要打开。

  你的作业批改如下。

  ### Task 5

  1. 基本正确。
  - 逆序：保留 6,5,4，共 3 条；
  - 两遍最后得到的全局 S,E,R 相同。

  2. 部分正确。

  不是“算法不看顺序”。更准确是：

  > 第 1 行确定遍历顺序；之后每条 trace 都要和当时已经累积的 S,E,R 比较，并且只在保留时更新它们。因此前面保留了谁，会改变后面 trace 的判定。

  3. 前半正确，后半还需要补清楚。

  算法没有指定保留 2 条、3 条或一半。若强行加入 K=2，可以加一个“保留两条后停止”的规则，或做一个外部截断；但这会改变终止条件，并可能不再覆盖全部特征，所以不再是原来的 Algorithm 1。

  只需补一句：case4 和 case1 完全相同，在正序和逆序中分别谁先遇到、谁被保留。

  ### 脱稿部分

  - 输入：基本对。可以写成“由带 CaseID、Activity、Timestamp 的事件组成的日志 L，按 case 组织成 trace”。
  - 维护状态：需要改。Si ⊆ S 等是判定条件，不是状态。状态应包括：
      - 当前已保留日志 D′
      - 累积的全局 S、E、R

  - 更新：不是每条 trace 都更新，只有“被保留”时才做并集更新。
  - 结束：正确，所有 trace 扫描完。
  - 输出：不能只写 (S,E,R)；按当前练习题面，至少要写保留下来的日志 D′。
  - “为什么没有 K”：还没答。提示：算法没有“目标保留数量”，而是扫描到结束；最终保留多少条由输入特征、重复程度和遍历顺序决定。
  - 保留规则：概念基本正确，改成“当前扫描的 trace 至少带来一个尚未出现在累积 S、E 或 R 中的特征”更准确。

  目前结论：EX-00 NOT PASS YET，但核心路径已经抓到了；不记入 Ledger，Mistake Log #1 仍保持 OPEN。

  请只补下面这几项：

  Task 5-2（修正版）：
  顺序影响结果，是因为……

  Task 5-3（修正版）：
  如果硬要只保留 2 条，我会加入……
  这会失去/改变……

  Task 5-4：
  case4 在正序……
  case4 在逆序……

  脱稿修正版：
  维护的状态是……
  更新只在……时发生
  输出是……
  这个算法没有 K，因为……

  三个后台 Agent 已启动，和主窗口合计 4 个并发；它们只读核对 Supervisor-Skills、Pengsida/learning_research、research_growth 以及三个工作台参考仓。它们返回后我会逐条复核路径和行号，不直接
  采信 Agent 的结论。

─ Worked for 3m 04s ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

■ exceeded retry limit, last status: 429 Too Many Requests

• 三个后台 Agent 都因服务端 429 失败，没有产生任何可采信报告。我不把“已派发”当成果；现在用较轻的路由重发三个互不写盘的只读任务，同时主窗口继续核对事实。并发仍控制在 4 个以内。

• Started `/root/supervisor_methods_retry`

• Started `/root/pengsida_methods_retry`

• Started `/root/reuse_refs_retry`


› 4是回答过了。这里也429？那就在降低一个并发


• 已按你的纠正处理：第 4 题我不再重复索要；你在隔壁已经答过，我会把那份作答作为待核对输入，而不是把“聊天里没贴出来”误判成未答。并发已降到主窗口 + 1 个子 Agent；不再继续开并发。现在主窗口
  开始独立冷审计，先核对契约实际位置（原路径已被移入 _withdrawn/）和代码链。

（后续由sol继续，因为持续）




 那接下来的学习资料呢？


• 接下来的材料目前还没有被“偷偷补写”：盘上只有 EX-00，没有 EX-01 及以后。按冻结大纲，下一站确实是“DFG 与边频次 + 带问题读 EdgeIM Stage 1”；我先把三套知识库的可迁移读法核对完，再把它们压
  进第 1 站题面，避免把通用方法和论文答案混在一起。你说第 4 题已在隔壁回答过，我会纳入核对，不再让你重复。

• Interacted with `/root/cold_audit_single`

• Context compacted

• SessionStart hook (completed)
  hook context: CONTEXT_RECOVERY_STATUS=UNVERIFIED
    PLATFORM=codex
    … +4 lines (ctrl + t to view transcript)

• 我先把恢复边界重新钉回文件：重读学习 OS、已冻结的训练大纲、以及当前 EX-00 题面；同时保留一个只读冷审计子窗口，当前总并发 2，不再加人。然后我会把“下一份该学什么、从哪几份资料学、每一步
  交什么”列成可直接开始的清单。

• Updated Plan
  └ 已重新打开附件、Frozen OS、pause handoff、v1.1 与训练包；EX-00 批改和三类知识库的只读核验已有事实依据。当前不写新教材，先按冻结顺序收尾 EX-00，再提供第 1 站。
    ✔ 读取附件并重新确认 Frozen OS、v1.1 与训练包边界
    ✔ 批改 EX-00 当前答案并给出最小重答项
    ✔ 核对三个本地知识库及工作台参考，形成第 1 站读法提案
    ✔ 完成 edgeim_sampling_audit 第一阶段独立冷审计（只读）
    □ 在 EX-00 PASS 且 G0/T0 明确后，决定是否创建 EX-01；不提前改代码或研究规格

• 我把这件事按“有边界的教材设计”处理：先给你一份可立即使用的第 1 站题面和来源映射，不先写盘；因为现有 EX-00 已把题面、作答和 Claude 对话混在一起，直接续写会继续污染教材。你确认结构后，我
  再单独落一个干净的 EX-01。

• 有。先把事实说清：

  目前盘上只有 [BRIEF.md](</mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/BRIEF.md)、EX-00、MISTAKE_LOG.md 和密封答案；还没有 EX-01。而 [EX-00/README.md](</mnt/d/
  MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/EX-00/README.md:133) 后半已经混入作答和对话，所以不能直接把它当干净教材继续追加。我暂时没有改它，也没有写新文件。

  第 4 题已算回答，不再要求重做。现在 EX-00 只剩这些最小缺口：

  Task 5-2：
  顺序影响结果，是因为……

  Task 5-3：
  如果硬要只保留 2 条，我会加入……
  维护的状态是……
  更新只在……时发生
  输出是……
  你的 Task 5-1 也已接受：正序 {1,2,3,6}，逆序 {6,5,4}，最终 S/E/R 相同，但保留的 case 集合不同。

  下一份学习材料应是第 1 站，而不是 PM4Py 或 pilot.py。

  ## EX-01：DFG 与过滤前后频次

  时间盒 2–3 小时。你需要做四件事：

  1. 用 EX-00 的六条 trace 画原始日志 D 的 DFG。每条相邻活动对画一条边，并记录出现次数。
  2. 用 Algorithm 1 的正序结果得到 D′，再画一次 DFG、重新数边频次。
  3. 做一张比较表：

     edge | count in D | count in D′ | edge still exists? | what changed?

  4. 阅读原始 PDF 的 Stage 1 和 Algorithm 1，写自己的 G0 paper note。每条陈述标：
      - PAPER-TEXT
      - USER-INFERENCE
      - AGENT-SUMMARY
      - UNKNOWN

  必须回答的五问：

  - Algorithm 1 的输入、状态、保留判据、终止条件、输出是什么？
  - 有没有预算参数？保留量由什么决定？
  - 过滤后 DFG 的边频次是在 D′ 上重算，还是从原始日志带过来？
  - Stage 1 的全局 R 与 Stage 2 的局部 Ri 是什么关系？
  - 哪些是原文，哪些是你的推断，哪些目前仍不知道？

  原文入口是：

  /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/EdgeIM-2025-ICWS.pdf

  EDGEIM.txt 只能用来定位段落，不能替代 PDF 作为判定依据。

  ## 三个知识库怎样进入这一步

  - external/Supervisor-Skills：先冻结少数可回答问题，再逐条做证据和不确定性标注。
  - external/learning_research：一篇论文深读 → 自己重实现 → 记录失败和不会的地方。
  - research_growth：用三层读法（技术细节、问题与动机、文献位置与局限），并保留自己的预测、假设和批评。

  所以第 1 站的资料包不是“再看几篇方法论文章”，而是：

  > 一篇原始论文 + 一张自己画的 DFG + 一份带来源标签的 paper note。

  LearnGraph 本地存在，但它属于后续工作台设计参考；Reviva 和 ebbingflow 当前不在本地，暂不把它们伪装成现成学习资料。后台冷审计也已只读结束：代码内部可以重放，但它测的是 fixed-K
  surrogate，不是论文 Algorithm 1，因此代码按冻结顺序留到第 5 站。

  你现在先补上面四个空白；通过后我再按这个结构单独写一个干净的 EX-01。


› 仿照前面Fable做的这个样子的去做吧？不假设我会。

    - Algorithm 1 的输入、状态、保留判据、终止条件、输出是什么？——这里前面写过了
    - 有没有预算参数？保留量由什么决定？——没有参数，保留量特征集合由日志L本身决定
    - 过滤后 DFG 的边频次是在 D′ 上重算，还是从原始日志带过来？——这里还没看
    - Stage 1 的全局 R 与 Stage 2 的局部 Ri 是什么关系？——Algo1的吗？


• 可以，我改成“从零开始、逐问拆开、每一步先解释再让你答”的方式。先纠正一个小点：算法没有 K 这件事你已经抓到了，但“保留量由特征集合决定”还要补上“扫描顺序和重复情况也会影响保留多少条”；我
  先核对论文里 Stage 1/Stage 2 的原文，再带你做第四问，不直接假装你已经懂。


  • 可以。我们先把“这几个字到底指什么”拆开，不假设你已经会。

  你现在的回答大体方向对，但有两个地方要修正：

  - “没有 K”：对。更完整是：算法不预先规定保留几条；保留数量由日志里的新特征、扫描顺序、重复程度共同决定。最终的全局特征并集可以一样，但保留的 case 数和身份可以不一样。
  - Si ⊆ S、Ei ⊆ E、Ri ⊆ R 不是状态，而是判定条件。状态是会随着扫描改变的东西：当前已保留日志 D′，以及当前累积的 S、E、R。

  最重要的是，你问的最后一题不只是 Algorithm 1。它是在问三个阶段怎样接起来：

  原始日志 L
     │
     ├─ Algorithm 1：过滤
     │    输出 D′ + 全局 S/E/R
     │
     ├─ Algorithm 2：边缘节点上的局部特征构造
     │    输出各节点的 Si/Ei/Ri
     │
     └─ Algorithm 3：中心节点合并
          输出最终 DFG / Petri net

  这里有一个很容易混淆的下标：

  - 在我们 EX-00 里，R₁ 是“第 1 条 trace 的关系集合”。
  - 在论文 Stage 2 里，Rᵢ 是“第 i 个 edge node 的关系记录”，而且是带次数的。

  可以先用这个比喻：

  - Algorithm 1 的全局 R：一张“有没有这条边”的清单。
    例如：有没有 A→B？有 / 没有。

  - Algorithm 2 的局部 Rᵢ：每个节点自己的计数表。
    例如：A→B 出现了 7 次。

  所以它们不是同一个东西：

  > Stage 1 的全局 R 主要用于判断一个 case 是否带来了新的关系；Stage 2 的局部 Rᵢ 则从过滤后的日志中统计关系出现次数；Stage 3 再把各节点的计数合并成 DFG。

  你现在要核对的地方在原始 PDF 的 printed page 407：

  - Section IV-B：Algorithm 1 的输出是 D′, S, E, R
  - Section IV-C：Algorithm 2 的输入写的是 Filtered D′
  - Algorithm 2 会逐条事件把局部关系计数加一
  - Section IV-D：Algorithm 3 把各个 Rᵢ 的计数加到中心 DFG

  这给了第 3 问一个很强的线索：它看起来不是把原始日志的边频次直接搬下来，而是基于 D′ 再构造局部计数。但你要在 /mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/EdgeIM-2025-ICWS.pdf
  上自己确认并记页码；我不替你把 G0 paper note 写完。

  现在只做这三行，不用重写整份笔记：

  A. Algorithm 1 的输出是……
  B. Algorithm 2 的输入和它处理的日志是……
  C. Algorithm 2 的 Ri 与 Algorithm 1 的全局 R，区别是……

  把这三行发来，我再用一个很小的例子带你算“过滤前后边频次”到底发生了什么。pilot.py 先不碰，按冻结顺序它还没到。