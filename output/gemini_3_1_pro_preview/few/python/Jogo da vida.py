import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
Q = int(input_data[1])

grid = [[int(c) for c in row] for row in input_data[2:2+N]]

for _ in range(Q):
    new_grid = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            live_neighbors = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        live_neighbors += grid[nr][nc]
            
            if grid[r][c] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_grid[r][c] = 1
            else:
                if live_neighbors == 3:
                    new_grid[r][c] = 1
    grid = new_grid

for row in grid:
    print("".join(map(str, row)))