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
        if tx != -1:
            break
    
    direction = {'N': (-1, 0), 'S': (1, 0), 'L': (0, 1), 'O': (0, -1)}
    
    # Simulate with cycle detection
    # visited stores {(r,c): step} when we first visited
    visited = {}
    r, c = A, B
    step = 0
    
    while True:
        # Check if at treasure
        if r == tx and c == ty:
            print(step)
            return
        
        # Check if out of bounds
        if r < 0 or r >= M or c < 0 or c >= M:
            print(-1)
            return
        
        # Check if we've been here before (cycle)
        if (r, c) in visited:
            print(0)
            return
        
        visited[(r, c)] = step
        
        # Move
        d = grid[r][c]
        dr, dc = direction[d]
        r += dr
        c += dc
        step += 1

solve()