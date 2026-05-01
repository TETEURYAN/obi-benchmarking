from collections import deque

def solve():
    line1 = input().split()
    N, M = int(line1[0]), int(line1[1])
    
    grid = []
    start = None
    
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(M):
            if row[j] == 3:
                start = (i, j)
    
    # BFS
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = [[False]*M for _ in range(N)]
    visited[start[0]][start[1]] = True
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and grid[nr][nc] != 2:
                    if grid[nr][nc] == 0:
                        print(dist + 1)
                        return
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist+1))

solve()