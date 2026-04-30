import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    a = [int(input_data[idx+i]) for i in range(N)]
    idx += N
    
    if K > N:
        print(sum(a))
        return
    
    # Key insight: when we merge K consecutive elements, they become 1 element (their OR).
    # We can keep merging. The question is: what's the minimum sum of remaining elements?
    
    # Let's think about which elements can be "consumed" (merged away).
    # When we merge K elements, they become 1. So net reduction is K-1 elements.
    # We can keep merging as long as there are >= K elements.
    
    # DP approach: dp[i] = minimum sum considering first i elements
    # For each position i, we can either:
    # 1. Keep element i as is: dp[i] = dp[i-1] + a[i-1]
    # 2. Merge some window ending at i: but this is complex
    
    # Better DP: dp[i] = minimum impurity sum for the first i elements
    # Transition: 
    # - Don't merge ending here: dp[i] = dp[i-1] + a[i-1]
    # - Merge a block of size K ending at position i (1-indexed): 
    #   The merged result has OR of a[i-K..i-1], and we need dp[i-K] + OR_value
    #   But after merging, we have 1 element, so dp[i] = dp[i-K] + OR(a[i-K:i])
    # - But we can also merge larger blocks by chaining merges
    
    # Actually, after merging K elements into 1, we can merge again.
    # The key observation: any contiguous subarray of length >= K can be reduced to 
    # a single element (its OR) through repeated merging, as long as we can always 
    # find K consecutive elements.
    
    # More precisely: a contiguous block of length L can be reduced to 1 element if L >= K,
    # or to L elements if L < K. But intermediate merges affect what's available.
    
    # Actually: a block of length L can be reduced to ceil((L-1)/(K-1)) ... 
    # No. Let's think: each merge reduces count by K-1. Starting with L elements,
    # we can reduce to L - m*(K-1) elements for any valid m, minimum is 1 if L >= K.
    # We can get to 1 element from L elements if L >= K (merge K, get L-K+1, repeat).
    # L - m*(K-1) = 1 => m = (L-1)/(K-1). This works if (L-1) % (K-1) == 0.
    # Otherwise minimum is 1 + ((L-1) % (K-1)) ... 
    # Actually minimum reachable from L is: ((L-1) % (K-1)) + 1 if L >= K, else L.
    
    # So a block of length L can be reduced to r = ((L-1) % (K-1)) + 1 elements if L >= K.
    # But all those elements will have OR of the entire block as their value? No...
    
    # This is complex. Let me use DP where dp[i] = min sum for first i elements.
    
    # Precompute sparse table for range OR queries
    import math
    LOG = max(1, math.floor(math.log2(N)) + 1) if N > 0 else 1
    sparse = [a[:]]
    for j in range(1, LOG + 1):
        prev = sparse[j-1]
        curr = []
        for i in range(N - (1 << j) + 1):
            curr.append(prev[i] | prev[i + (1 << (j-1))])
        sparse.append(curr)
    
    def query_or(l, r):  # [l, r] 0-indexed
        length = r - l + 1
        k = length.bit_length() - 1
        return sparse[k][l] | sparse[k][r - (1 << k) + 1]
    
    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        # Option 1: take element i alone
        dp[i] = min(dp[i], dp[i-1] + a[i-1])
        # Option 2: merge a block of size >= K ending at i, reducing to 1 element
        # Block from j+1 to i (1-indexed), length = i - j
        # This block can be reduced to 1 element if i - j >= K
        # The OR value is query_or(j, i-1)
        # But we need (i - j - 1) % (K - 1) == 0 for exact reduction to 1
        # Actually we can reduce block of size L to 1 if we can chain merges
        # L >= K and we can always merge: yes if L >= K we can get to 1
        # by merging first K, then again K (the new one + K-1 more), etc.
        for j in range(max(0, i - 1), -1, -1):
            L = i - j
            if L < K:
                continue
            # Can reduce to 1 element with OR value
            or_val = query_or(j, i-1)
            dp[i] = min(dp[i], dp[j] + or_val)
            break  # We want minimum, but OR only increases with larger blocks
        # Actually we should try all valid j where block can reduce to 1
        # But OR is monotone non-decreasing as block grows, so smallest valid block is best
        # Smallest block that can reduce to 1: size K (if (K-1)%(K-1)==0, yes)
        # Any size L >= K where (L-1)%(K-1)==0
        # Let's try all such j
    
    # Redo properly
    dp = [INF] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        dp[i] = min(dp[i], dp[i-1] + a[i-1])
        # Try blocks ending at i that reduce to exactly 1 element
        # Block size L = i - j, need L >= K and (L-1) % (K-1) == 0
        # L = 1 + m*(K-1) for m >= 1, so L in {K, 2K-1, 3K-2, ...}
        L = K
        while L <= i:
            j = i - L
            or_val = query_or(j, i-1)
            dp[i] = min(dp[i], dp[j] + or_val)
            L += (K - 1)
    
    print(dp[N])

solve()