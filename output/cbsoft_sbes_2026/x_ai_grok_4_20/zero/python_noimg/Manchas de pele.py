
import sys
sys.setrecursionlimit(10**6)

def dfs(i, j, grid, visited, N, M):
    stack = [(i, j)]
    visited[i][j] = True
    while stack:
        x, y = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j, grid, visited, N, M)
            count += 1

print(count)
