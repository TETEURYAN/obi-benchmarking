import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
grid = []
idx = 1
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)

r, c = -1, -1
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            r = i
            c = j
            break
    if r != -1:
        break

if r == 0:
    target_sum = sum(grid[1])
else:
    target_sum = sum(grid[0])

current_sum = sum(grid[r])
missing_value = target_sum - current_sum

print(missing_value)
print(r + 1)
print(c + 1)