
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])

grid = []
index = 2
for i in range(N):
    row = [int(c) for c in data[index]]
    grid.append(row)
    index += 1

directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

for q in range(Q):
    new_grid = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            live_neighbors = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    live_neighbors += grid[ni][nj]
            if grid[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_grid[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = 1
    grid = new_grid

for i in range(N):
    print(''.join(map(str, grid[i])))
