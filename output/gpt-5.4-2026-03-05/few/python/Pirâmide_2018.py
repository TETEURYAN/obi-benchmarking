import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = []
idx = 1
for _ in range(n):
    a.append(data[idx:idx + n])
    idx += n

pref = [[0] * (n + 1) for _ in range(n)]
for i in range(n):
    s = 0
    for j in range(n):
        s += a[i][j]
        pref[i][j + 1] = s

INF = 10**18
dp = [pref[0][j + 1] - pref[0][j] for j in range(n)]

for i in range(1, n):
    width = i + 1
    m = n - width + 1
    ndp = [INF] * m
    rowsum = [0] * m
    for j in range(m):
        rowsum[j] = pref[i][j + width] - pref[i][j]
    for j in range(m):
        best = INF
        if j < len(dp):
            if dp[j] < best:
                best = dp[j]
        if j - 1 >= 0:
            if dp[j - 1] < best:
                best = dp[j - 1]
        ndp[j] = best + rowsum[j]
    dp = ndp

print(min(dp))