import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    grid = []
    row_sums = [0] * N
    col_sums = [0] * N
    
    idx = 1
    for i in range(N):
        row = [int(x) for x in input_data[idx:idx+N]]
        grid.append(row)
        row_sums[i] = sum(row)
        for j in range(N):
            col_sums[j] += row[j]
        idx += N
        
    max_weight = -1
    for i in range(N):
        r_sum = row_sums[i]
        row = grid[i]
        for j in range(N):
            w = r_sum + col_sums[j] - (row[j] << 1)
            if w > max_weight:
                max_weight = w
                
    print(max_weight)

if __name__ == '__main__':
    solve()