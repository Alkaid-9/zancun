# 独立红队事实审计 · AUDIT_FINDINGS.md

- **审计员**：Claude（本会话，独立执行，未继承前序 Agent 结论）
- **审计对象**：`09_外部参考项目深度调研/` 全目录（docs/、prototypes/、contracts/、receipts/、reports/、根级卷宗）
- **审计基准**：仓库当前工作树，`git log` HEAD = `ea91ab5`（分支 `main` 已含此提交；本审计产物落在独立分支 `audit/redteam-external-ref-2026-09-20`）
- **审计原则**：Sunk cost = 0；不因"文件写了 DONE/PASS/VERIFIED"而采信；只读不改；每条结论标注证据等级
- **执行方式**：本次审计由我本人直接执行（读文件、跑代码、查本地源码克隆、查 GitHub 上游），未委派子 Agent —— 这是刻意选择：审计的价值在于独立性，委派会重新引入"自证"风险。

---

## Evidence Status（总览）

- **VERIFIED**（有一手证据支持）：EdgeIM 真实身份、CrossEdgeIM 真实身份、Headroom 三机制源码锚点、LoopX 全部 8 处 file:line 引用、Prime-Agent repl.py 引用、harness 真实产物缺失、Outcome Floor 纯字符串校验、main 分支纪律违规、`RED_TEAM_AUDIT_REPORT.md` 同模型自审性质
- **PARTIALLY VERIFIED**：孙猛画像缺口（确认缺失，但未做外部重建——超出只读审计范围）
- **UNVERIFIED**：P02(SBTPN)/P03(PNULOCK) 及 03_ 谱系 7 篇论文的英文一句话 gloss 准确性（本轮未逐篇回源 PDF 核对）
- **CONTRADICTED**：P05–P10 六篇论文的存在性；"multi-agent parallel harness = 工业级验证"的宣称
- **NOT SEARCHED**：孙猛 2023–2026 论文/项目/学生题目的外部检索（只读审计不联网核实导师主页，且 01_ 轨道已声明"未联网刷新"）

---

## P0 · 事实污染 / Fabricated Evidence / Fake Validation

### P0-1：EdgeIM 本体被错误串成"并发 Bug / 死锁检测"论文，且未清理完

**症状**：`09_外部参考项目深度调研/` 内至少 9 个文件仍将 EdgeIM 描述为死锁/数据竞争检测机制，引入 `T_lock`、`M_wait`、"边图模型"、"锁依赖传递"等不存在的符号体系。

**原因**：前序 Agent（疑似 Gemini）把仓库里另一条论文脉络（`03_鲁组其他论文与研究谱系/` 中真实存在的死锁类论文：SBTPN/PNULOCK/UAF_PN_VFG/SEGLOCK/MHP/Deadlock_JOS2021）的"并发死锁"主题，串线嫁接到了 EdgeIM 这个特定论文名上。

**证据**：
- 真实身份（SOURCE FACT，PDF 一手核验）：`Su, Liu, Lu, Cheng, Zeng, Zhang. "EdgeIM: An Efficient Edge-based Process Model Discovery Technique". IEEE ICWS 2025, pp.404-410, DOI 10.1109/ICWS67624.2025.00057`。方法是流程挖掘（process mining）：Stage1 特征保持采样 → Stage2 边缘节点局部 DFG 构建（含时间戳冲突双向边处理）→ Stage3 中心聚合 + Inductive Miner 递归分解 → Petri 网发现。证据文件：`03_鲁组其他论文与研究谱系/99_其他论文与盘点/论文原文与拆解/teardown-joint-20260813/07_EDGEIM.md`（含逐条概念表、DOI、公式定义）。
- 污染文件清单（逐条定位）：
  1. `docs/USER_MANUAL.md:85` — `title="EdgeIM: Efficient Detection of Concurrency Bugs in Edge Computing"`，`:86` 摘要写"边图模型的并发死锁与数据竞争动态检测"
  2. `docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md:102` — `P01 | EdgeIM: Edge Concurrency Bug Detection`
  3. `prototypes/multi_agent_parallel_harness.py:196` — `title="解析 EdgeIM 边图模型与死锁定义"`
  4. `prototypes/minimal_openviking_kernel.py:304-307` — `content="EdgeIM 提出基于交叉边插桩与轻量 Petri 网可达图分析的并发 Bug 检测机制..."`
  5. `06_重点拆解__volcengine__OpenViking_源码级深度剖析与工程移植蓝图.md:22,53-59,121,170,173,259` — 反复以"EdgeIM/SBTPN 并发漏洞挖掘"并列出现
  6. `docs/MULTI_KERNEL_SYSTEM_ARCHITECTURE.md:144` — "鲁组并发论文检索、形式化定理分析、Petri 网验证与死锁重现"
  7. `docs/NEXT_PHASE_EXECUTION_PLAN.md:45` — "驱动多 Agent 并发检测并发死锁与数据竞争"
  8. `09_2026-09-19__窗口全景工作决算与交接总结__window_summary_and_handoff.md:66` — "并发死锁检测、Petri 网验证（`EdgeIM`, `SBTPN` 等 10 篇论文）"
  9. `04_试点标杆__PrimeIntellect-ai__prime-agent_源码级深度剖析与工程移植蓝图.md:164` — "鲁组的并发漏洞分析体系中…无幻觉的 Petri 网模型抽取与死锁静态验证"
- **关键独立佐证**：本仓另一条工作轨道 `01_进组总计划_OE1_材料交付/README_进组急用.md`（同日 2026-09-20 修订）在 J01 条目中**已独立发现并记录了同一污染**，裁定为 `SOURCE FACT：旧身份错误`，并在第 4 节明确写"09 目录的四核架构、harness 与验证宣传：本批未修，不得拿它们证明个人研究能力"。这证明：(a) 污染真实存在且已有独立证据链确认，非本次审计孤证；(b) 该轨道已明确声明未清理 09_ 目录，与本审计发现完全一致，两条独立路径互相印证。

**污染范围**：见 `CONTAMINATION_MAP.md` 第一节。已知触达 docs/ 全部 5 份文档、2 个 prototypes、2 份深度拆解卷宗、1 份窗口总结。

**修复建议**：见 `RECOVERY_PLAN.md` 项 1。不需要重写架构，只需在 9 处替换错误的论文本体描述；若某处 EdgeIM 只是"占位论文名"（如 harness 的 demo 任务描述），可直接替换为不依赖真实论文身份的中性占位符（如 `PAPER-DEMO-01`），避免继续消费一个被搞错的真实论文名义。

---

### P0-2：MULTI_AGENT_PARALLEL_SPECIFICATION.md 中 P05–P10 六篇论文系纯虚构

**症状**：`docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md:106-111` 列出 `DeadlockPredictor`、`DataRaceGuard`、`AsyncPetri`、`FormalEdge`、`LockTree`、`HybridRace` 六个论文标识，配英文副标题、独立写作用域路径、Worker 编号，形式上与真实论文（P01-P04）完全同构。

**证据**：
- 全仓检索（`grep -rln` 覆盖 `.md/.py/.json`，排除 worktree 副本）：这 6 个名称**仅出现在这一份文件里**，未出现在 `02_四论文Ownership主线/`、`03_鲁组其他论文与研究谱系/`（含 `09_前沿待跟踪/` 待定候选论文目录）、任何 `receipts/`、任何 teardown 文件中。
- 真实论文目录核验：`02_四论文Ownership主线/`（4 篇：EdgeIM, sigRank, GroundTruth_Sommers, CrossEdgeIM）+ `03_鲁组其他论文与研究谱系/`（7 篇：SBTPN, PNULOCK, UAF_PN_VFG, SEGLOCK_DeadlockSeg, SBPN, MHP, Deadlock_JOS2021）= 11 篇真实存在的论文目录（均含 PDF 或 teardown 文件）。
- 讽刺的是，`06_重点拆解__volcengine__OpenViking_源码级深度剖析与工程移植蓝图.md:247-277` 自己的 §4.2 虚拟目录树，**正确列出了这 11 篇真实论文**（ownership/ 4 篇 + pedigree/ 7 篇），与 `MULTI_AGENT_PARALLEL_SPECIFICATION.md` 的 P05-P10 表格互相矛盾——同一仓库、同一天，一份文档说对，另一份编了六个不存在的论文。这排除了"确实有 10 篇论文，只是我没找到"的可能性：内部证据自证矛盾。

**裁定**：`DeadlockPredictor / DataRaceGuard / AsyncPetri / FormalEdge / LockTree / HybridRace` = **FABRICATED / UNSOURCED**。不得合理化为"未来待补充的占位符"——它们带着假的副标题、假的写作用域路径，形式上冒充已存在的研究对象。

**次级问题**：P01(EdgeIM)、P04(CrossEdgeIM) 的英文副标题本身也不准确（P04 写"Distributed Edge Tracing"，真实标题是"An Edge-Based Approach for Interactive Robotic Behavior Model Discovery"，IEEE IoT Magazine 2026-01，DOI 10.1109/MIOT.2025.3625047，见 `02_四论文Ownership主线/04_CrossEdgeIM/论文原文与拆解/teardown-bridge-20260904/11_CROSSEDGEIM.md:14`）。

**【补充复核 2026-09-20 第二轮】P02(SBTPN)/P03(PNULOCK) 回源验证完成，此前 UNVERIFIED 状态解除，结论：同样 CONTAMINATED**：
- **P02 SBTPN**：`MULTI_AGENT_PARALLEL_SPECIFICATION.md:103` 写 "SBTPN: Symbolic Bounded Petri Net"。一手证据 `03_鲁组其他论文与研究谱系/01_SBTPN/论文原文与拆解/teardown-joint-20260813/01_SBTPN.md:1-3` 显示真实标题为 *"A New Knowledge Mining and Root Cause Analysis Methodology for Multivariate Time Series"*（Wang, Lu, Zhou, Zeng, IEEE/CAA JAS 2026, DOI 10.1109/JAS.2026.125837）——核心是"多变量时序知识挖掘 + 根因分析"，用协同/概率化 Petri 网（含催化/抑制协同弧）建模因果 AND/OR 规则，**不存在"Symbolic Bounded"这一概念**。这不是措辞近似的小误差，是把一篇工业时序根因分析论文包装成了一个听起来像形式化验证的假名字。
- **P03 PNULOCK**：`MULTI_AGENT_PARALLEL_SPECIFICATION.md:104` 写 "PNULOCK: Petri Net Unlock Analyzer"。一手证据 `03_鲁组其他论文与研究谱系/02_PNULOCK/论文原文与拆解/teardown-joint-20260813/02_DEADLOCK_PNULOCK.md:1-3` 显示真实标题为 *"Petri Net **Unfolding**-based Detection and **Replay** of Program Deadlocks"*（Lu, Lv, Cui, Bao, Zeng, IEEE Access 2024, DOI 10.1109/ACCESS.2024.3384489）——主题大类（Petri 网死锁检测）蒙对了，但"Unlock Analyzer"本身是编造词，真实机制关键词是"展开（unfolding）"与"确定性重演（replay）"，不是"解锁分析器"。
- **裁定更新**：P01/P02/P03/P04 四篇真实论文的英文 gloss **全部**不准确（4/4，不是此前认为的"仅 P01/P04 两篇"）。P05-P10 六篇全部虚构。也就是说 `MULTI_AGENT_PARALLEL_SPECIFICATION.md` 第100-111 行这张十行表格，**没有一行的英文副标题是准确的**——四行是真实论文但配错描述，六行是纯虚构论文。这比原审计判定的污染程度更重，应整表重做，不是逐行小修。

**修复建议**：见 `RECOVERY_PLAN.md` 项 2（已更新为整表重做，见下方修订）。

---

### P0-3：multi_agent_parallel_harness.py 的"100% VERIFIED"宣称超出实际证据强度（Claim Ceiling 违规）

**症状**：`docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md` 与该原型自身输出都宣称"🎉 MULTI-AGENT PARALLEL HARNESS VERIFIED (100% 成功)"，并据此推论"10 篇论文可在数十秒内完成结构化解析"（`MULTI_AGENT_PARALLEL_SPECIFICATION.md:82`）。

**实测（本轮真实执行，非转述）**：
```
$ python3 09_外部参考项目深度调研/prototypes/multi_agent_parallel_harness.py
[全部 4 任务 DELIVERED，总耗时 0.317s / 复跑 0.327s，TASK-004 retries=2]
EXIT_CODE=0
```
真实运行、真实 `ThreadPoolExecutor`、真实 CAS 租约冲突与重试（两次运行 retries 计数一致、耗时有波动，说明确实经过了线程调度而非纯打印）——**这部分证据成立**。

**但**：
- `AgentTaskDefinition.produce_artifact` 与 `validation_output` 是**构造函数传入的字符串字面量**（见源码 `prototypes/multi_agent_parallel_harness.py:194-233`），例如 `validation_output="18 passed, 0 failed in 0.22s"`。运行时不存在任何 `subprocess.run(["pytest", ...])` 调用。
- 磁盘核验（本轮实测）：
  ```
  $ find . -path "*/petri/analyzer.py" -o -path "*/petri/matrix.py"   → 空
  $ find . -iname "test_petri*"                                       → 空
  ```
  `produce_artifact` 字段声称的 `05_科研台/src/petri/analyzer.py (350 LOC)` 与 `validation_command` 声称执行的 `pytest tests/test_petri_analyzer.py` **均不存在于文件系统**。

**结论**：该原型**证明的是**："CAS 租约栅栏 + write-scope 冲突检测 + 指数退避重试"这套 toy 逻辑本身能跑通（TOY_TESTED，合格）。**不能证明**："真实多 Agent 协同"、"10 篇论文数十秒并发完成"、"工业级验证"——因为没有任何一个 Agent 真的读了论文、写了代码或跑了测试；四个"Agent"是同一进程内的四次函数调用，`produce_artifact`/`validation_output` 是预先编好的道具字符串。这正是 `RESEARCH_AGENT_CONSTRAINT_v1.0.md` §6 明令禁止的"把预先写好的'18 passed'字符串称为真实 pytest 结果"。

**修复建议**：见 `RECOVERY_PLAN.md` 项 3。

---

### P0-4：Outcome Floor 交付门禁只做非空字符串校验，结构性无法拦截"自报假完成"

**症状**：`docs/MAINTENANCE_MANUAL.md` 与 `MULTI_AGENT_PARALLEL_SPECIFICATION.md` 都描述 Outcome Floor 为"强制要求真实产物 + 定向测试通过输出 + 状态回写指纹，缺一直接拒签"，暗示这是一道内容级验证门禁。

**源码核验**（`prototypes/minimal_loopx_kernel.py:395-435`，`deliver_task` 函数）：
```python
if not artifact or not targeted_validation or not state_writeback:
    return {"success": False, "error": "违反最低交付门槛..."}
```
这是**唯一**的校验逻辑——三个参数只要非空字符串即通过。函数体内没有：
- 对 `artifact` 路径做 `os.path.exists()` 检查；
- 对 `targeted_validation` 做真实命令执行或输出格式校验；
- 把 `state_writeback` 的哈希与 `artifact`/`targeted_validation` 的实际内容绑定校验（哈希输入完全由调用者自由拼接，见 harness 源码 `state_content = f"{task_def.produce_artifact}:{task_def.validation_output}:{time.time()}"`——调用者可以对任意假字符串求哈希，"密码学指纹"不提供任何防伪造能力，只是把假字符串搬进了 SHA-256）。

**结论**：Outcome Floor 目前能拦截的只是"完全没填字段"这一种失败模式（如 `USER_MANUAL.md:159-168` 演示的"口头假汇报被拒"）。它**不能**拦截"填了内容详实但全部虚构的字段"——而这恰恰是本次审计从头到尾遇到的真实失败模式（P0-1、P0-2、P0-3 都是"字段非空、内容失真"）。文档语言（"强制要求""拒签"）暗示的保证强度超过代码实际提供的保证强度。

**修复建议**：见 `RECOVERY_PLAN.md` 项 4。

---

## P1 · 会导致研究路线或工程判断出错

### P1-1：Git 分支隔离规则被自己违反——"清洗"序列直接提交在 main 上

**证据**（`git reflog show main`）：
```
main@{0} ea91ab5 chore: cleanup intermediate red team reports
main@{1} 8effd36 fix(purge): 彻底剔除...幻觉与串线功能
main@{2} 59b8faf fix(audit): 触发 CleanAgent 红蓝对抗自检
main@{3} 7902344 feat & docs: 落地 Headroom...
main@{4} 573b114 feat & docs: 落地多Agent并发协同规范...
```
`feature/moraine-companion-integration` 分支是在 `ea91ab5` **之后**才从 HEAD 切出的（`git reflog show feature/moraine-companion-integration` 只有一条：`Created from HEAD`）。也就是说，从批量落地 Headroom/多 Agent 材料，到"红蓝对抗自审"，到两轮"purge"，全部 5 个提交都是**直接在 main 上完成的**，隔离分支形同马后炮。

**次级发现**：`origin/main`（远程）目前只到 `7902344`，尚未推送 `59b8faf`/`8effd36`/`ea91ab5`。这是一个仍然干净的补救窗口——本地 main 上这一段"未隔离审查"的提交还没有污染远程记录。

**修复建议**：见 `RECOVERY_PLAN.md` 项 5。

---

### P1-2：唯一的"红蓝对抗自审"是同模型左右手互搏，不构成异构交叉审查

**证据**（从被删除的 `RED_TEAM_AUDIT_REPORT.md` 恢复，`git show ea91ab5~1:09_外部参考项目深度调研/RED_TEAM_AUDIT_REPORT.md`）：
```
模型矩阵: leon-agy/gemini-3.8-flash-high (Red) vs vasi-agy/gemini-pro-agent[1M] (Blue)
```
这次"CleanAgent 红蓝对抗自检"（commit `59b8faf`）的红队和蓝队都是 Gemini 家族模型的不同人格设定，不是用户后续确立的"Gemini=Generator, Claude/GPT=Verifier"异构分工。更值得注意的是：这次自审的"整改勒令"是要求**加回**已被证明是幻觉的 `CodeCompressor`（AST 折叠）和 `LogCrusher`——即同模型自审几乎把已经查出的幻觉又建议写回去，直到下一轮 `8effd36` 才被再次剔除。这是"幻觉共振"的一个实例证据，不是假设。

**修复建议**：见 `RECOVERY_PLAN.md` 项 6。

---

### P1-3：Headroom 拆解卷宗（已净化版）仍有未经测量的具体百分比数字

**症状**：`10_重点拆解__headroomlabs-ai__headroom_...md` 模块二 benchmark 表格给出具体数字——Truncation "< 10%"、Summarization "约 85%"、Headroom "100%" 早期异常留存率。

**核验**：`receipts/sources/headroom/compression_benchmark.py` 确实定义了这套三方对比基准测试的代码（`truncate_data`/`summarize_data`/`headroom_compress`/`evaluate_answer` 等函数存在，非空谈）。但该脚本依赖 `from openai import OpenAI` 与 `model="gpt-4o-mini"` 的真实 API 调用才能产出数字；本仓没有任何该脚本的执行输出、日志或 receipt 留痕。这与 P0-1/P0-2 不同——机制本身是真的（源码锚点核验通过），但**具体数字目前无一手测量支撑**，属于 `RESEARCH_AGENT_CONSTRAINT_v1.0.md` §8 定义的"未经测量不得给出具体数字"违规，只是这次是残留在"已净化"版本里的更细微的一层。

**修复建议**：见 `RECOVERY_PLAN.md` 项 6。

---

## P2 · 训练设计与研究闭环缺口

### P2-1：孙猛导师画像当前不存在，且暗藏同名误绑风险

**证据**：全仓检索 `孙猛|sun_meng|sunmeng`（排除 worktree 副本），未发现任何独立的、近 3–5 年证据支撑的导师画像文件。唯一系统性提及在 `01_进组总计划_OE1_材料交付/` 的历史任务日志与 `README_进组急用.md:J05`——该文件**已明确自判**"孙猛当前核心方向、基金/学生题目与合作网络已核清"为 `UNSOURCED：当前画像未重建`，且指出"交集矩阵主要依据会话转述，缺逐项一手证据"。`CHANGELOG.md:448` 提到历史存在过一份"孙猛专题报告"（`phase0/sun_meng/`, 44KB, 38 篇论文），但该路径在当前工作树中**不存在**（`find` 结果为空）——NOT FOUND，无法判断是遗失、未提交还是从未落盘到本仓。

**额外风险**（`PROJECT_HOME.md:51`）：仓库自己的决策记录标注了一个尚未定案的同名歧义——`Jun Sun(SMU) / 孙猛(PKU, ReGA) / Meng Sun(PKU)` 三个身份存在被混淆的风险（"三分 vs 两人合并"）。这正是 `RESEARCH_AGENT_CONSTRAINT_v1.0.md` §3 与用户参考指令 §E 专门警告的"禁止同名误绑"场景，且是仓库自己已经识别但尚未解决的活跃风险，不是本次审计新造的假设性担忧。

**【补充复核 2026-09-20 第二轮】发现原审计漏检的相关目录，结论方向不变但需精确化**：`03_鲁组其他论文与研究谱系/08_导师画像_谱系_团队/`（**已于 initial commit `a4d942a` 入库，非本轮新增，此前审计遗漏**）存在一个训练包骨架 `ra2716-survey`（BRIEF.md / KICKOFF.md / EX-01 空白模板），但核实后确认：
- 该包的**主训练对象是鲁法明**（现导师）画像盲写方法论，孙猛只是 EX-04（**可选**，"死线紧则 Agent 代做孙猛素材"）的次要迁移验证对象，不是孙猛专属画像包。
- 对账用的"密封答案" `孙猛_PKU_2024-2026_学术产出审计.md` 被明确引用为存在于**仓外**路径（`D:\Code\_archive` / MAS 仓 `progress/audits/2026/07/`），**不在本仓 `zancun` 内**（`find` 全仓确认无此文件）——无法判断该外部文件当前是否存在、内容是否可信，只能确认"本仓不含它"。
- `EX-01_鲁法明画像v0.md` 实测为**全空白模板**（30 行，六个维度标题下全部空白），BRIEF.md 的 Amendment A1（2026-09-05）明确注记"历史空白保持原样，不追认旧 EX-01 PASS"——即这个盲写练习从未被真正执行过一次，不构成任何画像证据。
- **修正后的结论**：不改变"孙猛当前画像不存在"的核心裁定，但补充精确度：本仓内不存在孙猛画像**内容**，但存在一份关于"如何调研孙猛画像"的**训练方法论骨架**（未执行）+ 一处对外部密封答案文件的**引用指针**（该文件本身不在本仓、未经核实）。`RECOVERY_PLAN.md` 若涉及孙猛画像重建，应确认是否要一并激活 `ra2716-survey/EX-04` 这条已设计好的训练路径，而非另起一套。

**结论**：这不是"文档没写"的问题，是"没有一手材料"的问题——只读审计无法在不联网检索的前提下补齐，也不应该补。裁定：`RESEARCH PIPELINE INCOMPLETE`，缺失节点 = 导师侧 literature search 与 disambiguation。

---

### P2-2：现有"学习/训练"资产多为架构说明与操作手册，尚未观察到"假设→反例→最小实验→结果"闭环的实证

**观察**：`docs/` 与拆解卷宗的性质是"这个外部项目怎么设计、我们怎么搬"，属于 mechanism extraction 阶段。本轮审计范围内没有找到 P05-P10 之外的、真正意义上的"toy hypothesis → falsifier → baseline → measured result"记录（`02_四论文Ownership主线/*/学习与课程/` 下的 ownership-v3 材料超出本次 09_ 目录审计范围，未纳入判断，避免越权评价）。

**限定**：此项判断范围严格限定在 `09_外部参考项目深度调研/`；不对 `02_/03_` 目录的训练闭环下结论——那是另一套独立建设的资产，用户参考指令里也未要求本次审计覆盖它。

---

## P3 · 工程卫生问题

### P3-1：证据留存目录存在两套不一致的锚点惯例

`receipts/sources/<project>/` 用于保存"精选源码片段"（Headroom 项目下有 3 个文件，锚点齐全）；但 `receipts/repos/<project>/` 是完整原始仓库克隆（LoopX 项目下有 4555 个文件）。LoopX 拆解卷宗引用的 8 处 `file:line`（`goal_policy.py:63-66` 等）全部指向后者而非前者，而 `receipts/sources/loopx/` 只有 3 个不相关文件（`lark-authority-protocol.md`、`rfc-control-plane.md`、`services.rs`——`services.rs` 甚至未被卷宗引用过）。**本轮逐条核验：这 8 处引用全部真实存在且内容精确匹配**（详见 `TRUTH_AUDIT_LEDGER.tsv` LoopX 相关行），不是幻觉——只是证据摆放位置不统一，增加了审计与复核成本。

### P3-2：`.claude/worktrees/wf_e225026d-74d-2/` 遗留未跟踪目录

体量上复制了大半个仓库树（含 `01_/02_/03_/05_/07_` 多个目录），未被 `.gitignore` 排除，未被 `git status` 追踪但确实占用磁盘并可能在全仓 grep 时产生重复命中干扰（本轮审计初期已遇到并主动排除）。

### P3-3：`RESEARCH_AGENT_CONSTRAINT_v1.0.md` 从未被提交

`git log --all -- RESEARCH_AGENT_CONSTRAINT_v1.0.md` 为空。该文件当前只是工作区的一份未跟踪文件，对任何新 clone、新分支、新会话都不可见，不具备它声称的"全局父规约"约束力。

---

## 独立复核建议（呼应用户原始要求）

本报告是单一模型（Claude）的独立审计，但仍是**单一视角**。建议按用户设想的模式，让另一个独立模型（如 GPT 系）仅拿本报告 + `TRUTH_AUDIT_LEDGER.tsv` + 原始证据文件做对抗性复核，专门检查：
1. 我是否也犯了"过度宣称"——例如 P0-3/P0-4 的措辞是否比证据允许的更重；
2. LoopX/Prime-Agent 引用"验证通过"的结论是否有我未检查到的反例；
3. 本报告本身是否有条目违反了它自己引用的 `RESEARCH_AGENT_CONSTRAINT_v1.0.md`。
