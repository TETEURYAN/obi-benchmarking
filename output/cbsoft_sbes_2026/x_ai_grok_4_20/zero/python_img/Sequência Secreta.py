
N = int(input())
seq = [int(input()) for _ in range(N)]

dp = [[0, 0] for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 0

for i in range(1, N):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + 1
    if seq[i] != seq[i-1]:
        dp[i][1] = dp[i-1][0] + 1
    else:
        dp[i][1] = 0

print(max(dp[N-1][0], dp[N-1][1]))
