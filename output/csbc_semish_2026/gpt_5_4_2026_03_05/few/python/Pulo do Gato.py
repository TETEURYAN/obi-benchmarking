import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

c = data[0]
tiles = data[1:1 + c]

INF = 10**9
dp = [INF] * c
dp[0] = 0

for i in range(1, c):
    if tiles[i] == 1:
        if i - 1 >= 0 and tiles[i - 1] == 1:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        if i - 2 >= 0 and tiles[i - 2] == 1:
            dp[i] = min(dp[i], dp[i - 2] + 1)

print(dp[c - 1] if dp[c - 1] != INF else -1)