# Bridge 研究提案与对外材料索引（2026-08-12）

> **2026-09-20 当前入口**：[进组急用修复与验收](../README_进组急用.md)、[材料使用指南](GUIDE_external_materials.md)。本索引下方的旧研究排序、日期、运行数字和迁移判断不是本轮验证结果。急用正文只取修订 OE1、鲁版一页纸和简历；通用声音版、旧图与渲染输出暂不外发。候选提案没有因本轮编辑获得 RESEARCH_VALIDATED。

> status: **drafts-complete / experiments-not-started**。三提案均是可证伪研究草案，
> 不是已验证结论；必须通过各自 kill criteria 后才可对外声称研究贡献。
> 输入：W1/W2/GRAND_MAP/W4/RADAR + EvoAgent Fusion-0 双出口。
>
> **08-13 收口窗增**：`COLLISION_AUDIT_V2_20260813.md`（16 条新证据 + T1/T2/T5 重裁 + watchlist 12 条）已挂本目录；T2 提案已同步收窄修订。
> **T5 编号双用警示**：本表第 4 行"T5"= companion 概率护盾（W7 波次）；GRAND_MAP §5 的"T5"= MCP/A2A 协议 PN 验证（bridge，观察·承压）。两者是**不同课题**，消歧待 `DEC-T5-NUMBERING` 拍板；在此之前引用任一"T5"必须带限定词（T5-companion / T5-bridge）。

## 1. 文件与优先级

| 优先 | 文件 | 课题 | 当前优势 | 最大风险 | 下一门禁 |
|---:|---|---|---|---|---|
| 候选 | `T2_conformance_formal_guarantee.md` | T2 轨迹过程发现+alignment 一致性 | 工具/概念迁移假设，非“直连孙组当前议程” | 最近邻与数据适用性待原始证据核验 | 用户选题后再定实验合同，本轮不执行 |
| 候选 | `T1_T4_propagation_containment.md` | T1 展开可达/隔离 + T4 概率根因 | 撤回“创新最高”的无证据排序 | 建模语义、状态空间、参数估计 | 先核对象与假设，不自动启动 |
| 候选 | `T3_memory_integrity_valueflow.md` | T3 use-after-poison 值流检测 | 最近邻差异待核，不称“差异硬” | 派生边可观测性尚属假设 | 阈值与公平 baseline 须预先确定 |
| 候选 | `T5_companion_prob_shield.md` | T5-companion 概率行为护盾 | 不宣称域全空白或数据独占；历史离线测试非研究效果证据 | 数据许可、效度、后端与本人能力均须核对 | 旧资产状态不自动授予复现/研究验收 |
| 急用 | [OE1 修订稿](OE1_lu_email_v4.md) | 鲁侧学习请教 | 只使用可追溯论文身份和本人填证据的表述 | 个人字段与贡献待确认 | 普通请教不依赖 BR-1；用户另行决定发送 |

## 1b. 迁移权重表（2026-08-13 增,迁移轴）

> **历史判断，未重新核证**：下表“Sun 核心/高复用/直通议程”等不是孙猛当前画像；本轮不据此排期或写入进组正文。旧权重不优先于用户真实训练目标。

> 口径:"Lu 现在 / Sun 之后 / 沉淀可迁移能力"(用户口径存档见 progress/decisions/2026-08-13__strategy__lu-sun-migration-weight.md)。
> **重估触发器:考研出分日全表强制重估;平时本表只读,不得据此单方面砍投入(防自我实现偏差)。**

| 课题 | 栈归属 | Lu 依赖 | Sun 复用 | 组无关可迁移资产(点名) |
|---|---|---|---|---|
| T2 | Lu 核心(D3 流程挖掘) | 高:PM4Py/conformance/组内接口人 | 高:monitor 规格来源叙事直通孙组议程 | conformance 思想、事件日志工程、XES 数据管线、EvoAgent trace 基建 |
| T1/T4 | Lu 重(D1/D2 PN 展开+概率根因) | 高:PN 工具链/鲁组血缘 | 中:概率保证语言与 iMDP 管线相通 | 概率建模思维、根因分析、状态空间工程 |
| T3 | Lu 血缘(D2 UAF+VFG 迁移) | 中:值流方法学 | 中:记忆安全议程(M④)对接 | 值流/污点分析思维、插桩工程、威胁建模 |
| T5 | Sun 核心(DTMC/iMDP/dtControl 管线) | 低:方法上几乎不依赖鲁栈 | 高:复现即预研,直接消费实验室管线 | **companion 域建模能力、自有纵向平台与数据(完全个人资产)、stormpy/Storm 工具链** |
| OE1 | Lu 通道 | — | — | 学术写作与对外沟通(通用底座) |

## 2. W4 评审门禁（所有提案共用）

1. **保证链诚实**：规格来源、翻译保真、验证器边界、日志完备性、成本函数
   都要写；链上有 LLM 时不得泛称端到端 formal guarantee。
2. **baseline 公平**：最近邻实测；同 backbone / 规则库 / 知识 / 调用预算；
   MAS 必须对照单 agent+等量采样。
3. **不可自产自评**：至少一个外部 benchmark + 真实 agent trace；
   自建/合成数据只作补充；训练与测试隔离。
4. **统计与成本**：≥3 seeds，mean±std/95% CI；token/calls/wall-clock；
   utility-safety 曲线。
5. **形式转换保真**：NL/policy/trace→PN/LTL 的 semantic faithfulness /
   intent drift 必须定量；结构 soundness ≠ 真实系统忠实。

## 3. 历史时间排序（未重新批准，不自动执行）

```text
现在       T2：受控 EvoAgent 轨迹 + 三类偏差注入
9-10月     T2：外部 trace + 全基线；同时 T1/T4 只做 M0 分层定义
11月       T2：ablation/统计/开销；过 kill criteria 才写稿
12月前     VerifAI/agent workshop + arXiv 占位（失败则诚实降级工程报告）
2027 H1    T1/T4 toy；T3 作为独立备选
（08-13增）T5 与 Phase 1 并线只做复现预研+谓词表 v0，不占 T2 窗口；2027 H1 与 T1/T4 同批评估
```

## 4. 当前禁止的表述

- ❌ “全球唯一/保证所有风险/无漏报/证明 agent 系统安全”
- ❌ “Inductive Miner 自动得到真实系统正确模型”
- ✅ “在明确模型、日志完备性与可观测假设下，对策略 PN 可表达偏差给出最小
  alignment 证据”
- ✅ “当日检索未命中 PN/PM 特有能力×agent 安全；结论由月度快查持续证伪”

## 5. 历史执行记录（本轮未复跑或重验）

- 提案正文：✅ 三份齐
- T5 提案正文（2026-08-13 增）：✅ `T5_companion_prob_shield.md`；P-EmoAgent AI 离线资产终审 `CODE/STAT/CLAIM=PASS`，41 项工程测试 + 19 项固定复算测试通过，local integration=`AI-ASSETS-READY`；真实后端/真实 E2 未开始，教学待用户，上游许可与公开发布 `NO-GO`；本状态不代表 EmoGuard 效果已验证或论文复现完成；实验 ⬜
- W4 雷区回填：✅ T2 保证链已主控收窄
- EvoAgent Fusion-0：✅ XES + GraphML 双出口
- 实验：⬜ 未开始
- BR-2 完成条件：提案部分 ✅；toy+arXiv ⬜
- OE-1：09-20 已修订为不依赖 BR-1 的请教草稿；本人字段、贡献证据、最终副本与发送决定仍开放。
