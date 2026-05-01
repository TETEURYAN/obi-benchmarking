
import sys

input = sys.stdin.read
data = input().split()

M = int(data[0])
grid = []
index = 1
for i in range(M):
    row = data[index]
    grid.append(list(row))
    index += 1

A = int(data[index]) - 1
B = int(data[index + 1]) - 1

# Find treasure
tx, ty = -1, -1
for i in range(M):
    for j in range(M):
        if grid[i][j] == 'X':
            tx, ty = i, j
            break
    if tx != -1:
        break

directions = {'N': (-1, 0), 'S': (1, 0), 'L': (0, 1), 'O': (0, -1)}

visited = [[False] * M for _ in range(M)]
path = []
x, y = A, B
time = 0
cycle = False
sea = False

while True:
    if x < 0 or x >= M or y < 0 or y >= M:
        sea = True
        break
    if visited[x][y]:
        cycle = True
        break
    if x == tx and y == ty:
        break
    visited[x][y] = True
    path.append((x, y))
    dx, dy = directions[grid[x][y]]
    x += dx
    y += dy
    time += 1

if x == tx and y == ty:
    print(time)
elif cycle:
    print(0)
else:
    print(-1)
