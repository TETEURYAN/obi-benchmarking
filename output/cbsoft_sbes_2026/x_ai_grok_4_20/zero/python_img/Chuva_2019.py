
import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0].split()[0])
M = int(data[0].split()[1])

grid = [list(line) for line in data[1:1+N]]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'o':
            start_i, start_j = i, j
            break

dirs = [(0, -1), (0, 1), (1, 0)]

from collections import deque
q = deque([(start_i, start_j)])
visited = [[False] * M for _ in range(N)]
visited[start_i][start_j] = True
grid[start_i][start_j] = 'o'

while q:
    x, y = q.popleft()
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if grid[nx][ny] == '#':
                continue
            if dx == 0 and dy != 0:
                if nx + 1 < N and grid[nx + 1][ny] == '#':
                    visited[nx][ny] = True
                    grid[nx][ny] = 'o'
                    q.append((nx, ny))
            elif dx == 1 and dy == 0:
                left_block = (y - 1 >= 0 and grid[nx][y - 1] == 'o' and 
                             (nx - 1 >= 0 and grid[nx - 1][y - 1] == '#'))
                right_block = (y + 1 < M and grid[nx][y + 1] == 'o' and 
                              (nx - 1 >= 0 and grid[nx - 1][y + 1] == '#'))
                if left_block or right_block or grid[nx - 1][y] == 'o':
                    visited[nx][ny] = True
                    grid[nx][ny] = 'o'
                    q.append((nx, ny))

for row in grid:
    print(''.join(row))
