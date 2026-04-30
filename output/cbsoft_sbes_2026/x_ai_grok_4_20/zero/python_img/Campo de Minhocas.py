
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

grid = []
index = 2
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

max_row = 0
for i in range(N):
    row_sum = sum(grid[i])
    if row_sum > max_row:
        max_row = row_sum

max_col = 0
for j in range(M):
    col_sum = 0
    for i in range(N):
        col_sum += grid[i][j]
    if col_sum > max_col:
        max_col = col_sum

print(max(max_row, max_col))
