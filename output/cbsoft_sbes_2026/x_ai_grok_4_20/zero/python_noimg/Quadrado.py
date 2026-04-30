
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
col_sums = [0] * N
for j in range(N):
    for i in range(N):
        col_sums[j] += grid[i][j]

total = sum(row_sums)
M = total // (2 * N - 2)

row_count = {}
for i, s in enumerate(row_sums):
    row_count[s] = row_count.get(s, 0) + 1

col_count = {}
for j, s in enumerate(col_sums):
    col_count[s] = col_count.get(s, 0) + 1

bad_row = -1
bad_col = -1
for i in range(N):
    if row_sums[i] != M:
        bad_row = i
        break
for j in range(N):
    if col_sums[j] != M:
        bad_col = j
        break

if bad_row == -1 or bad_col == -1:
    for i in range(N):
        if row_count[row_sums[i]] == 1:
            bad_row = i
            break
    for j in range(N):
        if col_count[col_sums[j]] == 1:
            bad_col = j
            break

original = M - (row_sums[bad_row] - grid[bad_row][bad_col])
altered = grid[bad_row][bad_col]

print(original, altered)
