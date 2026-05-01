import sys
from collections import deque

def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
                
    token_iter = get_ints()
    
    try:
        N = next(token_iter)
        M = next(token_iter)
    except StopIteration:
        return
        
    grid = []
    start = None
    
    for i in range(N):
        row = []
        for j in range(M):
            val = next(token_iter)
            row.append(val)
            if val == 2:
                start = (i, j)
        grid.append(row)
        
    queue = deque([(start[0], start[1], 1)])
    grid[start[0]][start[1]] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                val = grid[nr][nc]
                if val == 3:
                    print(dist + 1)
                    return
                elif val == 1:
                    grid[nr][nc] = 0
                    queue.append((nr, nc, dist + 1))

if __name__ == '__main__':
    solve()