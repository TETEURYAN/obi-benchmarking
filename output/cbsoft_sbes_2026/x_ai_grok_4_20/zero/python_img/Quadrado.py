
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
grid = []
index = 1
for i in range(N):
    row = [int(data[index + j]) for j in range(N)]
    grid.append(row)
    index += N

row_sums = [sum(row) for row in grid]
col_sums = [sum(grid[i][j] for i in range(N)) for j in range(N)]

total = sum(row_sums)
M = total // (N - 1)

row_diff = [row_sums[i] - M for i in range(N)]
col_diff = [col_sums[j] - M for j in range(N)]

changed_row = -1
for i in range(N):
    if row_diff[i] != 0:
        changed_row = i
        break

changed_col = -1
for j in range(N):
    if col_diff[j] != 0:
        changed_col = j
        break

original = grid[changed_row][changed_col] - row_diff[changed_row]
wrong = grid[changed_row][changed_col]

print(original, wrong)
