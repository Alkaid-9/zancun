# ra28 训练包 · 操作手册(Plan / 架构 / 使用 / 维护)

**Date**: 2026-08-12 21:14 · ra28 窗主控落盘
**定位**: 操作层文档——回答"接下来怎么用这套东西"。机制与规则的权威仍是 `KICKOFF.md`(窗口协议)/ `BRIEF.md`(题面 rubric)/ `../00_SYSTEM.md`(总纲),本档不复制只指针。
**当日全程日志与溯源**: `progress/handoff/2026-08-12__ra28-training-window__handoff.md`(交接档,含逐时刻证据链)
**任务记录**: `TASK-20260812-026(ra28/EX-05 代做降级)` → `progress/task_logs/2026/08/2026-08-12__research__ra28-ex05-delegated-execution.md`

---

## §1 接下来的 Plan(三条路径,按训练价值排序)

### 路径 1 · 完整训练闭环(推荐,时间充裕时)

```
逆向 review EX-05 patch(90 min,降级等价练习,LEDGER 已挂行)
  → 补做 EX-01(90 min,基线 25 finding 已密封)
  → EX-02(90 min,verdict 基线在产)
  → EX-03(90 min,三雷+症状报告就绪)
  → EX-04(60-90 min,参考基线 18 论点已密封)
  → 每题交付后主控派 Grader 批改 → 复盘 → 铸卡 → LEDGER
```

- 逆向 EX-05 的现成入口 = 代做回执 3 条 review 重点:①时间戳在上板时打而非构造时打的取舍;②导出失败静默降级(warning+吞异常)的权衡;③驱动脚本绕过 `__init__` 注入替身的耦合问题。
- 首铸卡点不变:EX-01《盲 review 操作程序》、EX-02《判断代码 work 五步》、EX-03《系统化 debug 五步》→ `../methodology/` + INDEX 登记。

### 路径 2 · 产出优先(时间紧张时)

放弃部分训练价值,直接收割产出:

1. 拍板开封 `_sealed/EX-01_answer.md` → 25 条 finding 按严重度 triage → 真 P0/P1 走正式修复(BRIEF §6:正常 patch 流程 + 领号记 task_log)→ mindbridge 作品集质量叙事升级("系统 review 过并修复")。
2. EX-04 密封参考(18 论点)可直接作作品集"架构决策"样本的底稿——但注意:那是 AI 观点,署名使用前你必须自己改写并至少过一遍反方论证,否则作品集叙事失真。

### 路径 3 · 研究线优先(9 月邮件驱动)

本窗跨包交付已完成,ra26 窗可立即开工:`research/pm4py_toy/data/` 双 trace 源(EvoAgent XES 编排拓扑 + mindbridge JSONL 黑板拓扑)→ PM4Py 流程发现 + conformance 对照 → "黑板 vs 编排拓扑对照"小结果 → OE-1 九月邮件(due 9-10)素材。此路径不依赖本窗任何未完项。

**三径不互斥**:建议 路径 3(ra26 窗并行开工)+ 路径 1 或 2 择一(视本周剩余时间)。

## §2 架构说明(本窗建成了什么)

### 2.1 产物地图

```
learning/training/ra28-mindbridge/
├── KICKOFF.md / BRIEF.md          ← 协议层(协调窗建,勿改)
├── OPERATIONS.md                  ← 本档(操作层)
├── EX-03/symptom-{1,2,3}.md       ← 做题输入:三份症状报告(Setter-3)
├── EX-05/logs/scenario-*.jsonl    ← 三场景事件 log(75/87/87 行)
├── EX-05/format_design.md         ← 四字段语义 + PM4Py 映射 + mock 边界 + 回滚表
└── _sealed/                       ← 密封区(开封条件见 §3.4)
    ├── EX-01_answer.md   27.4KB  finding 25 + 承诺表 29(Setter-1)
    ├── EX-02_answer.md   21.4KB  verdict 19 + 分诊 29(Setter-2,含 sqlite+mock 实测)
    ├── EX-03_answer.md    7.9KB  三雷根因+触发命令+最小修复(Setter-3)
    ├── EX-04_reference.md 13.4KB 参考评审 18 论点 + 追问弹药 6(Setter-4)
    ├── EX-05_reference_patches/   format-patch ×4(EX-05 Agent 冗余备份,分支误删可恢复)
    ├── ENV_NOTES.md               冒烟报错摘要(EX-02 素材)
    └── smoke_uvicorn_2026-08-12.log

research/pm4py_toy/data/           ← 跨包交付(ra26 消费)
├── scenario-{chat,consult,risk}.jsonl + README_mindbridge_logs.md
└── (ra26 自有 EvoAgent XES 12 件)

D:\Workspace\mindbridge(git 仓,master @ 9e1e239)
├── master                         ← 基线快照,永远可跑,勿直接改
├── training/ex03                  ← 3 个雷 commit(90fc126/5458dfb/c9f69a4)
└── training/ex05-event-export     ← 4 个 patch commit(1f16fda/3bf2d7a/1bf1ea7/7d7fe18)
```

### 2.2 多 Agent 分工与执行实况(全部后台子代理,零剧透回执)

| Agent | 状态 | 产物 | 隔离方式 |
|---|---|---|---|
| Setter-1 | ✓ 20:31 | EX-01 密封答案 | 只读主仓 |
| Setter-2 | ✓ 21:16 | EX-02 verdict 基线(19 verdict/29 分诊) | 只读主仓+跑实验,不装服务不改仓 |
| Setter-3 | ✓ 21:06 | ex03 三雷+症状+根因 | worktree `/tmp/mindbridge-ex03`(已清理) |
| Setter-4 | ✓ 21:04 | EX-04 参考评审 | 只读双仓(mindbridge+EvoAgent) |
| EX-05 代做 | ✓ 21:08 | patch 分支+log+格式档 | worktree `/tmp/mindbridge-ex05`(已清理) |

角色机制(Coach/Grader/主控纪律)见交接档 §5.2 与 BRIEF §3,不复制。

## §3 使用手册(逐场景)

### 3.1 做题(EX-01/02/04)

对主控说"开始 EX-NN"→ 主控起 90 分钟计时 + 复述禁读清单 → 交付物写 `EX-NN/` → 到点或提前说"提交"→ 主控派 Grader(输入=你的交付物+密封档+rubric)→ 批改单(召回/误报/过程分+3 条差距)→ 复盘一页 → LEDGER 行 + 触发铸卡。卡死说"卡死",Coach 按 H1→H2→H3 逐级解锁(记级别,不跳级)。

- **EX-01 注意**:先 20 分钟只读 README 产承诺表,再读码;Setter-1 通知曾泄露一条线索(交接档 §2 20:36 行),自评时声明即可。
- **EX-02 注意**:服务起不来本身是题面素材;你的实验环境=Setter-2 的实验环境(都不许装服务),对账才公平。
- **EX-04 注意**:交付后 Grader 会拿密封弹药库做三轮追问,提前想好黑板模式的坏处(反方 30% 权重)。

### 3.2 做 EX-03(故障排查)

```bash
cd /mnt/d/Workspace/mindbridge && git switch training/ex03
# 读 EX-03/symptom-{1,2,3}.md,逐雷:复现→缩小→假设→验证→根因→最小修复+回归
# 交付 EX-03/debug-N.md(排查日志+根因+diff+回归证据);修完 git switch master
```

雷各自独立 commit,可 `git log master..training/ex03` 看边界(commit message 中性无剧透)。**最小修复,顺手重构是扣分项**(rubric)。

### 3.3 逆向 review EX-05(降级等价练习)

```bash
git -C /mnt/d/Workspace/mindbridge log -p master..training/ex05-event-export  # 看 4 个 commit 全 diff
```

读 `EX-05/format_design.md` → 对 3 条 review 重点逐条表态(接受/要改+理由)→ 产一页 review 意见(建议格式:finding 编号/严重度/坐标/理由/建议修法)→ 交主控,主控以"patch 作者"身份回应,你体验 reviewer 视角 → 复盘写"两边坐过之后对 review 的理解变化"(BRIEF EX-05 反思项)→ LEDGER 行补全。

### 3.4 密封区开封规则

| 时机 | 谁 | 开什么 |
|---|---|---|
| EX-NN 交付后 | Grader | 对应 `EX-NN_answer/reference` |
| 用户拍板走路径 2 | 主控(记 task_log) | `EX-01_answer.md` 直接转修复清单 |
| EX-02 做题前 | 谁都不开 | `ENV_NOTES.md` 与 smoke log 是 EX-02 素材,同样禁读 |

### 3.5 ra26 窗接数据

读 `research/pm4py_toy/data/README_mindbridge_logs.md` 即可,字段语义与 pandas→PM4Py 转换示例在 `format_design.md`。两处 log 已核行数一致,以 `pm4py_toy/data/` 副本为消费入口。

## §4 维护手册

### 4.1 环境

- venv:`mindbridge-py/.venv`(Linux 布局 py3.10,13 依赖已装)。重建:`.venv/bin/pip install -r requirements.txt`(NTFS 上约 10 分钟)。
- 冒烟预期:`uvicorn app.main:app` 起不来(缺 MySQL/Redis/Ollama)属正常态,**不要修**(EX-02 素材)。离线跑三场景用 `scripts/run_event_export_scenarios.py`(ex05 分支,mock provider,无需外部服务)。
- 已知坑:drvfs/NTFS 写入慢;zsh 多 glob 有一个不匹配整条命令失败;`/tmp` 是 WSL 易失区,持久产物勿放(smoke log 已固化进 `_sealed/`)。

### 4.2 git 分支纪律

- `master` 永远可跑,基线 9e1e239;两个 training/* 分支**不要 merge 回 master**(ex03 含故意缺陷;ex05 等 review 结论后再定,回滚说明在 format_design.md 回滚表)。
- 若需重置训练场:`git branch -D training/ex03 && 重派 Setter-3`(产物覆写幂等);EX-05 同理。
- `.gitignore` 已验证排除 gguf/jsonl 两数据目录(git ls-files 零命中,.git 仅 2MB)——任何操作不得移除这两行。

### 4.3 Setter 重派预案(幂等)

判据 = 对应 `_sealed/` 文件末尾 `**COMPLETED**` footer:有 → 勿重派;无且超 1h 无写入 → 判中断,按交接档 §5.2 的 caps/回执纪律重派(产物覆写式)。**派单 prompt 必须含回执行数限制**(三/四行),这是 Setter-1 通知泄露事故后的强制措施。

### 4.4 记录链维护

- 训练进度唯一真相 = `../LEDGER.md`,只在末尾追加本包行;方法论卡登记 `../methodology/INDEX.md` 同样只追加。
- `TASK-20260812-026` 现为 partial:Setter-2 验收后主控补 Amendment 并标 done;后续新活(finding 转修复等)先领号(`POST :8899/api/next-task-id`,不可达走 INDEX 兜底)。
- 交接档是当日溯源总账,后续窗口只读不改;新窗口断点恢复走交接档 §8 三步。
- git commit:MAS_Safety_Project 仓 122+ 项未提交,惯例由用户手动分批 commit(建议:训练包产物/记录档/pm4py 数据三批)。

### 4.5 剧透事故应急

若任何通道(通知摘要/误读文件)泄露密封内容:① 主控立即在交接档记事故行(时间/通道/波及范围,不复述内容);② 波及的 EX 在批改时由 Grader 对相关条目单独标注;③ 用户自评声明。已有先例处置见交接档 §2 20:36 行。

---
**COMPLETED** | 2026-08-12 21:26(21:14 初版,收官态刷新) | Plan 三径 + 架构 + 使用 + 维护四节全;五 Agent 状态终版 | ra28 窗主控
