import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    T = sorted(int(x) for x in data[2:2+N])
    
    # Key insight: after sorting, in an optimal solution, each trio (A, B, C) with A<=B<=C
    # has its two smallest elements adjacent in the sorted array.
    # The balancing is (A-B)^2 where A<=B, so it's (B-A)^2 = (T[i+1]-T[i])^2 for adjacent pairs.
    # The third element C can be any element >= B and doesn't affect balancing.
    # 
    # So we need to choose K pairs of adjacent elements (i, i+1) from sorted array,
    # plus K additional elements (each >= the pair's second element, or just any remaining),
    # such that no element is used twice, minimizing sum of (T[i+1]-T[i])^2.
    #
    # Actually the third element just needs to be >= B (the middle element).
    # But since we sort and pick optimally, the third element can be any unused element.
    # The key observation: we can always find a valid third element as long as we have enough.
    #
    # The standard approach for this type of problem:
    # Sort the array. The optimal strategy is to pick K pairs of consecutive elements
    # (indices i, i+1) as the (A,B) part of each trio, and assign remaining elements as C.
    # We need to select K non-overlapping consecutive pairs from N elements,
    # and the remaining N-2K elements serve as the C values (always possible since 3K<=N).
    #
    # DP: dp[i][j] = min cost using first i elements of sorted array, having formed j complete pairs
    # Transitions:
    # - Skip element i: dp[i+1][j] = dp[i][j]
    # - Use elements i and i+1 as a pair: dp[i+2][j+1] = dp[i][j] + (T[i+1]-T[i])^2
    # We need dp[N][K] but we also need to ensure K "third" elements remain.
    # After choosing j pairs from first i elements, we've used 2j elements, leaving i-2j as potential C's.
    # We need at least K-j more pairs from remaining N-i elements, using 2*(K-j) elements as pairs
    # and K as C elements total. The constraint is that we always have enough elements.
    # Since 3K <= N, and we pick 2K elements as pairs + K as C's = 3K <= N, it's always feasible.
    # The DP just needs: after processing all N elements with exactly K pairs chosen, valid.
    
    INF = float('inf')
    # dp[j] = min cost having chosen j pairs so far
    # We iterate over elements
    
    # dp[i][j]: min cost considering first i elements, j pairs chosen
    # i from 0..N, j from 0..K
    # Transition: skip T[i] -> dp[i+1][j] = dp[i][j]
    #             pair T[i],T[i+1] -> dp[i+2][j+1] = dp[i][j] + cost
    
    # Use 1D rolling
    # dp[j] after processing i elements
    
    dp = [INF] * (K + 1)
    dp[0] = 0
    
    for i in range(N):
        # Process in reverse to avoid using same element twice in forward pass
        # Actually we need to be careful: pairing uses i and i+1 simultaneously
        # Let's use standard 2D DP with space optimization
        # We'll iterate i from N-1 down to 0, but it's cleaner to do forward
        pass
    
    # Full 2D DP
    dp = [[INF] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(N):
        for j in range(K + 1):
            if dp[i][j] == INF:
                continue
            # Skip element i
            if dp[i+1][j] > dp[i][j]:
                dp[i+1][j] = dp[i][j]
            # Pair elements i and i+1
            if j < K and i + 1 < N:
                cost = (T[i+1] - T[i]) ** 2
                val = dp[i][j] + cost
                if dp[i+2][j+1] > val:
                    dp[i+2][j+1] = val
    
    print(dp[N][K])

solve()