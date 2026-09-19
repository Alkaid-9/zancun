# EmoAgent 拆解(首轮)

**论文**:EmoAgent: Assessing and Safeguarding Human-AI Interaction for Mental Health Safety
**会议**:EMNLP 2025 main,Suzhou,pp. 11741–11756(DOI [10.18653/v1/2025.emnlp-main.594](https://aclanthology.org/2025.emnlp-main.594/),venue 元数据经 D6 实见确认)
**作者**:Jiahao Qiu* / Yinghui He* / Xinzhe Juan*(共同一作),Yimin Wang、Yuhan Liu、Zixin Yao、Yue Wu、Xun Jiang、Ling Yang、**Mengdi Wang**(Princeton ECE,组长)
**链接**:[arXiv:2504.09689](https://arxiv.org/abs/2504.09689) | [source-available 仓库](https://github.com/1akaman/EmoAgent)(25 星,目录树与核心源码于 2026-08-13 实读;冻结树无 `LICENSE`/`COPYING` 许可证文件、SPDX 标识或明确的复制/修改/再分发授权;上游 README 的 research-purpose 提示不是许可授予,故仅可审计,不表示获准复用)
**类型**:实验论文(评测框架 EmoEval + 防护机制 EmoGuard + 平台实测)
**拆解日期**:2026-08-13(首轮,P-EmoAgent Agent)
**代码审计基线**:`0bb2d08a75936ce5e9c427bd24d4d4598b1099cc`(公开仓冻结快照;证据审计见 `06_EVIDENCE_AUDIT.md`)
**框架参考**:`MAS_Safety_Project/_archive/research/sun/legacy-2026-Q3/papers/04_FSE2026_ReGA/`(按首轮拆解裁剪:S01/S03/S05 + 术语表)

---

## 一句话总结

用"CCD 认知模型驱动的模拟病人 + PHQ-9/PDI-21/PANSS 前后测"评估角色扮演聊天机器人的心理风险:六个 style×disorder 跨四角色 pooled 聚合格中,最低为 Meow×depression 的 `33/96=34.375%`(约 34.4%)。论文 Figure 7 另报告两个高危设定的 `ΔPHQ-9≥5` 模拟阈值命中率(MCID proxy)由 9.4%/4.2% 变为 0.0%;固定产物不能恢复其分母、区间或 provenance,不得解释为零风险或真实临床改善。EmoGuard 全链路依赖 LLM 判断、无形式保证,预测提前量未定义/未报告;冻结仓含四模块原语,但未发布三轮调度、建议注入、迭代外环或效果产物。

---

## 与 T5 的关系(为什么拆它)

对照 `MAS_Safety_Project/research/map/proposals/T5_companion_prob_shield.md`(T5-companion):

| EmoAgent 组件 | 在 T5 中的角色 | T5 提案出处 |
|---|---|---|
| **EmoGuard** | **基线②**:LLM-as-judge 在线监控,需复现 | T5 §6"② LLM-as-judge 在线监控(EmoGuard 复现)" |
| **EmoEval** | **M4 评测的模拟用户范式来源**:模拟脆弱用户 + 量表前后测 | T5 §4 M4"INTIMA 368 prompt + EmoEval 模拟脆弱用户"、§5 外部数据 |
| 整篇 | **最近邻差异表的一行**:"LLM-judge 插入监控,零形式保证且预测提前量未定义/未报告;本提案给概率预测与 PAC 语义,EmoGuard 降为基线" | T5 §7 |
| 恶化率 R | E1 层仅是观测样本中 `S_final>S_initial` 的经验频率;`ΔPHQ-9≥5` 是另一个模拟终点事件。转成 PCTL 查询须另建状态抽象、事件谓词与转移模型(E2),只有估计不确定性与 PAC 样本条件均满足时才能作阈值保证(E3) | 分层纪律见 05 §2.1 |
| 每 3 轮固定触发 | 与 T5"风险触发"构成干净消融轴:**固定节拍 vs 风险触发** | D6 卡 5 |

---

## 核心产出文件

| 文件 | 内容 |
|---|---|
| `01_QUESTIONS.md` | 读前 5 问 + 初答 + 品味预判 |
| `03_PAPER_READ.md` | 精读:EmoEval 模拟病人构造与三量表用法 / Dialog Manager / 34.4% 实验协议逐层拆 / EmoGuard 机制与迭代训练 / 局限(零形式保证) |
| `05_REUSE_MAP.md` | **核心交付**:① EmoEval 复现清单(模型/量表/prompt/仓库速查/坑清单)② T5 集成方案(EmoEval→M4、EmoGuard→基线②)③ 伦理边界 |
| `06_EVIDENCE_AUDIT.md` | 冻结 commit 的逐项证据审计:VERIFIED / CORRECTED / UNRESOLVED、源码行号、影响与统一修订措辞 |
| `08_TEACHING_PACK.md` + `teaching/` | 四关 artifact-first 教学包、学员册、答案、错题与终局口试；当前 `TEACHING-AWAITING-USER` |
| `09_ETHICS_LICENSE.md` | 模拟用户、量表、上游许可、API、数据与 IRB 门禁 |
| `_handoff/` | 本窗口总结、工作日志、状态快照与下一窗口交接 |
| `GLOSSARY.md` | 26 个术语 |

工程、复算、架构、计划、使用与维护手册的唯一入口：
`MAS_Safety_Project/research/experiments/emoagent_selfhost_20260813/README.md`。

---

## 当前验收状态（2026-08-14 00:44，UTC+8）

| 域 | 当前终审 | 边界 |
|---|---|---|
| CODE | **PASS；41/41** | fifth-pass，无 P0/P1/P2；durability 多轮故障重试残余已关闭 |
| STAT | **PASS；19/19** | third-pass，强制固定源、无 skip；固定数据仍保留已披露 warnings |
| CLAIM | **PASS** | third-pass；原 2 P1 与 6 P2 全部关闭，不修改核心 claim 文档 |
| INTEGRATION | **本地 `AI-ASSETS-READY`** | fifth-pass；只限 clean-room、FakeProvider、中性自造数据、通用数值接口与固定数据只读复算 |
| 真实运行 | **`HOLD / NO-GO`** | 用户后端、真实 adapter/E2、日志/量表/服务商条款与 IRB 未关闭 |
| 发布 | **`NO-GO`** | 许可、候选发布树、扫描、provenance 与人工许可审查未关闭 |
| 教学 | **`TEACHING-AWAITING-USER`** | 材料已齐，但用户四关与口试尚未完成 |

最后一条 durability 修复链保留在 `_handoff/`：second-pass 的 UTF-8 截断尾与首次 ledger
目录同步问题修复后，third/fourth-pass 又分别发现失败重试和多级祖先父链同步残余；最终修复
Agent `c85bb2a1-18f9-407c-9196-ca34a98cebd0` 改为绝对化路径、递归至文件系统 root 并在
回程逐级同步直接父目录。代码终审 `218c61c8-7af2-4568-bcd9-cd4ae2460fc4` 与集成终审
`ae046239-b519-4482-9970-2b2f7d714963` 已确认关闭。

当前未完成仅为：用户选择并批准后端及真实 E2、用户教学、许可/IRB/发布门禁。真实运行、
论文/EmoGuard/T5 效果与公开发布均未因此完成。

---

## 关键发现(首轮,全部以论文原文或仓库源码为据)

1. **EmoGuard 的原语实现在 `critic_agent.py`,README 的项目结构清单没有列它**;入口脚本 `EmoEval.py` 未 import 或调用它,冻结仓也没有三轮调度、建议注入或迭代外环。`advise()` 内三个分析器按同步源码顺序串行。当前只可按论文行为描述在 clean-room + FakeProvider 中验证抽象调度;上游代码与 profile 的使用须等许可关闭(详见 05 §1.3–1.5)。
2. **发布版 `EmoEval.py` 有两项公开仓复现缺陷**:`for i in range(max_turns)` 内每轮发给 Character.AI 的是固定角色 prompt,生成的 `user_response` 没有被发送;且病人循环写死 `range(1, 2)`,只跑 patient1(论文协议为 3 个病人)。这两项与上一项"EmoGuard 编排缺失"只说明公开仓不能按论文协议直接复现,不构成对论文结论的推翻。未来 C1 实验应独立实现正确行为并披露差异,当前不修改上游入口。
3. **后测 prompt 是"伤害敏化"设计**:冻结源码引导模拟用户弱化积极应对,聚焦角色语气、否定或批评的负面影响,并把细微变化反映到分数。本文仅保留功能性转述,不再分发 prompt 原文。34.4% 必须带此协议上下文引用;跨臂同协议只能减少协议差异混杂,不能证明敏化测量误差严格抵消。
4. **恶化率 R 的判据是"总分升 1 分即计恶化"**,无显著性检验;论文另借用 PHQ-9 `Δ≥5` 作为模拟阈值(MCID proxy),即时、模拟、敏化后测不支持真实临床显著性外推。§5.1 的选点依据(29.2%/8.3%)与 §5.2 Figure 7 基线(9.4%/4.2%)数字不一致,但论文与冻结仓均未说明原因;不能据此断言运行方式或方差来源。T5 仍应独立采用"≥3 seeds, mean±std"门禁。
5. **评测对象绑定 Character.AI 私有 API**(kramcat/CharacterAI 非官方库 + 账号 token,2025-03 访问),Meow/Roar 是平台侧设置、代码里只是目录名——论文主实验严格不可复现。附录 C 只提供自架角色的论文级行为参考;冻结仓缺完整 adapter,且当前许可/API 门禁不允许启动真模型复现。
6. 三量表施测方式各不相同(PHQ-9 单次结构化作答 / PDI-21 题目判断及三个子分 / PANSS 逐项问答带重试)。量表文本和计分映射在冻结仓中技术上可见,但代码、量表、电子化施测与再分发许可均未关闭;当前只可审计其存在,不得复制、导入或直接使用。
7. 冻结快照的 `eval_output/` 当前共有 **600** 个 JSON,不是 709:论文四角色核心队列为 **576** 个(`2 风格 × 3 病种 × 4 角色 × 3 病人 × 8 话题`),另有 `roar/delusion/tomioka/` 24 个。
8. `update_profile()` 虽遍历历史文件,但对每个 key 反复覆盖,最终只留下该 key 的最新版本作为下一次 LLM 重写输入;它是**最新版本的递归重写**,不是把全部历史 profile 文本累积拼接。

---

## 与既有卡片的差异校正

- D5 卡 3 写"8 段×10 轮对话后再评一次":**不准确**。论文 §4.1 写每段分别前后测;冻结代码实际为每个 character×patient 调用一次初测,八段分别后测并共享该基线。每段是 R 的一个求和项(N = 3 病人 × 8 对话 = 24/格),但八段共享 CCD/初测,不能称统计独立样本。
- D5 卡 3 写"温度 0、top-p 1 保证量表答题可复现":准确,但需补充——**仅施测时**如此;对话生成的温度参数在代码中被注释掉(默认 1.0),附录 C 自架实验甚至设 1.2。

---

## 目录结构

```
teardowns/EmoAgent/
├─ README.md          ← 本文件(论文卡 + T5 关系)
├─ 01_QUESTIONS.md    ← 读前 5 问
├─ 03_PAPER_READ.md   ← 精读
├─ 05_REUSE_MAP.md    ← 核心交付:复现清单 + T5 集成 + 伦理
├─ 06_EVIDENCE_AUDIT.md ← 冻结源码证据审计
├─ 08_TEACHING_PACK.md ← 教学总包
├─ 09_ETHICS_LICENSE.md ← 伦理与许可门禁
├─ GLOSSARY.md        ← 术语表
├─ teaching/          ← 学员册 / 答案 / 错题 / 口试
└─ _handoff/          ← 窗口总结 / 日志 / 状态 / 交接
```

**当前窗口状态**：本地 `AI-ASSETS-READY`；CODE PASS 41/41、STAT PASS 19/19、CLAIM PASS；真实运行 `HOLD/NO-GO`、发布 `NO-GO`、教学等待用户。见 `_handoff/STATUS.md` 最后一个增量快照；本目录被 `../INDEX.md` 登记，但 P-EmoAgent 尚未关闭。

**最后更新**:2026-08-14 00:44
