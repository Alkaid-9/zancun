LOG = [
    # ("case1", ["A", "B", "D", "F"]),
    # ("case2", ["A", "C", "D", "F"]),
    # ("case3", ["A", "B", "D", "E", "D", "F"]),
    # ("case4", ["A", "B", "D", "F"]),
    # ("case5", ["A", "C", "D", "E", "D", "F"]),
    # ("case6", ["A", "B", "C", "D", "F"]),
    # ("tst_a",["A", "B", "E", "D", "F"]),
    # ("tst_b",["A","B","D","E","F"]),
    # ("3_1",["X", "A", "B", "C", "E","Y"]),
    # ("3_2",["X", "A", "C", "B","E","Y"]),
    # ("3_3",["X", "B", "D", "A","F","Y"]),
    # ("3_4",["X", "B", "A", "D","F","Y"]),
    # ("tst_c",["X", "A", "B", "C", "B","E","Y"]),

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

        if (Si - S) or (Ei - E) or (Ri - R):
            D2.append((case_id, acts))

            S.update(Si)
            E.update(Ei)
            R.update(Ri)




    return D2, S, E, R

D2, S, E, R = algo1(LOG)
# print(D2, S, E, R)


forward = algo1(LOG)
reverse = algo1(LOG[::-1])

# print([x[0] for x in forward[0]])
# print([x[0] for x in reverse[0]])
# print(forward[1:] == reverse[1:])