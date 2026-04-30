
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
K = int(data[2])

cameras = []
index = 3
for i in range(K):
    C = int(data[index])
    L = int(data[index + 1])
    D = data[index + 2]
    cameras.append((C, L, D))
    index += 3

# 1-based to 0-based
# rows 0..M-1 (North to South), cols 0..N-1 (West to East)
observed = [[False] * N for _ in range(M)]

for c, l, d in cameras:
    r = l - 1
    col = c - 1
    if d == 'N':
        for i in range(r, -1, -1):
            observed[i][col] = True
    elif d == 'S':
        for i in range(r, M):
            observed[i][col] = True
    elif d == 'L':
        for j in range(col, N):
            observed[r][j] = True
    elif d == 'O':
        for j in range(col, -1, -1):
            observed[r][j] = True

# Start: (0,0), End: (M-1, N-1)
if observed[0][0] or observed[M-1][N-1]:
    print('N')
    sys.exit(0)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N S W E

visited = [[False] * N for _ in range(M)]
queue = deque([(0, 0)])
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    if x == M - 1 and y == N - 1:
        print('S')
        sys.exit(0)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and not observed[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))

print('N')
