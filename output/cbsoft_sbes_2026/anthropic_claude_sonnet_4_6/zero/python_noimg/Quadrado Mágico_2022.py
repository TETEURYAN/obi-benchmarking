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

# Determine the magic sum using a complete row or column
# Find a row without zero to get magic sum
magic_sum = None
for i in range(n):
    if i != zero_row:
        magic_sum = sum(grid[i])
        break

# Calculate the missing value from the row containing zero
row_sum = sum(grid[zero_row])
missing_value = magic_sum - row_sum

print(missing_value)
print(zero_row + 1)
print(zero_col + 1)