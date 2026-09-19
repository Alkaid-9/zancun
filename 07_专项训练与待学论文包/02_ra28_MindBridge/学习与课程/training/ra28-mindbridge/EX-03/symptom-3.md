# Bug Report #3：工程 harness 全线崩溃，外部配置疑似"完全失灵"

**报告人**: CI 值班
**严重度**: 阻断（离线验证通道不可用）
**分支**: `training/ex03`

## 现象描述

仓库自带的离线工程 harness（`app/harness/runner.py`，自配 sqlite + mock AI，本机无需 MySQL/Redis/Ollama 也能整链路跑）在本分支上无法运行：

- 任意 suite 一启动就抛异常崩溃，栈顶是：

```
TypeError: Connection.__init__() got an unexpected keyword argument 'check_same_thread'
```

- 栈里能看到是在建立数据库连接时挂的。奇怪的点在于：harness 明明在启动时给自己配置了 sqlite 数据库，报错却像是连接参数被塞给了另一种数据库驱动；
- 值班同学尝试在 shell 里手动 `export DATABASE_URL='sqlite:///./x.db'` 再跑，结果一模一样，改什么环境变量都像没改一样；
- 同一台机器、同一个 venv，切回基线 commit（9e1e239）harness 六个 suite 全 PASS。

另外有同学反馈 docker-compose 侧的环境变量覆盖行为也变得可疑，但因为本机起不了整套服务，未能单独确认，仅作旁证记录。

## 复现步骤

环境说明：以下命令假设已检出 `training/ex03` 分支；`<CHECKOUT>` 代表检出目录（如为 git worktree，Python 解释器请用主仓 venv 的绝对路径）。

```bash
cd <CHECKOUT>/mindbridge-py
/mnt/d/Workspace/mindbridge/mindbridge-py/.venv/bin/python -m app.harness.runner --suite skills
```

观察：启动即抛 `TypeError: Connection.__init__() got an unexpected keyword argument 'check_same_thread'`，任何 suite（`--suite all` 亦然）都跑不起来。

追加验证（显式给环境变量也无效）：

```bash
cd <CHECKOUT>/mindbridge-py
DATABASE_URL='sqlite:///./x.db' /mnt/d/Workspace/mindbridge/mindbridge-py/.venv/bin/python -m app.harness.runner --suite skills
```

结果与上面完全相同。

## 期望行为

- harness 在无外部服务的机器上应能自配置运行，六个 suite 全 PASS（基线行为）；
- 通过环境变量提供的配置（如 `DATABASE_URL`）应当实际生效，覆盖代码内默认值。
