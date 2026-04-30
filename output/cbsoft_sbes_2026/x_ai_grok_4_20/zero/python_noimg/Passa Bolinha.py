
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
I = int(data[1]) - 1
J = int(data[2]) - 1

grid = []
index = 3
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[False] * N for _ in range(N)]
stack = [(I, J)]
visited[I][J] = True
count = 1

while stack:
    x, y = stack[-1]
    moved = False
    for _ in range(4):
        dx, dy = directions[0]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] >= grid[x][y]:
            visited[nx][ny] = True
            stack.append((nx, ny))
            count += 1
            moved = True
            directions = directions[1:] + [directions[0]]
            break
        directions = directions[1:] + [directions[0]]
    if not moved:
        stack.pop()
        if stack:
            directions = [directions[-1]] + directions[:-1]

print(count)
