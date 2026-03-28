import sys
from collections import Counter

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        L = int(next(iterator))
        C = int(next(iterator))
    except StopIteration:
        return

    row_sums = [0] * L
    col_sums = [0] * C
    
    row_counts = [Counter() for _ in range(L)]
    col_counts = [Counter() for _ in range(C)]
    
    var_locations = {}
    
    for r in range(L):
        for c in range(C):
            var_name = next(iterator)
            
            if var_name not in var_locations:
                var_locations[var_name] = []
            var_locations[var_name].append((r, c))
            
            row_counts[r][var_name] += 1
            col_counts[c][var_name] += 1
        
        row_sums[r] = int(next(iterator))
        
    for c in range(C):
        col_sums[c] = int(next(iterator))
        
    row_unknowns = [set(rc.keys()) for rc in row_counts]
    col_unknowns = [set(cc.keys()) for cc in col_counts]
    
    row_known_sum = [0] * L
    col_known_sum = [0] * C
    
    solved_values = {}
    
    queue = []
    
    for r in range(L):
        if len(row_unknowns[r]) == 1:
            queue.append(('row', r))
            
    for c in range(C):
        if len(col_unknowns[c]) == 1:
            queue.append(('col', c))
            
    for item in queue:
        type_, idx = item
        
        if type_ == 'row':
            unknowns = row_unknowns[idx]
            if len(unknowns) != 1:
                continue
            
            var = unknowns.pop()
            cnt = row_counts[idx][var]
            val = (row_sums[idx] - row_known_sum[idx]) // cnt
            
            if var in solved_values:
                continue
            
            solved_values[var] = val
            
            if var in var_locations:
                for (r, c) in var_locations[var]:
                    if var in row_unknowns[r]:
                        row_unknowns[r].remove(var)
                        row_known_sum[r] += val * row_counts[r][var]
                        if len(row_unknowns[r]) == 1:
                            queue.append(('row', r))
                            
                    if var in col_unknowns[c]:
                        col_unknowns[c].remove(var)
                        col_known_sum[c] += val * col_counts[c][var]
                        if len(col_unknowns[c]) == 1:
                            queue.append(('col', c))
                            
        elif type_ == 'col':
            unknowns = col_unknowns[idx]
            if len(unknowns) != 1:
                continue
                
            var = unknowns.pop()
            cnt = col_counts[idx][var]
            val = (col_sums[idx] - col_known_sum[idx]) // cnt
            
            if var in solved_values:
                continue
                
            solved_values[var] = val
            
            if var in var_locations:
                for (r, c) in var_locations[var]:
                    if var in row_unknowns[r]:
                        row_unknowns[r].remove(var)
                        row_known_sum[r] += val * row_counts[r][var]
                        if len(row_unknowns[r]) == 1:
                            queue.append(('row', r))
                            
                    if var in col_unknowns[c]:
                        col_unknowns[c].remove(var)
                        col_known_sum[c] += val * col_counts[c][var]
                        if len(col_unknowns[c]) == 1:
                            queue.append(('col', c))

    sorted_vars = sorted(solved_values.keys())
    
    out_lines = []
    for var in sorted_vars:
        out_lines.append(f"{var} {solved_values[var]}")
        
    sys.stdout.write('\n'.join(out_lines) + '\n')

solve()