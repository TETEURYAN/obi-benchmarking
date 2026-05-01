from collections import defaultdict

def solve():
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
        s = int(input_data[idx]); idx += 1
        grid.append(row)
        row_sums.append(s)
    
    col_sums = []
    for j in range(C):
        col_sums.append(int(input_data[idx])); idx += 1
    
    # Known values of variables
    known = {}
    
    # We need to iteratively find rows/cols with only one unknown variable
    # Build constraints: each row and each column is a constraint
    # constraint: list of var names, sum value
    
    # Use a queue-based approach
    from collections import deque
    
    # constraints: list of (vars_list, sum_value, type, index)
    # We'll track for each constraint: remaining unknown vars and remaining sum
    
    # For each constraint, store the variables and current sum
    constraints = []
    
    # rows
    for i in range(L):
        constraints.append({'vars': list(grid[i]), 'sum': row_sums[i]})
    
    # cols
    for j in range(C):
        col_vars = [grid[i][j] for i in range(L)]
        constraints.append({'vars': col_vars, 'sum': col_sums[j]})
    
    # For each constraint, compute unknowns and remaining sum
    def get_unknowns_and_remaining(c):
        unknowns = []
        remaining = c['sum']
        for v in c['vars']:
            if v in known:
                remaining -= known[v]
            else:
                unknowns.append(v)
        return unknowns, remaining
    
    # Keep iterating until all variables are known
    changed = True
    while changed:
        changed = False
        for c in constraints:
            unknowns, remaining = get_unknowns_and_remaining(c)
            # unique unknowns
            unique_unknowns = list(set(unknowns))
            if len(unique_unknowns) == 1:
                var = unique_unknowns[0]
                if var not in known:
                    # count occurrences
                    count = unknowns.count(var)
                    # count * val = remaining
                    val = remaining // count
                    known[var] = val
                    changed = True
    
    # Output in alphabetical order
    sorted_vars = sorted(known.keys())
    for v in sorted_vars:
        print(v, known[v])

solve()