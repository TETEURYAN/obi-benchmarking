import sys
from collections import defaultdict, deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    C = int(input_data[1])
    
    idx = 2
    
    grid = []
    row_sums = []
    for _ in range(L):
        row = input_data[idx:idx+C]
        grid.append(row)
        idx += C
        row_sums.append(int(input_data[idx]))
        idx += 1
        
    col_sums = []
    for _ in range(C):
        col_sums.append(int(input_data[idx]))
        idx += 1
        
    equations = []
    var_to_eqs = defaultdict(list)
    
    for i in range(L):
        counts = defaultdict(int)
        for j in range(C):
            counts[grid[i][j]] += 1
        
        unknowns = set(counts.keys())
        target = row_sums[i]
        
        equations.append({
            'target': target,
            'unknowns': unknowns,
            'counts': counts
        })
        
        for v in unknowns:
            var_to_eqs[v].append(i)
            
    for j in range(C):
        counts = defaultdict(int)
        for i in range(L):
            counts[grid[i][j]] += 1
            
        unknowns = set(counts.keys())
        target = col_sums[j]
        
        equations.append({
            'target': target,
            'unknowns': unknowns,
            'counts': counts
        })
        
        for v in unknowns:
            var_to_eqs[v].append(L + j)
            
    queue = deque()
    for eq_idx, eq in enumerate(equations):
        if len(eq['unknowns']) == 1:
            queue.append(eq_idx)
            
    known = {}
    
    while queue:
        eq_idx = queue.popleft()
        eq = equations[eq_idx]
        
        if len(eq['unknowns']) == 1:
            v = next(iter(eq['unknowns']))
            
            if v not in known:
                val = eq['target'] // eq['counts'][v]
                known[v] = val
                
                for other_idx in var_to_eqs[v]:
                    other_eq = equations[other_idx]
                    if v in other_eq['unknowns']:
                        other_eq['target'] -= val * other_eq['counts'][v]
                        other_eq['unknowns'].remove(v)
                        if len(other_eq['unknowns']) == 1:
                            queue.append(other_idx)
                            
    for v in sorted(known.keys()):
        print(f"{v} {known[v]}")

if __name__ == '__main__':
    solve()