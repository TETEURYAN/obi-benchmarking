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
            idx += 1
            row.append(val)
            if val == 0:
                zero_r = i
                zero_c = j
        grid.append(row)
        
    target_sum = 0
    for i in range(N):
        if i != zero_r:
            target_sum = sum(grid[i])
            break
            
    current_sum = sum(grid[zero_r])
    missing_value = target_sum - current_sum
    
    print(missing_value)
    print(zero_r + 1)
    print(zero_c + 1)

if __name__ == '__main__':
    solve()