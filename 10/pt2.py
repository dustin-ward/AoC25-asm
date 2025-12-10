from sys import stdin
from scipy.optimize import linprog
import numpy as np

ans = 0
for line in stdin:
    parts = line.split(' ')
    joltages = [int(x) for x in parts[-1].strip()[1:-1].split(',')]

    M = []
    buttons = [x[1:-1].split(',') for x in parts[1:-1]]
    for b in buttons:
        b = [int(x) for x in b]
        v = [0]*len(joltages)
        for i in range(len(joltages)):
            if i in b:
                v[i] = 1
        M.append(v)

    A_ub = -np.array(M).T
    b_ub = -np.array(joltages)
    c = np.ones(A_ub.shape[1])
    result = linprog(c, A_eq=A_ub, b_eq=b_ub, integrality=1)

    ans += np.sum(result.x)

print(ans)
