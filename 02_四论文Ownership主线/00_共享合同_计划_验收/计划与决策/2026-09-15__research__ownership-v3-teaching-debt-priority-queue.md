# ownership-v3 补修优先级队列：三缺口 + 早期教学债合并登记

日期：2026-09-15。`TASK-20260915-015`。状态：`DESIGN-ONLY / NOT-EXECUTED`。

执行[进组补充计划](2026-09-15__research__lu-onboarding-supplement-next-plan.md) §3 J2步骤："用原三缺口交接加旧教学债构成有优先级队列；每缺口一个明确目标文件/负责人/来源/验收/停止条件；不一次重写全课程"。本档只做登记与结构化，不裁定顺序、不代用户/Sol做任何实际补修动作。

## 1. 为什么合并

三缺口（[交接](../handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md)）是09-13 v3合同发现的结构性缺口；另有5项"早期教学债"来自更早的课程内容审计（[多层基线§2.1](2026-09-14__research__multilayer-content-map-provisional-baseline.md:48)），已在09-15被独立核对并确认仍未关闭（[参考评估§2.1](two-desks-delta-20260914/REFERENCE_EVALUATION.md:48)）。两组此前分别记录在不同文档，未合并成一张可执行队列，容易造成"三缺口关了=课程都补完了"的误读——[参考评估原文](two-desks-delta-20260914/REFERENCE_EVALUATION.md:57)已明确警告"I01三缺口不能自动覆盖这些"。

## 2. 队列（不含强制执行顺序；依赖关系单独标注）

| # | 缺口/债务 | 目标文件 | 负责人 | 来源 | 验收标准 | 停止条件 |
|---|---|---|---|---|---|---|
| 1 | 独立QA缺口（I01） | `progress/audits/2026/09/2026-09-15__ownership-v3-controller-acceptance/CONTROLLER_ACCEPTANCE.md`（目录已建，文件未写） | 主控（只读核验，非Sol） | [交接§4](../handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md:41) | B-EVAL六项任务、CrossEdgeIM P0-P3四阶段全部完成可执行性核对；采用[CONTROLLER_ACCEPTANCE.md先例格式](three-desks-v0.1/sol-delivery/p1-20260910-sol/CONTROLLER_ACCEPTANCE.md) | 无客观阻塞；可随时继续抽样 |
| 2 | 研究问题出口缺口（I01） | `learning/training/lu-edgeim-algo1/TRANSFER_CARD_BRIDGE.md`（未撰写） | 待定（方案A=Sol／方案B=主控，用户未选） | [交接§4缺口2](../handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md:55) | B-DEFENSE六任务至少一条产出真实DROP/PARK/PROMOTE判定，非字段预填 | **阻塞**：用户尚未在方案A/B之间表态（[方案文档§5 Amendment A2](2026-09-15__research__ownership-v3-three-gaps-remediation-plan.md)已明确技术前置清空≠批准豁免） |
| 3 | 跨论文连接落地点缺口（I01） | CrossEdgeIM P0-P3 README（正式写入需Sol施工窗口） | Sol（v3合同§8.1独占写域） | [交接§4缺口3](../handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md:68) | 接入EdgeIM Mechanism Map原文具体引用句，非泛泛"已消费" | **阻塞已解除**（`TASK-20260915-018`，2026-09-15）：`TASK-20260906-004`状态冲突按事实裁定——INDEX行本身过时，已更正为`in_progress`与自身task log一致；v3合同§8.1前置条件视为满足；剩余阻塞仅为"正式写入需Sol施工窗口"（写域限制，非状态冲突） |
| 4 | 完整IM→过程树→Petri net→soundness教学链 | B-S3B模块补充材料（`ownership-v3/edgeim/B-S3B/`内，写域=Sol） | Sol | [参考评估:57](two-desks-delta-20260914/REFERENCE_EVALUATION.md:57) | 有来源的解释、示范、渐进练习与不同结构验收；"核对坐标通过"或标`SOURCE-OPEN`不能单独关闭 | 无新增阻塞；但落在Sol写域内，主控不可代写 |
| 5 | 四篇各30分钟连续追问 | 待定（新增题面/追问脚本文件，路径未定） | 待定 | [参考评估:58](two-desks-delta-20260914/REFERENCE_EVALUATION.md:58) | 对应题面、独立计时、评分、记录与重做；D1总30分钟不能替代单独连续追问30分钟 | 未查sealed，不能把"公开检索未找到"当"确认不存在"；需要先确认是否已有隐藏安排 |
| 6 | 跨四篇D2 | 待定（四论文跨篇题面文件，路径未定） | 待定 | [参考评估:59](two-desks-delta-20260914/REFERENCE_EVALUATION.md:59) | 四论文跨篇题面、评分及记录入口；模块D+2/D+7不能替代 | 依赖#4完成后D2范围才完整（D2覆盖四篇全文，B-S3B教学链缺口不补，D2出题基础不完整） |
| 7 | QA总表、模块回执、共享入口一致 | `BUILD_STATUS.md`（`ownership-v3/`内，写域=Sol/主控需谨慎） | 待定（[交接§5发现](../handoff/2026-09-15__ownership-v3-three-gaps-remediation__handoff.md)：谁来改此文件本身待讨论） | [参考评估:60](two-desks-delta-20260914/REFERENCE_EVALUATION.md:60) | 总表状态按#1真实审查结果统一，不与既有QA-PENDING行矛盾 | **依赖#1**：必须先有真实`CONTROLLER_ACCEPTANCE.md`结论，才能判断总表要不要改，否则是循环依据 |
| 8 | EX-05真实卡点、三篇教学展开与App/CLI交接 | 待定（EX-05目录内新增交接说明，或独立卡点记录） | 用户本人参与（AI只能提供脚手架，不能代做学习动作） | [参考评估:61](two-desks-delta-20260914/REFERENCE_EVALUATION.md:61) | 用户真实小过程验证必要前置与返回点；不是更多表格/导出功能 | 需要用户本人实际学习动作，AI不能代排 |

## 3. 依赖关系图（仅标注文档中已明确的客观依赖，非主观排序建议）

```text
#3（跨论文接线）  ← 状态冲突阻塞已解除（TASK-20260915-018，2026-09-15）；剩余仅写域限制（需Sol施工窗口）
#2（Transfer Card桥接） ← 阻塞于 方案A/B表态（用户）
#7（QA总表一致）  ← 依赖 #1（独立QA真实完成）
#6（跨四篇D2）    ← 依赖 #4（B-S3B教学链补完，否则D2出题范围不完整）
#1、#3、#4、#5、#8 当前均无客观阻塞（#3剩余仅写域限制），可并行推进
```

此图不代表"必须按此顺序做"，只标注"做后者前，前者必须先有结果"这一类硬依赖；没有依赖箭头的项之间不隐含优先级。

## 4. 队列验收标准

| 编号 | 可观察标准 |
|---|---|
| Q-AC1 | 每项缺口/债务都能在本表中找到目标文件、负责人、来源三项，缺一项本表本身即不算完整 |
| Q-AC2 | 依赖关系仅来自已核实的原文（v3合同§8.1、参考评估原表），不新增本档自己发明的顺序判断 |
| Q-AC3 | 表中"待定"项（#2负责人、#5/#6目标文件、#7负责人）如实标注待定，不假装已有答案 |
| Q-AC4 | 本表更新不改变#1-#8任何一项本身的验收标准原文，只做位置合并 |

## 5. 边界

本档不裁定`TASK-20260906-004`状态冲突、不裁定方案A/B、不代Sol/用户执行任何一项。本档也不是完整课程验收计划——[早期基线原文](2026-09-14__research__multilayer-content-map-provisional-baseline.md)明确"结构通过、课程内容通过和真实学习效果分别判断"，本队列只处理"结构性缺口是否登记完整"这一层。
