# GLOSSARY — 偏序 alignment × 网展开 术语表

**出处约定**:F=FoldA(arXiv:2506.08627),S=Siddiqui(arXiv:2504.00550);Def/Thm 编号照原文。

---

## 一、alignment 系

| 术语 | 定义与备注 | 出处 |
|---|---|---|
| **alignment(对齐)** | move 序列 \(\gamma\in((A\cup\{\gg\})\times(T\cup\{\gg\}))^*\):日志分量投影=轨迹、模型分量投影=模型从初态到终态的 occurrence sequence、无 \((\gg,\gg)\) | F Def 1 |
| **move(移动)四型** | 同步 \((a,t)\)(日志模型各走一步且标签同)/ log move \((a,\gg)\)(仅日志,T2 读作越权)/ model move \((\gg,t)\)(仅模型,T2 读作缺失)/ 非法 \((\gg,\gg)\) | F Def 1 |
| **最优 alignment** | 代价 \(\kappa(\gamma)=\sum\kappa(e,t)\) 最小者;标准代价:同步 0、log/model 1、silent 0.0001(可忽略正值) | F Def 2/Alg 1;S Def 11 |
| **同步积网 SPN** | trace net × model net:place 取并,转移=log 拷贝∪model 拷贝∪同标签配对(sync);在其上"最短路=最优 alignment" | F Def 3;S Def 15 |
| **扩展同步积** | SPN 外加目标变迁 \(t^*\)(preset=原终态)与目标 place \(p^*\);终态检查变为"目标事件出现";保 1-safe | S Def 9 |
| **trace net / event net** | 轨迹转成的无选择 Petri 网;全序 trace→链;p-trace(DAG)→依赖边变 place | S §3;F §3 |
| **p-trace(偏序轨迹)** | 同案例事件上的标注 DAG \(\rho_c=((E,\prec),l)\);原文 \(a\prec b\iff\) end(a)<start(b)(时间戳);T2 需换成 correlation_id 消息因果 | S Def 1 |
| **偏序 alignment** | move 上的严格偏序 \(\delta\),满足全序版三条件;与全序版唯一区别是序是偏的 | F Def 4 |
| **u-alignment** | 三元组 \((\rho_c,G_\mathcal{N},\varphi)\):日志偏序+模型 run 偏序+同步单射 \(\varphi\)(标签相等⟺被映射);合并同步节点后仍须无环 | S Def 8 |
| **alignment order** | u-alignment 合并同步节点后的整体偏序 \(\rho_c\biguplus G_\mathcal{N}\);节点四色=move 四型,边分 log/model 依赖 | S Def 8/§3.4 |
| **alignment run** | 扩展 SPN 中以目标事件 \(e^*\) 收尾的完整分布式 run;其局部配置即一个 alignment | S Def 10 |
| **missing / undesired events** | 传递归约后:日志有模型无的事件(log move)/ 模型有日志无的事件(model move);⚠ Siddiqui 命名以模型为被评对象,T2 视角要翻转(缺失↔undesired,越权↔missing) | S §3.4 |
| **missing / undesired dependencies** | 日志侧依赖边不在模型侧(或反向);T2 第③类"序/并发违例"的形式载体;是事后诊断、不在优化目标内 | S §3.4;04 §4.4 |

## 二、展开系(unfolding)

| 术语 | 定义与备注 | 出处 |
|---|---|---|
| **出现网 occurrence net** | \(O=(B,E,G)\):条件至多一入事件、无环、有限前驱、无自冲突;并发/冲突/因果三关系显式 | F Def 5;S Def 4 |
| **因果网 causal net** | 出现网再加"条件至多一出事件"=无选择;单个偏序 run 的载体 | S Def 4 |
| **分支过程 branching process** | 标注出现网 \(\beta=(O,p)\),\(p\)(S 记 \(h\))为到原网的同态;无重复事件(⚠ F Def 6(3) 漏写标签相等条件,以 S Def 5 为准);"展开"即构造之 | F Def 6;S Def 5 |
| **因果 < / 冲突 # / 并发 ‖** | 有向路径可达 / 同 place 分叉的两条路径 / 两者皆非;分支过程用 # 保存选择、用 ‖ 保存并发(不交织) | F Def 15;S §2 |
| **配置 configuration** | 因果封闭且无冲突的事件集;**↔ 偏序 run 一一对应**(方法的语义支点);完整配置=到达终态 | F Def 7 |
| **割 Cut(C) / Mark(C)** | 发生 C 后有 token 的条件集 \((\mathit{Min}(O)\cup C^\bullet)\setminus{}^\bullet C\);经标注压回原网 marking | F Def 7 |
| **局部配置 [e]** | 使 e 可发生的最小事件集 \(\{e'\mid e'\le e\}\);其代价 \(Z([e],\zeta)\)/\(s([e])\) 是优先队列键 | F Def 10;S Def 6 |
| **局部分布式 run** | \([e]\) 加上相关条件与边构成的因果网;算法返回物 | S Def 7 |
| **充分序 adequate order** | 有限配置上的序:井然 + \(\subset\)-单调 + 被同构有限扩展保持;ERV 用它保证 cut-off 不丢 marking | F Def 12;S §2 |
| **cut-off 事件** | \(\mathit{Mark}([e])\) 已被更小配置 \([e']\prec[e]\) 代表 ⇒ 停止扩展该支;循环/无界行为在此折返(有限前缀的来源) | F Def 13 |
| **完整有限前缀** | 含全部可达 marking 的有限分支过程(McMillan/ERV);本对论文**不构造完整前缀**,到达目标即停(有向展开) | F §2;S §2 |
| **possible extensions** | 当前前缀下可追加的事件集(需找两两并发的输入条件组合);**实现的组合瓶颈**,沿用 Römer 2000 优化 | S §3.2;F §4.1 |
| **有向展开 directed unfolding** | 按代价(+启发式)best-first 追加扩展、到达目标 marking 即停;概念源自 Bonet et al. 2008 | F §1/§4;S §3.3 |
| **easy sound** | 终态 marking 可达(等价:完整前缀含至少一个完整 run);两文对模型网的唯一健全性假设;F 额外支持无界 easy sound 网 | F §2/附录 0.A.2;S Def 9 脚注 |
| **1-safe** | 任意可达 marking 下每 place 至多 1 token;两文全程假设;T2 策略网需检查 | F 附录 0.B;S §2 |

## 三、算法与序

| 术语 | 定义与备注 | 出处 |
|---|---|---|
| **FoldAn / FoldAh** | FoldA 的无启发式(Dijkstra 式)/ 启发式(A\* 式)版本;序键分别为 \(Z([e],\zeta)\) 与 \(Z+h(\mathit{Mark}([e]))\),Python `id()` 破平(⚠ 不可复算) | F §4.1/§4.2 |
| **\(ERV[\triangleleft_c]\) / \(ERV[\triangleleft_h]\)** | Siddiqui 的 on-the-fly ERV 变体:代价序 / 启发式序;\(stopAtFirst\)=false 可枚举全部最优 alignment run | S Alg 1 |
| **代价序 \(\triangleleft_c\)** | 三键字典序:代价 \(s\) < → 配置大小 \(|C|\) < → 入队序 \(\gg\) 字典序;**充分性有全证**(Thm 0.B.1) | S Def 13 |
| **半充分序 semi-adequate** | \(f=s+est\)(est 可采)诱导的序;仍可用同一 cut-off 判据(Bonet et al. 2008,经 S 转述) | S Def 14 |
| **marking equation 启发式** | \(h(m)=\min\{\zeta^{\mathsf T}x:\mathbb{C}x=fm-m,x\ge0\}\),LP 松弛下界;可采**且一致**(一致性证明见 04 §3.4;F Thm 4.3 表述有跳步) | F §4.2;S §3.3 |
| **Dijkstra 不变式** | 非负可加代价+\(\subset\)-单调序 ⇒ 第一个弹出的目标事件即全局最优;F Thm 4.1(3) 的实质 | 04 §2.2 |
| **Classic PA** | Lu/Fahland/van der Aalst 2014 两步法:A\* 在可达图选一条全序最优→回放展开(循环处克隆 place)成偏序 alignment;缺陷=等代价解任选 | S §1/§5;F §2 |

## 四、评测与工具

| 术语 | 定义与备注 | 出处 |
|---|---|---|
| **#SPT / #QS / #VS / ET** | 同步积转移数 / 排队状态数 / 访问状态数 / 耗时;F 回归:ln(ET)~2.891·#SPT+0.715·choice−0.161·concurrency(adj R²=0.770) | F §5 |
| **choice / concurrency factor** | place 平均出度 / transition 平均出度;**选择度是性能之敌,并发度不是**(T2 发现层监控指标) | F §5.2 |
| **C/E/CN/EN/L 模型族** | F 实验 1 合成模型:并发/选择/嵌套并发/嵌套选择/循环;EN 最伤 | F Table 1 |
| **ITL 基准** | 大规模 conformance 基准(275–429 转移参照模型);prDm6/prEm6/prFm6 上 Dijkstra 全灭而 FoldAh 存活 | F §5.2(引 Munoz-Gama et al.) |
| **BPIC12** | 含 start+end 双时间戳的贷款流程日志(262,200 事件/13,087 案例)——**因双时间戳才能构造 p-trace**,S 真实实验唯一日志 | S §5.2 |
| **Cortado** | RWTH 交互式过程发现工具;S 的算法落地处,conformance 界面新增"fit 但有序偏差"第三态与依赖偏差列表 | S §4 |
| **chevron 视图** | 偏序 trace 变体的递归顺序/并行分块可视化(Schuster et al. ICPM WS 2021);T2 不复用 | S §3.4 |
| **PTAndLogGenerator / StochasticPetriNets** | S 合成实验的过程树生成器(控并发度 0–70%)与日志模拟 ProM 插件 | S §5.1 |
