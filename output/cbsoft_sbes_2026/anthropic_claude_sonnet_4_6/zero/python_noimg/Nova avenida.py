import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # We need to choose a North-South street to widen
    # North-South streets run vertically, there are M+1 such streets (at positions 0, 1, ..., M)
    # But the streets are between columns, so street j is between column j-1 and column j
    # Actually, streets in N-S direction: there are M+1 streets (borders of M columns)
    # Street at position j (0-indexed, j from 0 to M) has:
    #   - left side: column j-1 (if j > 0)
    #   - right side: column j (if j < M)
    # We need to expropriate ALL blocks on ONE side of the chosen street
    # So for street j:
    #   - cost of left side = sum of all blocks in column j-1 (N blocks)
    #   - cost of right side = sum of all blocks in column j (N blocks)
    # We choose the minimum between left and right for each street
    # Then find the minimum over all streets
    
    # Compute column sums
    col_sum = [0] * M
    for i in range(N):
        for j in range(M):
            col_sum[j] += grid[i][j]
    
    min_cost = float('inf')
    
    # Street 0: only right side (column 0)
    # Street M: only left side (column M-1)
    # Streets 1 to M-1: min of left (col j-1) and right (col j)
    
    for j in range(M + 1):
        if j == 0:
            cost = col_sum[0]
        elif j == M:
            cost = col_sum[M - 1]
        else:
            cost = min(col_sum[j - 1], col_sum[j])
        min_cost = min(min_cost, cost)
    
    print(min_cost)

main()