import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n = data[0]
a = data[1:1+n]

max_h = max(a)

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = max_h - a[i]

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        best = 10**9
        for k in range(l, r):
            val = dp[l][k] + dp[k + 1][r]
            if a[k] == a[k + 1]:
                val -= max_h - max(a[k], a[k + 1])
            if val < best:
                best = val
        dp[l][r] = best

print(dp[0][n - 1])