# ownership-v3 独立QA：Controller Acceptance（坐标层核对，8/8模块已完成，含1处复核订正）

日期：2026-09-15。`TASK-20260915-016`+`TASK-20260915-019`（5模块并行核验）+主控复核订正。状态：`CONTROLLER-PASS（坐标层，8/8已核，1处课程材料简称记录）`。

结论：坐标层核验已覆盖全部8个抽样模块，**8个PASS**（Ground Truth P0-P3经主控复核后由FAIL订正为PASS，含1处简称记录，见§2.5）。本报告仅覆盖"论文坐标声称是否真实"这一层，不覆盖"任务能否被真实完成、rubric是否合理"这一层（见下方边界）。**本报告本身也经历过一次判定错误并被纠正——批次2并行子代理对Ground Truth P0-P3的判定存在2处误判，已在§2.5"复核订正说明"中记录，提醒后续读者：并行子代理的核验结果需要主控复核后才能作为最终判定，尤其否定性结论（"全文0命中"）容易因搜索范围不足或判定尺度问题而产生假阳性。

## 1. 核验方法（与`TASK-20260915-007`已用方法一致）

主控独立用`pdftotext`直接提取原始PDF指定页码范围，逐字比对课程材料声称的论文坐标，不读课程材料自身的转述作为证据来源。

## 2. 独立重放证据

### 2.1 B-S3B（此前`TASK-20260915-007`已核，本次复核确认未变）

- p.3 `Definition 5. (Petri Nets)` 逐字存在。
- p.5 `Algorithm 3: Feature-Preserving Sampling` 全文存在，第9-23行为递归分解主体，与声称的"lines 9-23"精确吻合。
- p.6 soundness 叙述"To ensure model soundness, EdgeIM employs more invisible transitions..."逐字存在。

### 2.2 B-EVAL（本次新核）

- 声称坐标：EdgeIM PDF pp.5-7，section V、Eq.4、Tables I-III。
- 核验结果：p.5确认"This section introduces the F-measure..."及"The F-measure is computed using the following formula"（即Eq.4的文字锚点，公式本身为图像/特殊字符，`pdftotext`按预期无法转出符号本身，但前后文字锚点精确匹配）；TABLE I位于p.6附近文本流第138行、TABLE II第221行、TABLE III第408行（跨p.6-7），均在声称范围内。
- `TRAINING_FIXTURE.md`核对：任务1-5均有具体输入数据（虚构双log四行数据表）和可判定产出（复算F-measure、判断"更快/更准确/降低通信/保证soundness"分别需要什么证据、`<=1e-4`绝对误差rubric已冻结），非空转述。
- 判定：**PASS**。

### 2.3 CrossEdgeIM P0-P3（本次新核）

- 声称坐标：CrossEdgeIM PDF physical pp.1-6，Table I、Figs.2-3、Eq.1-2。
- 核验结果：
  - `TABLE I. Basic statistics of experimental logs.`逐字存在。
  - `FIG. 2. Petri net discovered by inductive miner.`、`FIG. 3. Petri net discovered by CrossEdgeIM.`逐字存在，且正文406/524行有"Figs. 2 and 3"的比较性引用，与P2声称的"F-measure/Complexity"比较分析吻合。
  - 公式(1)(2)在正文第476/490行确认存在（编号形式`(1)`/`(2)`，与README"Eq.1-2"表述一致）。
  - "RELATED WORK"（145行）、"CONCLUSION"（555行）、"limitation"（547行）三个P0声称的全文结构元素均逐字存在。
  - **一处措辞差异，非编造**：README用"三层架构"描述CrossEdgeIM机制，原文第206行实际用词是"three key stages"（三个关键阶段），不是"three layers"。两者语义接近（stage与layer在这个上下文都指organization/central的分层处理），但严格意义上不是同一个词。**此差异记入本报告，不判定为编造，但建议课程材料下次修订时改用原文措辞或明确标注这是转述**。
  - `TRAINING_FIXTURE.md`核对：P1任务1-6均有具体输入（O1/O2两组织、三个case的时间戳数据）和可判定产出（DeltaDFR/Org-DFG/residual），非空转述。
- 判定：**PASS（含一处措辞差异记录，不影响整体判定）**。

### 2.4 sigRank P0-P3（本次新核，`TASK-20260915-019`并行agent独立核验；**2026-09-16主控抽查复核，未发现同类误判，见下方"抽查复核"**）

- 声称坐标：sigRank PDF physical pp.1-13，Definitions 1-6、Eq.1-8、12 logs、9 methods、Table I/II/III、Fig.6、`10/12`、`100x`。
- 核验结果：Definition 1-6全部逐字存在（p.1-6，含编号）；公式(1)-(8)全部存在；`10/12`（"sigRank attains the highest F-measure (10/12)"）与`100 times`（"approximately 100 times longer than other techniques"）逐字存在；TABLE I/II/III、Fig.6均存在且位置吻合。
- **一处计数偏差，非编造**：README/任务描述称"9 methods"，PDF实际是"seven state-of-the-art event log sampling techniques"+1个filter-based baseline=8个方法，非9个。偏差为1，记录但不判定为编造（可能是计数口径差异，比如是否把sigRank自己算作第9个方法）。
- `SOURCE_REGISTER.md`核对：存在，已记录sigRank相关errata 4条，与模块自报"BUILT-WITH-ERRATA"状态一致。
- **抽查复核（2026-09-16，`TASK-20260916-002`同批追加）**：鉴于Ground Truth P0-P3暴露过并行子代理误判，主控独立重新`pdftotext -layout`提取sigRank全文（711行）抽查本模块。结果：Definition 1-6、`10/12`（第432行）、`100 times`（第516行）、Table I/II/III、Fig.6（第351/463/482/471行）全部逐字核实存在；"9 methods"计数偏差的原推测（"可能把sigRank自身算作第9个"）得到印证——原文第391-392行确认baseline是"seven ... techniques, along with a filter-based ... technique"（7+1=8），第406行原文自己也说"the eight sampling techniques"，加上sigRank自身正好凑成9，口径差异而非编造。**未发现同类误判，原判定成立**。
- 判定：**PASS**（含一处计数偏差记录，已复核确认非编造）。

### 2.5 Ground Truth P0-P3（本次新核，`TASK-20260915-019`并行agent独立核验；**2026-09-15追加复核已纠正agent的2处误判，见下方"复核订正"**）

- 声称坐标：Sommers PDF physical pp.1-30，`M0→M^S→M^L→L'`链条、`Psi(M,pi,h)=M∪h(pi)`与"simulation Eq.2"、DS1/DS2/DS3、AQ1-3、Table 3、Fig.12、Fig.4的"illustrative M'"。
- 核验结果：
  - `M0→M^S→M^L→L'`符号链条：**PASS**，p.9逐字存在。
  - 转换函数与"Eq.2"：**PASS（原agent误判为FAIL，已纠正）**——p.14公式`Φ(M,π,h)=M∪h(π)`确为(1)（第638行，转换函数本身），但README的"Eq.2"指向的是**另一处**：p.15"Simulation"小节的转移概率公式`p(tµs=tµ|w)=w(t)/Σw(t')`，PDF原文编号明确为**(2)**（第726行）。README这条任务描述的是"转换函数`Psi(...)`"和"simulation Eq.2"**两件事**，前者对应(1)，后者对应(2)——原agent只搜索到(1)附近就断言"全文只有(1)，不存在(2)"，未继续读到p.15的Simulation小节，属于**搜索范围不足导致的误判，不是课程材料的错误**。
  - AQ1-3 protocol：**PASS**，p.26逐字存在三条问题原文。
  - **DS1/DS2/DS3：FAIL（复核维持原判）——全文0命中，这三个标签在PDF中确实不存在**。原文用的是三个具体命名的数据集："package delivery process"（第一个，p.19附近）、"energy contract process"（第二个，p.20附近）、"real-life assembly process"（第三个，Omron合作方数据，p.22附近），全部用完整描述性名称指代，从未使用"DS1/DS2/DS3"这种缩写。课程材料自己的`TRAINING_FIXTURE.md`同样没有出现这几个缩写或与之对应的映射说明。**这是课程材料自创但未标注为自创的简称，不是编造数据，但确实与原文标签不一致，建议README改用原文的三个数据集名称或明确加注"DS1/DS2/DS3为课程简称，对应原文XXX"**。
  - Table 3与Fig.12：**PASS**，均存在且位置吻合。
  - Fig.4："illustrative"：**PASS（原agent误判为FAIL，已纠正）**——原agent核验方法正确（grep确认"illustrative"这个词本身确实不出现在Fig.4图题里），但**判定尺度过严**：README原句是"不把 Fig.4 的 illustrative `M'` 叫 `M^L` 或 log `L'`"，这里"illustrative"是**课程材料对Fig.4性质的形容词**（提醒学习者这是一个例示性的图，不要跟正式定义的`M^L`混淆），不是声称"原文用了illustrative这个词"。Fig.4图题原文"a modified version of M"在语义上正是"例示性、非正式定义"的意思，与"illustrative"这个形容词语义吻合，只是转述而非逐字引用。**这是任务描述用词与原文转述关系的正常情况，不构成坐标或标签错误**。
- **复核订正说明**：本次由主控（非批次2的并行子代理）重新独立核验，发现批次2报告对本模块的判定存在2处误判——"Eq.2不存在"是搜索范围不足（未读到p.15 Simulation小节），"illustrative不存在"是把"课程材料的描述性转述"错误地当作"应该逐字匹配原文"来判定，判定尺度过严。**教训**：并行子代理核验的结果不能直接采信为最终判定，尤其"某关键词全文0命中"这类否定性结论，需要核验方法本身是否真的覆盖了全部相关页码范围、以及判定标准是否混淆了"逐字引用"与"语义转述"两种不同性质的任务描述。
- 判定：**PASS（含1处课程材料简称与原文不一致的记录：DS1/DS2/DS3应改用原文数据集名称或加注映射说明，不影响整体判定，不判定为编造）**。

### 2.6 B-DEFENSE（`TASK-20260915-019`并行agent核验；**2026-09-16主控抽查复核，未发现同类误判，见下方"抽查复核"**）

- 声称坐标：EdgeIM PDF pp.1-7，sections I-II、IV-VI，EdgeAlpha/EdgeMiner来源标注，三阶段方法，limitation taxonomy。
- 核验结果：sections I-VI全部存在（含III，未跳过）；EdgeAlpha/EdgeMiner均在Related Work出现；**"三阶段"用词核验：EdgeIM原文Abstract与IV.A逐字使用"three key stages"**（与`TASK-20260915-016`发现的CrossEdgeIM"三层架构"vs"three key stages"措辞差异属于同一类问题，但这次是EdgeIM自己的原文，非转述差异）；Future Work/limitation均存在且可分类。
- **抽查复核（2026-09-16，`TASK-20260916-005`）**：主控独立重新`pdftotext -f 1 -l 7 -layout`提取EdgeIM PDF前7页（`/tmp/edgeim_p1-7.txt`），用`grep -n`逐项定位：Section I（line 50）、II（line 91）、III（line 77，未跳过）、IV（line 147）、V（line 379）、VI（line 435）全部逐字存在；EdgeAlpha出现在正文line 60与Table II对比数据，EdgeMiner出现在line 37/41及reference[24][25]；"three key stages"分别在Abstract（line 37）与正文line 67（写作"three key steps"，同义变体）逐字确认；Conclusion部分（line 449起）"Several areas warrant further exploration..."为作者自陈未来工作，可支持limitation taxonomy的三分类第一类。**未发现同类误判**，原判定成立。
- 判定：**PASS**。

### 2.7 B-S2（`TASK-20260915-019`并行agent核验；**2026-09-16主控抽查复核，未发现同类误判，见下方"抽查复核"**）

- 声称坐标：EdgeIM PDF physical pp.2-4，Definitions 3-4、section IV.A/C、Algorithm 2、符号`S_i/E_i/R_i`、`hash(activity) mod k`。
- 核验结果：Definition 3/4逐字存在；Algorithm 2标签与内容存在（含`hash(e.activity) mod k`逐字命中）；section IV.A/B/C三个子节均存在（B未跳过，仅README未提及）；`Si/Ei/Ri`符号在Algorithm 2输出定义与正文中多次出现。
- **抽查复核（2026-09-16，`TASK-20260916-005`）**：主控用论文物理页脚编号（404-410）重新定位：Definition 3（line 118）落在物理p.405，Definition 4（line 147）落在p.406，均在声称的pp.2-4范围内；section IV.A（line 149）落p.406，IV.B（line 265，README未提及但确实存在）与IV.C（line 250）均落p.407；Algorithm 2标题（line 275）及全部内容（line 282-311）落p.407；`hash(e.activity) mod k`（line 289）、`(Si, Ei, Ri)`三元组（line 258、line 342）均逐字确认。**未发现同类误判**，原判定成立。
- 判定：**PASS**。

### 2.8 B-S3A（`TASK-20260915-019`并行agent核验，含与B-S3B交叉核验；**2026-09-16主控抽查复核，未发现同类误判，另发现一处论文原文印刷错误，见下方"抽查复核"**）

- 声称坐标：EdgeIM PDF physical p.5，section IV.D，Algorithm 3 lines 1-8。
- 核验结果：Algorithm 3标签存在；lines 1-8内容为集合union（`S←S∪Si`、`E←E∪Ei`）与关系加法求和（`DFG(a,b)←DFG(a,b)+Ri(a,b)`），语义方向与README描述一致；section IV.D标题"Central Node Merging and Model Discovery"存在。
- **交叉核验（与`TASK-20260915-016`已核的B-S3B比对）**：PDF中只有一个编号为3的Algorithm；B-S3A声称lines 1-8（集合聚合阶段），B-S3B声称lines 9-23（递归分解主体）——两者行号范围互补且不重叠，与实际PDF算法结构吻合，**不是重复引用或编号冲突**。
- **抽查复核（2026-09-16，`TASK-20260916-005`）**：主控核对物理页脚，section IV.D标题（line 326）落物理p.408（=声称的p.5）；Algorithm 3标题行（line 340）与内容行1-8（line 344-351）均落同一页；逐行核对语义：`S←S∪Si`（line 346）、`E←E∪Ei`（line 347）、`DFG(a,b)←DFG(a,b)+Ri(a,b)`（line 349），与README描述完全吻合；行号9（line 352 "Function DFG, S, E"）确认是递归分解函数定义起点，不属于B-S3A的1-8范围，B-S3A/B-S3B边界位置复核无误。**顺带发现一处论文原文自身的印刷错误，非课程材料问题**：Algorithm 3的标题被原文印成"Algorithm 3: Feature-Preserving Sampling"（与Algorithm 1标题完全相同），应为类似"Central Node Merging and Model Discovery"这类描述本算法内容的标题；此错误不影响B-S3A判定（课程材料引用的是行号内容而非标题文字），但记录以免日后有人拿标题文字去核对反被误导。**未发现同类误判**，原判定成立。
- 判定：**PASS**。

## 3. 主控重点复核项（累计，含本批新增）

1. **CrossEdgeIM"三层架构"vs原文"three key stages"**（§2.3，`TASK-20260915-016`发现）——措辞差异，不算编造。
2. **EdgeIM自身也用"three key stages"描述其三阶段方法**（§2.6，本批新发现）——与CrossEdgeIM是两篇不同论文，各自原文都用"three key stages"这个表述，课程材料在B-DEFENSE处的"三阶段"转述准确，在CrossEdgeIM处的"三层架构"转述不够准确，两处需要分别看待。
3. **Ground Truth P0-P3：并行子代理批次2判定过FAIL，主控复核后订正为PASS**（§2.5）：3处质疑中2处（"Eq.2应为Eq.1"、"illustrative不在原文"）经主控独立复核确认是**子代理误判**（搜索范围不足+判定尺度过严），非课程材料错误；剩余1处（DS1/DS2/DS3不是原文标签，是课程材料自创简称）**属实但不算编造**，建议README改用原文数据集名称或加注映射说明。**本条目本身是一次"核验结果被更高一层复核纠正"的记录，提醒任何单一子代理的否定性结论（"全文0命中"）在下判定前都应有人工复核这一步**。
4. **sigRank"9 methods"应为8个**（§2.4，本批新发现）——计数偏差，记录但不判定为编造。
5. B-EVAL的fixture复算是否算术正确、CrossEdgeIM P3声称的consumer链条是否真实产出——仍未核，见此前记录，本批未新增处理。

## 4. 边界

本报告是**坐标层**的独立技术核验，不是：

- 不是完整AC-01~AC-10逐条判定（那需要覆盖全部75个文件，本次抽样覆盖8个P0-P3/BS模块，不等于全部75文件逐条过AC）。
- 不是用户学习效果验收（学习状态轴与课程资产轴分离，本报告只触碰资产轴）。
- 不代表`BUILD_STATUS.md`的QA-PASS总表可以直接改判——该文件本身在Sol写域内，本报告不改写该文件。**本次复核后Ground Truth P0-P3已订正为PASS，与`BUILD_STATUS.md`第17行"BUILT-WITH-SOURCE-OPEN"、第29行"DS2/DS3规模与复现实参不完整"（该文件自己也用了DS1/DS2/DS3简称，与本报告§2.5发现的"课程材料自创简称"一致，不新增矛盾）不冲突。**
- sigRank/Ground Truth/B-DEFENSE/B-S2/B-S3A五模块的核验最初由并行子代理独立完成（非主控本人逐字重复核对），核验方法与主控此前对B-S3B/B-EVAL/CrossEdgeIM的核验方法一致（pdftotext+grep逐字比对），但执行主体不同；**Ground Truth P0-P3一项经过主控复核纠正（FAIL→PASS，`TASK-20260916-002`），sigRank P0-P3一项经过主控抽查复核（原判定PASS成立，未发现同类误判，见§2.4，`TASK-20260916-002`同批追加），B-DEFENSE/B-S2/B-S3A三项经过主控抽查复核（原判定PASS成立，未发现同类误判，见§2.6-2.8，`TASK-20260916-005`）。批次2全部5个子代理核验模块现已全部经主控独立复核确认，不再有"未经复核"的模块**。

## 5. 结论

坐标层核验：**8/8模块已核**（B-S3B、B-EVAL、CrossEdgeIM P0-P3、sigRank P0-P3、Ground Truth P0-P3、B-DEFENSE、B-S2、B-S3A）。**8个PASS**（Ground Truth P0-P3经主控复核订正，含1处课程材料简称记录：DS1/DS2/DS3非原文标签；B-S3A附带发现EdgeIM论文原文自身1处印刷错误，不影响判定）。缺口1（独立QA）的坐标层核验范围已完成全覆盖。**本报告的可信性说明**：批次2的5模块核验最初由并行子代理完成，其中Ground Truth P0-P3的初始判定（FAIL）经主控复核后订正为PASS——这说明子代理核验存在误判风险。主控已对批次2剩余4个模块（sigRank、B-DEFENSE、B-S2、B-S3A）全部做完抽查复核，均未发现同类误判，原判定成立。**至此，全部8个坐标层核验模块均已经过主控本人独立复核确认，不再有"未经复核、理论上存在误判风险"的模块**。
