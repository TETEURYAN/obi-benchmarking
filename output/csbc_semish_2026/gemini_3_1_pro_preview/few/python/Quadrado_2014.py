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

row_sums = [sum(row) for row in grid]
col_sums = [sum(grid[i][j] for i in range(n)) for j in range(n)]

M = sorted(row_sums)[n // 2]

wrong_r = -1
for i in range(n):
    if row_sums[i] != M:
        wrong_r = i
        break

wrong_c = -1
for j in range(n):
    if col_sums[j] != M:
        wrong_c = j
        break

altered = grid[wrong_r][wrong_c]
original = altered + (M - row_sums[wrong_r])

print(f"{original} {altered}")