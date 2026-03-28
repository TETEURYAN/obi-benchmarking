import sys

grid = sys.stdin.read().split()

count = 0
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(7):
    for j in range(7):
        if grid[i][j] != 'o':
            continue
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            ti, tj = i + 2 * di, j + 2 * dj
            if 0 <= ni < 7 and 0 <= nj < 7 and 0 <= ti < 7 and 0 <= tj < 7:
                if grid[ni][nj] == 'o' and grid[ti][tj] == '.':
                    count += 1

print(count)