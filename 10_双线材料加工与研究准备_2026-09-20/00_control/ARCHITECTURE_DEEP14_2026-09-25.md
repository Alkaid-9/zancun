# Deep14 归档架构、数据流与职责（暂停时快照）

**状态：DESIGN-RECORDED / IMPLEMENTATION-PAUSED。** 它说明本窗口实际采用及后续建议的边界，不意味着这些组件已实现。设计源：`01_两天执行合同.md:9-30,32-65,90-131`、`02_逐篇施工与专项验收.md:5-20`、`07_第二轮研究动态_三论文拆解与JINZU应用计划.md:71-95`；修改范围以 `DEEP14_SCOPE_2026-09-25.md` 和用户最新“停一下”为准。旧两天 D1/D2 日期已过，不用它们驱动当前排程。

## 1. 目标、非目标、数据流

目标是 14 篇**逐篇独立、可追溯、能被否证**的深入论文资产，而非十四份自动生成的综述。原 11 篇与 3 篇第二轮原件保留不同来源池；只有原件可界定论文主张，旧稿只能提供导航/待核差分。

```text
用户范围决策（全部14篇深拆）
    ↓ 逐篇索引（TASKS.tsv 唯一当前状态权威；PAPER_POOL.tsv 仅输入工作池）
原件PDF＋旧稿路径＋SHA／版本 → 主控固定任务ID、唯一问题、输入快照
    ↓                                  ├── 只读 worker：局部主张/符号/反例候选
    ↓                                  └── 失败：保留任务/源/错误，不自升状态
主控打开原PDF回源 → 身份与主张表 → 机制/条件 → 主动反例/强简单baseline
    ↓                                         ├── 无计算：独立手推＋明确无运行项
    ├── 独立复核（替换worker槽）                └── 有计算：另行授权后独立oracle＋真实run
    ↓
每篇 B/papers/<id>/ACCEPTANCE.md（接收范围、拒绝、UNKNOWN、NOT_RUN、下一门）
    ↓    仅已接收的字段可供 research/比较、未来教学转换；不能跨线写本人 PASS
交接索引/manifest/任务状态；不能以manifest自证内容正确
```

当前实际落盘：控制基线和任务表、失败回执、**仅 ContrAgent 一篇 PARTIAL** 来源包；流程中未落盘的包不得当作存在。没有新代码/真实运行/跨论文综合/研究 toy。

## 2. 目录、仓库与权限

| 边界 | 用途 | 可写/只读 | 本窗口实例 |
|---|---|---|---|
| `/mnt/d/Alkaid/Desktop/zancun/10_双线材料加工与研究准备_2026-09-20/00_control/` | 决策、状态、输入哈希、失败、独立复核和交接 | 仅主控在获准执行或本次存档可写 | `TASKS.tsv`、`DEEP14_SCOPE...`、本交接 |
| 同包 `B/papers/<slug>/` | **逐篇**事实/机制/反例/验收 | 仅主控落盘；worker只回候选 | `contragent/` 存在，其余13篇不存在 |
| 同包 `A/` | 给本人下一学习块的课程辅助材料 | 此窗口冻结，不替用户写作答 | 历史 `A/D1/` 已备；A6/A7待真人回执 |
| 同包 `research/`、`runs/`、`tools/` | 已接收证据后的比较／实际运行／必要脚本 | 本窗口未启动 B 线运行；未来需逐项授权并保存原始证据 | 历史 `runs/D1-preflight-002/` 是 A 线 reviewer-only 运行；本窗口没有新 B 线 run / research toy / tools，不称已运行论文实验 |
| `/mnt/d/MyResearch/MAS_Safety_Project` | 原 EdgeIM 课程和研究事实源 | **只读**；不碰本人答卷、Ledger、sealed | 本窗口未回写 |
| `/mnt/d/Alkaid/Downloads/2609.*v1.pdf` | 新增三篇本地 PDF 版本 | 只读、按哈希冻结 | 三份哈希记录在 `R2_C0...` |
| LearnGraph 服务器、账户、CPA、Gemini 配置、旧外联材料 | 当前窗口之外的其它工作 | **禁止本窗口操作** | 未接触 |

`00_先看这里.md` 根索引及包内 `00_START_HERE.md` 原有 D1/D2 日期均属历史措辞；本次仅在两个入口各加**一条暂停交接指针**，不借存档大改计划。旧六项 dirty 文件的所属窗口不由本窗口接管或撤销。

## 3. 模型、并发、隔离与归属

- 主控 M=唯一写入、任务状态修改、事实回源与验收；子代理只读、固定一个来源/一个问题、`fork_turns="none"`、不覆盖模型/角色/推理强度、不派生代理、一次终态。当前环境子代理实际固定为 `gpt-5.6-sol / xhigh`，与用户提出的 `gpt-6-sol / xhigh` 不同；**不得在回执里填后者**。
- 旧两天合同的峰值上限：主控1、Claude只读worker≤3、Gemini≤4、worker总≤6、总≤7；并非生产能力保证。旧 AC00 单元格“≤2”和合同新修订有口径冲突，以最新明确的修订和实际新指令复核，不通过改数值获得验收。本窗口首波实派3，三者均失败后活动只剩主控；暂停后无存活worker。
- Gemini 专用入口历史为 `PRODUCTION HOLD`，未重试、未偷换成普通 Claude；Fable 教学只消费已接受的论文事实包，不代写用户答案。模型额度/真实花费在三次传输失败后 **UNKNOWN**，不编造 token 使用或账单。
- Agent 结果即使成功也仅是候选；同一模型/同家族复核不是独立原文或实验真值。独立 reviewer 占现有worker槽位，逐篇至少查身份、形式对象、关键数值/定理、失效条件和所有拟消费的 JINZU 主张。

## 4. 术语和状态的双轴合同

旧两天包 `P0=输入登记 / P1=原文机制片段 / P2=全文可复用论文包 / P3=作者结果复现`；第二轮 v2 管线 `P0=SOURCE / P1=MECHANISM / P2=FALSIFICATION / P3=EXECUTABLE / P4=TRANSFER / P5=RESEARCH`。**同名 P2 不同义**，任何新收据必须用两个显式字段，例如 `package_depth=SOURCE_REVIEW_PARTIAL` 与 `research_gate=FALSIFICATION_SPEC_ONLY`，不能孤立写“已P2”。

状态轴必须分开：`SOURCE_LOCAL`（身份/哈希）、`CLAIM_SOURCE_CHECKED`（一手原文定位）、`MECHANISM_RECONSTRUCTED`（假设/形式过程）、`FALSIFICATION_SPEC`（候选反例）、`COUNTEREXAMPLE_VALIDATED`（经独立核查）、`EXECUTABLE_NOT_RUN/RUN_EVIDENCED`（命令/日志）、`PEER_REVIEW_OPEN/PASS`、`USER_CAPABILITY_NOT_ASSESSED`。某轴变绿不能推动另一轴；未取得完整链条时整篇最多 `PARTIAL`。

## 5. 主要风险和防止产物污染

- **PDF抽取数学符号损失**：ContrAgent p.3 Eq.(1) 在文本层漏掉上划线；关键公式、表头、箭头/量词必须渲染页对照；无图像核查的数学结论限为待核。
- **来源与旧稿混淆**：`B/papers/contragent/DELTA.md` 已指出旧管线引入 `effect` 事件及“阻断无副作用”等未经原PDF支持的断言；先按 `CA-PDF` 再看 `CA-OLD`。
- **真实系统边界**：补论文机制不能推断已掌握、已复现、已验证 LearnGraph、已选题或已形成新颖方法；作者表格数字不等于本地实测。
- **共享工作区污染**：只给本任务新文件/精确现有 TASKS 行落盘；写前重读当前 status/hash；并行修改时停在 CONFLICT，不整仓回滚、不偷删旧草稿。

## 6. 文件归属、分工与验收交接

| 角色/边界 | 实际发生 | 恢复后拟负责（须获新指令） | 不可越界 |
|---|---|---|---|
| 用户 | 指定 14 篇深拆，随后下达暂停与存档要求 | 决定何时恢复、约束/并发、是否另许真实运行/外联 | 并未授权当前继续论文、重试或部署 |
| 主控 M | 锁定输入/派工记录、直接审核 CA PDF、独立存档、写 `TASKS.tsv` | 唯一写者；逐项确认原件、门禁、日志、`ACCEPTANCE.md`、任务行/归档 | 不把自己查过的主张标异构审核，不代写本人答案 |
| `deep_pnulock` / `deep_sbpn` / `deep_contragent` | 三个只读 Worker 传输失败，接受 0 个报告；其规格见 `DISPATCH_SPECS...` | 若恢复路由才可换成小节/单一定义的只读候选核验 | 无写权限、无审批权、无可归档研究产出 |
| 独立论文复核者（未投入） | `NOT_RUN` | 从原件挑战符号/关键数字/边界/反例；报告 PDF 页、证伪理由、未覆盖范围 | 不用同模型复述或作者实验当独立真值 |
| 学习者（A线） | 本窗口未做新个人回执 | 自行产生 R1/EX-05 预测/运行/解释等真实证据 | AI B线不得据论文包写本人 PASS/解锁 EX-06 |

实际文件映射：`00_control/` 存范围、失败、操作日志、计划和 manifest；`TASKS.tsv` 是状态仲裁；`B/papers/contragent/` 是唯一新 PARTIAL 论文包；其余 `B/papers/<slug>/` 目前是**拟建路径**。目录/职责到具体 14 篇的未来施工与关口详见 `NEXT_PLAN_DEEP14_2026-09-25.md`。存档验收为文件可定位＋只读哈希/TSV/JSON 检查；论文验收另靠各篇 `ACCEPTANCE.md` 和独立来源/运行证据，不能混成一个 PASS。模型额度/费用实际用量 UNKNOWN；已有三次 transport error 不能据此推算零花费。单篇冲突回滚仅限本窗口自有新增文件及精确状态行，不动原六项 dirty、原 MAS 仓或服务器。
