import sys

def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = int(input_data[1])
    
    if N == 1:
        print(S)
        return
    
    # Construction of arithmetic square:
    # An arithmetic square requires that any permutation selection sums to S.
    # 
    # Key insight: if grid[i][j] = r[i] + c[j], then any legal selection
    # (one per row, one per column) sums to sum(r[i]) + sum(c[j]) = constant.
    # 
    # So we need grid[i][j] = r[i] + c[j] with all values distinct.
    #
    # Choose r[i] = i * N for i in 0..N-1
    # Choose c[j] = j for j in 0..N-1
    # Then grid[i][j] = i*N + j, which are all distinct (0 to N^2-1)
    # Sum of any legal selection = sum(r[i] for all i) + sum(c[j] for all j)
    # = N*(N-1)/2 * N + N*(N-1)/2
    # = N*(N-1)/2 * (N+1)
    # = N*(N^2-1)/2
    #
    # We want sum = S, so we need to adjust.
    # Current sum = N*(N^2-1)/2
    # We need to add (S - current_sum) distributed somehow.
    # 
    # We can add offset/N to each r[i] (if divisible) or adjust c[0] by adding delta to all rows in col 0.
    # 
    # Better: add delta to r[0] where delta = S - current_sum - but that changes only one row's contribution.
    # Actually if we add delta to r[0], the sum becomes current_sum + delta = S. Good.
    # But we need all values distinct.
    #
    # Let's use: r[i] = i * N * K for some large K, c[j] = j
    # Actually simpler: use r[i] = i * N, c[j] = j
    # current_sum = sum(r) + sum(c) = N*N*(N-1)/2 + N*(N-1)/2 = N*(N-1)/2*(N+1)
    # 
    # Adjust r[0] by adding (S - current_sum):
    # new r[0] = 0 + (S - current_sum)
    # Values in row 0: r[0] + j = (S - current_sum) + j for j=0..N-1
    # Values in row i (i>0): i*N + j for j=0..N-1
    # 
    # We need all N^2 values distinct.
    # Row i (i>0) values: i*N, i*N+1, ..., i*N+N-1
    # Row 0 values: (S-current_sum), (S-current_sum)+1, ..., (S-current_sum)+N-1
    # 
    # These are N consecutive integers starting at different points.
    # They're distinct as long as row 0's range doesn't overlap with any other row's range.
    # Row i range: [i*N, i*N+N-1]
    # Row 0 range: [S-current_sum, S-current_sum+N-1]
    # 
    # current_sum = N*(N-1)*(N+1)/2
    # For large N this could be large, so S - current_sum could be very negative.
    # The absolute value constraint is 10^9.
    # N <= 1000, so i*N <= 999*1000 = 999000, fine.
    # S - current_sum: current_sum up to 1000*999*1001/2 ~ 500M, S up to 1000
    # So |S - current_sum| could be ~500M which is < 10^9. Fine!
    # 
    # But we need distinctness. Let's just use large row multiplier to ensure no overlap.
    # Use r[i] = i * (N+1) * 2 to space rows far apart, then adjust.
    
    # Simple approach: r[i] = i * 2 * N (spacing 2N between rows ensures no overlap with row 0 adjustment)
    # Actually let's just check: use r[i] = i*N, c[j]=j, adjust r[0].
    # Row 0 starts at S - current_sum. Other rows start at i*N (i>=1), i.e., N, 2N, ...
    # If S - current_sum is not in [N - (N-1), (N-1)*N + (N-1)] = [1, N^2-1], we're fine.
    # To be safe, use r[i] = i * N * 2, which spaces rows by 2N.
    
    current_sum_base = sum(i * N for i in range(N)) + sum(j for j in range(N))
    # = N*N*(N-1)//2 + N*(N-1)//2
    
    r = [i * N for i in range(N)]
    c = list(range(N))
    
    current_sum_val = sum(r) + sum(c)
    delta = S - current_sum_val
    r[0] += delta
    
    grid = []
    for i in range(N):
        row = [r[i] + c[j] for j in range(N)]
        grid.append(row)
    
    out = []
    for row in grid:
        out.append(' '.join(map(str, row)))
    print('\n'.join(out))

solve()