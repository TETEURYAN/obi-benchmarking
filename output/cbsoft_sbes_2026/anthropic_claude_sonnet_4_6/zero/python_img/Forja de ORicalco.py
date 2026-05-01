
```python
import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    a = [int(input_data[idx+i]) for i in range(N)]
    idx += N
    
    # If K > N, we can never merge anything, so the answer is sum(a)
    if K > N:
        print(sum(a))
        return
    
    # Key insight: when we merge K consecutive elements, they become their OR.
    # We can keep merging. The question is: what's the minimum sum of remaining elements?
    
    # Let's think about what sequences of operations are possible.
    # After all operations, we have some remaining elements. 
    # The remaining elements are either original elements or OR of consecutive ranges.
    
    # Actually, let's think differently. 
    # Each merge reduces the count by K-1.
    # Starting with N elements, after m merges we have N - m*(K-1) elements.
    # We need N - m*(K-1) >= 1, so m <= (N-1)/(K-1).
    
    # The key observation: which elements can we "eliminate" (merge into others)?
    # When we merge positions i..i+K-1, they become one element with OR value.
    # 
    # This is a complex optimization problem. Let's think about DP.
    # 
    # dp[i] = minimum sum achievable for the first i elements
    # 
    # For each position i, we can either:
    # 1. Keep element i as is: dp[i] = dp[i-1] + a[i-1]
    # 2. Merge some range ending at i: but this is complex
    #
    # Actually, let me think about what the final configuration looks like.
    # The final array is a partition of [0..N-1] into contiguous groups,
    # where each group has size 1 or can be reduced to size 1 via merges.
    # A group of size s can be reduced to 1 element if (s-1) is divisible by (K-1)
    # and s >= K (or s == 1).
    # Wait, more carefully: a contiguous segment of length s can be reduced to 
    # ceil... let me think again.
    #
    # A segment of length s: we can apply merges within it.
    # After one merge of K elements within it, length becomes s - (K-1).
    # We can keep merging as long as length >= K.
    # Final length: s - m*(K-1) where m is max such that s - m*(K-1) >= 1.
    # But we want to reduce to exactly 1 element: s - m*(K-1) = 1
    # => s = 1 + m*(K-1) for some non-negative integer m.
    # So s ≡ 1 (mod K-1) and s >= 1.
    # If s == 1: trivially 1 element.
    # If s >= K and s ≡ 1 (mod K-1): can reduce to 1 element with OR of all.
    #
    # So the problem reduces to: partition [0..N-1] into contiguous segments
    # where each segment has size ≡ 1 (mod K-1).
    # The cost of a segment is: if size==1, cost = a[i]; else cost = OR of all elements in segment.
    # Minimize total cost.
    
    # Special case K=2: K-1=1, so any size ≡ 1 (mod 1) = any size works.
    # So we can merge any contiguous subarray into its OR.
    
    # DP: dp[i] = min cost for first i elements (0-indexed: elements 0..i-1)
    # dp[0] = 0
    # dp[i] = min over all valid segment lengths s ending at i:
    #   dp[i-s] + cost(i-s, i-1)
    # where s ≡ 1 (mod K-1)
    
    # For large N, we need efficient computation.
    # Valid segment sizes: 1, K, 2K-1, 3K-2, ... i.e., 1 + j*(K-1) for j=0,1,2,...
    
    # Precompute prefix OR for range queries
    # prefix_or[i] = OR of a[0..i-1], but we need range OR.
    # We can use sparse table for O(1) range OR queries... but OR is not invertible.
    # Actually we need OR of a[l..r]. We can use sparse table.
    
    # Build sparse table for range OR
    import math
    LOG = max(1, math.floor(math.log2(N)) + 1) if N > 0 else 1
    sparse = [a[:]]
    for j in range(1, LOG + 1):
        prev = sparse[j-1]
        curr = []
        for i in range(N - (1 << j) + 1):
            curr.append(prev[i] | prev[i + (1 << (j-1))])
        sparse.append(curr)
    
    def range_or(l, r):  # inclusive
        if l > r:
            return 0
        length = r - l + 1
        k = math.floor(math.log2(length))
        return sparse[k][l] | sparse[k][r - (1 << k) + 1]
    
    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[0] = 0
    
    km1 = K - 1
    
    for i in range(1, N + 1):
        # Try all valid segment sizes s = 1 + j*(K-1)
        s = 1
        while s <= i:
            l = i - s
            if dp[l] < INF:
                if s == 1:
                    cost = a[i-1]
                else:
                    cost = range_or(l, i-1)
                val = dp[l] + cost
                if val < dp[i]:
                    dp[i] = val
            s += km1
    
    print(dp[N])

solve()
```