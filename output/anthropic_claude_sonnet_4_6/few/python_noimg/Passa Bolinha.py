import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    I = int(data[idx]); idx += 1
    J = int(data[idx]); idx += 1
    
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(data[idx])); idx += 1
        grid.append(row)
    
    # flag: 0 = down, 1 = up
    flag = [[False]*n for _ in range(n)]
    
    # Directions: initially facing North
    # After rotating 90 degrees clockwise 4 times: E, S, W, N
    # North: row-1, col+0
    # East:  row+0, col+1
    # South: row+1, col+0
    # West:  row+0, col-1
    # Starting direction: North (index 0)
    # Rotating clockwise: N->E->S->W->N
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
    
    def pass_ball(r, c):
        # Raise flag
        flag[r][c] = True
        val = grid[r][c]
        
        # Starting direction is North (index 0), rotate 4 times clockwise
        # Each rotation: turn 90 degrees clockwise
        # After 1st rotation: facing East (index 1)
        # After 2nd rotation: facing South (index 2)
        # After 3rd rotation: facing West (index 3)
        # After 4th rotation: facing North (index 0)
        
        for i in range(4):
            # Turn 90 degrees clockwise from current direction
            # Initial direction is North (0), after i+1 turns: direction index (i+1) % 4
            dir_idx = (i + 1) % 4
            dr, dc = dirs[dir_idx]
            nr, nc = r + dr, c + dc
            
            # Check if neighbor is valid, has flag down, and value >= current
            if 0 <= nr < n and 0 <= nc < n:
                if not flag[nr][nc] and grid[nr][nc] >= val:
                    pass_ball(nr, nc)
        
        # Return ball to whoever passed it (we don't need to do anything here)
    
    sys.setrecursionlimit(200000)
    
    start_r = I - 1
    start_c = J - 1
    
    pass_ball(start_r, start_c)
    
    count = sum(flag[i][j] for i in range(n) for j in range(n))
    print(count)

solve()