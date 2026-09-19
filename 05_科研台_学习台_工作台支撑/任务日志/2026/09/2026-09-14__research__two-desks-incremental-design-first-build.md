---
id: TASK-20260914-002
title: 科研台与学习台增量设计及首批施工方案
date: 2026-09-14
runtime:
  model: Codex; exact SKU UNKNOWN
  effort: UNKNOWN
  effort_source: 当前平台未提供可独立确认的有效 effort；不从配置推定
  launch: 当前交互式 Codex 会话
type: research
status: completed_with_open_gates
area: research-learning
project: research-desk
todo_ids: []
owners:
  - Codex controller
related:
  - progress/decisions/two-desks-delta-20260914/README.md
  - progress/decisions/2026-09-14__research__multilayer-content-map-provisional-baseline.md
  - progress/decisions/rd2-construction-v0.3/SOL_START_HERE.md
---

# 目标

用户要求推进科研台和学习台，并明确选择“先完成两台增量设计与首批施工方案（推荐）”；最高 2 并发，包含主线程。本任务只做有界交互式设计、既有代码的只读核对和方案交付，不修改应用、不启动实验或部署，不关闭真实用户验收。

# 当前状态

设计与首批方案已交付，续作补齐 B 的记录／返回／版本导出接口提案，等待用户审阅／代码范围批准；应用和真实数据未改。中央 allocator 实际签发 TASK-20260914-002，solver 预检通过。科研台应用为独立 Git 仓，main，HEAD d53d188faff8e64ae9d22d92dd1eeab1b8309b84，开工与主线程收尾只读 status 均干净；旧“未独立版本化”仅为历史。

# 最终结果

累计交付 5 份设计文档：科研 map 的内容与最低／正常／长期要求、原八类内容／七图映射、学习台目标要求与个人证据、两台入口和三条纸面路径、旧两稿九项完整对照、A 体验修复＋B 两台往返切片的范围／前置／验收／写域，以及 B 接口提案。设计仍为 PROPOSED，不是可直接启动的实施授权。

没有把科研 map 新设计倒写为上次已接受方案，没有修改旧合同、应用或用户记录。独立只读子代理因 429 失败，没有产出审查证据；主线程完成范围内自查，不能称独立复审通过。

# 修改内容

- 新建[设计总入口](../../../decisions/two-desks-delta-20260914/README.md)：授权、版本基线、已有／未做、恢复与开工边界。
- 新建[两台增量设计](../../../decisions/two-desks-delta-20260914/DESIGN_DELTA.md)：需求对账、科研内容版图、知识要求／证据分离、低保真与三条纸面路径、窄合同建议。
- 新建[九项场景对照](../../../decisions/two-desks-delta-20260914/SCENARIO_RECONCILIATION.md)：完整对比两稿，纠正盲审独立性、观察类型、指导使用与 SourceRef 的过强表述，并补两个合成反转情境。
- 新建[首批施工方案](../../../decisions/two-desks-delta-20260914/FIRST_BUILD_PLAN.md)：A1/A2/B1/B2 范围、G0–G4 条件、A-01–09 与 B-01–10 预期验收、源码位置和隔离交付。
- 续作新增[B 接口提案](../../../decisions/two-desks-delta-20260914/B_CONTRACT_PROPOSAL.md)：推荐记录字段、窄查询入口、原问题同身份进入分支、指定原视图返回、版本选择导出及旧记录兼容。
- 本任务记录及 handoff／task log 两份 INDEX 的本任务唯一入口；不修改它们的旧行、TODO 或生成视图。

# 尚未完成

- 用户审阅本次新增科研 map、两台路径与 A/B 实施范围；目标要求记录、分开的评价、返回上下文的具体 CONTRACT_DELTA 尚未冻结。
- C03 真实用户复验、真实考研及科研／工程案例试用；本轮仅合成纸面场景。
- 子代理未产出独立设计复核；后续如需独立审查应另有有效结果，不用本次 429 补记替代。
- A/B 代码、后续 C04–C07、官方考纲细目、完整多层图、指导使用、课程补修、研究实验、真实迁移、部署和 push 均未执行。

# 下一步

用户先审科研 map 的各档要求与两台代表路径，再决定是否批准首批 A 或 A＋B。未授权前只继续设计；B 按首批方案处理窄合同和 C03 使用反馈，不因设计交付自动开工。

# 验收与证据

| 检查 | 结果与范围 |
|---|---|
| 需求对账 | 主线程检查多层、四科／2027-12、鲁—孙—工业导向、权重不猜、本人证据／研究判断分离、科研范围与 toy 均进入设计 |
| 两稿九项 | 主线程完整重读两份场景稿与 09-12 订正；9 行对照齐全，区分共同点、覆盖差异、真实取舍和首批处置；不是独立实现证据 |
| 场景与首批 | 3 条纸面路径；A 9 项、B 10 项为未来验收预期，不标已运行或用户通过 |
| 当前代码 | 静态确认 renderP1Source 的前 300 截断、capture 保存阶段、七类关系与返回白名单；不根据旧 22/22 宣称本次测试通过 |
| 自查修正 | 更正函数名为 p1EntryPanel；要求正式记录绑定目标和知识，草稿单独保留；区分原视图／分支视图；未定位原段和响应丢失如实显示 |
| 子代理 | two_desks_design_review 为唯一新增只读位，总并发最高 2；429 exceeded retry limit，无实质输出，不重复派发、不计独立 PASS |
| 文档初检 | 4 份设计文档的 35 个本地链接均存在，无替换字符／行尾空白，围栏配对；最终全写域复验见补记 |
| 应用边界 | 收尾 research-desk Git status 仅显示 main，工作树干净；未打开真实库或旧用户验收数据库，未启动服务／测试／研究实验 |
| 暂存与外围 | MAS 暂存区为空；只操作本任务文档和索引，既有共享改动保留，无 commit/push |

# 风险与回滚

MAS 共享树有既有改动；应用代码、默认配置、registry、真实库和旧验收数据均只读。不得将本任务号的设计完成等同于 C03 用户验收通过或 C04–C07 开工；不 commit/push，不写模型 memory。

如需撤回本次设计，仅处理本任务新增目录／任务文件及两份 INDEX 的本任务行，不还原整个共享索引、不删除旧 TASK-20260914-001 存档，也不对应用执行 reset。会话绑定如已转到本任务，按精确 session 路由调整；本次未执行删除。

## Amendment

### 2026-09-14 14:14 UTC · 文档收尾与恢复复核

本补记只收口本设计任务，不增加施工授权。恢复时未把自动摘要或 `wrong_repo` 注入当任务事实；先读取该 session 的实际绑定，确认 `TASK-20260914-002` 与设计总入口，再重开 README、三份设计稿、暂定内容基线及本任务记录。

| 最终检查 | 实际结果与边界 |
|---|---|
| 文档全写域 | 4 份设计稿＋本任务记录，共 5 份 Markdown、39 个本地链接，目标文件均存在；无替换字符、行尾空白，围栏配对。只核链接目标存在，不把来源真实性或教学效果计为通过 |
| 共享索引 | 两份 INDEX 分别只有 1 条本任务入口；以 `ledger_edit.py --check --expect-sha256` 比对前序最终写后值，均退出 0。handoff 保持纯 LF，task log 保持纯 CRLF；本段续作未再写索引，其全部字节与前序写后值一致，未覆盖非本任务内容 |
| 差分空白 | `git -c core.whitespace=cr-at-eol diff --check -- progress/decisions/two-desks-delta-20260914 progress/task_logs/2026/09/2026-09-14__research__two-desks-incremental-design-first-build.md progress/handoff/INDEX.md progress/task_logs/INDEX.md` 退出 0；未跟踪新文档另以上述文档检查覆盖 |
| 仓库复核 | 规划仓 `master`，HEAD `f9f42db39be4286e6275ffbeb636ffae53e1f23e`，本地跟踪 ahead 14，未 fetch；暂存区为空，既有共享改动保留。应用仓 `main`，HEAD `d53d188faff8e64ae9d22d92dd1eeab1b8309b84`，工作树干净 |
| 恢复绑定 | session `01a09aa5-24c1-7233-868b-7426b5d94476` 的绑定现为本任务，`bound_at=2026-09-14T14:08:20.740351+00:00`；路径 `progress/decisions/two-desks-delta-20260914/README.md`，锚点 `## 0. 授权、状态与恢复`。本段续作只读确认，未再修改绑定 |
| 恢复协议 | solver 预检通过；在绑定指明的 `/mnt/d/MyResearch/MAS_Safety_Project` 中手动调用既有 `context_recovery.py hook`，返回 `CONTEXT_RECOVERY_STATUS=VERIFIED / TASK-20260914-002`，随后重开授权链。此项只证明本次精确路径下的手动协议核对，不等于自然 hook 或其他 cwd 已验收 |
| 并发及独立证据 | 收尾代理状态显示仅主线程运行；既有子代理均为 429 失败。本段未新派发、不重试；独立设计复核仍未完成 |

共享索引最终值仅用于既有登记面保形／并发收尾协议，不新增通用 hash 质量门：

- `progress/handoff/INDEX.md`：`3755e26481f0ac3e59e2369df75024a9f8147032d0f20a4febdc82c8cf08b961`。
- `progress/task_logs/INDEX.md`：`9cca5529d7497cf502d99a3e01afee851bab749b412898e207b882c620059420`。

本任务文档交付与登记收尾完成，状态保持 `completed_with_open_gates`。未运行应用测试、服务、研究实验、部署、commit 或 push；没有修改应用、真实数据、用户答案或模型 memory。下一步仍是用户审阅科研 map／两台路径并决定首批 A 或 A＋B，B 的局部合同及 C03 用户反馈按方案另行确认。

### 2026-09-15 06:45 UTC · 继续请求后的 B 接口收敛

用户要求继续、尽量 2 并发并加快，随后要求不再纠缠 429、直接推进任务。本段继续完成既有设计缺口，未把这些消息扩大为已经批准 A／B 代码或关闭 C03 用户验收。

- 新增 `B_CONTRACT_PROPOSAL.md`，明确三个新增记录 kind、复用 Feedback、版本引用、窄查询入口、三条写路径的一致语义、跨工作区成员归属、`branch_origin` 和显式版本／视图导出；同步设计总入口、首批方案及两份索引的本任务行。
- 主线程静态确认三个实际遗漏：默认选最近更新 View 而非原 View；导出当前只读最新对象且自动包含工作区全部 View；Attempt／Feedback 的问题与尝试引用有同工作区约束。提案分别给出原视图显式选择、v2 选择式导出、原 Q 同身份成为分支成员的最小处置，不修改原合同正本。
- 子代理 `b_return_contract_review` 在被中断的回合后无可用终态证据；继续时只剩主线程，因此重新派发一个只读 `b_return_check`。后者明确返回 `429 Too Many Requests / exceeded retry limit`，无实质核验内容。随后停止派发与排查，由主线程收口；未将任一次派发计为独立 PASS，总运行并发未超过 2。
- 写后检查覆盖 5 份设计文档＋本任务记录，共 6 份 Markdown、52 个本地链接，目标均存在；无替换字符／行尾空白、围栏配对；本任务 scoped `git diff --check` 退出 0。两份索引各只有一条本任务入口，CAS 替换返回 VERIFY-OK，未调整其他任务行。
- `solver` 预检通过。应用仓仍为 `main@d53d188faff8e64ae9d22d92dd1eeab1b8309b84` 且干净，MAS 暂存区为空；未运行应用测试、启动服务、读写真实库、实验、提交、推送或写模型 memory。

本段索引写后值（仅用于既有保形编辑收尾）：handoff `679a312f6ffd7ffa9cfdba494bd4f2529e0faedd72895a78e7e3fbc700d5734f`；task log `798aee29abb32503b8753e0cfcd28d3d4a1211b5c32e99e34bf3be602fabbbfb`。收尾以 `ledger_edit.py --check --expect-sha256` 复验，不把前次 14:14 补记的值当作最新值。

当前可直接审阅 A → B 的分段范围及本次窄接口选择；不再以“还没定模型”为由扩展架构。若批准施工，另立实施任务并把获批约定转入实际 CONTRACT_DELTA；当前提案仍为 NOT-FROZEN。撤回本段只处理新增 B 接口稿及本任务文档／索引的对应增量，不重置共享树。
