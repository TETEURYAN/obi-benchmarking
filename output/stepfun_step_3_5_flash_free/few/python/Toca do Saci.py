import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    grid = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(next(it)))
        grid.append(row)
    
    start = None
    end = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                start = (i, j)
            elif grid[i][j] == 3:
                end = (i, j)
    
    visited = [[False] * m for _ in range(n)]
    q = deque()
    si, sj = start
    visited[si][sj] = True
    q.append((si, sj, 1))
    
    while q:
        i, j, d = q.popleft()
        if grid[i][j] == 3:
            print(d)
            return
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                val = grid[ni][nj]
                if val == 1 or val == 3:
                    visited[ni][nj] = True
                    q.append((ni, nj, d + 1))

if __name__ == "__main__":
    main()