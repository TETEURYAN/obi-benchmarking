import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

R = int(input_data[0])
K = int(input_data[1])

dp = [[0] * (K + 1) for _ in range(R + 1)]
dp[0][0] = 1

for n in range(1, R + 1):
    for k in range(1, K + 1):
        if n >= k:
            dp[n][k] = dp[n - k][k] + dp[n - k][k - 1]

print(dp[R][K])