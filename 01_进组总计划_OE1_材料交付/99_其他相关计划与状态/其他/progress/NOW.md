# NOW · 新窗口入口（自动生成）

> **本文件由 `tools/scripts/generate.py` 自动生成，请勿手改。** 生成于 2026-09-18T19:35:45-07:00

## 权威链口诀

1. 行动项真相：`progress/TODO.md`（七线分区）
2. 完成证据：`progress/task_logs/INDEX.md` + 具体 task log
3. 待拍板：`progress/decisions/PENDING.md`
4. 线定义/红线：`progress/lines/*.md`
5. 本页与 `STATUS.md` / `PROJECT_HOME.md` / `dashboard/*` 均为生成物，禁止反向覆盖 TODO

## 全局 · 36/149 完成 · 33 阻塞 · 32 待拍板

## 等你（用户动作/拍板）

- [research] OpenReview 5 条隐藏 ID 人工核验（唯一可能改变 T2 威胁评估的未知量） — 需登录态浏览器
- [research] Semantic Scholar API key 申请 + S2 面 6 条查询复扫 — 申请（免费，官网表单）→AI 复扫

## B+ 战况

- **战役**（4）：[CMP-BPLUS-IMPLEMENTATION](/progress/CAMPAIGNS.md#campaigns) 看板 B+ 任务模块实施 · unknown；[CMP-LU-FINISHING-WAVE](/progress/CAMPAIGNS.md#campaigns) 鲁线补齐波 · unknown；[CMP-OE1-EMAIL](/progress/CAMPAIGNS.md#campaigns) OE1 九月致鲁老师邮件定稿 · unknown；[CMP-JINZU](/progress/CAMPAIGNS.md#campaigns) 鲁线进组冲刺 · unknown
- **拍板**（32）：[DEC-BR6-W1B](/progress/decisions/PENDING.md) BR-6 后续是全量预授权、按 P1→P2→P3 逐门批准，还是停在 Wave 1A 估时未知；[DEC-BRIDGE-DORMANT-OR-ARCHIVE](/progress/decisions/PENDING.md) `bridge/` 跨领域方法论比对悬空状态是否现在正式判定为无限期搁置并归档 估时未知；[DEC-CX3-CODEX-GOAL](/progress/decisions/PENDING.md) 是否安装 Codex Goal 补丁并完成 CX-3 估时未知；[DEC-EA6L-P2](/progress/decisions/PENDING.md) 是否启动 EvoAgent 学习课程 Phase 2，以及选择扩展方向与投入范围 估时未知；[DEC-GA2-BRAINSTORM](/progress/decisions/PENDING.md) 何时明确触发双框架 MVP 脑暴 估时未知
- …另有 27 项

## 各线现状与下一步
### EvoAgent 作品集改造 + 学习 · `active` / P1
- **红线**：EA-4 未经用户拍板、未解除“不动 EvoAgent 代码”护栏前，不推进 PN 加载改造；静态审计结论不能冒充运行验证；当前源码、历史审计和摘要数字必须分开标口径；旧路径下的历史 prompt 基本不可变，只补路径变更说明；活档才真改引用
- **下一步**：
  - **EA-7.1** · G10 SSRF：fetch_diff 对 webhook 可控 URL 带 Bearer 外发 [P0] [blocked:待Phase1动仓对账·D1已批8-13]
  - **EA-7.2** · G11 多租户隔离缺口 ×3 [P0] [blocked:待Phase1动仓对账+S1波后单列]
  - **EA-7.3** · G7 500 兜底回显 str(exc) [P0] [blocked:待Phase1动仓对账·D1已批8-13]

### 科研主线（鲁组 + 方法论 + MCM 复盘） · `active` / P1
- **现状**：**ACTIVE（P1）**。鲁组 9 月报到在即；MCM 复盘收尾（方法论转素材，不维护代码）。
- **红线**：`D:\Code\MCM_2026` 是只读档案素材；不以复盘名义继续维护代码，不重跑已完成的 MV-1~5 / F030 / HV-1；MCM 的论文口径、当前产物口径和历史审计口径必须分栏，不把会话坐标冒充当前源码坐标；Sun 方向在重启条件满足前只做归档收尾，不恢复为现役科研主线
- **下一步**：
  - **BR-13** · 执行鲁组学习—谱系—迁移双层计划 [P0]
  - **ML-2** · 建立 MCM26 后台证据控制层（来源注册 + 口径主账 + 差分复审） [P0]
  - **W2-W3** · 修 Rank flip_rate 方向反转 [P0] [blocked:DEC-MCM-SOURCE-FIX]

### 对外/求职（9月鲁组邮件 · 简历 · 作品集展示） · `active` / P1
- **现状**：**ACTIVE（P1 · 9 月前）**。9 月邮件是硬节点。
- **红线**：对外数字必须回指已验证来源；不得混用 EvoAgent 的 18 编号问题、5+6+3 摘要分组和 60/约 50 P0 候选口径；MCM 的 SNR 已翻案为真实 metric；邮件、简历不得继续称其为包装词；本线不复制 EvoAgent / research 的执行任务；只消费经验证的展示素材
- **下一步**：
  - **OE-1** · 9 月鲁邮件 v4 定稿与投递（正式标题 + DL 工程素材 + 话术分支） [P1]
  - **OE-2** · 个人学术主页搭建（GitHub Pages） [P2]
  - **KG-1** · Kaggle 独立参赛线（Kaggriculture，Simulation 赛） [P2]

### 考研备考（2027.12 初试） · `paused` / P2
- **现状**：**PAUSED（远期目标）**。2027 年前不占前排，但标记常年在看板可见。
- **红线**：2027 年前不把远期备考占位包装成现役任务，不挤占当前科研、求职和基础设施前排；Sun 联系属于复试后的远期动作，不提前与当前鲁组线混写
- **下一步**：暂无未完成任务

### Casual 生活向项目（人机恋等） · `active` / P3
- **现状**：**ACTIVE（但低优先）**。属于"生活向"线，想推进时才推进，不占前排。
- **红线**：生活向工具和账号注册不冒充科研进展；低优先项目不挤占现役科研与求职节点；GA 双框架在前置输入和用户触发前保持 WAITING，不主动扩建模板或部署栈；涉及 token、App ID、健康权限或设备的动作必须由用户提供或授权
- **下一步**：
  - **GA-1** · 等调研 1（顶尖研究员知识管理体系）报告 [blocked:等背景调研]
  - **GA-2** · 用户叫脑暴后启动 MVP 雏形 [blocked:等 GA-1 + 用户触发]
  - **GA-3** · OpenClaw 部署形态选择 [blocked:等用户决策]

### 仓库与协作基础设施 · `active` / P2
- **现状**：**ACTIVE（持续维护）**。护栏 3/4 待做 · CX-3/4 待做 · V1 VPS 待拍板。
- **红线**：共享文件采用单写者 + 主控合并；生成器和 dashboard 产物由对应实现方与主控统一集成；`.git drvfs ro` 旧结论已推翻；不得再把工具沙箱边界写成文件系统只读事实；看板公网部署前必须有访问控制；当前 `app.py` 仅适合本机回环访问
- **下一步**：
  - **WB-1** · 工作台 v2 重构施工（WP0 已隔离 TECH-PASS；WP1+ 仍按原门推进） [P0]
  - **TQ-1** · TaskQuay fork 沙盒委派闭环与 GPT 接入方案 [P1]
  - **DB-2** · task_id 撞号治理（8-12 多窗并发历史冲突） [P1] [blocked:等 DEC-TASKID-DEDUP 拍板]

### 挂起学习 + 档案馆可复用 · `paused` / P3
- **现状**：**PAUSED（挂起集合）**。想重启某件时，移入对应业务线。
- **红线**：本文件只描述 pending 线，不保存可计数 checkbox；任务唯一主账是 `progress/TODO.md` 的 `line:pending` 分区；`D:\Code` 是只读档案馆，不做持续维护；复用某项时先迁入对应业务线再行动；挂起项不得因出现在叙事清单中被误计为重复任务
- **下一步**：
  - **VSM-1** · vsummary 本地模型字幕增强复测 [P3]
  - **PEND-RM-01** · 摘录"如何有效地读论文"
  - **PEND-RM-02** · 摘录"论文写作模板"

## 待拍板（摘要）

- **DEC-REUSE-ROLLOUT-E3** · EvoAgent rollout 若需 LLM key/联网是否放行 · `research`
- **DEC-SUN-EARLY-CONTACT** · 孙组套磁是否从 2027 提前到 2026 年 11-12 月 · `research`
- **DEC-S2-DASHBOARD-VPS** · 选择看板 VPS 机器、部署版本、同步方式与访问控制 · `infra`
- **DEC-EA6L-P2** · 是否启动 EvoAgent 学习课程 Phase 2，以及选择扩展方向与投入范围 · `evoagent`
- **DEC-CX3-CODEX-GOAL** · 是否安装 Codex Goal 补丁并完成 CX-3 · `infra`
- **DEC-V1-DUAL-VPS** · 是否采用双 VPS + 甲骨文 Always Free 拓扑 · `infra`
- **DEC-GA3-OPENCLAW-HOME** · OpenClaw 部署在 WSL2 本机、NAS 还是云端 · `casual`
- **DEC-GA5-MOBILE-BRIDGE** · 手机桥接选飞书、微信还是 Telegram · `casual`
- **DEC-GA2-BRAINSTORM** · 何时明确触发双框架 MVP 脑暴 · `casual`
- **DEC-M1-LOCAL-LLM** · SillyTavern 本地模型选择 llama、mistral 还是 qwen · `casual`
- **DEC-W3-MERGE** · 是否按 W3 合并建议卡执行主导航图 + 伴随索引卷收束，并采用导航层 F①-⑧ / 细分层父域·序号口径 · `research`
- **DEC-BR6-W1B** · BR-6 后续是全量预授权、按 P1→P2→P3 逐门批准，还是停在 Wave 1A · `research`
- …另有 20 项，见 `decisions/PENDING.md`

## 阻塞中

- **EA-6L-P2** · 课程扩展未批准
- **EA-6L-F1** · 先完成工作树归属与实验基线对账
- **EA-7.1** · 待Phase1动仓对账·D1已批8-13
- **EA-7.2** · 待Phase1动仓对账+S1波后单列
- **EA-7.3** · 待Phase1动仓对账·D1已批8-13
- **EA-7.4** · 待Phase1动仓对账·D1已批8-13
- **EA-7.5** · 待Phase1动仓对账·D1已批8-13
- **EA-7.6** · 待Phase1动仓对账·D1已批8-13
- **EA-7.7** · 待Phase1动仓对账·D1已批8-13
- **EA-7.8** · 待Phase1动仓对账·D1已批8-13
- **EA-7.9** · 待Phase1动仓对账·D1已批8-13
- **EA-7.10** · 待Phase1动仓对账·D1已批8-13
- **BR-10** · DEC-R0-IMPL-GO + EvoAgent 009/024 收口 commit
- **SA-4** · 等 SA-1~3
- **W2-W3** · DEC-MCM-SOURCE-FIX
- **W3** · DEC-MCM-SOURCE-FIX;DEC-MCM-ERRATA
- **W4** · DEC-MCM-SOURCE-FIX;DEC-MCM-ERRATA
- **W4-W5** · DEC-MCM-WHITELIST;DEC-MCM-DEADCODE
- **W6+** · DEC-MCM-SOURCE-FIX;DEC-MCM-ERRATA
- **GA-1** · 等背景调研
- **GA-2** · 等 GA-1 + 用户触发
- **GA-3** · 等用户决策
- **GA-4** · 等 GA-3
- **GA-5** · 等 token/App ID
- **C1/C2/C3** · 等账号
- **E1/E2** · 等硬件与权限
- **M1/M2/M3** · 等本地模型选择
- **CX-3** · 等用户决定 Codex Goal 补丁
- **CX-4** · 等 CX-3
- **DB-2** · 等 DEC-TASKID-DEDUP 拍板
- **DS-1** · 等非 WSL2 环境
- **V1** · 等用户拍板与沙箱外实操
- **TG-1** · 等一次 Codex 长任务实证

## 最近死线

- **BR-1** · 2026-08-31 · -18 天
- **TR-1** · 2026-09-30 · 12 天
- **BR-2** · 2026-12-31 · 104 天
