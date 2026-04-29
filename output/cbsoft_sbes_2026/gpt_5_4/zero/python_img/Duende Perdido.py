from collections import deque
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    grid = []
    start = None
    for i in range(n):
        row = []
        for j in range(m):
            v = int(next(it))
            row.append(v)
            if v == 3:
                start = (i, j)
        grid.append(row)
    
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    si, sj = start
    q.append((si, sj))
    dist[si][sj] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        i, j = q.popleft()
        
        if grid[i][j] == 0:
            print(dist[i][j])
            return
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != 2 and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))

if __name__ == "__main__":
    main()