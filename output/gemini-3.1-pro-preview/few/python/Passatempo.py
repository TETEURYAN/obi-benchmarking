import sys
from collections import deque

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

L = int(input_data[0])
C = int(input_data[1])

grid = []
row_sums = []

idx = 2
for _ in range(L):
    row = input_data[idx : idx+C]
    grid.append(row)
    row_sums.append(int(input_data[idx+C]))
    idx += C + 1
    
col_sums = []
for _ in range(C):
    col_sums.append(int(input_data[idx]))
    idx += 1
    
row_unknowns = [{} for _ in range(L)]
col_unknowns = [{} for _ in range(C)]
row_known_sum = [0] * L
col_known_sum = [0] * C

var_rows = {}
var_cols = {}

for r in range(L):
    for c in range(C):
        var = grid[r][c]
        row_unknowns[r][var] = row_unknowns[r].get(var, 0) + 1
        col_unknowns[c][var] = col_unknowns[c].get(var, 0) + 1
        
        if var not in var_rows:
            var_rows[var] = set()
            var_cols[var] = set()
        var_rows[var].add(r)
        var_cols[var].add(c)
        
queue = deque()
for r in range(L):
    if len(row_unknowns[r]) == 1:
        queue.append(('r', r))
for c in range(C):
    if len(col_unknowns[c]) == 1:
        queue.append(('c', c))
        
known_vars = {}

while queue:
    type_, q_idx = queue.popleft()
    
    if type_ == 'r':
        if len(row_unknowns[q_idx]) == 1:
            var, count = list(row_unknowns[q_idx].items())[0]
            if var not in known_vars:
                val = (row_sums[q_idx] - row_known_sum[q_idx]) // count
                known_vars[var] = val
                
                for r in var_rows[var]:
                    if var in row_unknowns[r]:
                        c_count = row_unknowns[r].pop(var)
                        row_known_sum[r] += val * c_count
                        if len(row_unknowns[r]) == 1:
                            queue.append(('r', r))
                            
                for c in var_cols[var]:
                    if var in col_unknowns[c]:
                        c_count = col_unknowns[c].pop(var)
                        col_known_sum[c] += val * c_count
                        if len(col_unknowns[c]) == 1:
                            queue.append(('c', c))
    else:
        if len(col_unknowns[q_idx]) == 1:
            var, count = list(col_unknowns[q_idx].items())[0]
            if var not in known_vars:
                val = (col_sums[q_idx] - col_known_sum[q_idx]) // count
                known_vars[var] = val
                
                for r in var_rows[var]:
                    if var in row_unknowns[r]:
                        c_count = row_unknowns[r].pop(var)
                        row_known_sum[r] += val * c_count
                        if len(row_unknowns[r]) == 1:
                            queue.append(('r', r))
                            
                for c in var_cols[var]:
                    if var in col_unknowns[c]:
                        c_count = col_unknowns[c].pop(var)
                        col_known_sum[c] += val * c_count
                        if len(col_unknowns[c]) == 1:
                            queue.append(('c', c))
                            
for var in sorted(known_vars.keys()):
    print(f"{var} {known_vars[var]}")