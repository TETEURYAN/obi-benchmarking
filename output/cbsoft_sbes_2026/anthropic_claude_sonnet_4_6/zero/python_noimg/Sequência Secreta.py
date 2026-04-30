import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    v = [int(input_data[i+1]) for i in range(n)]
    
    # dp[i][last] = maximum numbers we can mark considering first i elements,
    # where last is the last marked number (1 or 2), or 0 if none marked yet
    # We want to maximize the count of marked elements such that no two consecutive marked are equal
    
    # dp[i][0] = max marked in v[0..i-1] where last marked was 1
    # dp[i][1] = max marked in v[0..i-1] where last marked was 2
    # dp[i][2] = max marked in v[0..i-1] where nothing marked yet (or we skip all)
    
    # State: dp[last] where last in {0: nothing marked, 1: last marked was 1, 2: last marked was 2}
    
    NEG_INF = -1
    # dp[0] = no element marked yet = 0
    # dp[1] = last marked was 1
    # dp[2] = last marked was 2
    
    dp = [0, NEG_INF, NEG_INF]
    # dp[0] means 0 elements marked so far, no last
    # dp[1] means some elements marked, last was 1
    # dp[2] means some elements marked, last was 2
    
    for i in range(n):
        cur = v[i]
        new_dp = [dp[0], dp[1], dp[2]]
        
        # Option: mark v[i] = cur
        # If nothing marked yet (state 0), we can mark cur
        if dp[0] != NEG_INF:
            val = dp[0] + 1
            if cur == 1:
                new_dp[1] = max(new_dp[1], val)
            else:
                new_dp[2] = max(new_dp[2], val)
        
        # If last marked was 1 (state 1), we can mark cur if cur != 1
        if dp[1] != NEG_INF and cur != 1:
            val = dp[1] + 1
            new_dp[2] = max(new_dp[2], val)
        
        # If last marked was 2 (state 2), we can mark cur if cur != 2
        if dp[2] != NEG_INF and cur != 2:
            val = dp[2] + 1
            new_dp[1] = max(new_dp[1], val)
        
        dp = new_dp
    
    ans = max(dp[1], dp[2])
    print(ans)

solve()