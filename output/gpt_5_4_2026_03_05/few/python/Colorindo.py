import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

N, M, X, Y, K = data[:5]

blocked = [[False] * M for _ in range(N)]
idx = 5
for _ in range(K):
    A = data[idx] - 1
    B = data[idx + 1] - 1
    blocked[A][B] = True
    idx += 2

sx = X - 1
sy = Y - 1

visited = [[False] * M for _ in range(N)]
q = deque()
q.append((sx, sy))
visited[sx][sy] = True
count = 0

dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]

while q:
    x, y = q.popleft()
    count += 1
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and not blocked[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))

print(count)