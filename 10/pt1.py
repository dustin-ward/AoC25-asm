from sys import stdin

ans = 0
for line in stdin:
    parts = line.split(' ')

    target = parts[0][1:-1]
    target_val = 0
    for c in reversed(target):
        target_val <<= 1
        if c == '#':
            target_val |= 1

    buttons = [x[1:-1].split(',') for x in parts[1:-1]]
    button_vals = []
    for b in buttons:
        v = 0
        b = [int(x) for x in b]
        for x in b:
            v |= (1 << x)
        button_vals.append(v)

    dp = {}

    S = [(0, 0)]
    while len(S) > 0:
        v, d = S.pop()
        dp[v] = d

        for b in button_vals:
            vv = v ^ b
            if vv in dp and dp[vv] <= d+1:
                continue
            S.append((vv, d+1))

    ans += dp[target_val]
print(ans)
