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
    
    row_sums = [sum(grid[i]) for i in range(n)]
    col_sums = [sum(grid[i][j] for i in range(n)) for j in range(n)]
    
    # The correct M: most rows/cols agree
    # Find M by majority or by the fact that only one cell is changed
    # If cell (r,c) is changed by delta, then row r and col c are off by delta
    # All other rows and cols have correct sum M
    
    # Find which rows are "bad" (not equal to M)
    # M is the sum of any row that is not the altered row
    # Since only one cell changed, exactly one row and one column are affected
    
    # Find the row sums - the correct M should be the most common row sum
    from collections import Counter
    row_counter = Counter(row_sums)
    col_counter = Counter(col_sums)
    
    # M is the most frequent row sum (at least n-1 rows have it)
    M_row = row_counter.most_common(1)[0][0]
    M_col = col_counter.most_common(1)[0][0]
    # They should be equal
    M = M_row  # trust row
    
    # Find bad row and bad col
    bad_rows = [i for i in range(n) if row_sums[i] != M]
    bad_cols = [j for j in range(n) if col_sums[j] != M]
    
    if len(bad_rows) == 1 and len(bad_cols) == 1:
        r = bad_rows[0]
        c = bad_cols[0]
        # delta = row_sums[r] - M (how much the altered value exceeds original)
        delta = row_sums[r] - M
        altered = grid[r][c]
        original = altered - delta
        print(original, altered)
    else:
        # Edge case: bad_rows or bad_cols might be empty if delta=0 (impossible since value changed)
        # Or multiple bad rows/cols - shouldn't happen per problem statement
        # Handle case where row sum difference and col sum difference help identify
        if len(bad_rows) == 0 and len(bad_cols) == 0:
            # Shouldn't happen
            pass
        elif len(bad_rows) == 1 and len(bad_cols) == 0:
            r = bad_rows[0]
            delta = row_sums[r] - M
            # Find col: col sum should also be off
            # But col_sums all equal M... contradiction
            # Try each col in that row
            for c in range(n):
                original = grid[r][c] - delta
                if original >= 1:
                    print(original, grid[r][c])
                    return
        elif len(bad_rows) == 0 and len(bad_cols) == 1:
            c = bad_cols[0]
            delta = col_sums[c] - M
            for r in range(n):
                original = grid[r][c] - delta
                if original >= 1:
                    print(original, grid[r][c])
                    return
        else:
            # Multiple bad rows/cols - use intersection
            r = bad_rows[0]
            c = bad_cols[0]
            delta = row_sums[r] - M
            altered = grid[r][c]
            original = altered - delta
            print(original, altered)

solve()