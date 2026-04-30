
import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

L = int(data[0])
C = int(data[1])
index = 2

grid = []
row_sums = []
for i in range(L):
    row = []
    for j in range(C):
        row.append(data[index])
        index += 1
    row_sums.append(int(data[index]))
    index += 1
    grid.append(row)

col_sums = [int(data[index + j]) for j in range(C)]

variables = set()
for row in grid:
    for var in row:
        variables.add(var)
var_list = sorted(list(variables))

var_to_idx = {var: i for i, var in enumerate(var_list)}
N = len(var_list)

row_unknowns = []
for i in range(L):
    cnt = defaultdict(int)
    for var in grid[i]:
        cnt[var] += 1
    row_unknowns.append(cnt)

col_unknowns = []
for j in range(C):
    cnt = defaultdict(int)
    for i in range(L):
        cnt[grid[i][j]] += 1
    col_unknowns.append(cnt)

values = [0] * N
determined = [False] * N

changed = True
while changed:
    changed = False
    for i in range(L):
        unknown_vars = []
        known_sum = 0
        for var, coef in row_unknowns[i].items():
            idx = var_to_idx[var]
            if determined[idx]:
                known_sum += values[idx] * coef
            else:
                unknown_vars.append((var, coef))
        if len(unknown_vars) == 1:
            var, coef = unknown_vars[0]
            idx = var_to_idx[var]
            if not determined[idx]:
                val = (row_sums[i] - known_sum) // coef
                values[idx] = val
                determined[idx] = True
                changed = True
        elif len(unknown_vars) == 0:
            pass

    for j in range(C):
        unknown_vars = []
        known_sum = 0
        for var, coef in col_unknowns[j].items():
            idx = var_to_idx[var]
            if determined[idx]:
                known_sum += values[idx] * coef
            else:
                unknown_vars.append((var, coef))
        if len(unknown_vars) == 1:
            var, coef = unknown_vars[0]
            idx = var_to_idx[var]
            if not determined[idx]:
                val = (col_sums[j] - known_sum) // coef
                values[idx] = val
                determined[idx] = True
                changed = True
        elif len(unknown_vars) == 0:
            pass

for i, var in enumerate(var_list):
    print(var, values[i])
