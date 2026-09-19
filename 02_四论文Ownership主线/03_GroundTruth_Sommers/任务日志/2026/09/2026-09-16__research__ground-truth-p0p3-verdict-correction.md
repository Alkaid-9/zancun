---
id: TASK-20260916-002
title: 主控复核纠正Ground Truth P0-P3判定：并行子代理FAIL判定含2处误判，订正为PASS
date: 2026-09-16
runtime:
  model: Fable 5
  effort: high
  effort_source: 独立重新pdftotext提取Sommers全文30页+逐字核对Eq.2/DS1-3/illustrative三项，发现子代理搜索范围不足与判定尺度问题
  launch: Claude Code CLI（用户交互会话，非无人值守；用户"继续做？"后主控主动选择处理最紧急项）
type: research
status: done
area: learning/training/lu-edgeim-algo1/ownership-v3/ground-truth
project: lu-side
todo_ids: []
owners:
  - user
related:
  - progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md
  - progress/task_logs/2026/09/2026-09-15__research__ownership-v3-controller-acceptance-batch2-parallel.md
  - learning/training/lu-edgeim-algo1/ownership-v3/BUILD_STATUS.md
note: TASK-20260916-001已由中央发号器发出但未登记即被压缩摘要转述、本窗口不予采信重新领号（协议"发出即占用不回收"，先例见TASK-20260812-010/011）；001作废跳号，本任务正式号=002
---

# 目标

用户回来后要求"继续做？"，主控选择处理上一窗口交接单标注的最紧急项——Ground Truth P0-P3的3处坐标/标签错误溯源。目标：确认这3处是课程材料真的编错、还是引用了论文别的版本，给出准确结论，不停留在"待核查"。

# 最终结果

**溯源结果：3处质疑中2处是上一批次并行子代理自己的核验错误，不是课程材料的问题；剩余1处属实但不算编造。**

1. **"Eq.2应为Eq.1"——子代理误判，已纠正**。主控重新用`pdftotext -f 1 -l 30 -layout`提取Sommers全文30页，全文搜索发现PDF第726行确实存在编号为(2)的公式（p.15"Simulation"小节的转移概率公式`p(tµs=tµ|w)=w(t)/Σw(t')`）。README原文"重建 `Psi(M,pi,h)=M union h(pi)`、mapping 约束和 simulation Eq.2"实际描述的是**两个不同的公式**：转换函数`Psi(...)`对应第638行的公式(1)，"simulation Eq.2"对应第726行的公式(2)——是两件事，不是"README声称Eq.2但其实是Eq.1"这种单一错误。上一批次子代理只搜索到公式(1)附近就停止，未继续读到p.15的Simulation小节，属于搜索范围不足导致的假阳性判定。
2. **"illustrative不在原文"——子代理误判，已纠正**。子代理的grep核验方法本身没错（"illustrative"这个词确实不在Fig.4图题里），但判定尺度有误：README原句"不把 Fig.4 的 illustrative `M'` 叫 `M^L` 或 log `L'`"里，"illustrative"是**课程材料对Fig.4性质的形容词**（提醒学习者这是例示性的图），不是声称"原文逐字用了这个词"。Fig.4图题原文"a modified version of M"在语义上正是例示性、非正式定义的意思，与"illustrative"语义吻合，只是转述关系。子代理把"课程材料的描述性转述"错误当作"应该逐字匹配原文"来判定，标准过严。
3. **"DS1/DS2/DS3不存在"——复核维持原判，属实**。全文确认0命中这三个缩写。原文用三个完整命名的数据集指代："package delivery process"（第一个）、"energy contract process"（第二个）、"real-life assembly process"（Omron合作方数据，第三个），从未用"DS1/DS2/DS3"这种缩写。课程材料自己的`TRAINING_FIXTURE.md`也没有出现这几个缩写或映射说明。这是课程材料自创但未标注为自创的简称，不是编造数据（三个数据集本身真实存在），但确实与原文标签不一致。**顺带发现**：`BUILD_STATUS.md`第29行本身也使用"DS2/DS3"这个简称（"Ground Truth 的代码/数据版本、种子、DS2/DS3 规模与复现实参不完整"），说明这个简称是建设者贯穿使用的习惯用法，不是孤立的笔误，但依然建议在README或COVERAGE_MATRIX中补一句映射说明。

已更新`CONTROLLER_ACCEPTANCE.md`：§2.5改写为"复核订正"版本、文档标题与开篇结论从"CONTROLLER-PASS-WITH-ONE-FAIL"改为"CONTROLLER-PASS"（8/8全部PASS，含1处简称记录）、§3第3条改写为"核验被纠正"的记录、§4边界补充"其余4个子代理模块未经同等复核"的提醒、§5结论同步。

# 修改内容

- 编辑 `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`：§2.5核验记录改写、标题/开篇/§3/§4/§5同步更新为8/8全PASS。
- 本条目：新建本任务日志；`INDEX.md`待用`ledger_edit.py`保形插入。
- 未修改 `ownership-v3/ground-truth/` 任何文件（README本身的DS1/DS2/DS3简称是否要改，属于Sol写域，本次只记录建议不代改）；未修改`BUILD_STATUS.md`（已确认其第17/29行与本次订正结论不矛盾，DS2/DS3简称用法双方一致）。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 复核基于独立重新核验，非凭猜测纠正 | 重新pdftotext提取+grep，不采信上批次转述 | PASS | `/tmp/sommers_full.txt`全文提取，`grep -n`定位第638/726行两个公式编号 |
| Eq.2纠正有具体证据 | 找到PDF中真实存在的公式(2)及其上下文 | PASS | 第726行`p(tµs = tµ |w) = ... (2)`，前文"Simulation"小节标题（第702行） |
| illustrative纠正有语义论证而非只咬字面 | 说明"形容词转述"与"应逐字匹配"的区别 | PASS | README原句结构"不把Fig.4的illustrative M'叫M^L"——illustrative修饰的是课程材料对图的定性，非声称引用原文用词 |
| DS1/DS2/DS3属实判定维持，不因两处纠正而连带松动 | 独立验证，不受前两项纠正结果影响判断标准 | PASS | 全文grep确认0命中；三个数据集完整名称逐一定位（p.19/20/22附近） |
| 与BUILD_STATUS.md交叉核对确认无新增矛盾 | 检查该文件是否也用DS1/DS2/DS3简称 | PASS | 第29行原文包含"DS2/DS3"，用法与本次发现的课程材料习惯一致 |
| 报告文档无乱码字节 | grep "�" | PASS | 首次编辑引入1处乱码（"可信性"），已修正复扫0命中 |

# 当前状态

Ground Truth P0-P3坐标层核验最终判定：**PASS**（含1处课程材料简称建议：DS1/DS2/DS3应在README或COVERAGE_MATRIX补注映射说明，不影响整体判定）。`CONTROLLER_ACCEPTANCE.md`当前状态为8/8模块全部PASS，不再有FAIL项。

**更重要的过程性发现**：批次2（`TASK-20260915-020`）派发的5个并行子代理中，至少1个（Ground Truth P0-P3）的核验结论存在2处误判，且误判方向都是"过度报告问题"（假阳性FAIL），不是"漏报问题"。这提示并行子代理核验的可靠性边界：否定性结论（"某关键词/标签全文0命中"）需要确认搜索范围是否真的覆盖了声称的全部页码/章节，以及判定标准是否混淆了"任务描述的转述性形容词"与"应逐字对应原文的技术标签"。

# 追加：sigRank P0-P3抽查（同一窗口内继续，未新开task_id）

响应"下一步"第1条，主控独立用`pdftotext -layout research/papers_lu/sigRank-2026-TSC.pdf`重新提取全文（`/tmp/sigrank_full.txt`，711行），抽查`CONTROLLER_ACCEPTANCE.md`§2.4记录的sigRank P0-P3模块，检查是否存在同类"搜索范围不足"或"转述判定过严"问题。

- **Definition 1-6**：全部逐字存在（第133/157/195/204/256/260行），与§2.4记录一致。
- **"9 methods"计数偏差**：复核证实原判定的推测方向正确——PDF原文第391-392行"The following seven state-of-the-art event log sampling techniques, along with a filter-based model discovery technique, are used as baselines"=7+1=8个baseline；第406行原文自己也说"the efficiency of the eight sampling techniques"，确认原文口径是8个baseline方法。若把sigRank自身算作第9个方法，总数正好凑成9，与README"9 methods"的表述吻合，不是编造，是计数口径（是否把sigRank自身计入）的正常差异，非误判。
- **`10/12`**：第432行"sigRank attains the highest F-measure (10/12)"逐字存在。
- **`100 times`**：第516行"which is approximately 100 times longer than other techniques"逐字存在（README"100x"是数字简写，语义一致）。
- **Table I/II/III、Fig.6**：全部存在（第351/463/482/471行），位置与README声称吻合。
- **结论：本次抽查未发现sigRank P0-P3存在同类误判**，§2.4原判定（PASS，含1处计数偏差记录）经复核确认成立，不需改判。

这次抽查把"待复核"的批次2模块从4个减到3个（B-DEFENSE、B-S2、B-S3A仍未经主控复核）。

# 尚未完成

- 批次2剩余3个模块（B-DEFENSE、B-S2、B-S3A）**未经过同等级别的主控复核**（sigRank已于本文件"追加"节抽查确认无误）；理论上仍存在同类误判风险，尚未逐一复核。
- DS1/DS2/DS3简称与原文数据集名称的映射说明——建议但未落地到`ground-truth/P0-P3/README.md`或`COVERAGE_MATRIX.md`，落地本身属于Sol写域。
- `TASK-20260906-004`状态裁定、缺口2执行批准、缺口3正式写入等此前交接单列出的其他待办，本次未涉及，仍是原状态。

# 下一步

1. 若要继续提高批次2剩余3模块（B-DEFENSE/B-S2/B-S3A）的信心，可安排针对性复核（同样检查"搜索范围不足"或"转述判定过严"两类问题）。
2. DS1/DS2/DS3映射说明的补注建议移交Sol下次施工窗口。
3. 继续处理交接单§3列出的其他入口（缺口2批准/缺口3移交/`BUILD_STATUS.md`一致性裁定）。

# 可拓展方向

- 本次纠正过程本身值得作为"如何复核子代理产出"的一个具体案例：不是重新执行同样的grep命令看是否得到相同结果（那只会重复同样的错误），而是要扩大搜索范围（读全文而非停在第一个匹配处附近）、重新审视任务描述的语义结构（区分"这是转述形容词"还是"这声称是原文用词"）。这两个纠正手法可以写成后续核验类任务的检查清单条目。

# 风险与回滚

- 风险：本次订正依赖主控对README任务描述的语义解读（尤其"illustrative"一项），存在解读主观性；如果Sol或用户认为这个解读不成立，仍可能需要修改README措辞以避免歧义，即使不算"错误"也可能算"表述不够清晰"。
- 回滚：本次只编辑了`CONTROLLER_ACCEPTANCE.md`一份文件（修改已有段落，非新增文件），如需回滚可用`git diff`定位改动范围后手动还原为批次2的原始判定文本。

# 文件和产物

- `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`（编辑，§2.5/标题/§3/§4/§5更新）
- 本文件
