
import sys
sys.path.insert(0, "/mnt/d/MyResearch/MAS_Safety_Project/research/edgeim_sampling_audit/src")
sys.path.insert(0, "/mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/EX-05a")
import pilot
from algo1 import algo1

def full_features(log):
    starts = set()
    ends = set()
    transitions = set()

    for trace in log:
        if len(trace) > 0:
            starts.add(trace[0])
            ends.add(trace[-1])
            for i in range(len(trace) - 1):
                transitions.add((trace[i], trace[i+1]))

    return starts, ends, transitions


# 任务 3 · 先预测再跑
# (p1) 10 个 universe 的不变量全过吗？
# 预测：全过
#
# (p2) |D′| 会落在什么范围？（用 EX-03 的上界想：这些 universe 活动只有 3–4 个）
# 预测：落在 2 到 5；上界是 min(|L|, |S|+|E|+|R|)
#
# (p3) 正序 D′ 里非法 trace 的占比，比全日志的 3/6 高还是低？为什么？
# 预测：高了；感觉约束不够
# 正序 D′ 里非法 trace 的占比，比全日志的 3/6 低




print("seed | 拓扑 | |D′|正 | |D′|逆 | 正序D′里非法条数/|D′| | 不变量")
print("-" * 60)

for seed in range(10):
    U = pilot.build_universe(seed)

    # 建 oracle map：trace → label
    oracle_map = {c.trace: c.oracle_label for c in U.candidates}

    # 取 6 条 trace，按 candidate_index 顺序作为正序
    forward_log = [(i, c.trace) for i, c in enumerate(U.candidates)]
    reverse_log = forward_log[::-1]

    # 正序、逆序各跑一次 algo1
    D2_forward, S_forward, E_forward, R_forward = algo1(forward_log)
    D2_reverse, S_reverse, E_reverse, R_reverse = algo1(reverse_log)

    # 断言：正序 D′ 的 (S,E,R) == full_features 的 (S,E,R)；逆序同样
    D_full = tuple([trace for _, trace in forward_log])
    S_full, E_full, R_full = full_features(D_full)

    assert (S_forward, E_forward, R_forward) == (S_full, E_full, R_full), \
        f"seed {seed} 正序不变量失败"
    assert (S_reverse, E_reverse, R_reverse) == (S_full, E_full, R_full), \
        f"seed {seed} 逆序不变量失败"

    # 记录：|D′| 正序、|D′| 逆序、正序 D′ 里 ILLEGAL 的条数
    illegal_count = sum(1 for _, trace in D2_forward if oracle_map.get(trace) == "ILLEGAL")

    # 根据 seed 推断拓扑（0-2: chain, 3-4: branch_merge, 5-7: shortcut, 8-9: loop）
    if seed <= 2:
        topology = "chain"
    elif seed <= 4:
        topology = "branch_merge"
    elif seed <= 7:
        topology = "shortcut"
    else:
        topology = "loop"

    print(f"{seed:4d} | {topology:12s} | {len(D2_forward):5d} | {len(D2_reverse):5d} | {illegal_count:3d}/{len(D2_forward):3d} | ✓")


def full_features(log: tuple[str, ...]) -> tuple[set[str], set[str], set[tuple[str, str]]]:
    starts = set()
    ends = set()
    transitions = set()
    for trace in log:
        for event in trace:
            if event.startswith("start"):
                starts.add(event.split(" ")[1])
            elif event.startswith("end"):
                ends.add(event.split(" ")[1])
            else:
                transitions.add((event.split(" ")[1], event.split(" ")[2]))

    return starts, ends, transitions


















