"""OE1 附件挖掘脚本（PM4Py DFG）— 2026-08-24 四块执行窗块④代办。

前置：solver 环境 `pip install pm4py`（2026-08-24 实装 pm4py-2.7.23.6），
系统 graphviz `dot` 二进制在 PATH（2.43.0）。

产出（全部落本目录 mining/ 子目录）：
1. all_cases_merged.xes —— cases/ 五份 .xes 的合并事件日志（中间产物，供复现）
2. dfg_frequency.png    —— 直接跟随频率 DFG（边标出现次数）
3. dfg_performance.png  —— 性能 DFG（边标平均耗时，aggregation=mean）

诚实标注（铁律 1）：合并语料 = 1 份真实流水线运行（task_real_harness）+
4 份合成演示轨迹（task_variant_01..04）。两张图标题与 README 均保留此口径，
对外展示时不得把合成轨迹说成真实运行。

运行：
    /home/alkaid/miniconda3/envs/solver/bin/python mine_dfg.py
"""
import json
import os

import matplotlib
matplotlib.use("Agg")  # 无头环境；必须在 pm4py 拉起 pyplot 前生效
import pandas as pd  # noqa: E402
import pm4py  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CASES_DIR = os.path.join(HERE, "cases")
MINING_DIR = os.path.join(HERE, "mining")

MERGED_NAME = "all_cases_merged.xes"
PNG_FREQ = "dfg_frequency.png"
PNG_PERF = "dfg_performance.png"
MANIFEST_KIND = "MINED ARTIFACT"


def load_kinds():
    """从 manifest.json 读每份 .xes 的性质标注（REAL RUN / SYNTHETIC DEMO）。"""
    path = os.path.join(HERE, "manifest.json")
    kinds = {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for entry in json.load(fh):
                kinds[entry["file"]] = entry["kind"]
    return kinds


def main():
    os.makedirs(MINING_DIR, exist_ok=True)
    kinds = load_kinds()

    frames = []
    per_source = []
    for name in sorted(os.listdir(CASES_DIR)):
        if not name.endswith(".xes"):
            continue
        df = pm4py.read_xes(os.path.join(CASES_DIR, name))
        frames.append(df)
        n = df["case:concept:name"].nunique()
        per_source.append((name, kinds.get(name, "[unregistered]"), len(df), n))

    merged = pd.concat(frames, ignore_index=True)
    merged_path = os.path.join(MINING_DIR, MERGED_NAME)
    pm4py.write_xes(merged, merged_path)

    # 频率 DFG：边 = 直接跟随关系，标注 = 出现次数
    dfg, sa, ea = pm4py.discover_dfg(merged)
    freq_path = os.path.join(MINING_DIR, PNG_FREQ)
    pm4py.save_vis_dfg(
        dfg, sa, ea, freq_path,
        graph_title="EvoAgent task pipeline - frequency DFG "
                    "(1 real run + 4 synthetic demo traces)")

    # 性能 DFG：边 = 平均耗时（这些轨迹时间戳为分钟级演示间隔）
    pdfg, psa, pea = pm4py.discover_performance_dfg(merged)
    perf_path = os.path.join(MINING_DIR, PNG_PERF)
    pm4py.save_vis_performance_dfg(
        pdfg, psa, pea, perf_path,
        graph_title="EvoAgent task pipeline - performance DFG (mean) "
                    "(1 real run + 4 synthetic demo traces)")

    print("== 合并语料 ==")
    for name, kind, events, cases in per_source:
        print("%-42s %-16s %3d events / %d case(s)" % (name, kind, events, cases))
    print("total: %d events / %d cases" % (
        len(merged), merged["case:concept:name"].nunique()))
    print("activities:", sorted(merged["concept:name"].unique()))
    print("start=%s end=%s" % (dict(sa), dict(ea)))
    print("== 产物 ==")
    for p in (merged_path, freq_path, perf_path):
        print("%9d B  %s" % (os.path.getsize(p), os.path.relpath(p, HERE)))

    # 台账：幂等更新 manifest.json（重跑先清旧 MINED 条目再追加）
    manifest_path = os.path.join(HERE, "manifest.json")
    entries = []
    if os.path.exists(manifest_path):
        with open(manifest_path, encoding="utf-8") as fh:
            entries = [e for e in json.load(fh)
                       if e.get("kind") != MANIFEST_KIND]
    entries += [
        {"kind": MANIFEST_KIND,
         "file": os.path.join("mining", MERGED_NAME),
         "note": "cases/ 五份 .xes 合并（1 真实 + 4 合成），mine_dfg.py 中间产物"},
        {"kind": MANIFEST_KIND,
         "file": os.path.join("mining", PNG_FREQ),
         "note": "直接跟随频率 DFG（标题保留语料构成标注）"},
        {"kind": MANIFEST_KIND,
         "file": os.path.join("mining", PNG_PERF),
         "note": "性能 DFG mean 聚合（时间戳为分钟级演示间隔）"},
    ]
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(entries, fh, ensure_ascii=False, indent=2)
    print("manifest.json updated: %d entries" % len(entries))


if __name__ == "__main__":
    main()
