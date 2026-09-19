import random
import sys
sys.path.insert(0, "/mnt/d/MyResearch/MAS_Safety_Project/research/edgeim_sampling_audit/src")
sys.path.insert(0, "/mnt/d/MyResearch/MAS_Safety_Project/learning/training/lu-edgeim-algo1/EX-05a")
import pilot
from algo1 import algo1



def full_features(log):
    S = set()
    E = set()
    R = set()

    for trace in log:
        if len(trace) > 0:
            S.add(trace[0])
            E.add(trace[-1])
            for i in range(len(trace)-1):
                R.add((trace[i],trace[i+1]))

    return (S, E, R)

print("seed | 拓扑 | |D′|正 | |D′|逆 | 正序 D′ 里非法条数 / |D′| | 不变量")


random.seed(0)


for seed in range(10):
    U = pilot.build_universe(seed)

    forward_log = []

    for candidate in U.candidates:
        forward_log.append(
            (candidate.candidate_index, candidate.trace)
        )

    reverse_log = forward_log[::-1]

    D_full = []

    for item in forward_log:
            D_full.append(item[1])


    S_full, E_full, R_full = full_features(D_full)

    # print(seed)
    # print(forward_log)
    # print(S_full, E_full, R_full)
    # print(len(D_full))


    D_forward, S_forward, E_forward, R_forward = algo1(forward_log)
    D_reverse, S_reverse, E_reverse, R_reverse = algo1(reverse_log)

    assert (S_forward, E_forward, R_forward) == (S_full, E_full, R_full), \
            f"seed {seed} 正序不变量失败"
    assert (S_reverse, E_reverse, R_reverse) == (S_full, E_full, R_full), \
            f"seed {seed} 逆序不变量失败"


    oracle_map = {}

    for candidate in U.candidates:
        oracle_map[candidate.trace] = candidate.oracle_label


    illegal_count = 0

    for item in D_forward:
        trace = item[1]

        if oracle_map[trace] == "ILLEGAL":
            illegal_count += 1

    # print(seed, len(D_forward), len(D_reverse), illegal_count)


    print(
        seed,
        U.topology,
        len(D_forward),
        len(D_reverse),
        f"{illegal_count}/{len(D_forward)}",
        "✓"
    )



    random_log = forward_log.copy()
    random.shuffle(random_log)

    D_random, S_random, E_random, R_random = algo1(random_log)

    assert (S_random, E_random, R_random) == (S_full, E_full, R_full), \
            f"seed {seed} 随机不变量失败"

    illegal_count = 0

    for item in D_random:
        trace = item[1]
        if oracle_map[trace] == "ILLEGAL":
            illegal_count += 1

    print(seed, len(D_random), illegal_count)




for seed in range(10):
    U = pilot.build_universe(seed)
    for candidate in U.candidates:
        if candidate.oracle_label == "ILLEGAL":
            print(seed, candidate.candidate_index, candidate.trace, candidate.oracle_label)

            print(U.model.starts)
            print(U.model.ends)


fixtures = []

for seed in range(10):
    U = pilot.build_universe(seed)
    for candidate in U.candidates:
        if candidate.oracle_label == "ILLEGAL":
            fixtures.append(( candidate.trace, U.model))

print(len(fixtures))
for trace, model in fixtures:
    # print(trace, model)
    assert trace[0] in model.starts and trace[-1] in model.ends,\
        f"trace {trace} 起始活动 {trace[0]} 或结束活动 {trace[-1]} 不在模型起始活动集合 {model.starts} 或结束活动集合 {model.ends}"
