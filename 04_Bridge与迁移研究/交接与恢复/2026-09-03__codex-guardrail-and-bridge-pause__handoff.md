# Codex 防呆核验与 Bridge/R1 当前进度归档

**日期**：2026-09-03（Asia/Taipei）
**任务**：TASK-20260903-001
**状态**：ARCHIVED / PAUSED / RECOVERABLE / NO-EXECUTION-AUTHORITY
**触发**：用户明确要求“先存档进度”

## 0. 本档边界

本档只保存本窗口截至归档时已经核对的事实、当前开放门和恢复路径。没有继续实验、没有读取 EdgeIM PDF 的 Stage-1、没有替用户裁定 R1、没有整理或提交整棵未跟踪树。既有代码、实验数值和其他窗口的修改均保持原状。

上下文恢复钩子在本窗口用正确的 SessionStart/compact 事件格式复核后返回：

CONTEXT_RECOVERY_STATUS=UNVERIFIED / REASON=missing_binding

因此本档不把会话摘要、cwd 或旧 task 号当成恢复授权；恢复正式工作前必须有用户确认的显式 session→repo→task 绑定。

## 1. 已重读的权威文件

- progress/handoff/2026-09-03__bridge-r1-pilot__pause-handoff.md：pilot 已暂停，禁止自动扩展。
- progress/decisions/2026-09-03__research__bridge-segment0-execution-brief-v1.1.md：G0/T0 尚未完成，PDF 不可降级。
- learning/Learning–Research OS v0.1 — FROZEN 2026-09-03.md：用户冻结的训练与 ownership 规则。
- learning/2026-09-03__learning-research-os-v0.1.md：用户已删除；不再作为候选或恢复入口。
- GUARDRAILS.md、AGENTS.md、CLAUDE.md 与 progress/templates/TASK_LOG_TEMPLATE.md：当前工作流和运行时留痕要求。
- ~/.codex/hooks.json 与 ~/.codex/config.toml：当前 Codex 实际配置；不把配置文件当作 effort 证据。

## 2. Codex 防呆核验结果

### 2.1 规则文本目前不会自动进入 Codex 上下文

当前工作目录是外层仓库 /mnt/d/MyResearch。该层没有 AGENTS.md；GUARDRAILS.md、WINDOW_PLAYBOOK.md、CROSSWINDOW.md 都是普通 Markdown 文件，不会因文件名自动成为 Codex 项目指令。嵌套 MAS_Safety_Project/AGENTS.md 只在以嵌套仓为项目范围时适用，且它没有引用外层 GUARDRAILS.md。当前 config.toml 没有 project_doc_fallback_filenames，所以这几个文件没有自动加载证据。

结论：我可以手动读取并遵守它们；但按当前盘面，不能声称 Codex 已全局自动使用该规则。

### 2.2 当前没有运行时 preflight 拦截

全局 hooks 只有既有的 Stop 组和 SessionStart 的 compact 恢复钩子；没有检查 runtime 四字段、长任务分类、Agent 派发或危险权限模式的 PreToolUse/UserPromptSubmit 门。恢复钩子本身在缺少 binding 时能正确拒绝升级为 VERIFIED，但它不负责 task log 或 effort 门禁。

### 2.3 本窗口的实际运行态会触发护栏告警

可核对的当前进程路径是 codex --yolo；本会话持久化 turn metadata 记录模型为 gpt-5.6-sol，effort 曾为 xhigh、后续为 ultra，权限为 approval=never、sandbox=danger-full-access。这与 GUARDRAILS.md §5 的 workspace-write + approval=on-request 基线不一致。~/.codex/config.toml 中的 xhigh 只能说明默认配置，不能解释托管/会话内变化。

本次归档仍是只读核验加受限文档落盘；没有启动长任务、实验或子 Agent。上述运行态应作为“当前会话护栏未实际拦住”的证据，而不是成功配置证明。

## 3. Bridge/R1 盘面事实（截至归档）

1. research/tracebridge_full_spectrum_20260830/ 仍有整棵未跟踪内容，包含 00_control/BRIDGE_LU_PLANNING_LOG.md、seg0 与 08-30→09-03 的 decisions/handoff；本窗口没有对其执行 git add、移动或清理。
2. research/edgeim_sampling_audit/ 的既有审计产物和暂存状态保持不动；其 STATUS.md 仍把数值定为非证据，不能引用为 EdgeIM faithful reproduction。
3. 计划日期已经按用户本轮修订为：CLAUDE.md 与 WINDOW_PLAYBOOK.md 的进组口径为九月底（09-10 为最早乐观估计）；执行计划仍把 09-20 定为 core freeze、09-25 定为 package check。按当前修订，这些是不同里程碑，T4 不需因日期冲突重排。
4. v1.1 已由用户降为 PROPOSED-DRAFT（待用户批），并明确 C-069 落盘前不得作为派发依据；它提出的 W2 撤回、新 G0/T0 与 C-065 关系仍待规划日志 amendment 消费。
5. STATUS.md 已收窄 H1 表述：首次携带 distinct 非法边的 trace 必留；重复者有条件地被滤；D′ 噪声占比高于随机是计数题，不是判据直接推论。该 STATUS 仍为非证据目录说明。
6. _withdrawn/README.md 已补三份文件的 SHA-256，并明确“已隔离、待登记”而非“已正式作废”；C-069 尚未写入规划日志。
7. 今日新工作此前没有对应 task log；本归档已先领取并登记 TASK-20260903-001。shuorenhua/防呆 TODO 与当前 EdgeIM CROSSWINDOW 细项仍是开放欠账，本档只记录，不擅自补写。
8. 同日短 OS 文件已按用户指示删除；当前只保留 17,302 B 的 Learning–Research OS v0.1 — FROZEN 2026-09-03.md，后续以它为唯一恢复入口。本档不再要求 superseded 标记。

## 4. 本次已完成

- 通过 8899 中央发号器领取 TASK-20260903-001。
- 在 progress/task_logs/INDEX.md 先占一行，再写本档；INDEX 使用保形 CAS 工具，未覆盖他窗改动。
- 固化 Codex 防呆核验结果、运行态、四项 Bridge 阻断和恢复顺序。
- 没有改代码、配置、实验结果、PDF、冻结 OS、计划正文或其他窗口的已有 M/暂存路径。

## 5. 未完成 / 不得从本档推导为已完成

- 用户 G0：完整读 PDF Stage-1、回答 v1.1 五问。
- T0：重新裁定 R1（撤销、降级复现、转频次问题或用户另提）。
- C-069：把用户本轮口令与 W2/T1/T2/T3/日期处置写入规划日志。
- TraceBridge 整棵树的持久化/版本控制方案与用户授权。
- 已确认保留的 OS 唯一恢复入口是否仍符合用户后续修订（本档不改其内容）。
- TODO、CROSSWINDOW 当前欠账和防呆机制的自动化接入。
- 任何实验扩展、PM4Py 下游补件、公开、commit 或 push。

## 6. 恢复第一动作

1. 读取本档；确认用户提供的 task/恢复绑定后，再读取 v1.1 §1 与 PDF Stage-1。
2. 用户本人写出五问答案并决定 T0；在此之前不写 measurement contract、不运行实验。
3. 若只需检查归档，保持只读；若要继续正式工作，先建立唯一的 session→repo→task binding，并重新填写 task log runtime 块。

## 7. 写域与回滚

本次新增写域仅为本档、对应 task log、task log INDEX 的新行，以及登记路由行。没有删除或覆盖既有文件；回滚只需在用户明确授权后按这些新增路径逐项移除/恢复，不能用 reset、clean 或整文件回写代替。

## 8. 反向引用

- task log：progress/task_logs/2026/09/2026-09-03__archive__codex-guardrail-and-bridge-pause.md
- task index：progress/task_logs/INDEX.md 的 TASK-20260903-001 行
- 当前 R1 暂停入口：progress/handoff/2026-09-03__bridge-r1-pilot__pause-handoff.md
- 当前段 0 规格：progress/decisions/2026-09-03__research__bridge-segment0-execution-brief-v1.1.md

**归档结论**：本窗口已安全停在“事实已保存、研究未恢复、无执行授权”。
