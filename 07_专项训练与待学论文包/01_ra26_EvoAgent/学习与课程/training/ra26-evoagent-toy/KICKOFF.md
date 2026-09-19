# ra26 专属窗口协议（KICKOFF）

**本窗职责**：只管 `ra26-evoagent-toy` 训练包全生命周期。**EvoAgent 仓对本窗一切角色只读**（EA-4 护栏）。产物统一落 `MAS_Safety_Project/research/pm4py_toy/`。

## 阶段 1 · 赛前准备（本窗第一动作）

> **幂等检查（先做）**：若 `_sealed/EX-01_answer.md` 已存在且带 completion footer、且 `research/pm4py_toy/` 环境已建——赛前准备已由协调窗代理完成（8-12 晚并行发动），本阶段跳过，直接报"就绪"。部分完成则只补缺项。

1. 读 `BRIEF.md` 全文 + `../00_SYSTEM.md` §2/§3/§7。
2. **环境前置（主控 shell）**：
   - `research/pm4py_toy/` 建 venv 装 `pm4py`（或复用既有环境，装好 `import pm4py` 冒烟）。
   - 建子目录：`convert/`（EX-02 脚本）、`data/`（log 数据；ra28 窗口会送三场景 log 过来）。
3. **E3 检查**：读 `progress/decisions/PENDING.md` 的 `DEC-REUSE-ROLLOUT-E3`——已放行则阶段 2 的 EX-01 含运行验证步；未拍则只走静态路径（不阻塞，照常开工）。
4. **派 Setter（子代理后台，本窗对话零代码分析）**：Setter 按 BRIEF §2 EX-01 题面独立静态采证 → `_sealed/EX-01_answer.md`。回执只报「完成 + 路径 + 条目数」。
5. 就绪报告一行：pm4py 冒烟结果 + E3 状态 + "可开始 EX-01"。

## 阶段 2 · 做题

- 同总纲：计时 90 分钟、禁读提醒（BRIEF §0 第 5 条）、Coach 按 H1→H3 逐级。
- EX-02 特殊：用户写完脚本后主控做**正式 code review**（P0-P3 分级，两轮封顶）——这一步主控就是 Grader，不用等交付后另派。
- EX-03 若 ra28 的对照 log 已送达 `data/`，按题面加对照实验；未送达就只跑 EvoAgent log（不等）。

## 阶段 3 · 批改与复盘

- EX-01 开封对账（你 vs Setter 的采证分歧——分歧点优先讨论，谁对以证据定）。
- EX-03/04 按"审稿人视角"批改：专挑越层结论和无出处数字，一轮修订。
- 铸卡：EX-01《陌生代码结构侦察》、EX-03《证据分层写作》→ `../methodology/` + INDEX。
- LEDGER 只追加本包行。
- EX-04 定稿后：TOY_REPORT.md 是转正产出——在 `progress/task_logs/` 记一行（训练产物转正的唯一通道），并通知 outreach 相关窗口可引用。

## 断点恢复

读本档 + `../LEDGER.md` 查 ra26 最后一行。
