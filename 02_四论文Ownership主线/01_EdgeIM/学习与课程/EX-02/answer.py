import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "EX-05a"))
from algo1 import algo1


import datetime
import pandas as pd
import pm4py


LOG = {
    "case1": "ABDF", "case2": "ACDF", "case3": "ABDEDF",
    "case4": "ABDF", "case5": "ACDEDF", "case6": "ABCDF",
}

def to_df(log):
    rows = []
    for case, acts in log.items():
        for i, a in enumerate(acts):
            rows.append({"case:concept:name": case,
                         "concept:name": a,
                         "time:timestamp": datetime.datetime(2026, 1, 1, 0, i)})
    return pm4py.format_dataframe(pd.DataFrame(rows))

df = to_df(LOG)
dfg, start, end = pm4py.discover_dfg(df)
print(dfg, start, end)
tree = pm4py.discover_process_tree_inductive(df)
print(tree)


# dict -> EX-05a 的输入格式
log_for_algo1 = [
    (case, list(acts))
    for case, acts in LOG.items()
]

D2, S, E, R = algo1(log_for_algo1)

print("D' =", [case for case, acts in D2])

assert [case for case, acts in D2] == [
    "case1", "case2", "case3", "case6"
]

# EX-05a 输出 -> 当前 to_df() 吃的 dict
LOG2 = {
    case: "".join(acts)
    for case, acts in D2
}

df2 = to_df(LOG2)

tree2 = pm4py.discover_process_tree_inductive(df2)

print("D tree :", tree)
print("D' tree:", tree2)

thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

rows = []

for t in thresholds:
    tree_D = pm4py.discover_process_tree_inductive(
        df,
        noise_threshold=t
    )

    tree_D2 = pm4py.discover_process_tree_inductive(
        df2,
        noise_threshold=t
    )

    s_D = str(tree_D)
    s_D2 = str(tree_D2)

    rows.append({
        "t": t,
        "D 的树": s_D,
        "D' 的树": s_D2,
        "一样吗": s_D == s_D2,
    })

result = pd.DataFrame(rows)
print(result.to_string(index=False))


