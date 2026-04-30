
N = int(input())
seq = [int(input()) for _ in range(N)]

dp = [[0, 0] for _ in range(N)]

dp[0][0] = 1
dp[0][1] = 0

for i in range(1, N):
    # não pega o i-ésimo
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    
    # pega o i-ésimo
    if seq[i] != seq[i-1]:
        dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + 1
    else:
        dp[i][1] = dp[i-1][0] + 1

print(max(dp[N-1][0], dp[N-1][1]))
