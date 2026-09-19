# ProbGuard — Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction

**会议**:ASE 2026(第 41 届 IEEE/ACM Automated Software Engineering,2026-10-12/16,慕尼黑;CCF-A)
**作者**:Haoyu Wang(SMU,一作,博士生)、Christopher M. Poskitt(SMU)、Jiali Wei(西安交通大学)、**Jun Sun(SMU,资深作者)**
**⚠ 重名消歧**:本文的 Sun = **Jun Sun(新加坡管理大学 SMU)**,与 ReGA(FSE 2026)的通讯作者 **Meng Sun(北京大学)** 是两个人、两个团队。SMU 组代表作:AgentSpec(ICSE 2026)、LawBreaker(ASE 2022)、REDriver(ICSE 2024)、Bazille et al.(CAV 2020,Jun Sun 是共同作者)。
**曾用名**:Pro2Guard(arXiv 早期版本);代码仓库仍叫 [Pro2Guard](https://github.com/haoyuwang99/Pro2Guard)
**原文**:[arXiv:2508.00500](https://arxiv.org/abs/2508.00500)(HTML 全文含公式与 Appendix A 证明,2026-08-13 实见)
**⚠ 版本警示(08-22 增)**:线上现行版已滚到 **v2**——其 Table 1 已删 FP 列(仅警告时间),正文不再报具身任务数/trace 总量等计数。本拆解全部实验数字(FP 0%/75%/100%、AWT、30 traces 等)出自 **08-13 所见旧版**,引用时必须锁定 arXiv 版本号;版本迁移对账(逐数字核 v2)登记为待办,留专门窗口。
**类型**:实验论文(方法 + 定理 + 两域实验 + 开源代码)
**拆解日期**:2026-08-13
**状态**:**S01–S04 v1 完成;S05/S06(复现)待 W-复现窗;S07(多轮清洁审查)待后续窗口**

---

## 一句话总结

把 agent 执行轨迹经谓词抽象压成 3–34 个符号状态,从 30 条 trace 学一个 DTMC(valid-transition-aware Laplace 平滑),运行时用 PRISM 查"从当前状态出发永远安全的概率" P_safe = P[AG ¬unsafe | s_i],低于阈值 θ 就提前干预——AV 域最长提前 38.66 秒预警,具身域 reflect@0.9 把 unsafe 率降 65.37% 且保住 80.4% 的任务完成率。

---

## 核心产出文件

| 文件 | 内容 |
|------|------|
| `01_QUESTIONS.md` | 读前 5 问 + S02 跟进问题 + 品味判断 + Critical Thinking 审计 |
| `02_SKELETON.md` | 结构骨架 + 24 个符号 + 流程图文字版 + 左墙右墙(适用边界)|
| `03_PAPER_READ.md` | 9 层精读:问题定位/方法逐步/DTMC 细节/PAC 条件/AV 构造/实验协议/结果批判/局限/**T5 域迁移逐条映射** |
| `04_DERIVATION.md` | 8 组公式逐式推导:Laplace 平滑归一化证明、PAC 样本界数值手推、Thm 3.4 三步复推、P_safe 线性方程组手推、监控自动机端点检验;含 4 个自主发现 |
| `GLOSSARY.md` | 20 个核心术语(形式化/学习与保证/系统与实验/团队谱系)|
| `ADDENDUM_DTMC_PRISM_FORMAT.md` | 轻窗补件(2026-08-14):src/safereach 定向精读,"DTMC 构造→PRISM 导出"数据格式/接口契约/属性文法 + 可照抄导出样例 + T5 谓词表对接检查表(只读未运行)|
| `GUIDE_addendum_dtmc_prism.md` + `MAINTENANCE_addendum_dtmc_prism.md` | addendum 配套双手册(2026-08-14 收官存档):四场景用法/快查表/FAQ;单一事实源/更新触发器/机械验证命令/遗留项台账 L1-L6。交接总档案在 `progress/handoff/2026-08-14__lightwindow-probguard-dtmc-format__handoff.md` |

---

## 关键发现(S01–S04 阶段)

1. **范式主张:reactive → proactive**。AgentSpec/GuardAgent/ShieldAgent 都是"违规临近或已发生才拦";ProbGuard 预测轨迹级风险,警告在所有评估场景中严格早于违规发生(检出率 100%,7 个 AV 场景)。
2. **valid-transition-aware Laplace 平滑是最实在的技术点**:只给语义合法转移分配 α=1 的伪计数,物理不可逆性(碰撞是吸收态)硬编码为零概率——既保 DTMC 逻辑一致,又给 PAC 界提供"所有合法转移概率有正下界 → 条件数 B 有限可算"的前提(Appendix A Step 2 依赖此)。
3. **PAC 界的诚实负结果是本文最有信息量的部分**:条件数 B(P̂) 决定一切——具身域(前向推进、混合好)B=1.0–481,需 530–10⁵ traces;AV 域(自环 >99.9%)B≈10⁷–10⁸,均匀 CTL 界需天文样本,只能退回频率估计(Bazille Thm 3,单性质,185–1016 traces)。**B 是"域适不适合 PAC 路线"的第一判据**。
4. **"保证"与"实践"是两张皮**:实验每场景只采 30 traces,远低于上述任何界;论文自认目的是"演示实用性而非正式认证"。引用本文时不得写"ProbGuard 提供了经认证的概率保证"。
5. **安全-完成率 Pareto**:具身域 baseline unsafe 40.63%;stop@0.9 → 2.60%(-93.6%)但完成率崩到 10.42%;reflect@0.9 → 14.07%(-65.37%)且保 47.74% 完成率,是甜点位。干预是纯文本 advisory(prompt 注入三字段风险 alert),不改控制流。
6. **推导中的自主发现**(详见 `04_DERIVATION.md`):① P_safe 非平凡要求 DTMC 存在安全吸收结构(安全 BSCC),否则 P_safe≡0、监控器对任意 θ 恒报警——这可能是 AV 域 θ=0.7 时 FP=100% 的结构性机制之一,也是 T5 应选有界式 P=?[F≤k unsafe] 的硬理由;② 监控自动机 Def 5.2 逐字执行比 F[0,K] 语义多给一步响应窗口(工程影响 ≈1 个控制周期,可忽略,复现时以代码为准);③ 若观测数据含 valid_tran 判为非法的转移,Eq (1) 分布欠归一——实现上必须断言或剔除;④ 主文样本界公式与 Appendix A 的 H* 定义在 max 作用位置上不一致(主文疑取最松界),实现 PAC 检查器应按 App A 保守版,裁决待读 Bazille 原文。

---

## 与 T5 及 Phase 1 的关系

**Phase 1(论文复现)**:本文是复现首选(D6 深挖卡结论,优先级高于 ReGA)——①管线与 T5 的 M2/M3 一比一对应;②具身域实验纯 API(gpt-4o-mini)+ PRISM,CPU 可跑;③PAC/PRISM 技能直接迁移;④**代码依赖 AgentSpec 的 `controlled_agent_executor`,复现 ProbGuard 必须先跑通 AgentSpec**。换域接口 = 实现一个 `Abstraction` 抽象类(六个方法),论文报告具身/AV 适配各约 200/250 行 Python——T5 域适配工作量的锚点。

**T5(companion 域概率护盾,`research/map/proposals/T5_companion_prob_shield.md`)**:本文是 T5 的方法学母版。
- stove 例(`stove_on ∧ ¬agent_in_kitchen ∧ elapsed≥T` 的累积无人看管风险)与"深夜连续高强度情绪对话"结构同构;
- AV 的 K-bounded response 监控自动机是 T5 时间窗谓词的现成形式化起点,但语义是"触发→K 步内必须响应";T5 需要的"滑动窗口内累积/持续超阈"(依赖螺旋)语义仍是空白 → T5 的形式化贡献点;
- 复现即预研:SafeAgentBench 谓词换 INTIMA 谓词、trace 换对话轨迹,就是 T5 原型;
- **改域后第一个该产出的数字是对话域的 B(P̂)**(具身 1.0–481 vs AV 10⁷–10⁸ 两个锚点之间,无人报告过),它直接决定 T5 能承诺哪一档 PAC;
- 竞速提醒:SMU 组约 5 个月一迭代(AgentSpec ICSE'26 → ProbGuard ASE'26),T5 差异化(窗口化谓词/干预 Pareto/对话域 B 值)要尽早占位。

---

## 目录结构

```
ASE2026_ProbGuard/
├─ README.md          ← 本文件(论文卡)
├─ 01_QUESTIONS.md    ← S01 产出
├─ 02_SKELETON.md     ← S02 产出
├─ 03_PAPER_READ.md   ← S03 产出
├─ 04_DERIVATION.md   ← S04 产出
├─ GLOSSARY.md        ← 术语表
├─ ADDENDUM_DTMC_PRISM_FORMAT.md ← 轻窗补件:DTMC→PRISM 格式笔记(T5 对接件)
├─ GUIDE_addendum_dtmc_prism.md / MAINTENANCE_addendum_dtmc_prism.md ← 补件双手册
└─ (待补)05_REPRODUCTION/ ← S05/S06 复现,待 W-复现窗
   (待补)07_REVIEW.md     ← S07 多轮审查,待后续窗口
```

**信息来源约定**:公式与定理均以 arXiv:2508.00500 HTML 全文为准(2026-08-13 抓取);Bazille et al. CAV 2020 的定理内容系经 ProbGuard 转述(原文未单独打开,已在各处标注);工程细节(仓库结构、依赖)引自 D6 深挖卡(`casual/companion-survey/14_academic/deep/D6_safety-formal.md`)的仓库实见记录。

---

**最后更新**:2026-08-13
