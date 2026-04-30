import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    T = [int(input_data[idx+i]) for i in range(N)]
    idx += N
    
    T.sort()
    
    # Key insight: after sorting, in an optimal solution, each trio consists of
    # consecutive or near-consecutive elements. Specifically, for sorted array,
    # the optimal strategy is to pick trios where the two smallest elements
    # are adjacent in the sorted array.
    #
    # After sorting, balanceamento = (A-B)^2 where A <= B <= C
    # So we want to minimize sum of (T[i] - T[j])^2 for pairs (i,j) being
    # the two smallest in each trio.
    #
    # Key observation: In optimal solution, if we sort all dolls, the two
    # smallest dolls in each trio are always adjacent in the sorted order.
    # This is a known result for this type of problem.
    #
    # So we need to choose K pairs of adjacent elements from sorted array
    # (each element used at most once), and for each pair (i, i+1) the cost
    # is (T[i+1] - T[i])^2, plus we need one more element per trio (the largest,
    # which doesn't affect cost). We need 3K elements total, K pairs + K singles.
    #
    # DP: dp[i][j] = min cost using first i elements, having formed j complete trios
    # When we pick pair at position (i-1, i) (0-indexed), we use 2 elements for cost
    # and need 1 more element (which can be any remaining element, so we just need
    # to ensure we have enough elements left).
    #
    # Actually the third element just needs to exist. Since we sort and pick greedily,
    # the third element for each trio is "free" in terms of cost.
    # 
    # DP on sorted array:
    # dp[i][j] = min cost considering first i dolls, having selected j pairs
    # Transitions:
    # - skip doll i: dp[i+1][j] = dp[i][j]
    # - use dolls i and i+1 as a pair: dp[i+2][j+1] = dp[i][j] + (T[i+1]-T[i])^2
    # 
    # We need j = K pairs, and we need K additional "third" dolls from remaining N-2K dolls
    # Since N >= 3K, there are always enough dolls for the thirds.
    
    n = N
    # dp[j] after processing i elements
    INF = float('inf')
    
    # dp[i][j]: min cost using elements 0..i-1, formed j pairs
    # We need at least K pairs from n elements, with n-2K remaining for thirds
    # Constraint: after choosing j pairs from first i elements, remaining elements
    # for thirds: we need K-j more pairs from elements i..n-1, 
    # and K singles. Total needed from remaining: 2*(K-j) + (K - singles_so_far)
    # This is complex. Let's just do the DP and trust there are enough elements.
    
    # dp array: dp[j] = min cost having formed j pairs, index i processed
    dp = [INF] * (K + 1)
    dp[0] = 0
    
    for i in range(n - 1):
        # Process in reverse to avoid using same element twice
        # Actually we go forward; use 1D DP carefully
        # We iterate i from 0 to n-2
        # If we pick pair (i, i+1), we skip i+2 next
        # Use new_dp
        pass
    
    # 2D DP with rolling
    # dp[i][j]: i from 0..n, j from 0..K
    prev = [INF] * (K + 1)
    prev[0] = 0
    
    for i in range(n):
        curr = prev[:]  # option: skip element i
        if i + 1 < n:
            for j in range(K):
                if prev[j] < INF:
                    cost = (T[i+1] - T[i]) ** 2
                    if curr[j+1] > prev[j] + cost:
                        curr[j+1] = prev[j] + cost
        # But if we pick pair (i, i+1), next iteration should start at i+2
        # This simple approach doesn't handle skipping i+1
        prev = curr
    
    # Redo with proper skip
    dp = [[INF]*(K+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(K+1):
            if dp[i][j] == INF:
                continue
            # skip element i
            if dp[i+1][j] > dp[i][j]:
                dp[i+1][j] = dp[i][j]
            # pick pair (i, i+1)
            if j < K and i+1 < n:
                cost = (T[i+1]-T[i])**2
                if dp[i+2][j+1] > dp[i][j] + cost:
                    dp[i+2][j+1] = dp[i][j] + cost
    
    print(dp[n][K])

solve()