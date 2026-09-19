# Skill 索引

**最后更新**：2026-05-22
**用途**：统一管理所有 skill，按科研阶段分类，支持退役机制

---

## 核心 skill（永不归档）

| Skill | 位置 | 用途 | 触发 |
|-------|------|------|------|
| PAPER_READING | ~/.claude/skills/paper-reading/ | 统一精读框架（5 Stage + 8 子模块，融合 PAPER_READING+PDF_DEEP_READ+ANALYSIS_FRAMEWORK） | 给 PDF / "读论文" |
| WRITING_INTEGRATION | tools/ai/ | 写作 6 检查点（骨架/段落/自审/多Agent/终审/Rebuttal） | "写论文" / "自审" |
| AUDITOR | tools/ai/ | 事后审查（5 维度） | 自动触发 |

## 科研体系整合入口（不是新的自动 skill）

| 文档 | 位置 | 用途 | 触发 |
|---|---|---|---|
| 三源科研体系整合卡 | `方法论/科研体系三源整合_20260904.md` | 将 Luo PDF、Supervisor-Skills、pengsida 与当前 OS 连接为“来源→适配→用户证据”流程 | 读论文 / 设计小实验 / 准备汇报 |

## P0 skill（选题 + 解题 + 实验）

| Skill | 位置 | 用途 | 触发 |
|-------|------|------|------|
| GAP_TO_IDEA | tools/ai/ | 找 Gap + 生成 idea | "找 gap" |
| DIRECTION_REFINE | tools/ai/ | 方向精炼（问题锚定 + 新颖性验证） | "精炼方向" |
| TASTE_CULTIVATION | research_growth/方法论/skills/ | 研究品味培养（4 条路径 + 日常练习） | "值不值得" / "品味" |
| PROBLEM_SOLVING | research_growth/方法论/skills/ | 第一性原理 + 问题拆解 + 跨域迁移 | "怎么解" / "设计方案" |
| TRANSFER_AUDIT | research_growth/方法论/迁移审计协议_20260905.md | 源机制证据 + representation + decision delta + 最小证伪 | "这个能迁移吗" / "这两个很像" / "迁移审计" |
| EXPERIMENT_DESIGN | research_growth/方法论/skills/ | 最小可行性 + 探索性实验设计 | "实验设计" |
| DEBUG_METHODOLOGY | research_growth/方法论/skills/ | 找不 work 原因（5 步）+ 调试九法 | "debug" / "不work" |

## P1 skill（投稿 + 导师）

| Skill | 位置 | 用途 | 触发 |
|-------|------|------|------|
| PRE_SUBMISSION_AUDIT | tools/ai/ | 投稿前审查（引用完整性 + claim 对齐） | "终审" / "投稿" |
| SUPERVISOR_GUIDE | tools/ai/ | 导师沟通（信号解读 + 消息模板） | "导师沟通" |
| SUPERVISOR_PACK | tools/ai/ | 导师汇报打包 | "汇报" |

## P2 skill（成长 + 代码）

| Skill | 位置 | 用途 | 触发 |
|-------|------|------|------|
| GROWTH_TRACKER | research_growth/方法论/ | 成长追踪（5 维度趋势 + 想法孵化器） | "成长" / "进步" |
| CODE_LEARNING | research_growth/方法论/skills/ | 任务驱动学代码 + 代码整洁之道 | "学代码" / "看代码" |

## 季节性 skill（豁免退役，按需激活）

| Skill | 位置 | 激活时机 |
|-------|------|----------|
| PRE_SUBMISSION_AUDIT | tools/ai/ | 投稿前 |
| PRESENTATION | research_growth/方法论/skills/ | Slides + Demo + Project Page + 画图/画表 | "做slides" / "project page" |

## 辅助 skill（审查 + 合成 + 知识库）

| Skill | 位置 | 用途 | 触发 |
|-------|------|------|------|
| REVIEW_PROTOCOL | tools/ai/ | 方向审查 D1-D6 | "方案评估" |
| BREAKDOWN_REVIEW | tools/ai/ | 单篇拆解审查 B1-B6 | "拆解审查" |
| CROSS_PAPER_SYNTHESIS | tools/ai/ | 跨论文合成 | "跨论文合成" |
| EXTRACT_MATRIX_DATA | tools/ai/ | 矩阵数据提取 | "提取矩阵" |
| PDF_QUICK_SCAN | tools/ai/ | 5 分钟快筛 | "快筛" |
| PDF_DEEP_READ | tools/ai/ | 8 层精读框架 | "精读" |
| _REVIEW_TOOL | tools/ai/ | 115 条安全措施 | 自动 |
| kb-context | .claude/skills/ | KB 上下文注入（检索相关论文） | "找相关论文" / "KB 上下文" |
| cross-disciplinary-insight | .claude/skills/ | 跨学科洞察（跨领域类比） | "跨学科分析" / "找类比" |
| cross_track_insight | tools/kb/ | 跨轨道洞察（Jiang↔Sun） | "跨轨道洞察" |
| dual_agent_review | tools/kb/ | 双 Agent 迭代审查 | "双 Agent 审查" |

---

## Skill 间数据流

```
选题阶段：
PAPER_READING §4 → GAP_TO_IDEA → DIRECTION_REFINE → TASTE_CULTIVATION

解题阶段：
PROBLEM_SOLVING → REVIEW_PROTOCOL

实验阶段：
EXPERIMENT_DESIGN → DEBUG_METHODOLOGY → CODE_LEARNING

写论文阶段：
WRITING_INTEGRATION → research-paper-writing

投稿阶段：
PRE_SUBMISSION_AUDIT → SUPERVISOR_GUIDE → SUPERVISOR_PACK

成长追踪：
GROWTH_TRACKER（每 5 篇论文更新）
```

---

## 退役规则

- **核心 skill**（PAPER_READING, WRITING_INTEGRATION, AUDITOR）：永不归档
- **非核心 skill**：8 周没出现在 PROGRESS_DASHBOARD.md 的"最近使用 skill"表中 → 自动归档
- **季节性 skill**（PRE_SUBMISSION_AUDIT, PRESENTATION）：豁免退役，按需激活
- **归档位置**：`_ARCHIVED_SKILLS.md`
- **恢复方式**：说"恢复 [skill name]"即可
