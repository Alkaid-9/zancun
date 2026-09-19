---
id: TASK-20260916-005
title: 主控独立复核批次2剩余3模块（B-DEFENSE/B-S2/B-S3A）：坐标层全PASS，顺带发现论文原文一处印刷错误
date: 2026-09-16
runtime:
  model: Fable 5
  effort: high
  effort_source: 独立重新pdftotext提取EdgeIM PDF前7页+grep逐项定位Definition/Algorithm/Section坐标，逐行核对语义
  launch: Claude Code CLI（用户交互会话，非无人值守；用户"继续？"后主控主动选择处理交接单标注的下一步第一条）
type: research
status: done
area: learning/training/lu-edgeim-algo1/ownership-v3/edgeim
project: lu-side
todo_ids: []
owners:
  - user
related:
  - progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md
  - progress/task_logs/2026/09/2026-09-15__research__ownership-v3-controller-acceptance-batch2-parallel.md
  - progress/task_logs/2026/09/2026-09-16__research__ground-truth-p0p3-verdict-correction.md
note: 领号时curl中央发号器返回TASK-20260916-005；grep INDEX.md核实003/004号未见任何登记痕迹，判断与此前001号性质相同——发号器"发出即占用不回收"，被发出但从未被消费登记的跳号；未发现任何窗口正在争用这两个号，按既定协议（先例TASK-20260812-010/011、本窗口内001号）作废跳号处理，不占用、不补登
---

# 目标

延续`TASK-20260916-002`交接单"下一步"第1条：对`CONTROLLER_ACCEPTANCE.md`批次2（`TASK-20260915-020`）5个并行子代理核验模块中，主控尚未复核的剩余3个（B-DEFENSE、B-S2、B-S3A）做同等级别的独立坐标层核验，检查是否存在与Ground Truth P0-P3同类的"搜索范围不足"或"转述判定过严"误判。

# 最终结果

**3个模块坐标层核验全部PASS，未发现同类误判；额外发现论文原文自身一处印刷错误（非课程材料问题）。**

主控独立执行：`pdftotext -f 1 -l 7 -layout research/papers_lu/EdgeIM-2025-ICWS.pdf /tmp/edgeim_p1-7.txt`重新提取EdgeIM论文前7页全文，配合无`-layout`模式交叉核对（双栏排版在`-layout`下会把左右两栏拼接到同一视觉行，需要额外核对避免误读），逐项核对三个模块README声称的论文坐标：

1. **B-DEFENSE**（声称：pp.1-7，sections I-II、IV-VI，EdgeAlpha/EdgeMiner来源标注，三阶段方法，limitation taxonomy）：Section I（line 50）、II（line 91）、III（line 77，未跳过）、IV（line 147）、V（line 379）、VI（line 435）全部逐字存在；EdgeAlpha出现在正文line 60与Table II对比数据，EdgeMiner出现在line 37/41及reference[24][25]；"three key stages"在Abstract（line 37）与正文line 67（写作"three key steps"，同义变体）逐字确认；Conclusion（line 449起）"Several areas warrant further exploration..."为作者自陈未来工作，支持limitation taxonomy分类。**PASS**。
2. **B-S2**（声称：physical pp.2-4，Definitions 3-4、section IV.A/C、Algorithm 2、符号`S_i/E_i/R_i`、`hash(activity) mod k`）：Definition 3（line 118，物理p.405）、Definition 4（line 147，物理p.406）均在声称范围内；section IV.A（line 149，p.406）、IV.B（line 265，README未提及但确实存在）、IV.C（line 250，p.407）均存在；Algorithm 2标题（line 275）及全部内容（line 282-311）落p.407；`hash(e.activity) mod k`（line 289）、`(Si, Ei, Ri)`三元组（line 258、line 342）逐字确认。**PASS**。
3. **B-S3A**（声称：physical p.5，section IV.D，Algorithm 3 lines 1-8）：section IV.D标题（line 326）落物理p.408（=声称的p.5）；Algorithm 3标题行（line 340）与内容行1-8（line 344-351）同页；`S←S∪Si`（line 346）、`E←E∪Ei`（line 347）、`DFG(a,b)←DFG(a,b)+Ri(a,b)`（line 349）与README描述完全吻合；行号9（line 352 "Function DFG, S, E"）确认是递归分解函数定义起点，不属于1-8范围，与`TASK-20260915-016`已核过的B-S3B（lines 9-23）边界互补不重叠，交叉核验无误。**PASS**。

**附带发现（非课程材料问题，论文原文自身的印刷错误）**：EdgeIM论文（ICWS 2025）正文中，Algorithm 3的标题被印刷成"Feature-Preserving Sampling"（line 340），与Algorithm 1（line 282）完全同名。但Algorithm 3实际内容是"中央节点聚合与模型发现"逻辑（集合union+关系加法），对应section IV.D标题"Central Node Merging and Model Discovery"，与Algorithm 1的"特征保持采样"内容完全不同——这是论文作者排版时的疏漏，不影响B-S3A判定（课程材料引用的是行号内容而非标题文字），但记录在案以免日后有人拿标题文字去核对反被误导。

已更新`CONTROLLER_ACCEPTANCE.md`：§2.6/§2.7/§2.8三个章节标题追加"2026-09-16主控抽查复核"标注并各附一段复核证据；§4边界段落与§5结论段落待同步（见"尚未完成"）。

# 修改内容

- 编辑 `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`：§2.6/§2.7/§2.8三节标题与正文追加主控抽查复核记录。
- 本条目：新建本任务日志；`INDEX.md`用`ledger_edit.py`保形插入。
- 未修改 `ownership-v3/edgeim/{B-DEFENSE,B-S2,B-S3A}/README.md`（三个模块本身内容未改，本次只做核验不做课程材料修订）。
- 未修改 `research/papers_lu/EdgeIM-2025-ICWS.pdf`（发现的印刷错误是论文原文自身问题，不是本项目产物，不做任何"修正"）。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| 独立重新提取原文，不采信批次2子代理转述 | 主控自己跑pdftotext，不读README/子代理报告作为坐标来源 | PASS | `/tmp/edgeim_p1-7.txt`（545行，`pdftotext -f 1 -l 7 -layout`） |
| 双栏排版拼接风险已规避 | 关键坐标用grep精确定位+无-layout模式交叉核对 | PASS | 例：Definition 4所在line 147同时含右栏"IV. EDGE-BASED..."标题，已用grep分离确认 |
| B-DEFENSE三阶段用词核验 | Abstract与正文是否逐字使用"three key stages" | PASS（含1处同义变体记录） | Abstract line 37="three key stages"；正文line 67="three key steps"（同义变体，非矛盾） |
| B-S2符号与算法逐字核验 | Definition 3/4、Algorithm 2、hash mod k、Si/Ei/Ri均存在 | PASS | line 118/147/275-311/289/258/342 |
| B-S3A行号边界与B-S3B交叉验证 | lines 1-8与9-23互补不重叠 | PASS | line 344-351（1-8内容）vs line 352起（9号为Function定义起点） |
| 报告文档无乱码字节 | grep "�" | PASS | 编辑后复扫0命中 |

# 当前状态

`CONTROLLER_ACCEPTANCE.md`§2.6/§2.7/§2.8三节的复核标注已写入并经本会话重新读盘确认真实落地。批次2全部5个并行子代理核验模块（sigRank、Ground Truth、B-DEFENSE、B-S2、B-S3A）现在均已经过主控独立复核：Ground Truth经`TASK-20260916-002`纠正2处误判后PASS，sigRank经同任务抽查确认无误判，本任务确认B-DEFENSE/B-S2/B-S3A三项均无同类误判。

**ownership-v3独立QA（缺口1）坐标层核验的可信度基线**：8个抽样模块（B-S3B、B-EVAL、CrossEdgeIM P0-P3、sigRank P0-P3、Ground Truth P0-P3、B-DEFENSE、B-S2、B-S3A）已全部经过主控本人独立复核确认，不再有"未经复核，理论上存在误判风险"的模块。

# 尚未完成

- `CONTROLLER_ACCEPTANCE.md`§4边界段落与§5结论段落仍是旧措辞（"其余3项未经过同等级别的主控复核"），需要同步改为"全部8个模块均已经过主控复核确认"——**本任务日志登记后紧接执行**，属于本次工作的收尾一部分，不是留给未来的开放项。
- DS1/DS2/DS3简称映射说明（Ground Truth模块，`TASK-20260916-002`已建议）——落地到README或COVERAGE_MATRIX属于Sol写域，本任务未处理。
- `TASK-20260906-004`状态裁定、缺口2执行批准、缺口3正式写入等更早交接单列出的其他待办，本次未涉及。

# 下一步

1. 同步更新`CONTROLLER_ACCEPTANCE.md`§4/§5为"8/8模块全部经主控复核"的最终措辞（紧接本次收尾）。
2. 移交Sol：DS1/DS2/DS3映射说明补注、Algorithm 3标题印刷错误的用户侧知会（如果用户后续要联系论文作者或在自己的笔记中引用，应知悉这处原文错误）。
3. 处理更早交接单列出的其他入口（缺口2批准/缺口3移交/`TASK-20260906-004`状态裁定）。

# 可拓展方向

- 本次核验方法论补充一条经验：双栏排版PDF用`pdftotext -layout`提取时，同一视觉行号可能拼接了左右两栏不相关的内容（本次实测Definition 4所在行同时含右栏的章节标题），核验类任务遇到双栏论文时应默认做"grep定位+无-layout交叉核对"两步，不能只信`-layout`输出的行号做视觉判断。
- 发现论文原文自身错误（Algorithm 3标题印刷错误）这件事本身提示：坐标层核验不能只核对"标题文字是否存在"，还要核对"标题下方内容是否与标题描述的功能一致"——本例中标题文字确实存在（"Algorithm 3: Feature-Preserving Sampling"），但内容与标题描述的功能完全不符，如果只做标题字符串匹配会被误导为"课程材料引用错误"，实际是原文自己的问题。

# 风险与回滚

- 风险：无实质性风险。三项判定均为PASS，未推翻任何已有结论，只是把"未经复核"的状态补齐为"已复核确认无误"。
- 回滚：本次只编辑了`CONTROLLER_ACCEPTANCE.md`的§2.6/§2.7/§2.8三节标题与追加段落，未删除任何原有文字。如需回滚，`git diff`定位新增段落后删除即可恢复到批次2的原始状态。

# 文件和产物

- `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`（编辑，§2.6/§2.7/§2.8三节追加复核记录）
- `/tmp/edgeim_p1-7.txt`（临时核验证据，非项目产物，会话结束后可能被系统清理）
- 本文件
