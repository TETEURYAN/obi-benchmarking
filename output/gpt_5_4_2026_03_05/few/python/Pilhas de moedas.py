import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n, k = data[0], data[1]
p = data[2:2 + n]

MAXV = 500
freq = [0] * (MAXV + 1)
for x in p:
    freq[x] += 1

values = [v for v in range(1, MAXV + 1) if freq[v] > 0]
m = len(values)

if m <= k:
    print(0)
    exit()

INF = 10**18

cost = [[0] * m for _ in range(m)]
for i in range(m):
    target = values[i]
    s = 0
    for j in range(i - 1, -1, -1):
        s += freq[values[j]] * (target - values[j])
        cost[j][i] = s

dp_prev = [INF] * m
for i in range(m):
    dp_prev[i] = cost[0][i]

for groups in range(2, k + 1):
    dp_cur = [INF] * m
    for i in range(groups - 1, m):
        best = INF
        for t in range(groups - 2, i):
            val = dp_prev[t] + cost[t + 1][i]
            if val < best:
                best = val
        dp_cur[i] = best
    dp_prev = dp_cur

ans = INF
for last in range(k - 1, m):
    if dp_prev[last] < ans:
        ans = dp_prev[last]

print(ans)