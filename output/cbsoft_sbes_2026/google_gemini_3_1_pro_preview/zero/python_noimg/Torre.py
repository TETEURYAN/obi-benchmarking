import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    grid = []
    idx = 1
    for _ in range(N):
        grid.append([int(x) for x in input_data[idx:idx+N]])
        idx += N
        
    row_sums = [sum(row) for row in grid]
    
    col_sums = [0] * N
    for j in range(N):
        col_sums[j] = sum(grid[i][j] for i in range(N))
        
    max_weight = -1
    for i in range(N):
        r_sum = row_sums[i]
        row = grid[i]
        for j in range(N):
            w = r_sum + col_sums[j] - 2 * row[j]
            if w > max_weight:
                max_weight = w
                
    print(max_weight)

if __name__ == '__main__':
    solve()