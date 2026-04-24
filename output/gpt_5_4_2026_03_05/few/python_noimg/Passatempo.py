import sys
from collections import defaultdict, deque

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
L = int(next(it))
C = int(next(it))

row_sum = [0] * L
col_sum = [0] * C
row_vars = [defaultdict(int) for _ in range(L)]
col_vars = [defaultdict(int) for _ in range(C)]
var_rows = defaultdict(list)
var_cols = defaultdict(list)
all_vars = set()

for i in range(L):
    for j in range(C):
        v = next(it)
        row_vars[i][v] += 1
        col_vars[j][v] += 1
        var_rows[v].append(i)
        var_cols[v].append(j)
        all_vars.add(v)
    row_sum[i] = int(next(it))

for j in range(C):
    col_sum[j] = int(next(it))

unknown_row = [len(row_vars[i]) for i in range(L)]
unknown_col = [len(col_vars[j]) for j in range(C)]

q = deque()
for i in range(L):
    if unknown_row[i] == 1:
        q.append((0, i))
for j in range(C):
    if unknown_col[j] == 1:
        q.append((1, j))

value = {}

while q:
    typ, idx = q.popleft()
    if typ == 0:
        if unknown_row[idx] != 1:
            continue
        for v, cnt in row_vars[idx].items():
            if v not in value:
                value[v] = row_sum[idx] // cnt
                break
        else:
            continue
        x = value[v]
        for r in var_rows[v]:
            if v in row_vars[r]:
                c = row_vars[r].pop(v)
                row_sum[r] -= c * x
                unknown_row[r] -= 1
                if unknown_row[r] == 1:
                    q.append((0, r))
        for cidx in var_cols[v]:
            if v in col_vars[cidx]:
                c = col_vars[cidx].pop(v)
                col_sum[cidx] -= c * x
                unknown_col[cidx] -= 1
                if unknown_col[cidx] == 1:
                    q.append((1, cidx))
    else:
        if unknown_col[idx] != 1:
            continue
        for v, cnt in col_vars[idx].items():
            if v not in value:
                value[v] = col_sum[idx] // cnt
                break
        else:
            continue
        x = value[v]
        for r in var_rows[v]:
            if v in row_vars[r]:
                c = row_vars[r].pop(v)
                row_sum[r] -= c * x
                unknown_row[r] -= 1
                if unknown_row[r] == 1:
                    q.append((0, r))
        for cidx in var_cols[v]:
            if v in col_vars[cidx]:
                c = col_vars[cidx].pop(v)
                col_sum[cidx] -= c * x
                unknown_col[cidx] -= 1
                if unknown_col[cidx] == 1:
                    q.append((1, cidx))

out = []
for a in range(26):
    for b in range(26):
        name = chr(97 + a) + chr(97 + b)
        if name in all_vars:
            out.append(f"{name} {value[name]}")
sys.stdout.write("\n".join(out))