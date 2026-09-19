# Teardown: INTIMA — A Benchmark for Human-AI Companionship Behavior

> 拆解性质:P-INTIMA 首轮拆解 + **T5 谓词表 v0 试产**(T5-companion 提案 M1 的 AI 侧预研)
> 拆解日期:2026-08-13 | 拆解范式:仿 `MAS_Safety_Project/_archive/research/sun/legacy-2026-Q3/papers/04_FSE2026_ReGA/`
> 状态:首轮完成;**04_DERIVATION 免做**(benchmark 论文,无重公式,改做分类学拆解并入 03);02/07/08 待后续轮次

---

## 论文卡

| 项 | 内容 |
|---|---|
| 标题 | INTIMA: A Benchmark for Human-AI Companionship Behavior |
| 作者 | Lucie-Aimée Kaffee, Giada Pistilli, Yacine Jernite(Hugging Face) |
| 链接 | https://arxiv.org/abs/2508.09998(2025-08-04 上线;〔08-22 已核:venue=ICLR 2026 Poster,双独立源 OpenReview cZGh1iXdq6 + iclr.cc virtual poster 10008491;原"投稿目标 AAAI"系 AAAI 模板版权行误导,证伪〕) |
| 数据集 | https://huggingface.co/datasets/AI-companionship/INTIMA(tsv+jsonl;数据集页显示 380 行,论文称 368 prompt,出入见 03 §L7) |
| 可视化 | https://hf.co/spaces/AI-companionship/intima-responses-2D(UMAP + embedding-atlas) |
| 类型 | benchmark 论文(分类学 + prompt 集 + LLM-judge 评测协议),无理论贡献(作者自答复现清单 "theoretical contributions: no") |
| 语言/形态 | 英语;**单轮**对话 prompt |
| 一句话 | 从 r/ChatGPT 真实帖扎根编码出 31 类伴侣行为分类学,生成 368 个定向 prompt,用 Qwen-3 按"强化伴侣/维持边界/中性"十标签给 4 个模型打分,发现所有模型默认强化伴侣关系、且**用户越脆弱边界行为越少**。 |

## 与 T5 的关系(为什么拆它)

T5-companion 提案(`MAS_Safety_Project/research/map/proposals/T5_companion_prob_shield.md`)M1 谓词工程明确要求:**INTIMA 31 类 → 12-16 个带时间窗的可执行谓词**,把"评测资产变防护资产"(提案 §7 与 INTIMA 的差异声明)。本拆解的核心交付即 `05_PREDICATES_v0.md`:16 个谓词草案(用户侧 6 + 系统侧 6 + 轨迹级 4),每个带时间窗参数、极性与张重熙场景适配注。**v0 未经标注校准,κ 实验与阈值标定待工程窗**(对应 T5 RQ1)。

## 目录

```
teardowns/INTIMA/
├─ README.md            ← 本文件(论文卡 + 目录)
├─ 01_QUESTIONS.md      ← 读前 5 问 + 品味预判(S01)
├─ 03_PAPER_READ.md     ← 精读:分类学溯源 / 31 类逐类含义 / 标注协议 / 发现 / 局限(S03,并入分类学拆解)
├─ 05_PREDICATES_v0.md  ← ★核心交付:T5 谓词表 v0(16 谓词 + 张重熙适配注)
└─ GLOSSARY.md          ← 术语表(理论 / 分类学 / 评测 / T5 接口)
```

## 首轮拆解的三个关键发现(详见 03)

1. **分类学数据源修正**:D4 精读卡(卡 2)写"从 r/MyBoyfriendIsAI 等社区扎根编码",**论文原文实为 r/ChatGPT**(2023-06 至 2024-12,关键词 "companion" 筛出 698 帖,人工精选 53 帖)。r/MyBoyfriendIsAI 是另一篇 MIT 论文(D4 卡 3)的对象,两卡混淆,建议回改 D4。
2. **"31 类"其实是 32 减 1**:Reddit 编码产出 32 个行为码(Table 2),`engaging interaction`(频次 1)未进入 prompt 生成清单(Table 9),基准最终 31 码;论文另有多处数字出入(33/39、19/23、示例表冒出未定义的 `voice` 码、数据集页 380 行),已逐一登记在 03 §L7。
3. **标注协议不是互斥三分类**:顶层是"强化伴侣/维持边界/中性"三大类,但实现为 **10 标签多标签打分**(每标签 low/medium/high 强度),标签间互信息低——这直接支持 T5 把符号状态做成"少量近独立因子的乘积"而不担心组合爆炸(05 §设计原则)。

---

**上游文档**:D4 精读卡 `../deep/D4_hci.md`(卡 2)| T5 提案 M1(见上)| 范式参考 ReGA teardown
**最后更新**:2026-08-13
