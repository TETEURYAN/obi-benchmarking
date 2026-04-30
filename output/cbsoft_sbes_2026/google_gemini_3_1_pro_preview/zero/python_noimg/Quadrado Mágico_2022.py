import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    grid = []
    idx = 1
    
    zero_r = -1
    zero_c = -1
    
    for i in range(N):
        row = []
        for j in range(N):
            val = int(input_data[idx])
            row.append(val)
            if val == 0:
                zero_r = i
                zero_c = j
            idx += 1
        grid.append(row)
        
    if zero_r == 0:
        magic_sum = sum(grid[1])
    else:
        magic_sum = sum(grid[0])
        
    current_sum = sum(grid[zero_r])
    missing_value = magic_sum - current_sum
    
    print(missing_value)
    print(zero_r + 1)
    print(zero_c + 1)

if __name__ == '__main__':
    solve()