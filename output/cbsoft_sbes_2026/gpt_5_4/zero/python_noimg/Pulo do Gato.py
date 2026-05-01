import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

C = data[0]
tiles = data[1:1 + C]

INF = 10**9
dp = [INF] * C
dp[0] = 0

for i in range(1, C):
    if tiles[i] == 1:
        if i - 1 >= 0 and dp[i - 1] != INF:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        if i - 2 >= 0 and dp[i - 2] != INF:
            dp[i] = min(dp[i], dp[i - 2] + 1)

print(dp[-1] if dp[-1] != INF else -1)