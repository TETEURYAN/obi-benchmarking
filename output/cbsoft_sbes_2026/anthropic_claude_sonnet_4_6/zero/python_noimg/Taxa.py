import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    F = float(input_data[idx]); idx += 1
    X = []
    for i in range(N):
        X.append(int(input_data[idx])); idx += 1
    
    if N == 1:
        print("0.00")
        return
    
    # The lots are arranged in a circle. We need to split them into N individual lots.
    # Each split divides a contiguous arc into two contiguous arcs.
    # Tax for a split = F * (area of larger part)
    # We want to minimize total tax.
    
    # Since lots are in a circle, we need to "cut" the circle into N pieces.
    # This is equivalent to: first, we pick one cut to linearize the circle,
    # then we do interval DP on the linear arrangement.
    # But since it's circular, we need to consider all possible "first cuts".
    
    # Actually, for circular arrangement: we need N-1 cuts total.
    # The key insight: in a circular arrangement, we can think of it as:
    # we need to make N-1 cuts among N possible positions (between adjacent lots).
    # The order of cuts matters for the tax calculation.
    
    # Let's think differently. The lots are on a circle. A "segment" is a contiguous
    # arc of lots. We start with the full circle (all N lots) and need to split it
    # into individual lots.
    
    # But a circle can't be split into two parts with a single cut in the usual sense...
    # Wait, re-reading: the land is around a lake. The first cut splits the circular
    # land into two arcs. Then each arc can be further split.
    
    # So: circular interval DP.
    # For a circular arrangement, the first cut must split the circle into two linear segments.
    # After that, each segment is linear and can be split independently.
    
    # prefix sums
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + X[i]
    total = prefix[N]
    
    # For linear segment from i to j (inclusive, 0-indexed), sum = prefix[j+1] - prefix[i]
    # dp[i][j] = minimum tax to split segment [i..j] into individual lots
    # When splitting [i..j] at position k (i <= k < j):
    #   left part = [i..k], right part = [k+1..j]
    #   tax = F * max(sum[i..k], sum[k+1..j]) + dp[i][k] + dp[k+1][j]
    
    # For circular: try all first cuts (i, i+1) for i in 0..N-1
    # First cut splits circle into [0..k] and [k+1..N-1] for some k
    # tax for first cut = F * max(sum[0..k], sum[k+1..N-1])
    # But we need to consider all rotations... actually the circle split:
    # We fix the circle as array X[0..N-1]. First cut separates some arc [i..j] from rest.
    # This is equivalent to: try all ways to split circle into two arcs.
    
    INF = float('inf')
    
    # dp for linear segments
    dp = [[0.0] * N for _ in range(N)]
    
    # length 1: no split needed, cost = 0
    # fill by increasing length
    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            dp[i][j] = INF
            seg_sum = prefix[j+1] - prefix[i]
            for k in range(i, j):
                left_sum = prefix[k+1] - prefix[i]
                right_sum = seg_sum - left_sum
                cost = F * max(left_sum, right_sum) + dp[i][k] + dp[k+1][j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    # For circular: first cut splits circle into two arcs
    # Try all first cuts: split between position k and k+1
    # Arc1 = [k+1 .. k] (going around) - but we need linear representation
    # Equivalent: for each starting point of the "open" arc
    # Actually: duplicate array and use linear DP on 2N array? No.
    
    # For circular with N lots, first cut creates two arcs.
    # We try all possible first cuts: between lot k and lot k+1 (mod N)
    # This gives arc [k+1..k+N-1] mod N of various lengths... 
    # Actually simpler: try all k from 0 to N-1 as the "split point"
    # meaning we split off [0..k] from [k+1..N-1] in the linearized version.
    
    ans = INF
    for k in range(N - 1):
        left_sum = prefix[k+1]
        right_sum = total - left_sum
        cost = F * max(left_sum, right_sum) + dp[0][k] + dp[k+1][N-1]
        if cost < ans:
            ans = cost
    
    print(f"{ans:.2f}")

solve()