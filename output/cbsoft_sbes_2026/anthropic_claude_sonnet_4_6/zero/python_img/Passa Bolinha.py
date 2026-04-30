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
    # Row increases going south, col increases going east
    # North: row-1, East: col+1, South: row+1, West: col-1
    dr = [-1, 0, 1, 0]  # North, East, South, West
    dc = [0, 1, 0, -1]
    
    def pass_ball(r, c, from_r, from_c):
        # Raise flag
        flags[r][c] = True
        
        # Current direction: initially facing North (0)
        # Turn 90 degrees clockwise 4 times
        direction = 0  # North
        
        for _ in range(4):
            # Turn 90 degrees clockwise
            direction = (direction + 1) % 4
            
            # Check neighbor in this direction
            nr = r + dr[direction]
            nc = c + dc[direction]
            
            # Check if valid position
            if 0 <= nr < N and 0 <= nc < N:
                neighbor_val = grid[nr][nc]
                my_val = grid[r][c]
                
                if neighbor_val >= my_val and not flags[nr][nc]:
                    # Pass ball to neighbor
                    pass_ball(nr, nc, r, c)
        
        # Return ball to whoever passed it (do nothing special, just return)
    
    # Professor passes ball to (I-1, J-1) (0-indexed)
    start_r = I - 1
    start_c = J - 1
    
    pass_ball(start_r, start_c, -1, -1)
    
    count = sum(flags[r][c] for r in range(N) for c in range(N))
    print(count)

solve()