from collections import deque
import sys
input = sys.stdin.readline

def main():
    line = input().split()
    N, F = int(line[0]), int(line[1])
    grid = []
    for _ in range(N):
        grid.append(list(input().strip()))
    
    # BFS from (0,0) if grid[0][0] <= F
    if int(grid[0][0]) > F:
        for row in grid:
            print(''.join(row))
        return
    
    visited = [[False]*N for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    grid[0][0] = '*'
    
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if int(grid[nr][nc]) <= F:
                    visited[nr][nc] = True
                    grid[nr][nc] = '*'
                    queue.append((nr, nc))
    
    out = []
    for row in grid:
        out.append(''.join(row))
    print('\n'.join(out))

main()