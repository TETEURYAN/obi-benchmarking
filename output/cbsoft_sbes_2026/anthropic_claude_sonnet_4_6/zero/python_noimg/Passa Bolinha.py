import sys
from sys import setrecursionlimit

setrecursionlimit(100000)

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    I = int(input_data[idx]); idx += 1
    J = int(input_data[idx]); idx += 1
    
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(input_data[idx])); idx += 1
        grid.append(row)
    
    # flags: 0 = down, 1 = up
    flags = [[False]*N for _ in range(N)]
    
    # Directions: North=0, East=1, South=2, West=3
    # Initially facing North
    # dr, dc for each direction
    # North: row-1, col+0
    # East: row+0, col+1
    # South: row+1, col+0
    # West: row+0, col-1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    def pass_ball(r, c):
        # Raise flag
        flags[r][c] = True
        val = grid[r][c]
        
        # Current direction starts at North (0), rotate 90 clockwise 4 times
        direction = 0  # starts facing North, but first action is to turn 90 clockwise
        
        for _ in range(4):
            # Turn 90 degrees clockwise
            direction = (direction + 1) % 4
            
            # Check the neighbor in front
            nr = r + dr[direction]
            nc = c + dc[direction]
            
            if 0 <= nr < N and 0 <= nc < N:
                neighbor_val = grid[nr][nc]
                if neighbor_val >= val and not flags[nr][nc]:
                    # Pass ball to neighbor
                    pass_ball(nr, nc)
                    # Neighbor returns ball, continue
        
        # Return ball to whoever passed it (handled by caller)
    
    # Convert to 0-indexed
    start_r = I - 1
    start_c = J - 1
    
    pass_ball(start_r, start_c)
    
    count = sum(flags[i][j] for i in range(N) for j in range(N))
    print(count)

solve()