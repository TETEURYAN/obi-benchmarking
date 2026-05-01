import sys

def solve():
    MOD = 10**9 + 7
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    # dp[i][j] = number of sequences of length i ending with j consecutive 1s
    # j ranges from 0 to K-1
    # If j == K, that means K consecutive 1s which is forbidden
    
    # dp[j] = count of sequences where last j bits are 1 (and bit before is 0 or start)
    # j = 0 means last bit is 0
    
    # State: consecutive 1s at the end, from 0 to K-1
    # dp[c] = number of sequences of current length ending with exactly c consecutive 1s
    
    if K == 1:
        # No 1s allowed at all
        # Only sequence: all zeros
        print(1)
        return
    
    # Initialize for length 1
    # dp[0] = 1 (sequence "0")
    # dp[1] = 1 (sequence "1")
    dp = [0] * K
    dp[0] = 1  # ends with 0 consecutive 1s (last bit is 0)
    dp[1] = 1  # ends with 1 consecutive 1 (last bit is 1)
    
    for i in range(2, N + 1):
        new_dp = [0] * K
        # Place a 0: any state goes to state 0
        for c in range(K):
            new_dp[0] = (new_dp[0] + dp[c]) % MOD
        # Place a 1: state c goes to state c+1, but only if c+1 < K
        for c in range(K - 1):
            new_dp[c + 1] = (new_dp[c + 1] + dp[c]) % MOD
        dp = new_dp
    
    ans = sum(dp) % MOD
    print(ans)

solve()