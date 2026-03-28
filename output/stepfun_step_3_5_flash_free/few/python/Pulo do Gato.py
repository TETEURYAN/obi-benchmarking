import sys

data = sys.stdin.read().split()
if not data:
    exit()
C = int(data[0])
cores = list(map(int, data[1:1+C]))

if C == 1:
    print(0)
    exit()

INF = 10**9
dp = [INF] * C
dp[0] = 0

for i in range(1, C):
    if cores[i] == 1:
        if i-1 >= 0 and cores[i-1] == 1:
            dp[i] = min(dp[i], dp[i-1] + 1)
        if i-2 >= 0 and cores[i-2] == 1:
            dp[i] = min(dp[i], dp[i-2] + 1)

print(dp[C-1] if dp[C-1] < INF else -1)