import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n = data[0]
a = data[1:1+n]

mx = max(a)

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = mx - a[i]

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        best = 10**9
        for k in range(l, r):
            val = dp[l][k] + dp[k + 1][r]
            if a[l] == a[k + 1]:
                m1 = a[l]
                for t in range(l, k + 1):
                    if a[t] < m1:
                        m1 = a[t]
                m2 = a[k + 1]
                for t in range(k + 1, r + 1):
                    if a[t] < m2:
                        m2 = a[t]
                common = mx - max(m1, m2)
                val -= common
            if val < best:
                best = val
        dp[l][r] = best

print(dp[0][n - 1])