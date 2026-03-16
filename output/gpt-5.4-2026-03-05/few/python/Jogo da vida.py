import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
q = int(data[1])
grid = [list(map(int, data[i + 2].strip())) for i in range(n)]

dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]

for _ in range(q):
    new_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            alive_neighbors = 0
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    alive_neighbors += grid[ni][nj]
            if grid[i][j] == 1:
                if alive_neighbors == 2 or alive_neighbors == 3:
                    new_grid[i][j] = 1
            else:
                if alive_neighbors == 3:
                    new_grid[i][j] = 1
    grid = new_grid

out = [''.join(map(str, row)) for row in grid]
sys.stdout.write('\n'.join(out))