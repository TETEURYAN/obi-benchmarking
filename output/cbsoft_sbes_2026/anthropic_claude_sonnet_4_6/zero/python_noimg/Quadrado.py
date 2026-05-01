import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(input_data[idx])); idx += 1
        grid.append(row)
    
    row_sums = [sum(grid[i]) for i in range(N)]
    col_sums = [sum(grid[i][j] for i in range(N)) for j in range(N)]
    
    # M is the magic constant - find it from the majority of row sums
    # Since only one number is altered, at most one row and one column are wrong
    # Find M: most common row sum or use median
    from collections import Counter
    row_counter = Counter(row_sums)
    col_counter = Counter(col_sums)
    
    # M should be the value that appears most in row sums
    M = row_counter.most_common(1)[0][0]
    
    # Find the bad row and bad column
    bad_rows = [i for i in range(N) if row_sums[i] != M]
    bad_cols = [j for j in range(N) if col_sums[j] != M]
    
    if len(bad_rows) == 1 and len(bad_cols) == 1:
        r = bad_rows[0]
        c = bad_cols[0]
        # The altered cell is (r, c)
        # row_sums[r] = M + (new_val - orig_val)
        # col_sums[c] = M + (new_val - orig_val)
        diff_row = row_sums[r] - M  # new_val - orig_val
        diff_col = col_sums[c] - M  # new_val - orig_val
        # Both should be equal
        diff = diff_row
        new_val = grid[r][c]
        orig_val = new_val - diff
        print(orig_val, new_val)
    else:
        # Edge case: bad_rows or bad_cols might be empty if diff cancels
        # This shouldn't happen given problem constraints but handle anyway
        # Try all cells
        for r in range(N):
            for c in range(N):
                new_val = grid[r][c]
                diff_r = row_sums[r] - M
                diff_c = col_sums[c] - M
                if diff_r == diff_c:
                    orig_val = new_val - diff_r
                    if orig_val >= 1:
                        # Verify
                        valid = True
                        for i in range(N):
                            s = row_sums[i]
                            if i == r:
                                s = s - new_val + orig_val
                            if s != M:
                                valid = False
                                break
                        if valid:
                            for j in range(N):
                                s = col_sums[j]
                                if j == c:
                                    s = s - new_val + orig_val
                                if s != M:
                                    valid = False
                                    break
                        if valid:
                            print(orig_val, new_val)
                            return

solve()