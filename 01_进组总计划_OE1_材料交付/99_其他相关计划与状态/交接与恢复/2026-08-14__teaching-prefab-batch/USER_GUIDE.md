# USER_GUIDE — 教学包使用手册(写给用户本人)

> 你是学员,AI 是主考。一句话用法:**挑一个包,把它的 `EXAMINER_SOP.md` @ 给 AI,说"主考 Gate 1"**。

## 一、开考口令(模板)

```text
按 <论文拆解目录>/teaching/EXAMINER_SOP.md 主考,我是学员,从 Gate 1 开始。
(续考:…从上次断点续,先读该包 answer_key 总分表与 mistakes.md 定位断点。)
```

例:`按 MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/teaching/EXAMINER_SOP.md 主考,从 Gate 1 开始`。

**轻考**(仅 FoldA/Anchor):把口令里的 `EXAMINER_SOP.md` 换成该包 `teaching/LIGHT_MODE.md` 即可(四关复述+口试,约 1h,红线不打折)。

## 二、一场考试长什么样(单关约 25–40 分钟)

1. **备考**:你先读该关讲义(= 拆解目录对应文档,SOP 材料集表里写了具体文件与节),读完**关闭讲义**。
2. **A 卡**:闭卷填关首 A 卡(协议图/公式链/结果卡等,是可评分 artifact)。
3. **90 秒复述**(8 分):按提示词链闭卷口述,提纲原样记录,不事后润色。
4. **变体/反例/应用**(各 4 分):逐题作答,必须留可评分 artifact,"只说懂了"计 0 分。
5. **判分**:主考按 `answer_key.md` 逐点给分;≥16 且无红线 → 下一关;否则登记 `mistakes.md` 走重考。
6. 四关全过+错题闭环 → 预约 **FINAL_ORAL**(闭卷口试,每题准备 30 秒/主答 90 秒/追问 2 分钟,先结论→再定义数字→再限制迁移)。

**时间预算**:整包(四关+口试)约 2–3.5 小时;完全可拆场,推荐一晚 1–2 关。断点由 answer_key 总分表 + mistakes.md 记录,任意窗口可续。

## 三、学员纪律(违者本场作废)

- 作答前**不开** `answer_key.md`(工作簿提交区要如实申报);FINAL_ORAL 全程闭卷。
- 不确定就写"**待核**"——不罚分;猜数字/猜因果被抓到按红线处理。
- 每题必须落 artifact(提纲/算式/表格),口头"懂了"不算。

## 四、七包现状与选择

| 包 | 状态 | 一句话看点 |
|---|---|---|
| 鲁组联卷 | AWAITING(**建议先考**,9-10 进组) | 四关=四篇 PN 方法族,Gate 4 兼进组面谈应对;卷面已深审并修正 2 处 P0(PASS(fixed)) |
| ProbGuard | AWAITING | DTMC/PAC/P_safe+复现实测数字,T5 方法母版 |
| AgentSpec | AWAITING | DSL 四算子+开销口径,ProbGuard 执行器依赖 |
| INTIMA | AWAITING | 31 类分类学→16 谓词折叠,T5 谓词工程 |
| Anchor | AWAITING(可轻考) | 双探针/PR 公式/探针库四决策,长时程审计;轻考入口 `teaching/LIGHT_MODE.md` |
| EmoAgent(LP-07 旧包) | AWAITING | EmoEval 协议/34.4%/EmoGuard 源码审计/T5 伦理 |
| FoldA | AWAITING(死线最松,可轻考) | 偏序对齐+展开最优性,T2 复用三清单;轻考入口 `teaching/LIGHT_MODE.md` |

## 五、常见问题

- **Q:我能只做一关吗?** 能。进度落在包内,下场续。但关内四步(复述→变体→反例→应用)一次做完,勿拆半关。
- **Q:答错很严重吗?** 分数不够=RETAKE(闭环后只重考该关);碰红线=该关全部四步重来。红线都是"引用这篇论文时会闹笑话/会造成事实错误"的点,考试就是为了在进组/写 T5 之前把它们烧进肌肉记忆。
- **Q:考过之后呢?** 主考按 `MAINTENANCE.md` §2 T4 把包状态翻成 TEACHING-PASSED 并登记 INDEX——那一刻这篇论文的 P 窗④段才算完成。
- **Q:教学包答案和拆解文档冲突怎么办?** 以拆解文档为准,当场指给主考,主考登记该包 mistakes.md 并修 answer_key(见维护手册 T1)。
