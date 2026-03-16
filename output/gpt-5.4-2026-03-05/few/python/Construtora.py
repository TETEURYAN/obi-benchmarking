import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1+n]

mx = max(a)

dp = [[0] * n for _ in range(n)]

for length in range(1, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        best = 10**9

        m = min(a[l:r+1])
        cost = mx - m
        i = l
        extra = 0
        while i <= r:
            if a[i] == m:
                i += 1
            else:
                j = i
                while j <= r and a[j] > m:
                    j += 1
                extra += dp[i][j-1]
                i = j
        best = min(best, cost + extra)

        for k in range(l, r):
            v = dp[l][k] + dp[k+1][r]
            if v < best:
                best = v

        dp[l][r] = best

print(dp[0][n-1])