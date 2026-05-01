n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# Find position of zero
zero_row, zero_col = -1, -1
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            zero_row, zero_col = i, j

# Determine magic sum from a complete row or column
magic_sum = None

# Try to find magic sum from rows that don't contain zero
for i in range(n):
    if i != zero_row:
        magic_sum = sum(grid[i])
        break

if magic_sum is None:
    # All rows contain zero? Not possible since only one zero
    # Try columns
    for j in range(n):
        if j != zero_col:
            magic_sum = sum(grid[i][j] for i in range(n))
            break

# The missing value is magic_sum - sum of the row containing zero
row_sum = sum(grid[zero_row])
missing_value = magic_sum - row_sum

print(missing_value)
print(zero_row + 1)
print(zero_col + 1)