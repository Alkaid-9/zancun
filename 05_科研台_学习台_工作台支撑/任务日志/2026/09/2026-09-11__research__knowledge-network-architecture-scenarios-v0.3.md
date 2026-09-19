# TASK-20260911-005：知识网络架构三场景走查（独立版）

**日期**：2026-09-11
**关联**：RD-2、[v0.1](../../decisions/2026-09-11__research__knowledge-network-architecture-v0.1.md)、[v0.2](../../decisions/2026-09-11__research__knowledge-network-architecture-v0.2.md)、[v0.3场景稿](../../decisions/2026-09-11__research__knowledge-network-architecture-v0.3-scenarios.md)

## 背景

用户把v0.2方案转给另一位assistant身份（Astra，按IMPLEMENTATION.md既有角色分工=规划/取舍/最终审阅）审阅，Astra提出多处具体反驳（工业缺口定性过头、maturity字段假设有问题、growth_mode不该焊死在Relation上、指导库整合需要usage record等）。用户拍板"两边各自独立画三张场景图，你来对比"，本任务是执行"我方独立画"这一半，不参照对方产出。

## 做了什么

1. 先认领三处v0.2的自我修正，不带着旧问题去画新图：
   - 核实`rd2-construction-v0.3/TRACEABILITY.md` R02行原文"学术／工业独立联动"已排C03/C04工位——工业缺口改判"需求已有、未具体化"，撤回此前"三重独立确认的真空"这个过头表述。
   - `maturity`字段本稿不采用，改用已有`state`(active/withdrawn)+`basis_refs`表达"这条边有多稳"。
   - `growth_mode`不再是Relation永久字段，改挂在`Attempt`活动记录上（复用DATA_CONTRACT.md §2已定义的Attempt子类，不新增对象类型）。
2. 画三条具体场景并各配一张mermaid图+对象/事件/跨层表：
   - 场景A：论文机制深挖→撞见工业应用→候选问题成形
   - 场景B：工业动向切入→倒查方法谱系→反哺自己基础学习
   - 场景C：学习失败→调用指导→调整→留证据→回原研究问题
3. 每个场景标注：复用对象、新增记录、跨越层、依据落点、用户点击动作、结果回哪——按Astra提出的六项标记要求逐项对应。
4. 汇总三场景共同暴露的具体缺口，不下结论、留给对比阶段。

## 结果

- 新文件：`progress/decisions/2026-09-11__research__knowledge-network-architecture-v0.3-scenarios.md`（PROPOSED/SCENARIO-WALKTHROUGH）
- 三个具体缺口（非猜测，均逐条核对过现有合同文件）：
  1. `relation_type`白名单没有覆盖"公司-产品"关系（场景A）和"活动引用指导条目"关系（场景C）——现有七类型（references/prerequisite/method_analogy/historical_influence/complements/goal_member/result_of）语义都不贴合。
  2. `SourceRef`的anchor按kind分流目前只覆盖`workbook_cell/workbook_range/workbook_image`（DATA_CONTRACT.md §2），不覆盖网页类来源（Google Alert指向的公告/博客）——工业维度一旦有真实数据会立刻撞上。
  3. v0.2 §7"指导库只需加`dimension_refs:["method"]`标签"这个提案在场景C走查后站不住：自动匹配只能证明"曾被推荐"，证明不了"用户接受、确实有效"，这是三个不同的事实。本稿建议最小补丁是加一条relation（"这次尝试参照了这条指导"），不新增对象类型、不新增A-F层。
- 一个明确留白（不确定，已在文中标注）：`产品X→方法M`是否可以复用现有`result_of`类型+`dimension_refs:industry`，还是需要新类型——本稿判断为"猜测语义相容，未确认"。
- TODO.md RD-2行追加note，`ledger_edit.py` CAS写入，收尾哈希`8fdfdb58...`，VERIFY-OK。

## 未完成 / 下一步

- 等待另一路（Astra）独立产出的三张对照场景图；两版对齐后需要一轮"真分歧 vs 假分歧"对比，本任务不包含对比工作。
- 三个具体缺口（两类relation_type、SourceRef网页anchor）尚未决定是否/何时动CONTRACTS.md白名单——留给C04范围决策时一并处理。
- v0.2 §10四个决策点仍未获用户裁定，本稿未重复处理，仅在场景内自然带出与其相关的具体例子（如场景B里`epistemic_status:unknown`的使用）。
- 本稿"猜测语义相容，未确认"标注的`result_of`复用可能性，需要在决定relation_type白名单是否修改时一并核实，不能直接当作结论采用。

## 验收证据

无代码变更，无测试运行；本任务为纯文档场景走查，验收标准是"三个场景是否具体到能暴露schema缺口"，非代码测试通过率。三处缺口均逐条对照了现有合同文件原文（TRACEABILITY.md/DATA_CONTRACT.md/CONTRACTS.md），不是凭空断言。

## 回滚

如需撤销，删除新增场景文件并用`ledger_edit.py --replace`把TODO.md该note移除即可；不影响任何已跑通的C00-C03代码或测试，也不影响v0.2文档本身。
