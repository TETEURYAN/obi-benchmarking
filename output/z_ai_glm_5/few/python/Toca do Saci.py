
import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    grid = []
    start = None
    
    for i in range(n):
        row = []
        for j in range(m):
            val = int(data[idx]); idx += 1
            row.append(val)
            if val == 2:
                start = (i, j)
        grid.append(row)
    
    queue = deque([(start[0], start[1], 1)])
    visited = {start}
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c, d = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                val = grid[nr][nc]
                if val == 3:
                    print(d + 1)
                    return
                elif val == 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d + 1))

solve()
