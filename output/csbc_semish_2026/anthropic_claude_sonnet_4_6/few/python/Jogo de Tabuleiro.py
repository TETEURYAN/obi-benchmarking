import sys

data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1

grid = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(data[idx])); idx += 1
    grid.append(row)

for i in range(1, n):
    for j in range(1, n):
        cells = [grid[i][j-1], grid[i-1][j-1], grid[i-1][j]]
        whites = cells.count(0)
        blacks = cells.count(1)
        if whites > blacks:
            grid[i][j] = 1
        else:
            grid[i][j] = 0

print(grid[n-1][n-1])