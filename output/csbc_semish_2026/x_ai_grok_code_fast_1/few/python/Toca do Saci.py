import sys

data = sys.stdin.read().split()

idx = 0

N = int(data[idx])

idx += 1

M = int(data[idx])

idx += 1

grid = []

for i in range(N):

    row = []

    for j in range(M):

        row.append(int(data[idx]))

        idx += 1

    grid.append(row)

# find pos2 and pos3

pos2 = None

pos3 = None

for i in range(N):

    for j in range(M):

        if grid[i][j] == 2:

            pos2 = (i, j)

        elif grid[i][j] == 3:

            pos3 = (i, j)

# now BFS

from collections import deque

dist = [[-1] * M for _ in range(N)]

dist[pos2[0]][pos2[1]] = 0

q = deque([pos2])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:

    x, y = q.popleft()

    for dx, dy in directions:

        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1 and grid[nx][ny] in [1, 2, 3]:

            dist[nx][ny] = dist[x][y] + 1

            q.append((nx, ny))

# now, the number of rooms is dist[pos3[0]][pos3[1]] + 1

print(dist[pos3[0]][pos3[1]] + 1)