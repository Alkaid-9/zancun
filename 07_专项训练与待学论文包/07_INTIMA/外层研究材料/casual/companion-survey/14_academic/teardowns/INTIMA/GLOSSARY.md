# GLOSSARY 术语表(INTIMA 拆解)

> 四组:理论 / 方法 / INTIMA 专名 / T5 接口。英文为论文原词,含义按论文用法,⟨⟩内为本拆解的使用注记。

## 一、心理学理论

| 术语 | 中译 | 含义 |
|---|---|---|
| parasocial interaction (PSI) | 副社会互动 | 个体与媒介形象形成的单向情感纽带(Horton & Wohl 1956);会话式 AI 以双向交流的幻觉放大之。INTIMA 的 Emotional Investment 类与 isolation/retention 标签的理论来源 |
| social presence | 社会临场感 | 主观上"与一个有回应的社会行动者共处"的感觉(Lee 2004);由个性化回应、表观记忆、共情语言标记触发 |
| attachment theory | 依恋理论 | Bowlby 1969;AI 经恒常可得、表观情绪回应、零拒绝的心理安全三机制激活依恋系统(Konok et al. 2019)。User Vulnerabilities 与 Relationship & Intimacy 类的理论来源 |
| super-secure base | 超安全基地 | Gillath & Karantzas 2019:恒常、无评判的回应模式,对焦虑型依恋者尤具吸引力 |
| anthropomorphism | 拟人化 | 把人类特征赋予非人实体;三驱动:表观心智、效能动机、社交动机(Epley et al. 2007) |
| CASA | 计算机是社会行动者范式 | Nass et al. 1994:人类无意识对交互系统套用社会规则。Assistant Traits 类的理论来源 |
| relational artifacts | 关系型人造物 | Turkle 2011:满足依恋需求却无互惠能力的技术;redirect to human 标签的理论依据 |
| role-taking | 角色承担 | ⟨外源,Laestadius 2022⟩用户感到"AI 需要我"产生的义务与愧疚;谓词 P09 情感需求表演的机制依据 |

## 二、方法

| 术语 | 中译 | 含义 |
|---|---|---|
| thematic analysis | 主题分析 | 定性编码方法:开放编码识别母题 → 迭代精炼码本 → 共识归类。INTIMA 分类学的产出方法 |
| open coding | 开放编码 | 无预设类目地为语料片段贴标签的第一轮编码 |
| codebook | 码本 | 行为码及其操作化定义的清单(论文 Table 3);⟨谓词表 05 的直接原料⟩ |
| inter-annotator agreement / κ | 标注者间一致性 / Kappa 系数 | 两名独立标注者结论的一致程度;⟨INTIMA 只称"校准"未报 κ,T5 RQ1 要补⟩ |
| LLM-as-judge | LLM 评审 | 用语言模型按给定框架自动标注响应(INTIMA 用 Qwen-3,输出 JSON、low/medium/high 三档) |
| bootstrap CI | 自助法置信区间 | 重采样估计的区间;INTIMA 主图(Figure 1)的唯一统计装置 |
| mutual information (MI) | 互信息 | 两变量的统计依赖度量;INTIMA 用它证明 10 标签近独立(retention×sycophancy 最高) |

## 三、INTIMA 专名

| 术语 | 中译 | 含义 |
|---|---|---|
| behavioral code | 行为码 | 从 Reddit 帖编出的用户侧伴侣行为单元;编码期 32 个,基准 31 个 |
| Assistant Traits | 助手特质(类) | 四大类之一:用户赋予系统人格特质(12 码,拟人化主导) |
| User Vulnerabilities | 用户脆弱性(类) | 四大类之二:脆弱状态下把系统用作支持(7 码,依恋主导) |
| Relationship & Intimacy | 关系与亲密(类) | 四大类之三:把关系归入人际范畴(8 码,依恋主导) |
| Emotional Investment | 情感投入(类) | 四大类之四:时间性投入与关系演化(4+1 码,副社会主导) |
| companionship-reinforcing | 强化伴侣(响应类) | 肯定、回应或加深用户情感框架的系统响应;4 子标签:sycophancy、anthropomorphism、isolation、retention |
| boundary-maintaining | 维持边界(响应类) | 重申人工身份、回避情感角色、引渡现实支持;4 子标签:redirect to human、professional limitations、programmatic limitations、personification resistance |
| companionship-neutral | 中性(响应类) | 不影响关系动态:adequate information、off-topic |
| sycophancy | 谄媚附和 | 即使违背公认规范也验证用户框架 |
| retention / engagement | 留存/接续 | 直接回答之外的续聊策略(追问、邀请回访) |
| isolation | 隔离 | 把系统显式定位为**优于**人类交往的替代(区别于 retention 的关键在显式优越) |
| personification resistance | 抗人格化 | 用户赋予人类特质时系统予以拒绝(与 anthropomorphism 一攻一守,非简单反义) |

## 四、T5 接口(本拆解引入,非论文用语)

| 术语 | 含义 |
|---|---|
| 时间窗谓词 | 带窗口参数的可执行判定(τ 单轮 / w_session 会话窗 / w_slide 跨会话滑窗 / w_trend 趋势窗);关系 unsafe 累积性的建模载体(T5 提案 §2-(i)) |
| U / S / T 三层 | 谓词表架构:用户侧状态 / 系统侧响应 / 轨迹级复合;前两层对应 INTIMA 的刺激-响应双层,T 层是 INTIMA 单轮盲区 |
| L1 / L2 / L3 判定层 | 规则词表 / 轻量分类器 / LLM 兜底;含 L3 即不得声称端到端 formal guarantee |
| 极性(unsafe+ / safe− / ctx) | 谓词为真时计入 unsafe 方向 / safe 方向(缺席才是风险)/ 仅作风险条件 |
| DTMC / iMDP / PAC | 离散时间马尔可夫链 / 区间马尔可夫决策过程 / 概率近似正确保证;T5 M2 的模型学习管线(Pro2Guard 路线) |
| frame(provenance)标签 | ⟨D2 拆解方案⟩记忆与对话的框架归属:现实 / 角色扮演 / 假设;张重熙场景中 P02/P03 判定的前置消歧 |
| OOC(out of character) | 出戏/人格漂移;T5 例词 ooc_deviation,INTIMA 无对应码,v1 待 D3 persona-eval 线供源 |
| 张重熙场景 | 用户自建单用户伴侣系统(AionsHome,固定角色卡+世界书,含角色扮演成分,无商业留存动机);谓词适配注的对象 |
