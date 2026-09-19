"""OE1 附件资产生成器（demo .xes）— 2026-08-22 四块执行窗块④代办。

产出（全部落本目录 cases/ 子目录）：
1. task_real_harness.xes —— 真实 EvoAgent 流水线运行导出：
   TaskStore(SQLite) + ReviewHarness(LocalRuleReviewer) 离线跑通
   PLANNING→EXECUTING→REVIEWING→SUCCESS，再用 task_to_xes 导出。
   无 LLM、无网络、无真实仓库数据（diff 为本地构造字符串）。
2. task_variant_01..04.xes —— 用同一导出代码路径（build_process_events/
   build_xes）生成的变体轨迹（失败/重试/取消/代理故障分支），用于让
   PM4Py 过程挖掘图有分叉可看。这些是**结构性演示数据**，非真实运行，
   邮件与 README 中必须保持此标注。

用途：附给鲁老师 OE1 邮件，证明"EvoAgent 任务数据 → XES → PM4Py 过程挖掘"
管线可用。运行：
    /home/alkaid/miniconda3/envs/solver/bin/python make_demo_assets.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EVOREPO = "/mnt/d/MyResearch/EvoAgent"
sys.path.insert(0, EVOREPO)

from evoagent.process_events import build_process_events, build_xes  # noqa: E402

CASES_DIR = os.path.join(HERE, "cases")


def base_snapshot(task_id):
    """与 tests/test_process_events.py 同构的快照骨架（时间戳全带时区）。"""
    return {
        "id": task_id,
        "state": "SUCCESS",
        "repository": "demo/lab-safety-checks",
        "pull_request": None,
        "input": {"source": "oe1-demo"},
        "report": {"summary": "demo"},
        "trace": [],
        "collaboration": [],
    }


def tr(step, state, ts):
    return {"step": step, "state": state, "message": state.lower(), "created_at": ts}


def col(sender, recipient, kind, ts, correlation_id=""):
    return {
        "sender": sender,
        "recipient": recipient,
        "kind": kind,
        "correlation_id": correlation_id,
        "content": {},
        "created_at": ts,
    }


VARIANTS = {
    # 失败终态：规划后直接失败
    "task_variant_01_failed": (
        [tr(1, "PLANNING", "2026-08-20T09:00:00+08:00"),
         tr(2, "FAILED", "2026-08-20T09:02:00+08:00")],
        [],
    ),
    # 重试成功：执行→失败→再执行→评审→成功
    "task_variant_02_retry_success": (
        [tr(1, "PLANNING", "2026-08-20T10:00:00+08:00"),
         tr(2, "EXECUTING", "2026-08-20T10:01:00+08:00"),
         tr(3, "FAILED", "2026-08-20T10:03:00+08:00"),
         tr(4, "EXECUTING", "2026-08-20T10:05:00+08:00"),
         tr(5, "REVIEWING", "2026-08-20T10:08:00+08:00"),
         tr(6, "SUCCESS", "2026-08-20T10:09:00+08:00")],
        [col("test-agent", "planner-agent", "agent_failure",
             "2026-08-20T10:03:30+08:00")],
    ),
    # 取消终态：评审阶段被用户取消
    "task_variant_03_cancelled": (
        [tr(1, "PLANNING", "2026-08-20T11:00:00+08:00"),
         tr(2, "EXECUTING", "2026-08-20T11:01:00+08:00"),
         tr(3, "REVIEWING", "2026-08-20T11:04:00+08:00"),
         tr(4, "CANCELLED", "2026-08-20T11:06:00+08:00")],
        [],
    ),
    # 代理故障但恢复：专项代理失败→复现验证→成功
    "task_variant_04_agent_failure_recovered": (
        [tr(1, "PLANNING", "2026-08-20T14:00:00+08:00"),
         tr(2, "EXECUTING", "2026-08-20T14:01:00+08:00"),
         tr(3, "REVIEWING", "2026-08-20T14:05:00+08:00"),
         tr(4, "SUCCESS", "2026-08-20T14:07:00+08:00")],
        [col("specialist", "planner-agent", "agent_failure",
             "2026-08-20T14:02:00+08:00"),
         col("test-agent", "synthesizer-agent", "reproduction",
             "2026-08-20T14:04:00+08:00", "finding-1")],
    ),
}


def export_snapshot(name, snapshot):
    xml = build_xes(build_process_events(snapshot))
    path = os.path.join(CASES_DIR, name + ".xes")
    with open(path, "wb") as fh:
        fh.write(xml)
    return path


def main():
    os.makedirs(CASES_DIR, exist_ok=True)
    produced = []

    # 1) 真实流水线运行（离线 LocalRuleReviewer）
    try:
        from evoagent.harness import ReviewHarness
        from evoagent.reviewer import LocalRuleReviewer
        from evoagent.store import TaskStore
        from evoagent.process_events import task_to_xes

        db_path = os.path.join(CASES_DIR, "demo_tasks.db")
        store = TaskStore(db_path)
        store.create("oe1-demo-real", "demo/lab-safety-checks", None,
                     {"source": "oe1-demo"})
        diff = ("--- a/checks.py\n+++ b/checks.py\n"
                "@@ -1,2 +1,3 @@\n def run():\n-    pass\n+    return 'ok'\n")
        ReviewHarness(store, LocalRuleReviewer()).run(
            "oe1-demo-real", "demo/lab-safety-checks", None, diff)
        xml = task_to_xes(store.get("oe1-demo-real"))
        path = os.path.join(CASES_DIR, "task_real_harness.xes")
        with open(path, "wb") as fh:
            fh.write(xml)
        produced.append(("REAL RUN", path))
    except Exception as exc:  # noqa: BLE001 —— harness 链依赖缺失时降级并如实报告
        print("[degrade] real-harness run unavailable: %r" % (exc,))

    # 2) 变体轨迹（结构性演示数据）
    for name, (trace, collab) in VARIANTS.items():
        snap = base_snapshot(name)
        snap["trace"] = trace
        snap["collaboration"] = collab
        snap["state"] = trace[-1]["state"]
        produced.append(("SYNTHETIC DEMO", export_snapshot(name, snap)))

    manifest = [{"kind": kind, "file": os.path.basename(p)} for kind, p in produced]
    with open(os.path.join(HERE, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
    for kind, p in produced:
        print("%-16s %s" % (kind, os.path.relpath(p, HERE)))
    print("total:", len(produced))


if __name__ == "__main__":
    main()
