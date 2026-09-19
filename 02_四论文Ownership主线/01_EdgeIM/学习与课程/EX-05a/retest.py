LOG = [
    ("case1", ["A", "B", "D", "F"]),
    ("case2", ["A", "C", "D", "F"]),
    ("case3", ["A", "B", "D", "E", "D", "F"]),
    ("case4", ["A", "B", "D", "F"]),
    ("case5", ["A", "C", "D", "E", "D", "F"]),
    ("case6", ["A", "B", "C", "D", "F"]),
]


def algo1(log):
    D2 = []
    S = set()
    E = set()
    R = set()

    for case_id, acts in log:

        Si = {acts[0]}
        Ei = {acts[-1]}
        Ri = {
            (acts[i], acts[i+1])
            for i in range(len(acts) - 1)
            }

        if Si - S or Ei-E or Ri-R:
            D2.append((case_id,acts))

            S.update(Si)
            E.update(Ei)
            R.update(Ri)

    return D2, S, E, R


D2, S, E, R = algo1(LOG)
print(D2, S, E, R)


forward = algo1(LOG)
reverse = algo1(LOG[::-1])

D2_forward, S_forward, E_forward, R_forward = forward
D2_reverse, S_reverse, E_reverse, R_reverse = reverse

print("正序保留：", [case_id for case_id, acts in D2_forward])
print("逆序保留：", [case_id for case_id, acts in D2_reverse])

print(
    "S/E/R 是否相同：",
    S_forward == S_reverse
    and E_forward == E_reverse
    and R_forward == R_reverse
)