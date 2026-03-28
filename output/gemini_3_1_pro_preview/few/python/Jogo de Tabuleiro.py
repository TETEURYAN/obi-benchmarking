import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
grid = []
idx = 1
for _ in range(n):
    row = []
    for _ in range(n):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)

for i in range(1, n):
    for j in range(1, n):
        s = grid[i][j-1] + grid[i-1][j-1] + grid[i-1][j]
        if s <= 1:
            grid[i][j] = 1
        else:
            grid[i][j] = 0

print(grid[n-1][n-1])