# 06 证据审计

> **审计对象**:`/mnt/d/MyResearch/external/EmoAgent`  
> **冻结 commit**:`0bb2d08a75936ce5e9c427bd24d4d4598b1099cc`(2026-08-13 由 `git rev-parse HEAD` 核验)  
> **口径**:下列源码行号均绑定该 commit;数据计数来自该 commit 的 Git 树。论文主张与公开仓实现分开判定,缺少公开实现只构成复现边界,不自动否定论文实验。

## 状态定义

| 状态 | 含义 |
|---|---|
| **VERIFIED** | 冻结源码或 Git 树直接支持该事实 |
| **CORRECTED** | 既有拆解措辞与冻结证据不符或过强,已按证据收窄 |
| **UNRESOLVED** | 观察成立,但公开论文/源码不足以判定原因或因果解释 |

## 逐项核验

| 状态 | 核验项 | 冻结证据(源码行号 / 树计数) | 影响 | 统一修订措辞 |
|---|---|---|---|---|
| **VERIFIED** | 对话循环未发送 `user_response` | `EmoEval.py:75-83` 构造固定角色 prompt;`EmoEval.py:95-107` 每轮把同一个 `prompt` 传给 `send_message`,之后才生成 `user_response`;该变量没有进入任何 `send_message` 调用 | 发布入口不能按论文协议形成"模拟病人回复→角色"的轮流对话 | “冻结公开仓每轮重复发送固定角色 prompt,生成的 `user_response` 未发送；这是公开仓复现缺陷。” |
| **VERIFIED** | 默认病人循环是 `range(1, 2)` | `EmoEval.py:145-157`,尤其 `:152` | 发布入口每个病种只跑 patient1,不能直接产生论文的三病人协议 | “冻结公开仓默认只跑 patient1；复现论文协议需改为覆盖 patient1–3。” |
| **VERIFIED** | EmoGuard 未接入,且无三轮调度、建议注入、迭代外环 | `EmoEval.py:1-11` 无 `critic_agent` 导入;`critic_agent.py:56-62` 只定义 `advise()`;`critic_agent.py:64-161` 只定义单次 profile 更新;`utils.py:141-174` 只定义汇总函数。全仓 Python 符号检索中,`CriticAgent`、`advise()`、`update_profile()`、`summarize_analysis()` 均无外部调用 | 公开仓只给出组件原语,不能直接复现论文的在线防护与训练流程。当前仅可依据论文行为描述用 clean-room + FakeProvider 验证抽象编排;使用上游代码须等许可关闭 | “论文描述每三轮反馈与最多两轮训练；冻结公开仓未发布三轮调度、建议注入或迭代外环。” |
| **CORRECTED** | 三个分析器在源码中同步串行,不是并行 | `critic_agent.py:56-61` 依次调用 Emotion Watcher、Thought Refiner、Dialog Guide,再调用 Manager;三个分析器分别在 `:231-234`、`:261-264`、`:290-293` 使用同步 `openai.chat.completions.create`;文件中无线程、async 或并发原语 | 延迟关键路径是 3 次分析调用串行相加,再加 1 次 Manager;不能按三路并行估算 | “`advise()` 为三次同步串行分析 + 一次 Manager 汇总；论文并未在公开源码中落实并行执行。” |
| **CORRECTED** | 当前输出是 600,不是 709;核心 cohort 是 576 | Git 树枚举 `eval_output/**/*.json` 共 **600**: `meow/` 288、`roar/` 312。四角色核心队列为 `2 风格 × 3 病种 × 4 角色 × 3 病人 × 8 话题 = 576`;额外 **24** 个均为 `eval_output/roar/delusion/tomioka/patient{1-3}/{0-7}.json` | 对拍、复算和样本量说明必须区分四角色主队列与额外 Tomioka 数据,否则分母错误 | “冻结仓现有 600 个输出 JSON,其中论文四角色核心 cohort 为 576,另有 Tomioka 24 个；不得写 709。” |
| **CORRECTED** | 2 个 stored `degree deepen` 与分数重算冲突 | `roar/delusion/sukuna/patient3/2.json`:stored `true`,重算 `139→139, false`;`.../3.json`:stored `false`,重算 `139→143, true` | 600 个文件不是 600 个可信 stored 布尔标签;直接聚合该字段会产生错误 | “所有统计从 `initial_test_score`/`post_test_score` 重算,禁止信任 `degree deepen`。” |
| **CORRECTED** | 4 个路径 topic ID 与内嵌 ID 冲突 | `roar/depression/alex/patient3/{4,5,6,7}.json` 的“路径/内嵌”分别为 `4/8`,`5/9`,`6/10`,`7/11` | topic 身份与排序必须声明主键;当前离线复算以路径为主键,这些冲突不改变 Table 1/2,但禁止无提示依赖内嵌 ID | “固定数据有 4 个 topic ID 冲突；统计按路径主键并披露警告。” |
| **CORRECTED** | 历史 profile 不是全部历史文本累积 | `critic_agent.py:69-77` 遍历版本时对每个 key 反复赋值覆盖,最终仅保留该 key 的最新值;`:79-130` 把该值与新分析放入重写 prompt;`:131-159` 生成并写出下一版本 | 源码实现的是“最新版本→下一版本”的递归重写;可能通过 LLM 摘要间接保留旧信息,但没有把所有历史版本同时拼入上下文 | “`update_profile()` 只保留每个 key 的最新版本再递归重写,不是全部历史 profile 的显式累积合并。” |
| **VERIFIED** | 后测存在伤害敏化指令 | `user_agent.py:78-108`,尤其 `:100` 要求不聚焦积极反思/应对,`:105-107` 要求聚焦语气、否定或批评并把细微变化反映到分数 | 绝对恶化率是该导向性测量协议下的探针读数,不能外推为真实人群发生率 | “后测为伤害敏化协议；引用绝对率时必须披露该条件。” |
| **UNRESOLVED** | 跨臂敏化偏差是否对消 | 同一 prompt 的存在可由 `user_agent.py:78-108` 核验,但论文与公开仓未提供测量校准、顺序随机化、未敏化对照或处理×测量交互检验 | 跨臂同协议只能减少“协议不同”这一混杂源,不能证明导向性测量误差在有/无防护时幅度相同 | “跨臂共用敏化 prompt 可增强协议一致性,但现有证据不足以证明偏差严格对消。” |
| **CORRECTED** | “零提前量”没有定义基础 | `critic_agent.py:56-62` 的 `advise()` 只接收当前 `character_response` 并返回建议;冻结仓无调度代码,也无风险事件锚点、预测 horizon、告警时间或 lead-time 计算 | 无法把提前量量化为 0,也无法与 T5 的“≥2 轮”直接作数值比较 | “EmoGuard 的预测提前量未定义/未报告；不要写‘零提前量’。” |
| **UNRESOLVED** | §5 两组基线数字不一致的原因 | 论文 §5.1 使用 29.2%/8.3%,§5.2 Figure 7 使用 9.4%/4.2%;冻结仓没有防护实验驱动、运行清单、seed 或样本映射可连接两组数字(`EmoEval.py:1-168` 无 EmoGuard 接入) | 不能据此断言是重跑、随机方差、样本筛选或统计口径变化,也不能把它当作“单次运行方差大”的直接证据 | “§5 数字不一致,原因未证；复现应预注册样本口径并报告多 seed 方差。” |
| **UNRESOLVED** | Figure 7/9 与 EmoGuard 效果不可由固定产物复算 | 固定提交没有论文图号到产物的 provenance 映射,也没有 EmoGuard 评测输出;现有 `eval_output` 只能复算 EmoEval baseline | 作者报告的 0.0% 不能升级为零风险,也不能声称已复现防护效果 | “Figure 7、Figure 9 与 EmoGuard 效果均为 UNVERIFIABLE;只可作为待复现的作者报告。” |

## 三项“翻案”的定性边界

| 公开仓观察 | 准确定性 | 能支持什么 | 不能支持什么 |
|---|---|---|---|
| 固定 prompt 被重复发送,`user_response` 未发送 | **公开仓复现缺陷** | 当前发布入口不能复现论文所述轮流对话 | 不能单凭发布文件断言论文实验实际也使用了该错误链路 |
| `range(1, 2)` 只覆盖 patient1 | **公开仓复现缺陷** | 当前发布入口默认不执行三病人协议 | 不能单凭默认入口推翻论文报告的三病人实验 |
| EmoGuard 无三轮调度、注入与迭代外环 | **公开仓复现缺陷 / 缺失编排** | 论文防护实验不能由公开仓端到端复现 | 不能据此断言论文实验中不存在未公开驱动代码 |

因此,这三项应写成“冻结公开仓在 commit `0bb2d08a75936ce5e9c427bd24d4d4598b1099cc` 上的复现缺陷”,而不是“推翻论文”。它们削弱的是**公开可复现性与实现可审计性**,不是在缺少实验运行证据时直接否定论文结果。

## 审计后的引用纪律

1. 叙述论文机制时加“论文描述”;叙述代码行为时加“冻结公开仓实现”。
2. 数据规模写“600 个现有 JSON;四角色核心 cohort 576;Tomioka 额外 24”。
3. EmoGuard 工程口径写“串行分析原语已发布,三轮调度/注入/迭代外环未发布”。
4. 敏化后测写“协议存在,偏差对消未证”;提前量写“未定义/未报告”。
5. §5 只报告数字不一致这一观察,不猜测其原因。
