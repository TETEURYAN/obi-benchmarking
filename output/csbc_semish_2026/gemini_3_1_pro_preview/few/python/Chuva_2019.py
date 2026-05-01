import sys
from collections import deque

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])

grid = [list(row) for row in input_data[2:2+N]]

queue = deque()

for j in range(M):
    if grid[0][j] == 'o':
        queue.append((0, j))
        break

while queue:
    r, c = queue.popleft()
    
    if r + 1 < N:
        if grid[r+1][c] == '.':
            grid[r+1][c] = 'o'
            queue.append((r+1, c))
        elif grid[r+1][c] == '#':
            if c - 1 >= 0 and grid[r][c-1] == '.':
                grid[r][c-1] = 'o'
                queue.append((r, c-1))
            if c + 1 < M and grid[r][c+1] == '.':
                grid[r][c+1] = 'o'
                queue.append((r, c+1))

for row in grid:
    print("".join(row))