import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
cnt = [0] * 101
for x in data[1:1+n]:
    cnt[x] += 1

vals = [i for i in range(101) if cnt[i] > 0]
m = len(vals)

if m == 1:
    print(0)
    sys.exit()

INF = 10**18

dp = [[INF] * m for _ in range(m)]

for i in range(m):
    dp[i][i] = 0

for length in range(2, m + 1):
    for l in range(m - length + 1):
        r = l + length - 1
        best = INF
        if l + 1 <= r:
            v = dp[l + 1][r] + 2 * (vals[r] - vals[l])
            if v < best:
                best = v
            v = dp[l][r - 1] + 2 * (vals[r] - vals[l])
            if v < best:
                best = v
        dp[l][r] = best

print(dp[0][m - 1])