Author: Fable 5 subagent (Agent tool, ≤2 并发)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# 13 · 桥线 T1 三篇拆解合成注记（2026-09-04）

> 输入：同目录六件拆解（10/10b、11/11b、12/12b）+ `MANIFEST_ADDENDUM_20260904.md`；角色表 = `_scratch/seg0/_withdrawn/T1_paper_verification.md` :13–16、:27。锚形式：`[10 §5.7]` = 拆解件章节；`[10 tables C6]` = 10_SIGRANK 末尾表格件校验条；`[10 errata]` = 合并说明块；`[12 交叉核对 #N]` = 12_SOMMERS 主窗交叉核对块；`[PDF p.N]` 一律转引自拆解件（本件未读 PDF）。三件 PDF sha256 本件以 `sha256sum` 复验，与附录一致。

## 0. 本件是什么 / 不是什么

本件是六件拆解 + 附录的合成注记，只做三件事：三篇各给桥线什么、六件拆解哪里一致哪里没对上、还有什么没关；不复述三篇内容。三篇角色沿用 T1 表不重判：P2 sigRank = 辅助（采样邻近方法与定位），P3 CrossEdgeIM = 背景（不进主实验 baseline），P4 Sommers = 必要辅助（合成真值、行为偏差与记录错误区分）[T1 :13–16, :27]。本件不含任何与 EdgeIM 的机制比较、不答 G0 五问；拆解件里"见 EdgeIM 原文 §IV.B，用户自读"的指针原样保留为指针。

## 1. 三篇一览表

| # | 题录 | 体裁与证据强度 | T1 角色 | 拆解件 | 拆解 verdict | 原文内部矛盾数（带页码） |
|---|---|---|---|---|---|---|
| P2 | Su, Liu, Zhang(S.), Zeng, Mo, Cheng. "Toward Efficient Support for Business Process Event Log Sampling". IEEE TSC 19(2):1606–1618, 2026. DOI 10.1109/TSC.2026.3665370 [MANIFEST] | 期刊长文 13 页，CC BY 4.0；方法本体仅 p.4–5 约 1.5 页，其余为评估与整页表图 [10 §0] | 辅助 | 10（p1+p2+tables 合并，含 errata）、10b | 10 = DONE-with-errata：p2 曾 PARTIAL（§5.2–5.5 四处 `[待补]`），tables 件已回填，五条 p2 叙述被 errata 改判 [10 errata]；10b = FINAL | ≥10：top-N 单位迹/变体 [PDF p.5]；正文 L_C vs 图 L_E [PDF p.5]；Def 5/6 例 L_E/L_C [PDF p.4]；precision 误写 fitness [PDF p.6]；"10/12"无可复现计数规则 [PDF p.7]；"各六个最优"与并列冲突 [PDF p.7]；p.11 行内时间数与 Table III 不对应 [PDF p.11]；"100 倍"vs Table III 14–22 倍 [PDF p.11]；ETMC4200 Table III vs Fig. 6(i) [PDF p.11 vs p.9]；Fig. 6(f) 缺 5% 组 [PDF p.9]（出处 [10 §4.1][10 tables C3/C6/C7][10b §2(a)(b)(d)]） |
| P3 | Su, Liu, Zeng, Zhang(J.), Cheng. "CrossEdgeIM: An Edge-Based Approach for Interactive Robotic Behavior Model Discovery". IEEE IoT Magazine, Jan 2026, pp.55–60. DOI 10.1109/MIOT.2025.3625047 [11 §0] | 杂志短文 6 页、15 篇参考文献；无定义/算法框/证明，两式皆评价指标，单基线 [11 §6-1][11b 体裁]。**校样 vs 终版未定**：附录按 PDF 标题元数据 `_proof` 记"作者校样 [推断]"，11/11b 按印刷页码 + Xplore 水印判"更像终版"`[需验证]` [MANIFEST][11 §0][11b 体裁] | 背景 | 11、11b | 11 = **PARTIAL**（Fig. 1/Fig. 3 未视觉判读，§5.4 全格 `[图读数不清]`）[11 文末]；11b = FINAL（Fig. 2/3 八组数字读出并按式(1)(2)复算）[11b §3] | ≥6："SD 提升最显著"vs 相对增幅最小 [PDF p.5]；"复杂度低 12–17%"vs 算得 −11.1%~−18.1% [PDF p.6]；"fitness 略低于 1"但 ID_Log = 1 [PDF p.6]；"responsiveness"vs 模型只发一次 [PDF p.3 vs p.5]；fog/edge、Stage/Phase、Edge Node 混用 [PDF p.2–3]（轻）；#Dep. vs organization [PDF p.4–5]（出处 [11b §3][11b §2(a)][11 §5.2]） |
| P4 | Sommers, Sidorova, van Dongen. "A ground truth approach for assessing process mining techniques". Process Science 2:1, 2025. DOI 10.1007/s44311-025-00006-8 [MANIFEST] | 期刊长文 30 页，ICPM 2024 受邀扩展，CC BY 4.0；第三作者为该刊 co-EiC（已声明回避）[12 §0]；实验 = 12 份两包裹日志、单次运行、自评自家两种对齐 [12 §5.1][12b §1(3)(4)] | 必要辅助 | 12（p1+p2 合并，p2 为第 3 次尝试，含主窗交叉核对块）、12b | 12 = DONE-with-reservations（Table 3/Fig. 12 单次判读**不得引用**；Table 2 连线未辨）[12 交叉核对 #2 #5]；12b = FINAL | ≥12：BI 编号 p.10、p.14×2 [PDF p.10, p.14]；t1/t1 [PDF p.12]；BI5 通配符 [PDF p.12 vs p.14]；van 颜色 [PDF p.5 vs p.6]；数据可得性 [PDF p.28 vs p.18]；"each deviation detected"vs RI^p_mi [PDF p.24]；quantitatively vs qualitative [PDF p.1 vs p.28]；"trivially extends"vs 同页局限 [PDF p.28]；systemic/systematic [PDF p.24 vs p.26]；Table 1 RI^o 符号碰撞 [PDF p.6]；"four more"列五项 [PDF p.13]；"not interfere"vs"influencing each other" [PDF p.13 vs p.23]（出处 [12 §4.2][12 §5.2][12 §5.5-6][12 交叉核对 #1 #3 #4][12b §2]） |

## 2. 每篇"给桥线提供什么 / 不提供什么"

### 2.1 P2 sigRank（辅助）

**提供** [10 §9]：(a) "事件日志采样"子线的基线家族清单——LogRank / LogRank+ / Sani [25] 五法（Frequency、Similarity、Hybrid、Longer、Shorter）/ IMi，各带一句机制描述 [10 §5.1][10b C16]；(b) 九项可借用的评测设置：12 日志 = 6 合成 + 6 真实、比例网格 30%→5% 六档、过滤式发现以 θ = 1 − r 对齐、每档 5 次均值、质量 = 样本模型对原日志 F 比值、时间 = 均值表 + 逐档柱图、固定 IM 隔离采样效应、点名困难日志 [10 §9 借用清单 1–8]；(c) 作者自报失效条件——多唯一/低频变体、稀疏 DFR、罕见结构模式的日志 [10 §5.6-5][PDF p.7, p.11]；(d) 术语 → 原文定义页的词汇表（Def 1–6、式(1)–(8)）[10 §9 词汇表]；(e) Table I/II/III 逐格回填，Table II 为逐档 F-measure 全表，可作对照数据 [10 tables]；(f) ProM 插件与仓库脚注 [10 §0]。

**不提供** [10 §9-9][10b §4]：硬件、方差、逐档时间数字、样本变体数；数据集 URL、基线参数（Similarity 阈值、Hybrid 权重、LogRank 迭代数）、并列破平规则；top-N 的唯一语义（迹带重数 vs 变体各一，两示例互斥）[10 §4.1(a)][10b §1(c)]；可直接引用的"10/12""100 倍"[10 tables 对照][10b §2(a)(b)]；对 EdgeIM 的任何内容——原文仅 p.1 一处并列引用 [13]，未转述 [10 §3.1 I-D][10b §4(c)]，指针：见 EdgeIM 原文 §IV.B，用户自读。

**10b 总评**：大修 `[推断]`；三条修改意见 = 统一并公开计数/时间口径、钉死 top-N 语义并补 w_act 消融、补与自家 [12]（CCPE 2024）及 [25] Hybrid 的区隔 [10b §5]。

### 2.2 P3 CrossEdgeIM（背景）

**提供** [11 §9]：(a) 同一作者群 2025-12 邻近路线的存在性确认——单组织边缘发现扩到多组织并联合并、换 IoRT 叙事、通讯作者与主要基金变化 [11 §9]；(b) 对 EdgeIM [8] 的原文自述句（全文唯一一处，p.1）可原样引用，标 `[CrossEdgeIM 原文转述，非 EdgeIM 原文]` [11 §9][11b C12]；(c) III.B–D 的"按组织切分 + 各自 IM + τ_split/τ_join 并联"可作"跨组织合并最简基线"引用 [11b §5]；(d) Fig. 2/3 十六组 fitness/precision/F/ECaM/ECyM/Complexity 数字（11b 单次读数，自洽复算）[11b §3]；(e) 数据仓库线索 `Lihuiling12/TASE` [11 §0]。

**不提供**：任何采样/过滤/特征保持步骤——文本层 "sampl"/"feature-preserving" 正文零命中 [11 §4.1]；对 G0 五问的任何输入 [11 §9]；方法学事实——证据等级为**作者自述级** [11 §9]；通信量/时延/隐私/可扩展性实测（零实验）[11b §1(c)]；代码 [11b §4]；与 EdgeIM 的机制差异陈述（原文未自述）[11b §3 表]，指针：见 EdgeIM 原文 §IV.B，用户自读。

**11b 总评**：按研究论文标准"大修偏拒"，按杂志专栏体裁可接受但应删未验证强主张 `[推断]` [11b §5]。

### 2.3 P4 Sommers（必要辅助）

**提供** [12 §9 P1–P6]：(a) GT 构造配方 M0 → M^S → M^L → L′，事件回链变迁，每个事件可标"基线 / 哪个 RI / 哪个 BI"并给负责与受影响对象 [PDF p.8–9, p.24]；(b) 分类学 7 RI + 11 BI，两类偏差在**生成时**就分开、各有具名模型元素（Table 2）[PDF p.10]；(c) 评估通式 d(f(M0, L′), gt^f(·)) 与 PD/CC 两个实例化定义 [PDF p.9]；(d) n·m·k 乘子与三个实例数据集 [PDF p.17–23]；(e) Table 3 式"模式 × 方法 → 对象集合 + 解释栏"的定性评估模板 [PDF p.26]；(f) Trident / mira 工具 [PDF p.16–17]。12b 补一条：最可迁移的资产是 Table 2 的 counterpart 结构与"GT = 四元组 + 回链"定义，二者独立于 t-PNID 与对齐方法 [12b §5]。

**前提** [12 §9]：base model 为 Petri 网族，对象级模式需 t-PNID；h 与仿真参数手工；被评技术能吃投影日志；评估者自定义 gt^f 与 d。

**不提供** [12 §9][12b §1(2)(4)]：数值型质量分（d 从未实例化）；频率受控数据集（三实例 k = 1、DS1 模式隔离）；与真实日志的真实感校准（一次都没做）；PD 评估实证（未跑任何发现算法）；对日志层采样/过滤的讨论（"sampling" 只指分布采样，"filter" 只指记录错误来源）；EdgeIM 相关内容（零提及）。与"日志缩减"最近的一句是对 Käppel et al. 2021 删迹法的批评 [12b §5][PDF p.4]。

**12b 总评**：大修 `[推断]`；必须项六条（编号/t1 错误、数据声明统一、量化/定性二选一、给仿真参数、讨论最优对齐非唯一性、Sommers 2024 a/b）[12b §5]。

## 3. 三篇之间的交叉关系

**作者群（只陈述拆解件已核的作者栏事实）**：sigRank 六人 Su / Liu / Shuaipeng Zhang / Zeng / Mo / Cheng [10 §0]；CrossEdgeIM 五人 Su / Liu / Zeng / Jinglin Zhang / Cheng [11 §0]；两篇交集 = Su / Liu / Zeng / Cheng。两篇各自的 EdgeIM 引文作者栏均为 "X. Su, C. Liu, F. Lu, L. Cheng, Q. Zeng, and S. Zhang" [10b §4(c)][11 §0]，与 EdgeIM 的交集亦为此四人；鲁法明不在两篇作者栏 [10 §0][11 §0][11b 作者注]。"S. Zhang" 的全名两拆解件未统一：11 §0 展开为 Shouli Zhang（依据是 EdgeIM 侧模板，本件不读），sigRank 的 Shuaipeng Zhang 是否同一人 `[需验证]`。通讯作者：sigRank = Liu + Mo，CrossEdgeIM = Liu [10 §0][11 §0]。Liu 在两篇均为 NOVA IMS + 山东理工双署名，Su / Zeng 均为山东科大 [10 §0][11 §0]。基金交集：NSFC 62472264、山东省杰青 ZR2025QA13、FCT UID/PRR/04152/2025（sigRank 侧另有 UIDB/04152/2025 写法）[10 §0][11 §0]。

**引用关系**：sigRank → EdgeIM = 引文 [13]，p.1 一处三文并列 "[12], [13], [14]"，未转述内容 [10 §3.1 I-D][10b §4(c)]；CrossEdgeIM → EdgeIM = 引文 [8]，p.1 一处与 EdgeMiner 合述 "mainly target single-organization IoT environments"，§II 未再提 [11 §2][11b C12]。两篇对 EdgeIM 的引用方式同型：一次、作为"已有路线"的背书或反衬，均不承担机制描述。sigRank ↔ CrossEdgeIM 互引：11b 列了 CrossEdgeIM 全部 15 篇，自引段 [8]–[13] 不含 sigRank [11b §4]；sigRank 47 篇是否引 CrossEdgeIM，10/10b 未逐条核 `[需验证]`。时间线：sigRank 收稿 2025-05-26、出版 2026-02-16 [10 §0]；CrossEdgeIM 出版 2025-12-03 [11 §0]；Sommers 收稿 2024-12-11、接收 2025-02-18 [12 §0]。Sommers 与另两篇零引用关系：Sommers 全文未提 EdgeIM、未讨论日志采样 [12 §0][12 §9][12b §5]；两篇引文分析均未出现 Sommers [10b §4][11b §4]（sigRank 侧未逐条核 `[需验证]`）。

**评估口径差异**：

| | 质量度量 | 参照对象 | 效率 | 下游算法 | 数据 |
|---|---|---|---|---|---|
| sigRank | 对齐式 fitness [36] / precision [37] → F-measure；式(8) 比值定义但分母 F(L_0, M_0) 未报 [10 §4.4][10b §2(c)] | 原日志 L_0；6 个"合成"日志也不用生成模型作真值 [10 §5.1] | 采样 + 发现 ms，六档均值 [10 §5.1] | IM 固定 [10 §5.1] | 12 公开日志，无 URL [10b §4] |
| CrossEdgeIM | F-measure 式(1) [14] + Complexity 式(2) ECaM/ECyM [15] [11 §4.4] | 日志；无真值 [11 §5.1] | 无实测，只有 O(e)/O(m log m)/O(K) 记号 [11 §1][11b §1(c)] | IM，变体未指明；集中式 IM 为唯一基线 [11 §4.3][11 §5.1] | 4 份"模拟机器人"日志，疑源自 TASE [11 §5.2] |
| Sommers | d(f(M0, L′), gt^f) 通式；CC = 最优对齐、PD = M0 + 频繁 BI；实验中 d 未实例化 [12 §1][12 §5.1] | 合成真值 M0/M^S/M^L/L′ + 回链 [12 §1] | 对齐计算时长（Fig. 12）[12 §5.3] | 三种对齐，两种自研；未跑发现算法 [12 §5.1][12 §9 P3] | 12 份两包裹日志 [12 §5.1] |

判断 `[推断]`：前两篇的"质量"都是**模型对日志的拟合**，没有真值；Sommers 恰以"无 GT 则算法识别的正确性无法核验"批评这类评估 [12 §2][PDF p.4]，但自身把 d 留在定义层。三篇口径互不可比：sigRank 的 F-measure 与 CrossEdgeIM 的 F-measure 分母、fitness 实现、基线都不同，不能并表；桥线若要对齐三者，只能按 Sommers 的前提自定 gt^f 与 d [12 §9 前提]。另一处只记事实：两篇都报告 IM 在特定输入上产出"花状"结构——sigRank 的 LogRank 样本模型 [10 §4.3]、CrossEdgeIM 的 IM 基线 precision 0.13–0.32 [11 §5.5(v)]。

## 4. 六件拆解交叉核对后仍存疑的清单

★ = 本件判断最要紧的三条（理由见表后）。

| # | 文件 | 位置 | 存疑内容 | 需要什么才能关闭 |
|---|---|---|---|---|
| 1★ | 10 §4.1(a)、10b §1(c) | sigRank p.5 Fig. 3 vs L_C 算例 | top-N 选择单位：迹带重数 vs 变体各一，ProM 实现取哪种未知 | 有网核 ProM 仓库代码（脚注 github.com/promworkbench/SoftwareProcessMining） |
| 2 | 10 errata、10 tables 对照、10b §2(a) | p.7 vs Table II | "10/12""各六个""9/12 唯一例外 Final"三种计数规则都复算不出 | 原文无规则，盘面不可关；用户自读 p.7 或问作者；引用时改用拆解件复算数并注明分母 |
| 3 | 10 tables C6、10b §2(b) | Table III vs Fig. 6(i) | ETMC4200 LogRank 84306 ms vs 刻度读作 180k–190k | 人工高倍看图 |
| 4 | 10 tables C7 | Fig. 6(f) | SimulateLog2000 缺 5% 组 | 人工看图 |
| 5 | 10b §2(b) | p.11 正文 | 行内时间数（10296/9127/12006…）与 Table III 任何格不对应 | 用户自读 p.11；若来自某一档，Fig. 6 无数字则不可关 |
| 6 | 10 tables C1、10b §3 | Table I | 2000AllNoise 归 Real-life | 有网核数据集来源（原文无 URL） |
| 7 | 10 §4.5、10b §1(a) | 式(5) | \|σ\| = 1 分母为零；实验日志是否含单事件迹 | 有网核数据 |
| 8★ | MANIFEST、11 §0、11b 体裁 | CrossEdgeIM 整件 | (i) 校样（元数据 `_proof`）vs 终版（页码 55–60 + 水印）；(ii) 附录"卷期页码未定"与 11 "Jan 2026, pp.55–60"不一致（页码已印、卷期未印 [11b 题录]）；(iii) 页脚水印 "Authorized licensed use limited to: Veer Narmad South Gujarat University. Downloaded on September 03,2026" [11 §0]，与来源栏 `[需核实]` 直接相关 | 用户核 PDF 属性与页脚、补下载来源一句；引用题录前定版本 |
| 9 | 11 §5.4 ↔ 11b §3 | Fig. 3 | 11 全格未读；11b 单次读出 16 组并复算自洽；ID_Log fitness = 1 决定"fitness 略低"是否只对 3/4 成立 | 第二次人工看图即可关 |
| 10 | 11 §4.0 ↔ 11b C1 | Fig. 1 | 11 未判读；11b 读出 Phase 1/2/3 与 "Edge Node" 标签 | 同上 |
| 11 | 11 §5.2、11b §1(b) | 脚注 1 | 数据谱系 TASE / #Dep. → "机器人交互"是否为改标签复用 | 有网核仓库 |
| 12 | 11 §4.1、§4.3、11b §1(f) | §III.B–C | case 终止判定、跨节点前驱事件如何到达、时钟假设、IM 变体 | 原文未给、无代码；不可关，只能标注 |
| 13 | 11b §3 | Fig. 2/3 | ECyM 八值 10001–10009 疑饱和；"8.2 vs 11.7 nodes" 对 IM 如何按组织算 | 前者有网核 [15] 实现；后者原文未给 |
| 14 | 12 交叉核对 #2 | Table 2 | RI ↔ BI 连线对应 | 人工看图 |
| 15★ | 12 交叉核对 #3、12b §4 | p.18 vs p.28 | gitlab 仓库（模型/日志/mira）可达性 | 有网核 |
| 16 | 12 交叉核对 #5 | Table 3 / Fig. 12 | 单次判读且两视角出入（Fig. 12 第 6 横轴标签）；关前一律不得引用 | 第二次人工判读 |
| 17 | 12 交叉核对 #1 | p.10 / p.14 | 旧编号是否 ICPM 2024 版残留 | 有网核 ICPM 2024 原文 |
| 18 | 12b §2 | p.13 / p.22 / Fig. 9 | "four more"列五项；"not discoverable by Alpha/IM"无实验；Fig. 9 三黄 vs p.21 四 RI | 用户自读 / 自跑 / 人工看图 |
| 19 | 12 §5.1 | p.24–27 | 硬件/重复/方差缺，仅凭文本层缺失推断 | 用户自读 |
| 20 | MANIFEST | 三件 | 下载来源 `[需核实]` | 用户补一句 |

**已在本轮关闭的**：12 §0 留的 Fig. 11/Table 3/Fig. 12 页码 `[需验证]` → p2 已逐页核为 p.25/26/27 [12 §5.3]；12 §0 "sha256 任务书给定、本篇未重算" → 本件 `sha256sum` 三件均与附录一致；10 p2 五条错误叙述 → errata 已改判 [10 errata]。

**哪条最要紧 `[推断]`**：#1，因为它是唯一改变"可复用工件行为"的存疑——T1 表把 sigRank 列为可选 sensitivity 的前提就是"合法获得实现 / 足够算法细节" [T1 :29]，而两示例互斥意味着复现者必须自己选一种口径；#8，因为题录版本与来源栏同时悬空，且水印显示的授权机构与本项目无关，引用卫生先于内容；#15，因为 Sommers 是必要辅助，框架能否落地取决于工具与数据是否可得。其余多为三篇自身缺陷，关不关不改变桥线用法。

## 5. 拆解质量自评

| 文件 | 字节 | `[PDF p.` 锚 | 需验证 | 推断 | 矛盾 | 图读数 | 状态 |
|---|---|---|---|---|---|---|---|
| 10_SIGRANK | 61850 | 216 | 19 | 22 | 9 | 12 | DONE-with-errata；三表全为图读数 |
| 10b | 27519 | 95 | 2 | 16 | 2 | 1 | FINAL；四格抽检 ✓ [10b §3] |
| 11_CROSSEDGEIM | 21131 | 75 | 8 | 12 | 0 | 29 | **PARTIAL** |
| 11b | 18053 | 122 | 11 | 14 | 6 | 8 | FINAL |
| 12_SOMMERS | 56278 | 245 | 12 | 15 | 14 | 5 | DONE-with-reservations；p2 三次尝试 |
| 12b | 26416 | 112 | 5 | 9 | 14 | 6 | FINAL |

（计数 = `grep -o | wc -l` 字符串出现次数，含转引重复，只作相对量。）

**10 ↔ 10b**。一致点：top-N 两口径；式(2)(3) 集合记号 vs 多重计数；0.5/0.5 无消融；Def 5/6 下标；p.6 笔误；m 未定义；"10/12"不可复算；硬件/方差缺；Fig. 6 为堆叠柱、Table III 无 IMi（10 p2 曾写错，tables 件纠正，10b 独立写对）。分歧点：(i) 10 §5.6-4 把"LogRank 141549 ms 约 100 倍"列为**支撑住**的结论，10b §3 指按 Table III 只有 14–22 倍，"100 倍"只可能是采样时间单比 `[需验证]`——10 未察觉；(ii) 10 tables 对照的"六档均值 12/12"是 sigRank 仅对 LogRank/LogRank+，10b 的"6 + 1 并列"是对全部 8 个采样法，分母不同，非矛盾但引用时须注明；(iii) 10b §1(d) 进一步指 m 应与 log n 比、复杂度应写 O(nm + n log n)，10 只说未计入统计遍历；(iv) 10b 独有：p.11 行内时间数两套口径、Fig. 2 "Accuracy"/正文 "Effectiveness"、NASA 与 2000AllNoise 5% 同为 0.3146 疑复制。

**11 ↔ 11b**。一致点：EdgeIM 仅 p.1 一处；并联 = 纯 AND、跨组织 implicit；起止集剪枝在循环下误删；跨节点前驱事件来源未说明；单基线且输入不对等；零通信实测；TASE 谱系；ECyM 疑饱和；版本疑终版；F 提升由 precision 驱动。分歧/补充：11b 读了 Fig. 1/3，因此多出两处数字矛盾、ID fitness = 1、Event/Case 整除、"responsiveness vs only once"；11 未给审稿判定，11b 判"大修偏拒"；11 §6-6 提"值得写 paper 的困难"（跨界摘要），11b 无。无实质分歧，11b 是 11 的超集。

**12 ↔ 12b**。一致点：BI 编号三处同定位；t1/t1；gitlab vs 数据声明；systemic/systematic；d 未实例化；k = 1；自评自家；realistic 未校准；"exponential"三点不成立；**GT 非唯一**——12 §6.2 假设 B 与 12b §1(1) 从不同入口到同一深层问题，是三对里一致率最高的。分歧点：(i) Table 3：12 单次判读填格，12b 拒填 → 主窗判"不得引用"[12 交叉核对 #5]；(ii) Fig. 12 第 6 标签 12b 疑与 Table 3 不同，12 假定同序；(iii) 12b 多出 Table 1 RI^o 碰撞、van 颜色、"each detected" 应为 5/6、DS2 RI^o_in 类型、PUPRLE 等笔误；(iv) 12 §6.3 给出研究方向首选（偏差可识别性），12b 未提。

**哪篇拆解最薄 `[推断]`**：11_CROSSEDGEIM——21 KB、PARTIAL、Fig. 1/3 未读，因此漏掉两处只能靠图内数字发现的矛盾。原因一半是论文本身（6 页无定义无算法，可拆的少），一半是时间盒（p.5 未判读）。好在 11b 完整且覆盖其全部缺口，且 P3 是背景篇，薄不伤桥线。最不稳的不是某一件而是一类：**图读数数字**（10 三表全表、11b Fig. 3、12 Table 3）均为单次判读，仅 10b 抽了 4 格复核。

## 6. 给用户的读法建议（只建议，不决策）

`[建议]` **读序按 T1 角色权重**：P4 Sommers（必要辅助）→ P2 sigRank（辅助）→ P3 CrossEdgeIM（背景）。

`[建议]` **P4**：先读 12 §1（三分法与 GT 四元组定义）和 §9（提供/前提/不提供），再读 12b §5 独立补充与 §1(1)（GT 是生成路径隐变量）。原文先 p.8–9、Table 2（p.10）、p.24。BI 编号一律以 Table 2 为准，正文编号不可直接引 [12 交叉核对 #1]。**不能引用**：Table 3 / Fig. 12 任何格内数字 [12 交叉核对 #5]；Fig. 9 闪电计数 [12b §3]；46 篇/16 篇引文计数 [12b §4]；"exponential increase" [12 §5.5-1]。

`[建议]` **P2**：先读 10 §4.1（复原伪码 + 两处口径矛盾）和 §9，再读 10b §4 可复现性表与 §2(a)。原文先 p.4–5 方法、p.11 Threats。引 Table I/II/III 时整表标 `[图读数]`，避开带 `[?]` 的格（trainingLog2-Fre-5% 0.24438、ETMC4200-sho-5% 0.967、NASA-30%-hyb 加粗）[10 tables]。**不能引用**："10/12"、"100 倍"、Fig. 6 任何柱值、p.11 行内时间数；O(n log n) 声明引用时须附 10b 的 O(nm + n log n) 异议 `[推断]`。

`[建议]` **P3**：只读 11 §9、11b §5 总评、11b §3 数字表；原文 p.1 摘要、p.2–4 §III、p.6 §IV.C。**不能引用**："12–17%"、"SD 最显著"、"8.2 vs 11.7"、三个复杂度记号、通信/隐私/可扩展性主张；Fig. 3 数字待第二次判读；题录版本未定前标 `[需验证]`。

`[建议]` **通用**：凡拆解件写"见 EdgeIM 原文 §IV.B，用户自读"处，本件与三篇都不替你答；三篇评估口径互不可比（§3 表），不要把 sigRank 与 CrossEdgeIM 的 F-measure 放进同一张表。

`[FINAL · §0–§6 齐全 · 05:4x 写盘]`
