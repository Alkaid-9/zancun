# B-EVAL Training Fixture

虚构数据，仅训练审计方法：

| log | method | fitness | precision | discovery | sampling |
|---|---|---:|---:|---:|---:|
| X | Base | 0.80 | 0.50 | 100 | N/A |
| X | New | 0.75 | 0.70 | 70 | 20 |
| Y | Base | 0.90 | 0.60 | 80 | N/A |
| Y | New | 0.90 | 0.55 | 60 | 25 |

作者文字：“New 在所有日志上更快、更准确，并降低了通信且保证 soundness。”

任务：

1. 复算四行 harmonic F-measure。
2. 计算 New total time，并判断“所有日志更快”。
3. 分别判断“更准确”“降低通信”“保证 soundness”需要什么证据。
4. 写一条最窄可辩护 claim 和一条 `REPRO-CONTRACT-OPEN` 清单。
5. 使用 rubric 已冻结的 `<=1e-4` 绝对误差；先声明显示位数和舍入方式，不得自行放宽 tolerance。
