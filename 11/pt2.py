from sys import stdin
from functools import cache

g = {}
for line in stdin:
    x, y = line.strip().split(':')
    g[x] = y.strip().split(' ')


@cache
def f(n, t):
    if n == t:
        return 1
    if n == 'out':
        return 0
    ans = 0
    for n2 in g[n]:
        ans += f(n2, t)
    return ans


s1 = f('svr', 'dac')
s1 *= f('dac', 'fft')
s1 *= f('fft', 'out')

s2 = f('svr', 'fft')
s2 *= f('fft', 'dac')
s2 *= f('dac', 'out')

print(s1+s2)
