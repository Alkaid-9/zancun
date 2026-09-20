# R1–R6 本人证据库存（2026-09-20）

状态：`ORIGINAL-SOURCE-RECONCILED / USER-ACTION-OPEN / NO-PASS-DECISION`。

本次已把 zancun 快照与原课程事实源 `/mnt/d/myresearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1`、原仓非 sealed 状态记录及 `_scratch/seg0/` 对账。没有读取 `_sealed`、answer key、examiner、holdout/reference/retest 或正式口试正文，也没有扫描 `09_外部参考项目深度调研`。`SUBMISSION-MISSING` 只表示指定交付物未找到，不表示课程没做过、用户没有能力或必须重做已有练习。

| 项 | 库存裁定 | 证据与边界 |
|---|---|---|
| R1 EX-01 G0 五问 note | `PARTIAL-USER-WIP-FOUND / REQUIRED-SUBMISSION-MISSING / EXPOSURE-RECORDED` | 原仓精确搜索仍未找到 `G0_user_paper_note.md`。但 [EX-01 作答](../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-01/answer_EX_01.md) 已有三组 DFG 表、任务 4 回答和三条读前预测，不能写成“EX-01 什么都没做”。[A2 草稿](99_其他相关计划与状态/其他/原MAS课程源补充_只读证据/A2_edgeim_paper_note_draft.md)明确署名 `Owner: A2 agent (SOL)`、状态 `USER-MUST-READ`；[复用台账](99_其他相关计划与状态/其他/原MAS课程源补充_只读证据/REUSE_LEDGER_20260903.md)又把它限定为“只作定位底稿”，所以不是本人 G0。正式五问仍以 [EX-01 README §5](../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-01/README.md#5-g0-note你写_scratchseg0g0_user_paper_notemd)为准；第 3 问已有 Sol 提示，只能记来源核实。 |
| R2 C00 | `SUBMISSION-MISSING / EXPOSURE-UNKNOWN` | 原课程源确认受控卡文件存在；[CONNECTIONS](../02_四论文Ownership主线/01_EdgeIM/学习与课程/CONNECTIONS.md)只是公开索引，EX-00 非 sealed 作答无 `CONNECT/C00` 提交。遵守禁读边界，不用打开密封卡来猜用户是否看过。 |
| R2 C01 | `SUBMISSION-MISSING / EXPOSURE-UNKNOWN` | 索引只登记主题；EX-01 非 sealed 作答无 `CONNECT/C01` 提交。 |
| R2 C05a | `SUBMISSION-MISSING / EXPOSURE-UNKNOWN` | 索引只登记主题；EX-05a 非 sealed 作答无 `CONNECT/C05a` 提交。 |
| R2 C02 | `SUBMISSION-MISSING / EXPOSURE-UNKNOWN` | 索引只登记主题；EX-02 非 sealed 作答无 `CONNECT/C02` 标识；正文普通“连接”措辞不算卡片提交。 |
| R3 sigRank L-S1 一页对照 | `SUBMISSION-MISSING / EXPOSURE-RECORDED / UNLOCK-UNKNOWN` | 正式输出要求见[四论文训练 L-S1](../02_四论文Ownership主线/01_EdgeIM/学习与课程/FOUR_PAPER_TRAINING_LOOP.md#l-s1sigrank-第一次开镜selection-philosophy)。原仓 `learning/一些讨论.md` 已出现完整 coverage/importance、内生样本量/固定比例等助手叙述，故不能当未见材料；仍未找到本人一页对照。L-S1 要求 EX-01 PASS，本轮不裁该前置是否满足。 |
| R4 EX-02 `SR-__` | `SUBSTANTIVE-WIP-FOUND / TEMPLATE-ONLY-FOR-SR` | 原仓 [EX-02 作答](../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-02/ans.md)和 `answer.py` 有手切、PM4Py/IMf 与阈值分岔过程；09-12 checkpoint 还记录脚本退出码 0。但 [Research Note 模板](../02_四论文Ownership主线/01_EdgeIM/学习与课程/RESEARCH_NOTE_TEMPLATE.md#system-reading)仍只有 `DEMO-SR-01` 和空白 `SR-__`，未找到指定 system-reading 记录。可复跑 WIP 不自动等于 SR 已交。 |
| R4 EX-03 `EC-__` | `SUBSTANTIVE-WIP-FOUND / TEMPLATE-ONLY-FOR-EC` | 原仓 [EX-03 作答](../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-03/answ-ex03.md)含反例、上界和频次塌平练习，也混有 AI 纠正；未找到带具体 ID、竞争解释、区分证据与裁定状态的 `EC-*` 记录。模板仍是空白 `EC-__`，不能把长对话自动改签为 evidence closure。 |
| R5 已学站全文回接句 | `LEARNING-WIP-FOUND / DESIGNATED-RECONNECT-MISSING` | 原仓存在 EX-00、EX-01、EX-05a、EX-02、EX-03 以及 EX-05/EX-06 的学习 WIP；并非空白课程。但定向搜索仍未找到 `MASTERY_GATE` 要求的“它怎样改变我对整篇 EdgeIM 的理解”可定位句。EX-05 是否完成仍 `UNKNOWN`，不在本轮推断。 |
| R6 rubric | `PUBLIC-ASSET-EXISTS / NOT-FROZEN` | [ownership-v3 状态表](../02_四论文Ownership主线/00_共享合同_计划_验收/学习与课程/ownership-v3/BUILD_STATUS.md)明确 rubric `NOT-FROZEN`；当前仓只含公开快照，历史 QA 未在本仓重放。 |
| R6 验收记录 | `WIP-CHECKPOINT-EXISTS / SCOPED-RUNTIME-PASS / CURRENT-INTEGRATED-REVIEW-MISSING` | 原仓 09-12 checkpoint 明确保存 EX-02/03 与 EX-05a WIP，并真实记录 EX-02、EX-05a 两个脚本退出码 0；同一记录也明确 `EX-03 USER-REPORTED / NOT PASS`、15 题未执行、不得写 Ledger。另有 [EX-00 v0 批改](../02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-00/_v0_sol/GRADING.md) 的历史 `NOT PASS YET`。因此“代码可跑”是 scoped runtime evidence，不是当前综合 PASS。 |
| R6 Ledger | `FILE-EXISTS / EDGEIM-PASS-ROW-MISSING` | [训练能力账本](../08_科研方法与长期成长材料/通用学习基础/学习与课程/training/LEDGER.md)只有“尚未开始”占位和 ra26/ra28 降级记录；没有当前 EdgeIM 正式 PASS 行。不得倒填。 |

## 搜索与复核说明

- 原课程源共核到 131 个文件；密封文件只确认路径存在，未打开正文。
- 精确文件搜索：`G0_user_paper_note.md` 未命中；另找到署名 SOL 的 A2 草稿，但来源台账明确禁止把它当本人 G0。两份来源件已按原哈希复制到[只读证据区](99_其他相关计划与状态/其他/原MAS课程源补充_只读证据/README.md)，与学习者证据隔离。
- 对 EX-00/01/05a/02 等非 sealed 作答定向搜索 `CONNECT/C00/C01/C05a/C02`、具体 `SR-*`、`EC-*` 与全文回接句，未命中指定提交；同时确认 EX-01/02/03、EX-05a/05/06 存在实质 WIP 和代码，不再使用“课程没做过”的暗示。
- 主线程抽查了 EX-01 五问题面与部分作答、A2 来源边界、EX-02/03 作答、EX-05a/05 代码、09-12 checkpoint、L-S1 暴露材料、Research Note 空模板、EX-00 历史批改、ownership-v3 状态表和 Ledger。
- 一个只读子代理先做库存，主线程沿出处抽查；子代理没有修改文件或读取 sealed。

## 当前最小恢复动作

R1 是六项恢复包中下一份缺失交付，不是要求从 EX-01 重新学起，也不撤销 EX-01/02/03、EX-05a/05 的既有 WIP：

1. 若用户在仓外已有 G0 note，只提供路径或粘贴本人原稿，不重写；
2. 若确实没有，只补 EX-01 README §5 的五问与来源标签，不重做已经存在的三张 DFG 表和任务 5 预测；第 3 问显式记 `EXPOSURE: Sol hint`，回 PDF 核原句和页码；
3. AI 只可澄清术语、核路径和按既定 rubric 批改，不代写五问；
4. R1 落盘并完成验收后，再判断 C01/L-S1 的真实解锁状态。

R2 的受控卡正文已确认存在于原课程源，但本次未读取；后续只能在满足公开前置后按授权入口释放，不得根据索引补造。R3 已有助手内容暴露，需用户关闭材料后以自己的表述完成。R4/R5 应把既有 WIP 迁移成最小指定记录，不重写整站。用户已明确当前尚未学完、做完；邮件、一页纸、简历和发送流程全部冻结，不与学习恢复并行推进。
