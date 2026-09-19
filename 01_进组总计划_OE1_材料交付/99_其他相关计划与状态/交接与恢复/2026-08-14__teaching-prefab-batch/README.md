# 教学包预制批(2026-08-14 凌晨)— 存档八件套入口

> **窗口**:P批 教学包预制批(开窗口令"按 PLAYBOOK 开教学包预制批",02:08)
> **性质**:P 窗④教学段的**预制**(出考卷/判分卷/主考 SOP),不是教学本身
> **终态**:预制 6/6 完成并验收 PASS;**④正式教学 0/7,全部 TEACHING-AWAITING-USER,等用户本人在场**
> **存档时刻**:2026-08-14 02:5x(用户存档令 02:50,原话要点:工作总结/日志/已完成未完成/进度/交接/归线/架构分工/plan/使用维护手册,全部落盘可溯源)

## 本目录八件怎么读

| 文件 | 回答什么 | 什么时候读 |
|---|---|---|
| `README.md` | 入口与地图 | 任何新窗口第一读 |
| `WINDOW_SUMMARY.md` | 工作总结:任务来源(口令原文)、归属线、决策记录、验收结论 | 想知道"这窗干了什么、为什么这么干" |
| `WORKLOG.md` | 逐时刻日志:02:08–02:5x 全动作,含六个分工 Agent 编号与交卷时刻 | 追根溯源、对账 |
| `HANDOFF.md` | 交接:已完成/未完成清单、目前进度、接续第一动作表 | **续窗第二读** |
| `NEXT_PLAN.md` | 接下来的计划:教学执行顺序建议、前置检查、与队列衔接 | 用户回来准备开考时 |
| `ARCHITECTURE.md` | 设计与架构方案:教学包五件套结构、信息隔离、四关状态机、八要素覆盖机制、六 Agent 分工方案与 prompt 骨架 | 想复制这套打法给其他论文 |
| `USER_GUIDE.md` | 使用手册:用户怎么开一场考试(口令/流程/时间预算/中断恢复) | 开考前 |
| `MAINTENANCE.md` | 维护手册:单一事实源链、更新触发器、机械验证命令、遗留项台账 L1–L5 | 拆解文档更新/月查时 |
| `ASSESSMENT.md` | 需求深挖/验收复盘(证据强度三档)/改进空间 P0–P2 与自我批评(03:0x 补) | 首考前后、月查、复制打法前 |
| `EXECUTION_PLAN.md` | 改进项的可发射计划:Wave A 交叉审(3 Agent 分工+DoD)/B 首考校准/C 轻考拍板/D 台账清尾,含触发口令与回退(03:0x 补) | 明天回来第一动作参照 |
| `ROADMAP.md` | 长远方向储备(03:4x 补):运营四原则 R1-R4 即刻生效(预制库存上限/考试通胀禁令/天花板意识/已考优先引用)+ 教学/流水线/资产/工具四层 15 项带触发条件 + 不做清单;启用须用户点头 | 月查、某触发条件满足时 |

### 2026-08-18 验收复核增量

| 文件 | 主题 | 结论 |
|---|---|---|
| [ACCEPTANCE_REPORT_2026-08-18.md](ACCEPTANCE_REPORT_2026-08-18.md) | **P批教学包预制、交叉审、P0/P1/P2 修订与存档终态验收复核** | `PARTIAL PASS`:六包考前质量门通过;汇总账/CROSSWINDOW 未通过;正式教学、INDEX、待核项未验收 |

### 2026-08-21 整改收口增量(TASK-20260821-001)

| 文件 | 主题 | 结论 |
|---|---|---|
| [REMEDIATION_LOG_2026-08-21.md](REMEDIATION_LOG_2026-08-21.md) | **ACC-01~04 整改落盘 + 全量重排执行日志**(逐处 file:line 对照) | 账目统一 17/17、P1×6/P2×11、16+1、6 份报告;CROSSWINDOW 04:48 行勘误销行;W2 INDEX/W5 排期卡/W6 规则完成;W3 待核与 W4 commit 见日志 §六 |
| [PENDING_VERIFICATION_TRIAGE_20260822.md](PENDING_VERIFICATION_TRIAGE_20260822.md) | **六包"待核"枚举三分类 + 在线裁决终态**(基线 60→盘面 47+2 对账;§七.A 执行表) | L8/O17/B10/C12;裁决=即解/留档/设计保留三类路由;鲁组 7 点位全决(含 SBTPN 符号错 μ/η 发现) |
| [RESOLUTION_RECEIPTS_20260822.md](RESOLUTION_RECEIPTS_20260822.md) | **五路裁决回执全文存档**(铁律 1 证据链) | INTIMA 4/4、AgentSpec+Anchor 5/5、FoldA 6/6、ProbGuard 7 裁决、鲁组主窗自查;重大发现:ICLR 2026 Poster、380=368+memory×12、P/R 标签互换、监控自动机前提证伪 |
| `verify_remediation.sh` | 可重跑断言脚本(A1/A1'/A2/A3/A5/A5'/A6 七组) | **exit 0**(2026-08-21 23:59:19;08-22 02:21 复跑仍绿);PLAYBOOK §四.1"机器计数"纪律的示范实现 |

## 六个教学包落点(本窗核心产出,每包 5 件)

| # | 论文/联卷 | teaching/ 绝对路径 |
|---|---|---|
| 1 | ProbGuard(ASE 2026) | `/mnt/d/MyResearch/MAS_Safety_Project/research/sun/phase1/papers/ASE2026_ProbGuard/teaching/` |
| 2 | AgentSpec(ICSE 2026) | `/mnt/d/MyResearch/MAS_Safety_Project/research/sun/phase1/papers/ICSE2026_AgentSpec/teaching/` |
| 3 | FoldA(偏序对齐,T2 竞对内核) | `/mnt/d/MyResearch/MAS_Safety_Project/research/sun/phase1/papers/FoldA_partial_order_alignment/teaching/` |
| 4 | 鲁组 PN 四篇联卷(SBTPN/PNULock/UAF/SegLock) | `/mnt/d/MyResearch/MAS_Safety_Project/research/papers_lu/teardown-joint-20260813/teaching/` |
| 5 | INTIMA(T5 谓词原料) | `/mnt/d/MyResearch/casual/companion-survey/14_academic/teardowns/INTIMA/teaching/` |
| 6 | Anchor(长时程人格/记忆审计) | `/mnt/d/MyResearch/casual/companion-survey/14_academic/teardowns/Anchor/teaching/` |

每包 5 件 = 三件套(`FINAL_ORAL.md` + `learner_workbook.md` + `answer_key.md`)+ `EXAMINER_SOP.md` + `mistakes.md`(错题四步闭环模板)。范式母版 = `casual/companion-survey/14_academic/teardowns/EmoAgent/teaching/`(LP-07 产物,第 7 个待教学包)。

## 一句话现状(05:0x 三刷时点)

六包预制+验收+**交叉审 6/6 全过+P0/P1/P2 三级发现全部清零**(P0×2 修复复验、P1/P2 17/17 处置〔16 修+1 备案;08-21 勘误原记 14/14〕,记录在各包 `_audit/` 报告尾部回填);轻考模式已落地(FoldA/Anchor 各有 `teaching/LIGHT_MODE.md`,约 1h/包);**AI 侧零剩余任务,卷面终态就绪**。下一步唯一需要用户的硬动作 = 在场开考,首选鲁组联卷 Gate 1(口令模板见 `USER_GUIDE.md` §一,建议同时启用 `EXECUTION_PLAN.md` Wave B 校准记录)。
