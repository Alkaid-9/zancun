# PROJECT HOME · 项目总览

> **自动生成，请勿手改** · 生成于 2026-09-18T19:35:45-07:00
> 数据源：`progress/TODO.md`、`progress/lines/`、`progress/decisions/PENDING.md`、`progress/task_logs/INDEX.md`

## 全局进度
- 完成：**36/149（24%）**
- 待办：**113** · 阻塞：**33** · 待拍板：**32**
- 逾期：**1** · 本周到期：**0**

## 七线总览
| 业务线 | 状态 | 进度 | 下一步 |
|---|---|---:|---|
| **EvoAgent 作品集改造 + 学习** | active | 9/23 (39%) | G10 SSRF：fetch_diff 对 webhook 可控 URL 带 Bearer 外发；G11 多租户隔离缺口 ×3；G7 500 兜底回显 str(exc) |
| **科研主线（鲁组 + 方法论 + MCM 复盘）** | active | 17/62 (27%) | 执行鲁组学习—谱系—迁移双层计划；建立 MCM26 后台证据控制层（来源注册 + 口径主账 + 差分复审）；修 Rank flip_rate 方向反转 |
| **对外/求职（9月鲁组邮件 · 简历 · 作品集展示）** | active | 0/3 (0%) | 9 月鲁邮件 v4 定稿与投递（正式标题 + DL 工程素材 + 话术分支）；个人学术主页搭建（GitHub Pages）；Kaggle 独立参赛线（Kaggriculture，Simulation 赛） |
| **考研备考（2027.12 初试）** | paused | 0/0 (0%) | — |
| **Casual 生活向项目（人机恋等）** | active | 0/8 (0%) | 等调研 1（顶尖研究员知识管理体系）报告；用户叫脑暴后启动 MVP 雏形；OpenClaw 部署形态选择 |
| **仓库与协作基础设施** | active | 10/29 (34%) | 工作台 v2 重构施工（WP0 已隔离 TECH-PASS；WP1+ 仍按原门推进）；TaskQuay fork 沙盒委派闭环与 GPT 接入方案；task_id 撞号治理（8-12 多窗并发历史冲突） |
| **挂起学习 + 档案馆可复用** | paused | 0/24 (0%) | vsummary 本地模型字幕增强复测；摘录"如何有效地读论文"；摘录"论文写作模板" |

## 待拍板
- **DEC-REUSE-ROLLOUT-E3** · EvoAgent rollout 若需 LLM key/联网是否放行
- **DEC-SUN-EARLY-CONTACT** · 孙组套磁是否从 2027 提前到 2026 年 11-12 月
- **DEC-S2-DASHBOARD-VPS** · 选择看板 VPS 机器、部署版本、同步方式与访问控制
- **DEC-EA6L-P2** · 是否启动 EvoAgent 学习课程 Phase 2，以及选择扩展方向与投入范围
- **DEC-CX3-CODEX-GOAL** · 是否安装 Codex Goal 补丁并完成 CX-3
- **DEC-V1-DUAL-VPS** · 是否采用双 VPS + 甲骨文 Always Free 拓扑
- **DEC-GA3-OPENCLAW-HOME** · OpenClaw 部署在 WSL2 本机、NAS 还是云端
- **DEC-GA5-MOBILE-BRIDGE** · 手机桥接选飞书、微信还是 Telegram
- **DEC-GA2-BRAINSTORM** · 何时明确触发双框架 MVP 脑暴
- **DEC-M1-LOCAL-LLM** · SillyTavern 本地模型选择 llama、mistral 还是 qwen
- **DEC-W3-MERGE** · 是否按 W3 合并建议卡执行主导航图 + 伴随索引卷收束，并采用导航层 F①-⑧ / 细分层父域·序号口径
- **DEC-BR6-W1B** · BR-6 后续是全量预授权、按 P1→P2→P3 逐门批准，还是停在 Wave 1A
- **PEND-RESTRUCT-1** · MAS 深度重构时是否归档 MAS 根与 progress 双 `.obsidian` 配置，只保留 MyResearch 根 vault
- **PEND-RESTRUCT-2** · MAS 深度重构 P1 的执行时点
- **DEC-MCM-SOURCE-FIX** · 是否解除 MCM 归档仓只读边界，修复 N1-N8 源码缺陷
- **DEC-MCM-RECOMPUTE** · 源码修复后是否重算受污染的 M001-M005/M007-M009，并对 M006 做性能回归
- **DEC-MCM-PUSH** · 是否 push MCM 仓 `50c4578` + `ceff63f`，以及 MAS 当前分批 commit/push
- **DEC-MCM-WHITELIST** · Track E 的 15 条白名单候选删/留裁决
- **DEC-MCM-DEADCODE** · 是否执行 MCM 死代码清理 wave
- **DEC-MCM-M004-E3** · 是否授权 E3 重跑 survival 段以终判 M004 infinite
- **DEC-MCM-ERRATA** · 是否输出论文侧勘误清单/队友报告
- **DEC-OE1-WINDOW-SLIP** · OE-1 邮件原定投递窗口(9-15)已过期+BR-1(NSFC放榜复查)逾期16天从未执行，如何处理
- **DEC-PROPOSAL-NOTES-PATH** · `proposal-notes.md` 死链指针核实：文件到底在哪，还是从未创建
- **DEC-BRIDGE-DORMANT-OR-ARCHIVE** · `bridge/` 跨领域方法论比对悬空状态是否现在正式判定为无限期搁置并归档
- **DEC-SCHOLAR-ALERT-SETUP** · 是否现在设置鲁法明+EdgeIM相关作者的轻量学术更新订阅（Scholar Alert/关键词订阅）
- **DEC-T5-NUMBERING** · "T5"编号双用消歧：companion 提案改 T6（A）/ bridge 协议 PN 验证改号（B）/ 维持双横幅限定词（C，现状）
- **DEC-R0-IMPL-GO** · 是否授权 R0 修复三波实施开工（BR-10）
- **DEC-LU-U3-L2-PROP-A** · L2 命题甲百行级实验是否立项(L2/L4 路线分歧唯一实证解法)
- **DEC-LU-U4-SUN-NAMING** · 作者名称口径最终采信(Jun Sun(SMU)/孙猛(PKU,ReGA)/Meng Sun(PKU) 三分 vs 两人合并)
- **DEC-LU-U5-FOCUS-P1** · FOCUS/WINDOW_PLAYBOOK 的 P批1 行是否刷新一句(补齐波已完成事实回写)
- **DEC-WB-LIGHTLOAD** · 轻量开工装载机制(N1)是否立项设计:启动减重＋开工前"本窗 skill/工具选装声明"(装载画像)
- **DEC-WB-PROJ-HUB** · 控制面×可视化工作台×日志&待办按项目联动(N2)是否立项设计
