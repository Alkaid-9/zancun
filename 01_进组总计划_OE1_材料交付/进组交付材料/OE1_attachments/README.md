# OE1 邮件附件暂存（2026-08-22 四块执行窗块④代办）

## 是什么

给鲁老师邮件的候选附件资产，包含离线规则流水线与合成轨迹的历史演示；不能仅凭文件存在证明当前环境管线可运行或本人实现。

> **2026-09-20 核查上限**：已检查文件存在与生成器关键代码，未执行生成器或 notebook，未重新验证旧数字。下方“真实运行/完成”均是历史来源标注，不是本次复跑回执。生成器依赖失败会降级，故未来复跑须核实实际走到的分支及新产物，不能只看退出码或旧文件。

## 文件清单

| 文件 | 性质 | 说明 |
|---|---|---|
| `make_demo_assets.py` | 生成脚本 | 一键重建 cases/ 全部内容 |
| `cases/task_real_harness.xes` | **真实运行** | `TaskStore + ReviewHarness(LocalRuleReviewer)` 离线真实流水线导出（无 LLM、无网络；diff 为本地构造字符串，仓库名为占位符） |
| `cases/task_variant_01..04.xes` | **合成演示** | 同一导出代码路径（`build_process_events`/`build_xes`）生成的变体轨迹：失败终态 / 重试成功 / 取消 / 代理故障恢复。**非真实运行，对外展示时必须保留此标注** |
| `manifest.json` | 台账 | 每份文件的性质登记 |
| `mine_dfg.py` | 挖掘脚本 | 合并 cases/ 五份 .xes → 频率/性能 DFG PNG ×2（pm4py 2.7.23.6 + Graphviz dot，幂等更新台账） |
| `pm4py_mining_demo.ipynb` | 演示 notebook | 同管线交互版（仓库内已带执行输出），另含归纳 Petri 网 + 重放拟合 |
| `mining/` | 挖掘产物 | `all_cases_merged.xes` + `dfg_frequency.png` + `dfg_performance.png` + `petri_net_inductive.png`（标题/口径保留真实与合成标注） |

## 过程挖掘（2026-08-24 历史记录，本轮未复跑）

- solver 环境 `pm4py-2.7.23.6` 已装（系统 `dot` 2.43.0 在 PATH）
- `mine_dfg.py`：合并 cases/ 五份 .xes（23 events / 5 cases）→ `mining/` 下三产物：
  - `all_cases_merged.xes` 合并日志（复现用中间产物）
  - `dfg_frequency.png` 频率 DFG（终态分布 success×3/failed×1/cancelled×1，与语料设计吻合）
  - `dfg_performance.png` 性能 DFG（边标 mean 耗时 45s~2m，演示级间隔）
- 两张 PNG 标题均带「1 real run + 4 synthetic demo traces」标注；manifest.json 已登记（MINED ARTIFACT ×3）
- `pm4py_mining_demo.ipynb`（08-24 用户拍板加做）：同管线交互版，执行输出已内嵌（0 错误 / 3 图），另含归纳 Petri 网（13p/17t/38a）+ 重放拟合 1.0（平凡性已在 notebook 内标注，不构成质量论断）

## 邮件引用口径（须本人复核后才使用）

> 附上经本人复核的 XES 演示样例：[实际复核范围和协助边界]。其中本地规则评审器路径不调用 LLM，四份变体是合成轨迹；这些演示不代表真实 LLM Agent 实验、论文完整复现或安全效果验证。

铁律 1 合规：不把合成轨迹说成真实运行。
