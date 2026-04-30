
import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

L = int(data[0])
C = int(data[1])
index = 2

grid = []
row_sums = []
vars_in_row = []

for i in range(L):
    row_vars = []
    for j in range(C):
        var = data[index]
        row_vars.append(var)
        index += 1
    row_sums.append(int(data[index]))
    index += 1
    vars_in_row.append(row_vars)

col_sums = []
for j in range(C):
    col_sums.append(int(data[index]))
    index += 1

all_vars = set()
for row in vars_in_row:
    for v in row:
        all_vars.add(v)

var_list = sorted(all_vars)
N = len(var_list)
var_to_idx = {v: i for i, v in enumerate(var_list)}

row_unknown_count = [C for _ in range(L)]
col_unknown_count = [L for _ in range(C)]

values = [0] * N
determined = [False] * N

row_var_count = [[0] * N for _ in range(L)]
col_var_count = [[0] * N for _ in range(C)]

for i in range(L):
    for v in vars_in_row[i]:
        idx = var_to_idx[v]
        row_var_count[i][idx] += 1

for j in range(C):
    for i in range(L):
        v = vars_in_row[i][j]
        idx = var_to_idx[v]
        col_var_count[j][idx] += 1

changed = True
while changed:
    changed = False
    for i in range(L):
        if row_unknown_count[i] == 0:
            continue
        unknown_idx = -1
        known_sum = 0
        for k in range(N):
            if row_var_count[i][k] == 0:
                continue
            if determined[k]:
                known_sum += values[k] * row_var_count[i][k]
            else:
                if unknown_idx != -1:
                    unknown_idx = -2
                else:
                    unknown_idx = k
        if unknown_idx >= 0:
            remaining = row_sums[i] - known_sum
            values[unknown_idx] = remaining // row_var_count[i][unknown_idx]
            determined[unknown_idx] = True
            changed = True
            for r in range(L):
                if not determined[unknown_idx] or row_var_count[r][unknown_idx] == 0:
                    continue
                row_unknown_count[r] -= 1
            for c in range(C):
                if col_var_count[c][unknown_idx] > 0:
                    col_unknown_count[c] -= 1
        elif unknown_idx == -1 and known_sum != row_sums[i]:
            pass

    for j in range(C):
        if col_unknown_count[j] == 0:
            continue
        unknown_idx = -1
        known_sum = 0
        for k in range(N):
            if col_var_count[j][k] == 0:
                continue
            if determined[k]:
                known_sum += values[k] * col_var_count[j][k]
            else:
                if unknown_idx != -1:
                    unknown_idx = -2
                else:
                    unknown_idx = k
        if unknown_idx >= 0:
            remaining = col_sums[j] - known_sum
            values[unknown_idx] = remaining // col_var_count[j][unknown_idx]
            determined[unknown_idx] = True
            changed = True
            for r in range(L):
                if row_var_count[r][unknown_idx] > 0:
                    row_unknown_count[r] -= 1
            for c in range(C):
                if not determined[unknown_idx] or col_var_count[c][unknown_idx] == 0:
                    continue
                col_unknown_count[c] -= 1
        elif unknown_idx == -1 and known_sum != col_sums[j]:
            pass

for i, v in enumerate(var_list):
    print(v, values[i])
