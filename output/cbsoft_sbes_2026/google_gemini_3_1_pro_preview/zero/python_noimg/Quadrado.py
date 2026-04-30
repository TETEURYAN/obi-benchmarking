import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    grid = []
    idx = 1
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    row_sums = [sum(row) for row in grid]
    
    if row_sums[0] == row_sums[1]:
        M = row_sums[0]
    elif row_sums[0] == row_sums[2]:
        M = row_sums[0]
    else:
        M = row_sums[1]
        
    wrong_r = -1
    for i in range(N):
        if row_sums[i] != M:
            wrong_r = i
            break
            
    col_sums = []
    for j in range(N):
        c_sum = sum(grid[i][j] for i in range(N))
        col_sums.append(c_sum)
        
    wrong_c = -1
    for j in range(N):
        if col_sums[j] != M:
            wrong_c = j
            break
            
    altered = grid[wrong_r][wrong_c]
    original = altered + (M - row_sums[wrong_r])
    
    print(f"{original} {altered}")

if __name__ == '__main__':
    solve()