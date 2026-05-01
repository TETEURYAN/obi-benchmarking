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
    
    # BFS from start
    # 0 = exit (goal), 1 = normal room, 2 = crystal (blocked), 3 = start
    dist = [[-1]*M for _ in range(N)]
    dist[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] != 2 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    if grid[nr][nc] == 0:
                        print(dist[nr][nc])
                        return
                    q.append((nr, nc))

solve()