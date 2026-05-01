
import sys
from collections import deque

data = sys.stdin.read().split()
N = int(data[0])
grid = []
index = 1
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

dist = [[float('inf')] * N for _ in range(N)]
dist[0][0] = 0
dq = deque()
dq.append((0, 0))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while dq:
    x, y = dq.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            cost = 1 if grid[nx][ny] == 1 else 0
            if dist[nx][ny] > dist[x][y] + cost:
                dist[nx][ny] = dist[x][y] + cost
                if cost == 0:
                    dq.appendleft((nx, ny))
                else:
                    dq.append((nx, ny))

print(dist[N-1][N-1])
