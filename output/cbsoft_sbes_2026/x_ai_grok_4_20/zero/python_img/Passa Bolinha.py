
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
stack = [(I, J, 0)]
visited[I][J] = True
count = 1

while stack:
    x, y, d = stack.pop()
    for _ in range(4):
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] >= grid[x][y]:
            visited[nx][ny] = True
            count += 1
            stack.append((nx, ny, (d + 1) % 4))
            break
        d = (d + 1) % 4

print(count)
