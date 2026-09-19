# Anchor 拆解:Best Friends, Not Forever(长时程人格塌缩与行为漂移审计)

> **拆解元信息**:2026-08-13 | P-Anchor 论文拆解 Agent(S01/S03 + 题族设计)| 状态:**v0,待工程校准**
> **原文为准**:所有数字、定义、表格均逐条核对 arXiv HTML 全文([arXiv:2607.28818](https://arxiv.org/abs/2607.28818));与档案二手转述(D3 卡 6)不一致处以本拆解为准。

## 论文卡

| 项 | 内容 |
|---|---|
| 标题(原文) | **Best Friends, Not Forever: Evaluating Long-Horizon Persona Collapse and Behavioral Drift in AI Companions** |
| 作者 | Pranav Narayanan Venkit, Akshara Prabhakar, Yu Li, Daniel Lee, Chien-Sheng Wu |
| 机构 | Salesforce AI Research |
| 发表 | 2026 preprint,[arXiv:2607.28818](https://arxiv.org/abs/2607.28818) |
| 框架名 | **Anchor** = Assistant-Normalised Character and Historical Outcome Recall |
| 一句话 | 首个把"人格演绎"(Identity Probe)与"轨迹记忆"(Trajectory Probe)拆开测的长时程 AI 伴侣审计:2,008 段对话 × 27 personas × 9 日程 × 3 记忆设置 × 4 模型,每段 85–130 个 session |
| 本地 PDF | `../../papers-P0/2607.28818_best-friends-not-forever.pdf` |
| 工件 | 公开仓库含 3 个合成开发题库 + 可运行判分器;**完整测试集私有**(留作隐藏评测) |

## 为什么拆这篇

它是**张重熙记忆改造的最高危回归点来源**:

1. **用户状态变更题全模型 ≈ 随机**(0.214–0.250,四选一基线 0.25)——"他知不知道你现在的工作/情绪/生活状态"是行业级空白,也是记忆改造最该测、最容易坏的地方。
2. **人设现行状态题在检索式打分下 0.75 → 0.25**——检索会召回旧状态而非现行状态。张重熙记忆库若走 RAG 路线,这是头号地雷(注意:原文标注该族仅 2 道校准题,证据为探索性,详见 `03_PAPER_READ.md` §4.6)。
3. 它的 **Trajectory Probe 七族**是现成的"记忆回归出题分类法",本拆解把它翻译成张重熙题库(`05_PROBE_BANK_v0.md`),供 **B5 评测方案**直接引用(B5 已明确"Anchor 题族必须进 golden set",见 `_meta/next-plans.md`)。

## 核心数字速览(全部原文核对)

| 结果 | 数字 | 出处 |
|---|---|---|
| 轨迹题平均准确率 | **44.4%**(四选一,随机 25%;模型×条件范围 0.355–0.636) | §5.5 |
| 用户状态变更族 | **0.214–0.250 ≈ 随机**,所有上下文条件下 | Table 8 |
| 人设更新族 | LC/HS 0.75、SM 0.875、**检索 0.25**(仅 2 题,探索性) | Table 8 |
| 时序族 | 0.429–0.494 | Table 8 |
| 问卷保持 PR₃ | Gemini 0.810 > Claude 0.764 > GPT-4o-mini 0.610 > GPT-5-mini 0.595 | Table 6 |
| 轮级四轴全保持(3 judge 多数) | Gemini 最低 79.0%,其余 >96% —— **与问卷排序矛盾** | Table 6 |
| judge 分歧 | 同一批 GPT-4o-mini 轮次:Claude judge 判 15.5% 保持,Gemini-Flash 判 99.8% | Table 9 |
| 日程效应 | 情感脆弱/求认同/混合/拟真日程的边界让步与风格偏离率高于 clean 与**显式对抗** | §5.4(仅主 judge) |
| 记忆架构 | 三种生成设置都救不了;聚合准确率 LC 0.430 / HS 0.441 / SM 0.459 / 检索 0.446,模型间差异 > 架构间差异 | §5.3, §5.5 |

## 目录导航

| 文件 | 内容 | 状态 |
|---|---|---|
| `01_QUESTIONS.md` | S01 问题驱动:拆解前的 10 个问题 + 论文的回答 + 未决问题 | v0 |
| `03_PAPER_READ.md` | S03 精读:立场与定义 / 实验协议 / **Trajectory Probe 七族构造** / **各记忆系统失败模式** / 结果全解 / 局限 | v0 |
| `05_PROBE_BANK_v0.md` | **核心交付**:七族 → 张重熙回归题库设计(每族 3–5 道中文题模板 + 构造规则 + 判分方式),供 B5 直接引用 | **v0,待工程校准** |
| `GLOSSARY.md` | 术语表:原文术语 → 拆解统一中文译名 → 原文定义 | v0 |

编号说明:本次拆解只做 S01(提问)、S03(精读)与题族设计(05);S02(略读)并入 README,S04(代码/工件)待公开仓库拆解后补。

## 与档案的关系

- `../../deep/D3_persona-eval.md` 精读卡 6:本拆解的前置摘要;卡 6 未标注"人设更新族仅 2 题"的探索性 caveat,本拆解已补正。
- `../../../13_evaluation/insights.md`:题库判分方式对齐其 L1/L2/L3 三层设计。
- `../../../_meta/next-plans.md` B5 评测方案 v1:`05_PROBE_BANK_v0.md` 是其"golden set 构造步骤"的直接输入。
- 交叉印证:LoCoMo(时序是长程记忆最弱项)、Assistant Axis(情感脆弱/元反思触发漂移,arXiv:2601.10387)、PersonaEval(中文 judge 打七折)。
