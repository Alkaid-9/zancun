# Bug Report #2：高风险预警"抢跑"，不等风险个案建好就被放行

**报告人**: 后端值班（高风险演练复盘）
**严重度**: 高（触碰风险处置流程规范）
**分支**: `training/ex03`

## 现象描述

高风险处置的流程规范是：检测到高风险 → 写台账 → **先创建风险个案** → 个案建好后再向值班咨询师发送预警（预警要能对应到已建好的个案，方便点开跟进）。

本周做高风险演练时发现时序不对：

- 审计时间线上，预警发送动作的时间点**早于**建案任务完成的时间点（时间线倒挂）；
- 有一轮演练中建案任务还在排队/重试中，预警就已经发出去了，值班老师点开预警时跟进链路不完整；
- 该现象在演练环境稳定出现，不是偶发抖动。

基线 commit（9e1e239）上跑同样的演练，时序是正确的（预警一定等建案成功之后）。

## 复现步骤

环境说明：无需 MySQL/Redis/Ollama，用内存 sqlite 即可复现。以下命令假设已检出 `training/ex03` 分支；`<CHECKOUT>` 代表检出目录（如为 git worktree，Python 解释器请用主仓 venv 的绝对路径）。

将下面的最小复现脚本存为 `/tmp/repro_alert_gate.py`（模拟一条高风险报告入队后，检查调度器此刻是否放行预警任务）：

```python
"""最小复现：高风险报告入队后，检查预警任务此刻是否被放行。"""
from types import SimpleNamespace

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base
from app.core.enums import ToolJobKind
from app.models.entities import PsychologicalReport
from app.services.tool_queue import ToolQueueService, ToolQueueWorker

engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
db = sessionmaker(bind=engine, autoflush=False, autocommit=False)()

settings = SimpleNamespace(
    tool_queue_enabled=False,
    tool_queue_max_attempts=3,
    tool_queue_excel_workers=1,
    tool_queue_email_workers=1,
    alert_email_rate_limit_per_minute=30,
)

report = PsychologicalReport(
    user_id=1, session_id=1, content="高风险样例输入", intent="RISK",
    emotion="HIGH_RISK", emotion_score=4.0, risk_level="HIGH",
    confidence=0.95, summary="repro",
)
db.add(report)
db.commit()
db.refresh(report)

jobs = ToolQueueService(db, settings).enqueue_report(report.id, report.risk_level)
case_job = next(job for job in jobs if job.kind == ToolJobKind.CASE_CREATE.value)
alert_job = next(job for job in jobs if job.kind == ToolJobKind.ALERT_SEND.value)

worker = ToolQueueWorker(settings)
ready = worker._dependency_ready(db, alert_job)
worker.stop()

print(f"case_create 任务状态: {case_job.status}")
print(f"alert_send 此刻是否被放行: {ready}")
```

运行：

```bash
cd <CHECKOUT>/mindbridge-py
PYTHONPATH=<CHECKOUT>/mindbridge-py /mnt/d/Workspace/mindbridge/mindbridge-py/.venv/bin/python /tmp/repro_alert_gate.py
```

实际输出：

```
case_create 任务状态: PENDING
alert_send 此刻是否被放行: True
```

## 期望行为

建案任务（case_create）尚未执行成功（仍为 PENDING/RUNNING）时，预警任务（alert_send）**必须处于等待状态**（上面脚本应输出 `False`）。只有建案成功后预警才允许被执行。基线 commit 上该脚本输出 `False`。
