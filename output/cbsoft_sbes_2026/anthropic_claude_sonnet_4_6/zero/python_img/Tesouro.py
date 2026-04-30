import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    M = int(input_data[idx]); idx += 1
    grid = []
    for i in range(M):
        grid.append(input_data[idx]); idx += 1
    A = int(input_data[idx]) - 1; idx += 1
    B = int(input_data[idx]) - 1; idx += 1
    
    # Find treasure position
    tx, ty = -1, -1
    for i in range(M):
        for j in range(M):
            if grid[i][j] == 'X':
                tx, ty = i, j
                break
    
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'L': (0, 1),
        'O': (0, -1)
    }
    
    # Simulate with cycle detection
    # Since there are M*M cells, if we take more than M*M steps without finding treasure or going out, it's a cycle
    
    visited = {}
    cur_r, cur_c = A, B
    time = 0
    
    while True:
        # Check if current position is treasure
        if cur_r == tx and cur_c == ty:
            print(time)
            return
        
        # Check if we've been here before (cycle)
        if (cur_r, cur_c) in visited:
            print(0)
            return
        
        visited[(cur_r, cur_c)] = time
        
        # Move
        cell = grid[cur_r][cur_c]
        dr, dc = direction[cell]
        new_r = cur_r + dr
        new_c = cur_c + dc
        
        # Check bounds
        if new_r < 0 or new_r >= M or new_c < 0 or new_c >= M:
            print(-1)
            return
        
        cur_r, cur_c = new_r, new_c
        time += 1

solve()