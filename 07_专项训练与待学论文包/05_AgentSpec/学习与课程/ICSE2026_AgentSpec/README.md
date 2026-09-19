# Paper: AgentSpec — Customizable Runtime Enforcement for Safe and Reliable LLM Agents

**会议**:ICSE 2026(第 48 届 IEEE/ACM International Conference on Software Engineering,2026-04-12/18,Rio de Janeiro,CCF-A)
**arXiv**:[2503.18666](https://arxiv.org/abs/2503.18666)
**作者**:Haoyu Wang(SMU 博士生,一作)、Christopher M. Poskitt(SMU)、Jun Sun(SMU)
**代码**:[github.com/haoyuwang99/AgentSpec](https://github.com/haoyuwang99/AgentSpec)(49 星,master 分支)[D6 实见]
**资助**:新加坡教育部 AcRF Tier 3(MOET32020-0004)(论文致谢节)
**类型**:方法+系统论文(DSL 设计 + 形式语义定义 + 三域实现 + 四 RQ 实验,无定理)
**精读日期**:2026-08-13
**状态**:**S01-S04 v1(首轮),复现与审查留后续窗**

---

## 一句话总结

第一个面向 LLM agent 的可定制**运行时强制**(runtime enforcement)框架:用 `trigger–check–enforce` 三段式 DSL 写安全规则,拦截 LangChain 决策回路,在代码/具身/自动驾驶三域实现 >90% 风险拦截、危害动作归零、AV 100% 合规,总开销毫秒级(§1、§5)。

---

## 作者辨析:SMU Jun Sun 组 ≠ PKU Meng Sun 组

这条研究线上有**两位孙姓 PI,务必区分**:

| | Jun Sun(孙军) | Meng Sun(孙猛) |
|---|---|---|
| 机构 | Singapore Management University | 北京大学 |
| 本线代表作 | **AgentSpec(本文,ICSE 2026)**、ProbGuard(ASE 2026)、FixDrive/LawBreaker/μDrive(AV 工具链) | ReGA(FSE 2026,Zeming Wei 一作) |
| 抽象对象 | 行为轨迹(黑盒、动作级) | 模型内部表示(白盒、token 级) |
| 本仓库对应拆解 | 本目录 | `_archive/.../04_FSE2026_ReGA/` |

- 本文三位作者全部属 SMU,Jun Sun 为 PI(ORCID 0000-0002-3545-1392,论文题头)。
- 两组的公开交点:本文参考文献 (53) 的 ICML 2025 立场论文 *Trustworthy AI agents require the integration of LLMs and formal methods*,作者名单同时含 Sun, M.(孙猛)与 Sun, J.(孙军),以及 ReGA 一作 Wei, Z.——是两组谱系的桥文献。
- 论文致谢感谢 Sun Yang、Wang Kun 支持 AV 实验;二人即同组 AV 工具链 LawBreaker/FixDrive(Yang Sun 一作)与 μDrive(Kun Wang 一作)的作者(参考文献 36/37/40)——AV 域实验是同组工具链自用。

---

## 关键数字(摘要与 §5,可直接引用)

| 域 | 数据集 | 结果 |
|---|---|---|
| 代码 | RedCode-Exec(25 风险类 × 30 例) | >90% 风险执行被拦截 |
| 具身 | SafeAgentBench(10 危害类) | 危害任务完成率全部归零;安全任务完成率仅 58.62%→54.26% |
| AV | FixDrive 违法场景(8 个) | 100% 合规 |
| 开销 | — | 解析 1.42ms;谓词求值 2.83ms(代码)/1.11ms(具身);对比 agent 单次执行 25.4s/9.82s |
| LLM 生成规则(o1) | 三域 | 具身 precision 95.56% / recall 70.96%;代码拦截 87.26%;AV 零样本 5/8 场景 |

---

## 在谱系中的位置:与 ProbGuard / T5 的关系

1. **ProbGuard 的执行器依赖与立项前身**。
   - 依赖:ProbGuard 仓库直接 `from agentspec.controlled_agent_excector import initialize_controlled_agent`——复现 ProbGuard 必须先跑通 AgentSpec,两者共享 LangChain 拦截层 [D6 元数据更新 3]。
   - 立项:本文 §6.3 自述局限"确定性、离散检查点强制,不做轨迹级前瞻",并明写 future work 是"从历史交互学 DTMC、做概率可达性查询以支持前瞻式干预"——这段原文就是 ProbGuard(ASE 2026,同一作 Haoyu Wang)的立项理由。
   - 对照:ProbGuard 实验以 AgentSpec 为反应式基线(报告比其省 12.05% token)[D6 卡 1]。
2. **T5(companion 域概率护盾)分级干预规则层的母版**。
   - 四种 enforcement(`stop` / `user_inspection` / `invoke_action` / `llm_self_examine`)与 T5 分级干预档位一一对应(硬切断/人工升级/降级转介/人格保持型软干预),映射表见 `03_PAPER_READ.md` Layer 10。
   - T5 基线③(确定性规则)= 本仓库;"反应式规则 vs 概率预测"的对照实验设计可整套照抄 [D6 卡 3]。

---

## 目录结构

```
ICSE2026_AgentSpec/
├─ README.md          ← 本文件(论文卡)
├─ 01_QUESTIONS.md    ← S01:读前 5 问 + 品味初评
├─ 02_SKELETON.md     ← S02:骨架 + DSL 语法符号表 + 三段式流程 + 左墙右墙
├─ 03_PAPER_READ.md   ← S03:分层精读(DSL/谓词/enforcement/实验/开销/局限 + T5 怎么抄)
├─ 04_DERIVATION.md   ← S04:DSL 语义形式化梳理(求值语义、与 LTL/自动机的关系)
└─ GLOSSARY.md        ← 术语表
```

**上游素材**:`casual/companion-survey/14_academic/deep/D6_safety-formal.md` 卡 3(AgentSpec)、卡 1(ProbGuard)
**框架参考**:`_archive/research/sun/legacy-2026-Q3/papers/04_FSE2026_ReGA/`(结构参照,内容按本论文裁剪)
**铁律**:以论文原文为准,逐条标出处;仓库实见信息标 [D6];推算与个人分析分别标 [推算] / [个人分析]。

---

**最后更新**:2026-08-13(S01-S04 v1)
