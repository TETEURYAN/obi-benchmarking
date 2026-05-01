import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    T = []
    for i in range(N):
        T.append(int(input_data[idx])); idx += 1
    
    T.sort()
    
    # Key insight: After sorting, in an optimal solution, within each trio (A, B, C) with A<=B<=C,
    # the balancing is (A-B)^2. We want to minimize sum of (A-B)^2 over K trios.
    # 
    # Important observation: In optimal solution, we can assume that in each trio,
    # the two smallest elements are adjacent in the sorted array.
    # 
    # This is a classic DP problem. After sorting, we use DP where:
    # dp[i][j] = minimum total balancing using j trios from the first i dolls
    # 
    # When we pick a trio ending at position i (0-indexed), the two smallest are at positions i-2, i-1
    # and the largest is at position i (or any position >= i-1).
    # 
    # Actually the key insight: sort the array. In optimal grouping, each trio consists of
    # consecutive or near-consecutive elements. Specifically, for each trio, the two elements
    # contributing to balancing (A and B) should be adjacent in sorted order.
    # 
    # DP formulation after sorting:
    # dp[i][j] = min cost using exactly j trios from first i elements
    # Transitions:
    # - Skip element i: dp[i][j] = dp[i-1][j]
    # - Form a trio with elements i-2, i-1 as the two smallest (A,B) and some element as C (>=B):
    #   The C element can be any element after i-1. But to minimize, we want A,B adjacent.
    #   Actually the C element doesn't affect balancing, so we just need to "use" one more element.
    #   
    # Better DP: dp[i][j] = min cost to form j trios using some subset of first i elements,
    # where element i is either not used, or is the largest in its trio.
    # 
    # After sorting T[0..N-1]:
    # dp[i][j]: min cost considering first i elements, having formed j trios
    # Option 1: T[i] not used -> dp[i-1][j]
    # Option 2: T[i] is C (largest) in a trio, T[i-1] is B, T[i-2] is A (but A,B must be chosen)
    #   Actually we need to pick which two are A and B. To minimize (A-B)^2, pick adjacent ones.
    #   If T[i] is the largest, we need two more from first i-1 elements.
    #   Best: T[i-1] and T[i-2] as B and A -> cost = (T[i-2]-T[i-1])^2 + dp[i-3][j-1]
    # Option 3: T[i] is B (middle) in a trio... this gets complex.
    # 
    # Simpler known result: optimal solution has trios where A,B are adjacent in sorted order.
    # So we only need: dp[i][j] = min(dp[i-1][j], dp[i-3][j-1] + (T[i-2]-T[i-1])^2)
    # where trio is (T[i-2], T[i-1], T[i]) - but C=T[i] doesn't matter for cost.
    # Wait, the trio is A<=B<=C, cost=(A-B)^2. If we pick T[i-2],T[i-1] as A,B and T[i] as C:
    # cost = (T[i-2]-T[i-1])^2
    
    n = N
    INF = float('inf')
    
    # dp[j] for j trios, iterate over elements
    # Use 1-indexed: T[1..n]
    # dp[i][j] but optimize space
    
    dp = [[INF] * (K + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    
    for i in range(1, n + 1):
        for j in range(0, K + 1):
            # Option 1: skip T[i]
            dp[i][j] = dp[i-1][j]
            # Option 2: form trio with T[i-2], T[i-1], T[i] (1-indexed: T[i-2], T[i-1], T[i])
            if j >= 1 and i >= 3:
                cost = (T[i-3] - T[i-2]) ** 2  # T is 0-indexed, so T[i-3] and T[i-2]
                if dp[i-3][j-1] != INF:
                    val = dp[i-3][j-1] + cost
                    if val < dp[i][j]:
                        dp[i][j] = val
    
    print(dp[n][K])

solve()