import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
V = [0] * (N + 1)
for i in range(1, N + 1):
    V[i] = int(input_data[i])

dp = [[0, 0] for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = dp[i-1][0]  # not including i
    dp[i][1] = dp[i-1][1]
    if V[i] == 1:
        dp[i][0] = max(dp[i][0], dp[i-1][1] + 1)
    elif V[i] == 2:
        dp[i][1] = max(dp[i][1], dp[i-1][0] + 1)

print(max(dp[N][0], dp[N][1]))