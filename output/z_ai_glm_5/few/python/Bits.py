import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])
    
    MOD = 10**9 + 7
    
    # dp[i] stores the number of valid sequences of length i
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        # Recurrence: dp[i] = 2 * dp[i-1] - dp[i-K-1]
        # For i < K, the term dp[i-K-1] is 0.
        # For i == K, the term dp[i-K-1] corresponds to dp[-1], which conceptually is 1.
        
        term1 = (2 * dp[i-1]) % MOD
        
        idx = i - K - 1
        
        if idx == -1:
            term2 = 1
        elif idx < -1:
            term2 = 0
        else:
            term2 = dp[idx]
            
        dp[i] = (term1 - term2 + MOD) % MOD
        
    print(dp[N])

if __name__ == '__main__':
    solve()