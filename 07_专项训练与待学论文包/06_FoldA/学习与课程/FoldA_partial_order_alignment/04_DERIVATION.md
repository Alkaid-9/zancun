# DERIVATION — 代价函数与最优性保证逐步推导 + 偏序/全序语义差异形式化 + T2 复用改造点

**日期**:2026-08-13 ｜ 公式以 arXiv:2506.08627(FoldA)与 arXiv:2504.00550(Siddiqui)HTML 全文为准。
**标注约定**:〔原文〕= 论文陈述照录;〔复推〕= 按原文思路逐步展开;〔档案推导〕= 本档案读者自行补全/发现,非论文声明,复现时需核验。

---

## 1 符号与代价函数的三个记法(先统一账本)

同一个代价,三处记法(对照表):

| 层 | FoldA | Siddiqui | 含义 |
|---|---|---|---|
| move/转移代价 | \(\kappa(e,t)\)(Def 2)、\(\zeta(t)\)(Alg 1) | \(cost(h(e))\)(Def 11) | 同步积单个转移的代价 |
| 配置代价 | \(Z([e],\zeta)=\sum_{e'\in[e]}\zeta(p(e'))\)(Def 11) | \(s(C)=\sum_{e\in C}cost(h(e))\)(Def 11;附录又记 \(lc\),命名不一致) | 配置=偏序 run 的总代价 |
| alignment 代价 | \(\kappa(\gamma)=\sum_{(e,t)\in\gamma}\kappa(e,t)\) | \(s([e^*])\) | 最终返回值 |

**标准代价**〔原文,FoldA Alg 1 / Siddiqui Def 11〕:

\[
\zeta(t)=\begin{cases}
0 & t\text{ 为同步 move}\\
1 & t\text{ 为 log 或 model move}\\
0.0001\ (\text{Siddiqui: 可忽略正值}) & t\text{ 为 silent}
\end{cases}
\]

三条结构性质(一切保证的地基):
- **P1 非负**:\(\zeta\ge0\);
- **P2 可加**:配置代价 = 成员事件代价之和;推论 \(s(C\oplus E)=s(C)+s(E)\)(Siddiqui 附录用到);
- **P3 单调**:\(C\subseteq C'\Rightarrow s(C)\le s(C')\)(P1+P2 直接得,Siddiqui Def 11 明示)。

〔档案推导〕**silent 代价为什么是"可忽略正值"而不是 0**:(i) 若 silent=0 且模型含 silent 环,会出现无穷多同代价配置,FoldA 的 \(\le\)+`id()` 序在第一键上失去分辨力,井然性(well-foundedness)只能靠平局键兜底;\(\triangleleft_c\) 因有 \(|C|\) 第二键天然免疫,但 \(\varepsilon>0\) 让两文的序在第一键就严格递增,更干净;(ii) \(\varepsilon>0\) 使等偏差解中偏向"绕行 silent 最少"的最短解释——对 T2 的"最小证据"叙事正中下怀(证据里不含无谓路由)。

---

## 2 最优性保证:从代价序到"第一个弹出即最优"

### 2.1 定理原文

**FoldA Thm 4.1**〔原文〕:算法返回的 \(\delta\)(= 分支过程 \(\beta\) 中最优配置 \([e]\))满足:(1) 对应同步积 \(sp\) 从 \(im\) 到 \(fm\) 的合法 firing sequence(**有效**);(2) 若合法 alignment 存在,展开包含之且算法必找到(**完备**);(3) \(\delta\) 在全体合法 alignment 中最小化 \(Z([e],\zeta)\)(**最优**);(4) **终止**。

原文证明各一句话:(1) 分支过程只添加使能转移;(2)(4) 由 easy sound + Adriansyah 论文 Thm 4.3.4/Lemma 4.4.1(\(fm\) 在 \(sp\) 中可达 ⇒ 在 \(\beta\) 中可达);(3) "按代价递增探索配置、取第一个到达 \(fm\) 者"。下面把 (3) 与被一笔带过的 cut-off 安全性逐步展开。

### 2.2 Dijkstra 不变式〔复推〕

设优先队列按序 \(\prec\)(第一键为配置代价 \(s\),启发式版见 §3.3)弹出扩展事件;\(e^*\) 为**第一个**弹出的目标事件(\(h(e^*)=t^*\),或 FoldA 的 \(\mathit{Mark}([x])=fm\))。断言:\(s([e^*])\) 是全体 alignment run 代价的最小值。

1. 任取另一 alignment run,以目标事件 \(e'\) 收尾。由 **P3**,\([e']\) 的任一前缀配置代价 \(\le s([e'])\)。
2. 反设 \(s([e'])<s([e^*])\)。考察算法运行:\([e']\) 的事件按因果序逐个成为 possible extension;每个这样的扩展事件 \(g\) 满足 \([g]\subseteq[e']\),故 \(s([g])\le s([e'])<s([e^*])\)。
3. 优先队列总是弹出当前 \(\prec\)-最小者,而 \(e^*\) 弹出时其键值为 \(s([e^*])\);键值更小的 \([e']\) 家族事件(除非被 cut-off 截断,见 §2.3)必然**先于** \(e^*\) 全部弹出——归纳到 \(e'\) 自身:\(e'\) 先于 \(e^*\) 弹出,与"\(e^*\) 是第一个目标事件"矛盾。
4. 故 \(s([e^*])\le s([e'])\) 对一切 alignment run 成立。∎
5. **终止**:easy sound ⇒ 目标 marking 可达 ⇒ 展开中存在目标事件;序井然(P1 + 平局键)且每次弹出严格消耗队列、cut-off 截断保证前缀有限(ERV 经典结论),故目标事件在有限步内弹出。

关键依赖:P1(键值非负,井然)、P3(前缀不比整体贵)、以及第 3 步暗用的"**先弹出者不被其超集反超**"——即充分序第 ② 性质 \(C_1\subset C_2\Rightarrow C_1\prec C_2\)。三者缺一,不变式即破。

### 2.3 cut-off 安全性:截断为何不丢最优〔复推〕

设 \(e\) 被判 cut-off:存在 \(e'\),\(\mathit{Mark}([e])=\mathit{Mark}([e'])\) 且 \([e']\prec[e]\)。要证:删掉 \([e]\) 之后的所有延伸,不影响最优值。

1. 任何经过 \([e]\) 到达终态的完整 run 形如 \([e]\oplus E\)。
2. 由 \(\mathit{Mark}\) 相同,充分序第 ③ 性质给出同构 \(I\):\([e']\oplus I(E)\) 也是合法配置、同样到达终态,且 \([e']\oplus I(E)\prec[e]\oplus E\)。
3. **代价不增**:同构扩展保标签(经同态 \(h\))⇒ 保代价,\(s(I(E))=s(E)\);又 \([e']\prec[e]\) 在代价第一键序下蕴含 \(s([e'])\le s([e])\)。由 P2:
\[
s([e']\oplus I(E))=s([e'])+s(E)\ \le\ s([e])+s(E)=s([e]\oplus E).
\]
4. 故被截断支上的每个解都有不劣的镜像解存活于保留支;嵌套 cut-off 情形由性质 ③ 的"扩展保序"归纳保持(此即 ERV 修正 McMillan 的核心,FoldA §2 转述)。∎

〔档案推导〕注意第 3 步需要"\(\prec\) 蕴含代价 \(\le\)"——对 \(\triangleleft_c\)(第一键即 \(s\))和 FoldA 的 \(Z\)-序均成立;若 T2 改造代价序(§5),此蕴含必须重新检查,否则 cut-off 会剪掉真最优。

---

## 3 充分序验证

### 3.1 FoldA 的序:\(e\prec e'\iff Z([e],\zeta)\le Z([e'],\zeta)\),`id()` 破平〔原文+档案批注〕

- 三性质核查:① 井然——\(Z\ge0\) 且 silent \(\varepsilon>0\) ⇒ 无无穷下降链;② \(\subset\)-单调——\(C_1\subset C_2\Rightarrow Z(C_1)\le Z(C_2)\)(P3),在 \(\le\) 序下成立;③ 扩展保持——同构扩展等代价。
- 〔档案批注〕形式瑕疵两处:(a) 以 \(\le\) 定义的关系是全预序而非(严格)偏序,充分序定义(Def 12)按惯例作用于严格序;`id()` 平局把它全序化后回到正轨,但 **`id()` 是 Python 内存地址,跨运行不可复现**——最优值不受影响(任一等代价解都最优),返回的具体 alignment 可漂移;(b) 论文未对该序显式验证充分性三条(引用 ERV 概念了事),严格版可直接换用 Siddiqui \(\triangleleft_c\)(证明齐全)。

### 3.2 Siddiqui Thm 0.B.1:\(\triangleleft_c\) 是充分序〔复推,补细节〕

\(C\triangleleft_c C'\) iff ① \(s(C)<s(C')\);或 ② \(s\) 相等且 \(|C|<|C'|\);或 ③ \(s,|C|\) 均相等且 \(\phi(C)\) 按入队全序 \(\gg\) 字典序更小。

- **井然**:\(s,|C|\in\mathbb{N}_0\) 良基;\(\gg\)(入队先后)良基;字典序组合良基。∎
- **\(\subset\)-单调**:\(C_1\subset C_2\Rightarrow s(C_1)\le s(C_2)\)(P3)。若严格小,键①完成;若相等,\(|C_1|<|C_2|\) 由真包含直接得,键②完成。∎(附录原文在等代价分支同时写了 \(|C_1|<|C_2|\) **and** \(\phi(C_1)\gg\phi(C_2)\)——第二个条件多余,行文冗余无害。)
- **扩展保持**:设 \(\mathit{Mark}(C_1)=\mathit{Mark}(C_2)\)、\(C_1\triangleleft_c C_2\),\(E_1\) 与 \(E_2=I_1^2(E_1)\) 同构扩展。同构经同态保标签 ⇒ \(s(E_1)=s(E_2)\)、\(|E_1|=|E_2|\);可加性 \(s(C\oplus E)=s(C)+s(E)\)。三 case:
  1. \(s(C_1)<s(C_2)\):两边同加 \(s(E)\),键①保持;
  2. \(s\) 等、\(|C_1|<|C_2|\):代价仍等、大小仍严格小,键②保持;
  3. \(s,|C|\) 均等、\(\phi(C_1)\gg\phi(C_2)\):代价与大小仍等;原文称"由字典序性质"\(\phi(C_1\oplus E_1)\gg\phi(C_2\oplus E_2)\)。〔档案批注〕这一步严格成立还需"扩展事件的入队次序与两侧配置的既有字典序相容"这一实现约定,原文未展开;工程上入队序由扩展枚举顺序决定——**T2 复算性改造正落在此键上**(§5.4)。∎(带上述标注)

### 3.3 启发式有向化:\(f(C)=s([e])+est(C)\)

- \(est\) = 解同步积 **marking equation** 的最小代价(线性松弛下界;两文同引 Adriansyah Thm 4.4.8/4.4.9)。
- Siddiqui Def 14:\(C\triangleleft_h C'\) iff \(f(C)<f(C')\),平局回退 \(\triangleleft_c\)。〔原文〕引 Bonet et al. 2008:\(s\) 单调 + \(est\) 可采(admissible)⇒ \(\triangleleft_h\) 属**半充分序**族,cut-off 判据不变仍正确(Bonet 原文未打开,此处系转述 Siddiqui)。
- FoldA Thm 4.2〔原文〕:\(\forall e\in E,\exists s\in RG(N):h(\mathit{Mark}([e]))=h(s)\)——启发式只依赖 marking,展开中的取值与可达图一致(平凡但必要:说明经典下界可直接搬)。
- FoldA Thm 4.3〔原文+复推〕:证 \([e_1]\subset[e_2]\Rightarrow Z([e_1])+h(M_1)\le Z([e_2])+h(M_2)\)(即 ⊂-单调对 \(f\) 成立;\(M_i=\mathit{Mark}([e_i])\))。反证:设 \(>\) 成立。记 \(E_d=[e_2]\setminus[e_1]\),由可加性 \(Z([e_2])=Z([e_1])+Z(E_d)\),代入得
\[
h(M_1)\ >\ Z(E_d)+h(M_2).
\]
原文由此收束:"存在从 \(M_1\) 经 \(E_d\)、\(M_2\) 到 \(fm\) 的更便宜路径,与 \(h\) 是下界矛盾"。

### 3.4 〔档案推导〕原文证明的一处跳步:admissible ≠ consistent

严格看,\(h(M_2)\) 是 \(M_2\to fm\) 的**下界**而非真实代价:可采性只给 \(h(M_1)\le Z(E_d)+opt(M_2\to fm)\),而 \(opt\ge h(M_2)\),故 \(h(M_1)>Z(E_d)+h(M_2)\) **并不直接**与可采性矛盾。补全所需的是更强的**一致性(consistency/单调性)**:对任意真实可行段 \(E_d\):\(h(M_1)\le Z(E_d)+h(M_2)\)。

marking-equation 启发式确实一致,一行证明:\(h(m)=\min\{\zeta^{\mathsf T}x:\ \mathbb{C}\,x=fm-m,\ x\ge0\}\)(\(\mathbb{C}\) 为关联矩阵)。若 \(m\xrightarrow{E_d}m'\),则 \(m'-m=\mathbb{C}\,x_{E_d}\);对 \(m'\) 的任意可行解 \(x'\),\(x'+x_{E_d}\) 是 \(m\) 的可行解,代价 \(Z(E_d)+\zeta^{\mathsf T}x'\)。取下确界得 \(h(m)\le Z(E_d)+h(m')\)。∎

**结论**:Thm 4.3 成立,但论证依赖一致性而非单纯可采性;FoldA 的表述有跳步(把"下界"当"真实代价"用了)。Siddiqui 经 Bonet 半充分序定理绕开了这个坑。**T2 若换启发式(如安全加权代价下重解 LP),必须验证一致性而不只是可采性,否则 ⊂-单调破、cut-off 可能剪掉最优。**〔此为本档案读者推导;复现窗对照 Bonet et al. 2008 原文核验〕

---

## 4 偏序 vs 全序 alignment:语义差异形式化

### 4.1 对象定义对照(2×2 输入/输出矩阵)

|  | 输出全序 | 输出偏序 |
|---|---|---|
| **输入全序 trace** | 经典 alignment(Adriansyah):\(\gamma\in(\text{moves})^*\) | FoldA 主文:最优配置=偏序 alignment \(\delta\) |
| **输入偏序 p-trace** | Cortado 旧法:枚举全部全序化、逐条对齐、聚合 | Siddiqui:u-alignment \((\rho_c,G_\mathcal{N},\varphi)\);FoldA 附录 0.A |

形式差异一句话:\(\gamma\) 是 move 上的**全序**(序列);\(\delta\) 是同一合法性条件((1) 投影得轨迹 (2) 投影是模型 occurrence sequence (3) 无 \((\gg,\gg)\))下 move 上的**严格偏序**;u-alignment 再把 \(\delta\) 结构化为"日志偏序 ⊎ 模型 run 偏序 + 同步单射 \(\varphi\)",并要求合并同步节点后无环(Def 8 条件 2,排除对齐制造因果环)。

### 4.2 引理 L1(代价对线性化不变)〔档案推导,由定义直接得〕

\(\kappa(\gamma)=\sum_{(e,t)\in\gamma}\kappa(e,t)\) 只依赖 move **多重集**。故对偏序 alignment \(\delta\) 的任意两个线性化 \(\gamma_1,\gamma_2\in\mathit{Lin}(\delta)\):\(\kappa(\gamma_1)=\kappa(\gamma_2)=\kappa(\delta)\)。**代价函数对序结构是盲的。**

### 4.3 命题 P1(标准代价下,最优值不因偏序化而改变)〔档案推导〕

**全序输入情形**:\(\min_{\gamma}\kappa=\min_{\delta}\kappa\)。
证明骨架:(≤)任一偏序 alignment \(\delta\) 的线性延拓 \(\gamma\) 合法(轨迹侧受 \(\sigma\) 全序约束,延拓投影仍为 \(\sigma\);模型侧延拓是合法 occurrence sequence——配置的任意线性化都是 firing sequence,展开语义经典结论),且 \(\kappa(\gamma)=\kappa(\delta)\)。(≥)任一全序 \(\gamma\) 经 Lu et al. 2014 的回放-展开构造诱导偏序 \(\delta_\gamma\),move 集不变,代价相等。∎

**偏序输入情形**:\(\min_{\delta}\kappa=\min_{\sigma'\in\mathit{Lin}(\rho_c)}\ \min_{\gamma\ \text{对}\ \sigma'}\kappa\)。
证明骨架:(≤)对最优的全序化-对齐对 \((\sigma'^*,\gamma^*)\),诱导偏序 alignment 代价相等且轨迹侧与 \(\rho_c\) 相容(全序化只加边不删边,\(\gamma^*\) 的日志 move 序 refines \(\rho_c\));(≥)最优 \(\delta^*\) 的任一线性化给出某个 \(\sigma'\) 上的合法 \(\gamma\)。∎
推论:**Cortado 旧法(枚举全部全序化取优)与一步 unfolding 的最优值相同,差别全在计算量与返回对象的结构**——全序化枚举最坏 \(|\mathit{Lin}(\rho_c)|\) 次对齐(反链宽 \(k\) 时達 \(k!\) 级),unfolding 一次完成。

### 4.4 那"偏序更优"到底优在哪?(FoldA Fig 1 反例的精确读法)〔档案推导,重要〕

P1 说明:**优势不在代价值**。差异在三个层面:

1. **返回对象携带依赖结构** ⇒ 依赖偏差可定义。Siddiqui 四象限中的 missing/undesired **dependencies**(传递归约上的依赖差集 \(\prec^{opt-}_{\varphi\downarrow1}\setminus\prec^{opt-}_{\varphi\downarrow2}\) 及反向)在全序 \(\gamma\) 上根本无法定义——全序化把 \(m\|m'\) 强行压成 \(m<m'\),信息损失恰为"被强加的序对"集合,不可逆。
2. **等代价最优解间的诊断非唯一性**(Fig 1 的真正要害):模型两分支(一支 A、B 顺序,一支 A、B 并发)与"A、B 并发"的轨迹对齐,\(\gamma_1\)(并发支)与 \(\gamma_2\)(顺序支)**等代价**;两步法(Lu 2014)任选其一,若选 \(\gamma_2\),偏序化后报出"模型 A→B、轨迹 A‖B"的依赖偏差,而 \(\gamma_1\) 支无此偏差——**依赖偏差的报告内容取决于选了哪个等代价解,而两步法无任何准则**。
3. **诚实边界**〔档案推导,勿被论文标题带偏〕:标准代价下,unfolding 法**同样**在等代价配置间任选(FoldA 靠 `id()`,Siddiqui 靠入队序)!它相对两步法的实质改进是:(a) 搜索空间(配置)中"并发支/顺序支"是**不同对象**,区分度存在;(b) Siddiqui 的 \(stopAtFirst=\mathrm{false}\) 可**枚举全部最优 alignment run**,把选择权交给后处理;(c) FoldA 结论明言"保留依赖使未来可设计更高级代价函数"。**把依赖偏差纳入优化目标(依赖感知代价)两文都没做**——依赖差集不是事件可加量,塞进 \(s(C)=\sum_e cost(h(e))\) 需要新的可加化技巧(或牺牲充分序),这是真开放问题,也是 T2 可认领的形式化贡献点(见 §5.2-③)。

### 4.5 搜索空间语义对照(为什么免交织)

- 可达图:节点=交织后的 marking;\(k\) 个并发事件的行为段贡献最多 \(k!\) 条路径、\(2^k\) 个中间 marking。
- 分支过程:并发保持为 \(\|\)(无分支)、选择保持为 \(\#\)(条件分叉);同一行为段是**1 个**含 \(k\) 事件的配置;其全部交织=该配置的线性化集,不被枚举。
- 配置 \(C\leftrightarrow\) 偏序 run,\(\mathit{Mark}(C)\) 把配置压回 marking——"最短路"从路径空间挪到配置空间,序 \(\prec\) 起 Dijkstra 键作用,cut-off 起访问标记作用。付出的对价:possible-extensions 枚举(找两两并发的条件组合)是组合性的,FoldA 实验 2 的长尾与超时即此(03 §4)。

---

## 5 T2 复用改造点(核心节)

> T2 检查层需求回放(T2 §4-3/4-4):安全策略 PN ↔ 偏序轨迹的**离线最优 alignment**;三类偏差 sound/complete 检出;**最小可复算偏差证据**;保证措辞限定在"精确最优 alignment + 固定代价 + 完整可观测日志"内。

### 5.1 直接复用件(算法层照搬,引用即可)

| # | 组件 | 出处 | 复用方式 |
|---|---|---|---|
| R1 | 同步积构造(标签配对生成 log/model/sync 转移) | FoldA Def 3 / Siddiqui Def 15 | 照搬;T2 的"模型侧"= 安全策略 PN |
| R2 | 目标变迁 \(t^*\)+place \(p^*\) 终态编码 | Siddiqui Def 9 | 照搬(比 FoldA 的 dummy end 更规范,保 1-safe) |
| R3 | 标准代价骨架 {0,1,ε} | FoldA Alg 1 / Siddiqui Def 11 | 作默认;安全加权版见 A5 |
| R4 | 充分序 \(\triangleleft_c\) + cut-off + \(imarks\) O(1) 查表 | Siddiqui Def 13 + Thm 0.B.1 + Alg 1 | 照搬 Siddiqui 版(证明齐全),不用 FoldA 的 `id()` 版 |
| R5 | marking-equation 启发式 \(\triangleleft_h\)/FoldAh | Siddiqui Def 14 / FoldA §4.2 | 照搬;换代价须重验一致性(§3.4) |
| R6 | 最优性定理模板(有效/完备/最优/终止 四点) | FoldA Thm 4.1 | T2 保证条款的证明骨架,前提替换为 T2 假设 |
| R7 | u-alignment 分解 + 偏差四象限(传递归约上) | Siddiqui §3.4 | 三类偏差的形式载体(映射见 5.2) |
| R8 | \(stopAtFirst=\mathrm{false}\) 枚举全部最优 run | Siddiqui Alg 1 | 等代价多解的后选机制(5.2-③ 用) |

### 5.2 T2 三类偏差 ↔ 论文概念映射(**方向翻转警告**)

Siddiqui 的 missing/undesired 以**模型**为被评对象(Cortado 是发现工具,模型待修);T2 以**安全性质网为基准评轨迹**,读法必须翻转:

| T2 偏差(T2 §4-4) | alignment 概念 | Siddiqui 命名 | 证据形态 |
|---|---|---|---|
| ① 缺失偏差:强制步骤(验证/审批)被跳过 | **model move** \((\gg,t)\) | "undesired events"(模型侧多出) | 该 move 事件 + 其局部配置(到此为止的最小因果史) |
| ② 越权偏差:策略外活动/消息出现 | **log move** \((a,\gg)\) | "missing events"(日志侧多出) | 同上 |
| ③ 序/并发违例:跨 agent 交接乱序、未同步并行写 | **依赖差集**:\(\prec^{opt-}_{\varphi\downarrow1}\setminus\prec^{opt-}_{\varphi\downarrow2}\)(轨迹有序、策略无)及反向(策略要求序、轨迹并发/逆序) | missing / undesired **dependencies** | 传递归约上的违例边对 \((m_1,m_2)\) |

③ 的三条注意事项(源自 §4.4 的诚实边界):
- 依赖偏差是**最优 alignment 上的事后诊断**,不在优化目标内;等代价最优解间报告内容可漂移。
- T2 短期方案:R8 枚举全部最优 run,**后选依赖偏差最少者**并在论文中如实声明该准则(可复算:准则确定 + 5.4 的确定性枚举序);
- T2 长期贡献点:**依赖感知的可加代价函数**(把序违例纳入 \(s\))——两文均未做,FoldA 结论留了官方空位;难点是依赖差集非事件可加量,需可加化技巧或放宽充分序框架,属可认领的形式化开放问题。

### 5.3 需改造件(agent 轨迹三座山:并发、循环、LLM 语义)

**A1 偏序来源改造(并发)——Siddiqui Def 1 必须换掉。**
原文 p-trace:\(a\prec b\iff\) end(a) 时间戳 < start(b) 时间戳。LLM-MAS 不适用:异步 agent 无可比时钟,时间重叠≠语义并发。T2 替换定义〔档案草拟,衔接 T2 §4-2〕:
\[
a\prec_{\text{T2}} b\iff a,b\ \text{同 agent 且执行序相邻传递闭包内}\ \lor\ a\ \text{发消息}\ m,\ b\ \text{收}\ m\ (\text{correlation\_id 判定})
\]
取传递闭包,即 Lamport happens-before 的 correlation_id 实现;**未观测因果不补边**(T2 红线),偏序更稀疏 ⇒ 反链更宽 ⇒ 正落在 unfolding 优势区(Siddiqui 并发 70% 实验),但同时放大长尾风险 ⇒ **混合调度**:反链宽度=1 的轨迹段走经典 A\*(PM4Py 现成),宽段走 unfolding;每 trace 设 timeout,超时降级 A\*+全序化(如实标注该 trace 的诊断为全序近似)。

**A2 循环(agent retry/reflection)。**
Siddiqui 合成评测**无循环**(FoldA §2 点名);FoldA 含 L 型模型且支持无界 easy sound 网——循环处理机制(cut-off)本身没问题,但 FoldA 实验 1 显示**嵌套选择(EN)是最大性能杀手**,而 LLM agent 的"重试→反思→改道"结构恰是"循环+选择"混合。T2 对策:发现层(IM→WF-net)监控模型 choice factor(FoldA 回归系数 0.715 的那个指标)作为检查层性能前置预警;策略 PN 侧人工规约时控制选择嵌套深度。

**A3 LLM 活动标签语义。**
同步 move 生成条件是标签相等(\(\lambda_1(t_1)=\lambda_2(t_2)\neq\tau\))。LLM 轨迹活动名(工具名+参数、自由文本)噪声大:匹配漏 ⇒ 本应同步的对儿劣化为 log+model 双罚,**系统性高估偏差**;匹配错 ⇒ 假同步,**漏报偏差**。T2 对策:(i) 在日志层固化活动本体(EvoAgent `process_events.py` 的事件模式 + SAP XES 扩展兼容,T2 §4-1),alignment 只见规范化活动名;(ii) 重复标签(`call_llm` 数十次)会使同步对集合 \(SM\) 膨胀、同步积转移数暴涨(FoldA 回归:#SPT 是时间第一预测子)——用"活动名+会话段索引"细分标签或按 correlation 分段对齐;(iii) 映射层误差**不在任何定理覆盖内**,写进 T2 假设清单(活动映射正确性假设),与 T2 §4-4(c) 的"活动映射假设显式声明"对上。

**A4 确定性 tie-break(证据可复算的工程前提)。**
FoldA `id()`(内存地址)与 Siddiqui 第三键(入队序,依赖扩展枚举顺序)都不保证跨运行一致。T2 的"最小**可复算**偏差证据"要求:固定代价 + 固定算法 + **确定性规范序**。改造:第三键换成"事件的规范编码字典序"(如 \((\zeta,|C|,\) 按 (转移 id, 输入条件规范编码) 递归定义的字符串\()\)),使 \(\triangleleft_c\) 全序化且平台无关;同时 R8 的"枚举全部最优"在规范序下输出稳定,5.2-③ 的后选结果才可复算。〔充分性三性质在换键后需按 §3.2 模板重验:键③只影响平局,井然与 \(\subset\)-单调不受扰,扩展保持需验证规范编码与同构扩展相容——预计成立,复现窗给出形式验证。〕

**A5 安全加权代价。**
T2 需要"强制步骤跳过"比"普通活动跳过"更贵、越权活动按风险分级。推广 \(\zeta:T\to\mathbb{R}_{\ge0}\)(按安全性质网的转移标注加权)。**最优性定理无恙**:§2/§3 全部推导只用了 P1/P2/P3 与"\(\prec\) 第一键=代价",不依赖 {0,1,ε} 具体值。三个检查项:(i) 若给某类 move 代价 0,井然性与"最短解释"语义靠 \(|C|\) 第二键兜底(\(\triangleleft_c\) 天然有);(ii) \(\triangleleft_h\) 的 LP 启发式要在新 \(\zeta\) 下重解且重验一致性(§3.4 的证明对任意非负 \(\zeta\) 逐字成立——marking equation 结构不变);(iii) 保证措辞改为"最小**安全加权**代价解释",权重表进假设清单。

**A6 case 概念与规模控制。**
两文算法都是 per-case(单轨迹)的;T2 的 case = 一次多 agent 任务执行,由 correlation_id/交互图划界(T2 §4-1 现成)。超长轨迹(数百步)对齐可能超时:分段(窗口化)后每段最优 ≠ 全局最优——要么如实声明"分段最优",要么做分解定理(此处与 Lomazova 2020 的组合分解定理有对比义务,T2 §2 已列必引;其定理是全序布尔拟合的分解,T2 若做偏序 alignment 版分解即是增量)。

### 5.4 不复用件

- chevron 可视化与 Cortado 集成(Siddiqui §4):T2 有自己的证据渲染需求(最小证据 = 违例 move/边 + 局部配置 + 代价分解),不搬 UI;
- 两文评测 harness:T2 用自己的偏差注入协议(craft G2 惯例),但**学 FoldA 的偏差位置敏感性设计**(注入在轨迹头/中/尾分桶报告)与 timeout 报告纪律(完成率单列,均值/中位数/最大值三报);
- FoldA 的 `id()` 平局与"以 \(\le\) 定义序"的写法(§3.1 已述形式瑕疵)。

### 5.5 引用义务与差异句(供 T2 行文直接取用)

- 算法层引用链:McMillan 1992(展开)→ ERV 1996/2002(充分序+cut-off)→ Bonet et al. 2008(有向展开/半充分序)→ Lu et al. 2014(偏序 conformance 开题)→ **Siddiqui PETRI NETS 2025(p-trace 一步法+充分序证明+四象限)** + **FoldA BPM 2025(问题陈述+有向展开 alignment+大规模评测)**。
- 差异句模板:"我们**复用** unfolding alignment 的算法内核(FoldA;Siddiqui et al.),贡献在:(1) 偏序来源从时间戳改为 LLM-MAS 消息因果(correlation_id happens-before);(2) 模型侧为**安全性质 Petri 网**而非发现/参照模型;(3) 偏差证据的**确定性可复算**构造(规范序替换实现相关平局)与三类偏差到 alignment 概念的映射;(4) [若做] 依赖感知代价/全最优后选准则。"——与 T2 §7 表内"LLM-MAS 场景+安全性质网+偏差证据最小性;算法层拟复用而非重造"逐字兼容。

---

## 6 本文件推导中的自主发现清单(供快速引用)

1. **admissible/consistent 跳步**(§3.4):FoldA Thm 4.3 证明文本把下界当真实代价用;marking-equation 启发式实际满足一致性(附一行 LP 证明),结论无恙但论证需补强——T2 换代价重解启发式时必须验一致性。
2. **P1 命题**(§4.3):标准代价下偏序化不改变最优值;偏序 alignment 的增量全在结构/诊断/复杂度,不在代价——T2 行文不得写"偏序 alignment 找到更优对齐",要写"找到并发保真、可诊断依赖偏差的等价最优对齐"。
3. **等代价诊断漂移**(§4.4):依赖偏差报告依赖等代价解的选择;两文都没把依赖纳入目标;T2 的短期后选方案(R8+确定性序)与长期可加化开放问题。
4. **cut-off 与代价序的耦合**(§2.3):任何 T2 代价序改造必须保持"\(\prec\) 蕴含代价 \(\le\)",否则截断不安全。
5. **原文勘误三处**(详见 03 §1.3/§3.2/§5.1):FoldA Def 6(3) 漏标签条件;Siddiqui §3.4 第 2 类偏差文字为复制粘贴笔误;FoldA 正文 697 vs Table 2 的 679 不一致。
