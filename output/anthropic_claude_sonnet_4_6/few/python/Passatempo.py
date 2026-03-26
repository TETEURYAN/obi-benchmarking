import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    
    # rows[i] = (list of var names, sum)
    rows = []
    for i in range(L):
        vars_in_row = []
        for j in range(C):
            vars_in_row.append(data[idx]); idx += 1
        s = int(data[idx]); idx += 1
        rows.append((vars_in_row, s))
    
    # cols[j] = (list of var names, sum)
    col_sums = []
    for j in range(C):
        col_sums.append(int(data[idx])); idx += 1
    
    cols = []
    for j in range(C):
        vars_in_col = [rows[i][0][j] for i in range(L)]
        cols.append((vars_in_col, col_sums[j]))
    
    # known values
    known = {}
    
    # For each row/col, track remaining sum and unknown vars
    # We'll use a queue-based approach
    
    # Build constraints: list of [set of unknown vars, remaining_sum]
    constraints = []
    for vars_list, s in rows:
        constraints.append([list(vars_list), s])
    for vars_list, s in cols:
        constraints.append([list(vars_list), s])
    
    # remaining unknown count and sum for each constraint
    # We'll iterate until all solved
    
    changed = True
    while changed:
        changed = False
        for i, (vars_list, s) in enumerate(constraints):
            # compute remaining sum and unknown vars
            remaining_sum = s
            unknowns = []
            for v in vars_list:
                if v in known:
                    remaining_sum -= known[v]
                else:
                    unknowns.append(v)
            # deduplicate unknowns but keep track of counts
            # Actually variables can repeat in a row/col
            # Count occurrences of each unknown
            from collections import Counter
            cnt = Counter(unknowns)
            unique_unknowns = list(cnt.keys())
            
            if len(unique_unknowns) == 1:
                var = unique_unknowns[0]
                count = cnt[var]
                val = remaining_sum // count
                known[var] = val
                changed = True
            elif len(unique_unknowns) == 0:
                pass  # already solved
    
    # Sort variables alphabetically
    sorted_vars = sorted(known.keys())
    out = []
    for v in sorted_vars:
        out.append(f"{v} {known[v]}")
    print('\n'.join(out))

solve()