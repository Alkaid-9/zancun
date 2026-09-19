# CODEX 作业书 · 鲁线全量验收＋F1 命题1 可行性试验＋复现（2026-08-24）

> **给 Alkaid 的使用说明**（本节不粘给 codex）：
> 1. `cd /mnt/d/MyResearch/MAS_Safety_Project` 后起 codex——它自动读仓内 AGENTS.md 获得仓库规则；
> 2. **先贴 §一 公共头**（一次），再按顺序贴 §四 启动令 A→B→C；册 A 是只读的，codex 用默认/read-only 沙箱即可；册 B 需要写权限（它会自己申请）；
> 3. 每册跑完把 codex 尾报贴回 Claude 窗，我方做汇裁登记（codex 是 OpenAI 谱系＝真异构验收者，它的 FAIL 比 Claude 自审值钱）;
> 4. 预算参考：册 A ≈30-60 分钟、册 B ≈60-120 分钟、册 C 以阶段为单位另约。
> 5. 若 codex 中途要装依赖（numpy/pandas 等），属预期，放行即可；要改仓内正本文件的请求一律拒绝并贴回给我。

---

## §一 公共头（先贴这段）

```
你是鲁法明论文研究线的独立验收员与实验工程师。工作目录=/mnt/d/MyResearch/MAS_Safety_Project。
鲁线产物在 research/papers_lu/teardown-joint-20260813/。你与产出这些材料的 Claude 谱系完全独立，
你的价值恰恰在于不带它的任何预设——一切以你自己读到的原文和算出的数字为准。

全局纪律（违反任一条=本次作业无效）：
1. 数值表禁手填：凡转录≥4行数值且需运算的表,必须脚本逐项生成并留档脚本;报告注明"脚本生成可复算"。
2. 独立取证：需要 PDF 原文数据时,用 pdftotext 自己提取(命令自定),禁止读 _launch/pdftxt/ 下
   的现成提取件(那是被审方的处理品);禁止读任何 _audit_*/ 目录里的结论性文字后再"验证"它——
   先算后看,顺序不可反。
3. FAIL 纪律：任何判据不达标只能如实标 FAIL 并给出复算路径,禁止静默放宽口径或调参救回;
   调参最多 2 次且每次必须记录前后差异。
4. 禁区: research/sun/phase1/papers/_review_20260815/** 只读禁区零写入;所有 *_archive_* 目录只读;
   不 git commit/push;不改仓内既有正本文件——你的一切输出写到
   research/papers_lu/teardown-joint-20260813/_codex_20260824/ 下(可新建)。
5. 输出契约:每个检查项 verdict ∈ {PASS, FAIL, WAIVER(必须附理由), INCONCLUSIVE(附缺什么材料)};
   最终回执含字段: files / tests / spec_coverage / open_questions / verdict。
6. 凭据卫生:不读取、不引用、不输出任何 API key/cookie/凭据。
```

## §二 册 A · 全量验收判据（这是你要的"验收指标"，全部量化）

### A1 数值链全重验〔权重最高〕
对象: `_audit_remediation_20260824/A4_pdf_verification.md` 的比值重算表与终判数字。
独立路径:
- `pdftotext -f 14 -l 14 /mnt/d/MyResearch/DeadlockSeg-2026-TST.pdf -` 取 SegLock Table 5（p.14）;
- `pdftotext -f 24 -l 24 /mnt/d/MyResearch/Deadlock-2024-IEEEAccess.pdf -` 取 PNULOCK Table VII（p.24）;
- 自己转录 8 个共享基准(Test1a/1b/2a/3/4/6/7/8)三列数值 → 脚本重算加速比(PNULOCK T VII 同名检测列 ÷ SegLock T5 SegLock 列)、范围、中位。
PASS 判据(全部满足):
1. 你转录的 T5 PNULock 列与 T VII 同名真值 **8/8 全部不等**,且呈"上移一位"对应关系(T5 的 Test1b 值=T VII Test1a 值…),T VII Test8=0.639 未被任何共享名使用;
2. 你的真实加速比 8 项与 A4 报告表逐项一致(容差 ±0.0005,舍入级);
3. 范围≈1.70–6.35×、中位≈2.76×(差<0.01);
4. 复核 A4 §终判第1条定性:"范围宣称大体成立(整体量级非逐项保证)+名实错位非注水"是否被上述数字支撑——给出你自己的独立措辞评价。

### A2 教学 B 卷判分锚验算
对象: `teaching/learner_workbook.md` 四道 B 题(1.2B/2.2B/3.2B/4.2B)的主考判分锚。
方法:不看锚先自答——按各题题干独立推导数值链(涉及 SBTPN 式(6)-(8):λ⁺=(ψ₂−ψ₁)/(1−ψ₁)、λ⁻=(ψ₁−ψ₂)/ψ₁、式8=算术平均、[0.5,δ] 门槛;公式定义见 01 卡 §2.3 或 06 卡),然后对照锚文本。
PASS 判据:四题锚中每条数值断言与你的推导一致;不一致处逐条列出(每一条都是 P0 级教学事故候选)。

### A3 勘误指针面一致性巡检
方法: `grep -rn "1/2–1/6" research/papers_lu/teardown-joint-20260813/ --include="*.md"` 排除 _archive_*/_launch/_audit_finishing/_review 路径后逐处检查:
1. 每处应带 08-24 勘误指针且指针内数字=A4 口径(真实 1.70–6.35×/中位 2.76×);
2. 对照 task log(`progress/task_logs/2026/08/2026-08-24__research__lu-line-quality-remediation.md` R1-a 行)的"4 处合理保留清单",核对裸引用残留与清单相符、无新裸引用。
PASS 判据:零未登记裸引用;指针数字零偏差。

### A4 F1 卡逻辑审
对象: `bridge/D1D2_closure_bridge.md`。检查:
1. 三命题各自有无可证伪表述+量化门槛+kill criteria(缺一即 FAIL 该命题);
2. §6 面谈话术主句是否为"已设计"版(出现完成时态实验宣称而无数据支撑=P0);
3. 竞对核查声明抽查:对卡中列的近邻竞对任选 2 个联网检索,确认"Bayesian×Petri deadlock 结构化耦合无人占据"的声明当前仍成立(若发现新占位者,给出论文名+占据点)。

## §三 册 B · F1 命题1 可行性试验(合成数据)

目标: 验证 D2 检测器假阳性环 → 三层接口管道 → SBTPN 式(6)-(8) 概率归因排序 这条链在**合成数据**上能否达到命题 1 门槛。
背景读三件(按序): `bridge/D1D2_closure_bridge.md`(命题与管道规格) → `repro/sbpn/` 里式(6)-(8) 的已验证实现(直接复用其代码层) → `06_SBPN.md` §公式(参数含义)。

**合成样本协议**(固定 seed=20260824):
- 一个样本 = 一个模拟死锁场景:真根因锁对 (a,b) + k 个干扰环(k~Uniform[2,5]),干扰环与真根因共享 0-1 把锁(制造歧义);
- 每环生成事件时间戳序列(锁获取/释放/等待),叠加噪声抖动;
- 变量化映射:每环 → 报警变量(环规模/等待总时长/锁重叠度等 ≥3 个特征,映射规则写死在脚本里);
- 时序对齐:按事件窗口聚合到统一时间轴(管道第 3 层);
- ψ₁/ψ₂ 统计量取自 repro/sbpn 实现层的同构定义;排序输出=各环的式(8) 归因分。
规模: N≥50 样本。

**指标与判定**:
- 主指标 = top-1 命中率(真根因环排第一的样本占比);命题 1 门槛 **≥50%**;
- 副指标 = top-3 命中率;基线对比 = 随机排序(期望 1/k̄) 与"最大环优先"启发式;
- kill criteria(照抄 F1 卡,不得修改): top-1 <50% ⇒ 命题 1 判 FAIL,降级为串联管道定位;
- 调参 ≤2 次,每次记录改动与前后指标。

DoD: 结果 md 含 verdict ∈ {PASSED, FAILED, INCONCLUSIVE} + 主副指标 + 基线对比表(脚本生成) + 种子与复跑命令;代码与数据落 `_codex_20260824/f1_prop1/`;明确声明"合成数据可行性验证,非论文级实验,结论仅用于面谈话术分级"。

## §四 册 C · 论文复现(按预注册 DoD 执行)

先读 `repro/C0_repo_check_dod_preregistration.md` ——三线判据已预注册,**全文有效,不得事后放宽**。要点:
- **C1 SBPN 主实验层**(最优先): SBPN 官方仓纯数据无代码 → 按 C0 锁定的重建路线走;公式层以 repro/sbpn 已 PASS 的 29 项数值锚为底座向上重建主实验(RCA 准确率 vs SOTA 对比线);FAIL 只能标 FAIL;
- **C2 EdgeIM**: 注意 ds-kiel/EdgeMiner 是 Kiel 组先行项目非官方实现(C0 已裁定不影响判据);
- **C3 MHP**: 无官方仓,维持重建路线。
建议节奏: 本次会话只做 C1 第一阶段(公式层→主实验层的脚手架与数据管线),跑通端到端一个 batch 即收,余量另开会话。产出落 `_codex_20260824/c_repro/`,回执同公共头契约。

## §五 启动令(依次粘贴)

```
【启动令 A】读 CODEX_ACCEPTANCE_BRIEF_20260824.md 的 §一 与 §二,执行册 A 全部四项(A1-A4),
按输出契约出验收报告到 _codex_20260824/a_acceptance/report.md。先算后看,独立取证。
```
```
【启动令 B】读 brief §三,执行册 B F1 命题1 可行性试验。严格按合成样本协议与 kill criteria,
结果到 _codex_20260824/f1_prop1/。这是写代码任务,需要 workspace-write 权限。
```
```
【启动令 C】读 brief §四 与 repro/C0_repo_check_dod_preregistration.md,只做 C1 第一阶段,
端到端跑通即收。结果到 _codex_20260824/c_repro/。
```

---

*作业书版本 v1(2026-08-24)·作者=Claude 主窗 TASK-20260824-007·汇裁权在 Claude 窗与用户*
