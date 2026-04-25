import sys

data = sys.stdin.read().split()
N = int(data[0])
Q = int(data[1])
grid = []
idx = 2
for i in range(N):
    row = data[idx]
    grid.append([int(c) for c in row])
    idx += 1

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(Q):
    new_grid = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            count = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 1:
                    count += 1
            if grid[i][j] == 0:
                if count == 3:
                    new_grid[i][j] = 1
            else:
                if count == 2 or count == 3:
                    new_grid[i][j] = 1
    grid = new_grid

for row in grid:
    print(''.join(map(str, row)))