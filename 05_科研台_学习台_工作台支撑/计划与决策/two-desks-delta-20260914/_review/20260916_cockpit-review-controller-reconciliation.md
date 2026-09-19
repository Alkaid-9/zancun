# 科研项目驾驶舱独立评论：主控证据对账

日期：2026-09-16。任务：`TASK-20260916-008`。会话：`01a0aa0a-203a-7290-b7c8-be62c8f1f896`。

状态：`CONTROLLER-RECONCILED / DOC-PATCH-ONLY / IMPLEMENTATION-NOT-AUTHORIZED`。

本件对[独立评论](20260916_fable5-independent-review.md)第三轮A-E逐项回到一手合同、代码和生成链核验。它不改写原评论的两次自我更正，也不把同一操作者调度下的fresh-context只读核验冒名为组织外部审计、异构审或用户接受。

## 1. 任务身份与治理更正

1. 原计划、任务日志和路由使用`TASK-20260916-004`，但共享INDEX已明确把当日003／004判为发号器发出未消费的作废跳号；该身份无效。
2. 8899发号器本轮不可达。按INDEX兜底协议通读当日登记号后取最大值+1，并用`ledger_edit.py`＋CAS登记`TASK-20260916-008`；当前会话绑定008。
3. 原评论第26行称整个目录被`.gitignore`首行`/*`排除，不符合当前磁盘。`git check-ignore -v --no-index`对方案、评论、任务日志均无命中；这些文件是未跟踪，不是被忽略。
4. `project: research-desk`当前不在项目卡注册表，生成视图的`UNKNOWN_LOG_PROJECT`是真实诊断。slug一经注册终身不改，本任务不擅自立卡。

## 2. A-E裁定

| 项 | 裁定 | 一手证据与修订 |
|---|---|---|
| A Skill计数依赖 | `ACCEPT-WITH-CORRECTION` | P1确实不能在只有G0时承诺“有效运行数”。但WP-S S1只生成技能manifest；S3只是从task log EVENTS聚合`skill_id`的弱信号，也不能证明有效运行。方案已拆分技能目录、EVENTS引用次数和有效运行回执；无回执源时显示`N-A`，不显示0。 |
| B research_judgment合同 | `PREMISE-REJECTED / DEPENDENCY-GAP-ACCEPTED` | `B_CONTRACT_PROPOSAL.md`仍是未冻结历史提案，但实际`research-desk/acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md`已标`AUTHORIZED / CONTROLLER-TECH-PASS / OPEN-GATES`，代码也校验同一五态枚举和版本引用。真实缺口是驾驶舱未显式钉实际合同，且该合同／回执尚未跟踪。G0现要求记录哈希、应用commit、代码／测试一致性，合同重开时重审§3.3／§4。 |
| C P5存储落点 | `ACCEPT-WITH-CONTRACT-GATE` | 通用Object／Revision和B三类记录是已实现先例，文件仍应持有正文；但单一`manuscript_artifact`不是已批准答案，现有七类Relation也不足以表达全部产物链。方案已规定默认复用Object／Revision，不新建store；具体kind、locator、采用状态和关系语义留给P5 CONTRACT_DELTA。 |
| D 静态优先 | `ACCEPT-WITH-COST-CORRECTION` | `research_desk.py::render_current`证明Markdown渲染模式可复用，但它只读统一JSON；驾驶舱还要适配SQLite、Markdown账本、项目卡和缺失的Skill manifest，并处理跨仓新鲜度。结论收窄为“渲染壳成本低，可信聚合不是近零成本”。方案改为P1a静态验证件；实测减负后才考虑P1b交互页。 |
| E 独立评审语义 | `ACCEPT-WITH-EXPANSION` | fresh-context只读子代理只是普通scoped review的一种，不是独立评审的唯一定义，也不能关闭要求异构审或外部人审的包。方案新增review class、固定受审版本、reviewer来源／同谱系关系、方法、receipt和未查面；UI不得显示无范围裸PASS。 |

## 3. 关键一手锚点

- 实际B合同：`/mnt/d/MyResearch/research-desk/acceptance/b-TASK-20260915-004/CONTRACT_DELTA.md:3-20`。
- B运行时校验：`/mnt/d/MyResearch/research-desk/app/research_service.py:157-209`；通用Object／Revision：`record_store.py:102-151,218-237`。
- 当前Relation词表：`/mnt/d/MyResearch/research-desk/app/research_service.py:30-33`。
- WP-S manifest与弱遥测：`progress/decisions/2026-09-01__maintenance__workbench-v2-skill-registry-design.md:23-52,68-75`。
- CURRENT生成器：`/mnt/d/MyResearch/research-desk/app/research_desk.py:824-905`；它写静态Markdown，但不读取驾驶舱所需全部正本。
- project slug不可改：`progress/projects/README.md:35-39`。

## 4. 本次没有关闭的门

- 未执行G0、P1a／P1b或P2-P7；未运行应用测试、服务、模型或真实数据库。
- 未补R11原始链接、作者、版本或许可。
- 未注册`research-desk`项目卡；未选择P5具体kind／关系方案。
- 未关闭A/B独立复核、用户试用、WP0异构审／接受／采收／加载或历史证据采收。
- 本次主控对账只支持“设计缺口已被准确写回”，不支持“产品已完成”。

## 5. 后续顺序

1. 用户决定R11口径和项目slug是否立卡。
2. 另领任务执行G0，钉实际B合同、跨仓快照／新鲜度与需求矩阵。
3. 先走现有隔离DEMO最短真实路径。
4. 另行授权后做P1a静态验证件；真实阅读观察支持减负后再讨论P1b。

