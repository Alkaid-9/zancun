# 科研方法论基建与科研台、学习台接入审计

日期：2026-09-16  
任务：`TASK-20260916-007`  
状态：`AUDIT-COMPLETE / MAIN-CONTROLLER-VERIFIED / 3-INDEPENDENT-READ-ONLY-REVIEWS-COMPLETE`  
范围：知识图谱、菌丝网、科研地图、团队脉络、领域全景、横纵展开、跨领域方法、成果追踪、开源／论文／OpenReview、经验与失败、纠错、工业界追踪，以及它们与当前科研台、学习台、工作台的实际接入。

> 本文不是“仓库里有没有文件”的清点，而是检查这些能力能否从当前工作台进入、写回各自正本、保留版本与证据，并形成可重复的使用或更新闭环。静态资产存在、页面有入口、设计文档完成、技术测试通过、用户真实使用和持续机制运行是不同状态。

## 1. 本次结论

结论不是“全做了”，也不是“什么都没做”。准确状态是：

1. **内容底盘较厚**：科研地图已有结构化的流派、团队、论文、课题和部分关系数据；鲁侧、孙侧、全域、拒稿情报、开源工具和 craft 方法材料均有实体。
2. **科研台／学习台只接入了一个有限切片**：来源选择与保存、目标要求、Attempt/Feedback、独立研究判断、受限 return_context，以及到工作台的人工引用路径已经实现；这不等于完整知识网络或持续调研系统。
3. **用户点名的大多数“网络化、持续化、自动回流”能力仍是设计或待施工**：完整关系操作、七图投影、菌丝／共同画布、C04 搜索与学术工业比较、C05 指导使用链、C06 学习证据闭环、C07 失败／转向／成果继承、工作台自动桥都没有整体交付。
4. **持续跟踪明显陈旧**：调研台账停在 2026-08-16，九月补缺波仍标 `PREPARED-NOT-LAUNCHED`；工业最小集、被引反查、OpenReview 尽力面和 watchlist 复扫均未发射。

因此，当前应称：`SUBSTANTIAL-CONTENT / PARTIAL-DESK-INTEGRATION / CONTINUOUS-LOOPS-OPEN`。

## 2. 判定口径

| 状态 | 本文含义 | 不能冒充 |
|---|---|---|
| 内容资产 | 文件、表格、数据或手册实体在盘，可定位和阅读 | 已进入科研台／学习台日常路径 |
| 已接入 | 当前产品能从对象身份进入、保存／引用、返回正本，并有实际合同或测试证据 | 用户已接受、完整网络已实现 |
| 仅设计／部分容器 | 需求、schema、交互或施工包已写，或只有局部字段 | 产品能力已交付 |
| 陈旧／未运行 | 曾有快照、计划或一次性扫描，但当前更新波未执行 | 持续追踪机制正在工作 |

三台职责本来就被明确分开：科研台负责问题、假设、方法比较和研究判断；学习台负责目标、动作、帮助条件、反馈、重做／复测和本人能力证据；工作台负责任务、依赖、执行、验收和恢复（`progress/runbooks/lu-onboarding-and-desks-architecture.md:7-11`）。所以本审计不会因为某份地图能被人读到，就判它已经接入学习证据或任务执行。

## 3. 用户点名能力逐项审计

| 能力 | 内容资产 | 当前与三台的真实接入 | 持续机制 | 判定 |
|---|---|---|---|---|
| 知识图谱／多层知识网络 | 已有 Object/View/Revision、旧地图及局部关系；地图解析器可提取实体和部分边 | B 已支持目标、尝试反馈、研究判断和受限返回；完整语义关系与跨层影响未建齐 | 无自动跨层更新；不自动翻转研究结论或掌握状态 | **部分接入，不是完整知识图谱** |
| 菌丝网／共同画布 | Canvas v0.4 有任务枝、菌丝、共同画布与权限合同 | 只列为 C02 与 `X-CANVAS/X-DISPATCH` 后续入口 | 外部画布试验和拖拽未完成 | **设计存在，产品未实现** |
| 科研地图 | W1-W4、W6-W7 和 W5 v0 有大量实体；本轮 solver 检查通过 | C03 有导航与局部投影，但动态筛选、完整关系操作和 Map 最小闭环未完成 | 月度雷达和补缺波没有在九月运行 | **静态／结构化底盘强，工作台闭环弱** |
| 团队脉络 | 解析结果含 33 个团队；L1 地图有团队卡 | 旧静态浏览器可按流派／团队／论文联动，新科研台没有完成团队关系工作面 | 结构化快照生成于 08-14，边主要是词元匹配／包含派生；不是持续动态图 | **有内容，未形成持续团队雷达** |
| 领域全景、纵向谱系、横向比较 | L0/L1/L2、问题×方法矩阵、鲁／孙侧和拒稿元分析均有实体 | 七图只完成最小局部投影或设计，学术／工业完整比较归 C04 | 关键比较表仍有 v0 不解析区域，未见本月回流 | **内容存在，产品化与保鲜未闭** |
| 相似方法论跨领域寻找 | 交叉带、bridge、Transfer Card、融合地图和 craft 材料可供人工使用 | 当前可记录文字判断，但正式 relation 类型、配方采用、效果和迁移证据分别待 C02/C05/C06 | 没有自动发现或定期跨域扫描 | **人工素材有，方法使用链未接通** |
| 重要成果后续追踪 | 有 SURVEY_LEDGER、radar 和一次性快查 | 当前科研台来源登记能保存来源，但不等于监控作者／成果更新 | 九月 RS-A/RS-B 未发射，预定输出目录与常规产物不存在；台账仍停 08-16 | **有台账，无正在运行的追踪闭环** |
| 开源项目、论文、OpenReview | OSS landscape、170 篇解析论文、19 个 review case、W4/FD 资产存在 | A 能从来源全集检索和保存，但不保证原件全文抽取；驾驶舱只在设计中 | GitHub／论文／OpenReview 的九月重扫未执行 | **一次性资产丰富，持续发现未运行** |
| 经验吸取、为什么失败 | W6 craft、拒稿情报、Attempt/Feedback 和真实 incident 均有 | 学习台已有字段和版本容器；C07 的失败／分歧／转向／成果继承仍未交付 | 真实使用和后续复测仍开放 | **能记录局部案例，尚非系统闭环** |
| 错题集／纠错本 | 有纠错本设计；EdgeIM MISTAKE_LOG 只有 1 条且仍为 `OPEN` | B 有 Attempt/Feedback 和帮助条件，但学习台最小闭环明定要到 C06 加用户使用 | 主 LEDGER 只有两条降级代做记录；不能称持续运作 | **设计有、孤立记录有，个人闭环未验收** |
| 工业界追踪 | OSS／工具扫描及 TraceBridge 的一次 bounded census 在盘 | 学术／工业独立联动目前只有导航和设计入口，完整比较归 C04 | IND-1 从未发射，IND-2 仍是条件项 | **一次性资产有，当前工业雷达未运行** |
| 与工作台的任务化衔接 | N3 已有身份、观察版本、来源、继续点和人工任务路径 | 仅 `MANUAL-ONLY`；没有 Task HTTP 写端点、幂等派发或自动回执 | WP0 原门与自动桥均开放 | **人工引用已接，自动闭环未接** |

### 3.1 知识网络与菌丝网的证据上限

- 架构正本明确写着：专业知识“有旧地图及局部关系；正式内容未建齐”，研究认识“完整语义网未完”，科研方法指导的 C05 使用链待做，个人实践的真实学习验收开放，执行协调的跨台调度桥待接（`progress/runbooks/lu-onboarding-and-desks-architecture.md:13-23`）。
- RD-2 追踪表把“团队／同期／方法／跨域／互补”判为正式关系尚无产品闭环，把“局部树和横向网”判为只有草稿线字段，把模糊类比与迁移判为缺类型与使用检查（`progress/decisions/rd2-construction-v0.3/TRACEABILITY.md:21-30`）。
- 同一追踪表说明 Canvas v0.4 只是合同继承；外部画布试验和拖拽没有完成（`progress/decisions/rd2-construction-v0.3/TRACEABILITY.md:47-58`）。

### 3.2 科研地图实体的本轮复验

在项目规定的 solver 环境中执行：

```text
env CONDA_DEFAULT_ENV=solver CONDA_PREFIX=/home/alkaid/miniconda3/envs/solver ... \
  /home/alkaid/miniconda3/envs/solver/bin/python tools/scripts/map_to_yaml.py --check
```

结果为退出码 0：41 张规范表中解析 25、跳过 16，另解析 4 个块；40 个流派、33 个团队、170 篇论文、19 个 review case、5 个课题；关系边为 school_team 41、paper_container 149、topic_school 18。另有 `[需验证]` 标记：流派 12、团队 11、论文 8。16 张跳过表包括多张问题×方法／红蓝海矩阵和综合表，因此这些数字证明“结构化底盘存在”，不证明所有横纵关系已进入图模型。

现有 `data/_meta.yaml` 是 2026-08-14 05:35 生成的静态快照，记录同一组实体统计（`research/map/data/_meta.yaml:1-71`）。其关系模型明确说明团队边来自词元匹配、论文边来自结构内含，可能漏边／错边；问题×方法矩阵和综合表在 v0 不解析（`research/map/data/SCHEMA.md:68-76`、`:96-102`）。所以“当前解析器仍能通过检查”和“产品里已有经人工确认的完整谱系”不能画等号。

地图总纲本身也把八层需求写成分区、脉络、团队、OpenReview 对比、困难、动向、taste 和工程实践（`research/map/README.md:11-22`），并记录 W1-W4、W6-W7 的资产与 W5 v0（`research/map/README.md:30-40`）。这回答了“有没有做内容”，但不回答“当前台上是否能连续使用”。

### 3.3 跟踪、OpenReview 与工业界为什么判为未运行

- 调研台账的最后建档日是 2026-08-16；G1 工业最小集、G2 工业全景、G3 被引反查、G4 OpenReview 尽力面、G5-G6 全文与 watchlist 复扫均仍是待执行或条件项（`research/map/surveys/SURVEY_LEDGER.md:54-65`）。
- 九月计划 frontmatter 仍是 `PREPARED-NOT-LAUNCHED`，发射记录表五行全部为空（`research/map/surveys/PLAN_survey_gapfill_202609.md:1-7`、`:63-70`）。
- 计划本身已经写好了 IND-1 的产品能力矩阵、RS-A 的 watchlist／arXiv／接收列表复扫、RS-B 的 Semantic Scholar 被引反查与 OpenReview 尽力面，以及 IND-2 的条件触发（`research/map/surveys/PLAN_survey_gapfill_202609.md:19-55`）。缺的是执行与回流，不是又写一份计划。
- 本地最后一条明确的 radar 快查是 2026-08-14（`research/map/CHANGELOG.md:67-73`）。现有脚本只固定监测鲁法明、孙猛两位作者和五组关键词，另有三项仍需人工（`research/map/radar/tools/monthly_check.py:39-56`、`research/map/radar/tools/README.md:61-69`）。
- OpenReview forum 全文、5 个隐藏 ID、Semantic Scholar 复扫、GitHub code search、2026 接收列表和被引反查仍列在未搜面（`research/map/SEARCH_BOUNDARY.md:35-48`）。

### 3.4 学习、失败与纠错为什么不能判成已闭环

- 架构表只证明 B 有版本和帮助条件容器，同时明确“真实学习验收开放”（`progress/runbooks/lu-onboarding-and-desks-architecture.md:17-21`）。
- RD-2 的完成口径规定：学习台最小闭环必须完成 C06 并通过对应用户使用；C03 侧栏切换不算（`progress/decisions/rd2-construction-v0.3/TRACEABILITY.md:60-66`）。
- 驾驶舱设计同样禁止把 Skill 完成、技术 PASS、论文产物、研究判断和用户接受合为一个 PASS（`progress/decisions/two-desks-delta-20260914/RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md:11-24`）。

因此，错题文件、失败案例或 Attempt 字段可以判为“资产／容器已有”；在没有本人真实尝试、反馈、重做和复测证据时，不能判“学习纠错机制正在有效运作”。

独立核验进一步确认：EdgeIM `MISTAKE_LOG.md` 只有 2026-09-03 的一条记录，状态仍为 `OPEN`，关闭条件要求 EX-00 PASS 后 D+2、D+7 复测（`learning/training/lu-edgeim-algo1/MISTAKE_LOG.md:3-18`）；总 `LEDGER.md` 只有两条明确标为“降级→逆向训练”的 AI 先行记录（`learning/training/LEDGER.md:3-10`）。纠错本方案自己标注为讨论整合稿、C06 未施工，并把两条真实案例走查列为下一步（`progress/decisions/2026-09-12__learning__correction-notebooks-and-growth-v0.1.md:1-13`、`:156-164`）。

### 3.5 工业资产不是零，但不等于持续追踪

TraceBridge 在 8 月底确实形成过一次有边界的工业普查：29 个技术 canonical works、1 个 radar work、39 个 source manifestations，并明确标为 English/public-static、`BOUNDARY-INCOMPLETE`（`research/tracebridge_full_spectrum_20260830/02_census/wave1_industry_reports_blogs/REPORT.md:1-16`、`:89-101`）。因此不能说工业界“没做过”；准确说法是：有一次性且边界明确的研究资产，未接成九月持续雷达或 C04 学术／工业比较闭环。

### 3.6 三路独立只读复核

存档后按用户要求重试此前 429 的三路任务，三路本次均返回 `complete`：

1. `audit_network_maps`：确认地图实体与静态浏览能力真实存在，但完整关系、菌丝画布、动态产品闭环和用户验收均不能推出。
2. `audit_research_tracking`：确认九月 IND-1/RS-A/RS-B/SUMMARY 的发射表为空，预定输出不存在；OSS/OpenReview/论文资产主要是 8 月快照。
3. `audit_learning_industry`：确认“错题机制持续运作中”不成立；同时纠正“工业只有早期 OSS 扫描”的窄说法，补入 8 月底 bounded census。

主控已沿上述关键出处重新读取并核对。三路均未联网、未检查密封答案、未启动服务或扫描，也未代签用户验收；这些仍是本审计的未覆盖面。

## 4. 当前真正接上的最短路径

当前已有、可以如实声称的链路是：

```text
已登记来源
  -> A：从来源全集检索／选择并获得保存反馈
  -> B：记录目标要求、Attempt/Feedback、帮助条件、独立研究判断
  -> 受限 return_context 回到阅读位置
  -> N3：生成带身份／版本／来源／继续点的人工工作台引用
```

A/B/N3 的已提交事实和历史测试见当前交接（`progress/handoff/2026-09-15__desks-window-current__handoff.md:32-44`）。N3 不派发任务、不写研究或学习状态，也没有自动桥（`progress/runbooks/lu-onboarding-and-desks-architecture.md:50-57`）。

## 5. 还没有接上的目标闭环

```text
持续发现（论文／OpenReview／GitHub／工业）
  -> 来源版本与精确证据
  -> 概念／团队／方法／竞争与继承关系
  -> 研究问题、替代解释和决策
  -> 学习缺口、尝试、反馈、重做与复测
  -> 工作台授权任务、run、产物与验收
  -> 结果回写地图、watchlist、失败经验和下一次扫描
```

这条链目前跨越 C04-C07、EXR、WP0 自动桥和真实用户使用，多处仍开放。驾驶舱方案把 C04 搜索／学术工业比较、C05 指导使用、C06 学习证据、C07 失败与成果继承分开施工，并明确不得一次打包宣称完成（`progress/decisions/two-desks-delta-20260914/RESEARCH_COPILOT_PROJECT_COCKPIT_PLAN.md:128-157`）。

## 6. 与既有 TASK-006 盘点的关系

`TASK-20260916-006` 主要回答“材料有没有、可提什么方案”。本审计增加的是“是否进入当前科研台／学习台并形成闭环”这一条轴。两者不互相删除：已有材料仍然是资产，但诸如“地图已建成”“错题集已建成”不能直接升级成“桌面已集成、持续机制正在运行”。

## 7. 开放项与停止边界

本任务只做审计与存档，不授权：

- 实施 C04-C07、EXR、Canvas、自动派发或新数据库；
- 发射九月扫描、联网检索、联系导师或设置外部订阅；
- 代填学习尝试、错题、反馈、复测或能力证据；
- 修改 TODO/PENDING、生成视图、应用源码、真实数据库或服务状态；
- commit、push、deploy 或代替用户验收。

三路只读独立核验已在存档后重试并完成：网络／地图，研究跟踪／OpenReview／OSS，学习／失败／工业。结果已用于修订本文证据与结论，但不自动开启任何施工。外网时效、真实 research-desk 交互、服务运行态、用户学习与使用接受仍未验收。
