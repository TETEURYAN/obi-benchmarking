import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    v = [int(input_data[i+1]) for i in range(n)]
    
    # dp[i][last] = maximum numbers we can mark from index 0..i
    # where i is marked and last is the value at position i (1 or 2)
    # We want to select a subsequence (in order) such that no two consecutive selected are equal
    
    # dp[i][last_val] = max count ending at position i with value v[i]
    # Transition: dp[i] = max over all j < i where v[j] != v[i] of dp[j] + 1
    # Also dp[i] = 1 (just pick element i alone)
    
    INF = float('inf')
    
    # dp1[i] = max length of valid subsequence ending at i with last value = v[i]
    # We track best ending with value 1 and best ending with value 2
    
    best = [0, 0]  # best[0] = best count ending with value 1, best[1] = best count ending with value 2
    
    ans = 0
    
    for i in range(n):
        val = v[i]  # 1 or 2
        other = 2 if val == 1 else 1
        
        # We can extend any subsequence ending with 'other'
        # or start fresh
        cur = best[other - 1] + 1
        
        # Update best for val
        if cur > best[val - 1]:
            best[val - 1] = cur
        
        if cur > ans:
            ans = cur
    
    print(ans)

solve()