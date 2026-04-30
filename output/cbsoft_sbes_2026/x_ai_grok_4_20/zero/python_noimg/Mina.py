
from collections import deque
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
grid = []
index = 1
for i in range(N):
    row = [int(data[index + j]) for j in range(N)]
    grid.append(row)
    index += N

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

dist = [[float('inf')] * N for _ in range(N)]
dist[0][0] = grid[0][0]

queue = deque([(0, 0, grid[0][0])])

while queue:
    x, y, cost = queue.popleft()
    if cost > dist[x][y]:
        continue
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            new_cost = cost + grid[nx][ny]
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                if grid[nx][ny] == 0:
                    queue.appendleft((nx, ny, new_cost))
                else:
                    queue.append((nx, ny, new_cost))

print(dist[N-1][N-1])
