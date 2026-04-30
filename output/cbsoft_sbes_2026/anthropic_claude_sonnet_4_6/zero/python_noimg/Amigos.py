import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    
    a = []
    for i in range(N):
        a.append(int(input_data[idx])); idx += 1
    
    b = []
    for i in range(N):
        b.append(int(input_data[idx])); idx += 1
    
    # positions of friends (1-indexed)
    top = [i+1 for i in range(N) if a[i] == 1]  # K positions
    bot = [i+1 for i in range(N) if b[i] == 1]  # K positions
    
    # We need to find K positions (a subset of N positions) such that
    # both top and bot friends can move to those positions with minimum total swaps.
    # The number of swaps to move a sorted sequence of friends to target positions
    # equals sum of |top[i] - target[i]| when both are sorted (optimal assignment).
    
    # The key insight: we need to choose K positions p1 < p2 < ... < pK
    # such that cost(top -> positions) + cost(bot -> positions) is minimized.
    # cost of moving sorted friends to sorted positions = sum |friend[i] - pos[i]|
    
    # This is a DP problem.
    # Let top sorted positions: t[0..K-1]
    # Let bot sorted positions: b[0..K-1]
    # We need to choose K positions (sorted) p[0..K-1] from 1..N
    # minimize sum_i |t[i] - p[i]| + sum_i |b[i] - p[i]|
    
    # DP: dp[i][j] = min cost choosing j positions from first i positions (1..i)
    # Transition: dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + |t[j-1] - i| + |b[j-1] - i|)
    # Answer: dp[N][K]
    
    # With N up to 150000 and K up to 150000, O(N*K) might be too slow.
    # But let's think: we can optimize.
    
    # Actually the optimal positions must be chosen from a smarter set.
    # The cost for position p[j] (0-indexed j) is |t[j] - p[j]| + |b[j] - p[j]|
    # = if t[j] and b[j] are on same side of p[j], or p[j] between them:
    #   if p between t[j] and b[j]: |t[j]-b[j]|
    #   else: 2*dist to closer + |t[j]-b[j]|... 
    # Actually |x-p| + |y-p| is minimized when p is between x and y, giving |x-y|
    # So optimal p[j] in [min(t[j],b[j]), max(t[j],b[j])]
    
    # But positions must be distinct and ordered. Use DP but only over relevant positions.
    # The candidate positions are at most 2K values from t and b arrays, plus neighbors.
    # Actually let's just do O(N*K) with optimized python... N,K up to 150000 is 2.25e10 ops - too slow.
    
    # Better: since cost[j][p] = |t[j]-p| + |b[j]-p|, and positions must be increasing,
    # use the fact that optimal p[j] lies in [min(t[j],b[j]), max(t[j],b[j])].
    
    # DP with only 2K candidate breakpoints - positions from t and b arrays.
    
    candidates = sorted(set(top + bot))
    # But we need exactly K positions chosen from 1..N
    # DP over candidates only
    
    INF = float('inf')
    # dp[j] = min cost to assign first j friends-pairs using positions chosen so far
    # We iterate over candidate positions in order
    
    prev = [INF] * (K + 1)
    prev[0] = 0
    
    for pos in candidates:
        curr = prev[:]
        # try using this position as the j-th position (1-indexed j)
        for j in range(1, K + 1):
            if prev[j-1] < INF:
                cost = abs(top[j-1] - pos) + abs(bot[j-1] - pos)
                val = prev[j-1] + cost
                if val < curr[j]:
                    curr[j] = val
        prev = curr
    
    print(prev[K])

solve()