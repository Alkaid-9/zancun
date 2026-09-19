---
date: 2026-08-24
type: mock-interview-question-set
stage: E2
title: 技术深挖压力场题库（鲁老师接轨）
status: ready_for_user_run
---

# E2 技术深挖压力场

本题库用于一次约 60 分钟的技术压力演练。考官从题目中抽问并可追问；面试者可以查证，但必须先区分“我记得”“正本写了”“我还不知道”。

## 题目

### E2-01｜SBTPN 的 AND/OR 与协同弧

**问题**：为什么普通 BN 难以直接表达 AND 结构？SBTPN 如何处理？协同弧 S 在这里是什么，不能把它说成什么？

**主证据**：`01_SBTPN.md` §1、§2.1；`05_FAMILY_SYNTHESIS.md` §一。

**合格要点**：AND/OR 关系、PN 变迁进入 BN、协同弧催化/抑制含义；协同弧不是普通因果弧，也不能凭此声称因果发现已被证明。

### E2-02｜式 (6)–(8) 的角色而非背数字

**问题**：请说明式 (6)–(8) 在概率 RCA 管线中各自承担的功能，以及候选为何还要经过路径过滤。

**主证据**：`01_SBTPN.md` §2.2–§2.4；`teaching/EXAMINER_SOP.md` Gate 1；`repro/sbpn/README.md` §2。

**合格要点**：按公式层的联合/条件概率修正与排序作用作解释；不能把可复算公式层误说成 benchmark 或真实根因验证。

### E2-03｜η 阈值与噪声前提

**问题**：η1/η2 在方法中起什么作用？如果数据噪声前提不满足，结论会怎样变化？

**主证据**：`01_SBTPN.md` §2；`teaching/EXAMINER_SOP.md` Gate 1；`05_FAMILY_SYNTHESIS.md` §一。

**合格要点**：说明阈值敏感性和噪声条件；不把记忆中的数值当作未经查证的定理常数。

### E2-04｜PNULock 的信息丢失与定理 1

**问题**：PNULock 试图修复哪些传统锁模型的信息丢失？定理 1 为什么既能产生潜在交错，又不能保证每个交错真实可执行？

**主证据**：`02_DEADLOCK_PNULOCK.md` §1、§2.1；`teaching/EXAMINER_SOP.md` Gate 2。

**合格要点**：区分循环内同一锁不同轮次、冲突/并发结构；明确“蕴含更多潜在交错”与“不必然可执行”同时成立。

### E2-05｜确定性重演与 recover

**问题**：从展开得到死标记后，recover、δ 映射和三分重演怎样串起来？哪里最容易把未知说成确定？

**主证据**：`02_DEADLOCK_PNULOCK.md` §2.2–§2.4；`teaching/EXAMINER_SOP.md` Gate 2。

**合格要点**：能描述候选配置→伴随/恢复→调度映射→真死锁判定；承认跨运行映射、通信死锁和不可执行交错是边界。

### E2-06｜PNULock 与 SegLock 的方法差异

**问题**：SegLock 相比 PNULock 换掉了什么、保留了什么？为什么“更快”不能只凭 Table 5 口述？

**主证据**：`04_DEADLOCKSEG_SEGLOCK.md` §1–§2、§6；`05_FAMILY_SYNTHESIS.md` §一；`_audit_remediation_20260824/A4_pdf_verification.md` §核点 1–2。

**合格要点**：图方法与 PN 展开的差别、历史锁/序增强因果；说明 Table 5 错位与 Table 6 口径问题，内存数字缺失。

### E2-07｜UAF 分段 PN 的迁移价值

**问题**：UAF 论文的段集、段映射 λ、伴随标签 α/β 分别解决什么问题？它和死锁线的可迁移边界是什么？

**主证据**：`03_UAF_PN_VFG.md` §2.2–§2.3；`05_FAMILY_SYNTHESIS.md` §一、§二。

**合格要点**：说清静态中间代码、控制流/值流/并发约束；迁移只能先作为设计类比，不声称 UAF 结果直接验证 bridge。

### E2-08｜独立取证方法论

**问题**：请从原始 PDF 到 A4 结论重述一次证据链，并指出哪一步能排除“你自己抄错”。

**主证据**：`_audit_remediation_20260824/A4_pdf_verification.md` §核点 1–3；`04_DEADLOCKSEG_SEGLOCK.md` §0。

**合格要点**：原 PDF 双路提取/视觉核验、同名基准逐项对照、脚本或 hash 复核、声明残余不确定性。

### E2-09｜SBPN 复现级别审问

**问题**：当前 SBPN route replay 的“通过”具体证明了什么？为什么不能升级到 L3？

**主证据**：`repro/sbpn/README.md` §口径声明；`_codex_20260824/c_repro/REPORT.md`；`_codex_20260824/c_repro_l3/agent_c/report.md`（如存在）。

**合格要点**：区分公式/局部逻辑、官方 synthetic route replay、benchmark truth/baseline 缺失；明确 L1/L2 与 L3 的边界。

### E2-10｜Bridge-0 六维语义契约

**问题**：D2 反例进入 D1 概率变量前，至少要检查哪六类语义？请给出一个“命中率不变但语义已丢失”的例子。

**主证据**：`bridge/D1D2_closure_bridge.md` §1–§2；`_codex_20260824/bridge0/agent_b/semantic_map.tsv`；`counterexample_suite.md`。

**合格要点**：事件身份、窗口/时间、资源关系、偏序/并发、聚合信息损失、不确定性/出处；例如合并不同轮次事件后 top-1 不变但无法回溯根因。

### E2-11｜Prop 2 的冻结协议

**问题**：按 G0，Prop 2 的候选数、k、样本量、主指标、失败分母和通过条件分别是什么？为什么崩溃不能删出分母？

**主证据**：`bridge/D1D2_closure_bridge.md` §2 命题 2；`CODEX_ACCEPTANCE_BRIEF_20260824.md` B 段；`progress/decisions/2026-08-24__research__evidence-passport-bridge-route-v2-execution.md`。

**合格要点**：C=6、k=3、N=100、top-1-any/top-3-joint、完整分母、Wilson 与 paired bootstrap、相对两基线 5pp 且区间下界>0；删除失败场景会造成选择偏差。

### E2-12｜Prop 3 的降级与未知压力

**问题（未知/越界压力题）**：Prop 3 目前能否说“已验证”？如果对方追问真实 MAS 映射覆盖率和 terminal-state 一致率，你没有数据时怎么回答？

**合格回答**：明确 `DESIGN_HYPOTHESIS_ONLY`；说出尚缺数据和未来预注册候选门槛，给出查证/补数路径，不编数字。

**主证据**：`bridge/D1D2_closure_bridge.md` §2 命题 3；`ONBOARDING_PREP_PACK_20260824.md` §三、§六。

### E2-13｜开放研究判断

**问题**：如果 Bridge-0 发现窗口聚合导致严重语义丢失，你会保留、改造还是终止 Bridge-1？请给出停止规则。

**主证据**：`bridge/D1D2_closure_bridge.md` §1–§3；`_codex_20260824/bridge0/BRIDGE0_NEXT_EXPERIMENT_BRIEF.md`；`evidence_passport_v2.md`。

**合格要点**：按预设 kill criteria 停止或降级为串联管道；不能为了保住主张临时改阈值。

## E2 必考红线

至少抽 E2-12；建议抽 E2-06、E2-09。任何把公式层复算、route replay 或设计假说说成完整论文复现/机制验证的回答，记为 X 级泄漏并触发复盘。
