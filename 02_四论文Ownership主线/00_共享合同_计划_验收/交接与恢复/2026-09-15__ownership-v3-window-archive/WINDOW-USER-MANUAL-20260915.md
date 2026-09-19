# 使用手册 - ownership-v3三缺口补修窗口档案

> 面向：项目所有者（用户）和后续执行窗口

## 1 如何快速看懂当前状态

打开`CONTROLLER_ACCEPTANCE.md`，看文档标题旁的状态词：
- `CONTROLLER-PASS-WITH-ONE-FAIL`（当前状态）＝坐标层核验已经做完全部8个模块，7个没问题，1个（Ground Truth P0-P3）有3处具体错误需要处理。
- 如果之后再看到这份文件，状态词变了（比如变成`CONTROLLER-PASS`或`ALL-FIXED`），说明Ground Truth的问题已经被处理，去看该文件的Amendment历史了解怎么处理的。

打开三缺口方案文档`ownership-v3-three-gaps-remediation-plan.md`，看文档头部的`Authority`行：
- 只要还写着`DRAFT / AWAITING-USER-APPROVAL`，就说明缺口2（Transfer Card桥接文档）、缺口3（CrossEdgeIM正式写入）这两项还没有真正被批准执行——即使下面的Amendment记录了很多"前置已解除""技术上可以做了"，这些都不等于"已经在做"或"已经做完"。

## 2 如何选择下一件工作（想要的结果 → 选哪条流）

| 你想要的结果 | 该做什么 |
|---|---|
| 想知道课程材料是不是真的有错 | 看`CONTROLLER_ACCEPTANCE.md` §2.5，Ground Truth P0-P3的3处问题，每处都有具体的PDF位置证据 |
| 想让Transfer Card机制真正开始用 | 明确对AI说"批准撰写`TRANSFER_CARD_BRIDGE.md`"或类似的清晰表态——目前只是"技术上已经准备好了"，还没人批准动手写 |
| 想让CrossEdgeIM的学习材料接上EdgeIM原文的具体引用 | 需要安排一次Sol（建设身份）的施工窗口，把方案文档里已经写好的锚点内容（第32/99/142行那句引用）交给它去写进正式材料 |
| 想知道整体还剩多少活没干 | 看`WINDOW-ARCHIVE-20260915.md` §5"当前明确没有完成的工作"，按四类分好了 |
| 想知道这个窗口具体做了什么、按什么顺序 | 看`WINDOW-WORKLOG-20260915.md`，按事件顺序写的阶段日志 |

## 3 各工作流的操作与验收方法

### 工作流：批准缺口2执行
- **开工前要回答的问题**：是否接受方案文档§3描述的内容（判定枚举DROP/PARK/PROMOTE，配套模板`research_growth/方法论/TRANSFER_CARD_TEMPLATE.md`）？如果接受，直接说"批准"或"写"即可，不需要再重新讨论方案本身（本窗口已经把技术细节都核实过了）。
- **应看到的产物**：新文件`learning/training/lu-edgeim-algo1/TRANSFER_CARD_BRIDGE.md`。
- **不能接受的替代证据**：如果这份文件出现了，但B-DEFENSE六个任务仍然一条真实的Transfer Card判定都没有产出（还是`SHARED_ARTIFACTS.md`表格里那个空占位），说明"接线"这个动作本身还没有真正发生，桥接文档只是搭好了桌子，饭还没上。

### 工作流：核实Ground Truth的3处错误
- **开工前要回答的问题**：这3处（Eq.2/DS1-3/illustrative）是课程材料真的编错了，还是引用了论文的某个补充材料/其他版本导致的？
- **应看到的产物**：一份简短的溯源结论（哪怕结论是"确认是错误，没有其他来源依据"）。
- **不能接受的替代证据**：不能因为"坐标层核验已经做过一轮"就跳过这个溯源步骤直接下结论说"肯定是错的"——本窗口的核验只证明了"PDF正文里没有这些标签"，没有证明"课程材料的作者当时依据的是不是别的什么文件"。

## 4 如何检查档案没有丢

本归档包共6个正文文件+1个manifest+1个校验和文件，共8个文件。检查方法：

```bash
cd progress/handoff/2026-09-15__ownership-v3-window-archive/
sha256sum -c WINDOW-ARCHIVE-MANIFEST-20260915.sha256
```

如果输出全部是`OK`，说明文件完整未被篡改。如果某一行报`FAILED`，说明对应文件内容变了（可能是被其他窗口误改，也可能是本窗口后续又补充了内容而忘记重新生成校验和——后者不算问题，但要留意manifest本身是否也该更新）。

## 5 如何报告进度

用固定格式（供后续窗口/用户快速理解现状）：

```
[ownership-v3三缺口] 坐标层核验：8/8完成（7 PASS + 1 FAIL: Ground Truth P0-P3）
[ownership-v3三缺口] 缺口2执行：<未批准/已批准待撰写/已撰写待验证>
[ownership-v3三缺口] 缺口3执行：<待Sol施工窗口/施工中/已写入>
[TASK-20260906-004] 状态：已裁定，INDEX与task log一致（in_progress）
```
