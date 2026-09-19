---
id: TASK-20260915-016
title: ownership-v3独立QA(缺口1)第一批坐标核验：B-EVAL+CrossEdgeIM P0-P3
date: 2026-09-15
runtime:
  model: Fable 5
  effort: high
  effort_source: pdftotext逐页提取原始PDF+逐字比对课程材料声称坐标，非读转述
  launch: Claude Code CLI（用户交互会话，非无人值守）
type: research
status: completed_with_open_gates
area: learning/training/lu-edgeim-algo1
project: lu-side
todo_ids: []
owners:
  - user
related:
  - progress/handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md
  - progress/decisions/2026-09-15__research__ownership-v3-teaching-debt-priority-queue.md
  - progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md
  - learning/training/lu-edgeim-algo1/ownership-v3/edgeim/B-EVAL/README.md
  - learning/training/lu-edgeim-algo1/ownership-v3/crossedgeim/P0-P3/README.md
---

# 目标

推进队列（`TASK-20260915-015`）中标注为"唯一无阻塞可继续项"的#1独立QA缺口：对B-EVAL六项任务和CrossEdgeIM P0-P3四阶段声称的论文坐标做`pdftotext`独立核验，产出正式`CONTROLLER_ACCEPTANCE.md`（此前路径已建但文件未写，见`TASK-20260915-007`）。

# 最终结果

新建`progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`。坐标层核验结果：B-EVAL（pp.5-7、Eq.4文字锚点、Tables I-III）全部核对通过；CrossEdgeIM P0-P3（physical pp.1-6、Table I、Figs.2-3、Eq.1-2、RELATED WORK/CONCLUSION/limitation结构元素）全部核对通过，但发现一处措辞差异——课程材料用"三层架构"描述CrossEdgeIM，原文实际用词是"three key stages"，语义接近但非逐字对应，已如实记入报告判定为"不算编造但建议修订"，不隐瞒也不夸大。连同此前`TASK-20260915-007`已核的B-S3B，累计3/8模块完成坐标层核验，全部PASS。

# 修改内容

- 新建 `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`：坐标层核验报告，含独立重放证据、主控重点复核项、边界声明（采用`three-desks-v0.1`先例格式）。
- 本条目：新建本任务日志；`progress/task_logs/INDEX.md` 待用 `ledger_edit.py` 保形插入。
- 未修改 `ownership-v3/` 任何文件（Sol独占写域）；未修改`BUILD_STATUS.md`总表。

# 验收与证据

| 验收项 | 标准 | 结果 | 证据 |
|---|---|---|---|
| B-EVAL坐标核验方法可信 | 直接pdftotext提取原始PDF逐字比对 | PASS | `pdftotext -f 5 -l 7`输出含"This section introduces the F-measure"/"The F-measure is computed using the following formula"/TABLE I(138行)/TABLE II(221行)/TABLE III(408行) |
| CrossEdgeIM坐标核验方法可信 | 同上，针对CrossEdgeIM-2026-IoTMag.pdf | PASS | `pdftotext -f 1 -l 6`输出含"TABLE I. Basic statistics..."/"FIG. 2. Petri net discovered by inductive miner."/"FIG. 3. Petri net discovered by CrossEdgeIM."/公式(1)(2)/RELATED WORK(145行)/CONCLUSION(555行) |
| 措辞差异如实记录不隐瞒 | 发现"三层架构"vs"three key stages"后不回避 | PASS | 报告§2.3/§3明确记录此差异并给出具体行号(206行) |
| Fixture任务可执行性核对 | 检查TRAINING_FIXTURE.md是否有具体输入和可判定产出 | PASS | B-EVAL fixture含4行虚构数据表+5项具体任务；CrossEdgeIM P1 fixture含O1/O2组织+3个case时间戳+6项具体任务 |
| 未越权代做用户/Sol工作 | 报告边界声明不包含代复算、不改BUILD_STATUS.md | PASS | 报告§3明确"这需要用户或Sol实际做一遍复算并留痕，不是主控代做" |
| 不过度推广判定范围 | 报告明确标注剩余5模块未核 | PASS | 报告§4/§5明确"sigRank/Ground Truth/B-DEFENSE/B-S2/B-S3A五个模块尚未核对...不得从三个模块PASS推广为全部PASS" |

# 当前状态

缺口1（独立QA）坐标层核验进度：3/8模块完成（B-S3B、B-EVAL、CrossEdgeIM P0-P3），全部PASS。这只是"坐标是否真实"这一层，不是"任务能否被真实完成"或"rubric是否合理"这两层——报告边界已明确区分，未越界宣称完整验收。

# 尚未完成

- 剩余5个模块（sigRank P0-P3、Ground Truth P0-P3、B-DEFENSE、B-S2、B-S3A）的坐标层核验。
- 已核3个模块的"任务能否被真实完成"层核验（比如B-EVAL fixture的F-measure复算是否真的落在`<=1e-4`容差内）——这需要实际动手复算，本次只核了"任务描述本身是否可执行"，未做复算本身。
- `BUILD_STATUS.md`总表是否需要根据这批新证据更新——仍是`TASK-20260915-007`记录的未决问题（谁来改、以什么方式改），本次不处理。
- CrossEdgeIM P3声称的consumer链条（Transfer Card/B-DEFENSE）是否真实产出判定——本次报告只是重申了`TASK-20260915-007`已发现的"字段预填非真实消费"，未做新核实。

# 下一步

1. 若继续缺口1：对剩余5模块套用同样的pdftotext核验方法。
2. "三层架构"vs"three key stages"这处措辞差异是否需要修订课程材料——落在Sol写域内，建议记入队列文档#4条目下单独提给用户/Sol，不由主控直接改`ownership-v3/`内文件。

# 可拓展方向

- 本次核验方法（pdftotext提取+grep锚点比对）已经用了两次（`TASK-20260915-007`和本次），可以考虑写成一个可复用的小脚本而非每次手打命令，减少下次核验的重复劳动。这是效率改进，不影响本次判定的有效性，仅记录供参考。

# 风险与回滚

- 风险：`pdftotext`对图像化公式（如Eq.4的实际数学符号）无法转出内容，本次核验依赖"公式前后文字锚点"作为间接证据，不是对公式符号本身的逐字核验；如果公式内容本身被课程材料转述错误（而不是坐标位置错误），本次方法无法探测到，这是方法本身的已知局限，已如实说明。
- 回滚：新建单文件，删除即可完全回滚。

# 文件和产物

- `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`（新建）
- 本文件
