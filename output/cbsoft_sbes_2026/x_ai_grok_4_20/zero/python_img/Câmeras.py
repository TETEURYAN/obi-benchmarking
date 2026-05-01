
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
K = int(data[2])

cameras = []
index = 3
for _ in range(K):
    C = int(data[index])
    L = int(data[index + 1])
    D = data[index + 2]
    cameras.append((C, L, D))
    index += 3

observed = [[False] * (M + 2) for _ in range(N + 2)]

for c, l, d in cameras:
    if d == 'N':
        for i in range(l, 0, -1):
            observed[c][i] = True
    elif d == 'S':
        for i in range(l, M + 1):
            observed[c][i] = True
    elif d == 'L':
        for j in range(c, N + 1):
            observed[j][l] = True
    elif d == 'O':
        for j in range(c, 0, -1):
            observed[j][l] = True

if observed[1][1] or observed[N][M]:
    print('N')
    sys.exit()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False] * (M + 2) for _ in range(N + 2)]
queue = deque([(1, 1)])
visited[1][1] = True

while queue:
    x, y = queue.popleft()
    if x == N and y == M:
        print('S')
        sys.exit()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= M and not visited[nx][ny] and not observed[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))

print('N')
