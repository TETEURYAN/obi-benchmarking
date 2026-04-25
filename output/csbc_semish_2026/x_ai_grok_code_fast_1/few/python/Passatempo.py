import sys

input_data = sys.stdin.read().split()
idx = 0
L = int(input_data[idx]); idx += 1
C = int(input_data[idx]); idx += 1
grid = []
row_sums = []
for i in range(L):
    row = []
    for j in range(C):
        row.append(input_data[idx]); idx += 1
    row_sums.append(int(input_data[idx])); idx += 1
    grid.append(row)
col_sums = []
for j in range(C):
    col_sums.append(int(input_data[idx])); idx += 1

var_set = set()
for row in grid:
    for var in row:
        var_set.add(var)
var_list = sorted(list(var_set))

known = {}
while len(known) < len(var_set):
    progress = False
    # Check rows
    for i in range(L):
        current_sum = sum(known.get(var, 0) for var in grid[i])
        unknown_vars = [var for var in grid[i] if var not in known]
        if len(unknown_vars) == 1:
            var = unknown_vars[0]
            value = row_sums[i] - current_sum
            known[var] = value
            progress = True
    # Check columns
    for j in range(C):
        col_vars = [grid[i][j] for i in range(L)]
        current_sum = sum(known.get(var, 0) for var in col_vars)
        unknown_vars = [var for var in col_vars if var not in known]
        if len(unknown_vars) == 1:
            var = unknown_vars[0]
            value = col_sums[j] - current_sum
            known[var] = value
            progress = True
    if not progress:
        break

for var in var_list:
    print(var, known[var])