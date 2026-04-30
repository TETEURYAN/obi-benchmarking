MOD = 10**9 + 7

N = int(input())

if N == 0:
    print(1)
elif N == 1:
    print(1)
else:
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 5
    for i in range(3, N + 1):
        dp[i] = (dp[i-1] + 4 * dp[i-2] + 2 * dp[i-3]) % MOD
        # Wait, let me verify with the recurrence
        # From the 7 endings:
        # 1 ending uses N-1 (two 1x1 stacked)
        # 3 endings use N-2 (the L-brick oriented 3 ways + one more)
        # 2 endings use N-3 (L-brick taking 3 width)
        # Actually: 1*(N-1) + 4*(N-2) + 2*(N-3)
        # dp[2] = 5, dp[1]=1, dp[0]=1
        # dp[3] = dp[2] + 4*dp[1] + 2*dp[0] = 5 + 4 + 2 = 11
        # dp[4] = dp[3] + 4*dp[2] + 2*dp[1] = 11 + 20 + 2 = 33
        # dp[6] = ?
        # dp[5] = dp[4] + 4*dp[3] + 2*dp[2] = 33 + 44 + 10 = 87
        # dp[6] = dp[5] + 4*dp[4] + 2*dp[3] = 87 + 132 + 22 = 241 ✓
    print(dp[N])