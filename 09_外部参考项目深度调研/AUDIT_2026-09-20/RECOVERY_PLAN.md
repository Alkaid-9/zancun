# RECOVERY_PLAN.md

原则：只做最小必要修复，不重做整个仓库，不新造第五套架构，不因为"顺手"而扩大修改范围。每项标注涉及文件、修改方式、验收标准。**本计划本身不执行——按用户流程，先呈报审计结果，双方确认后再动手，且修复动作也应遵循 git 分支隔离规约。**

---

## 1. 修正 EdgeIM 本体描述（对应 AUDIT_FINDINGS P0-1）

**范围**：9 个文件中，把错误的"并发死锁/数据竞争检测"描述替换为真实的"边缘流程挖掘"描述，或在纯 demo 场景下替换为不冒用真实论文名义的中性占位符。

**具体动作**：
- `docs/USER_MANUAL.md:85-89`：替换 `title`/`abstract`/`overview` 三个字段为真实内容，或改用占位符 `PAPER-DEMO-01`（因为这里只是演示 API 用法，不需要绑定到任何真实论文）。
- `docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md:102`：P01 的英文副标题改为准确描述或标注"[演示用占位描述，非论文原题]"。
- `prototypes/multi_agent_parallel_harness.py:196`：task 描述文本同上处理（低风险，只影响打印文本，不影响程序逻辑，可选择性修复）。
- `prototypes/minimal_openviking_kernel.py:302-307`：demo 数据替换为真实摘要，或明确标注为虚构 demo 数据。
- `06_重点拆解__volcengine__OpenViking_...md`：修正 §引言/§价值主张里的错误并列描述；**保留** §4.2 目录树（已经是对的）。
- `docs/MULTI_KERNEL_SYSTEM_ARCHITECTURE.md:144`：科研台职责描述改为准确覆盖"流程挖掘 + 并发死锁验证"两类真实存在的研究方向（该目录下确实有 SBTPN 等死锁类论文，只是不能挂在 EdgeIM 名下）。
- `docs/NEXT_PHASE_EXECUTION_PLAN.md:45`：Week 4 专项描述同上修正。
- `09_2026-09-19__窗口全景工作决算与交接总结__window_summary_and_handoff.md:66`：修正 LINE-03 一行描述（历史交接文档，建议加勘误批注而非静默改写，保留可追溯性）。
- `04_试点标杆__PrimeIntellect-ai__prime-agent_...md:164`：修正应用场景描述。

**验收标准**：修复后，`grep -rn "T_lock\|M_wait\|Efficient Detection of Concurrency Bugs" 09_外部参考项目深度调研/` 应为空。

---

## 2. 整表重做（不是逐行小修）：`MULTI_AGENT_PARALLEL_SPECIFICATION.md` 第100-111行论文表（对应 AUDIT_FINDINGS P0-2，**范围已在第二轮复核后扩大**）

**范围**：`docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md:100-111` 整张表，不只是 P05-P10 六行。

**第二轮复核新增事实**：回源核对后确认 P02(SBTPN)/P03(PNULOCK) 的英文 gloss 同样是错的（P02 编造了"Symbolic Bounded"概念；P03 编造了"Unlock Analyzer"术语）。连同此前已确认的 P01(EdgeIM)/P04(CrossEdgeIM) 副标题错误，**这张表 10 行里没有一行的英文描述是准确的**——4 行真实论文全部配错描述，6 行论文全部虚构。

**具体动作**：
- P01-P04：四行的英文副标题需要整体替换为一手证据确认的真实标题（EdgeIM → process model discovery；SBTPN → multivariate time-series knowledge mining & RCA；PNULOCK → PN unfolding-based deadlock detection & replay；CrossEdgeIM → interactive robotic behavior model discovery），或者如果表格意图只是"论文标识 + 写作用域路径"的调度演示、不需要精确学术描述，就把英文副标题整列删除，只保留论文名与路径，避免继续输出任何具体描述性文字。
- P05-P10：删除六行；若确实需要演示"10 个并发 Worker"的调度能力，改用中性占位符（`SLOT-05`...`SLOT-10`）或明确标注"以下为容量演示占位符，非真实论文"；若只需演示 4 篇真实论文的并发处理，将表格缩短为 P01-P04，并在旁注说明"当前科研台仅 4 篇 Ownership 主线论文进入并发调度试点，其余 7 篇（03_ 目录）待后续纳入"。

**验收标准**：`grep -rn "DeadlockPredictor\|DataRaceGuard\|AsyncPetri\|FormalEdge\|LockTree\|HybridRace\|Symbolic Bounded\|Unlock Analyzer" 09_外部参考项目深度调研/` 应为空；且 P01-P04 保留的任何英文描述文字都必须能在对应 teardown 一手证据文件中找到逐字或近义对应。

---

## 3. 降级 Harness 的证明力措辞（对应 AUDIT_FINDINGS P0-3）

**范围**：`docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md` §五、`docs/USER_MANUAL.md` §四。

**具体动作**：
- 把"🎉 MULTI-AGENT PARALLEL HARNESS VERIFIED (100% 成功)"改为"TOY_TESTED: CAS 租约栅栏与写作用域冲突退避逻辑通过（不代表真实多 Agent 协同或真实论文处理）"。
- 删除或标注"10 篇论文可在数十秒内完成结构化解析"这一推论为 HYPOTHESIS，注明"尚未有真实 Agent 执行案例支撑"。
- 若要让这个 harness 真正具备证明力，需要至少一个任务的 `produce_artifact` 指向真实写入的文件，`validation_command` 真正 subprocess 执行并捕获 exit code——这是后续工程任务，不在本次文档修复范围内，留待用户决定是否值得投入。

**验收标准**：文档中不再出现未经限定的"100%验证""工业级""真实多 Agent"等措辞；如保留百分比数字，须附带其精确适用范围（如"4/4 toy 任务的 CAS 逻辑测试通过"）。

---

## 4. 明确 Outcome Floor 的真实能力边界（对应 AUDIT_FINDINGS P0-4）

**范围**：`docs/MAINTENANCE_MANUAL.md` 故障排查表、`docs/MULTI_AGENT_PARALLEL_SPECIFICATION.md` §一 Level 4 描述。

**具体动作**：加一句限定说明，例如："当前实现仅校验三字段非空，不校验内容真实性（不做文件存在性检查、不真实执行验证命令、哈希不提供防伪造能力）。如需内容级校验，需扩展 `deliver_task` 增加 `os.path.exists(artifact)` 与真实子进程执行。"

**验收标准**：文档措辞与 `prototypes/minimal_loopx_kernel.py:395-435` 源码实际行为一致，不留证明力缺口。若用户希望真正补上这道门禁（而不只是改措辞），这是一个独立的、值得做的小工程任务，建议另开 issue/TODO，不与本次文档纠偏合并。

---

## 5. 落实 main 分支保护（对应 AUDIT_FINDINGS P1-1）

**具体动作**：
- 本次审计已从 `ea91ab5` 切出 `audit/redteam-external-ref-2026-09-20` 分支，只在此分支内新增审计产物，未改动 main 上的既有文件。
- 建议：鉴于 `origin/main` 目前仅到 `7902344`（尚未推送 `59b8faf`/`8effd36`/`ea91ab5`），可以考虑在本地把 main 回退到 `7902344`，将后续 4 个提交（`573b114` 已推送需另评估、`7902344`已推送、`59b8faf`/`8effd36`/`ea91ab5`未推送）的内容通过 `feature/moraine-companion-integration` 分支重新组织后再合并——这样可以让 main 的历史干净地反映"审查后才合并"的纪律。**这是否要做、如何做，需要用户决定**（涉及改写本地分支历史，风险可控但需要用户明确同意），本审计不擅自执行。
- 后续所有 Agent 生成内容，落地前必须先 `git checkout -b`，不直接在 main 上 commit。

**验收标准**：`git log main` 不再出现未经跨模型审查的大批量内容提交；新工作流程写入 `git-branch-and-review-protocol.md`（已存在于用户记忆库，本次审计未发现需要修改该规约本身）。

---

## 6. 修正"红蓝对抗自审"的角色配置 + Headroom benchmark 数字降级（对应 AUDIT_FINDINGS P1-2、P1-3）

**具体动作**：
- 若未来还需要"红蓝对抗"环节，红蓝两队必须是异构模型（如 Gemini 生成 vs Claude/GPT 审查），不能是同模型不同人格设定。当前记忆库 `git-branch-and-review-protocol.md` 已经写明这条规则，只是这次实际执行时被违反——不需要改规则文本，需要改执行纪律。
- `10_重点拆解__headroomlabs-ai__headroom_...md` 模块二表格的具体百分比（<10%/85%/100%）改为"[UNVERIFIED — 未在本仓执行 compression_benchmark.py 产出真实数字，机制真实存在但数字待实测]"，或者如果用户希望这些数字成立，安排一次真实执行（需要 OpenAI API key）并把 receipt（command/stdout/timestamp）存入 `receipts/`。

**验收标准**：不再有"红蓝对抗"环节使用同一模型家族的不同人格；Headroom 卷宗数字要么删除要么附带真实执行 receipt。

---

## 7. 孙猛画像与下阶段计划对齐（对应 AUDIT_FINDINGS P2-1，呼应用户原始指令 §E/§11）

**范围**：`docs/NEXT_PHASE_EXECUTION_PLAN.md` 中任何隐含"孙猛画像已就位"的桥接设计前提。

**具体动作**：
- 不在本次只读审计中重建孙猛画像——这需要联网检索近 3-5 年论文/项目/学生题目，超出本轮"只读审计现有仓库文件"的授权范围，也超出 `01_` 轨道已声明的"未联网刷新"边界。
- 建议：在 `NEXT_PHASE_EXECUTION_PLAN.md` 中新增一条��置任务"孙猛当前研究画像重建（含姓名歧义排查：Jun Sun(SMU) vs 孙猛(PKU,ReGA) vs Meng Sun(PKU)）"，并将其列为跨导师 bridge 设计的阻塞前提，而不是隐含假设。
- 此项是否现在做、谁来做（用户本人 or 后续授权 Agent 联网检索），需要用户决定。

**验收标准**：`NEXT_PHASE_EXECUTION_PLAN.md` 不再隐含"孙猛当前方向已知"这一未经验证的前提。

---

## 8. 治理性收尾（低优先级，P3）

- 提交 `RESEARCH_AGENT_CONSTRAINT_v1.0.md`（当前未跟踪，建议 `git add` 后随本次审计分支一并提交，使其对后续会话真正可见）。
- 清理 `.claude/worktrees/wf_e225026d-74d-2/` 遗留目录（确认是否还有进程/会话依赖后再删，避免误删活跃工作）。
- 统一 `receipts/sources/<project>/`（精选片段）与 `receipts/repos/<project>/`（完整克隆）两种留存惯例的使用规则，建议在 `00_深度调研SOP与工程规范_v2.0.md` 补一条："凡卷宗引用 file:line，必须注明该文件位于 receipts/sources/ 还是 receipts/repos/，避免复核者误以为引用无据"。

---

## 不建议做的事（呼应用户指令 §10 非目标）

- 不重新设计"四核架构"——MKASA 的整体构想（Prime-Agent 调度 + Moraine 记忆 + OpenViking 上下文 + LoopX 控制平面）本身没有被证明是错的，只是几处应用场景描述踩了污染源 A/B。architecture 层面不需要推翻。
- 不因为发现了 harness 的证明力缺口，就要求"必须做出一个真正的工业级多 Agent 系统"——这超出当前阶段目标，也不是用户要求的范围。
- 不擅自重建孙猛画像（见项 7）、不擅自改写 main 分支历史（见项 5）——这两项都标注为"需要用户决定"，本审计到此为止，等待确认。
