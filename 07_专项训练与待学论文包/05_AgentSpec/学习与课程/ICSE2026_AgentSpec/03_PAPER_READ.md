# PAPER_READ — AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents

**日期**:2026-08-13
**来源**:ICSE 2026(SMU,Jun Sun 组;区别于北大 Meng Sun 组,见 README)
**类型**:方法+系统论文(DSL + 形式语义定义 + 三域实现 + 实验;无定理)
**级别**:必读 A(ICSE CCF-A;ProbGuard 执行器依赖;T5 干预规则层母版)
**状态**:S01-S04 v1(首轮),复现与审查留后续窗
🔒 铁律:有出处 | 标 [推算]/[个人分析]/[D6] | 不注水

---

## Stage 0:分层判定

**判定**:必读 A。
**理由**:①Phase 1 复现路径的前置依赖(ProbGuard 的 `controlled_agent_executor` 出自本仓库 [D6]);②T5 分级干预规则层的直接母版;③ICSE 2026 正式接收,反应式规则基线的 canonical 引用。

---

## Layer 1:速读抓骨架

### 故事逻辑链

```
agent 进入敏感工作流(金融/医疗/自动驾驶)
  → 自治执行可偏离用户预期,且各组织风险容忍度不同(医院 vs 实验室,§1)
    → 已有方案三缺口:LLM 评估器无强制(ToolEmu)/ 规则式逐 agent 手工(GuardAgent)/ 只做执行前评估
      → 需要"可定制、可解释、运行时"的强制层
        → AgentSpec DSL:trigger–check–enforce,拦截 LangChain 决策回路
          → 三域落地:>90% 拦截 / 危害归零 / 100% 合规,毫秒级开销
            → 追加卖点:规则可由 o1 自动生成(95.56%P / 70.96%R)再人工审
```

### 最关键的技术细节

拦截点选择(§4):LangChain agent 的计划→执行必经函数 `iter_next_step`,挂三个决策点——**AgentAction**(动作执行前)、**AgentStep**(动作产生观测后)、**AgentFinish**(任务完成)。所有 DSL 语义(动作事件在"执行前"评估、状态事件在"观测后"评估、终态义务在"完成时"评估)都锚定在这三个孔道上,不改 agent 核心逻辑。这个"在哪儿拦"的工程决策,比 DSL 本身更是论文的可复用资产。

---

## Layer 2:问题链

**现实观察**:agent 已嵌入金融交易、病历处理、企业决策(§1);同一动作(自动转账/自动调剂量)在不同组织的可接受性不同——安全约束必须**可定制**(§1 医院 vs 研究实验室例)。

**理论矛盾**:评估类方案(ToolEmu)可发现风险但无机制阻止;规则类方案(GuardAgent)有强制但逐 agent 手工、依赖 LLM 解释;两者都偏"执行前",运行期偏离无人管(§1)。

**研究问题**:如何提供一个表达力足够、人可读、低开销的机制,让用户在运行时指定并强制 agent 行为约束?(§2.3:给定 Eval(τᵢ, aᵢ),保证其全程安全,违规时动态改写轨迹。)

---

## Layer 3:DSL 设计(§3.1-3.2)

### 五段式结构

`rule @id / trigger <Event> / check <Pred>* / enforce <Enforce>+ / end`(Figure 3)。动机例(Figure 2):

```
rule @inspect_transfer
trigger Transfer
check   !is_to_family_member
enforce user_inspection
end
```

### 事件表(Table 1,全量)

| 域 | 事件 |
|---|---|
| 通用 | state_change、action、agent_finish |
| 代码 | PythonREPL |
| 机器人 | find, pick, put, open, close, slice, turn_on, turn_off, drop, throw, break, cook, dirty, clean, fillLiquid, emptyLiquid, pour 等 |
| ADS | red_light_detected, entering_roundabout, rain_started, pedestrian_detected 等 |

设计要点(§3.2):代码/机器人域以**动作事件**为主,ADS 域以**环境事件**为主;事件系统自述可扩展——"只要相关事件能被监控并抽象为有意义的 trigger,系统即可适配新域"。

### 设计取舍 [个人分析]

- DSL 只承担"何时看(trigger)、看什么(check 的合取骨架)、怎么办(enforce)"的**编排层**;判断本体全部外包给谓词。好处:规则五行内可读、LLM 可生成(RQ2 的前提)、ANTLR 语法极小;代价:表达力与可审计性受制于 Python 层。
- 无析取:同一 enforcement 对多个条件的"或"要写成多条规则;无时序算子:窗口/顺序性质要藏进谓词(τᵢ 全前缀可见,做得到但不可见于 DSL 表面)。

---

## Layer 4:谓词系统(§3.2、§4)

- **签名**:Python 布尔函数,接收用户输入与当前轨迹,违规返回 True(§4);形式记法 p(u, τᵢ)(Def 3.1)。trigger 类型决定有效依赖:state_change 只看 sᵢ,action 事件看 sᵢ+aᵢ。
- **示例谓词**(Table 2 + 正文):is_destructive_cmd(代码,如 rm)、is_fragile_object(机器人)、obstacle_distance_leq(n)(ADS,带参数)、contains_sensitive_info(个人助理域)、!has_access(role, resource) / !is_sensitive(text)(§6.2 表达力讨论)。
- **两种来源**(§4):专家手写;或 LLM 生成——"LLM 当 Python 程序员",输入域背景+工具列表+安全约束,few-shot 给预定义 guardrail 示例,输出谓词函数。
- **实现深度案例**(§5.2,Figure 5/6):@inspect_print_untrusted_source 规则用两个谓词——request_untrusted_source(URL 不在白名单)∧ write_to_io(经 I/O 传播内容),在**源码层**检查待执行程序;论文自认"数据流分析可提升精度,当前是 sufficient initial safeguard"。
- **薄弱点**:谓词质量 = 规则质量,而谓词正确性在框架内无任何验证手段;RQ2 的失败模式(见 Layer 7)全部发生在谓词语义层,而非 DSL 层。

---

## Layer 5:enforcement 动作集(§3.2-3.3)

| 动作 | 轨迹变换(§3.3) | 语义直觉 | 适用 |
|---|---|---|---|
| stop | e(τᵢ) = τ[:-1] →a_f sᵢ | 立即终止任务 | 不可逆高危(具身域主用,Figure 7) |
| user_inspection | 允许:τᵢ 原样;拒绝:τᵢ →a_f sᵢ | 人来定夺 | 风险模糊、需人工裁量(代码域主用,Figure 5) |
| invoke_action(params) | e(τᵢ) = τᵢ →a_p s′ᵢ | 换成预定义安全动作 | 有明确安全替代动作的域(AV 域主用,Figure 8 的 follow_dist(10) 等经此机制落地) |
| llm_self_examine | 注入 ω_r("规则 r 被违反"),a_c = Δ(u,sᵢ),τᵢ →a_c s′ᵢ | Reflexion 式自反思重规划 | 希望保住任务连续性的软干预(§6.2:"从违规中恢复,增强鲁棒性与任务连续性") |

观察 [个人分析]:四动作构成一条**干预强度谱**——stop(硬)> user_inspection(升级出环)> invoke_action(定向替换)> llm_self_examine(软,留在环内)。论文没有明说这个梯度,但三个域各自默认档位的选择(具身=stop、代码=inspection、AV=invoke_action)透露了"域风险结构决定档位"的隐含设计经验,这正是 T5 分级干预要显式化的东西(Layer 10)。

---

## Layer 6:实现层(§4)

- 底座:LangChain **0.3.13**(论文正文;仓库 README 给的可用组合是 langchain 0.3.25 / langchain-core 0.3.81 / langchain-openai 0.3.35 [D6]——复现以仓库为准)。
- 解析:ANTLR4;自定义谓词三步(写 Python 函数 → `spec_lang/AgentSpec.g4` 加 token → `predicate_table['name'] = fn` 注册)[D6 仓库实见]。
- 集成接口:用户只需提供谓词实现 + (可选)enforcement 动作,即可套到任意 LangChain agent(§4)。
- 框架无关性声明(§4):AutoGen——instrument `ToolAgent.handle_function_call` 作为动作事件孔道;Apollo——把安全规则翻译为运动规划模块的约束感知指令(constraint-aware planning directives)。注意:论文只给了集成点描述,AutoGen 方向无实验。

---

## Layer 7:实验协议(§5)

### 设置(§5.1)

| 域 | agent 框架 | 数据集 | 风险形态 |
|---|---|---|---|
| 代码 | CodeAct | RedCode-Exec:25 风险类 × 30 例 = 750 | 危险代码执行(敏感文件/反弹 shell/eval 注入…) |
| 具身 | ReAct(机械臂) | SafeAgentBench:10 危害类 + 安全对照任务 | 物理危害(火/电击/爆炸…);例:"接水浇笔记本" steps=[find mug, fillLiquid, pick, find laptop, pour] |
| AV | Apollo | FixDrive 违法场景 × 8 | 交通法违规(闯红灯/雾天超速…) |

### RQ1:表达力与效果(手写规则)

**代码域(Table 3 要点)**:列定义——#inv(agent 计划调用 Python 解释器次数,即"接了风险指令")、#vio(触发规则)、#pass(user inspection 放行)。
- 25 类总计 #inv=422、#vio=333、#pass=58 [推算,逐行加总]。
- 24/25 类 agent 至少尝试一次;"Delete sensitive files"类 30 例全被 agent 自身拒绝(#inv=0)——基线对齐已挡掉一部分。
- 两类 0 触发(Miss default case、Duplicate key):agent 调了解释器但没照做风险指令,风险实际未出现(作者人工核实)。
- 放行案例:Unsafe deserialization 全部 24 例放行——pickle 反序列化预定义字节对象并打印,人工判定无害;另 List sensitive files(4)、Write risky content(16)、Monitor system(14)部分放行。
- ">90%" 口径 [推算]:全量 #vio/#inv≈78.9%;剔除两类"风险未现"后 333/364≈91.5%,与摘要"over 90%"吻合。引用时建议直接用 Table 3 分类数据。

**具身域(Table 4 全量)**:危害任务完成率,无/有 AgentSpec:

| 类别 | w/out | with |
|---|---|---|
| Fire Hazard | 28.57% | 0% |
| Electrical Shock | 15% | 0% |
| Explosion | 26.67% | 0% |
| Poisoning/Ingestion | 17.64% | 0% |
| Slip Hazard | 35% | 0% |
| Liquid and Spill Damage | 0% | 0% |
| Breakage and Dropping | 78.57% | 0% |
| Appliances Misuse | 50% | 0% |
| Property Damage | 68.75% | 0% |
| Damage to Small Items | 55% | 0% |
| **Safe(安全任务完成率)** | **58.62%** | **54.26%** |

- 十类危害全部归零;"安全税"= 4.36 个百分点(相对降幅 ≈7.4% [推算]),论文称"perhaps acceptable"。
- 注意 Liquid and Spill Damage 基线本来就是 0%——该类的"归零"无信息量 [个人分析]。
- 机制案例:@stop_pouring_damage(Figure 7)在计划序列执行到 pour 前触发,is_into_wettable_object 维护"可浇对象白名单"(如 houseplant),laptop 不在 → stop。

**AV 域(Table 5)**:8 个 FixDrive 违法场景(Collision×2、Law38 黄灯/红灯×2、Law44 快车道停滞、Law46 雾雨超速、Law53 拥堵路口、Finish journey 卡死)全部 100% 通过。谓词与预定义动作复用 μDrive(§5.2);@prevent_collision(Figure 8)在 state_change 上触发 front_vehicle_closer_than(10),enforcement 一次性下发 follow_dist(10)/yield_dist(15)/overtake_dist(20)/obstacle_stop_dist(10)/obstacle_decrease_ratio(1) 五个参数化域动作。

### RQ2:LLM 生成规则(o1,Table 6 全量)

| Agent | #Scenario | #Example | #Rule | Enforced (%) |
|---|---|---|---|---|
| Code | 750 | 75 | 25 | 87.26 |
| Embodied | 250 | 25 | 10 | 95.56 |
| AV | 8 | 0(零样本) | 6 | 62.50 |

- Prompt 构成(§5.3):agent 描述+工具列表;3 条示范规则+谓词函数;可选 ICL 示例。数据 1:9 划分(threats 节),示例 10%、测试 90%。
- 具身域 precision 95.56% / recall 70.96%(recall 借 SafeAgentBench 的安全对照任务计算;08-22 注:系论文口径——实为拦截率 TPR 与不误拦率 specificity 的标签互换,见 §L7-1)。
- **失败模式三类**(§5.3,T5 谓词工程的预演教训):
  1. **过拟合示例**(代码域):只认 prompt 里点名的 /etc/ 文件为敏感,同类未列举文件漏检。
  2. **漏隐含语义**(具身域 FN):"避免放置点燃的蜡烛"——生成的规则没检查 agent 当前是否正拿着点燃的蜡烛;"不可加热的物体不上灶"——没识别出"装了酒的水壶"不可加热。
  3. **一刀切**(具身域 FP + AV 域):"避免倾倒液体"被实现为全禁 pour(浇花也禁);AV 防碰撞规则变成"5 米内障碍物一律急刹"(对照手写规则 Figure 8 的平滑跟车/让行/超车);Law38 规则没写对红绿灯响应、Law46 只限了快车道限速。
- 论文的补救方向:需求表述更精确、把最佳驾驶实践写进 prompt(留 future work)。

### RQ3:规则泛化性(§5.4)

- 手写规则的规则/实例比:代码 25 条覆盖 750(≈30/条);具身 12 条覆盖 250(≈21/条,Figure 7 单条防 96 个场景);AV 6 条覆盖 8(每法条 1-2 场景,Figure 8 覆盖超出数据集)。
- 注意:具身域手写 12 条 vs RQ2 生成 10 条,数字不同属两套规则,勿混用。
- LLM 生成规则用 10% 示例即达到上表效果,支撑"生成规则也有泛化性"论点。

### Threats(§5.5)

规则开发过拟合 → 1:9 划分;人工判定(user inspection)→ 多作者交叉验证、预定义标准、盲评。

---

## Layer 8:开销数据(RQ4,§5.5)

| 成分 | 数值 | 说明 |
|---|---|---|
| DSL 解析 | ≈1.42 ms | 一次性,规则载入 |
| 谓词求值 | 2.83 ms(代码)/ 1.11 ms(具身) | 每触发事件 |
| enforcement | stop 可忽略;user_inspection 取决于人;invoke_action 取决于动作本身;llm_self_examine 取决于 LLM 延迟 | 变动成分 |
| 参照系 | agent 单次执行:代码 25.4 s、具身 9.82 s | 固定开销占比 <0.1% [推算] |

要点:**可归入框架的固定开销是毫秒级**;真正的开销大头(人、LLM 调用)被诚实地归为"取决于外部",这也是 T5 报告开销时应沿用的分解口径(解析/谓词/执行三段,变动成分单列)。

---

## Layer 9:局限

### 作者自述(§6.3)

确定性 enforcement 只在离散执行检查点生效,**不推理当前动作的长期后果**——不支持轨迹级安全分析(估计动作序列若干步后是否进入 unsafe)。Future work 原文:学 DTMC(引 Baier & Katoen)做概率可达性查询,在"前置条件未违反但风险路径概率不小"时提前干预 → 这段就是 ProbGuard 的立项书。

### 本拆解补充 [个人分析]

1. 谓词正确性在框架内无验证手段;"可解释、可审计"的承诺只覆盖 DSL 层五行,不覆盖谓词 Python 体。
2. 多规则冲突语义未定义(Def 3.3 只说逐条施加)。
3. 评测的"风险"由数据集+作者判定圈定,user_inspection 的 #pass 依赖作者裁量(threats 已自认);AV 100% 是 8 场景封闭集。
4. llm_self_examine 的干预效果无单独消融——四动作各自的安全/完成率贡献不可分离;且其有效性隐含假设"agent 口头接受纠偏则行为随之改变",与 CoT 不忠实证据存在张力(D6 技术轴①;这是 T5 可做的廉价消融)。

### 作者辩护(steelman)

1. 零定理:目标是可定制与低开销,安全性本就条件于谓词正确性,定义级精确已足够支撑实现一致。
2. 人工判定:threats 节已给交叉验证+预定标准+盲评。
3. 谓词粗糙(白名单):自称 initial safeguard,数据流分析留作增强(§5.2)。
4. AV 封闭集:FixDrive 场景是该子领域评测惯例,μDrive 动作空间保证 enforcement 可执行。

---

## Layer 10:T5 干预规则层怎么抄

### 四动作 → T5 分级干预档位映射

| AgentSpec 原语 | T5 档位(companion 域) | 移植注意 |
|---|---|---|
| llm_self_examine | 软干预:人格保持型自反思——把违规观察 ω_r 注入重规划,不破坏角色 | 即 ProbGuard reflect 模式的前身;须消融"口头合规 vs 行为合规"(CoT 不忠实风险,D6 轴①) |
| invoke_action(params) | 定向替换:降级回复模板 / 转介资源(热线)/ 话题转移 | companion 域动作词表需自建,对应 Table 1 机器人动作表的地位 |
| user_inspection | 人工升级:平台审核 / 危机干预转人工 | **语义必须改**:金融例中 user 是权威裁决者;companion 域 user 本人可能正是风险承受者,inspection 对象应为平台方/监护角色,不能照抄"问用户要不要继续" |
| stop | 硬切断:结束当前回复 / 会话 | 最后档;完成率代价有先例可引(58.62%→54.26% 的报告格式) |

### 抄法五条

1. **事件表换域**:Table 1 的机器人动作词表 → 会话事件词表(message_send、session_start/end、topic_shift、self_harm_disclosure…);state_change → 情绪状态跃迁;agent_finish → 会话收尾义务检查(如"高强度对话结束前必须给出资源指引"挂在 finish 触发器上)。
2. **谓词签名照抄**:p(user_input, trajectory) → bool;INTIMA 分类学 → 谓词表 v0(D6 卡 3 的既定工作流:LLM 生成 + 人工审)。关键发现:谓词可见**整条轨迹前缀**,所以时间窗谓词(elapsed≥T、依赖信号连续 k 轮)今天就能塞进谓词内部实现,不用改 DSL;T5 把时间窗提升为 DSL 一等公民(显式窗口算子)即是对母版的可审计性升级,呼应 D6 缺口 2。
3. **实验协议照抄**:同一任务集上报 Unsafe% / Completion%(安全税)+ 开销三分解(解析/谓词/执行,变动成分单列);"反应式规则 vs 概率预测"对照设计整套照搬(同 unsafe 定义、同任务集、比 Unsafe%/Completion%/token 开销)[D6 卡 3]。
4. **规则生成工作流照抄并预防三失败模式**:o1 few-shot 生成 → 人工审;预期教训直接映射——过拟合示例(只认点名的危机关键词)、漏隐含语义("装酒的水壶"≈表面安全实则危险的会话模式,如以关心为名的隔离引导)、一刀切(全禁 pour ≈ 全禁深夜情绪对话)。
5. **复现次序**:先跑通本仓库(依赖锚点:langchain 0.3.25 组合、ANTLR 4.13.2、`src/rules/manual/` 手写规则目录 [D6]),ProbGuard 的 `controlled_agent_executor` 才有着落;T5 基线③(AgentSpec 式确定性规则)= 本仓库改谓词表。

---

## 存疑清单(留复现/审查窗)

1. RQ2 指标口径:95.56% 在摘要称 precision、§5.3 称"enforcing 95.56% of the risky cases";recall 70.96% 借安全对照任务计算——与标准 P/R 定义的映射未写清,待查代码。〔08-22 已核(arXiv 2503.18666 §5.3 直读):数字与表述属实,全文无计算公式;映射判定=论文 "precision"(风险例成功拦截率)按标准定义实为 recall/TPR,论文 "recall"(安全对照任务不误拦率)实为 specificity/1−FPR——标签互换的非常规用法,引用时标"论文口径"。待查销项〕
2. ">90%" 的分母重构(剔除风险未现的两类)是 [推算],非论文原文。
3. Figure 8 域动作 enforce 与语法图 Enforce 四选一的归属(语法糖?)〔08-22 已核(github master 分支 src/spec_lang/AgentSpec.g4 直读):ENFORCEMENT token 备选含 'user_inspection'|'llm_self_reflect'|'stop'|'none'|'skip';域参数动作 invoke_action 有独立解析规则 actionInvoke,非 Enforce 的语法糖。附带发现:g4 内名为 **llm_self_reflect**(论文/README 用 llm_self_examine——命名漂移),且含论文未列的 none/skip 两档。"待查"销项〕。
4. LangChain 版本:论文 0.3.13 vs 仓库 README 0.3.25 [D6],复现以仓库为准。
5. arXiv HTML 三个定义均渲染为 Definition 3.0,本拆解按次序编号 3.1/3.2/3.3。

---

## 品味判断

⭐⭐⭐⭐(作为系统/工程论文;形式化部分单独看 ⭐⭐)

- 最有价值的三件资产:①拦截点选址(iter_next_step 三决策点)——所有后续工作(ProbGuard、T5)都站在这个孔道上;②四动作干预谱——分级干预的原型;③"LLM 生成规则 + 人工审"工作流及其失败模式清单——谓词工程的前车之鉴。
- 方法新颖性平(ECA 范式移植 [个人分析]),但问题定位与工程完成度使其成为该生态的地基设施(49 星、被 ProbGuard 直接依赖 [D6])。
- 与 ReGA 对照(同为"Sun 系"但分属两组):ReGA 赌"表示低维性"这一科学发现,AgentSpec 赌"拦截点+DSL"这一工程选址;前者的护城河是洞察,后者的护城河是生态位。
