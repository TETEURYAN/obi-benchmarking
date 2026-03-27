import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
grid = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)

for i in range(1, N):
    for j in range(1, N):
        cells = [grid[i][j-1], grid[i-1][j-1], grid[i-1][j]]
        white = cells.count(0)
        black = cells.count(1)
        if white > black:
            grid[i][j] = 1
        else:
            grid[i][j] = 0

print(grid[N-1][N-1])