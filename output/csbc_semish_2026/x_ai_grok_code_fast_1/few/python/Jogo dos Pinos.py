import sys

input_data = sys.stdin.read().splitlines()
grid = [list(line) for line in input_data]

count = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(7):
    for j in range(7):
        if grid[i][j] == 'o':
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < 7 and 0 <= nj < 7 and grid[ni][nj] == 'o':
                    nni, nnj = ni + di, nj + dj
                    if 0 <= nni < 7 and 0 <= nnj < 7 and grid[nni][nnj] == '.':
                        count += 1

print(count)