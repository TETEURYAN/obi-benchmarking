import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    seq = [int(data[i+1]) for i in range(n)]
    
    # dp[i][last] = max numbers we can mark considering first i elements,
    # where last is the last marked number (0 means nothing marked yet)
    # We want to maximize count of marked elements such that no two consecutive marked are equal
    
    # dp[i][last_val] = max marked in seq[0..i-1] where last marked value is last_val
    # last_val = 0 means no element marked yet
    # last_val = 1 or 2
    
    # State: dp[i][last] where i is current index, last is last marked value (0,1,2)
    # Transition: for seq[i], we can skip it or mark it (if seq[i] != last)
    
    INF = float('-inf')
    # dp[last] = max count
    dp = {0: 0, 1: INF, 2: INF}
    
    for i in range(n):
        v = seq[i]
        new_dp = {0: INF, 1: INF, 2: INF}
        for last, cnt in dp.items():
            if cnt == INF:
                continue
            # Option 1: skip seq[i]
            if cnt > new_dp[last]:
                new_dp[last] = cnt
            # Option 2: mark seq[i] if v != last
            if v != last:
                if cnt + 1 > new_dp[v]:
                    new_dp[v] = cnt + 1
        dp = new_dp
    
    ans = max(dp[1], dp[2])
    print(ans)

solve()