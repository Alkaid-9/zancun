# pending-r-track-20260908 — R线(自主研究线)方法学参考文献暂存登记

`生成: 2026-09-08 · 用户主任务窗口(非子代理)· 全部下载均来自公开合法渠道(arXiv开放获取/Google Patents公开详情页),零绕付费墙`

## 为什么单独暂存,不直接入 papers_lu/ 顶层

顶层 `papers_lu/` 目前的 12 篇 PDF 全部是**鲁法明署名**的核心论文(EdgeIM 四论文十字训练闭环 + 死锁/UAF/MHP/SBPN 谱系)。本目录这 5 篇是《第二条研究线-方向恢复与双入口试探-2026-09-08.md》§3.2/§3.3 提到的**外部方法学镜头**——P/O 两个候选研究入口的参考文献,不是鲁组署名成果,性质不同,故暂不与顶层混放。是否移入顶层、是否需要建正式 teardown,留待 P/O 入口实际选定后再判断,本次不擅自决定。

## 清单

| # | 文件 | 来源 | 判型/页数 | 对应候选入口 | 用途(据源文件§3.2/§3.3) |
|---|---|---|---|---|---|
| 1 | `ObjectCentricConformance-2312.08537.pdf` | arXiv 开放获取 | PDF 1.4,23页 | O(对象/交互一致性) | Object-Centric Conformance Alignments with Synchronization——对象身份与同步如何进入 alignment 形式化的外部方法镜头 |
| 2 | `TraceCompiler-2608.02680.pdf` | arXiv 开放获取 | PDF 1.7,17页 | Agent外圈(不抢当前实现) | 从 noisy traces 恢复有证据的 producer-consumer dependency |
| 3 | `CausalPastLogic-2605.20923.pdf` | arXiv 开放获取 | PDF 1.7,20页 | Agent外圈(不抢当前实现) | 分布式 LLM agent workflow 的因果可见性与本地运行时 guard |
| 4 | `Agentproof-2603.20356.pdf` | arXiv 开放获取 | PDF 1.7,26页 | Agent外圈(不抢当前实现) | 显式工作流结构、策略自动机、静态/运行时检查 |
| 5 | `CN119477231B-patent-page.html` | Google Patents 详情页(HTML,非PDF全文) | HTML,128KB | O(对象/交互一致性) | "基于托肯重演的对象为中心业务流程违规检查方法及系统"——鲁法明为发明人之一的专利,O入口的鲁侧直接线索;**PDF全文直链未获取成功(拉到387字节XML错误页),仅存档详情页HTML,标题/发明人可核验,权利要求全文仍缺** |

## 本轮同时尝试但未获取全文的鲁侧文献(未入本目录,登记于此备查)

| 题录 | DOI | 尝试结果 |
|---|---|---|
| 2021《基于程序运行轨迹Petri网模型挖掘的死锁检测方法》,鲁法明等,计算机集成制造系统27(9):2611-2624 | 10.13196/j.cims.2021.09.014 | CNKI DOI 解析页仅返回付费墙链接;期刊官网`cims-journal.cn`摘要页存在但未找到直开PDF端点(试了2个常见猜测URL均失败,未继续枚举);**未获取,需人工渠道(校园网/科研通/作者索取)** |

## 本轮成功拉取并已入库 papers_lu/ 顶层的鲁侧文献(不在本目录,记录于此供交叉参考)

| 文件 | 来源 | 说明 |
|---|---|---|
| `DeadlockLockSegGraph-2021-JOS.pdf` | 软件学报官网`jos.org.cn`直链(`jos/article/pdf/6244`) | 2021《基于锁增广分段图的多线程程序死锁检测》,鲁法明等,32(6):1682-1700;19页全文,首页题录/作者表核验一致,sha256 `514198a7...c670`;补齐了死锁谱系四篇(01 SBTPN/02 PNULock/03 UAF/04 SegLock)��外的历史缺环,正在建对应 teardown(`15_DEADLOCK_JOS2021.md`) |

## 曾误判为缺口、核实后排除的两项(记录避免以后重复排查)

1. **Ground Truth论文**——曾以为不在 `papers_lu/` 需要补,实际早已入库为 `Sommers-2025-ProcessScience.pdf` 并完整拆解(`teardown-bridge-20260904/12_SOMMERS.md`+`12b_..._kg_critique.md`),只是文件命名用作者名而非"GroundTruth"字面导致按名搜索漏判。
2. **Fragility/ScienceFlow/AutoDesign三篇**——曾以为是EdgeIM相关缺口,实际是完全无关的另一条harness工程P窗队列(TODO.md),PDF早已存在于`research/map/surveys/pdfs/`,与本任务无关。

--- completion footer: 2026-09-08 · 用户主任务窗口 · R线新增5篇(暂存)+ 鲁侧1篇新拉取(已入顶层)+ 1篇鲁侧仍缺 + 2项误判缺口已排除
