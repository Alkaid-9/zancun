# PAPER_READ — 偏序 alignment via Petri 网展开(FoldA + Siddiqui 双文精读)

**日期**:2026-08-13 ｜ 公式以 arXiv HTML 全文为准(2506.08627 / 2504.00550,实见);图内容受 HTML 转文本限制,仅据图注与正文,已逐处标注。

---

## 0 问题定位:alignment 的两个结构性缺陷

经典最优 alignment(Adriansyah 2014 博士论文,两文共同的引理来源)的计算路径:轨迹 → event/trace net → 与模型网做**同步积** → 在同步积的**可达图**上跑最短路(Dijkstra/A\*)。两个缺陷:

1. **交织爆炸**:可达图按交织语义枚举并发行为的所有先后顺序;模型并发/选择度高时状态数指数增长(FoldA §1 引 McMillan)。
2. **强加全序**:alignment 定义本身是 move 序列;即使轨迹事件间无依赖也被排成一条线。Lu/Fahland/van der Aalst 2014(LNBIP 202)提出偏序 alignment 补救,但其计算**仍先算一条全序最优 alignment 再偏序化**——而等代价最优全序解不唯一、诱导的偏序结构不同,任取一条可能得到次优偏序 alignment(FoldA §1 Fig 1 反例;§2 明说 Siddiqui 一文"完全没有点出这个根本问题")。

两文的共同答案:把搜索空间从可达图换成**分支过程**(Petri net unfolding),在配置(=偏序 run)空间做代价导向的有向搜索,**一步**产出偏序最优 alignment。

---

## 1 形式定义链(自下而上)

### 1.1 基础层

- **轨迹与日志**(FoldA §3):活动集 \(A\),trace \(\sigma=\langle e_1,\dots,e_n\rangle\in A^*\),日志 \(L\subset\mathcal{B}(A)\)(trace 多重集)。
- **偏序轨迹 p-trace**(Siddiqui Def 1):同案例事件集 \(E\) 上的标注 DAG \(\rho_c=((E,\prec_{\rho_c}),l_{\rho_c})\),其中 \(a\prec_{\rho_c}b\) **当且仅当 a 的结束时间戳严格小于 b 的开始时间戳**;\(l_{\rho_c}:E\to\mathcal{L}\)。边称为依赖(dependency)。⚠ 时间戳构造是 T2 必改点(04 §5.3)。
- **标注 Petri 网/系统网**(Siddiqui Def 2):\(\mathcal{N}=(P,T,F,\lambda)\),\(\lambda:T\to L^\tau\)(silent 记 \(\tau\));系统网 \(SN=(\mathcal{N},M_{init},M_{final})\)。FoldA 记法 \(N=(P,T,F,i,f)\)。
- **假设**:全文 1-safe(每 place 至多 1 token);模型网 **easy sound**——终态 marking 可达(FoldA 明确以此为唯一模型假设,支持无界 easy sound 网,见其附录 0.A.2;对照 García-Bañuelos et al. 的 PES 方法需要完整前缀故不支持无界网,FoldA §2)。

### 1.2 alignment 层

- **(全序)alignment**(FoldA Def 1):\(\gamma\in((A\cup\{\gg\})\times(T\cup\{\gg\}))^*\) 满足 (1) \(\pi_1(\gamma)_{\downarrow A}=\sigma\)(第一分量投影=轨迹);(2) \(i\xrightarrow{\pi_2(\gamma)_{\downarrow T}}f\)(第二分量投影是模型从 i 到 f 的 occurrence sequence);(3) \((\gg,\gg)\notin\gamma\)。move 四型:log move \((a,\gg)\)、model move \((\gg,t)\)、同步 move \((a,t)\)、非法 move \((\gg,\gg)\)。
- **最优 alignment**(FoldA Def 2):代价函数 \(\kappa:(A\cup\{\gg\})\times(T\cup\{\gg\})\to\mathbb{R}^+\),\(\kappa(\gamma)=\sum_{(e,t)\in\gamma}\kappa(e,t)\);\(\gamma\) 最优 iff \(\forall\gamma'\in\Gamma_{\sigma,N}:\kappa(\gamma)\le\kappa(\gamma')\)。
- **同步积**(FoldA Def 3;Siddiqui Def 15 为带标签函数的等价版):\(sp=N_l\times N_m=(P,T,F,i,f)\):
  - \(P=P_l\cup P_m\);
  - \(T=(T_l\times\{\gg\})\cup(\{\gg\}\times T_m)\cup SM\),FoldA 记 \(SM=\{(a,t)\in T_l\times T_m\mid a=t\}\);Siddiqui 版为 \(\{(t_1,t_2)\mid\lambda_1(t_1)=\lambda_2(t_2)\neq\tau\}\)(显式排除 silent 配对);
  - \(F\) 按分量继承原网流关系;\(i=i_l\cup i_m\),\(f=f_l\cup f_m\)。
- **偏序 alignment**(FoldA Def 4):同步积 move 上的**偏序** \(\delta\),使 Def 1 的 (1)(2)(3) 得到尊重。正文自注:与全序版的唯一区别就是"序是偏的"。
- **u-alignment**(Siddiqui Def 8,结构化版):三元组 \((\rho_c, G_\mathcal{N}, \varphi)\)——p-trace、模型 run 诱导的偏序 \(G_\mathcal{N}=((T',\prec_\mathcal{N}),l_\mathcal{N})\)、单射对齐函数 \(\varphi:E'\to T'\)(\(E'\subseteq E\)),满足:(1) 标签相等 ⟺ 被 \(\varphi\) 映射(即同步);(2) 将每对同步节点合并为单节点后,\(\rho_c\biguplus G_\mathcal{N}\)(**alignment order**)仍是严格偏序——排除对齐制造因果环的病态匹配。
- **扩展同步积**(Siddiqui Def 9,标准编码技巧):加目标变迁 \(t^*\)(preset = 原终态 marking)与目标 place \(p^*\)(保 1-safe);\(M^{ext}_{final}=[p^*]\)。终态可达检查 ⇒ "目标事件 \(e^*\)(\(h(e^*)=t^*\))出现"。FoldA 等价做法:加 dummy end 事件,停机条件变为 \(\exists x\in\beta:\mathit{Mark}([x])=\mathit{fm}\)。
- **alignment run**(Siddiqui Def 10):扩展同步积的完整分布式 run \(\upgamma=(B,E,F,h)\),以 \(e^*\) 收尾(无后继条件唯 \(b^*\),\(\pre b^*=e^*\))。全体记 \(\mathcal{U}_{SN_\otimes^{ext}}\)。

### 1.3 展开层

- **出现网**(FoldA Def 5 / Siddiqui Def 4):\(O=(B,E,G)\),条件 \(B\)、事件 \(E\);① 每条件至多一个入事件 \(|\pre b|\le1\);② 无环;③ 有限前驱;④ 无自冲突。**因果网**(Siddiqui)再加 ⑤ 每条件至多一个出事件——因果网=无选择的偏序 run 载体。三关系:因果 \(x<y\)(有向路径)、冲突 \(x\#y\)(同 place 出发立即分叉的两条路径)、并发 \(x\|y\)(两者皆非)。
- **分支过程**(FoldA Def 6 / Siddiqui Def 5):标注出现网 \(\beta=(O,p)\),标注 \(p\)(Siddiqui 记 \(h\))是到原网的网同态:事件↦转移、条件↦place;\(p\) 限制在 \(\pre e\) 上是到 \(\pre{p(e)}\) 的双射;起点 \(p(\mathit{Min}(O))=i\);**无重复事件**。⚠ 勘误:FoldA Def 6(3) 写作"\(\pre e_1=\pre e_2\Rightarrow e_1=e_2\)",**漏掉标签相等条件**;Siddiqui Def 5 的版本正确:\(\pre v=\pre v'\wedge h(v)=h(v')\Rightarrow v=v'\)。照 FoldA 字面实现会禁止"同一组条件上的两个不同选择分支",属笔误,以 Siddiqui/ERV 原始定义为准。
- **配置与割**(FoldA Def 7):\(C\subseteq E\) 因果封闭(\(\forall e\in C,e'<e\Rightarrow e'\in C\))且无冲突。割 \(\mathit{Cut}(C)=(\mathit{Min}(O)\cup C^\bullet)\setminus{}^\bullet C\);对应原网 marking \(\mathit{Mark}(C)=p(\mathit{Cut}(C))\)。\(\uparrow C\) 为 C 之后仍可能的"未来"子网。**配置 ↔ 偏序 run 一一对应,这是整个方法的语义支点。**
- **局部配置**(FoldA Def 10 / Siddiqui Def 6):\([e]=\{e'\mid e'\le e\}\)——使 e 可发生的最小事件集;其对应的因果网叫**局部分布式 run**(Siddiqui Def 7:\(B_e=\{c\mid(c,e)\in F^*\},E_e=[e]\))。
- **配置代价**:FoldA Def 11:\(Z([e],\zeta)=\sum_{e'\in[e]}\zeta(p(e'))\);Siddiqui Def 11 记 \(s(C)=\sum_{e\in C}cost(h(e))\),并指出单调性 \(C\subseteq C'\Rightarrow s(C)\le s(C')\)(代价非负 ⇒ 显然)。
- **充分序**(FoldA Def 12,源自 ERV):有限配置上的偏序 \(\prec\) 满足 ① well-founded;② \(C_1\subset C_2\Rightarrow C_1\prec C_2\);③ 被有限扩展保持——若 \(C_1\prec C_2\) 且 \(\mathit{Mark}(C_1)=\mathit{Mark}(C_2)\),则同构 \(I_1^2\) 下 \(C_1\oplus E\prec C_2\oplus I_1^2(E)\)。
- **cut-off 事件**(FoldA Def 13):\(e\) 是 cut-off,若存在 \([e']\) 使 \(\mathit{Mark}([e])=\mathit{Mark}([e'])\) 且 \([e']\prec[e]\)——该支到达的 marking 已被"更小"配置代表,停止扩展。cut-off 机制是有限完整前缀存在的原因(McMillan;循环/无界行为在此被截断)。

---

## 2 "折叠"机制辨析(FoldA 之名与 cut-off 的角色)

任务书要求拆"folding 机制",需先正名:**两文的核心操作是 unfolding(展开)**——把系统网摊开成无后向冲突的出现网,使并发/冲突/因果三关系显式化。论文未解释 "FoldA" 命名来源(合理推断为 unFOLDing Alignments 的缩合;原文无说明,此处标注为推断)。档案约定:

- **展开(unfold)**:同步积 → 分支过程。行为不减,交织被压缩(一个配置代表其全部线性化)。
- **可称"折叠"的两处**:① **cut-off 截断**——marking 重复处停止展开,等价于把无限展开"折回"到已见 marking(循环行为折叠为有限前缀);② **配置对交织的商**——\(k!\) 条交织折叠为 1 个偏序 run。这两处"折叠"正是复杂度收益的来源;而 possible-extensions 计算是为此支付的代价(见 §4.3)。

---

## 3 算法主体

### 3.1 FoldA:Algorithm 1(有向展开,一体两版 FoldAn/FoldAh)

标准代价(Algorithm 1 第 1 行):

\[
\zeta(t)=\begin{cases}0 & t\ \text{为同步 move}\\ 1 & t\ \text{为 model 或 log move}\\ 0.0001 & t\ \text{为 silent}\end{cases}
\]

主循环(伪代码在 HTML 中行序有乱,以下按正文叙述复原意图;08-22 已核:复原序与 arXiv v1 现行 HTML Algorithm 1 逐条吻合):

1. \(sp\gets N_l\times N_m\);初始化分支过程 \(\beta\)(为 \(im\) 的每个 place 建初始条件);计算 possible extensions \(pe\);cut-off 集与 \(\delta\) 置空。
2. **while \(pe\neq\emptyset\)**:取 \(Z([e],\zeta)\) 最小的扩展事件 \(e=(t,X)\)(X 为输入条件集);
3. 若 \([e]\cap\textit{cutoff}=\emptyset\):把 \(e\) 及其后集条件加入 \(\beta\);
4. 若 \(\exists x\in\beta:\mathit{Mark}([x])=\mathit{fm}\):\(\delta\gets[x]\),**break**(第一个到达终态的配置即最优);
5. 否则重算 \(pe\);若 \(e\) 是 cut-off 则记入 cutoff 集;从 \(pe\) 移除 \(e\);返回 2。

充分序实现:\(e\prec e'\) iff \(Z([e],\zeta)\le Z([e'],\zeta)\),**平局用 Python 内建 `id()`(内存地址)打破**——保证全序化,但跨运行不确定(T2 复算性硬伤,04 §5.4)。工程优化:\(pe\) 用优先队列;事件按 marking 建索引加速 cut-off 检测;每事件缓存局部配置与代价。此版称 **FoldAn**(naive,Dijkstra 式)。

**FoldAh**(§4.2):改用 \(Z([e],\zeta)+h_{sp}(\mathit{Mark}([e]))\) 排序,\(h\) 为解同步积 marking equation 最小代价的经典下界(Adriansyah Thm 4.4.8/4.4.9);A\* 式。论文补证了该启发式在有向展开中仍有效(Thm 4.2/4.3,推导展开见 04 §3)。

**正确性定理**(Thm 4.1,原文四点):算法返回的 \(\delta\)(由最优配置 \([e]\) 定义)满足 (1) 对应 \(sp\) 从 \(im\) 到 \(fm\) 的合法 firing sequence;(2) 若合法 alignment 存在,展开包含之且算法必找到(完备);(3) \(\delta\) 在全体合法 alignment 中代价 \(Z\) 最小(最优);(4) 终止。证明骨架:(1) 由分支过程定义(只加使能转移);(2)(4) 由 easy sound 性 + Adriansyah Thm 4.3.4/Lemma 4.4.1(\(fm\) 在 \(sp\) 中可达 ⇒ 在 \(\beta\) 中可达);(3) 配置按代价递增探索、取第一个到达 \(fm\) 者(Dijkstra 不变式;逐步复推见 04 §2)。

### 3.2 Siddiqui:UnfoldSyncNet(\(ERV[\triangleleft_c]\) / \(ERV[\triangleleft_h]\))

输入扩展同步积 \(SN_\otimes^{ext}\) 与布尔旗 \(stopAtFirst\);输出 alignmentRuns 与 lowestCost。与经典 ERV 的差异:优先队列按 \(\triangleleft_c\) 排序;弹出事件 \(e\) 若 \(h(e)=t^*\)(目标事件)→ 存其局部分布式 run,记录 \(s([e])\);\(stopAtFirst\) 为真即停(单个最优),为假则继续(**枚举全部最优 alignment run**——比 FoldA 多出的能力);其余为标准 ERV:cut-off 检查经 marking 查找表 \(imarks\)(O(1)),非 cut-off 则扩展后集条件、重算 possible extensions。作者点名 **possible extensions 计算是实现关键**(需找两两并发且无因果/冲突关系的条件组合),沿用 Römer 2000 博士论文的数据结构优化。

**代价充分序**(Def 13,\(C\triangleleft_c C'\) iff):
1. \(s(C)<s(C')\);或
2. \(s(C)=s(C')\) 且 \(|C|<|C'|\);或
3. \(s(C)=s(C')\)、\(|C|=|C'|\) 且 \(\phi(C)\) 按入队序 \(\gg\) 字典序更小。

\(\triangleleft_c\) 是严格偏序且**充分**(Thm 0.B.1,附录全证,逐步复推见 04 §3.2)。

**启发式版**(Def 14):\(f(C)=s([e])+est(C)\),\(est\) 用 marking equation 下界;\(C\triangleleft_h C'\) iff \(f(C)<f(C')\),平局回退 \(\triangleleft_c\)。由 Bonet et al. 2008:\(s\) 单调 + \(est\) 可采 ⇒ \(\triangleleft_h\) 属**半充分序**族,cut-off 判据不变仍正确。

**结果读出**(§3.4,两步):① 最优 alignment run 去掉 \(e^*\),事件↦move 节点、条件↦依赖边(按来源分 log/model 依赖)→ **最优 alignment order** \(G_\varphi^{opt}\);② 分解 \(G_\varphi^{opt}\to G^{opt}_{\varphi\downarrow1}\biguplus G^{opt}_{\varphi\downarrow2}\)(日志侧与模型侧偏序,同步节点拆开并登记 \(\varphi\))→ u-alignment;\(G^{opt}_{\varphi\downarrow1}\) 与输入 p-trace 同构(sanity 保证)。
**偏差四象限**(在传递归约 \(G^-\) 上):
- **missing dependencies**:\((m_1,m_2)\in\prec^{opt-}_{\varphi\downarrow1}\setminus\prec^{opt-}_{\varphi\downarrow2}\)(日志有此依赖、模型无);**missing events**:log move \((m_1,\gg)\);
- **undesired dependencies**:\((m_1,m_2)\in\prec^{opt-}_{\varphi\downarrow2}\setminus\prec^{opt-}_{\varphi\downarrow1}\)(模型有、日志无);**undesired events**:model move \((\gg,m_2)\)。
⚠ 勘误:原文第 2 类的文字段落("Events and dependencies in the log but not in the model…")是第 1 类的复制粘贴笔误,以上按其形式化关系式与图例(蓝=模型侧)修正。⚠ 命名方向注意:此处 missing/undesired 是**以模型为被评对象**(Cortado 是发现工具,模型待修);T2 以安全性质网为基准评轨迹,方向要翻转(映射表见 04 §5.2)。

### 3.3 两套算法对照

| 维度 | FoldA | Siddiqui |
|---|---|---|
| 输入 | 主文:全序 trace(附录 0.A 示例偏序);构造 event net | 原生 p-trace(DAG)→ trace net |
| 终态编码 | dummy end 事件 | 目标变迁 \(t^*\)+place \(p^*\)(Def 9,更规范) |
| 充分序 | \(Z\le\) + `id()` 平局(未给充分性证明,引 ERV 概念) | \(\triangleleft_c\) 三级平局 + 充分性全证(Thm 0.B.1) |
| 启发式 | marking equation;自证在展开中可用(Thm 4.2/4.3) | marking equation;引 Bonet 半充分序定理 |
| 输出 | 最优配置=偏序 alignment(出现网形态) | u-alignment(双偏序+对齐函数)+ 偏差四象限 + chevron 可视化 |
| 多解 | 返回一个 | \(stopAtFirst\)=false 可枚举全部最优 |
| 模型假设 | 1-safe、easy sound,**支持无界 easy sound 网**(附录 0.A.2) | 1-safe、easy sound |
| 工具 | 独立仓库(基于 PM4Py) | 集成进 Cortado(替换其"全序列化+逐条对齐再聚合"的旧法) |

---

## 4 复杂度

- **无闭式复杂度**,两文皆然。理论锚点:可达性相对前缀大小 NP-complete(Esparza & Schröter 2001,Siddiqui §1 引);前缀通常远小于可达图(McMillan/ERV);瓶颈在 possible-extensions 枚举(组合性,Römer 优化可缓解不可消除)。
- **FoldA 经验复杂度**(实验 1,485 合成模型 24,250 traces,单偏差注入,100s/trace 上限):#VS(visited states)随 #SPT(同步积转移数)**近线性**,但系数随偏差位置(FoldAn)与模型类型漂移;**时间随 #VS 多项式/指数**(分支过程越大、单步扩展检查越贵——这是与传统方法本质不同的成本结构)。FoldAn 对"偏差靠后"极敏感(回溯),FoldAh 用启发式抹平了偏差位置的影响,但**无偏差 case 的最大耗时从 2.98s 恶化到 70.44s**(启发式本身要解 LP/marking equation)。嵌套选择(EN)最伤;并发(C/CN)在启发式下与浅结构相当。
- **FoldA 回归分析**:\(\ln(ET)\) ~ 前置指标:adj \(R^2=0.770\),系数 #SPT 2.891、choice factor(place 平均出度)0.715、concurrency factor(transition 平均出度)−0.161;加后置指标:adj \(R^2=0.970\),#SPT 1.288、ln(#VS) −0.399、ln(#QS) 2.271——**排队多而访问少 = 有向搜索失效**的代理指标。
- **给 T2 的可移植结论**:①同步积规模(≈模型转移数+轨迹长度+标签匹配对数)是第一预测子——LLM 轨迹长、重复标签多时同步对 \(SM\) 膨胀,需在活动映射层控制;②选择度是敌人、并发度不是——发现层(IM)产出模型的选择度应被监控为检查层性能的前置指标。

---

## 5 评测

### 5.1 FoldA

- **可行性(Sepsis,1050 traces,IM 完美拟合模型)**:三法代价一致(都最优);FoldAn **中位数** 0.023s vs Dijkstra 7.425s、A\* 0.614s——但**极端长尾**:FoldAn 最大 2702s(A\* 25s,Dijkstra 87s),均值 5.43s vs A\* 0.69s。中位数叙事与均值叙事相反,读结果必须两个都看。
- **实验 2(19 log-model 对:7 真实日志 × IM(噪声 0.2;SP 用 0.5)/Split Miner + 6 个 ITL 基准模型 [275–429 转移];大日志采样 1000 traces,100s/trace)**:
  - 时间:**A\* 全胜**(省 71.45%–99.11%);Dijkstra 13/19 更快(省 38.64%–99.27%)。
  - 排队状态:A\* 在 15/19 上比 FoldAh 多排 22.73%–578.80%;Dijkstra 全部更多,最高多 **118,318.48%**。
  - 访问状态:A\* 16/19 更少(0.80%–59.89%);Dijkstra 14/19 更多。
  - 超时:FoldAh 在 ITL prCm6 仅完成 328/500、BPIC17 完成 679/1000(Table 2;正文作 697,数字不一致,疑笔误),而 A\*/Dijkstra 基本全完成;SP/SP_SPLIT 均值 0.204/0.895s 但最大 93.4/99.99s。
  - 诚实结论(§6):时间上不敌 A\*/Dijkstra,赢在排队状态少、并发表示保真、且保留依赖为高级代价函数/增量/并行计算留口。
- **ITL prDm6/prEm6/prFm6 上 Dijkstra 全灭(0 完成)而 FoldAh 完成 732/1200、1200/1200、686/1200**——大模型上 unfolding 反而比无启发式可达图搜索更能活下来,这一格常被忽略,对 T2 的"大策略网"场景是正面证据。

### 5.2 Siddiqui

- **合成(8 棵过程树,块结构无循环无重复标签,并发度 0%–70%;每网模拟 500 traces;注入 0%–50% 噪声;对照 Classic PA=Lu et al. 2014 的 A\* 两步法,作者自己实现于 classic-pa 仓库〔08-22 已核:仓库存活;其自述为 "ILP-based A*" 经典实现,"=Lu 两步法"系方法级归类〕)**:并发 70% 时 \(ERV[\triangleleft_h]\) 全面最优;\(ERV[\triangleleft_c]\)(无启发式)在 50% 起就因前缀膨胀掉队;30% 时三者接近,高噪声段 ERV 系占优。**支持核心假设:并发越高,交织枚举的开销增长快于扩展计算的开销。**
- **真实(BPIC12:262,200 事件/13,087 案例/4,366 变体,含 start+end 时间戳——正因如此才能构造 p-trace;IM 噪声阈 0.05 与 0.5 两个模型,ECyM 1899/289;3s/trace 超时)**:偏差代价越高运行时近指数增长;低代价段 Classic PA 快;0.05 模型高代价段 \(ERV[\triangleleft_h]\) 更稳,总时间差约 130s;\(ERV[\triangleleft_c]\) 高阈值下频繁超时。0.5 模型上 Classic PA 全段更快(作者解释:非同步转移多 → 等代价事件多 → 前缀变宽)。
- **工具**:Cortado 的 conformance 界面新增三态判定(fit / 不 fit / **fit 但有序偏差**——第三态是其贡献)、缺失事件条纹高亮、缺失/多余依赖成对列出。

### 5.3 评测口径的批判性备注

- 两文的"真实"实验都只在**业务过程日志**上;无任何 agent/软件轨迹。T2 引用时不得暗示其在 agent 域已验证。
- Siddiqui 合成实验**无循环**(FoldA §2 点名此弱点);其真实实验仅 1 个日志。FoldA 的 485 模型含循环(L 型)但单文只注入"删除单事件"型偏差(无插入/替换,作者自认因组合爆炸)。**"插入型偏差 + 循环 + 高并发"三者同时出现的区域两文都没测**——恰是 LLM-MAS 轨迹的常态,T2 实验设计应补此格。
- FoldA 基线用 PM4Py 同栈实现(控制了语言/预处理变量,方法学干净);Siddiqui 的 Classic PA 是自己复刻的(潜在实现偏差,作者未报告校验)。

---

## 6 局限清单

**论文自认**:FoldA——时间劣于 A\*/Dijkstra;对模型结构(选择)与偏差位置敏感;启发式在无偏差 case 上有额外开销;未来需面向分支过程的专用启发式。Siddiqui——\(ERV[\triangleleft_c]\) 无启发式不实用;低并发下扩展计算开销高;未来做启发式与缓存优化。

**本档案补充(引用时须注意)**:
1. 离线、单案例(per-case)算法;无在线/增量版本(FoldA 结论说"可容易改造",未做)。
2. 1-safe 假设贯穿;策略网若含多 token 计数语义需先检查。
3. 代价函数固定为标准型;安全加权代价的最优性虽由同一定理覆盖(定理只要求非负可加),但两文均未实验非标准代价。
4. FoldA `id()` 平局 ⇒ 等代价多解时结果跨运行不稳定;Siddiqui 的第三键(入队序)依赖扩展枚举顺序,复算性同样未被论证。
5. 标签完全匹配假设;无噪声标签/近似匹配机制。
6. 无任何统计保证叙事(与 ProbGuard 的 PAC 对照):这里的保证是**精确算法的最优性/完备性**,前提是输入(模型、轨迹、代价)无误——输入错误不在界内,与 T2 §4-4(b) 的措辞义务一致。

---

## 7 与 T2 的接口摘要(详细改造清单见 04 §5)

- 直接复用:同步积构造、\(t^*/p^*\) 终态编码、\(\triangleleft_c\)/\(\triangleleft_h\) 充分序机械、cut-off、marking-equation 启发式、u-alignment 分解与偏差四象限。
- 必须改造:p-trace 构造(时间戳→correlation_id/消息因果)、活动标签映射层、确定性 tie-break(证据可复算)、安全加权代价函数、循环+选择混合结构的性能预算、per-case 概念(interaction graph 定义案例边界)。
- 不复用:chevron 可视化(Cortado 专属,可选)、两文评测 harness。
