# WP0 Codex 作业书预写（DRAFT 等门 4）＋施工方案 Codex 执行者适配

- **task_id**: `TASK-20260901-002`（8899 中央领号，发号回执「发出即占用，不回收」）
- **date**: 2026-09-01
- **type**: maintenance
- **status**: completed_with_open_gates
- **project**: dashboard-v3（工作台 v2 线，TODO `[topic:workbench-v2]` WB-1）
- **sessions**: 本窗（工作台重构设计窗，primary）

## 背景与授权

用户 2026-09-01 宣布施工执行者=Codex（原文逐字：「施工我准备用codex去做，所以才让你写施工方案、分工方案、流程图之类的」，已录施工方案 §7 依据行）；随后对「WP0 作业书可门 4 前预写、标 DRAFT 等门」的报价答复**「做」**——本任务即该口令的执行。

## 完成

1. **施工方案 v1 → v1.1**（`progress/decisions/2026-08-31__maintenance__workbench-v2-construction-plan.md`）：新增 §7 Codex 施工模式（7.1 三方分工／7.2 派工协议／7.3 天然异构 A/B／7.4 每 WP 施工流程图／7.5 顺序与首单）；§2 加降级注记（R1–R5 子代理编制=兜底）；Status 行升版。蓝图 html 门 4 卡同步注记。
2. **`tools/dashboard/_briefs/CODEX_BRIEF_WP0.md` DRAFT-v0.1 落盘**：§零 FINAL 化清单（7 项）＋§一 公共头八纪律（写域白名单／禁写区／禁 git 操作与 core.hooksPath／stdlib only／字节保形红线／三件套三元组报数／FAIL 纪律六字段回执／凭据卫生）＋§二 Lot A–E 切分（每 Lot 量化 PASS 判据）＋§三 全局验收门映射＋§四 回执模板＋§六 启动令。

## 锚点核验（铁律 1 证据）

- 契约 §4 表自带「M4 写门校验」列（存在性/迁移合法性/非空/as_of 新鲜度/append-only/primary 唯一/门不可跳过/非空），§5 状态机含硬规则——提案档已冻 v1（§14 拍板）。
- M4 三强制字段=`project`（slug 闭集拒收）/`output`（commit/artifact/decision/evidence/none 五枚举，none 附原因）/`decided_by`（user/default/overridden）；rollout=warn-only 先跑一周；严禁 core.hooksPath——`2026-08-28__maintenance__workbench-refactor-design-and-plan.md` §二.1＋M4 行＋A3 派工行；proposal 档 73 行当时即标「Codex 侧」。
- 测试三件套与三元组报数纪律=`dashboard-maintenance.md`（旧基线经壳跑 49/1/50 口径、golden 9 case 逐字节）。
- Codex 可行性先例：`TASK-20260830-005`（Codex 0.151.0 与 Claude 双端手动 compact 注入 VERIFIED）；作业书模式先例：`TASK-20260824-018`（孙线 SUN 作业书）＋鲁线 `CODEX_ACCEPTANCE_BRIEF_20260824.md`（输出面 `_codex_YYYYMMDD/` 冻结面外）。

## 未完成／开放门

- **门 4**（09-10 进组后用户开工口令）→ 执行作业书 §零 FINAL 化清单（基线三元组实测／worktree＋分支／锚 commit／DB gitignore／路由风格／WP0 施工任务号另领）→ 才可下发 Codex。
- commit 门：本批全部文件未 commit（需用户口令）；INDEX/TODO 行已保形写在盘、随下次登记面清算。
- WB-S（能力层插件化设计稿）仍待用户「做」的口令，与本单无关。

## 下一步

门 4 开启 → FINAL 化 CODEX_BRIEF_WP0 → 按施工方案 §7.4 流程发【启动令 WP0-A】。

## 回滚

删 `tools/dashboard/_briefs/` 目录与本 task log；`git checkout -- ` 施工方案与蓝图两文件（721c2e2 后增量即消）；INDEX/TODO 两行经 `ledger_edit.py` 反向删行（CAS）。
