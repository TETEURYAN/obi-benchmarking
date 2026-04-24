import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    A = []
    for i in range(N):
        A.append(int(data[idx])); idx += 1
    
    # Each annotation a_i can represent either a_i or M - a_i actual meters explored
    # The sequence of actual distances must be non-decreasing
    # We want the minimum sum among all valid non-decreasing sequences
    
    # For each dive i, the actual distance is either A[i] or M - A[i]
    # We need to find a non-decreasing sequence choosing one of the two options per dive
    # and minimize the total sum
    
    # DP approach:
    # dp[i][0] = min sum for first i+1 dives, where dive i chose A[i]
    # dp[i][1] = min sum for first i+1 dives, where dive i chose M - A[i]
    # Transition: dp[i][c] = min over valid previous choices
    
    INF = float('inf')
    
    # options[i] = (val0, val1) where val0 = A[i], val1 = M - A[i]
    # But if A[i] == M - A[i], both are same
    
    options = []
    for i in range(N):
        v0 = A[i]
        v1 = M - A[i]
        options.append((v0, v1))
    
    # dp[c] = min sum when current dive chose option c (0 or 1)
    # We also need to track the actual value chosen to check non-decreasing
    
    # State: (min_sum, chosen_value)
    # dp[0] = min sum ending with option 0 of dive 0
    # dp[1] = min sum ending with option 1 of dive 0
    
    # For transitions, we need the value of the previous choice
    # dp[i][c] depends on dp[i-1][c'] where options[i-1][c'] <= options[i][c]
    
    # Since N <= 10^4, O(N) with 2 states is fine
    
    # dp[c] = (min_sum, prev_value)
    # Actually we just need min_sum for each of the 2 states
    
    prev = [INF, INF]
    prev_val = [options[0][0], options[0][1]]
    prev[0] = options[0][0]
    prev[1] = options[0][1]
    
    for i in range(1, N):
        v0, v1 = options[i]
        curr = [INF, INF]
        
        # For current option 0 (value v0):
        # Need previous value <= v0
        best = INF
        if prev_val[0] <= v0 and prev[0] < INF:
            best = min(best, prev[0])
        if prev_val[1] <= v0 and prev[1] < INF:
            best = min(best, prev[1])
        if best < INF:
            curr[0] = best + v0
        
        # For current option 1 (value v1):
        best = INF
        if prev_val[0] <= v1 and prev[0] < INF:
            best = min(best, prev[0])
        if prev_val[1] <= v1 and prev[1] < INF:
            best = min(best, prev[1])
        if best < INF:
            curr[1] = best + v1
        
        prev = curr
        prev_val = [v0, v1]
    
    ans = min(prev[0], prev[1])
    if ans == INF:
        print(-1)
    else:
        print(ans)

solve()