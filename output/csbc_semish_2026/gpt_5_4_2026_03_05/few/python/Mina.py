import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
grid = []
idx = 1
for _ in range(n):
    grid.append(data[idx:idx + n])
    idx += n

INF = 10**9
dist = [[INF] * n for _ in range(n)]
dist[0][0] = 0
dq = deque()
dq.append((0, 0))

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

while dq:
    x, y = dq.popleft()
    d = dist[x][y]
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            w = grid[nx][ny]
            nd = d + w
            if nd < dist[nx][ny]:
                dist[nx][ny] = nd
                if w == 0:
                    dq.appendleft((nx, ny))
                else:
                    dq.append((nx, ny))

print(dist[n - 1][n - 1])