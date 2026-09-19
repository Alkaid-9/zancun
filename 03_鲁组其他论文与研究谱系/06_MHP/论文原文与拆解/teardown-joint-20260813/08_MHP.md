# 08 · Segment-Based MHP(STCFG)——第一性原理全拆(D2 线·MHP 基座篇)

> Lu F.(鲁法明), Wang X.(王小宇), Zeng Q.(曾庆田), Yuan G.(袁贵元), Bao Y.(包云霞). "Segment-Based May-Happen-in-Parallel Analysis for C Programs." *Concurrency and Computation: Practice and Experience*, 37(21-22): e70203, 2025. DOI: 10.1002/cpe.70203 [PDF p.1]
> 主输入:`_launch/pdftxt/MHP.txt`(-layout 提取)+ 原 PDF 第 5–7 页重取核对。原文页码按 PDF 自标 "X of 11" 计(**实际 11 页**,任务书所记"10 页"与 PDF 自标不符,以 PDF 为准)。
> 符号约定:原文六个段属性用花体字母,PDF 文本提取在字体层面全部丢失(两种提取方式均复现此丢失)。本文以 F/J/FL/LF/L/IL 命名六属性、J_must(t)/D(t) 命名两个辅助集,**指称关系由正文散文逐条交叉验证恢复**(验证过程见 §4.2),此为全文唯一系统性重构层,特此声明。

---

## 0. 身份卡

- **题录**:Segment-Based May-Happen-in-Parallel Analysis for C Programs,CCPE(Wiley,并发计算老牌期刊)37 卷 21-22 期 e70203,2025。收稿 2024-11-24,修回 2025-05-31,录用 2025-07-05 [PDF p.1]。关键词:MHP | multi-threading | Pthreads | static analysis [PDF p.1]。
- **作者线** [PDF p.1]:鲁法明(一作,山科大计算机学院)/ **王小宇(二作,同为 04 篇 SegLock 二作,鲁侧图 T1 接口人——此人横跨 Java 动态分段图与 C 静态 STCFG 两条载体线)**/ 曾庆田(山科大流程挖掘掌门,D3 线人脉)/ 袁贵元(通讯,gyuan_yuan@163.com)/ 包云霞(通讯,数学学院,baoyunxia98@163.com)。双通讯 = 袁贵元 + 包云霞。
- **基金** [PDF p.1, p.10 重复]:山东省自然基金 ZR2023MF097 / ZR2024QF107 / ZR2024ZD22;国家重大科技专项 2022ZD0119501;国家自然基金 52374221。与 04 篇 SegLock 基金池重叠(ZR2024ZD22)。
- **家族位置**:D2 线"分段思想"的**第三条实现路径**——02/04 是 Java 动态轨迹上的分段(轨迹网/分段图),03 是 C 静态源码上的分段 PN,本篇是 C 静态源码上的**分段控制流图(STCFG,LLVM/SVF 载体)**。且本篇做的是 MHP——"许多并发缺陷分析的基座"(原文第一句:"MHP analysis serves as the basis for many concurrency bugs analyses" [PDF p.1])——即家族里位置最上游的一篇:03 的 UAF、数据竞争检测、死锁静态检测都要先回答"这两条语句可能并行吗"。
- **值得记录的反常**:参考文献 [1]–[26] 中**零自引** [PDF p.10-11]——2021 锁增广分段图(中文)、02 PNULock、03 UAF、04 SegLock 一篇都没引。lock-fork 耦合这一组内祖传 insight 在本篇以"全新发现"面目出现。时间线上本篇收稿(2024-11)与 SegLock 收稿(2024-12)几乎同步,是同一批思想在 C/静态侧的平行投产。
- **MANIFEST 警示确认**:本篇与 Di, Sui, Ye, Xue. "Region-Based May-Happen-in-Parallel Analysis for C Programs"(ICPP 2015,本篇引文 [19])**是两篇不同论文**——后者是 UNSW 薛京灵组的工作,正是本篇的主对照基线 RRG。注意标题镜像结构(Region-Based ↔ Segment-Based,余下逐词相同):这是刻意的对位命名,宣示"同一问题、换切分单位"。检索与引用时勿混淆。

---

## 1. Task:形式化

### 1.1 判定问题

- **输入**:C/Pthreads 多线程程序 Prog。论文只建模五种语句语义:fork = pthread_create(),join = pthread_join(),lock = pthread_mutex_lock(),unlock = pthread_mutex_unlock(),其余全部记为普通语句 s [PDF p.2]〔页锚经 G1 审计更正:原标 p.3〕。
- **输出**:对任意语句对 (s1, s2),判定谓词 MHP(s1, s2) ∈ {true, false}。
- **语义定义(纯文本)**:MHP(s1, s2) = true 当且仅当 存在 Prog 的某次合法执行,使 s1 的某次执行实例与 s2 的某次执行实例可以并发发生(二者之间不存在强制先后序)。原文表述:"MHP analysis determines whether two statements in a program can run concurrently" [PDF p.1]。
- **复杂度地板**:对任意两条语句做 sound 且 complete 的并发性判定是 NP-complete(引 Taylor 1983 [6])[PDF p.1]。因此一切实用 MHP 分析都是**过近似**:宁可多报 MHP(假阳性),不可漏报(假阴性会让下游竞争检测漏掉真 bug)。
- **精度指标的方向性**:好的 MHP 分析 = 在保持过近似(不漏真并发对)的前提下,把"实际上有序或互斥、却被误判为并发"的对子尽量删掉。

### 1.2 抽象线程与 multi-forked 线程

- **抽象线程**:每个线程创建语句对应一个抽象线程 t;主线程记 tm [PDF p.3]。全文"thread"均指抽象线程(尾注 1 [PDF p.10])。
- **定义 1(Multi-Forked Thread)** [PDF p.3],线程 t 是 multi-forked 线程,当且仅当下列至少一条成立:
  - 条件一:t 的父线程是 multi-forked 线程;
  - 条件二:设 t 对应创建语句 fork(t),存在一条从 fork(t) 出发又回到 fork(t) 的路径 P,且 P 上不含 join(t) 语句(即 fork 在循环里且回边上没有配对 join)。
- 意义:multi-forked 抽象线程对应**多个运行时线程**,因此其内部语句之间不能声称任何 HB(两个运行实例可交错),其段可与自身并发 [PDF p.3:运行例中 t2 的 s_gvar6 与自身并发]。

### 1.3 STCFG

- **底座 TCFG**(Di et al. [19] 的概念):在过程间控制流图 ICFG 上加 fork 边与 join 边 [PDF p.2]。
- **STCFG(Segmented Thread-sensitive Control Flow Graph)**:节点不再是语句而是**段(segment)**;每段包含至少一条语句;段内所有语句**共享同一份并发上下文属性**(六个属性集,见 §4.2);段间边沿控制流/fork/join 结构 [PDF p.4]。纯文本记:STCFG = (SegSet, Edge, Prop),Prop: SegSet → (F, J, FL, LF, L, IL) 六元组。原文未给这种六元组式的正式定义,STCFG 是以"构造过程 + 属性表"方式给出的(结构化定义缺位,见 §6)。

### 1.4 段间关系(定义 2 [PDF p.7],逐条纯文本恢复)

给定两段 seg 与 seg':

- **HB 关系**:若 seg 与 seg' 之间存在确定的先后序,称二者有 HB 关系。四个来源、四个记号:
  - 同线程控制流导致:记 seg < seg';
  - fork 导致:记 seg <fork seg';
  - join 导致:记 seg <join seg';
  - **lock 与 fork 的耦合导致:记 seg <lock-fork seg'**(本篇新增的第四种 HB 来源)。
- **冲突关系(Conflict)**:因锁互斥而不可能并发:
  - 过程内锁导致:记 seg #intra seg';
  - **过程间锁导致:记 seg #inter seg'**(本篇新增的细分)。
- **并发**:记 seg || seg'。**判定为"排除式默认":若 seg 与 seg' 既无任何冲突关系也无任何 HB 关系,则判并发** [PDF p.7 末句:"If seg and seg' do not have any conflict relationship or HB relationship, they are considered to be concurrent"]。
- **语句对提升**:MHP(s1, s2) = true 当且仅当 seg(s1) || seg(s2),其中 seg(s) 为 s 所属段(摘要:"it is sufficient to examine the relationship between segments to infer the relationship between statements" [PDF p.1])。同段两语句 / 同语句自身对:归约为该段与自身的关系——同线程且非 multi-forked 则由控制流 HB 排除,multi-forked 则自并发(运行例 s_gvar6 与自身 MHP [PDF p.3])。同段自身对的显式规则原文未单列,此句后半为按规则 3 + 运行例的推断。

---

## 2. Challenge

### 2.1 语句粒度 MHP 的两个精度损失来源(本篇立论)

1. **锁与线程创建语句的耦合被忽略** [PDF p.2]:"even the latest MHP analyses only examine whether there is an HB relationship between statements caused by thread creation or join operations during HB analysis. This actually overlooks coupling information between locks and thread creation operations, leading to a missing HB relationship and reduced analysis precision."——既有 HB 分析只认 fork/join 两种排序来源,把锁当作纯互斥设施。但"父线程持锁 l 期间 fork 子线程,子线程要拿 l 就必须等父线程放锁"这一场景中,**锁产生的是跨线程的顺序,不只是互斥**。漏掉这条 HB → 把有序对误判为并发 → 假阳性。
2. **过程间锁处理不当** [PDF p.2]:"existing methods may introduce inaccuracies in MHP analysis due to incorrect handling of inter-procedural locks."——祖先线程持锁期间 fork 出的后代线程,享受的是"祖先替它持有"的保护(过程间锁),后代自己并没有拿锁。既有方法把这种继承保护当成真实持锁,推出错误的互斥冲突 → 把真并发对(如后代与祖先自身、后代与兄弟)误判为互斥 → **假阴性**(运行例:先前方法假设 t2 内所有语句都受 l 保护,把 s_gvar2 与 s_gvar6 误判冲突 [PDF p.3];实验中 DRB006 基线 9 个真竞争全漏 [PDF p.10])。

### 2.2 既有方法谱系及其挑战([PDF p.2] 相关工作段逐条)

| 方法 | 粒度/模型 | 论文指出的缺陷 |
|---|---|---|
| Bristow et al. [13](1979) | 过程间优先图 | 早期,仅表达同步先后 |
| Naumovich PEG [14](Java) | 语句级并行执行图 | 需限制同一 CFG 对应的线程数;join 处理差 |
| Li & Verbrugge [15] | PEG 改良 | 只改善扩展性 |
| Barik TCT [16] | 线程创建树 | 假设每线程与父/子线程并行 → 大量假阳性 |
| Naik et al. [17] | 流敏感+上下文敏感 | 不考虑 join 语句 |
| Joisha PCG [18] | **过程粒度** | 太粗,只算过程级 MHP |
| Di et al. TCFG+RRG [19](2015) | region 粒度 | 见下 |
| Zhou et al. [20](2018) | 静态向量钟 | 未消化 lock-fork 耦合 |
| X10 系 [7–9] | 语言结构化并发 | 靠 async-finish 结构简化,不适用于 C 的低层并发 [PDF p.1-2] |

对主基线 RRG 的定点打击 [PDF p.8]:"RRG considers only one pair of threads at a time when modeling TCFG properties, which can result in the loss of contextual information due to complex thread interleavings";TCT 则"struggles to accurately model complex fork/join dependencies";且"Neither approach considers lock-fork coupling nor distinguishes between inter-procedural and intra-procedural locking mechanisms"。

### 2.3 C 语言侧的固有难度([PDF p.1-2] Figure 1 四模式)

结构化并发语言(X10)的 MHP 简单且准;C 的 fork/join 可任意摆放,产生四类复杂模式 [PDF p.2 Figure 1]:(a) 完全 join(t2 全并回 t1);(b) 不 join(t2 寿命长于 t1);(c) **间接 join**(t1 创建 t2、t3,t3 先并入 t2,再经 t2 间接并回 t1;原文此句 "t3 is joined into t3 after complete" 疑有排版笔误,按图题 Indirect join 与上下文应为 t3 并入 t2);(d) 部分 join(某些路径 join、某些不 join)。结论:"即便有最精确的别名分析 [10–12],仍须处理交错复杂性" [PDF p.2]。

---

## 3. Insight & Novelty

### 3.1 lock-fork 耦合 HB(第四种排序来源)

- 【解决什么问题】fork/join-only 的 HB 分析漏掉"持锁育儿"场景产生的跨线程顺序,把 s_gvar1/s_gvar2 与 s_gvar5 这类实际有序的对子报成并发(假阳性)[PDF p.3]。
- 【受哪个 insight 启发】**锁在特定句法位形下是排序设施**:若父线程在持有 l 的区间内 fork 了 t,而 t 启动后要获取 l,则 t 的获锁点之后的一切都必须排在父线程释放 l 之后——这条顺序既不是 fork 边也不是 join 边,是"lock × fork"的乘积效应。此即组内 2021 分段图/02 PNULock/03 UAF(lock/fork 耦合因果)/04 SegLock(lock-start 耦合)的同一祖传洞见,本篇首次装进 MHP 基座(家族联系为外部知识,论文内零自引,见 §0)。
- 【设计了什么,具体】两个互为镜像的属性集 + 一条判定规则 + 两条传播规则:LF 集记 (l, t) = "本段执行时所属线程持着 l,且 t 是在持 l 期间 fork 出的"[PDF p.5];FL 集记 (t, l) = "线程 t 在自己被创建之后获取过 l"[PDF p.5];规则 6:(l, t_seg') ∈ LF(seg) 且 (t_seg', l) ∈ FL(seg') ⟹ seg <lock-fork seg' [PDF p.7];Algorithm 2 第 22/23 行把 FL/LF 沿 fork/join 语义向后代线程整体传播 [PDF p.6-7]。

### 3.2 过程内/过程间锁二分(把"谁真的持锁"写进类型)

- 【解决什么问题】把祖先替后代持有的保护当成后代自己持锁,推出假冲突,漏报真竞争——DRB006 上两条基线 0/0(9 个真竞争全漏),本方法 9/9 [PDF p.10]。
- 【受哪个 insight 启发】**锁的保护效力取决于持有者身份**:过程内锁(intra)是线程实际获取的,排斥任何其他线程;过程间锁(inter)是祖先替后代拿的,只保护后代不受"第三方"干扰,**不隔离后代与祖先自身、也不隔离同一保护伞下的后代之间** [PDF p.5:"intra-procedural locks are the locks actually acquired by threads and can affect any other thread. In contrast, inter-procedural locks ... are locks assigned by the ancestor thread to ensure that descendant threads are protected from interference by other threads. However, inter-procedural locks do not affect the ancestor thread or other descendant threads of the ancestor"]。
- 【设计了什么,具体】L 集(intra)与 IL 集(inter)分开记;IL 元素带创建者标签 l_t(锁 l + 创建它的线程 t)[PDF p.5];生成条件:fork(t) 发生在父线程 tp 的 intra 锁 l 保护下、且 l 一直持到对应 join(t),则 l_tp 加入 t 及其全部后代线程的所有段(Algorithm 2 第 24 行)[PDF p.7];冲突判定规则 1/2 里给 inter 锁装了**祖先例外条款**(见 §4.6),运行例由此救回 seg4 || seg10 的真并发("preventing potential false negatives that might arise from confusing intra-procedural and inter-procedural locks" [PDF p.8])。

### 3.3 段 = 并发上下文等价类(粒度 trade-off 的本质)

- 【解决什么问题】逐语句做 HB/冲突判定,同一并发上下文被重复计算千百次;过程粒度(PCG)又粗到不可用。
- 【受哪个 insight 启发】**并发属性只在同步点变化**:两个相邻同步语句之间的所有普通语句,其"能与谁并发、被什么锁护着"完全相同——它们是并发语义下的等价类。因此按属性变化点切段,**相对属性系统是无损压缩**(商映射):段粒度 vs 语句粒度的 trade-off 并不发生在"分组"这一步——分组不丢属性系统内的任何信息——而是**全部前移到属性抽象本身**(六个集合装不下的信息,比如获锁次序、执行轮次,才是真正丢掉的东西;对照 04 篇 SegLock 用弧标签把轮次留下来了)。原文的操作性表述:"if a statement does not affect the properties of the segment, it is added to the current segment. However, if a statement has the potential to alter the properties of the current segment, a new segment must be created" [PDF p.4]。
- 【设计了什么,具体】六种开段场景 A–F(见 §4.1)+ 六属性集(§4.2)+ Table 2 逐场景初始化规则(§4.3)+ 不动点更新算法(§4.4)。判定时"only need to check whether segments can run concurrently" [PDF p.2]。
- 【与同名对手的差分】RRG 的 region 同样是分组,但按论文批评,RRG 建 TCFG 属性时一次只考虑一对线程,复杂交错下上下文信息丢失 [PDF p.8];STCFG 的段属性是全线程视角一次算全。

### 3.4 建图期传播、查询期免搜索(效率来源)

- 【解决什么问题】TCT/RRG 在查询期做可达性搜索,MHP 查询多时慢 [PDF p.8]。
- 【受哪个 insight 启发】HB/冲突判定所需的全部上游事实(哪些线程已 fork 未 join、谁持什么锁、谁被谁的锁罩着)都可以**在构图时预付**,折进段属性;查询退化为常数次集合运算,不再碰图。
- 【设计了什么,具体】Algorithm 2 的三步收尾传播(第 22/23/24 行)把跨线程语义摊平到每个段;Figure 5 六条判定规则全部是"查两个段的属性集"级别的操作 [PDF p.7]。效率归因原文自述:构造阶段提速因"first segmenting the program ... reduces the complexity of property initialization, updating, and context propagation";分析阶段提速因"context propagation performed during the construction phase, eliminating the need for reachability search during analysis" [PDF p.8]。

---

## 4. 方法全恢复

### 4.0 流水线总览

源码 → LLVM 16.0.0 IR(O1 优化)→ SVF 中间表示 + Andersen 指针分析 [PDF p.8] → 程序切段(§4.1)→ 逐线程初始化段属性(§4.3,后代优先)→ 环/汇合处不动点更新(§4.4)→ 三步全局传播 + inter 锁标注(§4.5)→ 得到带满属性的 STCFG → 对目标语句对查其所属段,套六条规则(§4.6)→ 无 HB 且无冲突 ⟹ MHP。

### 4.1 切段:六种开段场景 A–F([PDF p.4] Figure 4)

新段在且仅在以下场景创建(段以触发语句开头;不触发属性变化的语句并入当前段):

- **A**:进入新线程(线程入口);
- **B**:遇到 fork 语句;
- **C**:遇到 join 语句;
- **D**:遇到 lock 语句;
- **E**:遇到 unlock 语句;
- **F**:语句 s 有多个前驱语句、且 s 不属于当前线程任何既有段(分支汇合点)。

循环去重:因循环/分支汇合,一条语句可能被再次分析;若它已属于某段,不再开新段 [PDF p.4-5,Figure 3b 中 fork(t2) 有两个前驱语句但第二次分析不再开段的例子]。

Figure 3b 的切分实录 [PDF p.5]:seg1/seg6/seg9 = 三个线程入口(tm/t1/t2);seg2/seg7 = lock 触发;seg3/seg4 = fork(t1)/fork(t2) 触发;seg5 = join(t2) 触发;seg8 = unlock 触发。

对照:与 04 篇 SegLock 的差分点之一在这里——SegLock 把**锁释放**当分段点是其自我标榜的细化(动态轨迹上),本篇静态侧 lock 与 unlock **都是**分段点(D、E 两场景),分段密度更高。

### 4.2 段属性:六个集合([PDF p.5] §3.1.2 逐条)

每段维护(符号为本文重构命名,指称关系恢复依据附后):

1. **F(seg)——Thread fork set**:"records all descendant threads that may execute concurrently"——此刻可能与本段并发执行的后代线程集;
2. **J(seg)——Thread join set**:"records threads that cannot be concurrent due to join"——因 join 已确定不可能与本段并发的线程集;
3. **FL(seg)——Fork-lock set**:元素 (t, l),"recording locks acquired by a thread after its creation"——线程 t 被创建之后获取过锁 l;
4. **LF(seg)——Lock-fork set**:元素 (l, t),"captures the lock-fork coupling where a thread holds a lock l while creating another thread t"——持 l 期间 fork 了 t;
5. **L(seg)——Intra-procedural lock set**:实际保护本段的过程内锁;
6. **IL(seg)——Inter-procedural lock set**:保护本段的过程间锁,元素 l_t(l = 锁,下标 t = 创建该保护的线程)。

辅助集(用于初始化,[PDF p.5] §3.1.3):**J_must(t)** = 必须被 t join 的线程集("the set of threads that must be joined by thread t");**D(t)** = 以 t 为祖先的线程集("the set of threads whose ancestor is t")。因二者依赖子线程信息,构造时**后代线程优先分析** [PDF p.5-6]。

指称恢复依据(花体符号在提取中丢失,以下为交叉验证锚点):Figure 3b 中 seg4 的属性实录 [PDF p.5] ——F = {t1, t2}(可与 t1/t2 的段并发)、LF = {(l, t1), (l, t2)}(t1、t2 在祖先 tm 持 l 期间被创建)、FL = {(tm, l)}(tm 在执行本段前获取了 l)、L = {l}(本段受过程内锁 l 保护);seg9 的 IL = {l_tm}(受 tm 创建的过程间锁保护)。六个集合的用途分别与规则 5(F)、规则 4(J)、规则 6(FL/LF)、规则 1(L)、规则 2(IL)一一咬合,无歧义。

**与 TCFG 属性系的对照** [PDF p.5]:TCFG 用四属性(before fork / after join / fork-join / disjoint program paths)建 HB + 一个 lock set 建冲突;STCFG 的增强 =(1)F/J 承接 fork/join HB;(2)**FL/LF 新增锁-线程耦合建模**;(3)**保护锁分成 intra/inter 两类**。

### 4.3 初始化规则(Table 2 [PDF p.5] 逐格恢复,5 列 × 6 行)

记 seg' = 被初始化段,seg = 其前驱段。除线程入口外,seg' 先整体复制 seg 的属性再按触发语句修正 [PDF p.5]:

| 触发语句 | F(seg') | J(seg') | L(seg') | FL(seg') | LF(seg') |
|---|---|---|---|---|---|
| entry(t) | ∅ | ∅ | ∅ | ∅ | ∅ |
| fork(t) | F(seg) ∪ {t} ∪ D(t) | J(seg) | L(seg) | FL(seg) | (L(seg) × {t}) ∪ LF(seg) |
| join(t) | F(seg) − {t} − J_must(t) | J(seg) ∪ {t} ∪ J_must(t) | L(seg) | FL(seg) | LF(seg) − (L(seg) × {t}) |
| lock(l) | F(seg) | J(seg) | L(seg) ∪ {l} | FL(seg) ∪ {(t_cur, l)} | LF(seg) |
| unlock(l) | F(seg) | J(seg) | L(seg) − {l} | FL(seg) | LF(seg) − ({l} × F(seg)) |
| multi-pre | F(seg) | J(seg) | L(seg) | FL(seg) | LF(seg) |

逐行讲解(散文依据 [PDF p.5-6]):

- **fork(t)**:t 上线,t 及其未来后代 D(t) 都可能与本段之后的代码并发 → 入 F;当前持有的每把锁 l ∈ L(seg) 与新线程 t 构成耦合对 (l, t) → 入 LF("add ordered pairs from L(seg) × {t} to LF(seg')")。
- **join(t)**:t 及"必须被 t join 的"J_must(t) 全部结束 → 出 F、入 J("Threads joined by t can no longer execute concurrently with the current segment");t 死了,一切 (l, t) 耦合失效 → 从 LF 删 L × {t}(× 左操作数的花体下标已丢失,按与 unlock 行的对称性恢复为 L(seg);语义上 t 结束应使所有 (·, t) 对失效,残留对只会声称与"已结束线程"的 HB,方向错但不影响 MHP 判定的非并发结论——此为推断)。
- **lock(l)**:l 入 L;同时记录"当前线程 t_cur 在创建后拿过 l"→ (t_cur, l) 入 FL。**FL 终身不删**(unlock 行不动 FL):它是获锁史,不是持锁态——规则 6 需要的正是"t 迟早要拿 l"这个历史事实。
- **unlock(l)**:l 出 L;释放 l 使"持 l 育儿"的全部耦合失效 → 从 LF 删 {l} × F(seg)。
- **multi-pre(分支汇合)**:纯复制,不修正 [PDF p.6:"No additional initialization is required beyond inheriting from the predecessor segment"]。

### 4.4 汇合与循环:不动点更新(Algorithm 1 [PDF p.6] 逐行恢复)

循环/分支汇合使一条语句可能已属于既有段 seg,而新到达的前驱段 'seg 会改变 seg 的属性。先算五个差量:

- dF = F('seg) − F(seg)
- dJ = J(seg) − J('seg)
- dL = L(seg) − L('seg)
- dFL = FL(seg) − FL('seg)
- dLF = LF('seg) − LF(seg)

再以工作表传播(Algorithm 1 伪码,行号对原文):

```
输入:'seg 与 seg
1: W ← 段工作表
2: 计算差量 d*(如上)
3: W ∪ {seg}
4: while W ≠ ∅:
5:   seg ⇐ 从 W 取出一段
6:   F(seg)  ⇐ F(seg)  ∪ dF     // 并集方向
7:   J(seg)  ⇐ J(seg)  − dJ     // 差集方向
8:   L(seg)  ⇐ L(seg)  − dL     // 差集方向
9:   FL(seg) ⇐ FL(seg) − dFL    // 差集方向
10:  LF(seg) ⇐ LF(seg) ∪ dLF    // 并集方向
11:  if seg 任一属性变化:
12:    for seg' ∈ succ(seg):
13:      if seg' 已初始化 then W ∪ {seg'}
```

方向语义(原文自述的"选择性更新策略" [PDF p.6]):"To ensure soundness while minimizing unnecessary constraints ... we deliberately include more threads in F(seg) to prevent false negatives. At the same time, we remove redundant entries from J(seg), L(seg) and FL(seg) to reduce false positives."——即 **F 走 may 方向(路径并集:任一路径可能并发就算并发),J/L/FL 走 must 方向(路径交集:仅全路径成立的排序/持锁/获锁史才保留)**。这是 MHP 过近似的教科书配方:并发证据取并、非并发证据取交。**但 LF 走的是并集方向(第 10 行 ∪)**,且原文补充"adding threads to F(seg) may introduce new thread-lock pairs in LF(seg), which are handled by updating dLF correspondingly"——LF 与 F 联动、同为 may 方向。LF 是规则 6 推 HB(= 非并发证据)的原料,may 方向的原料喂 must 性质的结论,存在健全性缺口,详见 §6.2。

### 4.5 构造总算法与三步全局传播(Algorithm 2 [PDF p.6] 逐行恢复)

```
1:  切段(§4.1)
2:  t ← 抽象线程
3:  初始化 seg_entry(入口段,全空集)
4:  W ← 段工作表;5: W ∪ {seg_entry}
6:  while W ≠ ∅:
7:    seg ⇐ 取出一段
8:    for seg' ∈ succ(seg):
9:      if seg' 未初始化:
10:       if 就绪(所依赖的后代线程已分析完) then 初始化 seg'(§4.3 规则)
12:       else 先处理后代线程            // fork/join 段依赖 J_must/D,后代优先
15:       W ∪ {seg'}
16:     else 更新 seg' 属性(Algorithm 1)
21: 全线程分析完毕后:
22:   对每个因 fork(t) 创建的段 seg:把 J(seg) 与 FL(seg) 加入 t 及 D(t) 中每个线程的所有段
23:   对每个因 join(t) 创建的段 seg:把 LF(seg) 加入 t 及 D(t) 中每个线程的所有段
24:   把过程间锁 IL 加到所有相关段
```

三步传播的语义论证(散文 [PDF p.6-7] 逐条):

- **第 22 行(fork 向下播 J 与 FL)**:t 被创建时,"threads joined by any ancestor of t cannot execute concurrently with t"(祖先已 join 掉的线程与 t 天然有序 → J 下传);"if an ancestor of t is blocked due to lock acquisition and cannot execute concurrently with other threads, then t must not be able to execute concurrently with those threads"(祖先因获锁被排到某些线程之后,其后代 t 也被连带排序 → FL 下传)。
- **第 23 行(join 向下播 LF)**:若 join(t) 所在段与某些段有 lock-fork 耦合(join 发生在持锁区间内),则"等待 t 结束"这一事实使 **t 的全部语句**也被同一耦合排序 → 把 join 段的 LF 灌进 t 及其后代的所有段。实例 [PDF p.7]:Figure 3b 中 t2 在 seg5 被 join,seg5 与 seg7/seg8(t1 的获锁段)有 lock-fork 耦合;因 seg5 必须等 t2 跑完,所以 seg9(t2 全体)必须先于 seg7/seg8 → 把 (l, t1) 加入 LF(seg9),规则 6 即可判出 seg9 <lock-fork seg7/seg8。
- **第 24 行(inter 锁标注)**:若 fork(t) 发生在父线程 tp 的 intra 锁 l 保护下、且 l 一直持到对应 join(t),则 t 受过程间锁 l_tp 保护,l_tp 加入 t 及 D(t) 全体段的 IL [PDF p.7]。实例:Figure 3b 中 fork(t2) 在 tm 持 l 下发生、l 持到 join(t2),故 IL(seg9) = {l_tm}。

### 4.6 段关系判定六规则(Figure 5 [PDF p.7],正文散文逐条恢复)

记 t_seg / t_seg' = 两段所属线程;t_il = 过程间锁 il 的创建线程;multi-forked = multi-forked 线程全集。

- **规则 1(intra 冲突)**:L(seg) ∩ L(seg') ≠ ∅ ⟹ seg #intra seg'。(两段都真实持有同一把锁 → 不可能重叠。)
- **规则 2(inter 冲突)**,两个触发条件任一成立即判 seg #inter seg':
  - **2a**:IL(seg) ∩ IL(seg') ≠ ∅,且交集中存在 il 使 **t_il 不是两段所属线程的共同祖先**。(同一底层锁的两把"保护伞"若出自不同持有者,两个持锁区间互斥 → 两段所在线程的生命期不可重叠;若 t_il 是共同祖先,则两段同处一把伞下,伞只防外人、不防伞内 → 不判冲突——这是祖先例外条款的第一半。)
  - **2b**:L(seg) ∩ IL(seg') ≠ ∅(一方真实持锁与另一方的保护伞同底层锁;交集按底层锁对象匹配,l 与 l_t 视为同一把锁——此匹配语义为推断),且 **t_seg 不是 t_seg' 的祖先**。(真实持锁者若正是撑伞的祖先,伞内后代与它本就设计为并发 → 不判冲突——祖先例外条款的第二半;若持锁者是第三方,则它与保护伞的持有区间互斥 → 判冲突。)
- **规则 3(控制流 HB)**:t_seg = t_seg' 且该线程 ∉ multi-forked ⟹ 两段间存在控制流 HB(同线程按 CFG 定序;multi-forked 线程有多个运行实例,跨实例无序,故不给 HB)。
- **规则 4(join HB)**:t_seg ∈ J(seg') 且 t_seg' ∉ multi-forked ⟹ seg <join seg'。(seg 所属线程在 seg' 之前已被 join,其全部语句先于 seg'。)
- **规则 5(fork HB)**:t_seg' ∉ F(seg) 且 t_seg' ∉ J(seg),但 t_seg' ∈ D(t_seg),且 t_seg ∉ multi-forked ⟹ seg <fork seg'。(seg' 的线程是 seg 线程的后代、但在 seg 处尚未出生也未死亡 → 其 fork 点在 seg 之后 → seg 先于 seg' 全部;"∈ D(t_seg)"处花体符号丢失,按 D 集定义与语义唯一性恢复。)
- **规则 6(lock-fork HB)**:存在形如 (l, t_seg') 的元素 ∈ LF(seg),且存在形如 (t_seg', l) 的元素 ∈ FL(seg') ⟹ seg <lock-fork seg'。(seg 执行时其线程持着 l 且 t_seg' 已在持锁期内被 fork;t_seg' 建线程后要拿 l → 必须等 seg 的线程放锁 → seg 先于 seg' 中获锁点之后的段。)
- **收尾**:六规则都不命中 ⟹ seg || seg' [PDF p.7]。

### 4.7 运行例全复盘(Figure 2a 程序 + Figure 6 [PDF p.3, p.8-9])

程序形状(Figure 2a 为图片不可提取,以下由 §2.1/§3.1/§3.3 散文重构,置信度按句标注):主线程 tm 持锁 l 期间:先写 gvar1,fork(t1),循环内 fork(t2)(t2 为 multi-forked,依据 [PDF p.3] "Since t2's creation statement is in a loop, t2 corresponds to multiple runtime threads"),写 gvar2,join(t2),然后释放 l,写 gvar3;t1 内:lock(l) 后写 gvar4,释放后写 gvar5(gvar4 受 l 保护、gvar5 不受,依据 "s_gvar1 and s_gvar2 ... cannot be concurrent with s_gvar4"(锁冲突)与 "HB relationship due to lock and fork coupling between s_gvar1, s_gvar2, and s_gvar5" [PDF p.3]);t2 内:写 gvar6,无锁保护("s_gvar6, which is not protected by a lock, is concurrent with itself" [PDF p.3])。语句级精确位置为推断,段级结论以下列原文断言为准。

真值(§2.1 人工分析 [PDF p.3]):并发修改对**恰好 4 对**——(gvar2, gvar6)、(gvar3, gvar4)、(gvar3, gvar5)、(gvar6, gvar6 自身)。非并发的机制:gvar1/gvar2 与 gvar4 = 锁冲突;gvar1 与 gvar6 = fork HB;gvar1/gvar2 与 gvar5 = **lock-fork 耦合 HB**(tm 持 l 时 t1 已 fork,t1 获锁须等 tm 放锁);t2 全体先于 t1(join(t2) 与 unlock 都先于 t1 的获锁点);gvar6 自并发 = multi-forked。

TCFG 系方法的失误(§2.2 [PDF p.3] + Table 1):Table 1 打勾矩阵共 7 处标记 [PDF p.4 提取]〔页锚经 G1 审计更正:原标 p.3〕,颜色语义:黑勾 = 判对的并发对,红勾 = 误判为并发(实际有序/互斥),绿勾 = 误判为非并发(实际并发)。颜色在文本提取中丢失,按散文恢复:绿 = (gvar2, gvar6)(被"t2 全体受 l 保护"的错误假设判成冲突 [PDF p.3]);红 = (gvar1, gvar5)、(gvar2, gvar5)(缺 lock-fork HB)与 (gvar5, gvar6)(缺"t2 先于 t1"的耦合序,此对归属为推断);黑 = (gvar3, gvar4)、(gvar3, gvar5)、(gvar6, gvar6)。红黑合计 6 报 3 真,与 Table 3 中 RRG 在 DRB005 上 6/3 吻合 [PDF p.10]。

STCFG 的判定实录(§3.3 [PDF p.8],Figure 6a/6b/6c 为图片,属性表不可提取,以下为正文引用的三条推理):

1. **inter 冲突**:IL 或 L 相关交集非空(集合符号丢失;按规则 2b 句式)且 t_seg10 不是 t_seg8 所属线程的祖先 ⟹ seg8 #inter seg10;
2. **lock-fork HB 链**:(l, t1) ∈ LF(seg3) 且 (l, t1) ∈ LF(seg4);经 Algorithm 2 的 LF 传播机制得 (l, t1) ∈ LF(seg10);又 (t1, l) ∈ FL(seg9) ⟹ seg3、seg4、seg10 均 <lock-fork seg9;
3. **祖先例外救回真并发**:seg4 与 seg10 之间无任何 HB/冲突 ⟹ seg4 || seg10,"从而避免混淆 intra/inter 锁可能造成的假阴性"。

最终 MHP 结果(Figure 6c [PDF p.8]):恰 4 对涉及全局变量修改的并发,与人工真值一致 → DRB005 上 4/4 [PDF p.10]。

---

## 5. 实验协议与结果批判

### 5.1 协议 [PDF p.8]

- 实现:SVF [21, 22] + LLVM 16.0.0,指针分析用 Andersen 算法 [23];测试程序编 LLVM IR 时开 **O1** 优化。
- 机器:Intel Core i7-12700 @ 2.1 GHz,64 GB 内存,Ubuntu Linux(内核 5.15.0)。
- 基准:**12 个 C 程序 = SPLASH2 基准套件 4 个 + 自研 8 个**("eight that we develop ourselves")。
- 基线:**TCT 与 RRG 均为作者复现**("we reproduce the TCT and RRG methods")——非原作者代码,复现保真度不可查验(基线原实现是否公开未说明)。
- 计时口径:只计模型构造 + MHP 分析,**不含 SVF 中间表示构造与指针分析时间** [PDF p.8 §4.2]。

### 5.2 精度:Table 3 逐行抄录 [PDF p.10]

格式 = 报告数/真阳性数;True = 真实数据竞争数。

| 程序 | 说明(原文) | True | TCT | RRG | STCFG |
|---|---|---|---|---|---|
| DRB001 | Simple data race program | 2 | 2/2 | 2/2 | 2/2 |
| DRB002 | Intra-procedural lock test | 0 | 0/0 | 0/0 | 0/0 |
| DRB003 | Join test | 2 | 3/2 | 2/2 | 2/2 |
| DRB004 | Array bounds test | 0 | 3/0 | 2/0 | 2/0 |
| DRB005 | Program of Figure 2a | 4 | 7/3 | 6/3 | **4/4** |
| DRB006 | Inter-procedural lock test | 9 | 0/0 | 0/0 | **9/9** |
| DRB007 | Indirect join test | 5 | 8/5 | 6/5 | **5/5** |
| DRB008 | Multiple nested join test | 9 | 10/9 | 9/9 | 9/9 |
| fft | Complex 1-D FFT | 0 | 803/0 | 684/0 | 684/0 |
| lu_cb | Matrix triangulation | 0 | 276/0 | 169/0 | 169/0 |
| lu_ncb | Matrix triangulation | 0 | 276/0 | 169/0 | 169/0 |
| radix | Integer sort | 0 | 252/0 | 205/0 | 205/0 |

原文对失误归因 [PDF p.8]:TCT/RRG 的错误来自复杂 fork/join 依赖建模不准、RRG 的单线程对建模丢上下文、两者都无 lock-fork 耦合与 intra/inter 锁区分;DRB004 上三方法全误报,因把整个数组当单一操作对象、不判元素地址;SPLASH2 上"**所有**假阳性源于未考虑访问对象是否为全局变量/同址"——并附声明:"TCT, RRG, and the proposed method are not actual data race detection methods",不考虑内存对象与路径条件 [PDF p.8]。

### 5.3 效率:数字逐条抄录 [PDF p.8](Figure 7/8 为图,绝对秒数不可提取;四个测试程序按上下文推断为 SPLASH2 四程序)

- 总时间(Figure 7):STCFG 平均执行时间 = TCT 的 **21.96%**;比 RRG **快 33.3%**(表述歧义:按行文取"STCFG 用时约为 RRG 的 2/3");
- 构造阶段(Figure 8):STCFG 耗时 = TCT 的 **6.05%**;相对 RRG **降 73.29%**;
- 分析阶段(Figure 8):相对 TCT **提升 63.28%**;相对 RRG **提升 13.47%**。
- 内部一致性验算(本文所做):由三组比值反解,TCT 的构造/分析时间比约 0.93、RRG 约 0.50 时三组数字自洽——无内部矛盾,但绝对值不可复核。
- 排版笔误:Figure 7/8 图题把 TCT 误写为 "MHP"("Execution time comparison of MHP, RRG, and STCFG")[PDF p.10],正文明确为 TCT [PDF p.8]。

### 5.4 批判:"Preliminary results" 措辞的诚实度与支撑力

摘要原句:"Preliminary results show that our method provides higher precision and achieves higher efficiency" [PDF p.1]。逐条对账:

1. **"preliminary" 用得诚实,且必要**。证据规模确实初步:8 个自研微用例 + 4 个 SPLASH2 程序;基线是自己复现的两个 2005/2015 年方法;无与 2018 静态向量钟 [20] 的实测对比(只在相关工作里点名);无任何复杂度分析(全文没有一个大 O);程序规模(行数/线程数/段数)未报告。
2. **"higher precision" 的支撑力要拆成两半看**。在自研用例上成立且机制清晰:STCFG 严格优于 RRG 的仅 3 个用例——DRB005(6/3→4/4,lock-fork 耦合)、DRB006(0/0→9/9,inter 锁)、DRB007(6/5→5/5,间接 join),**恰好一一对应本篇引入的三个机制,即用例是为机制定制的**(用例名 DRB 前缀易联想 DataRaceBench,但原文明说 8 个为自研,不可当标准基准引用)。而在全部 4 个真实程序上,**STCFG 与 RRG 的数字逐字相同**(684/169/169/205)——真实程序上精度增益为零,只剩速度增益。
3. **真实程序上召回率从未被测试**。SPLASH2 四程序 True 列全为 0:只能度量假阳性,不能度量"该报的是否报了";DRB006 展示的 9/9 召回优势没有任何真实场景对应物。
4. **DRB006 的 0/0 要正确解读**:不是基线"精度低",而是基线在 inter 锁场景**全漏**(9 个假阴性)——这一格是全表唯一的杀手级数字,但它测的是基线的已知盲区(论文自己指出的),属于"按靶画箭再射箭"的自证结构。方向正确、力度有限。
5. **MHP 与竞争检测的指标错位**:表头是 "Data races found",量的却是 MHP 对(论文自己声明三方法都不是竞争检测器 [PDF p.8])。把 MHP 对数当竞争数报,数百个假阳性(fft 684)在竞争检测语境里是不可用水平;在 MHP 语境里则无从判断好坏(缺 MHP 真值)。指标与任务的错配使 Table 3 的语义两头不靠。
6. 计时**剔除了指针分析**:对静态分析,Andersen 常是大头;端到端加速比未知。

结论:数字无内部矛盾、自我声明克制(preliminary、not actual race detection、limitations 段),诚实度合格;但"higher precision"的外推力仅覆盖自研用例,对真实程序的可证明增益只有效率。

---

## 6. Potential flaw

### 6.1 情境局限:同步词汇表太窄(论文自认 + 后果推演)

- 自认 [PDF p.8 结论]:"currently only supports mutex locks and fork/join operations, without covering other synchronization statements in the Pthreads standard"。即只有 create/join/mutex_lock/mutex_unlock 四原语(§2.1 的表述加 unlock 共四种映射 [PDF p.2]〔页锚经 G1 审计更正〕);**条件变量(pthread_cond_wait/signal,即 C 侧的 wait/notify)、barrier、读写锁、信号量、trylock、C11 原子操作全部不建模**。这与 02/04 篇"只有五原语、wait/notify 留白"是同一家族性短板。
- **后果比自认的更重(推断)**:SPLASH2 程序重度使用 barrier 同步(fft/lu/radix 的标准实现以 BARRIER 宏为主要同步手段)。barrier 不建模 → 大量真实 HB 缺失 → MHP 过报。因此 [PDF p.8] "SPLASH2 上所有假阳性都源于未考虑内存对象同址"这一 **"all" 归因很可能过强**:barrier 缺失的 HB 也应是来源之一。这直接削弱"精度损失只剩内存对象过滤"的叙事。
- 判定为"排除式默认"(无 HB 无冲突即并发)使每一个未建模的同步原语都自动转化为假阳性——方向上保守(不漏报),但代价是词汇表外的程序上精度塌陷。

### 6.2 坏数据性质:哪里会坏、怎么坏

1. **LF 并集方向的健全性缺口(文本可见的最尖锐问题)**:Algorithm 1 第 10 行 LF 取并集、与 F 联动(§4.4)。LF 是规则 6 推 HB 的原料;HB 是"必然有序"断言,原料应取路径交集(must)。若两条汇合路径中只有一条在持 l 期间 fork 了 t,并集后的 (l, t) 会对另一条路径的执行虚构 seg <lock-fork seg' → **虚构 HB → 漏报真 MHP → 下游漏检真竞争**。这与论文"deliberately include more threads in F to prevent false negatives" [PDF p.6] 的自我辩护正好相反:F 取并防漏报,LF 取并却制造漏报。全文无 soundness 定理、无证明,该缺口无从对账(基于提取文本的行结构推断;若原图 Algorithm 1 第 10 行实为差集,此条撤回,但那将与"dLF = LF('seg) − LF(seg)"的差量方向矛盾)。
2. **multi-forked 线程的 join 语义未闭合**:定义 1 条件二(fork 回路上无 join)判 multi-forked;但运行例中 t2 既是 multi-forked 又被 join(t2) 等待,规则 4 的守卫只查 **t_seg' 是否 multi-forked,不查被 join 的 t_seg 自身**——若 join 语句的执行次数少于 fork 次数(部分实例未被等待),"t2 全体先于后续段"的 HB 就是虚构。论文未陈述"join 覆盖全部运行实例"的假设,静态也难验证(推断)。
3. **间接调用/函数指针**:pthread_create 的入口本身就是函数指针,靠 Andersen 指针分析解析 [PDF p.8];Andersen 是流不敏感的 may 分析,入口集合过大时抽象线程增多、F 集膨胀,精度按线程数平方稀释。锁对象若在数组/结构体里(SPLASH2 常见的每元素锁),别名合并会把不同锁并成一把 → 虚假冲突。论文对二者零讨论。
4. **动态线程数**:线程数依赖输入(循环上限、命令行参数)时,multi-forked 机制一刀切地放弃线程内 HB——保守但粗糙;"以线程创建语句为抽象线程"的建模对线程池、递归 fork 等模式的行为未定义。
5. **规则 2a 在 multi-forked 祖先下的空转(推断)**:若撑伞祖先自身是 multi-forked,同一 l_t 的两个运行实例持锁区间互斥,伞下两段实际不可并发,但抽象层面 t_il 仍是"共同祖先"→ 2a 不触发 → 假阳性。规则未按运行实例细分。
6. **Table 2 join 行的 LF 清理只删 L(seg) × {t}**:若 t 被 join 时相关锁已释放(L 中已无 l),(l, t) 残留;残留对经第 23 行传播还会被灌进后代——就 MHP 而言方向错的 HB 仍给出"非并发"的正确结论,故是脏而不毒(§4.3 已注);但它说明属性系统缺不变式陈述,工程实现极易在此引入真 bug。

### 6.3 哪个值得写 paper

- **最值得:把"MHP 基座"补成带证明的全词汇表版本**——(a) 六属性系统的形式化 + 过近似 soundness 定理(顺手修 6.2.1 的 LF 方向);(b) 扩到条件变量/barrier(barrier 给段属性加"相位"维度,条件变量给 LF/FL 加"信号耦合"镜像,与 lock-fork 是同构扩展);(c) 在有真值标注的真实基准(如 DataRaceBench 真身)上测召回。这三件事合起来是一篇扎实的期刊长文,且直接补掉本篇 "preliminary" 的全部缺口——组内没人占这个位。
- 次优:**MHP × 值流的闭环**——把本篇 MHP 输出接 03 篇的源汇路径过滤(内存对象同址判定正是 [PDF p.8] 自认的假阳性根源,而组内 03 已有 SVF 值流全套),做成真正的竞争/UAF 检测器;工程为主、故事现成。
- 不值得单独写:纯效率改进(段粒度加速已被本篇与 RRG 占位)、LLM 辅助路径条件([PDF p.10] 展望段已自留,且验证成本高)。

---

## 7. Motivation 还原(问句形式)

1. 竞争检测、死锁检测、UAF 检测都要先问"这两句可能同时跑吗"——**如果地基本身漏水,楼上做得再精有什么用?**(MHP 是基座 [PDF p.1])
2. 既有 HB 分析只认 fork/join——**锁难道只产生互斥、不产生顺序吗?**"父线程持锁育儿、子线程要锁得排队"这条序,谁来接?[PDF p.2]
3. 祖先替后代持的锁,和后代自己拿的锁,**保护效力是同一回事吗?**把两者混为一谈会把伞下的真并发(后代 vs 祖先/兄弟)判成互斥,漏掉的竞争谁负责?[PDF p.2, p.5]
4. 逐语句判 MHP,同一并发上下文被算几百遍——**哪些语句其实共享同一份并发命运?**能否按"命运变化点"切开,段内一次算清?[PDF p.4]
5. TCT/RRG 查询一次搜一次可达性——**能不能把搜索预付到建图期,让查询退化成查表?**[PDF p.8]
6. (家族视角,论文不明说)组里在 Java 轨迹(02/04)和 C 静态 PN(03)上反复用的分段 + lock-fork 耦合,**能不能在"不背 PN 状态爆炸包袱"的纯图载体上再落一次,顺便占住 MHP 这个上游位?**
7. (对位命名暴露的问题意识)Di et al. 2015 已用 region 做了 C 的 MHP——**region 与 segment 差在哪?**答:切分依据。region 按结构切,segment 按"并发上下文等价"切,且属性里多了锁-线程耦合两个维度。

---

## 8. 张力结构分析

1. **粒度张力(精度 vs 效率)及其真实落点**:表面上"段粗于语句、细于过程",是效率-精度折中;第一性看,**切分本身不损失属性系统内的任何信息**(段 = 属性等价类,商映射无损),真正的取舍全部藏在**属性抽象**里——六个集合记"有无"不记"次序与次数"(对照:04 SegLock 的弧标签记轮次 m 与序号 k)。于是本篇的粒度张力实为:**集合式属性能表达的并发语义边界,决定了段粒度的精度上限**;论文用三个新机制(LF/FL/IL)扩了边界,但没触碰"集合 vs 序列"的根本限制。
2. **过近似方向的内部撕扯(sound vs precise)**:F 取并(防漏报)、J/L/FL 取交(防误杀)是自觉的方向管理 [PDF p.6];但 LF 被 F 拖着走并集(联动条款),让"防漏报"的机制反过来制造漏报隐患(§6.2.1)。张力根源:**LF 同时承担 may 语义(与 F 联动的存在性)与 must 语义(推 HB 的必然性)**,一个集合背两种模态,系统里没有第二个槽位安放。
3. **建图期 vs 查询期(空间换时间)**:三步全局传播把跨线程事实灌进每个段(J/FL/LF/IL 全量下传后代),属性表随线程深度与段数膨胀;换来查询期纯集合运算、免可达性搜索 [PDF p.8]。构造 6.05%/26.71%、分析 36.72%/86.53%(相对 TCT/RRG 的耗时占比,由 §5.3 换算)说明红利大头在构造侧——**分段先行降低了传播的迭代基数**,这与"查询免搜索"是两笔独立收益,论文归因把二者说清了,难得。
4. **抽象线程 vs 运行时线程**:静态命名(每 fork 语句一个抽象线程)与动态实例(循环 fork 出 N 个)的错位,用 multi-forked 标签一刀切补丁——保守方向正确,代价是 multi-forked 线程内部全序尽失 + join 语义悬空(§6.2.2)。这是所有静态并发分析的祖传张力,本篇的处理属于"显式承认 + 最粗补丁"。
5. **MHP 基座 vs 竞争检测门面**:评测用 "data races found" 讲故事,又声明自己不是竞争检测器 [PDF p.8]——想借下游任务的可感知价值,又不愿承担下游任务的指标责任。这一张力直接产出 §5.4.5 的指标错位。
6. **家族张力(一个 insight 摊销四个载体 vs 单篇新颖性)**:lock-fork 耦合在 02(PN 展开)、03(分段 PN 伴随标签 α/β)、04(lock-start 耦合因果 + 分段图)、本篇(LF/FL 集 + STCFG)四度落地;本篇零自引地把它呈现为新发现(§0)。对组是效率(一个洞见吃四篇),对单篇是新颖性风险(审稿人若识破谱系,增量只剩 IL 二分 + 段属性工程);**IL 的 intra/inter 二分与祖先例外条款是本篇真正独有的增量**,DRB006 的 9/9 vs 0/0 是它的证据。

---

## 9. 家族内差分(与 03 静态分段 PN、04 动态分段锁图的三方对照)

### 9.1 同名"分段",三套坐标

| 维度 | 03 UAF(分段 PN + 值流) | 04 SegLock(分段图 + 锁图) | 08 本篇(STCFG) |
|---|---|---|---|
| 输入域 | C/C++ 源码(静态,LLVM 风格中间码) | Java **单条运行轨迹**(动态) | C 源码(静态,LLVM 16 + SVF)[PDF p.8] |
| 切分依据 | PN 上的段映射 λ(继承 2021 中文分段图谱系) | 轨迹事件:start/join 之外**锁释放也开段**(规则 v) | 六场景 A–F:线程入口/fork/join/**lock/unlock**/多前驱汇合 [PDF p.4] |
| 承载结构 | 分段 PN(锁 = 库所,伴随标签 α/β)+ 分段值流图 | 锁增广分段图 + 序增广锁图(弧带轮次 m、序号 k)+ 历史锁耦合因果图 | 单一 STCFG,段节点挂六属性集(F/J/FL/LF/L/IL) |
| 并发判定引擎 | PN 展开(occurrence net 判并发/冲突,cut-off 做循环摘要) | 段间可达闭包(不可达 = 并发)+ 图矩阵求环 | 属性集合运算六规则,**查询期零图搜索** [PDF p.7-8] |
| 判定目标 | UAF(free→use 源汇路径 × 三约束兼容性) | 死锁(锁图环 × 五因果过滤)+ 确定性重演 | **MHP 语句对**(上游基座,无下游判定) |
| lock-fork 耦合的形态 | "lock/fork 耦合因果"(定义 2 第三型),α/β 伴随标签 | "lock-start 耦合因果"(定义 2 第 3 关系),物化为段间弧 | LF/FL 集 + 规则 6 + join 下传(第 23 行)[PDF p.6-7] |
| 循环/多实例处理 | cut-off 展开段 = 循环摘要(语义等价) | 弧标签区分轮次(只覆盖已观测轮次) | multi-forked 标签,一刀切放弃线程内序 [PDF p.3] |
| 本篇独有 | — | — | **intra/inter 锁二分 + 祖先例外条款(IL/规则 2)**;三方中仅此篇处理"继承保护 ≠ 真实持锁" |

三句话概括差分:**切分依据**上,03 切在 PN 结构、04 切在轨迹事件、08 切在"并发上下文属性变化点"——只有 08 把切分准则显式定义为属性等价;**承载结构**上,03 用双图(PN + 值流)分担控制因果与数据到达、04 用双图(段图 + 锁图)分担因果与资源环、08 用单图 + 富属性把一切折进节点;**判定目标**上,03/04 是终端检测器(UAF/死锁),08 是上游谓词供应商,不产出 bug 报告(论文自我声明 [PDF p.8])。

### 9.2 判定机制的谱系位置

同一个问题"两个事件能否重叠",家族给了三个答案:04 在动态轨迹上做**图可达**(观测到什么算什么,理论覆盖面窄但零误建模);03 在静态 PN 上做**展开**(语义最全,状态爆炸风险最高);08 在静态图上做**属性集合代数**(最轻,表达力被集合抽象封顶)。这正是 README 谱系"重模型 vs 轻模型"路线之争在**静态侧**的复刻:03 之于 08,恰如 02 之于 04——每条线都是"PN 精算版"与"图近似速算版"成对出现。08 与 04 还共享二作王小宇,坐实两条轻量线同源。

### 9.3 MHP 作为上游基座如何喂下游

- **喂 03 类静态检测**:03 的三约束兼容性判定中,"控制流因果约束"部分(线程内序、fork/join 序、lock/fork 耦合序)与本篇的 HB 四来源语义重合——03 现在用自己的 PN 展开算这些,若换用 08 的段属性查表,可把展开只留给循环摘要,规模瓶颈立减;反向,08 自认的假阳性根源(不判内存对象同址、无路径条件 [PDF p.8])恰是 03 值流图与条件约束已覆盖的能力。**08 出"可能并行"候选对,03 出"数据真到达"过滤,拼起来才是完整检测器**——这条组内闭环两篇都没引用对方,属于地图机会而非既成事实(与 README 对 D1/D2 闭环的判断同构)。
- **喂 04 类动态检测**:静态 MHP 可为动态工具剪枝——只对 MHP = true 的语句对插桩/调度探索,降低 CalFuzzer 式探针的开销;08 的 LF/FL 与 04 的 lock-start 因果语义同源,静态先验可直接初始化动态侧的因果图。同样,无既成互引,纯接口推演。
- **喂竞争检测(论文自己的定位)**:MHP 对 + 别名同址过滤 + 路径条件 = 数据竞争检测器;[PDF p.10] 展望段给出的路线是"静态保 soundness + LLM 做数组边界/循环/路径条件推理降误报"——把 §6.3 的"次优 paper"(接值流)替换成了接 LLM,这是 2025 年的时代口味,也再次说明作者知道缺的是内存语义层。

### 9.4 给进组话术的一条增量

面谈可用的一句话定位:"你们组的分段思想我数出三条载体线——Java 轨迹图(SegLock)、C 静态 PN(UAF 篇)、C 静态 STCFG(MHP 篇)——MHP 篇是唯一做上游基座的,而且是唯一处理过程间锁继承保护的;我想知道 STCFG 的段属性有没有可能直接喂 UAF 篇的兼容性判定,把展开省下来?"——同时点到三篇、指出唯一性、给出可执行的组内缝合点(此缝合点为本文推演,非论文内容)。

---

## 附:安全门自查

- **不编造**:所有断言带 [PDF p.X] 锚;花体符号丢失处的指称恢复(F/J/FL/LF/L/IL、D(t)/J_must(t)、规则 5 的 D 集、Table 2 join 行 × 操作数、Table 1 颜色分配、Figure 2a 程序形状、Figure 7/8 四程序身份、规则 2b 底层锁匹配)全部显式标注"推断/恢复依据";Figure 2a/4/5/6/7/8 与 Table 1 颜色为图像内容,文本不可提取处已声明。
- **不过度承诺**:§5.4/§6 的批判均区分"论文自认/文本可证/推断";LF 并集健全性问题附撤回条件;"barrier 致 SPLASH2 假阳性"标为推断。
- **全覆盖**:正文 §1–5 全部技术内容(定义 1/2、六属性、Table 2 六行、Algorithm 1/2、六规则、Table 3 十二行、效率六数、结论自认局限、LLM 展望)无跳过;Figure 6a/6b 的逐段属性表因是图像未逐格恢复(正文引用的三条推理已全录),为本文唯一篇幅/载体受限缺口。
