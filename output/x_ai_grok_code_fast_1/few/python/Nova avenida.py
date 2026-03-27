import sys

data = sys.stdin.read().split()

N = int(data[0])
M = int(data[1])

grid = []
idx = 2
for i in range(N):
    row = [int(x) for x in data[idx:idx+M]]
    grid.append(row)
    idx += M

min_cost = float('inf')
for j in range(M):
    col_sum = 0
    for i in range(N):
        col_sum += grid[i][j]
    if col_sum < min_cost:
        min_cost = col_sum

print(min_cost)