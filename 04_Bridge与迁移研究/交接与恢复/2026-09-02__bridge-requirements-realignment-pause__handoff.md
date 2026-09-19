# Bridge→鲁组 · 需求重对齐暂停交接

**Date**: 2026-09-02 21:48 Asia/Taipei
**Task**: `TASK-20260830-004`
**Type**: pause handoff（用户三声"先存档"止损）
**Status**: `ARCHIVED / RECOVERABLE / REQUIREMENTS-RESTATED / SLICE-PROPOSED-UNAPPROVED / NO-EXECUTION-AUTHORITY / FABLE-LABELED / SOL-SEPARATE`
**Window / author marker**: `FABLE`（Claude Code 主窗，claude-fable-5）。用户 09-02 22:2x 明示：与隔壁 `SOL`（Codex 独立审查窗）区分、标注 fable、不覆盖别的档。
**Parallel archive**: `2026-09-02__bridge-requirements-realignment__sol-review-pause-handoff.md`（SOL 22:10，本窗只读不改；其审查意见已作为外部输入登记到 09-02 决策检查点 §12）
**Write owner**: Claude Code 主窗 = FABLE
**Supersedes as recovery entry**: `2026-08-31__bridge-current-state-and-reference-assets__handoff.md`（其六节总纲/材料/资产状态仍有效；其 §9 "恢复后从 M1 逐字段设计"游标被本档 §3 取代）

## 0. 一句话

用户 09-02 重审目标，撤回 T4/T3-lite 进入本周期，重述八条目标条件；主控提出 EdgeIM 复现 + 覆盖采样噪声窄实验作为切片；**四项拍板全部待用户**；本轮零执行、零代码、零安装，未 commit。

## 1. 本轮新增/修改文件

| 文件 | 性质 |
|---|---|
| `progress/decisions/2026-09-02__research__bridge-requirements-realignment-and-edgeim-slice-proposal.md` | **主档**：六层收缩链、H1–H10、用户七答与八条、推敲、切片提案、时间盒草案、横向对比、待拍板 |
| `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-02__bridge-direction-provenance__scratch.md` | 草稿纸 1（还原与推敲的思考路线） |
| `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-02__bridge-redesign-edgeim__scratch.md` | 草稿纸 2（重设计的思考路线） |
| 本档 | 暂停交接 |
| `BRIDGE_LU_PLANNING_LOG.md` | 胶囊更新至 09-02 21:48；追加 C-037；追加 preflight |
| `progress/task_logs/2026/08/2026-08-30__research__bridge-lu-two-week-masterplan-alignment.md` | 追加 09-02 amendment |
| `progress/handoff/INDEX.md` | 顶部插入本档路由一行 |
| `/mnt/d/MyResearch/CROSSWINDOW.md` | TASK-004 行状态由"⏸ 08-30 暂停"改为 09-02 存档态 |

**22:2x 追加（FABLE 标注轮）**：上表各 FABLE 文件加 `FABLE` 窗标；决策检查点新增 §12（SOL 输入登记 + FABLE 回应）与 §9 第 5 项；规划日志追加 C-038；TASK-004 amendment 与 CROSSWINDOW 行各补一条；handoff/INDEX 为 SOL 档补一条路由（标 SOL 作者，仅指针）。**未改任何 SOL 文件**；未改文件名（SOL 档 §1 按现名引用本窗文件，改名会断其引用）。

| 并行档（非本窗，只读） | 性质 |
|---|---|
| `progress/handoff/2026-09-02__bridge-requirements-realignment__sol-review-pause-handoff.md` | SOL 独立审查暂停交接（22:10）：三处偏差、最近邻更新（sigRank/CrossEdgeIM/IMi）、合成 ground truth、五个未下载新源、v2 `EvoAgent A-min + T2 replication-plus` 建议 |
| `progress/handoff/2026-09-02__bridge-scheme-evaluation-framework__sol-pause-handoff.md` | SOL 评估框架暂停交接（22:33）：五门八维评估框架、工作量预算 80–108h、七条否决信号；唯一待答="T2 vs A-min 优先级"→ 用户后续选 A |
| `progress/handoff/2026-09-02__bridge-t2-priority-and-research-object__sol-pause-handoff.md` | SOL T2 优先级+研究对象暂停交接（23:05）：**用户已选 A（T2 受保护、A-min 可降级）**；R1 采样机制审计 / R2 全链复做 / R3 agent trace conformance 三选一待答；精化实验设计（统一下游发现器、操作化研究问题、四层指标、噪声六分类、三级裁定、所有权六能力） |

未触碰：第一、二节冻结档、技术检查点、材料/中央研究回执、`repro/edgeim/`、EvoAgent、任何代码。

## 2. 新窗口读取顺序

1. 本档 §0、§3、§4；
2. 09-02 决策检查点 §4（用户输入）、§6（提案）、§9（待拍板，五项）、**§12（SOL 输入与 FABLE 回应）**；
2a. SOL 档 §3（审查裁决）、§4.2（新源，未下载）、§5（设计要求）——只读；
3. 规划日志胶囊 + C-037 + C-038；
4. 需要旧盘面时读 08-31 交接档；需要 EdgeIM 事实时读 `07_EDGEIM.md` §0/§1/§5.6/§6 与 `repro/edgeim/README.md`（**注意 §4 封存提议**）。

## 3. 当前游标与恢复后第一动作

```text
R1 总纲设计
→ 第一节：已冻结，但用户 09-02 八条构成候选重述（时间盒改为"九月中下旬质量检查点"、轴改为"T2 做深做实"）——是否正式修订第一节，待用户
→ 第三节：工作底稿 ASYMMETRIC-SINGLE-SPINE 仍是盘面权威；09-02 提案拟 supersede 其 T4/T3-lite 部分，待用户
→ 恢复后唯一第一动作：请用户对 09-02 检查点 §9 五项逐一拍板（切片 / 移出项 / toy 处置〔封存 vs SOL 建议"披露先验的代码隔离"〕/ supersede / 是否以 SOL v2 结构为下一轮底稿），并给检查点日期（09-20 vs SOL 建议 09-20 冻结+09-25 包检）、EvoAgent 处置（只写账本 vs A-min 12–16h 可裁项）、仓库名三个一句话
→ 用户已在 SOL 窗选 A（T2 受保护主产物、A-min 可降级至 8–12h）——待本窗确认该决策也在此生效
→ SOL 推荐 R1 EdgeIM 采样机制审计（vs R2 全链复做 / R3 agent trace），FABLE 支持 R1——待用户拍板
→ 获批后：写 v2 检查点（新文件，不覆盖 FABLE/SOL 任一档），M1 重写为 T2 基础切片字段；再排第五节时间盒；仍不进入实现
```

C-028（旧 L1 卡复用）继续后置；RC1 对 255 条的核销按提案移出本周期，但在用户批准前其"研究处理关闭机制"地位不变。

## 4. 待用户拍板（复制自决策档 §9）

1. 切片 = EdgeIM 复现 + 覆盖采样噪声反转实验（备选：时间戳粒度悖论）？（SOL 建议：退回改写为"T2 基础切片 + 有边界 clean-room 重实现 + 薄 PN/alignment 手算层"；FABLE 接受此改写方向）
2. 从本周期移出 T4、T3-lite、RC1 255 条核销、Evidence Contract typed relation？（SOL：部分接受，保留最小数据合同；FABLE 接受）
3. `repro/edgeim/` AI toy 封存（用户 L1 完成前不看、主控不引用）？（SOL：改为"披露先验的代码隔离"；FABLE 接受）
4. 以 09-02 检查点 supersede 第三节底稿的 T4/T3-lite 部分？（SOL：暂不落盘；FABLE 同意等 1–3 定后再写 v2）
5. 是否以 SOL v2 `EvoAgent A-min + T2 独立公开仓` 为下一轮讨论底稿？（FABLE：A-min 作独立可裁时间盒；"架构 A"出处 [需验证]）

另需一句话：检查点日期（暂 09-20；SOL 建议 09-20 冻结 / 09-25 包检）；EvoAgent 本周期只写贡献账本还是加 A-min？；公开仓库名。

## 5. 未决与待查新

- EdgeIM 官方代码：SOL 09-02 联网有界查找**未发现**同名公开仓库（非不存在证明）；FABLE 本窗网搜 429 未复核。SOL 另核出 sigRank（TSC 2026）/ CrossEdgeIM（IoT Mag 2026）/ Sommers ground-truth（Process Science 2025）等五源，**未下载**，DOI 待 FABLE 侧复核 [需验证]。
- SOL 所称用户先前的 EvoAgent"架构 A"选择：FABLE 未在 08-30 技术检查点检索到该字样，出处待核 [需验证]。
- 开学后实际日容量（用户口径 6–8h，未按课表验证）。
- 用户是否接受"在老师论文的已识别弱点上做实验"的姿态。
- 进组卡 `jinzu-sprint.md`（08-22 游标、OE1 08-25 死线未销）与 CLAUDE.md 09-10 硬日期均已过时，未回写（非本任务写域，另待口令）。

## 6. 未授权边界

不运行分类/L1/T0/T1；不安装、clone、运行第三方仓库；不写代码、不建公开仓、不启动实验；不改已冻结第一、二节正文；不 staged/commit/push。

## 7. 本档验收

| 项 | 结果 |
|---|---|
| 用户输入逐条落盘（七答 + 八条 + 方案 B 原话） | PASS（决策档 §4） |
| 提案与拍板状态分离，无一项写成已批 | PASS |
| 思考路线留档（用户 09-02 要求） | PASS（两份草稿纸） |
| 恢复顺序与第一动作明确 | PASS |
| 零执行、零 commit | PASS |
