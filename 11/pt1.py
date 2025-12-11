from sys import stdin
from functools import cache

g = {}
for line in stdin:
    x, y = line.strip().split(':')
    g[x] = y.strip().split(' ')

ans = 0


@cache
def f(n):
    if n == 'out':
        return 1
    ans = 0
    for n2 in g[n]:
        ans += f(n2)
    return ans


print(f('you'))
