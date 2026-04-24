import sys

data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1

grid = []
for i in range(n):
    row = [int(data[idx+j]) for j in range(n)]
    idx += n
    grid.append(row)

row_sum = [sum(grid[i]) for i in range(n)]
col_sum = [sum(grid[i][j] for i in range(n)) for j in range(n)]

max_weight = 0
for i in range(n):
    for j in range(n):
        weight = row_sum[i] + col_sum[j] - grid[i][j]
        if weight > max_weight:
            max_weight = weight

print(max_weight)