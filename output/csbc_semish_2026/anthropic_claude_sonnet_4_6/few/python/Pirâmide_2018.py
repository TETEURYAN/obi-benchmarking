import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(data[idx])); idx += 1
        grid.append(row)
    
    # dp[i][j] = minimum weight of pyramid where row i has i boxes ending at column j (0-indexed)
    # Row i (1-indexed) needs exactly i consecutive boxes
    # The consecutive boxes in row i must "contain" the consecutive boxes in row i-1
    # i.e., if row i-1 ends at column j (boxes from j-i+2 to j), 
    # then row i must have i boxes that include columns j-i+2 to j
    # So row i can start at j-i+1 (end at j) or start at j-i+2 (end at j+1)
    # In other words, if row i ends at column e, row i-1 must end at column e or e-1
    # (since row i has i boxes: columns e-i+1..e, row i-1 has i-1 boxes: columns e-i+2..e or e-i+1..e-1)
    # Wait let me re-think:
    # Row i (1-indexed) has i consecutive boxes. Let's say they span columns [l, l+i-1] (0-indexed).
    # Row i+1 has i+1 consecutive boxes spanning [l', l'+i]. 
    # The constraint: box below each box in row i must be in pyramid.
    # Row i is above row i+1 (row 1 is top). So box at (i, c) requires box at (i+1, c) to be present.
    # So the i boxes in row i must all have their counterparts in row i+1.
    # Row i spans [l, l+i-1], row i+1 spans [l', l'+i].
    # We need [l, l+i-1] subset of [l', l'+i].
    # So l' <= l and l'+i >= l+i-1, i.e., l' <= l and l' >= l-1.
    # So l' = l or l' = l-1.
    # Equivalently, if we track the left start:
    # l_{i+1} in {l_i - 1, l_i}
    
    # dp[i][l] = min weight for rows 1..i where row i starts at column l
    # Row i spans columns l to l+i-1, must be valid: l >= 0, l+i-1 <= n-1
    
    INF = float('inf')
    
    # Initialize for row 1 (i=1, 1-indexed), spans [l, l], l in 0..n-1
    dp = [INF] * n
    for l in range(n):
        dp[l] = grid[0][l]
    
    for i in range(2, n+1):  # row i (1-indexed)
        new_dp = [INF] * n
        # row i spans [l, l+i-1], valid if l+i-1 <= n-1 => l <= n-i
        # row i-1 spans [l_prev, l_prev+i-2]
        # l_prev in {l, l+1} (since l' in {l_prev-1, l_prev} means l_prev in {l, l+1})
        row_sum = [0] * n  # precompute sum of i consecutive starting at l
        for l in range(n - i + 1):
            s = sum(grid[i-1][l:l+i])
            row_sum[l] = s
        
        for l in range(n - i + 1):
            # previous row could have started at l or l+1
            best_prev = INF
            if l < n and dp[l] < best_prev:
                best_prev = dp[l]
            if l+1 < n and dp[l+1] < best_prev:
                best_prev = dp[l+1]
            if best_prev < INF:
                new_dp[l] = best_prev + row_sum[l]
        
        dp = new_dp
    
    print(min(dp))

solve()