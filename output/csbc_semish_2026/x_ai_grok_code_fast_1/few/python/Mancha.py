import sys
from collections import deque

data = sys.stdin.read().splitlines()
N = int(data[0])
grid = [list(line) for line in data[1:]]

# Encontrar S: menor row, depois menor col
min_row = N
min_col = N
for i in range(N):
    for j in range(N):
        if grid[i][j] == '*':
            if i < min_row or (i == min_row and j < min_col):
                min_row = i
                min_col = j

# BFS a partir de S
dist = [[-1] * N for _ in range(N)]
dist[min_row][min_col] = 0
q = deque([(min_row, min_col)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    x, y = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == '*' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# Verificar se é regular
is_regular = True
for i in range(N):
    for j in range(N):
        if grid[i][j] == '*':
            manh = abs(i - min_row) + abs(j - min_col)
            if dist[i][j] != manh:
                is_regular = False
                break
    if not is_regular:
        break

print('S' if is_regular else 'N')