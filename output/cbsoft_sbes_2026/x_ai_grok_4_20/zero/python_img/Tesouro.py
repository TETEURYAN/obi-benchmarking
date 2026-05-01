
import sys

input = sys.stdin.read
data = input().splitlines()

M = int(data[0])
grid = data[1:1+M]
A, B = map(int, data[1+M].split())
A -= 1
B -= 1

directions = {'N': (-1, 0), 'S': (1, 0), 'L': (0, 1), 'O': (0, -1)}

tx, ty = -1, -1
for i in range(M):
    for j in range(M):
        if grid[i][j] == 'X':
            tx, ty = i, j
            break
    if tx != -1:
        break

visited = [[False] * M for _ in range(M)]
path = []
x, y = A, B
time = 0
cycle = False
out = False

while True:
    if x < 0 or x >= M or y < 0 or y >= M:
        out = True
        break
    if visited[x][y]:
        cycle = True
        break
    if grid[x][y] == 'X':
        break
    visited[x][y] = True
    path.append((x, y))
    dx, dy = directions[grid[x][y]]
    x += dx
    y += dy
    time += 1

if grid[x][y] == 'X' if 0 <= x < M and 0 <= y < M else False:
    print(time)
elif cycle:
    print(0)
else:
    print(-1)
