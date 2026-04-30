import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    C = int(input_data[1])
    
    grid = []
    row_sums = []
    idx = 2
    for i in range(L):
        row = []
        for j in range(C):
            row.append(input_data[idx])
            idx += 1
        grid.append(row)
        row_sums.append(int(input_data[idx]))
        idx += 1
        
    col_sums = []
    for j in range(C):
        col_sums.append(int(input_data[idx]))
        idx += 1
        
    row_unknowns = [defaultdict(int) for _ in range(L)]
    col_unknowns = [defaultdict(int) for _ in range(C)]
    row_known_sum = [0] * L
    col_known_sum = [0] * C
    
    var_rows = defaultdict(set)
    var_cols = defaultdict(set)
    
    for i in range(L):
        for j in range(C):
            var = grid[i][j]
            row_unknowns[i][var] += 1
            col_unknowns[j][var] += 1
            var_rows[var].add(i)
            var_cols[var].add(j)
            
    ready = []
    for i in range(L):
        if len(row_unknowns[i]) == 1:
            ready.append(('row', i))
    for j in range(C):
        if len(col_unknowns[j]) == 1:
            ready.append(('col', j))
            
    known = {}
    
    while ready:
        type_, index = ready.pop()
        if type_ == 'row':
            if len(row_unknowns[index]) != 1:
                continue
            var, count = list(row_unknowns[index].items())[0]
            if var in known:
                continue
            val = (row_sums[index] - row_known_sum[index]) // count
            known[var] = val
        else:
            if len(col_unknowns[index]) != 1:
                continue
            var, count = list(col_unknowns[index].items())[0]
            if var in known:
                continue
            val = (col_sums[index] - col_known_sum[index]) // count
            known[var] = val
            
        for r in var_rows[var]:
            if var in row_unknowns[r]:
                count = row_unknowns[r].pop(var)
                row_known_sum[r] += count * val
                if len(row_unknowns[r]) == 1:
                    ready.append(('row', r))
                    
        for c in var_cols[var]:
            if var in col_unknowns[c]:
                count = col_unknowns[c].pop(var)
                col_known_sum[c] += count * val
                if len(col_unknowns[c]) == 1:
                    ready.append(('col', c))
                    
    for var in sorted(known.keys()):
        print(f"{var} {known[var]}")

if __name__ == '__main__':
    solve()