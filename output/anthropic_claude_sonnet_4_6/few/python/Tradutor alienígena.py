import sys

def solve():
    data = sys.stdin.read().split()
    N_str = data[0]
    s = data[1]
    
    MOD = 1_000_000_007
    N = int(N_str)
    n = len(s)
    
    # Precompute the number of digits in N
    len_N = len(N_str)
    
    # dp[i] = number of valid ways to parse s[0:i]
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        # Try all substrings s[j:i] as a number
        # The number must be between 1 and N
        # No leading zeros
        # Max length of N is len_N, so we try lengths 1 to len_N
        for length in range(1, len_N + 1):
            j = i - length
            if j < 0:
                break
            if dp[j] == 0:
                continue
            # Check leading zero
            if s[j] == '0':
                continue
            # Extract substring
            sub = s[j:i]
            # Compare with N_str
            if length < len_N:
                # sub < N for sure (fewer digits, no leading zero)
                dp[i] = (dp[i] + dp[j]) % MOD
            elif length == len_N:
                # Compare lexicographically (same length, no leading zeros)
                if sub <= N_str:
                    dp[i] = (dp[i] + dp[j]) % MOD
    
    print(dp[n])

solve()