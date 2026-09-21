# A5 EX-05 运行预检

状态：`INPUTS-FROZEN / REVIEW-PASS / REVIEWER-PREFLIGHT-WITHHELD / USER-FIRST-RUN-PENDING`

AI 已执行 reviewer-only 隔离预检，但在你的三条预测和首次运行回执落盘前，本页不披露它的退出码、stdout、数字或存放路径。原始证据留给复核者，不是学习输入。

## 固定输入

| 对象 | 路径 | SHA-256 |
|---|---|---|
| 正式 WIP | `/mnt/d/Alkaid/Desktop/zancun/02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-05/test_invariants.py` | `0eff7611a6f45cab213b7eb47a37ecafba540a3a6ab9ce2c555c0ef54cbeb3f0` |
| 探索 WIP | `/mnt/d/Alkaid/Desktop/zancun/02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-05/own.py` | `8a76cb097ae898c38241b1c7adc31721e8a428041416622e345392db7529dcb4` |
| 公开生成器 | `/mnt/d/MyResearch/MAS_Safety_Project/research/edgeim_sampling_audit/src/pilot.py` | `7c7a4bcb212f47566207be4e6092c2130a1db7e6fd345a0baec4cf6439556b53` |

Python：`/home/alkaid/miniconda3/envs/solver/bin/python`，开工版本 `3.10.19`。

## 安全试走方式

- 不在旧 EX 目录运行。
- 把 `test_invariants.py` 复制到 `mktemp -d` 创建的临时目录。
- 用 `PYTHONDONTWRITEBYTECODE=1` 和 `python -B` 阻止向导入源写 `__pycache__`。
- 绝对导入路径仍只读指向原 MAS 源代码。
- stdout、stderr、exit code、cwd、命令和输入哈希由复核者写入隔离运行证据目录；本人首次回执前不在学习入口披露路径。
- 试走后重算上表哈希并检查两个仓的相关 Git diff。

## 预检命令

```sh
trial_dir=$(mktemp -d)
cp '/mnt/d/Alkaid/Desktop/zancun/02_四论文Ownership主线/01_EdgeIM/学习与课程/EX-05/test_invariants.py' "$trial_dir/test_invariants.py"
cd "$trial_dir"
PYTHONDONTWRITEBYTECODE=1 /home/alkaid/miniconda3/envs/solver/bin/python -B test_invariants.py
```

不要用这条命令直接跑 `own.py`；它是输出较多的探索稿，且不是题面指定正式交件。

## 失败记录

```text
run ID：
exit code：
stderr 首个异常：
traceback 第一个相关代码行：
保留的原始日志：
竞争解释：
下一个最低成本检查：
```

即使 exit code 为 0，也只能说“该固定版本在本次环境和列出的有限输入上执行完成”，不能说 EX-05 PASS、本人掌握或性质已普遍证明。
