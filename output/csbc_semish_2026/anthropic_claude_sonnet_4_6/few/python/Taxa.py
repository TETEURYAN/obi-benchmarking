import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    F = float(data[idx]); idx += 1
    X = []
    for i in range(N):
        X.append(int(data[idx])); idx += 1
    
    if N == 1:
        print("0.00")
        return
    
    # The lots are arranged in a circle. We need to split them into N individual lots.
    # Each split divides a contiguous arc into two contiguous arcs.
    # The tax for a split is F * (area of the larger part).
    # We want to minimize total tax.
    
    # Since lots are in a circle, we can think of this as interval DP on a circular arrangement.
    # We need to make N-1 cuts. The cuts must be between adjacent lots.
    # There are N possible cut positions (between lot i and lot i+1).
    # We need to choose N-1 of them (all but one, since it's a circle - actually we need all N cuts
    # but wait, N lots need N-1 splits).
    
    # Actually: the lots form a circle. To split into N individual lots, we need N-1 splits.
    # Each split takes a contiguous segment (arc) and splits it into two contiguous segments.
    # The cost is F * max(left_sum, right_sum).
    
    # This is equivalent to: we have N elements in a circle, we need to build a binary tree
    # of splits. The root covers all N elements, and each internal node splits its range into two.
    
    # For circular arrangement: fix one "cut" position to linearize.
    # Since we must make exactly N-1 cuts among N possible positions between adjacent elements,
    # and the circle has N gaps, we must leave exactly one gap uncut... wait no.
    # Actually in a circle with N lots, to separate all N lots we need N cuts (one between each pair).
    # But we only need N-1 splits (each split adds one more piece). Starting with 1 piece, after N-1 splits we have N pieces.
    # But a circle needs N cuts to separate all... 
    # Wait: if we have a circular arrangement, the "terrain" is one connected piece initially.
    # Each split divides one piece into two. After N-1 splits, we have N pieces.
    # For a circle of N lots, we need to cut N-1 of the N gaps between adjacent lots.
    # One gap remains "uncut" - but that's fine because the split operations handle it.
    
    # Actually no - to separate N lots arranged in a circle into individual lots, 
    # we need exactly N cuts (all N gaps must be cut). But N-1 splits give N pieces...
    # Hmm, let me reconsider. Each split cuts one gap. N-1 splits cut N-1 gaps.
    # But we need all N gaps cut to separate all lots. Contradiction?
    
    # Re-reading: the terrain is initially one piece (the whole circle). 
    # A split divides it into two contiguous arcs. After N-1 splits we have N pieces = N lots. OK.
    # For a circle, the first split must cut the circle at two points? No - one cut on a circle gives two arcs.
    # So one split = one cut on the circle = cuts one gap. After N-1 splits, N-1 gaps are cut, giving N arcs. Correct!
    
    # So we fix which gap is NOT cut (the "root" gap), linearize, and do interval DP.
    # We try all N possible "uncut" gaps and take the minimum.
    
    # Interval DP: dp[i][j] = min cost to split segment from i to j into individual lots
    # sum[i][j] = sum of X[i..j]
    # dp[i][i] = 0
    # dp[i][j] = min over k in [i, j-1] of: dp[i][k] + dp[k+1][j] + F * max(sum[i][k], sum[k+1][j])
    
    INF = float('inf')
    
    # Precompute prefix sums for doubled array (for circular)
    # We'll try each starting point (which gap is the "root")
    
    best = INF
    
    for start in range(N):
        # Linearize starting after gap between start-1 and start
        arr = [X[(start + i) % N] for i in range(N)]
        
        # Prefix sums
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + arr[i]
        
        def rsum(i, j):
            return prefix[j+1] - prefix[i]
        
        # dp[i][j]
        dp = [[INF] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0.0
        
        for length in range(2, N+1):
            for i in range(N - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    left = rsum(i, k)
                    right = rsum(k+1, j)
                    cost = dp[i][k] + dp[k+1][j] + F * max(left, right)
                    if cost < dp[i][j]:
                        dp[i][j] = cost
        
        if dp[0][N-1] < best:
            best = dp[0][N-1]
    
    print(f"{best:.2f}")

solve()