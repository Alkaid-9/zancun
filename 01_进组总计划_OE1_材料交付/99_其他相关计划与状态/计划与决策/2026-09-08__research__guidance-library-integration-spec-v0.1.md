# 科研指导库融合规格 v0.1

日期：2026-09-08  
状态：PROPOSED / DESIGN-ONLY  
关联：RD-G1、TASK-20260908-002  
上游：[科研台施工蓝图 v0.1](2026-09-08__research__research-desk-construction-blueprint-v0.1.md)、[三源科研体系整合卡](../../../research_growth/方法论/科研体系三源整合_20260904.md)、[系统性科研回看稿](</mnt/d/Edge下载/学习科研规划回看与系统性科研补充-2026-09-07.md>)。

证据范围：本轮定向回读三源适配入口、迁移协议与模板、W6 手册相关章节、现有方法论、系统性科研回看稿及既有盘点；检查了源目录。没有重新逐篇审计全部 handbook、PDF、访谈或安装状态。下文的卡片与接口是本轮设计，不是现有软件功能。

本规格回答“科研指导库怎样进入科研台”。它定义来源、调用和证据边界，不把外部经验材料改写成自动评分器，也不把读取过的材料算成用户已掌握。

## 1. 指导库的职责

指导库是科研台的**方法适配层**：

- 在面对具体问题时，提供合适的提问框架、实验步骤、写作检查或迁移审计；
- 把建议绑定到来源和适用阶段；
- 按学习、协作研究和执行模式决定哪些判断需要用户先做，并记录人机分工；
- 将最终产物回链到学习记录、研究问题、菌丝卡和能力证据。

指导库不负责：

- 判定论文是否新颖或一定能发表；
- 将 AI 完成的核心定义、推理、代码或实验解释直接记成用户个人掌握；
- 把“看过材料”写成掌握；
- 直接改变 Graph 关系、任务状态、研究状态或能力等级。

## 2. 来源分层

### 2.0 pengsida 经验库是跨层来源

pengsida 的 `learning_research` 经验库不是只属于“实验与调试”的单一模块。当前本地可核入口是 [摘录总表](../../../research_growth/摘录文档/pengsida_learning_research/00总表.md)，并已被 `research_growth/方法论/02阅读.md`、`03创新.md`、`04实践...md`、`05写作.md` 和[三源科研体系整合卡](../../../research_growth/方法论/科研体系三源整合_20260904.md)二次适配。它跨越本规格的六层：

| pengsida 经验主题 | 指导库挂载 | 与科研台的关系 |
|---|---|---|
| 系统思维、目标管理、深耕领域 | F 系统性科研 | 研究议程、研究系列和方向复盘 |
| 广泛读论文、literature review、literature tree | A 导航 + F 议程 | Map、方法谱系、challenge-insight tree |
| Goal-driven Research、选题、解题、技术贡献 | D 研究判断 + F 议程 | problem、residual、prior-art 和候选贡献 |
| 最小实验、failure case、实验不 work、debug | C 实验与调试 | 执行请求、失败记录和下一轮实验 |
| 写作、review、rebuttal、slides、demo | A 导航 + B 审查 | 论文结构、表达审计和研究产物 |
| 讨论、向导师／学长蒸馏知识、科研学习方式 | E 经验观察 + Collaboration Board | 协作请求、讨论记录和反馈来源 |
| Research Project 流程 | F 议程 + Workbench bridge | task→challenge→solution→验证→改进→写作的项目链 |

当前状态是“本地材料已存在、已有部分适配、尚未逐项接入科研台”：摘录总表列出了完整和部分摘录，也有待读／待摘录项；目录说明和当前磁盘路径还存在 `Notion文档/` 与 `摘录文档/` 的命名差异。G1-a 必须核对真实文件覆盖、原始链接、二次适配和重复关系，不能因为三源整合卡已经存在就宣布整库融合完成。

### A 导航层：问题与论文结构

主要来源：Luo《博士生科研入门辅导》及同类入门材料。

适配操作：

- 新问题／老问题识别；
- What、Why、How、So What；
- 方向→问题→方法→实验→写作的链条；
- 广读到深读的顺序；
- 摘要、引言、Overview、Related Work 的结构检查。

科研台落点：`problem_card`、`paper_note`、`outline`。

### B 提问与审查层：导师经验

主要来源：`external/Supervisor-Skills` 的 Preliminary、Idea Generation、Paper Writing、Scientific Plotting 和 Case Studies。

适配操作：

- 隐含假设、符号、图和案例检查；
- 问题类型与能力匹配；
- 贡献、实验和表达的审阅清单；
- 图能否让读者复原主线。

科研台落点：`review_checklist`、`assumption_card`、`figure_audit`、`proposal`。

### C 实验与调试层：实践方法

主要来源：pengsida 经验库的实践／Research Project 部分、`research_growth/方法论/04实践...`、`EXPERIMENT_DESIGN.md`、`DEBUG_METHODOLOGY.md`、代码学习和复现记录。

适配操作：

- prediction；
- toy／最小实现；
- 一次只改一个因素；
- good case／failure case；
- 候选原因排序和逐项排除；
- 修复后复跑原失败样例。

科研台落点：`experiment_plan`、`run_request`、`failure_record`、`debug_note`。

### D 迁移与研究判断层

主要来源：迁移审计协议、问题解决、品味培养、科研流程完整性审计和已有 OS。

适配操作：

- 源机制证据；
- 目标域前提；
- representation；
- decision delta；
- 竞争解释；
- 最小证伪；
- claim ceiling、ownership 和冷启动。

科研台落点：`transfer_card`、`research_question`、`claim_boundary`、`ownership_check`。

### E 参考与观察层：经验材料

主要来源：CCF 优博成长访谈、高手经验、团队／导师公开分享、拒稿和领域工程实践。

适配方式：

- 作为心态、方法感和工作习惯的类比材料；
- 记录“来源主张”和“我是否适用”的分离；
- 不直接变成规则、能力结论或研究证据。

科研台落点：`observation`、`analogy_card`、`discussion_branch`。

### F 系统性科研层：议程与成果继承

来源入口：杨学《如何做好系统性科研》的用户截图整理、回看稿 §4 和 §5；现有盘点 04 §9；W6-D 的信息源／风向／taste；既有 Map 的雷达、综述与提案资产。此层保留长期研究系列，不能被 E 层“心态参考”覆盖。

操作：从领域与开放问题形成候选议程；用小专题／综述厘清分支与竞争解释；每项工作记录留下的定义、工具、反例、数据、评价协议；将后续问题连接到实际结果或反馈。方向可以修订，也允许不服务当前议程的 F/E 探索。

科研台落点：`research_agenda`、`research_series`、`reuse_record`、`feedback_record`，均为待实现对象。议程→问题系列→工作→资产→后续问题是一条可检查链，不能用一条“相关”线代替。

杨学来源上限：回看稿记载依据去重后的九页截图，知乎正文未取得、视频未完整转录；本轮沿用这个边界，不声称已经读过完整访谈。讲座经验可以启发设计，不证明某种研究策略必然成功。

六层是方法目录，可交叉选用；它们既不是六级能力，也不替代 WORLD/FIELD 五层、Map 八层或七图视角。

### 2.1 已有资产如何接入

| 现有资产 | 保留与适配 | 仍待逐项核对 |
|---|---|---|
| [research_growth 入口](../../../research_growth/README.md)、[pengsida 摘录总表](../../../research_growth/摘录文档/pengsida_learning_research/00总表.md)、三源整合卡 | pengsida 作为跨六层经验源；已有二次方法笔记继续被引用 | 摘录覆盖、原始链接、目录命名差异、模板重复和实际可调用性 |
| [Supervisor-Skills](../../../external/Supervisor-Skills/README.md) | handbook 是来源，skills 是执行配方；两类分开登记 | 每项适用条件、版本、许可；不整仓自动启用 |
| [W6 CRAFT_MANUAL](../../research/map/W6_craft/CRAFT_MANUAL.md) 及 A–D | 保留领域正确性、反例重放、实验、统计评价和信息源训练 | 旧进组日程、人数／次数阈值和“必做”表述不直接移为全局规则 |
| [现有科研方法论](../../learning/methodology/RESEARCH_METHODOLOGY.md) | 保留拆解→审计→批判→产出的操作谱系 | 固定阅读时长、每篇全做、自动转研究方向的旧口径需适配 |
| [迁移审计协议](../../../research_growth/方法论/迁移审计协议_20260905.md) 与 [模板](../../../research_growth/方法论/TRANSFER_CARD_TEMPLATE.md) | 深层研究迁移审计沿用原模板，不新设重复模板 | SENSE 轻记录与研究候选升级的边界 |
| [SKILL_INDEX](../../../research_growth/方法论/SKILL_INDEX.md) | 作为待核验目录，不据文件名宣称已安装或自动触发 | 路径、触发、退役规则和平台兼容性；旧自动退役不默认继承 |
| CCF、高手经验、系统性科研回看 | 同时支持反思与议程设计，引用原件覆盖状态 | 不同 PDF／Word／截图的覆盖对账；已有 BR-15 承接原材料核验 |

## 3. 统一条目格式

每条指导条目登记为普通 Markdown 或 YAML，不要求复制原 PDF：

```yaml
id: guide:experiment:prediction-first
kind: guidance_item
layer: experiment
title: 先写预测再运行最小实验
source_refs:
  - file:research_growth/方法论/skills/EXPERIMENT_DESIGN.md
stage_refs: [learning, exploration, research]
trigger:
  object_kinds: [experiment_plan, research_question]
  tags: [prediction, toy, failure]
user_first:  # 仅此学习模式配方的要求，不是全部执行任务的前置
  required: true
  fields: [prediction, reason, expected_observation]
ai_actions: [find_missing_baseline, propose_counterexample, format_log]
forbidden_actions: [declare_success, upgrade_capability, assert_novelty]
outputs: [experiment_plan, failure_record]
acceptance:
  - user_can_explain_prediction
  - original_failure_case_replayed
provenance_status: adapted
revision: 1
```

必填字段：

- 身份：`id`、`kind`、`title`、`revision`；
- 来源：`source_refs`、页码／章节／行号、版权状态；
- 使用条件：适用阶段、对象类型、触发标签；
- 所有权：用户先写字段、AI 可做动作、禁止动作；
- 产物：会生成或更新哪些记录；
- 验收：怎样证明指导真的被使用；
- 来源阅读状态：未读／部分／已读及范围；适配状态：草稿／试用／采用／退役；使用证据：独立调用记录。这些状态分列，“tested”只表示指定场景使用过。

身份与位置分离：示意 `file:` 字符串是待登记定位符，不作为最终稳定 ID。正式 `source_refs` 引用来源 ID，来源登记另存 repo/root、相对路径、章节及版本。原件移动只更新位置。指导条目稳定 ID 不能由标题或目录变化决定。

快速记录只需：当前问题、来源、这次采用的提示、实际动作和下一步。完整模板按需展开；不会要求每次聊天填满全部字段。

## 4. 调用路由

科研台根据当前对象和用户意图提供候选指导，不自动堆叠全部方法：

```
用户意图／当前卡片
  → 阶段识别（学习／探索／研究／写作／复盘）
  → 对象和缺口识别
  → 返回最多 3 个 guidance proposals
  → 用户选择
  → 用户先写关键字段
  → AI 辅助与来源定位
  → 产物写回 + 验收记录
```

推荐触发：

| 当前情况 | 首选指导 |
|---|---|
| 刚接触一篇论文 | A 导航层 + 论文阅读模板 |
| 不清楚问题是什么 | A 问题卡 + B 四问检查 |
| 想做跨领域类比 | D 迁移审计 + E 类比卡 |
| 实验不 work | C prediction／toy／debug |
| 想整理研究候选 | D residual／prior-art／最小证伪 |
| 准备写摘要或引言 | A 结构 + B 写作清单 |
| 需要判断是否挂起 | D claim ceiling + E 观察记录 |

一次一个主指导、一个辅助检查、最多三项推荐是首轮交互提案，后续按真实使用调整，不成为用户必须遵守的数量门。

## 5. 用户、AI、Agent 的权限

按模式处理，模式选择和切换显式可见：

| 模式 | 人与 AI 的工作安排 | 结果怎样记录 |
|---|---|---|
| 学习／掌握验证 | 对本次练习选定的定义、预测或关键步骤，先让用户尝试；可主动请求讲解或提示 | 提示程度和个人表现分开记录，讲解后完成不冒充独立完成 |
| 协作研究／开放探索 | AI 可以提假设、写推理、写代码、提出反例；用户组织目标与裁决 | 记录贡献角色、待核主张和人机系统产物，不要求用户重做全部工作 |
| 执行／资料整理 | 在明确任务与写域内，CLI／Agent 可以直接整理、索引、运行已授权工作 | 回执进入执行证据；人工审核和掌握状态另存 |

既有冻结教学站点继续遵守其本地规则；本规格不重写题面、答案或门禁，也不把站点规则推广到整个科研台。

用户负责的确认包括：

- 学习模式中选定的先尝试字段，以及是否请求提示；
- 对关键关系的接受／拒绝；
- 是否接受关于实验结果和失败解释的正式主张；未核实的产物仍可保留；
- 能力证据和研究状态的收口。

AI 可以：

- 检索指定来源；
- 生成提问、反例候选和格式化草稿；
- 对照原文定位缺项；
- 将讨论拆成候选卡片和待办提案；
- 生成索引和别名。

AI／Agent 不得无确认地：

- 把关系写入正式 Graph；
- 改变任务线主归属；
- 自行推断后创建、关闭或延期正式 TODO；用户已经明确要求“挂待办”时可直接登记，无需再提同一项确认；
- 升级能力等级、研究状态或新颖性结论；
- 用经验材料覆盖原文、代码或实验事实。

所有提案均保存 `proposal_id`、来源、解释、置信度排序值、用户决定和回滚关系。

## 6. 与 Map、菌丝和能力层的映射

指导条目本身不是地图节点的终点，而是可复用的“方法节点”：

- A/B 条目通常连接到 Method Landscape 和 Knowledge；
- C 条目连接到 Evidence、Competency 和 Trajectory；
- D 条目连接到 Idea Genealogy、Transfer 和 Research agenda；
- E 条目连接到 Identity & Fit、Trajectory 和开放观察。

一张 Mycelium Card 至少可记录：

`problem`、`source_refs`、`mechanism`、`representation`、`example`、`counterexample`、`downstream`、`failure`、`my_action`、`next_question`。

上述为可选扩展字段，不是最小必填表。同一张卡可被多个视图引用；不要为七个视角复制七份正文。

关系也要分清：`analogy_candidate` 表示启发性相似；`alternative_to` 表示替代；`complements` 表示共同目标下的互补及拼接前提；`reused_in` 需有实际使用回执；`motivates_question` 需指出哪个结果改变了后续问题。新增关系名是 v0.4 的扩展提案。用户可以保留很模糊的类比，只有提升为迁移有效或工作继承主张时才展开完整审计。

例如，“EdgeIM 与控制论都使用结构表示”可先保留 SENSE；不能据此宣布同一机制。若后续项目实际使用了一份失败样例生成器，才登记 `reused_in`，记录资产版本、目标工作、用途与限制；若该失败引出新问题，再登记 `motivates_question`。共用主题、共同目标、实际复用分别显示。

指导调用后，能力记录至少区分：

- `personal`：用户能否解释、变体、诊断和迁移；
- `orchestration`：用户能否拆分、调度、设停止条件和互审；
- `system`：在人机配置下实际完成的产物。

## 7. 版权与来源边界

- 原 PDF、外部仓库和访谈原件继续保留在各自资料位置；
- 指导库登记摘要、章节定位和适配规则，不复制不必要的大文件；
- Supervisor-Skills 的 CC BY-NC-SA 4.0 约束随改编摘要保留；
- 经验访谈的原话、截图和转录按来源状态保存，不把二手摘要冒充原始证据；
- 跨账号默认准备用户自行携带的文件包，不自动上传。公开分享时另按具体内容判断许可和脱敏范围。

## 8. 首批实现与验收

候选池可覆盖以下类别，首轮只完整试用三条（论文定位、轻类比转迁移审计、资产继承），其余逐项扣细节，不按数量判定整合完成：

- 论文 What/Why/How/So What；
- problem_card；
- prediction-first；
- toy／最小实验；
- failure analysis；
- transfer audit；
- claim ceiling；
- 论文摘要／引言检查；
- 图和符号检查；
- 冷启动复述。

验收场景（尚未执行）：

1. 打开一条 EdgeIM 学习记录，科研台只推荐相关的 1–3 条指导；
2. 学习模式先让用户尝试或显式请求讲解；协作研究模式允许 AI 先出草稿，两种来源标记不同；
3. 关闭指导库后，学习记录和来源关系仍能独立读取；
4. 拒绝一条关系或待办提案，正式 Graph 不发生变化；
5. 记录一次失败实验后，能力状态不自动升级；
6. 从指导卡可追溯到原文件、章节和版本；
7. 删除派生索引后重建，指导条目和调用记录不丢失。
8. 用同一资产的两个版本模拟复用，正确回到实际版本；没有复用回执的“看起来相关”保持类比状态。
9. 拒绝旧方法库的一条固定时长规则，不影响来源可读性和当前学习入口。

### 8.1 产品入口与归档

科研台设“指导库”独立入口，按问题／阶段／来源筛选；学习记录、研究卡和画布侧栏显示“相关指导”。用户可查看来源、选用或隐藏推荐、打开原模板、记录本次效果、提出修改。未填写的核心字段显示未填，不由后台悄悄补齐。

建议在内容库下设 `guidance/items/`、`guidance/recipes/`、`guidance/uses/`：条目存适配，配方说明调用次序，使用记录回链现有学习／研究记录。来源正文仍在原处，展示不要求独立数据库。三者是目录提案；首轮允许全部使用普通 Markdown。

一条使用记录保存对象 ID、指导 ID/版本、模式、贡献角色、证据引用和下一步。误关联可撤回引用，保留已发生的使用事实；方法升级不会静默改写历史使用版本。外部画布只放这些对象的引用。

## 9. 后续开放门

- 是否将 Luo PDF、Supervisor-Skills 和经验访谈的适配摘要放进独立 `research-knowledge` 仓；
- 首轮三条指导卡的实际使用反馈与后续候选优先级；
- 指导条目是否允许用户自定义、版本化和退役；
- 是否需要把指导调用接到外部画布的 Agent 提案面；
- 是否将某些检查清单做成 CLI 命令，或仅保持 Markdown／JSON。

后续按五项小任务推进：G1-a 来源／版本／覆盖对账（首项显式核对 pengsida 原库、本地摘录、二次方法笔记和待摘录项）；G1-b 学习与协作模式适配；G1-c 三条指导配方样例；G1-d 侧栏及画布回链；G1-e 实际使用验收。原材料补全引用 BR-15，不重复建立同一 OCR／访谈核验任务。

当前完成为来源映射和调用规格草案。逐项适配、用户试用、应用接入仍未完成；普通文件样例可先做，工具安装与自动执行链按对应实施范围推进。
 
