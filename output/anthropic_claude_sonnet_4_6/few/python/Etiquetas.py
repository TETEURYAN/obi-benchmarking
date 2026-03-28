import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    K = int(data[idx]); idx+=1
    C = int(data[idx]); idx+=1
    A = [int(data[idx+i]) for i in range(N)]
    idx += N
    
    # Total sum
    total = sum(A)
    
    # We want to maximize sum of uncovered = total - sum of covered
    # So we want to minimize sum of covered by K labels of length C
    # Each label covers C consecutive squares, no overlap
    # We must place exactly K labels
    
    # prefix sum for range sums
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]
    
    def range_sum(l, r):  # [l, r) 0-indexed
        return prefix[r] - prefix[l]
    
    # dp[i][j] = minimum cost to place j labels using squares 0..i-1
    # We need to place exactly K labels in N squares
    # dp[i][j] = min sum covered when we've considered first i squares and placed j labels
    
    # Transition:
    # dp[i][j] = min(dp[i-1][j], dp[i-C][j-1] + range_sum(i-C, i))
    # dp[i][j]: after processing i squares, placed j labels
    # Base: dp[0][0] = 0
    
    # i from 0 to N, j from 0 to K
    # dp[i][j]: minimum covered sum using exactly j labels, all fitting within first i squares
    
    INF = float('inf')
    
    # Space optimization: use 1D dp rolling
    # dp[j] for current i
    
    # dp[i][j] = min(dp[i-1][j], dp[i-C][j-1] + sum(i-C..i-1)) if i >= C
    
    # We'll keep two arrays: prev_dp (dp[i-1]) and prev_C_dp (dp[i-C])
    # Actually let's keep full 2D but optimize
    
    # N=10000, K=10000, but K*C <= N so K <= N/C
    # If C=1, K can be up to 10000, N=10000 -> O(N*K) = 10^8 might be tight
    # Let's try with numpy or optimized approach
    
    # Actually K*C <= N means K <= N/C, so N*K <= N*(N/C) <= N^2/C
    # Worst case C=1: N*K = 10^4 * 10^4 = 10^8 - too slow in pure python
    # Need to optimize
    
    # For fixed j, dp[i][j] = min over placements
    # dp[i][j] = min(dp[i-1][j], dp[i-C][j-1] + window_sum(i-C, i))
    
    # Let's use arrays and be efficient
    
    # dp shape: (N+1) x (K+1)
    # But 10^8 ops in python is too slow
    # Use numpy
    
    import numpy as np
    
    dp = np.full((N+1, K+1), INF)
    dp[0][0] = 0
    
    pre = np.array(prefix, dtype=np.int64)
    
    for i in range(1, N+1):
        dp[i] = dp[i-1].copy()
        if i >= C:
            ws = int(pre[i] - pre[i-C])
            prev_row = dp[i-C]
            # dp[i][j] = min(dp[i][j], dp[i-C][j-1] + ws) for j>=1
            candidates = np.empty(K+1)
            candidates[0] = INF
            candidates[1:] = prev_row[:K] + ws
            dp[i] = np.minimum(dp[i], candidates)
    
    min_covered = dp[N][K]
    print(total - int(min_covered))

solve()