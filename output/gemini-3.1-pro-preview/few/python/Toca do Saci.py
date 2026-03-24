import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    grid = []
    idx = 2
    start_r = -1
    start_c = -1
    
    for r in range(n):
        row = [int(x) for x in input_data[idx:idx+m]]
        grid.append(row)
        idx += m
        if start_r == -1:
            try:
                start_c = row.index(3)
                start_r = r
            except ValueError:
                pass

    queue = deque([(start_r, start_c, 1)])
    grid[start_r][start_c] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m:
                val = grid[nr][nc]
                if val == 2:
                    print(dist + 1)
                    return
                elif val == 1:
                    grid[nr][nc] = 0
                    queue.append((nr, nc, dist + 1))

if __name__ == '__main__':
    solve()