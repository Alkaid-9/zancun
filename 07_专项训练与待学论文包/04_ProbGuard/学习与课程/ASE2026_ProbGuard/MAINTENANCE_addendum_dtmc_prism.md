# 维护手册 · ADDENDUM_DTMC_PRISM_FORMAT(DTMC→PRISM 格式笔记)

**日期**:2026-08-14 | **维护对象**:`ADDENDUM_DTMC_PRISM_FORMAT.md`(下称"笔记")及其两处下游引用(T5 §9 指针行、本目录 README 登记)
**配套**:使用手册 `GUIDE_addendum_dtmc_prism.md` | 交接档 `progress/handoff/2026-08-14__lightwindow-probguard-dtmc-format__handoff.md`

---

## §一 单一事实源与裁决顺序

1. 格式断言的**事实源 = `external/Pro2Guard` commit `ab2f4ab` 的源码原文**;笔记与源码冲突 → 以源码为准并修笔记。
2. 工程语义(哪能跑/怎么修/12 坑)的事实源 = teardown(`research/map/oss_landscape/teardowns/ProbGuard_AgentSpec.md`);笔记不与其重复,只交叉引用。
3. 层纪律:V-HEAD/V-产物/V-README 三层断言不得互相混写(笔记 ⓪);维护时新增任何断言先定层。

## §二 更新触发器(谁动了什么 → 改哪里)

| # | 触发事件 | 动作 | 辖区 |
|---|---|---|---|
| T1 | `external/Pro2Guard` 被拉新 commit(不再是 ab2f4ab) | 跑 §四 机械抽查;行号漂移则全文重核;笔记头部 commit 锚更新;若上游修好 runtime_monitor,§7 整节重写 | 谁拉新谁触发,精读窗执行 |
| T2 | W-复现窗(LP-01)P0/P2 实测完成 | 回填台账 L1(filter 语法)/L3(样例 B Result 值);"待复现窗实测"字样消解;若 P2 重跑产出新 dtmcs,§6.3 对照表补"新产物"列 | LP-01 窗 |
| T3 | T5 谓词表 v0 冻结或改版 | 校验 §⑨ 六列定义与 v0 实际列名一致;bit 序变更 → 笔记 §3.2 警示句同步 | T5 辖区窗 |
| T4 | `git fetch --unshallow` 考古完成 | 〔反推〕三项(旧版分子 α 条件化/剪枝/Fraction)改为实证或修正;台账 L2 消解 | 需用户允许网络 |
| T5 | `DEC-T5-NUMBERING` 拍板(T5 改号) | 笔记/GUIDE/本手册/交接档内"T5"引用加限定或改号 | 拍板窗连带 |
| T6 | 本目录重组(05_REPRODUCTION/ 建立等) | README 树与两处 INDEX 指针同步;笔记不动 | 重组窗 |

## §三 登记规约(动哪里登哪里)

- 改**本目录**文件(笔记/双手册/README):登 `research/sun/phase1/papers/INDEX.md` ProbGuard 行(状态格)+ 目录 README"最后更新"。
- 改 **map 辖区**(T5 提案、oss teardown、CHANGELOG):按地图铁律登 `research/map/CHANGELOG.md`。
- 窗口级变更(新精读窗/复现窗动本笔记):交接档落 `progress/handoff/` 并在其 INDEX §1 加行。

## §四 机械验证命令集(每次 T1 触发或月查跑;全部只读)

```bash
cd /mnt/d/MyResearch
# 0) commit 锚未漂移(期望输出 ab2f4ab*)
git -C external/Pro2Guard rev-parse --short HEAD

# 1) 关键行抽查(行号+内容双匹配;任一 miss = 行号漂移,触发全文重核)
rg -n 'denom \+= count \+ \(alpha if abs\.valid_trans' external/Pro2Guard/src/safereach/build_model.py   # 期望 :63
rg -n 'f"\{n\+alpha\}/\{denom\}"' external/Pro2Guard/src/safereach/build_model.py                        # 期望 :69
rg -n 's : \[0\.\.\{K\}\] init' external/Pro2Guard/src/safereach/build_model.py                          # 期望 :108
rg -n 'pctl_formula = f"P=\? \[ G !\{state\} \]"' external/Pro2Guard/src/safereach/runtime_monitor.py    # 期望 :46(损坏行仍在=HEAD 未修)
rg -n 'FINISH = "finish"' external/Pro2Guard/src/safereach/abstraction.py                                # 期望 :4
rg -n 'def convert_to_bool_var' external/Pro2Guard/src/safereach/autonomous_vehicle/abstraction.py       # 期望 :98

# 2) 样例 B 参照物未被改动(runtime_monitor 副作用会改 init!期望 init 0;若非 0 = 有人跑过监控,笔记 §6.3 需记录)
rg -n 'init' external/Pro2Guard/src/safereach/embodied/dtmcs/merged_log_raw_t3/dtmc.prism

# 3) 下游指针存活(期望各 ≥1 命中)
rg -l 'ADDENDUM_DTMC_PRISM_FORMAT' MAS_Safety_Project/research/map/proposals/T5_companion_prob_shield.md MAS_Safety_Project/research/map/CHANGELOG.md MAS_Safety_Project/research/sun/phase1/papers/ASE2026_ProbGuard/README.md
```

## §五 引用纪律(禁语与限定,写作窗同守)

- 不得写"ProbGuard 的导出格式是 X"而不带层声明(HEAD 代码/仓内产物/README 宣称三选一)。
- 〔反推〕项外引必须保留"由产物数字反推"限定;台账 L2 消解前不得升级为事实句。
- 不得写"格式已实测/管线已跑通"(本窗零执行;可跑性主张属 LP-01 窗,以其 E2 裁定词为准)。
- 样例照抄须注明 A/B/C 来源;样例 B 数值属旧版产物,不得当 HEAD 预期输出。

## §六 遗留项台账(活账;消解后划线并注日期)

| # | 事项 | 辖区 | 状态 |
|---|---|---|---|
| L1 | `filter(printall, P=? […], true)` 语法未经 PRISM 实测(笔记 §7.2 标注) | LP-01 P0 | 开 |
| L2 | 〔反推〕三项待考古(`git fetch --unshallow`,需网络+用户) | 可选窗 | 开 |
| L3 | 样例 B 冒烟 `Result:` 数值未实测,实测后回填笔记 §7.3 注释 | LP-01 P0 | 开 |
| L4 | T5 提案文件存在 P-EmoAgent 窗并发未提交修改(status 行/§5 许可措辞;2026-08-14 00:55 git diff 实见,与本窗 §9 一行不冲突)——仅记录在案,commit 时两窗改动会同批入库 | 无需动作 | 记录 |
| L5 | 谓词表 v0 补 §⑨ 六列(bit_index/lhs-op-rhs/bool_var/时间窗/unsafe/absorbing)并冻结行序 | T5 辖区窗 | 开 |
| L6 | papers/INDEX ProbGuard 行已刷新(轻窗 addendum);LP-01 收官时再刷新一次拆解深度格 | LP-01 | 开 |
| L7 | **并发复现窗实见**(2026-08-14 01:06–01:09,本手册落盘同时):`05_REPRODUCTION/{patches/constraints-langchain.txt, prism-build/prism/}` 被另一窗口创建,PRISM 4.8.1 发行版整套拷入且 `bin/prism` 01:09 被改写(install.sh 迹象)= **LP-01 复现窗已实际开工**。本轻窗零参与;该窗收官后:双手册 T2 触发器生效(回填 L1/L3),README"待补 05_REPRODUCTION"行由其接管 | LP-01(在途) | 记录 |

**最后更新**:2026-08-14
