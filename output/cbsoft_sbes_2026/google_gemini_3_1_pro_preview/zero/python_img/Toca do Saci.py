import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    grid = []
    idx = 2
    start_r = start_c = -1
    
    for r in range(N):
        row = input_data[idx:idx+M]
        idx += M
        grid.append(row)
        if '3' in row:
            start_r = r
            start_c = row.index('3')
            
    r, c = start_r, start_c
    prev_r, prev_c = -1, -1
    count = 1
    
    while grid[r][c] != '2':
        if r > 0 and (r - 1 != prev_r or c != prev_c) and grid[r - 1][c] != '0':
            prev_r, prev_c = r, c
            r -= 1
        elif r < N - 1 and (r + 1 != prev_r or c != prev_c) and grid[r + 1][c] != '0':
            prev_r, prev_c = r, c
            r += 1
        elif c > 0 and (r != prev_r or c - 1 != prev_c) and grid[r][c - 1] != '0':
            prev_r, prev_c = r, c
            c -= 1
        else:
            prev_r, prev_c = r, c
            c += 1
        count += 1
        
    print(count)

if __name__ == '__main__':
    solve()