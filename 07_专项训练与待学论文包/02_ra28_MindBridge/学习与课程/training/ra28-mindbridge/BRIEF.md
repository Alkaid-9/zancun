# 训练包 ra28 · mindbridge：code review + debug 训练场

**训练对象**: `D:\Workspace\mindbridge\mindbridge-py`（自家多 Agent 心理咨询工程，资产卡 RA-28 / 实体卡 RE-17）
**为什么选它当 review/debug 训练场**: 自家代码可自由改（无 EA-4 类护栏）；README 有成体系的能力承诺可逐条对账（"判断代码 work"的天然题库）；带 Docker/脚本可真跑（E2/E3 验证可达）；体量适中（app/ 12 子模块），90 分钟块啃得动一个模块。
**主训练模式**: 盲做先行 + 对账（EX-01/02）· 故障注入（EX-03）· 先写后审 + 追问（EX-04）· 角色反转（EX-05）

---

## §0 开箱清单（新窗口第一动作）

1. 读 `learning/training/00_SYSTEM.md` §2/§3（闭环机制 + 答案隔离），查 `LEDGER.md` 断点。
2. **环境前置（一次性，做 EX-02 前必须完成）**：
   - `D:\Workspace\mindbridge` 目前**无 git** → 先 `git init + 首 commit`（整包快照；4.36GB gguf 目录加 `.gitignore`，模型另行备份不进 git）。这是埋雷/回滚/patch 的前提，也是 RA-28 卡片标注的强制前置。
   - Python 环境按 `mindbridge-py/requirements.txt` 建（建议独立 venv）；跑 `scripts/run-dev.sh` 冒烟一次确认服务能起（起不来本身就是 EX-02 的第一条真实素材，记下现象即可，不用现在修）。
3. **输入白名单（做题可读）**：`mindbridge-py/` 源码全部、`README.md`、本 BRIEF。
4. **禁读清单（答案隔离）**：本包 `_sealed/`；`progress/reuse/assets/RA-28__mindbridge-finetune-suite.md` 的"出处与风险"段；`progress/audits/2026/08/2026-08-12__audit__reuse-assets-research-alignment.md` §3.2——这些有 AI 预写的结论会剧透。
5. EX 顺序固定 01→05，不跳。每个 EX 开始前看 §3 是否需要先派 Setter（独立窗口）。

## §1 训练目标与毕业判据

| 能力 | 通过 EX | 毕业判据（LEDGER 可验收） |
|---|---|---|
| 盲 review（系统化读陌生实现并出 finding） | EX-01 | 抓到密封清单 ≥60% 真问题，误报 ≤2 |
| 判断代码 work（承诺→实验→verdict） | EX-02 | 5 条承诺全部给出带证据标签的 verdict，Grader 判"无越层" |
| 系统化 debug | EX-03 | 3 个注入故障排掉 ≥2，其中 ≥1 个 ≤H1 提示 |
| 架构 trade-off 论证 | EX-04 | 苏格拉底三轮追问后核心论点仍站住（Grader 判定） |
| 写可 review 的 patch | EX-05 | patch 一次通过 AI review 无 P0/P1 级 finding |

## §2 练习序列

### EX-01 · 盲 review（90 min）｜首铸卡：盲 review 操作程序

**题面**：
1. （0-20 min）只读 `README.md`，产**承诺表**：README 声称系统能做什么，逐条编号 C1..Cn（例如"支持 X / 兜底 Y / 隔离 Z"），每条标"README 原文位置"。不读任何代码。
2. （20-85 min）读 `app/agents/event_driven_runtime.py` + `app/agents/result.py` + 安全评估相关模块（自己定位哪个文件是安全模块——定位过程也是考核点），产 **finding 清单**：每条 = 位置（file:line）/ 问题描述 / 严重度（P0-P3）/ 证据标签（STATIC-CONFIRMED 或 DOC-CLAIM）。找什么：逻辑错误、并发隐患、承诺与实现不符、静默失败路径、边界缺失。
3. （85-90 min）自评：预估自己漏了几个、哪类问题最没把握。

**交付物**：`EX-01/承诺表.md` + `EX-01/findings.md` + 三行自评。
**hint**：H1"某类问题你一条都没报，再想想"→ H2"看 X 模块的 Y 机制"→ H3 直接给一条漏掉的 finding，你补分析。
**rubric**：召回率（vs 密封清单）40% · 误报扣分 20% · 过程分 40%（是否系统遍历、finding 是否带精确坐标、证据标签是否老实——"我怀疑但没验证"就标 DOC-CLAIM，标了 STATIC-CONFIRMED 却给不出行号直接扣）。
**铸卡点**：复盘时把你实际走的 review 路线整理成《盲 review 操作程序》v0.1（入口怎么选、遍历顺序、什么时候记 finding、怎么控时）。

### EX-02 · 判断代码 work：承诺验证（90 min）｜首铸卡：判断代码 work 五步

**题面**：从 EX-01 承诺表挑 5 条**可实验验证**的承诺（挑选本身是考核：哪些承诺 90 分钟内可验、哪些不可验为什么）。每条走：设计最小验证实验（冒烟 / 构造输入戳边界 / 断言中间态）→ 跑 → verdict ∈ {works / partial / broken / unverifiable} + 证据（命令 + 输出摘录 + 标签 TEST-CONFIRMED 或 RUNTIME-CONFIRMED）。
**交付物**：`EX-02/verdict表.md`（5 行，每行含实验设计一句话 + 证据）。
**hint**：H1"这条承诺的失败路径在哪种输入下触发？"→ H2 给实验设计思路 → H3 给具体命令。
**rubric**：实验设计是否"最小且能判死"40% · verdict 证据充分性 40% · 挑选眼光 20%（挑了 5 条全 unverifiable = 挑选失败）。
**铸卡点**：《判断代码 work 五步》v0.1（承诺表→可验性分诊→最小实验→verdict 分级→证据归档）。
**Setter 需求**：有——Setter 独立对同 5 条（或其超集）跑验证产密封 verdict 表，Grader 对账你与 Setter 的分歧点（分歧≠你错，能论证赢 Setter 加分）。

### EX-03 · 故障注入 debug（90 min，可加一块）｜首铸卡：系统化 debug 五步

**题面**：Setter 已在 `training/ex03` 分支埋 **3 个故障**（难度梯度：直接逻辑错 / 状态与时序类 / 配置与环境类——具体位置密封）。你拿到的只有三份**症状报告**（`EX-03/symptom-{1,2,3}.md`，Setter 生成，格式像真实 bug report：现象 + 复现步骤 + 期望行为）。逐个排：复现 → 缩小范围（二分/日志/断点，写下你每一步排除了什么）→ 假设 → 验证 → 根因 → 最小修复 + 回归验证。
**交付物**：每雷一份 `EX-03/debug-N.md`（排查日志 + 根因 + 修复 diff + 回归证据）。
**hint**：H1 方向（"雷在哪一层"）→ H2 定位（模块级）→ H3 给根因你写修复。
**rubric**：排掉数 50% · 流程系统性 30%（排查日志能看出"排除法"还是"乱翻碰运气"）· 修复质量 20%（最小修复 vs 顺手重构——重构在这里是扣分项）。
**铸卡点**：《系统化 debug 五步》v0.1。
**Setter 需求**：必须——埋雷 + 写症状报告 + 密封根因说明。**埋雷规则**：只动 `training/ex03` 分支；每雷独立 commit（回滚粒度）；雷必须是"运行可触发"而非纯读码可见；密封档含每雷的触发命令。

### EX-04 · 架构 review：黑板模式 trade-off（60-90 min）

**题面**：写一页架构评审：mindbridge 的事件驱动黑板协作（五 Agent 任务认领）vs 编排式（如 EvoAgent 的 harness 流水线）——从吞吐、可观测性、失败传播半径、扩展新 Agent 的成本四个维度对比；结论段回答"如果重写 mindbridge 你保留黑板还是换编排，为什么"。每个论点标注依据（读码坐标 / 运行观察 / 推断）。
**交付物**：`EX-04/架构评审.md`。
**批改形态**：无密封答案（开放题）。Grader 做**苏格拉底三轮**：每轮挑你论证最弱的一点追问，你书面回防；三轮后 Grader 出总评（核心论点站住/翻车/带伤站住）。
**rubric**：论据与坐标 40% · 反方视角完整性 30%（有没有主动写"黑板的坏处"）· 追问回防 30%。

### EX-05 · 事件导出 patch（90 min，衔接产出）

**题面**：自己动手：给 runtime 加事件导出（黑板任务发布/认领/完成/否决 → 结构化 log），跑 CHAT / CONSULT / RISK 三场景各 ≥3 轮，产 log 文件。要求 patch 风格符合仓内现有代码、带回滚说明、log 格式预留 case id / activity / timestamp / agent id 四字段（下游 ra26 管线要吃）。
**交付物**：patch（独立分支）+ 三场景 log + 一段"格式设计说明"。
**批改形态**：角色反转——**AI 对你的 patch 做正式 code review**（你体验被 review，对照你在 EX-01 当 reviewer 的感受，复盘写一段"两边坐过之后我对 review 的理解变化"）。
**rubric**：patch 一次过（无 P0/P1）50% · log 四字段可用性 30% · 反思质量 20%。
**产出衔接**：三场景 log 直接成为 ra26 训练包 EX-03 的对照数据（研究产出线的"黑板拓扑对照组"）。

## §3 Agent 派单要点（新窗口直接抄）

- **Setter（EX-01/02/03 前置，独立窗口后台跑）**：输入 = `mindbridge-py/` 全源码 + 本 BRIEF 对应 EX 段；输出 = `_sealed/EX-NN_answer.md`（EX-01：独立 finding 清单含严重度与坐标；EX-02：密封 verdict 表；EX-03：埋雷 commit + 症状报告三份（症状报告放 `EX-03/`，根因说明放 `_sealed/`））；caps = 除 EX-03 的 `training/ex03` 分支外不动任何源码；产物零剧透（对用户窗口只回"就绪"）；第一动作建骨架末动作 footer。
- **Coach（做题中，同窗轻量）**：只按 H1→H2→H3 响应"卡死"请求，禁止跳级；每次解锁在 LEDGER 行记级别。
- **Grader（交付后）**：输入 = 你的交付物 + `_sealed/` 对应档 + 本 BRIEF rubric；输出 = 批改单（召回/误报/过程分 + 3 条最有价值的差距分析）+ 复盘要点建议；EX-04 走三轮追问协议。
- 全部继承：单写者、90 分钟块、修订封顶 2 轮、无 re-review 子代理（Grader 产物由主控/你本人终审）。

## §4 产出衔接（训练→研究/作品集）

- EX-05 的三场景 log → ra26 包 EX-03 的对照数据 → toy 报告"黑板 vs 编排拓扑对照"章（9 月邮件可讲的小结果）。
- EX-01/02 的真 finding（非训练噪音）→ 择真修复 → mindbridge 作为作品集项目的质量提升（简历叙事：不只是写了，还系统 review 过）。
- EX-04 评审档 → 作品集"架构决策"写作样本。

## §5 死线降级

OE-1（9-10）不依赖本包，无直接死线。若 ra26 的 toy 因故要抢进度而 EX-05 未做 → 允许 Agent 代做事件导出（旧方案档 §2 M1/M2 拓扑），你转做"逆向训练"：review Agent 的 patch（等价练习，LEDGER 记 `[降级→逆向训练]`）。

## §6 红线

- git init/快照未完成前，禁止任何写操作练习（EX-03/05）。
- 埋雷只在 `training/ex03` 分支；main 永远可跑。
- gguf / jsonl 两个数据目录任何练习不碰。
- 训练 finding 若要转正式修复，走正常 patch 流程并记 task_log（训练产物本身不进 progress 权威链）。
