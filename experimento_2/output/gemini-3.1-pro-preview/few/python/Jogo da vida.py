import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
q = int(input_data[1])

grid = [[int(c) for c in s] for s in input_data[2:2+n]]

for _ in range(q):
    new_grid = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            alive_neighbors = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        alive_neighbors += grid[nr][nc]
            
            if grid[r][c] == 1:
                if alive_neighbors == 2 or alive_neighbors == 3:
                    new_grid[r][c] = 1
            else:
                if alive_neighbors == 3:
                    new_grid[r][c] = 1
    grid = new_grid

for row in grid:
    print("".join(map(str, row)))