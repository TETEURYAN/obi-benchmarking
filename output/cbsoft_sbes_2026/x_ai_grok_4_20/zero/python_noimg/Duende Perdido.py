
from collections import deque
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
grid = []
index = 2
start = None
for i in range(N):
    row = []
    for j in range(M):
        val = int(data[index])
        row.append(val)
        if val == 3:
            start = (i, j)
        index += 1
    grid.append(row)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque([(start[0], start[1], 0)])
visited = [[False] * M for _ in range(N)]
visited[start[0]][start[1]] = True

while queue:
    x, y, dist = queue.popleft()
    if grid[x][y] == 0:
        print(dist)
        sys.exit(0)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] != 2:
            visited[nx][ny] = True
            queue.append((nx, ny, dist + 1))
