---
date: 2026-08-13
auditor: A9(W-对外材料窗口波次 · 发布前终审)
target: proposals/ 对外材料全集(onepager v1 / 三声音中英 / 鲁版 / 简历 / 图 / 占位符链路 / 渲染产物)
type: final-review
rule: 只报告不改稿(审改分离,修复由主 Agent 执行);不登 CHANGELOG
基准: factcheck_onepager_20260813.md(名称口径裁定)、INDEX.md §4(禁语)、OE1_lu_email_v4.md §3(鲁版雷区)
手段: 通读 + rg 机械扫描(禁语/脱敏/人名/名称/锚定数字/占位符正则)
---

# 对外材料发布前终审报告(final_review_20260813)

## ① 总裁定

**NEEDS-FIX。** 名称口径、禁语、脱敏、红线头、渲染修正同步均已过关,但存在 5 条必须修复的 FAIL——最严重的一条是**简历把一页纸里的"未来计划"写成了"已完成工作"**(平台护盾原型),与全体材料及 INDEX 执行状态直接矛盾,属对外诚信风险;另有声音 B 中英版参考文献/RQ 实质错位、简历占位符链路两处断裂。修完 5 条 FAIL 即可转 RELEASE-READY(WARN 不阻塞)。

---

## ② R1–R8 逐项结果表

| 项 | 判定 | 一句话结论 |
|---|---|---|
| R1 名称口径 | **PASS**(1 WARN) | 8 个可独立外发文本单元逐一核过:v1 中/英、声音 A/C 中英、Voice A/C 英均"首现括注、二现直写";声音 B 中英正文首现无括注但括注在其参考文献内(见 W1);简历与鲁版正文不提该论文(不提不是错);全集无裸 Pro2Guard(冲突分析表/factcheck 引用属记录性质,豁免) |
| R2 禁语与空白口径 | **PASS** | 机械扫描(全球唯一\|无人区\|保证所有\|无漏报\|证明.{0,6}安全\|the only\|guarantee.{0,12}all\|no false negative)对外正文零命中(命中项全部是"自查记录"性引用);空白句在 v1 中英 + 三声音中英共 8 处**全部**同时带"2026 年 8 月/August 2026"时点限定与"带概率保证/probabilistic-shielding"收窄限定;"不声称端到端形式保证/no end-to-end formal guarantee"句 8 个版本全在 |
| R3 脱敏与人名 | **PASS**(标注) | companion 仅出现于素材路径引用(`casual/companion-survey/...`)与自查记录,正文零命中;INTIMA 全集只写短名,**无任何一处引用含 companionship 的官方副标题**(英文 Voice B [5] 用的是脱敏描述短语,处理正确);人机恋/伴侣/角色扮演/张重熙/romantic/role-play 正文零命中;对外正文无作者人名(v1 撰写说明第 5 条 Jun Sun/Meng Sun 警示属内部注,发前随说明区删除) |
| R4 事实句一致性 | **FAIL**(F1) | 锚定数字交叉表全部一致(见下表);精确数 8,824 未泄漏,"44 个文件"仅在撰写说明;XES/GraphML 处处为互操作事实表述,"实验表明/评测显示"类零命中;美赛全集无 HMC/NUTS/Truthometer。**唯一例外:简历宣称"已原型化带 PAC 保证的运行时行为护盾",与所有其他材料的"未来计划"定位矛盾 → F1** |
| R5 中英一致性(三声音) | **FAIL**(F2、F3) | A/C 中英对:四段结构对应、语气同向、限定句同在(C 版 4.7 GB 不对称见 W2);**B 版中英实质错位:参考文献 8 条集合与编号完全不一致(F2),RQ 集合不同(F3)**;英文三版均无联系方式行(W3) |
| R6 占位符与替换链路 | **FAIL**(F4、F5) | 占位符 × 文件 × 键覆盖表见下;两处断裂:**英文简历复用中文占位符会被填成中文值(F4)**、**简历 [GPA(选填)] 无 config 键(F5)**;其余 15 种占位符全部有键覆盖 |
| R7 渲染与图 | **PASS**(3 WARN) | 两个 HTML 均已是修正后版本:ProbGuard 括注在(zh"原名 Pro2Guard、ASE 2026"/en"formerly Pro2Guard — ASE 2026")、评测域已含"自动驾驶"、空白句已收窄,旧句无残留,撰写说明未混入;两 .mmd 语法复查通过(subgraph/end 配对、引号配对、节点 id 全 ASCII);鲁版图正文与文件头注释均无 shield/DTMC/iMDP/PAC/概率字样。关联 WARN:W4(声音版无法直接过渲染切片)、W5(HTML 无红线头)、W8(鲁图导出文件名带 lu) |
| R8 红线头 | **PASS**(1 WARN) | 8 个对外草稿全部有"严禁未经用户确认外发"或等义红线:v1/voices/voices_en/lu_variant/resume(引言区)、diagram/README(HTML 注释)、两 .mmd(%% 注释);fill_placeholders.sh、send kit("发信动作须用户本人完成")、factcheck、placeholder_sheet 属工具/记录豁免;render/out 两 HTML 无红线头(见 W5) |

### R4 锚定值交叉表(对外正文口径)

| 锚定值 | v1 中/英 | 声音 A/B/C 中 | Voice A/B/C 英 | 简历中/英 | 鲁版正文 | HTML zh/en | 判定 |
|---|---|---|---|---|---|---|---|
| 约 8,800 行 | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | ✓ | ✓/✓ | 一致(无 8,824 泄漏) |
| 43 单元测试 | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | ✓ | ✓/✓ | 一致 |
| 44 文件 | 仅撰写说明 | — | — | — | — | — | 合规(正文不写) |
| 2,400 条 | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | —(MindBridge 已删,合规) | ✓/✓ | 一致 |
| Qwen2.5-7B + q4_k_m | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | — | ✓/✓ | 一致 |
| 约 4.7 GB | 仅撰写说明 | 仅 C 版正文 | 三版均无 | 无 | — | 无 | C 版中英不对称(W2) |
| 数月 / 数千轮 | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | ✓ | ✓/✓ | 一致(months/thousands of turns 对应) |
| XES 1.0 + GraphML(互操作) | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | ✓("还谈不上研究结果") | ✓/✓ | 一致,全部事实表述 |
| PM4Py / networkx | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | ✓ | ✓/✓ | 一致 |
| 5-agent / five-agent | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | — | ✓/✓ | 一致 |
| 向量+BM25、Recall@K/MRR/NDCG | ✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓/✓ | — | ✓/✓ | 一致 |
| 美赛 M 奖 / 4,470 行 / 23 核 / 自适应 MH | —(一页纸不提,合规) | — | — | ✓/✓ | M 奖+自适应 MH(子集,合规) | — | 一致;无 HMC/NUTS/Truthometer |
| 平台护盾原型(DTMC/iMDP+Storm) | 计划(2026.09–12) | 计划 ×3 | 计划 ×3 | **"已原型化" ← 冲突** | — | 计划 | **FAIL → F1** |

### R6 占位符 × 出现文件 × config 键 × 覆盖表

(排除引文编号 [1]–[8]、mermaid label、markdown 链接、checkbox;send kit/placeholder_sheet 内的引用性出现不列)

| 占位符 | 出现文件(正文) | config 键 | 覆盖 |
|---|---|---|---|
| [姓名] | v1、voices、lu_variant、resume(中文节) | NAME_ZH | ✓ |
| [姓名][学校][专业] | **resume 英文节 L51/L54** | NAME_ZH/SCHOOL_ZH/MAJOR_ZH(将填入中文值) | **✗ F4** |
| [Name] | v1、voices_en | NAME_EN | ✓ |
| [学校] / [university] | v1、voices、lu_variant、resume / v1、voices_en | SCHOOL_ZH / SCHOOL_EN | ✓ |
| [专业] / [major] | 同上分布 | MAJOR_ZH / MAJOR_EN | ✓ |
| [身份表述] / [status] | v1、voices / v1、voices_en | IDENTITY_ZH / IDENTITY_EN | ✓(已定口径) |
| [课题组]、[课题组/实验室名] / [lab] | v1、voices / v1、voices_en | LAB_ZH / LAB_EN | ✓(值待用户,见 §二特别注记) |
| [联系方式] | v1 说明、voices、lu_variant、resume | CONTACT_ZH | ✓(英文版无插槽,W3) |
| [电话 / 微信] | OE1(基准) | PHONE_WECHAT | ✓ |
| **[GPA(选填)]**(半角括号) | **resume L15/L54** | **无**(GPA_HOURS 三个变体均不含此写法) | **✗ F5** |
| [GPA / 每周可投入时长，选填](全角逗) | OE1 | GPA_HOURS | ✓(字节级核对一致) |
| [Reisig 进度] | lu_variant L45;OE1 §3 称呼 | REISIG_PROGRESS | ✓ |
| [填实际进度] | OE1 正文 | REISIG_PROGRESS | ✓ |
| [日] | OE1 落款 | DATE_DAY | ✓ |
| [日期] | 仅作称呼出现,非正文 token | DATE_FULL(键在脚本、不在 config 模板) | 注记:无实害 |
| [项目名称/方向] | OE1 §4 分支 B | NSFC_PROJECT | ✓ |

---

## ③ FAIL 清单(修复可直接执行)

### F1(R4,最高优先)简历把"未来计划"写成"已完成工作"
- **文件**:`resume_onepage.md`
- **定位句**:中文版 L30"基于概率模型检验(DTMC/iMDP + Storm)为该平台原型化带 PAC 保证的运行时行为护盾。";英文版 L69"Prototyped a runtime behavior shield with probabilistic guarantees for the platform via DTMC/iMDP abstraction and the Storm model checker."
- **矛盾证据**:①v1/三声音中英共 8 个版本均把"符号 trace → DTMC → 越界概率验证"列为 2026.09–12 **计划**(且声音 A 写"尝试");②`INDEX.md` 头部"drafts-complete / **experiments-not-started**……必须通过各自 kill criteria 后才可对外声称研究贡献",§5"实验:⬜ 未开始";③简历自己的技能节写"Storm/stormpy、PRISM 语言,**学习中**",与"已原型化"自相矛盾;④factcheck 量化数字来源清单无任何护盾原型实测记录。
- **改法**(两选一,中英同步):
  - 删除该 bullet(推荐,平台条剩两条 bullet 仍完整);
  - 或改为计划口径——中文:"下一步计划:以概率模型检验(DTMC/iMDP,Storm 工具链)为该平台构建运行时行为监测(2026 下半年,复现打底后推进)";英文:"Next step: runtime behavior monitoring for the platform via probabilistic model checking (DTMC/iMDP, Storm toolchain) — planned for H2 2026."
  - 若用户确实已做过 toy 原型:须先补证据入 factcheck 并明确"toy/原型验证于模拟数据"限定,否则维持删改。

### F2(R5)声音 B 中英参考文献 8 条编号对象不一致 + ShieldAgent 归类错位
- **文件**:`onepager_v2_voices.md` L69 与 `onepager_v2_voices_en.md` L60–69
- **定位**:中文 B:[1]INTIMA [2]RCT [3]EmoAgent [4]ProbGuard [5]ShieldAgent [6]JAIR [7]dtControl [8]ReGA;英文 B:[1]ProbGuard [2]ReGA [3]ShieldAgent [4]**AgentSpec** [5]INTIMA [6]RCT [7]JAIR [8]dtControl——集合不同(中含 EmoAgent 无 AgentSpec,英相反)、编号全错位;且英文 L50"deployed defenses remain prompt rules or LLM judges without quantitative commitments **[3, 4]**"把 ShieldAgent[3] 归入"无量化承诺防护",与同文 L56(ShieldAgent=shield pipeline)、与中文 B L58 及 v1 全局口径("ShieldAgent 属概率护盾工作")直接矛盾,被懂行读者对照即翻车。
- **改法**:以中文 B 的 8 条为基准集合与顺序重排英文参考文献(即英文 [4] AgentSpec 换成 EmoAgent — LLM-judge 式监控基线,EMNLP 2025, arXiv:2504.09689),正文引用号同步重排;英文 L50 的 [3, 4] 改为只引 EmoAgent(及可留 AgentSpec 若决定保留,但 ShieldAgent 必须从该句移除)。若用户偏好保留 AgentSpec,则中文 B 同步加入并做成 9 条或替换,总之**两版集合与编号必须逐条相同**。

### F3(R5)声音 B 中英 RQ 集合实质不同
- **文件**:`onepager_v2_voices.md` L60–62 与 `onepager_v2_voices_en.md` L52–54
- **定位**:中文 RQ1(域建模)/RQ2(**预测增量**:提前量与 AUC vs LLM-judge)/RQ3(干预权衡 Pareto,可选);英文 RQ1(modeling)/RQ2(**enforcement**≈中文 RQ3)/RQ3(**情绪状态机 SMC 偏差 + monitor 合成**——中文 B 完全没有,系 v1"备选方向"内容)。中英两版对外承诺的研究问题不同,成对递出即穿帮。
- **改法**:拍板一套 RQ 后双语对齐。推荐以中文 B 为准重写英文 RQ2/RQ3:RQ2 = "Does DTMC/iMDP-based out-of-bound probability prediction improve lead time (turns) and AUC over LLM-judge and prompt-only baselines?";RQ3(optional) = "What Pareto trade-off do decision-tree-compressed graded interventions exhibit on the safety × persona-consistency plane?";删去英文现 RQ3 或明示其为 secondary direction(与中文同步)。

### F4(R6)英文简历复用中文占位符,脚本会填入中文值
- **文件**:`resume_onepage.md` 英文节
- **定位句**:L51"**[姓名]** | [学校], [专业], Undergraduate (3rd year) | [联系方式] | GitHub: alkaid";L54"[学校] — [专业], undergraduate program, Sep 2024 – Jun 2028 (expected)"
- **问题**:跑 `fill_placeholders.sh resume_onepage.md` 时 NAME_ZH/SCHOOL_ZH/MAJOR_ZH 会把英文简历填成中文姓名/中文校名/中文专业名。
- **改法**:英文节 [姓名]→[Name]、[学校]→[university]、[专业]→[major](共 3 类 5 处);[联系方式] 可保留(邮箱中英同值)。

### F5(R6)简历 [GPA(选填)] 无 config 键覆盖
- **文件**:`resume_onepage.md` L15/L54(写法为半角括号"[GPA(选填)]")+ `fill_placeholders.sh` L53 + `placeholder_sheet.md` 主表
- **问题**:脚本 GPA_HOURS 仅映射 "[GPA / 每周可投入时长，选填]"(全角逗)、"[GPA/投入时长（选填）]"(全角括)、"[GPA]" 三种;简历的半角括号变体不被替换(仅触发残留警告);placeholder_sheet 主表也无此行(主表自声明范围仅"一页纸+OE1",但 resume L6 明确宣称"可用 fill_placeholders.sh 批量替换",承诺与能力不符)。
- **改法**(任一,建议前者):① `fill_placeholders.sh` MAPPING 的 GPA_HOURS 数组增加 "[GPA(选填)]";并在 placeholder_sheet 主表补一行注明该占位符用于简历、选填、留空则整段删除;② 或把简历两处改写为已映射 token "[GPA]"。

---

## ④ WARN 清单(可发但建议改)

| # | 项 | 位置 | 建议 |
|---|---|---|---|
| W1 | R1 | 声音 B 中英正文首现 ProbGuard 无括注(中 L66"复现 ProbGuard [4]"、英 L58"ProbGuard [1]"),括注在参考文献内 | 编号引文体例下合规;但一页纸读者未必翻到文末,建议正文首现补"(原名 Pro2Guard)/(formerly Pro2Guard)"一次,彻底对齐 factcheck 口径 |
| W2 | R5 | 中文声音 C L85 有"(约 4.7 GB)",英文 Voice C L83 无 | 中英对称:英文补 "(~4.7 GB)" 或中文删;该数字属"发前须用户逐项确认公开"清单成员,统一后便于一次拍板 |
| W3 | R5/R6 | 中文三声音每版末尾有"(联系方式:[联系方式])";英文三版与 v1 英文版均无联系方式插槽 | 发英文版时在标题下或页脚手动补联系方式;或在 voices_en 三版末尾补同款插槽(config 注释目前只声明了 v1 的情况) |
| W4 | R7/R6 | `render_onepager.sh` 切片约定(需"## 中文版/## English Version"语言区头 + 一级标题)只被 v1 满足;voices/voices_en(节头为"## 三、声音 A…/## Voice A…")与 resume(中文节内无一级标题)、lu_variant 均无法直接渲染 | 选定声音后:把该声音节整理成 v1 同构结构(或另存单声音文件)再渲;README"后续 v2/v3 沿用即可"的前提目前不成立,建议主 Agent 修复时一并处理 |
| W5 | R8/R7 | `render/out/` 两个 HTML 无红线头,且是"双击即可打印外发"的形态,当前还带未填占位符 | 可接受现状(占位符浅黄高亮本身即"未定稿"信号),但建议:目录加 `DRAFT` 标记或 README 一句"out/ 内容填完占位符重渲前禁止外发";已列入放行检查单 |
| W6 | R4 组合风险 | 简历含"运行时安全/概率模型检验/护盾(F1 句)/DTMC/iMDP/PAC"字样;若与鲁版一页纸配套递出,踩 OE1 §3"不堆术语"雷区且暴露孙侧主线;resume 尾部适配提示只讲 bullet 顺序,未讲删句 | F1 修复后大半消解;建议 resume 适配提示补一句:"递鲁场景:'研究方向'行改为'多智能体系统行为分析 × 形式化方法',技能行'概率模型检验工具链'降格或删除" |
| W7 | R1 连带 | 英文 Voice B 参考文献 [1] 描述短语 "probabilistic runtime shielding for LLM agents" 非官方副标题(现版为 "Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction",factcheck 遗留项 L1 提示副标题两说) | 描述性短语不算错;若求稳可改为 "proactive runtime monitoring for LLM agent safety via probabilistic prediction",与 arXiv 现页逐字一致 |
| W8 | R7 | `pipeline_lu.mmd` 按 README 流程导出默认得 `pipeline_lu.svg`,文件名中的 "lu" 若原样发给鲁,暴露"按受众定制材料"的内部命名 | 导出/外发时重命名为中性文件名(如 `mas_log_analysis.svg`);`pipeline_shield.svg` 同理不得出现在鲁场景 |

标注(无需动作):① INTIMA 全集未引用含 companionship 的官方副标题,英文 Voice B [5] 的脱敏描述处理正确;② placeholder_sheet L28/L84 注释中 GPA token 写成半角逗号(与 OE1 原文全角逗号不一致),仅为注释显示问题,不影响替换;③ config 模板段缺 DATE_FULL 键,而 [日期] 不作为正文 token 出现,无实害。

---

## ⑤ 用户拍板后放行检查单

- [ ] **修复确认**:主 Agent 执行 F1–F5 后复核(F1 简历删/改护盾句是先决项,未修不得外发简历)
- [ ] **选声音**:在 `onepager_v2_voices.md` §六勾选 A/B/C(推荐 A 已在档);英文取 `onepager_v2_voices_en.md` **同字母**版本;若选 B,先确认 F2/F3 双语对齐完成
- [ ] **[课题组] 口径**:在 `placeholder_sheet.md` §二"用户说明区"写一句话说明——9 月进组对象与鲁法明邮件是否同一件事(决定一页纸声音与鲁版分工)
- [ ] **量化数字放行**:逐项确认愿意公开——约 8,800 行 / 43 单元测试 / 2,400 条 / 约 4.7 GB(仅 C 版)/ 4,470 行 / 23 核(简历);C 版暴露最多
- [ ] **填占位符**:按 `placeholder_sheet.md` §三抄 `placeholder_config.env` 并填值 → `./fill_placeholders.sh <选定文件>` → 检查输出"残留扫描"为零(选填项留空的,发稿中整句删除)
- [ ] **删说明区**:外发副本中删除全部中文说明区——v1 撰写说明、voices 头部/导读表/推荐意见/§六、voices_en 头部/导读/尾注、lu_variant 任务一与任务三、resume 引言与适配提示
- [ ] **渲染重跑**:选定声音整理为切片约定结构(W4)→ `render_onepager.sh` 重渲 zh/en → 打开 HTML 确认无浅黄占位符高亮、无说明区、名称口径为 ProbGuard 括注版 → 浏览器打印 PDF(边距 None、去页眉页脚)
- [ ] **图导出**:mermaid.live 导出 SVG/PNG;鲁场景仅用 `pipeline_lu` 且导出文件名中性化(W8);通用场景才用 `pipeline_shield`
- [ ] **鲁场景组合自查**:任何鲁触点不得使用 v1/通用声音版;简历如随附按 W6 微调;首封 OE1 邮件默认不附一页纸(lu_variant 任务三既定建议)
- [ ] **OE1 发信包**:按 `OE1_send_kit.md` 时间线执行(8-25 起 BR-1 复查 → 定分支 → 9-7/9-8 上午发送),发信动作用户本人完成

---

*终审完毕。本文件为本次唯一产出;未修改任何稿件,未登 CHANGELOG。*
