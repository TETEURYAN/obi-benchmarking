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

# Find position of zero
zr, zc = -1, -1
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            zr, zc = i, j

# The magic sum can be determined from a complete row/column
# Find magic sum from a row that doesn't contain zero
magic_sum = None
for i in range(n):
    if i != zr:
        magic_sum = sum(grid[i])
        break

# The missing value is magic_sum - sum of the row containing zero
missing = magic_sum - sum(grid[zr])

print(missing)
print(zr + 1)
print(zc + 1)