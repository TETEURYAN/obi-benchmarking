
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
F = int(data[1])
grid = []
index = 2
for i in range(N):
    row = data[index]
    grid.append(list(row))
    index += 1

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False] * N for _ in range(N)]
queue = deque()

if int(grid[0][0]) <= F:
    queue.append((0, 0))
    visited[0][0] = True
    grid[0][0] = '*'

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if int(grid[nx][ny]) <= F:
                visited[nx][ny] = True
                grid[nx][ny] = '*'
                queue.append((nx, ny))

for row in grid:
    print(''.join(row))
