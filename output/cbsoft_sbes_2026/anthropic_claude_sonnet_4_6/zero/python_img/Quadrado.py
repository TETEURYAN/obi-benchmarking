import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(data[idx])); idx += 1
        grid.append(row)
    
    row_sums = [sum(grid[i]) for i in range(N)]
    col_sums = [sum(grid[i][j] for i in range(N)) for j in range(N)]
    
    # Find M: the correct magic sum
    # Most rows and columns have sum M, one row and one column are off
    # M can be determined by majority or by the correct rows/cols
    
    # Count row sums frequencies
    from collections import Counter
    row_freq = Counter(row_sums)
    col_freq = Counter(col_sums)
    
    # M should be the most common row sum (at least N-1 rows have it)
    M_row = row_freq.most_common(1)[0][0]
    M_col = col_freq.most_common(1)[0][0]
    
    # They should be equal
    M = M_row  # should equal M_col
    
    # Find the bad row and bad column
    bad_rows = [i for i in range(N) if row_sums[i] != M]
    bad_cols = [j for j in range(N) if col_sums[j] != M]
    
    # The altered cell is at intersection of bad row and bad col
    if len(bad_rows) == 1 and len(bad_cols) == 1:
        r = bad_rows[0]
        c = bad_cols[0]
        altered_value = grid[r][c]
        # row_sums[r] - altered_value + original = M
        # col_sums[c] - altered_value + original = M
        original = M - row_sums[r] + altered_value
        print(original, altered_value)
    else:
        # Edge case: might need more careful handling
        # Try all possible bad cells
        # This shouldn't happen given problem constraints
        # But handle just in case
        for r in bad_rows:
            for c in bad_cols:
                altered_value = grid[r][c]
                original_from_row = M - row_sums[r] + altered_value
                original_from_col = M - col_sums[c] + altered_value
                if original_from_row == original_from_col and original_from_row >= 1:
                    print(original_from_row, altered_value)
                    return

solve()