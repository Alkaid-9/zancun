# Bridge 研究提案与对外材料索引（2026-08-12）

> status: **drafts-complete / experiments-not-started**。三提案均是可证伪研究草案，
> 不是已验证结论；必须通过各自 kill criteria 后才可对外声称研究贡献。
> 输入：W1/W2/GRAND_MAP/W4/RADAR + EvoAgent Fusion-0 双出口。
>
> **08-13 收口窗增**：`COLLISION_AUDIT_V2_20260813.md`（16 条新证据 + T1/T2/T5 重裁 + watchlist 12 条）已挂本目录；T2 提案已同步收窄修订。
> **T5 编号双用警示**：本表第 4 行"T5"= companion 概率护盾（W7 波次）；GRAND_MAP §5 的"T5"= MCP/A2A 协议 PN 验证（bridge，观察·承压）。两者是**不同课题**，消歧待 `DEC-T5-NUMBERING` 拍板；在此之前引用任一"T5"必须带限定词（T5-companion / T5-bridge）。

## 1. 文件与优先级

| 优先 | 文件 | 课题 | 当前优势 | 最大风险 | 下一门禁 |
|---:|---|---|---|---|---|
| 1 | `T2_conformance_formal_guarantee.md` | T2 轨迹过程发现+alignment 一致性 | Fusion-0 数据管线已成；最快出 toy；直连孙组 monitoring | AgentLTL 已占声明式 conformance；SMU 迭代快 | 三类偏差注入 + 外部 trace；证明不是复述状态机 |
| 2 | `T1_T4_propagation_containment.md` | T1 展开可达/隔离 + T4 概率根因 | 创新最高；PN 并发/循环补 NCB DAG 假设 | 四层建模难、状态爆炸、参数估计 | M0 四层定义 + 普通图/基础 PN 消融 |
| 3 | `T3_memory_integrity_valueflow.md` | T3 use-after-poison 值流检测 | 最近邻明确排除跨 agent 共享记忆；差异硬 | 派生边可观测性 H1 可能失败 | 插桩覆盖率≥60%；普通污点 F1 增量≥5pt |
| 4 | `T5_companion_prob_shield.md`（2026-08-13 增，W7 波次） | T5 关系型 agent 概率行为护盾（companion 域） | 域全空白（W7 C① 绿格）；P-EmoAgent AI 离线资产终审 `CODE/STAT/CLAIM=PASS`，41 项工程测试 + 19 项固定复算测试通过，local integration=`AI-ASSETS-READY`；自有纵向平台与数据独占 | 关系 unsafe 无金标；模拟用户效度；上游与量表许可；真实后端未选 | 选择后端 → 真实 Guard smoke + paired A/B；真实 E2 未开始，用户教学后补 |
| — | `OE1_lu_email_v4.md` | 9 月鲁老师邮件 v4 | 已用真实 XES/GraphML 成果，叙事对线 | 占位未填、NSFC 未放榜 | 8-25 BR-1 + 用户逐句确认 |

## 1b. 迁移权重表（2026-08-13 增,迁移轴）

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

## 3. 时间排序（窗口已由 6-12 月下调至 3-9 月）

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

## 5. 执行状态

- 提案正文：✅ 三份齐
- T5 提案正文（2026-08-13 增）：✅ `T5_companion_prob_shield.md`；P-EmoAgent AI 离线资产终审 `CODE/STAT/CLAIM=PASS`，41 项工程测试 + 19 项固定复算测试通过，local integration=`AI-ASSETS-READY`；真实后端/真实 E2 未开始，教学待用户，上游许可与公开发布 `NO-GO`；本状态不代表 EmoGuard 效果已验证或论文复现完成；实验 ⬜
- W4 雷区回填：✅ T2 保证链已主控收窄
- EvoAgent Fusion-0：✅ XES + GraphML 双出口
- 实验：⬜ 未开始
- BR-2 完成条件：提案部分 ✅；toy+arXiv ⬜
- OE-1：v4 草稿 ✅；占位+BR-1 后分支确认 ⬜
