import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    grid = []
    for i in range(n):
        row = [int(data[idx + j]) for j in range(m)]
        idx += m
        grid.append(row)
    
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
    
    print(count)

main()