
import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
grid = data[1:1+N]

stars = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == '*':
            stars.append((i, j))

if not stars:
    print("S")
    sys.exit(0)

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N and grid[x][y] == '*'

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start):
    dist = [[-1] * N for _ in range(N)]
    dist[start[0]][start[1]] = 0
    q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

def manh(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

root = stars[0]
dist_from_root = bfs(root)

for p in stars:
    if dist_from_root[p[0]][p[1]] == -1:
        print("N")
        sys.exit(0)

for i, p in enumerate(stars):
    for j in range(i + 1, len(stars)):
        q = stars[j]
        d_m = manh(p, q)
        if dist_from_root[p[0]][p[1]] + dist_from_root[q[0]][q[1]] - 2 * dist_from_root[root[0]][root[1]] != d_m:
            if abs(dist_from_root[p[0]][p[1]] - dist_from_root[q[0]][q[1]]) > d_m:
                print("N")
                sys.exit(0)

print("S")
