# 工作台 v2 设计窗 · 关窗交接档（窗口工作总结）

**Date**: 2026-08-31 深夜 ～ 2026-09-01（关窗令：09-01）
**Type**: handoff（本窗关窗状态权威＝路由与总结；各项**语义**权威仍是下文 §三 所列决策档，冲突以决策档为准）
**窗口身份**: 工作台 v2 重构设计窗（纯纸面设计窗：契约谈判→冻结→施工包→作业书→WB-S；8899 工作台代码**零改动**）
**所属线**: 看板/工作台线（项目卡=`progress/projects/dashboard-v3.md`；TODO 挂点=`[topic:workbench-v2]` WB-1 块，位于 [line:infra] 段）；旁支产出挂 [line:infra]（research_growth 第三仓）
**起草**: `TASK-20260901-006`（8899 领号）；授权=用户 2026-09-01 关窗令逐字：「存档目前的窗口的工作总结、工作日志、已完成、未完成，目前进度，以及对应的交接文档，属于哪一条线等等……接下来的plan和架构说明、使用手册、维护手册也要写。」

---

## 一、一句话结果

**Task 统一契约 v1 已冻结，施工全套图纸与两份 Codex 作业书已预写并入库，WB-S 技能注册表已批准并入施工方案 v1.2，research_growth 素养库已建第三仓并推私有远端——WP0 开工唯一等待的东西是门 4（09-10 进组后用户口令）。**

## 二、已完成（工作日志逐条溯源：任务号 → 内容 → 产物 → 入库位置）

| 任务号 | 内容 | 关键产物 | 入库 |
|---|---|---|---|
| `TASK-20260901-001` | 契约 v1 冻结批量执行（§8 八项+O1–O7+§13 拍板落账，授权=08-31「先做吧」） | 提案档 §14 拍板记录；施工四件套；蓝图 html；archive-1/2/3/4 | commit `721c2e2`（九档） |
| `TASK-20260901-002` | 施工执行者=Codex 适配（施工方案 §7：三方分工/派工协议/异构 A/B/流程图）＋WP0 作业书预写 | `tools/dashboard/_briefs/CODEX_BRIEF_WP0.md`（DRAFT-v0.1，Lot A–E） | commit `02da69b` |
| `TASK-20260901-003` | WB-S 能力层插件化设计稿（SKILL-MANIFEST 注册表；三源实测 77+≈17+39+5） | `decisions/2026-09-01__maintenance__workbench-v2-skill-registry-design.md` | commit `02da69b` |
| `TASK-20260901-004` | WB-S §9 五项拍板落账（「冻结，都接受」）＋并入施工方案 v1.2 作 WP-S＋WPS 作业书预写＋批量 commit | 设计稿 §10；方案 v1.2；`CODEX_BRIEF_WPS.md`；archive-1(09-01) | commit `02da69b`（9 档 559 行） |
| `TASK-20260901-005` | research_growth 素养库持久化（方案 A「可行。A吧？」＋远端「批」） | 第三仓：`main`，根提交 `5c22554`＋子模块注册 `22ace3d`；远端=`github:Alkaid-9/Research_Learning`（私有，push 前三重门实测过，post-push 未认证 404 确认） | 仓侧已推；MAS 侧 task log 随本次清算入库 |
| `TASK-20260901-006` | 本关窗批：交接档＋架构/使用/维护三手册＋素养库仓手册 | 本档＋`runbooks/workbench-v2-{architecture,user-guide,maintenance}.md`＋`runbooks/research-growth-repo.md` | 随本次登记面清算批入库（不 push） |

窗口起点上下文：08-31 深夜产品模型对齐检查点＝`decisions/2026-08-31__maintenance__workbench-product-model-alignment-checkpoint.md`（§14–§16）。task log 全文在 `progress/task_logs/2026/09/`，索引入口按 `TASK-20260901-001` 至 `TASK-20260901-006` 检索 `progress/task_logs/INDEX.md`。

## 三、设计与架构档案总清单（语义权威指针）

| 档 | 路径（progress/decisions/ 下，另注除外） | 版本状态 |
|---|---|---|
| **契约提案档**（数据脊柱 §4 十字段/§5 状态机/O1–O7/§13 科研挂载/§14 拍板） | `2026-08-31__maintenance__task-unified-contract-v0-proposal.md` | **CONTRACT-v1-FROZEN** |
| **施工方案**（WP 切分/验收 7 门/产物/UI 规范/排期/**§7 Codex 分工=分工方案权威**） | `2026-08-31__maintenance__workbench-v2-construction-plan.md` | **PLAN-v1.2**（含 WP-S） |
| **蓝图**（可视化渲染视图，浏览器直开） | `2026-08-31__maintenance__workbench-v2-blueprint.html` | 与 v1.2 同步 |
| **WB-S 设计稿**（manifest schema 12 字段/数据流/试点三卡/§10 拍板） | `2026-09-01__maintenance__workbench-v2-skill-registry-design.md` | **DESIGN-v1-FROZEN** |
| **WP0 作业书**（Lot A–E＋公共头八纪律＋§零 FINAL 化 7 项） | `tools/dashboard/_briefs/CODEX_BRIEF_WP0.md` | DRAFT-v0.1（等门 4） |
| **WP-S 作业书**（S1–S3＋ARIS 零写入红线） | `tools/dashboard/_briefs/CODEX_BRIEF_WPS.md` | DRAFT-v0.1（等 P1 排期） |
| 对齐检查点 / 用户原文存档 | `…workbench-product-model-alignment-checkpoint.md`；archive-1/2/3/4（08-31）＋archive-1（09-01） | 已入库 |
| **三本手册**（本批新增，见 §六） | `progress/runbooks/workbench-v2-{architecture,user-guide,maintenance}.md` | RUNBOOK-v1 |

## 四、未完成与门清单（十项；含本轮已清项）

1. **门 4 开工令**（解锁者=用户，09-10 进组后）→ 触发 WP0 作业书 §零 FINAL 化＋首单下发。
2. **WP-S 排期门**（P1 与 WP5 同期；前置=WP0 验收）→ 届时 WPS 作业书 FINAL 化。
3. **四仓复核窗 R07 豁免**（Keelson/Wegent/NotEMD/LearnGraph；需用户点名并记 overridden）——影响 WP2 任务现场栏目与 P1 关系视图细节，不阻塞 WP0。
4. **C-P0 压缩专项 §-2 四拍板点**（用户已排序在工作台后；多选题，只调 WP3 注入参数）。
5. **MAS 两仓 push**（从未授权；外仓另有三重门）。
6. **已清：登记面清算 commit**（解锁者=用户本轮「找一下相关的文件并且执行」）：只采收 TODO 的 TASK-005/WB-1 行、task log INDEX 的 001-006 行、handoff INDEX 的本窗路由、task log 005/006、本档与四本 runbook；`PENDING.md` 及三面内他窗 hunks 明确排除；不 push。
7. **PENDING.md 两张 08-22 工作台老卡**（`DEC-WB-PROJ-HUB` 疑似被契约 v1 覆盖、`DEC-WB-LIGHTLOAD` 与 WB-S L2 注入部分重叠）——销账等用户口令，本窗零触碰。
8. **WB-S 第五源扩项**（research_growth 三件方法资产进注册表扫描面）——未批；批后记入 WPS 作业书 §零。
9. **Bridge 侧回传三件**（队列中，属 Bridge 窗）：Git_UI_Pro 0.1.35→0.1.48 stale、Tier A vs TIER-B-PROPOSED、Supervisor-Skills per-skill license 分裂确认。
10. 蓝图内示意数据（收件箱 mock 卡片）为演示占位，建成后以真数据渲染——非缺陷，注记备查。

## 五、目前进度（门梯视图）

```text
门1 commit ✅(721c2e2/02da69b)  门2 拍板 ✅(§14+§10)  门3 R07豁免 ⏳需点名
门4 开工 ⏳09-10 ─► P0(WP0→WP1/WP2→WP3) ─► 用户验收 ─► P0.5(WP4)
─► 四仓复核窗(豁免后) ─► P1(WP5＋WP-S 同期) ─► P-06(WP6 拓扑)
```

## 六、接下来的 plan（时间轴）

- **09-10 前**：不开工（R07 周配额，止损类窗除外）。可选拍板项（均一句话可清）：PENDING 两卡销/留、WB-S 第五源扩项批/驳、R07 豁免点名、C-P0 四项选择题。
- **09-10 进组后**：① 用户门 4 口令 → ② 主控过 WP0 作业书 §零 FINAL 化 7 项（实测基线三元组、建 worktree `feat/wb2-wp0`、领施工任务号、钉锚 commit）→ ③ 发【启动令 WP0-A】→ ④ 按施工方案 §7.4 流程循环走完 Lot A–E（Codex 施工→六字段回执→Claude 异构 A/B 审→任一 FAIL 重派→双 PASS 采收登记→用户 accepted→commit 门）→ ⑤ WP1/WP2 双 Codex 会话并行（写域不相交）→ WP3 → **用户验收 P0**。
- **P0 后**：WP4（P0.5 门控台）→ 四仓复核窗 → WP5＋WP-S（P1 同期）→ WP6（P-06 拓扑）。全程 C-P0 四项只调 WP3 参数，不阻塞。
- 操作细节见 `runbooks/workbench-v2-user-guide.md`（用户动作）与 `-maintenance.md`（主控动作）。

## 七、新窗恢复协议

读序：**本档 → `progress/NOW.md` → 契约提案档 → 施工方案 v1.2 →（若开工）对应 CODEX_BRIEF**。纪律六条：task_id 必 8899 领号；TODO/INDEX/handoff-INDEX 只走 `ledger_edit.py` CAS 保形写（INDEX=CRLF、TODO=LF）并收尾钉哈希；改手改源后必跑 `generate.py`，生成视图（NOW/STATUS 等）禁手改；commit 逐批等口令、push 另有三重门、amend 前验 HEAD 全哈希；压缩恢复以盘为准不信摘要（[[compaction-ground-truth-disk]] 教训）；引用任务号先 grep INDEX 核实（铁律 1）。

## 八、research_growth 第三仓速查

路径 `/mnt/d/MyResearch/research_growth`；`main`；远端 `git@github.com:Alkaid-9/Research_Learning.git`（私有）；两提交（`5c22554` 全量快照＋`22ace3d` 子模块注册，MIT 子仓上游公开）；外仓 `/*` 规则原生忽略，零冲突。使用与维护全文=`progress/runbooks/research-growth-repo.md`。

---

*关窗交接档 · 2026-09-01 · 起草=TASK-20260901-006 · 本档与四本 runbook 随本次登记面清算批入库（不 push）· 收尾账本哈希见 task log 006*
