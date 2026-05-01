import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    grid = []
    start = None
    
    for i in range(N):
        row = []
        for j in range(M):
            val = int(input_data[idx]); idx += 1
            row.append(val)
            if val == 2:
                start = (i, j)
        grid.append(row)
    
    # BFS/path following: from start (2), follow cells with value 1, 2, or 3
    # The path is unique (no ambiguity), so we just follow it
    # Count rooms until we reach 3 (inclusive of start and end)
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    visited = [[False]*M for _ in range(N)]
    
    current = start
    visited[current[0]][current[1]] = True
    count = 1  # count current room
    
    while grid[current[0]][current[1]] != 3:
        r, c = current
        moved = False
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if grid[nr][nc] in (1, 2, 3):
                    visited[nr][nc] = True
                    current = (nr, nc)
                    count += 1
                    moved = True
                    break
        if not moved:
            break
    
    print(count)

solve()