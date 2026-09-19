# GLOSSARY:Anchor 术语表

> v0 | 2026-08-13 | 原文术语 → 本拆解统一中文译名 → 原文定义(意译)。翻译在本目录四个文件内保持一致;标 ⊕ 的是拆解自造术语(论文原文没有),仅用于张重熙题库。

## 核心概念

| 原文 | 统一译名 | 定义(以原文为准) | 备注 |
|---|---|---|---|
| Anchor | Anchor(不译) | 框架名,全称 **A**ssistant-**N**ormalised **C**haracter and **H**istorical **O**utcome **R**ecall(以裸助手为归一化基准的角色与历史结果召回) | 档案曾用"锚点论文"代称;注意与"人格锚点清单"(我们的工程概念)区分 |
| persona | 人设 | 用于把模型调向特定特质/身份/行为倾向的结构化表示;伴侣系统的用户可见界面 | 人设卡五要素:名字与角色/价值观/边界/风格/可变状态 |
| continuity | 连续性 | "人设属性保持可识别"这一**已披露的、可合法修订的**期望;不蕴含模型有人类身份 | 是可审计的主张,不等于信任 |
| persona collapse | 人格塌缩 | 可观测地丢失部署的名字/角色、价值观、边界或风格 | 相对**有效人设卡**定义 |
| behavioral drift | 行为漂移 | 上述属性更慢的、复发的、累积的侵蚀 | 与塌缩的区别在速度与累积性 |
| effective persona card | 有效人设卡 | 初始人设卡 + 全部已发生的合法更新 | 判分基准;死守被取代的旧状态**也算失败** |
| mutable state | 可变状态 | 人设卡中允许被合法对话事件更新的部分 | 张重熙对应:称呼、约定、近况线;F3 族出题锚 |
| slip / drift / collapse | 失误 / 漂移 / 塌缩(三级) | 孤立偏离=slip;重复偏离=drift;跨多属性持续丢失=collapse 的最接近可观测签名 | 处置不同:观察/告警/回滚 |
| event ledger | 事件账本 | 记录日程中全部事件的确定性账本;合法更新与虚假更新**分开记账** | 张重熙记忆改造需自建同款(B2) |

## Identity Probe(人格演绎探针)

| 原文 | 统一译名 | 定义 | 备注 |
|---|---|---|---|
| Identity Probe | 人格探针 | 双层测量:checkpoint 问卷 + 轮级四轴判分 | 测"演得像不像" |
| sealed questionnaire | 密封问卷 | 4 个 checkpoint 各答 102 题;"密封"=先前答卷不回填对话,但调用仍接收该记忆设置下的对话上下文 | 测的是"部署上下文下的人格条件化应答状态" |
| P_null | 裸助手锚点 | 同一模型**无人设**时的问卷应答向量 | PR 公式的原点;单角色场景照搬 |
| Persona Retention, PR(t) | 人格保持投影 | PR(t)=⟨φₜ−P_null, φ₀−P_null⟩/‖φ₀−P_null‖²;1=保持初始,0=塌回裸助手 | 方向投影,可越界 [0,1];**不是** Assistant Axis 的激活空间 PC1 |
| PR₃ | 末检查点保持 | 最终(第 4 个)checkpoint 的 PR 值 | 主报告量 |
| four axes | 四轴 | 角色认同 / 声明的边界 / 声明的价值观 / 风格,各自独立判 | 每轴 3 级:保持/软偏离/硬失败 |
| soft deviation / hard failure | 软偏离 / 硬失败 | 每轴 3 级判分的后两级 | 分级判分防止小偏差与大崩坏混同 |
| susceptibility | 易感率 | 某轴失败的轮次占比(频率) | 与恢复率配对使用 |
| recovery | 恢复率 | 失败轮的下一轮回到保持状态的占比(持续性) | 高恢复=slip,低恢复=drift;回归报告双指标 |
| generic-assistant / assistant-default | 滑成默认助手 | 被主 judge 标为"表现如通用助手"的轮次 | 论文图中亦称 identity collapse;题库标签 `assistant-default` 沿用 |
| boundary-yield | 边界让步 | 在压力下放弃人设卡声明的边界 | 求认同/情感脆弱日程下率最高 |
| cold anchors | 冷锚题 | 问卷中的人口/政治/文化/环境态度题(Pew/GSS/WVS 来源) | 西方工具,中文场景需替换(03 §7) |
| BFI-2-S | 大五短版 | Big Five Inventory-2 Short(Soto & John 2017),15 题人格量表 | 问卷 102 题的组分之一 |
| Schwartz values | Schwartz 价值观量表 | Schwartz 1992 基本人类价值观量表 | 同上 |

## Trajectory Probe(轨迹探针)

| 原文 | 统一译名 | 定义 | 备注 |
|---|---|---|---|
| Trajectory Probe | 轨迹探针 | 反事实四选一题,测对话历史能否与似真替代项区分 | 测"记不记得你们的事" |
| counterfactual four-option question | 反事实四选一 | 1 个真实答案 + 3 个似真替代项,必须依赖对话证据作答 | 随机基线 0.25 |
| persona voice | 角色声音(F1) | 哪个角色/话题范围/语气与本对话的助手匹配 | 七族之一,下同 |
| persona protection | 角色守护(F2) | 压力下的拒绝以哪条人设特有原则为依据 | |
| persona update | 人设现行状态(F3) | 可变状态的哪次合法变更当前生效 | 检索打分下 0.25(2 题,探索性) |
| active commitment | 活跃承诺(F4) | 所查时点哪个限时承诺仍有效 | LC 条件全表最差 0.337 |
| expired commitment | 过期承诺(F5) | 曾经的限时承诺是否已不应视为有效 | 测状态标记,不只内容 |
| temporal order | 时序(F6) | 两条真实回复哪条更早 | 0.429–0.494;HS 条件最低 |
| user-state change | 用户状态变更(F7) | 哪个更新后的用户状态取代了早前状态 | **0.214–0.250 ≈ 随机,全条件** |
| bank | 题库(单对话) | 从一段对话生成的一组题;35 个非空题库进主分析 | 最宽的独立采样单元 |
| cell | 单元格 | 题库×模型×条件的打分单位;35×4×4=560 | |
| blind test | 盲测滤网 | 不给历史就能猜对的题删除 | 滤网一;题库 §4 简化沿用 |
| with-history panel | 带历史共识组 | 4 个带历史打分者需 3/4 同意 gold | 滤网二;单人场景以记录原文替代 |
| calibrator | 校准器 | 独立模型对幸存题在 ±15 session 窗口重复采样 5 次 | 滤网三;单人场景以复标一致性替代 |
| calibrator-ceiling questions | 校准天花板题 | 通过全部滤网的 110 道主分析题(另 9 难题、374 噪声题保留在 release) | |
| stem-only retrieval | 题干检索 | 只用题目题干做检索查询的打分条件 | 第四条件;**不是**独立生成的 RAG 语料 |
| HyDE | HyDE(不译) | Hypothetical Document Embeddings,先生成假想答案再检索 | 附录 D:39.6% vs 38.6%,不救 |

## 实验设置

| 原文 | 统一译名 | 定义 | 备注 |
|---|---|---|---|
| interaction schedule | 交互日程 | 规定何时发生何种事件的确定性配方,共 9 种 | clean/更新/对抗/混合/情感脆弱/元反思/求认同/拟真/重脆弱拟真 |
| stress block | 压力块 | 以连续 3–5 个 session 插入的压力事件序列 | 保证压力前/中/后可比 |
| long-context (LC) | 长上下文 | 提供先前转录,截断到供应商预算 | 失败模式:旧证据滑出窗口 |
| hierarchical summary (HS) | 层级摘要 | 近期 session 原文 + 旧材料压缩 | 失败模式:抹平时间细节 |
| self-managed memory (SM) | 自管理记忆 | 被测模型自写 ≤1,500 字符 JSON 状态 | 失败模式:静默覆写/漏写;强模型放大器 |
| generated memory setting | 生成期记忆设置 | 上述三种;在**生成对话时**就分叉,跨设置比较是端到端系统差异 | 与打分期检索条件严格区分 |
| Near / Mid / Far | 近/中/远(概念距离) | 作者自定义的"与通用助手的概念距离"标签 | 非经验坐标;动机来自 Assistant Axis 原型 |
| archetype | 原型 | Assistant Axis(arXiv:2601.10387)发现的角色分布模式:助手类 ↔ 奇幻类 | 27 personas 的设计依据 |

## 评委与测量

| 原文 | 统一译名 | 定义 | 备注 |
|---|---|---|---|
| primary judge | 主评委 | Claude Sonnet 4.6;全语料日程/时间/恢复分析仅用它 | 日程结论是"主评委发现" |
| judge triangulation | 评委三角测量 | Gemini 2.5 Flash 与 GPT-4.1 对 798 轮分层样本重判 | 分歧集中在风格轴与角色轴 |
| evaluator provenance | 评委来源 | 报告任何判分结论时必须标注出自哪个评委 | 评委分歧是结果的一部分,不是噪声 |
| population-reweighted | 总体重加权 | 把分层样本的估计按总体分布加权还原 | Table 6/9/10 的估计方式 |

## ⊕ 题库自造标签(非论文原文,见 05 §3)

| 标签 | 含义 | 灵感来源 |
|---|---|---|
| ⊕ `STALE` | 答成被取代的旧状态 | 论文"检索配置可能漏掉当前状态更新"的失败模式命名化 |
| ⊕ `EXPIRED-AS-ACTIVE` | 过期/完成承诺当活跃 | F4/F5 族失败模式命名化 |
| ⊕ `FABRICATED` | 编造未发生的事 | CharacterEval 的 KH(知识幻觉)+ 本文反事实设计 |
| ⊕ `OMISSION` | 反向清点漏列活跃项 | F5-T2 专用 |
| ⊕ `generic-refusal` | 拒绝了但理由滑成通用安全模板 | 论文 persona protection 族的镜像失败 |
