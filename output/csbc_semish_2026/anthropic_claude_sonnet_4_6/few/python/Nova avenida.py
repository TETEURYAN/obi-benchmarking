import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    grid = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(int(data[idx])); idx += 1
        grid.append(row)
    
    # We need to choose a North-South street to widen.
    # North-South streets run between columns.
    # There are M+1 such streets (at positions 0, 1, ..., M),
    # but the boundary streets (0 and M) have only one side with blocks.
    # For street j (between column j-1 and column j), we can choose:
    #   - left side: column j-1 (sum of all rows in column j-1)
    #   - right side: column j (sum of all rows in column j)
    # We pick the minimum of the two sides for each street,
    # then find the minimum over all streets.
    
    # Compute column sums
    col_sum = [0] * M
    for i in range(N):
        for j in range(M):
            col_sum[j] += grid[i][j]
    
    # Streets between columns: street j is between col j-1 and col j (j from 1 to M-1)
    # For boundary streets (j=0: left of col 0, j=M: right of col M-1),
    # there's only one side to expropriate.
    # But actually boundary streets only have one side of blocks,
    # so cost = that one side's column sum.
    
    # Street at left boundary (j=0): only right side = col_sum[0]
    # Street at right boundary (j=M): only left side = col_sum[M-1]
    # Interior streets j (1 to M-1): min(col_sum[j-1], col_sum[j])
    
    ans = min(col_sum[0], col_sum[M-1])
    for j in range(1, M):
        cost = min(col_sum[j-1], col_sum[j])
        if cost < ans:
            ans = cost
    
    print(ans)

main()