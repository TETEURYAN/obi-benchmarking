from collections import defaultdict

def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    
    L = int(input_data[idx]); idx += 1
    C = int(input_data[idx]); idx += 1
    
    # rows[i] = (list of var names, sum)
    rows = []
    for i in range(L):
        vars_in_row = []
        for j in range(C):
            vars_in_row.append(input_data[idx]); idx += 1
        s = int(input_data[idx]); idx += 1
        rows.append((vars_in_row, s))
    
    # columns
    cols = []
    for j in range(C):
        s = int(input_data[idx]); idx += 1
        cols.append(s)
    
    # Build column constraints: cols[j] = sum of rows[i][0][j] for i in range(L)
    col_constraints = []
    for j in range(C):
        vars_in_col = [rows[i][0][j] for i in range(L)]
        col_constraints.append((vars_in_col, cols[j]))
    
    # All constraints = rows + col_constraints
    all_constraints = rows + col_constraints
    
    # known values
    known = {}
    
    # We need to iteratively solve
    # For each constraint, track remaining sum and unknown vars
    
    # Build constraint info
    # constraint_sum[k] = remaining sum
    # constraint_vars[k] = list of vars (with duplicates)
    
    n_constraints = len(all_constraints)
    constraint_sum = []
    constraint_vars = []
    
    for (vars_list, s) in all_constraints:
        constraint_sum.append(s)
        constraint_vars.append(list(vars_list))
    
    # For each variable, which constraints contain it
    var_to_constraints = defaultdict(set)
    for k, vars_list in enumerate(constraint_vars):
        for v in vars_list:
            var_to_constraints[v].add(k)
    
    # Process iteratively
    changed = True
    while changed:
        changed = False
        for k in range(n_constraints):
            # Find unknown vars in this constraint
            unknown_vars = set()
            for v in constraint_vars[k]:
                if v not in known:
                    unknown_vars.add(v)
            
            if len(unknown_vars) == 1:
                # Can solve for the one unknown
                target_var = next(iter(unknown_vars))
                # remaining sum = constraint_sum[k] - sum of known vars
                remaining = constraint_sum[k]
                for v in constraint_vars[k]:
                    if v in known:
                        remaining -= known[v]
                # Count occurrences of target_var
                count = constraint_vars[k].count(target_var)
                value = remaining // count
                if target_var not in known:
                    known[target_var] = value
                    changed = True
    
    # Collect all variables
    all_vars = set()
    for vars_list, s in all_constraints:
        for v in vars_list:
            all_vars.add(v)
    
    # Sort alphabetically
    sorted_vars = sorted(all_vars)
    
    for v in sorted_vars:
        print(v, known[v])

solve()