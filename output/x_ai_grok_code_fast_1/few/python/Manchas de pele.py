import sys
from collections import deque

input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])
grid = []
idx = 2
for i in range(n):
    row = [int(x) for x in input_data[idx:idx+m]]
    grid.append(row)
    idx += m

visited = [[False] * m for _ in range(n)]
count = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            count += 1
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

print(count)