
from collections import deque
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
grid = []
index = 2
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

# Find starting position
start = None
for i in range(N):
    for j in range(M):
        if grid[i][j] == 3:
            start = (i, j)
            break
    if start:
        break

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS
queue = deque([(start[0], start[1], 0)])  # i, j, dist
visited = [[False] * M for _ in range(N)]
visited[start[0]][start[1]] = True

while queue:
    x, y, dist = queue.popleft()
    
    # If this is an exit (0), we found the answer
    if grid[x][y] == 0:
        print(dist)
        sys.exit(0)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if grid[nx][ny] != 2:  # Not a crystal wall
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

# Should not reach here as per problem guarantee
print(0)
