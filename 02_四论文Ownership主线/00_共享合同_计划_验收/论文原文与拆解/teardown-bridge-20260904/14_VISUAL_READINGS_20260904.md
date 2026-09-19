Author: Fable 5 main window (direct vision read of extracted/rendered images; TASK-20260904-001 追补)
Date: 2026-09-04
Layer: EVIDENCE, not a decision

# 14 · 图内数字视觉回填（主窗直读，08:0x）

> 方法：`pdfimages -png` 抽出原生分辨率嵌入图（CrossEdgeIM p.4 2173×1886、p.5 2173×1150）；Sommers p.26 用 `pdftoppm -r 220` 渲染后旋转 90° 再读。图件在 `_launch/img/`。本件只补 `11_CROSSEDGEIM.md` §5.4 与 `12_SOMMERS_p2.md` §5.2 标 `[图读数不清]`/`[单次判读]` 的格子，**不改原拆解件**；引用时以本件为准，原件对应格子视为被本件替代。

## 1. CrossEdgeIM Fig. 3（CrossEdgeIM 结果）[PDF p.5] `[图读数·原生分辨率·主窗单人判读]`

| 子图 | Fitness | Precision | F-measure | EcaM | EcyM | Complexity |
|---|---|---|---|---|---|---|
| (a) EM_Log | 0.9697 | 0.2289 | 0.3704 | 45 | 10001 | 89.5969 |
| (b) FP_Log | 0.9434 | 0.3916 | 0.5535 | 36 | 10002 | 71.7418 |
| (c) ID_Log | 1 | 0.3986 | 0.5700 | 37 | 10005 | 73.7273 |
| (d) SD_Log | 0.9787 | 0.4603 | 0.6261 | 32 | 10001 | 63.7959 |

Fig. 2（IM 基线）[PDF p.4] 主窗直读结果与 `11_CROSSEDGEIM.md` §5.3 四行逐格一致（不重抄）。

**自检**：式 (1) F-measure 与式 (2) Complexity 重算——(a) 2·0.9697·0.2289/(0.9697+0.2289) = 0.3704 ✓；2·45·10001/10046 = 89.597 ✓；(d) 2·32·10001/10033 = 63.796 ✓。

**对正文主张的核对**（正文 [PDF p.5–6]）：

| 主张 | 图上数字 | 判定 |
|---|---|---|
| "significantly higher F-measure scores across all datasets" | 0.3704>0.2335、0.5535>0.3779、0.5700>0.3962、0.6261>0.4857 | 四组都成立 |
| "the most notable improvement in SD_Log (0.6261 vs 0.4857)" | 绝对增量 EM +0.137、FP +0.176、ID +0.174、SD +0.140；相对增量 EM +58.6%、FP +46.5%、ID +43.9%、SD +28.9% | SD 的**增量**无论绝对还是相对都不是最大（绝对最大是 FP，相对最大是 EM）；只有"SD 的 F-measure 绝对值最高"成立。"most notable improvement" 与图不符 `[⚠️主张与图不符]` |
| "complexity scores 12–17% lower" | EM −18.1%、FP −12.2%、ID −15.9%、SD −11.1% | 实际区间 11.1%–18.1%，两端都落在所述区间之外；量级对，范围说法不准 `[需验证：作者取整方式]` |
| Fitness "slightly lower than IM's perfect score" | 三组 <1（0.9697/0.9434/0.9787），ID 为 1 | 成立，FP 差 5.7 个百分点，"slightly"偏乐观 [推断] |
| 11 open 2："Complexity 对比是否只由 ECaM 驱动" | ECyM 八个值全在 10001–10009，式 (2) 调和平均在 ECyM ≫ ECaM 时 ≈ 2·ECaM（89.60 ≈ 2×45，63.80 ≈ 2×32） | **是**：Complexity 在本实验里数学上退化为 2×ECaM，ECyM 不携带区分信息；"12–17% lower"实质就是 ECaM 从 55/41/44/36 降到 45/36/37/32 |

## 2. Sommers Table 3 [PDF p.26] `[表读数·220 dpi 旋转后二次判读]`

主窗直读与 `12_SOMMERS_p2.md` §5.2 单次判读逐格比对，**12 行中 10 行一致**，两处需改：

| 行 | p2 单次判读 | 本件判读 | 说明 |
|---|---|---|---|
| RI^e_mi（四列） | {p,v,c} | **{p,v,e}** | 第三个对象是 e（employee），不是 c（courier）；DS1 对象类型含 employees 与 couriers [PDF p.14 文本层 :661]，放大 2× 后字形明确 |
| RI^o_mi（GT / γ̃ 下标；γ 主集合） | {v}_(p,c) / {p,v,c} | **{v}_({p,e})** / **{p,v,e}** | 同上，c → e |

其余 10 行（RI^e_in(1)/(2)、RI^o_in、RI^p_mi、BI5、BI7、BI10、BI3、BI9、BI2）与 p2 表一致，p2 的 `[表读数·单次判读·需验证]` 标记对这 10 行可以撤下；两行 `e/c` 之外的集合结构不变，p2 §5.2 基于集合包含关系的判断（γ̃ 主集合与 GT 12/12 一致等）不受影响。

RI^e_in(1) 的 γ̃ 格为 {p}_({c})——与 p2 一致，p2 标的 `[格内措辞不清]` 指解释栏 "γ and γ̃ incorrectly add the courier as responsible and affected object"，本次读清：原文就是这句。

## 3. 方法结论（给用户）

- 页级 `Read`（子代理用的）对**正文与矢量表**可靠：Fig. 2 逐格与本件完全一致。失败的两类是**栅格嵌入图**（页渲染把 2173 px 的图压到页宽）和**横排整页表**（旋转 90° 后字符太小）。
- 解法都是一条命令：`pdfimages -png` 抽原图 / `pdftoppm -r 220` 渲染 + PIL 旋转，再让模型 `Read` 图片。两图三张表合计 4 次 Read、约 5 分钟，比子代理 60 分钟循环重读便宜两个量级。
- 仍未做：sigRank Fig. 6（堆叠柱状图，84306 vs ≈180k 那条矛盾）——柱状图读数本质是估读，抽原图也只能缩小误差，不能给精确值；Sommers Fig. 12 横轴标签同理。
