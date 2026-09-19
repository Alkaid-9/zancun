# 科研素养成长库

科研能力的学习、积累、迭代。

## 目录结构

```
research_growth/
├── 方法论/          ← 科研方法论笔记
├── 高手经验/        ← 顶尖科研工作者的经验总结（PDF 提取）
├── Notion文档/      ← pengsida Notion 文档
│   ├── pengsida_learning_research/  ← 已手动摘录的核心文档
│   └── raw/                         ← API 抓取的原始 JSON
├── 读书笔记/        ← 读论文/读教材的笔记
├── 反思与思考/      ← 自己的科研反思
└── tools/           ← 工具脚本
    ├── call_api.py     ← GPT/Claude API 调用
    └── notion_to_md.py ← Notion JSON → Markdown 转换
```

## 已有材料

### 高手经验（PDF 全文提取，6 份）
| 文件 | 作者 | 核心内容 |
|------|------|----------|
| `John_Schulman.txt` | OpenAI 联合创始人 | 选问题(Idea vs Goal-driven)、持续进步、个人发展 |
| `Michael_Nielsen.txt` | 诺贝尔物理学奖 | 有效研究原则、心态、创造力 |
| `Bill_Freeman.txt` | MIT 教授 | 科研经验精要 |
| `Zhihua_Zhou.txt` | 周志华（南大） | 本科生科研能力培养 |
| `Zhilin_Yang.txt` | 杨植麟 | 科研经验 |
| `Wujun_Li.txt` | 李武军 | 本科生科研入门 |

### Notion 文档（手动摘录）
| 文件 | 状态 | 内容 |
|------|------|------|
| `博士生应该具有的意识与能力...如何做Research Project.md` | ✅ 完整 | 博士生 7 大意识 + 7 大能力 + 16 步 Research Project 流程 |
| `01_想idea的能力.md` | ⚠️ 部分（toggle 子块未展开） | Goal-driven research、导师学生分工表 |

### 待摘录
- [ ] 如何有效地读论文
- [ ] 论文写作模板
- [ ] 怎么rebuttal
- [ ] 怎么做学术报告slides
- [ ] 怎么找论文
- [ ] 如何给算法debug

## 工具

| 工具 | 用途 | 状态 |
|------|------|------|
| `notion_to_md.py` | Notion JSON → Markdown | ✅ 可用，但 toggle 子块需手动展开 |

## API 状态

全部使用 mimo（token-plan-sgp.xiaomimimo.com）。不再使用外部代理。

## 学习路线

1. 先读「Research Project」文档（已有），理解博士生能力框架
2. 读高手经验 PDF，对比自己的不足
3. 结合 MAS Safety 项目实践方法论
4. 每完成一个阶段写反思笔记到 `反思与思考/`

## 三源科研体系整合（2026-09-04）

`方法论/科研体系三源整合_20260904.md` 是当前个人方法库的统一入口：

- Luo PDF：研究方向、问题定义、论文结构与读者/审稿人视角；
- Supervisor-Skills：导师经验蒸馏出的提问与检查机制；
- pengsida：Research Project、最小实验、失败定位与调试；
- 当前 OS：事实边界、用户先做、ownership、claim ceiling 和冷启动验收。

入口只做适配和映射，不替代冻结 OS，也不把来源里的经验性数字、venue 口径或接受率写成硬规则。

## 迁移判别与研究操作符（2026-09-05）

- `方法论/迁移审计协议_20260905.md`：把跨域 sense 依次压到源机制证据、目标域前提、representation、decision delta、竞争解释和最小证伪，再决定 `DROP / PARK / PROMOTE`。
- `方法论/TRANSFER_CARD_TEMPLATE.md`：每个跨域联想的可复用审计卡。
- `反思与思考/2026-09-05_Execution-Structure-Intervention_研究母结构.md`：首个完整案例，保存 `execution -> structure -> intervention`、semantic prior-art search 和 Transfer Judgment 的原始推理链。
- `反思与思考/2026-09-05_鲁法明研究谱系与稳定Research-Grammar.md`：区分鲁法明本人署名与公开合作网络，串联 Petri 网、流程挖掘、并发程序、RCA 和工业 AI，并把公开证据与 plausible next-step inference 分栏保存。
- `反思与思考/2026-09-05_EdgeIM四论文十字训练闭环.md`：把 EdgeIM 设为 ownership 主干，把 sigRank、Ground Truth Approach、CrossEdgeIM 分别作为横向比较、实验方法论和纵向 genealogy 镜头，并在不同学习节点穿插解锁。

上述案例中的论文身份、年份、方法细节和实验数字目前按“用户输入、待逐项核验”保存，不作为已完成 related-work audit 或 novelty 证据。
