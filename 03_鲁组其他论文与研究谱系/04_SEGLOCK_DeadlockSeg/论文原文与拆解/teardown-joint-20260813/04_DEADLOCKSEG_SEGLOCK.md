# 04 · SegLock:细化分段图 + 锁图的死锁检测与重演(D2 线)

> Lu F., Wang X.(王小宇), Yuan G.*(袁贵元,通讯), Zheng J., Bao Y. "Deadlock Detection and Replay of Multi-Thread Programs Based on Refined Segmentation and Lock Graphs." *Tsinghua Science and Technology*, 2026(2024-12-30 收稿,2025-04-18 接收). DOI: 10.26599/TST.2025.9010085
> 作者线:鲁法明(一作)/ 王小宇(博士生,鲁侧图 T1 借力的"王小宇线")/ 袁贵元(同济博士 2023,山科大讲师)/ 郑佳婧(2021 锁增广分段图中文论文一作系,现中科曙光)/ 包云霞
> 鲁侧图定位:**D2 死锁线的最新迭代:从 PNULock 的 PN 展开退回到轻量图方法,精度持平、开销大降——组内"重模型 vs 轻模型"路线之争的现行答案**

---

## 1. 问题

动态死锁检测的两个残留假阳性来源 + 一个重演痛点(直接对标组内前作):

1. **现有分段图**(Bensalem & Havelund、Agarwal 等,按 start/join 分段)**建模不了"锁获取/释放与线程 start 耦合"的因果依赖**——线程 t1 持锁 G 期间 start 了 t2,则 t2 中需要 G 的操作必须等 t1 释放 G,这是跨线程因果,start/join 分段捕获不到(= PNULock 论文里 Program 1 的同一问题,本文给出图方法解法);
2. **现有锁图的 lockSet 只记"当前持有锁"**,丢失"曾持有随即释放"的**历史锁**信息:轨迹 σ2 中 t1 依次 acq(m)、acq(n)、rel(n)、acq(q)、acq(p),t2 反向;若 (m,q)/(n,p) 各成环但环的达成要求双方都先拿到对方历史上拿过的锁,则环不可能并发形成(ConLock+ 论文里出现过这个例子但其算法排除不了);
3. 现有重演(DeadlockFuzzer/ConLock 系)**推不出直观调度方案与死锁触发路径**。

## 2. 方法

### 2.1 轨迹与因果依赖体系(定义 1–2,本文的理论核心)

轨迹 = 五原语序列:$\sigma \in ConPrimitive^*$,$ConPrimitive = \{start(u,v), stop(v), join(u,v), acq(u,l), rel(u,l)\}$。

**定义 2 给出五种因果/互斥关系**(前三种是已有工作的,后两种是本文新增):
1. 线程内因果 $e_i <_{thread} e_j$;线程间 start 因果 $e_k <_{start} e_m$;
2. join 因果 $e_k <_{join} e_m$;
3. **"lock-start" 耦合因果** $e_k <_{lock\_start} e_l$:$e_i = acq(u,o)$、$e_j = rel(u,o)$、期间存在 $e_m = start(u,v)$,且 v 中有 $e_n = acq(v,o)$,则 u 在持锁区间内的事件先于 v 中 $e_n$ 之后的事件;
4. 锁集互斥 $e_i \#_{lockSet} e_j$:$lockSet(e_i) \cap lockSet(e_j) \neq \emptyset$(门锁保护,不可能并发);
5. **"历史持有锁-持有锁"耦合因果** $e_i' <_{lock\_held} e_j'$:定义**历史持有锁集** $lockSet\_OnceHeld(e_i)$ = 线程 u 在获取当前各持有锁的过程中曾获取过的锁集;令

$$L\_IS = lockSet\_OnceHeld(e_i) \cap lockSet(e_j)$$

若 $e_i, e_j$ 要并发成死锁,则对 $o \in L\_IS$,u 获取历史锁 o 的事件必须发生在 v **最后一次**获取持有锁 o 的事件之前。

对应五类假阳性:单线程环、start/join 因果环、门锁环(前三者已有方法能杀)、lock-start 耦合环、历史锁耦合环(本文新杀的两类)。

### 2.2 锁增广分段图(定义 3)

$$SegG\_Lock = (SegSet, SegR, \varphi_s, \varphi_r)$$

相对传统分段图的两个增广(论文原文加粗处):
- **段的细分**:除 start/join 外,**锁释放操作也成为分段点**——规则(v):线程 v 在段 $s'$ 执行 $acq(v,l)$ 时,反向找到首个获取 l 的段 $s''$;若 $s''$ 属于其他线程且 l 未在 $s''$ 内释放,则从当前获取操作起新开段 $s'\_new$,并从 $s''$ 后代中"以 rel(u,l) 结尾"的段 $s''\_desc$ 向 $s'\_new$ 加弧——**lock-start 耦合因果被物化成段间弧**;
- **段标签 $\varphi_s$ 记录段内锁事件序列**:$\varphi_s(currentSeg) := \varphi_s(currentSeg) \circ l^{(k)}$(k = 轨迹序号,带下划线 = 释放,不带 = 获取),例:段 4 = $(G^{(16)}, \underline{G}^{(17)}, o_2^{(18)}, G^{(19)}, \underline{G}^{(20)}, o_1^{(21)}, \underline{o_1}^{(22)}, \underline{o_2}^{(23)})$。**历史锁集就从这个标签串反向扫描算出**。

段间可达闭包 $(s_1, s_2) \in SegR^+$ 记 $s_1 \rhd s_2$(先序);互不可达 = 两段并发。

### 2.3 序增广锁图(定义 4)

$$LockG\_Order = (V, R)$$

顶点 = 锁;t 持 $lock_1$ 申请 $lock_2$ 时加弧,标签扩为

$$\langle seg1ID, (t, lockSet), m, seg2ID \rangle^{(k)}$$

相对扩展锁图新增 **m(第几次获取该锁)与 k(轨迹序号)**——**循环中同一锁语句的多轮执行在图上成为不同弧**(PNULock 用"每次执行独立变迁"达成的目标,这里用弧标签达成,代价小得多)。

### 2.4 检测判定(§4)

潜在死锁 = 序增广锁图中的有向环 c,且要同时通过:
1. 环、2. 操作属不同线程、3. 所在段之间无有向路径(不被 start/join/lock-start 因果串起来)、4. 持锁集两两不交、5. **"历史持有锁-持有锁"耦合因果图 $DependG\_Lock_c = (V_c, R_c)$ 无环**(定义 5:顶点 = 环中各获取操作 + 历史锁获取操作,边 = lock_held 耦合因果 + 线程内因果;**该图有环 ⟹ 各因果不可能同时满足 ⟹ c 是假阳性**)。

### 2.5 重演(§5,两阶段调度)

- **伴随事件**(定义 6):$accompEvents(e)$ = 线程获取 $lockSet(e)$ 中各持有锁过程中执行的获取操作;
- **死锁伴随事件集**(定义 7):$DLAE(c) = \{e \mid e \in \sigma_{LockAcq} \wedge \exists e' \in E_c: e < e'\}$(环中事件的祖先,必须执行);**一阶集** $1\_DLAE(c)$ 再并入"受伴随事件影响的"获取事件;二阶集 = 差集;
- **调度方案生成**:二阶集事件按原轨迹授权序;一阶集事件构建**死锁调度特征关系图** $SchdG = (V, R)$(定义 8,边 = $<_{thread} \vee <_{start} \vee <_{join} \vee <_{lock\_start} \vee <_{lock\_held}$ 五种因果),**拓扑排序**得到使环中各获取操作并发的授权序;两段拼接成每锁的授权线程序列(Fig. 4 全流程:σ1 得 $G: t_1 \to t_2 \to t_2 \to t_1$、$o_1: t_1 \to t_1$、$o_2: t_1 \to t_2$);
- 执行端与 PNULock 相同:CalFuzzer lockBefore/lockAfter/unlockAfter + park/unpark,δ 清空 + 环检出 → 真死锁;δ 清空 + 正常终止 → 假死锁;其余未知。跨运行 ID 映射同 PNULock 附录(主线程锚定 + fork 序 + 锁申请序 + 共享变量访问序一致)。

## 3. 实验

原型:Java + CalFuzzer,三层架构(输入/处理/界面),界面可视化两图与重演结果。机器:i5-6300HQ,8GB,Ubuntu 18.10。

**基准 14 个**:8 个 CalFuzzer 例程 + Pingpong/cyclicDemo(ComRaDe)+ ConLockDemo(历史锁假阳性,取自 ConLock)+ PetriDeadLockDemo(lock-start 假阳性)+ OnceHeldLockDemo(两类叠加)+ MulThreadDeadlockDemo(三线程真死锁 + 四线程假阳性)。

对比 iGoodlock 与 **PNULock(组内前作,02 篇)**,结果(Table 5/6):
- **精度**:SegLock = PNULock,均零假阳性;iGoodlock 在 ConLockDemo 4/1、PetriDeadLockDemo 2/1、OnceHeldLockDemo 4/2、MulThreadDeadlockDemo 2/1;
- **检测时间**:SegLock 全面快于 PNULock(如 Test7:0.153s vs 0.927s;MulThread:0.235s vs 1.354s)〔⚠️ 08-24 勘误:本行数字直引原文 Table 5 [PDF p.14],但其 PNULock 列疑整列错位一行——Test7 真实对照值应为 0.260s(比值 1/1.7 非 1/6),引用前必读 02b §〇.2＋_audit_remediation_20260824/A4_pdf_verification.md〕——PNULock 的 PN 含更多信息且受状态爆炸拖累;SegLock 用**图矩阵求环(多项式)** vs iGoodlock 图遍历(指数),有死锁时甚至快过 iGoodlock;
- **内存**:iGoodlock < SegLock < PNULock(SegLock 两图 + 因果图的信息量代价,PNULock 状态爆炸代价);
- **重演**:SegLock 与 PNULock 都确定性一次成功、时间相当(0.12–0.53s);iGoodlock/DeadlockFuzzer 有抖动(thrashing),Test1a/1b 需 3+ 次。

**内部对标的结论要读出来:精度上 SegLock 没有超过 PNULock,它的贡献是把同等精度做进了轻量模型**——检测时间降为 1/2 到 1/6〔⚠️ 08-24 勘误:按错位数字算;按真实对照为 1.70–6.35×(中位 2.76×,宣称范围大体成立但名实错位),见上注〕,内存也更低。

## 4. 局限(论文自认 + 我的补充)

论文自认:
- 只考虑五原语,wait/notify/notifyAll 未处理(σ3 的 park/unpark 假阳性只能靠重演兜底,检测阶段识别不了);
- 未来方向:深度学习/LLM 死锁检测、自动程序修复。

我的补充:
- 与 PNULock 相同的评测短板:14 个例子仍是**教学级小程序**,最大也就几十个事件;"图矩阵多项式 vs 遍历指数"的复杂度优势没有在大轨迹上实测;
- 序增广锁图对循环的处理是"区分各轮执行",但轨迹里只出现**实际执行过的轮次**——PNULock 靠展开能推广到未观测交错,SegLock 的图方法在这点上理论覆盖面更窄(两篇都没做覆盖率对比,这是内部路线之争缺失的一块证据);
- 历史锁耦合因果图的构造复杂度未给出形式化分析;
- 未与 2023 年后的 SOTA(如 PLDI'23 线性时间 sound prediction)对比。

## 5. 进组视角

**复现/扩展切入点**
- 复现:CalFuzzer + 论文三条轨迹 σ1/σ2/σ3 手工构图(Fig. 2/3 可逐弧核对),再跑 14 基准复算 Table 5/6——工作量小于 PNULock 复现,可以作为**理解 D2 全线的入口读物 + 第一个复现目标**;
- 扩展 A:补一个"检测能力覆盖面"对照实验:构造 PNULock 能检出、SegLock 检不出的交错(若存在),把两条路线的 trade-off 从"快慢"深化到"能力边界"——这对组内技术决策有直接价值;
- 扩展 B:wait/notify 原语扩展(论文自留的坑,且 PNULock 论文也留了同一个坑:两条线都停在资源死锁)。

**与 T 课题的关系(T1 的另一半)**
- 鲁侧图 T1 写的是"D2 展开 + 死锁割集(王小宇线)"——王小宇正是本文二作。**T1 面前摆着组内现成的两套载体:PNULock 的展开(重、语义全)与 SegLock 的增广图(轻、可扩展)**;MAS 传播割集若要在线/边缘部署(对接 T2 的边缘叙事),SegLock 式的轻量图 + 因果标签更现实;若要离线生成攻击偏序证据与重演调度,展开更强。进组后值得直接问王小宇他自己的判断;
- 本文"因果依赖体系(五关系)+ 兼容性判环"的模式可平移到 MAS:把 acq/rel 换成 agent 对共享资源(记忆库、工具、信道)的占用/释放,"历史持有锁"对应"agent 曾获取过的权限/上下文"——**权限升级链检测**可能是比死锁更贴 MAS 安全的同构问题;
- 调度特征关系图 + 拓扑排序生成确定性触发序,可直接用作 MAS 攻击复现的调度器设计模板(T1 的"割集验证"一步需要它)。

**可能的"见面礼"问题(与王小宇/鲁老师聊)**
1. SegLock 与 PNULock 在"能检出的交错空间"上是否严格等价?有没有 PNULock 能报、SegLock 漏的构造样例?(两篇论文都没回答,这是路线之争的关键证据)
2. 结论提到 LLM 死锁检测——设想是 LLM 直接判轨迹,还是 LLM 生成候选交错再由 SegLock 验证?后者与我要做的 MAS 方向天然衔接;
3. ZR2024ZD22(山东省重大基础研究)资助下,这条线下一步是扩原语还是上真实规模基准?
