# QUESTIONS — FoldA(BPM 2025)+ Siddiqui(PETRI NETS 2025):偏序 alignment via 网展开

**日期**:2026-08-13
**论文**:FoldA(arXiv:2506.08627,BPM 2025 / LNCS 16044)+ Siddiqui/van der Aalst/Schuster(arXiv:2504.00550,PETRI NETS 2025 / LNCS 15714)
**类型**:算法论文(形式定义 + 算法 + 最优性定理 + 实验;Siddiqui 另有工具集成)
**关联**:T2 检查层(§4-3)的直接技术底座;"算法拟复用而非重造"

> 读前五问按任务要求聚焦三件事:**它解决 alignment 的什么痛点 / 复杂度从哪里来、搬到哪里去 / 偏序与全序 alignment 的差异到底是什么**。以下问答在通读全文后回填。

---

## Q1:它解决了 alignment 的什么痛点?(两个痛点,不是一个)

**痛点 1——状态空间爆炸(性能)**。经典最优 alignment(Adriansyah 2014)在"模型 × 轨迹"同步积网的**可达图**上跑 Dijkstra/A\*。可达图采用交织(interleaving)语义:\(k\) 个并发事件的一段行为要展开成最多 \(k!\) 条交织路径、\(2^k\) 个中间 marking,模型并发/选择度一高就炸。unfolding 把搜索空间换成**分支过程**(branching process):并发保持为并发关系 \(\|\)、选择保持为冲突关系 \(\#\),不枚举交织。

**痛点 2——全序 alignment 的语义失真(质量)**。经典 alignment 输出是 move 的**序列**,即使事件之间本无依赖也强加全序;更要命的是:代价函数只对 move 多重集敏感、对顺序不敏感,**等代价的最优全序 alignment 可以诱导出不同的依赖结构**。Lu et al. 2014 的经典偏序法(Classic PA)先用 A\* 任选一条最优全序、再回放展开成偏序 alignment——选到"错"的那条,产出的偏序 alignment 就带虚假依赖偏差(FoldA Fig 1 反例:\(\gamma_1,\gamma_2\) 等代价,\(\gamma_2\) 会把"轨迹中 A、B 并发 vs 模型中 A→B 顺序"报成依赖违例,而 \(\gamma_1\) 无此偏差)。FoldA 是第一篇把这个问题**显式陈述**并绕过它的:直接在配置(=偏序 run)空间按代价序搜索,第一个到达终态的配置就是**偏序意义下的最优**。

Siddiqui 的动机表述略有不同侧重:真实日志时间戳**重叠/粗粒度/缺失**导致强行全序化本身就是造假,p-trace 是更诚实的输入;此外 Classic PA 是"两步走"(先全序对齐再人工偏序化),unfolding 是"一步走"。

## Q2:方法流程是什么?(两文骨架同构)

```
输入:过程模型 N_m(1-safe、easy sound 的系统网)+ 轨迹
  ├─ FoldA 主文:全序 trace σ(附录给偏序版);Siddiqui:偏序 p-trace ρ_c(DAG)
第 1 步:轨迹 → trace net / event net(无选择的出现网;偏序 DAG 的边→依赖 place)
第 2 步:构造同步积网 SPN = trace net × model net
  转移三分:log move (a,≫) / model move (≫,t) / 同步 move (a,t)(标签相等才配对)
  [Siddiqui] 再加目标变迁 t* 消费终态 marking、目标 place p*(1-safe 保持)
第 3 步:代价导向的有向展开(directed unfolding)
  代价:同步 0,log/model 1(常数正),silent 0.0001(可忽略正值)
  充分序:FoldA 用 Z([e],ζ)(+ 启发式 h)排序,Python id() 破平;
          Siddiqui 用 ◁_c(代价 < → 配置大小 < → 入队字典序)或 ◁_h(f=s+est)
  cut-off:Mark 重复且已有更小配置 → 截断该支
  终止:第一个 Mark([x]) = 终态 marking 的配置弹出 → 即最优
第 4 步:读出结果
  FoldA:最优配置 = 最优偏序 alignment δ(出现网形态)
  Siddiqui:alignment run → alignment order(去掉 t*,move 为节点、条件为依赖)
           → 分解为 u-alignment(p-trace 侧 ⊎ 模型 run 侧 + 对齐函数 φ)
           → 偏差四象限:missing/undesired × events/dependencies(基于传递归约)
```

## Q3:复杂度是什么账?(从哪儿省、在哪儿付)

- **理论**:两文都**没有**给闭式复杂度。可靠锚点:① 可达性问题相对前缀大小 NP-complete(Esparza & Schröter,Siddiqui §1 引);② 完整前缀大小不超过可达图且常远小于(McMillan/ERV 经典结论);③ 展开的组合瓶颈在 **possible extensions 计算**(找一组两两并发的条件使某转移可扩展)——Siddiqui 明说这是"实现的关键部分",沿用 Römer 博士论文的数据结构优化。
- **经验**(FoldA 实验 1/2):合成模型上 #visited states 随同步积规模近线性,但**时间随 visited states 呈多项式/指数**(分支过程越大,每次扩展检查条件组合越贵);嵌套选择(EN 型)最伤,并发(C/CN 型)在启发式下反而处理得好;偏差越靠轨迹末尾、无启发式版本回溯越多。真实日志上:**A\* 时间赢 71–99%,但 unfolding 排队状态少(Dijkstra 最多多排 118,318%)**;FoldA 有极端长尾(SP 均值 0.204s、最大 93s;BPIC17/ITL prCm6 大量 100s 超时)。回归:ln(ET) ≈ 2.891·#SPT + 0.715·choice factor − 0.161·concurrency factor(adj R²=0.770)——**选择度是害,并发度反而略益**,这是"搜索空间换掉交织"的直接证据。
- **Siddiqui 实验**:并发 70% 时 \(ERV[\triangleleft_h]\) 全面胜出且对噪声鲁棒;30% 时与 Classic PA 打平;BPIC12 上低偏差代价段 Classic PA 快、高偏差段 \(ERV[\triangleleft_h]\) 稳,\(ERV[\triangleleft_c]\)(无启发式)频繁超时。
- **给 T2 的账**:LLM-MAS 轨迹 = 每 agent 内全序链 + 跨 agent 消息边 → **天然高并发宽度**,正落在 unfolding 的优势区;但代价是长尾风险 → 离线审计可容忍(设 timeout + A\* 回退)。

## Q4:偏序 alignment 与全序 alignment 的差异,形式上差在哪一个字?

差在**序的类型**,但后果链很长:

- **定义层**:全序 alignment \(\gamma\in((A\cup\{\gg\})\times(T\cup\{\gg\}))^*\) 是 move **序列**;偏序 alignment \(\delta\) 是同一组合法性条件(投影得轨迹 / 投影是模型 occurrence sequence / 无 \((\gg,\gg)\))下 move 上的**偏序**(FoldA Def 4)。Siddiqui 进一步给了带结构的版本:u-alignment \((\rho_c, G_\mathcal{N}, \varphi)\)——日志偏序、模型 run 偏序、同步 move 的单射对齐函数,合并同步节点后必须仍是严格偏序(禁止对齐制造因果环)。
- **代价层**:\(\kappa(\gamma)=\sum_{(e,t)\in\gamma}\kappa(e,t)\) 只依赖多重集 ⇒ 一个偏序 alignment 的所有线性化等代价 ⇒ **代价最优性对依赖结构是盲的**——这是全序方法"选哪条都算对、但偏序化后质量不同"的形式根源(详细推导见 04 §4)。
- **诊断层**:偏序 alignment 能表达全序 alignment 原则上表达不了的第三类偏差——**依赖偏差**(模型要求 A→B 顺序而轨迹中 A‖B,或反之),即 Siddiqui 的 missing/undesired dependencies。这恰是 T2 三类偏差中"序/并发违例"的现成载体。
- **搜索层**:可达图节点 = marking(交织后),分支过程节点 = 条件/事件(并发保持);配置 ↔ 偏序 run 一一对应,"最短路"从路径空间挪到配置空间。

## Q5:读前最值得质疑的三个假设(读后判断)

1. **"排队状态少 = 优势"的叙事是否成立?** 部分成立。排队状态少意味着内存压力小、也为增量/并行计算留了口(FoldA 结论自认),但时间上 A\* 仍普遍占优,且 FoldA 的长尾超时说明 possible-extensions 计算的常数因子会在复杂模型上失控。**结论:选型必须按并发度分流,不能全盘换 unfolding**(T2 混合调度依据)。
2. **p-trace 的构造假设可信吗?** Siddiqui Def 1 用时间戳:\(a\prec b\) 当且仅当 end(a) < start(b)。业务日志尚可,**LLM-MAS 轨迹不可**——异步 agent 的时钟不可比、LLM 调用时间重叠不代表语义并发。T2 必须换成 correlation_id/消息因果(happens-before)构造,这正是 T2 方法 §4-2"未观测因果关系不得补猜"的落点(改造点详见 04 §5.3)。
3. **同步 move 的"标签相等"匹配在 LLM 语义下还能用吗?** 两文都要求 \(\lambda_1(t_1)=\lambda_2(t_2)\)(FoldA 记 \(a=t\))才生成同步转移。业务活动标签规范;LLM agent 的活动名(工具名+参数、自由文本步骤)噪声大,匹配失败会把本应同步的 move 劣化成 log+model 双罚,**系统性高估偏差**。T2 需要活动规范化/映射层(R3 已预防:偏差定义在活动/交互层),且这层的误差不在两文任何保证覆盖内——保证边界要如实声明。
4. (追加)**FoldA 的 id() tie-break 可复算吗?** 不可——Python `id()` 是内存地址,跨运行不稳定。等代价最优解不唯一时,两次运行可能返回不同 alignment。对论文无伤(最优性不受影响),**对 T2 "最小可复算偏差证据"是硬伤**,必须换确定性规范序(Siddiqui 的 ◁_c 第三键用入队序,确定性取决于扩展枚举序——同样要固定)。见 04 §5.4。

---

## 品味判断(一句话)

这对论文是"老理论(McMillan 1992/ERV 1996/Bonet 2008 的展开与充分序)× 成熟问题(alignment)"的严丝合缝组装,创新浓度不在任何单个组件而在**组装的正确性论证**;正因为组件全是三十年打磨过的现成件,T2 把它当"拟复用内核"是对的——**风险不在算法,在输入语义(agent 偏序怎么来、标签怎么归一)与证据工程(确定性、可复算)**,那正是 T2 自己的贡献空间。
