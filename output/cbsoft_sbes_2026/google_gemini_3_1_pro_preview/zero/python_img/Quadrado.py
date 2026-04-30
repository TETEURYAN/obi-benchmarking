
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    grid = []
    idx = 1
    for _ in range(N):
        row = []
        for _ in range(N):
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
        
    r = -1
    M_prime = -1
    for i in range(N):
        if row_sums[i] != M:
            r = i
            M_prime = row_sums[i]
            break
            
    c = -1
    for j in range(N):
        col_sum = sum(grid[i][j] for i in range(N))
        if col_sum != M:
            c = j
            break
            
    altered = grid[r][c]
    original = altered + M - M_prime
    
    print(f"{original} {altered}")

if __name__ == '__main__':
    main()
