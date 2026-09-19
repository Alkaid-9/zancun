# 08b：Segment-Based MHP 论文——知识图谱提取与批判性分析（B3）

**对象论文**：Faming Lu, Xiaoyu Wang, Qingtian Zeng, Guiyuan Yuan, Yunxia Bao. "Segment-Based May-Happen-in-Parallel Analysis for C Programs". *Concurrency and Computation: Practice and Experience* 37(21-22): e70203, 2025. DOI 10.1002/cpe.70203。收稿 2024-11-24，修回 2025-05-31，录用 2025-07-05 [PDF p.1]。

**输入与页码说明**：主输入为 pdftotext 全文 + 对 p.5/7/9/10 的 -layout 重取。PDF 实际为 11 页（页脚 "1 of 11" 至 "11 of 11"，pdfinfo 确认 Pages: 11；任务说明中的"10 页"与实物不符）。本文引用页码一律指论文印刷页码（与 PDF 页序一致）。

**符号还原说明（诚实声明）**：论文用花体字母命名 6 个段属性集合，文本提取时花体符号全部丢失。本文依 p.5 的文字定义用纯文本别名指代：F=线程fork集、J=线程join集、FL=fork-lock集、LF=lock-fork集、L=过程内锁集、IL=过程间锁集 [PDF p.5]。Table 2 各列公式已与 p.5-6 的逐条文字规则交叉核对，列序判定为 F、J、L、FL、LF（IL 不在 Table 2 中，由算法2第24步全局追加 [PDF p.6]）。凡属推断处均已标注。

---

# 第一部分：知识图谱提取

## 1. 核心概念及其关系（10 个概念）

### C1. MHP 分析（May-Happen-in-Parallel）
判定程序中两条语句能否在运行时并行执行的静态分析，是数据竞争等并发缺陷检测的基础 [PDF p.1]。对任意两语句做既 sound 又 complete 的并发判定是 NP-complete 的（引 Taylor [6]）[PDF p.1]，因此一切实用方法都是近似。

### C2. 抽象线程与多重派生线程（multi-forked thread）
每个抽象线程对应程序中一条线程创建语句；通常对应单个运行时线程，但当创建语句在循环中等情形下对应多个运行时线程，称 multi-forked thread [PDF p.3]。Definition 1：t 是 multi-forked，若 (a) 其父线程是 multi-forked，或 (b) 存在从 fork(t) 出发又回到 fork(t) 且不经过 join(t) 的路径 P [PDF p.3]。全文脚注声明"thread"一律指抽象线程 [PDF p.10]。

### C3. TCFG（Thread-sensitive Control Flow Graph，基线模型）
Di et al. [19]（ICPP 2015）提出：在过程间控制流图 ICFG 上添加 fork/join 边，并配 Region Relation Graph（RRG）做 region 级 MHP 分析 [PDF p.2]。TCFG 以 4 个属性建模 HB（before fork、after join、fork-join、disjoint program paths）并用一个锁集捕捉冲突 [PDF p.5]。TCFG/RRG 是本文的直接前作与主对比基线。

### C4. STCFG（Segmented Thread-sensitive Control Flow Graph，本文模型）
本文核心模型：把语句按"并发相关上下文信息"一致性分组为段（segment），段为节点构成 STCFG；MHP 分析只需检查段间关系，再回推语句对关系 [PDF p.1 摘要, p.4]。相对 TCFG 的三点增强：(1) 用 F/J 捕捉 fork/join HB；(2) 用 FL/LF 建模锁与线程的耦合；(3) 把保护锁区分为过程内/过程间两类 [PDF p.5]。

### C5. 段（segment）与六种切分场景
段是 STCFG 节点，至少含一条语句；语句不改变段属性则并入当前段，否则开新段 [PDF p.4]。六种开段场景 A–F：A=进入新线程；B/C/D/E=遇到 fork/join/lock/unlock 语句；F=语句有多个前驱且不属于当前线程任何既有段 [PDF p.4]。

### C6. 段上下文属性（六个集合）
每段维护 [PDF p.5]：
1. F（线程fork集）：可能与本段并发执行的所有后代线程；
2. J（线程join集）：因 join 而不可能与本段并发的线程；
3. FL（fork-lock集）：形如 (t, l) 的线程-锁对，记录线程创建后自行获取的锁；
4. LF（lock-fork集）：形如 (l, t) 的锁-fork 耦合对，记录某线程持锁 l 期间创建了线程 t；
5. L（过程内锁集）：实际保护本段的过程内锁；
6. IL（过程间锁集）：保护本段的过程间锁，记作 l_t（l 为锁，下标 t 为创建该锁保护关系的线程）。
初始化规则（Table 2，与 p.5-6 文字规则核对）[PDF p.5-6]：entry(t) 时全部置空集；fork(t)：F(seg') = F(seg) ∪ {t} ∪ D(t)（D(t)=t 的后代线程集），LF(seg') = (L(seg) × {t}) ∪ LF(seg)；join(t)：F(seg') = F(seg) − {t} − JN(t)（JN(t)=t 必须 join 的线程集），J(seg') = J(seg) ∪ {t} ∪ JN(t)，LF(seg') = LF(seg) − (L(seg) × {t})；lock(l)：L(seg') = L(seg) ∪ {l}，FL(seg') = FL(seg) ∪ {(t, l)}；unlock(l)：L(seg') = L(seg) − {l}，LF(seg') = LF(seg) − ({l} × F(seg))；多前驱场景仅继承不修改 [PDF p.5-6]。

### C7. Happens-Before（HB）关系（四种来源）
Definition 2：若 seg 与 seg' 之间有确定的先后次序则为 HB [PDF p.7]。四种记法：同线程控制流导致的 seg < seg'；fork 导致的 seg <fork seg'；join 导致的 seg <join seg'；lock 与 fork 耦合导致的 seg <lock-fork seg' [PDF p.7]。判定规则（Figure 5 之 3–6）[PDF p.7]：
- 规则3（控制流）：两段同线程且该线程非 multi-forked ⇒ 控制流 HB；
- 规则4（join）：seg 所属线程 t_seg ∈ J(seg') 且 t_seg' 非 multi-forked ⇒ seg <join seg'；
- 规则5（fork）：t_seg' 不在 F(seg) 也不在 J(seg)，但属于 t_seg 的后代，且 t_seg 非 multi-forked ⇒ seg <fork seg'（集合归属处花体符号有损，此处按上下文语义复原，属有依据推断）；
- 规则6（lock-fork 耦合）：存在 (l, t_seg') ∈ LF(seg) 且 (t_seg', l) ∈ FL(seg') ⇒ seg <lock-fork seg'。

### C8. 冲突关系（intra / inter）
seg 与 seg' 因过程内锁不能并发记 seg #intra seg'；因过程间锁不能并发记 seg #inter seg' [PDF p.7]。判定规则（Figure 5 之 1–2）[PDF p.7]：
- 规则1：两段过程内锁集 L 交集非空 ⇒ #intra；
- 规则2：(a) 两段过程间锁集 IL 交集非空，且交集中存在锁 il 使 t_il 不是两段所属线程的公共祖先 ⇒ #inter；或 (b) 一段的 IL 与另一段的 L 交集非空，且前者所属线程不是后者所属线程的祖先 ⇒ #inter（p.8 实例"L(seg8) 与 IL(seg10) 交集非空且 t_seg10 非 t_seg8 祖先 ⇒ seg8 #inter seg10"印证此读法 [PDF p.8]）。
**MHP 判定总则**：seg 与 seg' 既无任何 HB 又无任何冲突 ⇒ 并发，记 seg || seg' [PDF p.7]。

### C9. 锁-fork 耦合（lock-fork coupling，本文最核心的新观察）
现有 MHP 分析在 HB 阶段只看 fork/join 引起的次序，忽略"父线程持锁 l 期间创建子线程 t；t 启动后若申请 l 必须等父线程释放"这一耦合造成的额外 HB [PDF p.2]。运行示例：t_m 持锁 l 时启动 t2，故 s_gvar1、s_gvar2 必先于 s_gvar5 执行，尽管二者之间没有 fork/join HB 也没有共同锁保护 [PDF p.2-3]。机制上由 LF（父侧持锁创建）与 FL（子侧启动后取锁）配对触发规则6 [PDF p.5, p.7]。

### C10. 过程内锁 / 过程间锁二分
过程内锁是线程实际持有的锁，可影响任何其他线程；过程间锁不是线程实际获取的锁，而是祖先线程"代持"以保护后代线程不受其他线程干扰，它不影响祖先线程自身及祖先的其他后代 [PDF p.5]。生成条件：fork(t) 发生在父线程 t_p 的过程内锁 l 保护之下、且 l 一直持有到对应 join(t) ⇒ t 受过程间锁 l_tp 保护，l_tp 加入 t 及其所有后代线程的全部段 [PDF p.7]。混淆两类锁会同时造成误报与漏报：既有方法把 t2 内全部语句都当作受 l 保护，错判 s_gvar2 与 s_gvar6 冲突（漏报真实并发对）[PDF p.3]。

### 概念间关系清单（三元组）
- Pthreads 原语（pthread_create/join/mutex_lock/unlock，论文记 fork/join/lock/unlock [PDF p.2]）——触发——段切分场景 B–E [PDF p.4]
- 语句 ——按上下文一致性归组—— 段；段 ——作为节点构成—— STCFG [PDF p.4]
- STCFG ——扩展自—— TCFG（[19] 引入 TCFG；本文在其上加"Segmented"）[PDF p.2-3]
- Table 2 初始化规则 + 算法1（Δ 差量沿 worklist 传播）+ 算法2（构图与三步全局传播）——产生/维护—— 段属性 [PDF p.5-6]
- 算法2 第22-24步 ——全局传播——：fork(t) 段的 J、FL 下发到 t 及 D(t) 全部段；join(t) 段的 LF 下发到 t 及 D(t) 全部段；IL 追加到所有相关段 [PDF p.6-7]
- 段属性 ——经 Figure 5 六规则判定—— HB 关系 / 冲突关系 [PDF p.7]
- LF × FL 配对 ——产生—— <lock-fork HB（规则6）[PDF p.7]
- IL ——产生—— #inter 冲突（规则2，带祖先豁免条件）[PDF p.7]
- 无 HB 且无冲突 ——推出—— seg || seg' ——回推—— 段内任意语句对 MHP [PDF p.1, p.4, p.7]
- multi-forked 线程 ——豁免/削弱—— HB 规则3/4/5（规则均要求相关线程非 multi-forked；multi-forked 线程内部语句无 HB，甚至可与自身并发，如 s_gvar6 || s_gvar6）[PDF p.3, p.7]
- MHP 结果 ——服务于—— 数据竞争 [1-3]、死锁 [4,5] 等并发缺陷检测 [PDF p.1]

## 2. 理论框架图（文字描述）

推理管线共六层 [PDF p.1, p.4-8]：

```
(1) C 程序
      │  LLVM 16.0.0 编 IR（O1 优化）；SVF [21,22] 建中间表示；
      │  Andersen 算法 [23] 做指针分析                    [p.8]
      ▼
(2) 程序分段：按六场景 A-F 切段（线程入口 / fork / join /
      lock / unlock / 多前驱），段内语句共享统一并发属性      [p.4]
      ▼
(3) STCFG 构造（算法2）：
      3a. 按 Table 2 规则初始化各段 F/J/L/FL/LF；
          后代线程未分析完则优先分析后代（JN(t)、D(t) 依赖子线程信息）[p.5-6]
      3b. 循环/分支汇合导致重访时，算法1 计算差量
          ΔF=F(pre)−F(seg)、ΔJ=J(seg)−J(pre) 等五项，
          沿 worklist 传播到后继段；策略为"F 宁多加（防漏报），
          J/LF/FL 删冗余（降误报，集合名恢复存 LF/L 歧义，见 §逻辑审视注）"  [p.6]
      3c. 全线程分析完后三步全局传播：fork 段的 J、FL 下发子孙；
          join 段的 LF 下发子孙；过程间锁 IL 全局追加        [p.6-7]
      ▼
(4) 段间关系判定（Figure 5 六规则）：
      冲突：规则1 #intra（L∩L≠∅）；规则2 #inter（IL 相关两条）
      HB：规则3 控制流 / 规则4 join / 规则5 fork /
           规则6 lock-fork 耦合（LF 与 FL 配对）             [p.7]
      ▼
(5) MHP 判定：无任何 HB 且无任何冲突 ⇒ seg || seg'          [p.7]
      ▼
(6) 语句对 MHP：语句对关系 = 其所在段对的关系
      （"只需检查段能否并发即可推断语句"）                    [p.1, p.4]
```

效率关键设计：上下文在构图期一次性传播完毕，查询期不再做可达性搜索 [PDF p.8]。正确性关键假设：六属性集合完整保真了语句级分析所需的并发信息（论文以 p.5 的 TCFG-vs-STCFG 对照段落作论证，无形式化证明，见第二部分）。

## 3. 关键数据表逐值解读

### 表A：Table 3 "Data races found by TCT, RRG, and STCFG"（精度主表）[PDF p.10]
记法：每格 X/Y = 该方法报出的 MHP 对数 / 其中真阳性数 [PDF p.8]；"True data race"列为真实数据竞争数 [PDF p.10]。

| 程序 | 说明 | 真值 | TCT | RRG | STCFG | 逐值解读 |
|---|---|---|---|---|---|---|
| DRB001 | 简单数据竞争 | 2 | 2/2 | 2/2 | 2/2 | 三方法全对，无区分度 [p.10] |
| DRB002 | 过程内锁测试 | 0 | 0/0 | 0/0 | 0/0 | 三方法全对，无区分度 [p.10] |
| DRB003 | join 测试 | 2 | 3/2 | 2/2 | 2/2 | TCT 多 1 个误报；RRG 已完美，STCFG 打平 [p.10] |
| DRB004 | 数组越界测试 | 0 | 3/0 | 2/0 | 2/0 | 三方法都误报：把整个数组当单一对象、不判元素地址是否相同 [p.8]；STCFG 与 RRG 完全相同 [p.10] |
| DRB005 | 即 Figure 2a 程序 | 4 | 7/3 | 6/3 | 4/4 | 核心展示行。TCT 报 7 中 3、RRG 报 6 中 3：各含误报且都漏 1 个真对（即被过程间锁误判为冲突的 s_gvar2–s_gvar6 对 [p.3]）；STCFG 4/4 完美。收益来源=锁-fork 耦合（消 {1,5},{2,5} 类误报 [p.3]）+ 锁二分（找回漏报）[p.10, p.3] |
| DRB006 | 过程间锁测试 | 9 | 0/0 | 0/0 | 9/9 | 最悬殊行：TCT/RRG 把过程间锁当真实保护 ⇒ 9 个真实竞争对全部漏报（漏报率 100%）；STCFG 9/9 全对。注意这是修复基线的漏报（soundness 方向），不是通常意义的"精度（降误报）" [p.10, p.3, p.5] |
| DRB007 | 间接 join 测试 | 5 | 8/5 | 6/5 | 5/5 | TCT 3 误报、RRG 1 误报、STCFG 完美 [p.10] |
| DRB008 | 多重嵌套 join | 9 | 10/9 | 9/9 | 9/9 | TCT 1 误报；RRG 已完美，STCFG 打平 [p.10] |
| fft | 复数一维 FFT（SPLASH2） | 0 | 803/0 | 684/0 | 684/0 | 真值 0，全部报出均为误报；**STCFG=RRG（684），无任何改进**；TCT 多 119 [p.10] |
| lu_cb | 矩阵三角化（SPLASH2） | 0 | 276/0 | 169/0 | 169/0 | 同上，STCFG=RRG（169）[p.10] |
| lu_ncb | 矩阵三角化（SPLASH2） | 0 | 276/0 | 169/0 | 169/0 | 同上，与 lu_cb 数值完全一致 [p.10] |
| radix | 整数排序（SPLASH2） | 0 | 252/0 | 205/0 | 205/0 | 同上，STCFG=RRG（205）[p.10] |

**全表结构性观察**（本报告归纳，数值均出自 p.10）：
1. STCFG 严格优于 RRG 的行只有 3 个：DRB005、DRB006、DRB007——全部是作者自制用例，且名字直接对应本文两项新机制（过程间锁、join 处理）。
2. 在全部 4 个 SPLASH2 真实内核与 DRB004 上，STCFG 与 RRG 逐值相同（684/169/169/205/2），真实负载上精度增益为零。
3. 4 个 SPLASH2 程序真值全记 0，因此真实程序上只度量了误报，从未展示真阳性检出能力；论文自己解释 SPLASH2 误报全部源于不判"访问对象是否全局变量/同地址" [PDF p.8]。
4. STCFG 全表 12 行零漏报（每行报出数 ≥ 真值且真阳性 = 真值）；TCT/RRG 在 DRB005 漏 1、DRB006 漏 9。
5. 论文明确声明三方法都"不是真正的数据竞争检测方法"，只判语句能否并行、不判地址与路径条件 [PDF p.8]——但表题却叫"Data races found"，列头叫"Number of MHP pairs"，度量对象存在错位（详见第二部分）。
6. 佐证一致性：p.4 Table 1（TCFG 标记矩阵）经与 p.3 真值 {2-6, 3-4, 3-5, 6-6} 对照可复原为：正确 3 对、误报 {1,5},{2,5},{5,6} 3 对、漏报 {2,6} 1 对（颜色信息提取丢失，此为逻辑复原），即报 6 中 3——与 Table 3 中 RRG 行 DRB005=6/3 吻合 [PDF p.3, p.4, p.10]。

### 表B：效率结果（Figure 7/8 为位图不可提数，以下为正文数值）[PDF p.8]
- 范围：仅"四个测试程序"（未点名；按上下文推断为 4 个 SPLASH2 内核，属推断）；计时只含模型构建 + MHP 分析，**剔除 SVF 中间表示构建与指针分析时间** [PDF p.8]。
- 总执行时间：STCFG 平均仅为 TCT 的 21.96%；比 RRG 快 33.3% [PDF p.8]。
- 模型构建阶段：STCFG 耗时仅为 TCT 的 6.05%；相对 RRG 减少 73.29%。归因：先分段再初始化/更新/传播，降低了属性运算复杂度 [PDF p.8]。
- MHP 分析阶段：相对 TCT 提升 63.28%；相对 RRG 提升 13.47%。归因：构图期已完成上下文传播，查询期免可达搜索 [PDF p.8]。
- 硬件环境：2.1 GHz Intel i7-12700、64 GB 内存、Ubuntu Linux（内核 5.15.0）[PDF p.8]。
- 注意：Figure 7/8 图题把 TCT 误写为 "MHP"（"Execution time comparison of MHP, RRG, and STCFG"）[PDF p.10]，与正文"compares the execution time of TCT, RRG, and STCFG"[PDF p.8] 不一致；且论文未给出任何一台程序的原始秒数，仅有比率。

## 4. 引用网络（TOP5 + 谱系）

**TOP1：[19] Di, Sui, Ye, Xue. "Region-Based May-Happen-in-Parallel Analysis for C Programs", ICPP 2015** [PDF p.11]
角色：同名近题直接前作 + 主基线（RRG）+ 模型宿主。本文的 TCFG 概念即由 [19] 引入（"Di et al. introduce Thread-sensitive Control Flow Graph (TCFG)... and Region Relation Graph (RRG)" [PDF p.2]），STCFG 字面上就是"Segmented TCFG"。[19] 已经做了"region 级（而非语句级）MHP"，故"粗粒度化"这一思想不属本文首创；本文对 [19] 的批评是"一次只考虑一对线程建模 TCFG 属性、复杂交织下丢上下文；不考虑锁-fork 耦合；不分过程内/间锁" [PDF p.8]。标题从 "Region-Based...for C Programs" 到 "Segment-Based...for C Programs" 的镜像关系使本文的增量边界问题格外突出（见第二部分）。

**TOP2：[16] Barik. "Efficient Computation of MHP Information for Concurrent Java Programs", LCPC 2005（TCT）** [PDF p.11]
角色：第二基线。提出 Thread Creation Tree，把每线程映射到创建语句、细粒度处理 fork/join；但假设每线程与父/子线程并行，导致大量误报 [PDF p.2]。注意 TCT 原为 Java 设计，本文将其复现到 C/Pthreads 语境作基线 [PDF p.8]。

**TOP3：[14] Naumovich, Avrunin, Clarke. "An Efficient Algorithm for Computing MHP Information for Concurrent Java Programs", ESEC/FSE 1999（PEG）** [PDF p.11]
角色：语句级 MHP 分析谱系的奠基（Java 线）。用 Parallel Execution Graph 合并各线程 CFG；缺点是需限制同一 CFG 对应的线程数、join 处理差 [PDF p.2]。[15] Li & Verbrugge 2004 对其做实用化改进 [PDF p.2]。本文的语句级对照面即源于这一谱系。

**TOP4：[7] Agarwal, Barik, Sarkar, Shyamasundar. "MHP Analysis of X10 Programs", PPoPP 2007（与 [8][9] 构成结构化并发线）** [PDF p.10-11]
角色：反衬性引用。X10 的 async-finish 结构化并发使 MHP 分析更简单、更准 [PDF p.1]；[8] Sankar et al. CC 2016、[9] Saha & Nandivada PPoPP 2020 延续该线。本文以此论证 C 的低层并发原语与复杂调度（Figure 1 的 full/not/indirect/partial join 四型 [PDF p.2]）使结构化语言的 MHP 方法不适用 [PDF p.2]。人事上注意 Barik 横跨 [7] 与 [16] 两线。

**TOP5：[21][22] Sui & Xue（SVF）+ [23] Andersen** [PDF p.11]
角色：实现基座。算法在 LLVM 16.0.0 上用 SVF 实现，指针分析用 Andersen 算法 [PDF p.8]。谱系上值得注意：SVF 作者 Sui、Xue 同时是 TOP1 [19] 的作者——本文的主基线、宿主模型（TCFG）与工具链（SVF）全部出自同一 UNSW 研究线，本文定位是对该线的增量改进。

**次要节点**：[6] Taylor CACM 1983——NP-complete 论据，为近似方法正名 [PDF p.1]；[20] Zhou et al. CGO 2018 静态向量钟——被点名的"最新"语句级 MHP，作为"最新方法也只看 fork/join HB"论断的对象 [PDF p.2]；[18] Joisha et al. POPL 2011（PCG）——过程粒度 MHP，粗粒度化的另一先例 [PDF p.2]；[13] Bristow et al. 1979——最早的过程间优先图 [PDF p.2]；[17] Naik et al. PLDI 2006——流敏感+上下文敏感但不管 join [PDF p.2]；[1-5]——下游数据竞争/锁误用检测，构成动机层（其中 [2] D4 被在运行示例定义处引用，提示 Figure 2a 示例可能改编自 D4 论文 [PDF p.2]）；[24-26]——LLM 辅助静态分析，仅支撑未来展望段 [PDF p.10]。

---

# 第二部分：批判性分析

## 1. 方法论审视

**基线为自行复现，内部效度存疑**。原文："we reproduce the TCT and RRG methods and compare them with our method"[PDF p.8]。两点风险：(1) TCT [16] 原为 Java 设计 [PDF p.2]，移植到 C/Pthreads 必然涉及原文未规定的设计决策，复现保真度无从验证；(2) RRG [19] 出自 SVF 同一团队，原实现大概率存在，论文未说明是否联系原作者或使用原码。基线复现版本无代码公开（见第 4 节），第三方无法审计"基线被弱化"的可能性。此外 Figure 7/8 图题把基线 TCT 误标为 "MHP" [PDF p.10]，反映实验报告环节的粗糙。

**基准选择偏差显著**。12 个程序 = 8 个自制 + 4 个 SPLASH2 [PDF p.8]。三层问题：
- (a) 8 个自制用例逐一对准本文新机制命名（DRB002 过程内锁测试、DRB006 过程间锁测试、DRB007 间接 join 测试等 [PDF p.10]），属"为展示自家特性而构造"的用例集；STCFG 相对 RRG 的全部精度优势恰好只出现在其中 3 个（DRB005/006/007）[PDF p.10]。
- (b) SPLASH2 只取 4 个且论文通篇未给任何挑选理由 [PDF p.8, p.10]。按 SPLASH2 官方构成（4 kernels + 8 applications，属公开常识）推断：所选 fft、lu_cb、lu_ncb、radix 恰是全部 kernel 中除 cholesky 外的部分，8 个 application（barnes、ocean、water 等）全部回避。最可信的解释（推断，论文未言明）：方法自认"目前只支持 mutex 锁与 fork/join，不覆盖 Pthreads 其他同步语句" [PDF p.8 结论]，而 SPLASH2 应用大量使用 barrier/条件变量，无法有意义地分析；亦不排除可扩展性原因。无论哪种，都应在论文中明说——只挑 4 个而不解释，构成选择性报告。
- (c) 自制用例命名 DRB001–DRB008 与 LLNL 知名套件 DataRaceBench 的 DRBxxx 命名撞名（DataRaceBench 为 OpenMP 套件，属公开常识），论文声称八个用例"we develop ourselves" [PDF p.8]，撞名易使读者误以为用了标准基准；且运行示例（即 DRB005）定义处引用了 [2]（D4, PLDI 2018）[PDF p.2]，提示该例可能改编自他文，与"自制"表述的边界模糊。

**统计强度薄弱**。摘要自称 "Preliminary results" [PDF p.1]。全部时间数据来自单机单配置 [PDF p.8]，未报告重复次数、方差、置信区间或显著性检验（全文无相关字样）；效率图（Figure 7/8）为柱状位图，未附任何原始秒数表，读者只能拿到六个比率（21.96%、33.3%、6.05%、73.29%、63.28%、13.47%）[PDF p.8]；且计时剔除了 SVF 构建与指针分析 [PDF p.8]——作为方法间公平对比可以接受，但端到端成本被隐藏，"higher efficiency"的实际用户可感收益不明。精度侧样本量：12 个程序中真正有区分度的仅 5-6 行（DRB001/002 三方全对，SPLASH2 四行 STCFG=RRG）[PDF p.10]。

**Ground truth 方法学缺失**。"True data race" 列 [PDF p.10] 的确定方式全文未着一字：无人工标注协议、无动态工具交叉验证、无引用。对 8 个自制小程序，作者既设计缺陷又数缺陷，小程序上手工判定尚可信，但不可核验（用例未公开）。对 SPLASH2 四程序全部记真值 0 [PDF p.10] 是强断言且无出处——MHP 分析的真值本身是难题（需穷举调度），论文用"真实数据竞争数"替代"真实 MHP 对数"作真值，回避了这一难题但引入下一条问题。

**度量对象错位**。表题"Data races found"、列头"Number of MHP pairs"、真值列"True data race" [PDF p.10] 三者不是一回事；正文亲承"TCT、RRG 与本方法都不是真正的数据竞争检测方法……只判两语句能否并行，不考虑访问对象是否同地址、也不考虑路径条件" [PDF p.8]。用"竞争真值"评"MHP 报告"意味着：MHP 层面的漏报（可并行但不构成竞争的语句对被漏掉）完全不在度量范围内——一个方法可以在此指标上完美而在 MHP 意义下大量漏报。MHP 精度的正当评法应以"可并行语句对全集"为真值（哪怕抽样人工判定），论文未做。

## 2. 逻辑审视

**推理链最薄弱一步：段级关系 ⇒ 语句对 MHP 的保真性从未被证明**。摘要断言"只需检查段间关系即可推断语句间关系" [PDF p.1]，支撑仅有两处非形式论证：(1) "段内所有语句共享统一并发属性" [PDF p.4]——这对被追踪的六个集合成立（切分点恰在每条并发相关语句处），但"六集合已捕获语句级判定所需的全部信息"只是通过与 TCFG 四属性的对照段落 [PDF p.5] 口头声明；(2) "To ensure soundness while minimizing unnecessary constraints, our approach implements a selective update strategy... deliberately include more threads in F(seg) to prevent false negatives. At the same time, we remove redundant entries from J(seg), LF(seg) and FL(seg) to reduce false positives" [PDF p.6]〔G1 审计标注：原文此处集合名为花体、文本提取丢失，引文中的三集合名系本卡恢复而非原文字面；08 卡按 Algorithm 1 行结构恢复为 J/L/FL（LF 行走并集、与"删冗余"矛盾），存在 LF/L 歧义，以原 PDF 花体为准〕——从 J/LF/FL 里"删冗余"恰是最危险的操作（删多了会把并发对误判为有 HB/冲突，造成漏报），而"删的都是冗余"无任何证明。全文没有一条定理、引理或健全性论证；没有复杂度分析；算法1/2 的终止性也未论证（F 在 fork 时增、join 时减，属性集非单调，worklist 收敛不显然）[PDF p.6]。一篇静态分析论文完全依赖 12 个小程序的经验结果替代正确性论证，这是最硬伤。

**规则层面的语义粗糙点**。规则3 把"同线程（非 multi-forked）的两段"一律归为控制流 HB [PDF p.7]——互斥分支上的两段并无先后关系，只是不可能共存；作为 MHP 判定这是安全的粗化，但把它称作 Happens-Before 在语义上不严谨。Definition 1 的 multi-forked 判定依赖"存在回到 fork(t) 且不含 join(t) 的路径" [PDF p.3]，但路径在哪个图上找（是否覆盖递归创建、函数指针间接创建）未指明。规则5 的集合归属在文本提取中花体丢失，但按原文行文其条件依赖"t_seg 非 multi-forked" [PDF p.7]——multi-forked 场景下 HB 规则 3/4/5 全部失效，意味着循环创建线程的程序里段间几乎只能靠冲突关系排除并发，精度退化程度未讨论。

**过度概括**。摘要："Preliminary results show that our method provides higher precision and achieves higher efficiency" [PDF p.1]；贡献列表："The results confirm the effectiveness of our algorithm" [PDF p.2]。但逐值看 [PDF p.10]：精度优势只在 3/12 个自制用例上成立，4 个真实内核上与 RRG 逐值打平、与真实精度相关的收益为零。"higher precision" 的成立域被悄然放大到未经验证的一般 C 程序。

**替代解释成立且未被排除：精度提升与"分段"无关**。论文捆绑了三个机制：(i) 锁-fork 耦合 HB（规则6）、(ii) 过程内/间锁二分（规则2）、(iii) 分段粒度。没有任何消融实验分离三者。但 Table 3 本身可以反推归因 [PDF p.10, p.3]：DRB005/DRB007 的误报消除来自 (i)，DRB005/DRB006 的漏报修复来自 (ii)，两者都是锁语义建模的改进、与"以段代语句"无逻辑关联；分段唯一的贡献通道是效率（p.8 的归因也只在效率节使用分段 [PDF p.8]）。换言之，"segment-based" 作为标题卖点，对论文的精度故事没有贡献——精度提升完全可以在语句级 TCFG 上加上 (i)(ii) 实现。此外 (i) 与 (ii) 修复的是相反方向的错误（(i) 降误报、(ii) 补漏报/修 soundness），统称"精度更高"掩盖了这一区别。而 SPLASH2 四程序上 STCFG=RRG 说明两种锁模式在测过的真实代码中一次都没触发——锁-fork 耦合与过程间锁在真实世界的普遍性完全未被证明，这直接动摇"解决的是重要问题"的前提。

## 3. 贡献审视

**相对语句级 MHP 的增量**：粗粒度化换效率有明确先例——[18] 过程粒度（PCG）[PDF p.2]、[19] region 粒度 [PDF p.2]。"以段代语句"作为思想不新；新的是段的切分准则（六场景绑定 Pthreads 原语 [PDF p.4]）与"构图期传播上下文、查询期免可达搜索"的工程设计 [PDF p.8]。

**相对 [19]（region-based 前作）的增量**：这是全文最需要正面回答却被回避的问题。论文对 segment 与 region 的形成规则、粒度差异没有任何逐点对比（对 [19] 的全部讨论仅 p.2 一句综述 + p.8 一句归因），在标题镜像（Region-Based → Segment-Based）的背景下，模型层面的真实增量无法从论文中判断。可确认的增量只有：锁-fork 耦合 HB（规则6）与过程内/间锁二分（规则2）两项锁语义精化，以及构建/查询效率（总时间比 RRG 快 33.3% [PDF p.8]）。诚实的标题应该更接近"Lock-Aware MHP"而非"Segment-Based MHP"。

**真正的 novelty**：锁-fork 耦合（父线程持锁创建子线程 ⇒ 子线程取同锁的代码段与父线程持锁段之间存在 HB）作为纳入 MHP 的 HB 来源，就本文的文献综述而言是首次（"even the latest MHP analyses only examine... thread creation or join" [PDF p.2]；本报告未能独立穷尽验证该优先权主张）。这是一个真实、干净的语义观察，配套的 LF/FL 双集合机制设计合理 [PDF p.5, p.7]。过程内/间锁二分同样是有价值的语义区分，且修复的是基线的漏报（DRB006 从 0/0 到 9/9 [PDF p.10]），对 may-analysis 而言是 soundness 修复，价值高于普通降误报。

**对下游并发缺陷检测的启发**：MHP 是竞争检测的候选对过滤器，误报每降一分，下游别名/路径分析的负担就轻一分 [PDF p.1]。但本文止步于 MHP 对计数：不判内存地址、不判路径条件 [PDF p.8]，未接入任何真实竞争检测器做端到端对比，故"对下游有多大帮助"仍是未兑现的推论。锁-fork 耦合的建模思路对死锁检测（锁获取顺序与线程创建交织的场景）可能有借鉴价值——此为本报告的推断，论文未提。LLM 增强 MHP 的未来展望段 [PDF p.10] 无技术内容，属愿景性填充。

**适用面限制**：只支持 mutex 与 fork/join，不支持 barrier、条件变量、信号量、读写锁、trylock 等 [PDF p.8 结论自认]。对以 barrier 为主要同步手段的科学计算类 C 程序（恰是 SPLASH2 的主体），方法现状下不可用或严重失准。

## 4. 可复现性

**已提供**：LLVM 16.0.0 + SVF + Andersen、O1 优化、硬件/OS 规格 [PDF p.8]；Table 2 初始化规则 [PDF p.5]、算法1（属性更新）与算法2（STCFG 构造）伪码 [PDF p.6]、六条判定规则 [PDF p.7]。

**缺失（复现阻断点）**：
- SVF 具体版本未给（SVF 各版本 API 差异大）[PDF p.8 仅给 LLVM 版本]；
- 锁与线程对象的身份判定细节缺失：pthread_mutex_t 指针别名如何经 Andersen 结果映射为锁标识、pthread_create 经函数指针启动例程如何解析，均未说明（p.8 只有一句"employing Andersen's algorithm during pointer analysis phase"）；
- 算法2 伪码含未定义占位步骤："Process descendant threads"（第13行）、"ready for initialization"（第10行）[PDF p.6]，无法直接落码；算法1 第5行"a statement removed from W"与上下文的段 worklist 矛盾（应为 segment），需读者自行纠错 [PDF p.6]；
- 循环/递归中 fork 的图构造细节、终止性与复杂度均缺失 [PDF p.3, p.6]；
- 基线复现细节（TCT 从 Java 移植到 C 的全部决策）为零 [PDF p.8]。

**代码/数据公开声明原文抄录**："The data that support the findings of this study are available from the corresponding author upon reasonable request." [PDF p.10]。即：无公开代码仓库、无公开基准包，8 个自制用例（承载了全部精度优势）不可获得，Table 3 与 Figure 7/8 不可独立核验。

**结论**：凭论文本身不可复现；属"原则上可向通讯作者索取"级别。核心算法骨架可以重写，但与论文数值对齐所需的实现细节不足。

## 5. 总评（审稿人视角）

**判定：大修（major revision）**。按 CCPE 的实际录用标准，问题集中在评估而非思想，修订后可接收（事实上已录用刊出）；若投 PLDI/OOPSLA/ICSE 级别会议，以当前证据强度倾向拒稿。理由：有两个真实但偏窄的语义观察（锁-fork 耦合、锁二分），无正确性论证，评估在真实负载上未显示任何精度收益。

**三个最硬质疑点**：

1. **真实负载零增益 + 基准自选**：在仅有的 4 个真实程序（SPLASH2 内核）上，STCFG 的精度与 RRG 逐值完全相同（684/169/169/205 个误报，真阳性均为 0）[PDF p.10]；全部精度优势来自 8 个自制、按自家新特性命名的微用例中的 3 个 [PDF p.10]。SPLASH2 十二个程序为何只挑 4 个 kernel、回避全部 application，论文无一字解释 [PDF p.8]。请证明锁-fork 耦合与过程间锁模式在真实代码中确实存在并影响分析结果，并在非自制基准上重做精度评估。

2. **无健全性/终止性/复杂度论证**：论文断言段级关系足以推断语句对 MHP [PDF p.1]，但六属性抽象的保真性、Table 2 更新规则与算法2 第22-24步全局传播的正确性、"选择性更新策略"中对 J/LF/FL 的删除不致漏报 [PDF p.6]，全部没有定理或证明；算法收敛性与复杂度亦缺失。请给出健全性定理（相对某个并发语义）及至少是非形式的完整论证，并补三机制（耦合/锁二分/分段）的消融实验以支撑归因。

3. **真值与度量效度不成立**："True data race" 的确定方法学全文缺失 [PDF p.10]；表题"Data races found"与正文"三方法都不是数据竞争检测方法" [PDF p.8] 自相矛盾，用竞争真值度量 MHP 输出使 MHP 层面的漏报不可见；两个基线均为作者自行复现且 TCT 为跨语言移植 [PDF p.8]，无原始实现对照、无代码/用例公开 [PDF p.10]。请公开工件、说明真值协议、并用 MHP 语义的真值（而非竞争真值）重新度量。

**次级问题清单**（修订应一并处理）：Figure 7/8 图题 TCT 误作 "MHP" [PDF p.10]；p.2 "t3 is joined into t3 after complete" 笔误 [PDF p.2]；算法1 第5行 "statement/segment" 混用 [PDF p.6]；效率评估的"四个测试程序"未点名 [PDF p.8]；效率指标口径混用（"21.96% of TCT" 与 "33.3% faster than RRG"）[PDF p.8]；DRB 命名与 DataRaceBench 撞名 [PDF p.10]；原始时间数据未披露（仅比率）[PDF p.8]。

---

## 安全门自检
- **不编造**：全部数值与引文均出自 PDF 文本并标页码；花体符号丢失处（六集合名、规则5/规则2 的集合归属、Table 1 颜色）已明示为"依上下文复原/逻辑推断"；SPLASH2 构成、DataRaceBench 命名为公开常识并已标注；"为何只挑 4 个 SPLASH2"的解释明确标注为推断。
- **不过度承诺**：对锁-fork 耦合的优先权仅表述为"就本文综述而言"；对下游死锁检测的启发标注为本报告推断；未断言作者复现基线有失公允，仅指出不可审计。
- **全覆盖**：任务书两大部分共 9 个小节全部落实；概念 10 个、框架图 1 幅（文字版）、关键数据表 2 组逐值解读、引文 TOP5 + 谱系、批判 5 节含三硬质疑点。
