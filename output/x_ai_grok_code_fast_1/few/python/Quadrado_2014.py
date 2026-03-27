import sys
from collections import Counter

data = sys.stdin.read().split()
N = int(data[0])
grid = []
idx = 1
for i in range(N):
    row = [int(x) for x in data[idx:idx + N]]
    grid.append(row)
    idx += N

row_sums = [sum(row) for row in grid]
col_sums = [sum(grid[i][j] for i in range(N)) for j in range(N)]

row_counter = Counter(row_sums)
M = [k for k, v in row_counter.items() if v == N - 1][0]

bad_row = [i for i in range(N) if row_sums[i] != M][0]
bad_col = [j for j in range(N) if col_sums[j] != M][0]

current = grid[bad_row][bad_col]
original = current - (row_sums[bad_row] - M)
print(original, current)