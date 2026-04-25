import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    E = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    D = int(data[idx]); idx+=1
    
    # Store "want together" pairs
    want = set()
    for _ in range(M):
        x = int(data[idx]); idx+=1
        y = int(data[idx]); idx+=1
        if x > y:
            x, y = y, x
        want.add((x, y))
    
    # Store "don't want together" pairs
    dont = set()
    for _ in range(D):
        u = int(data[idx]); idx+=1
        v = int(data[idx]); idx+=1
        if u > v:
            u, v = v, u
        dont.add((u, v))
    
    violations = 0
    num_groups = E // 3
    
    for _ in range(num_groups):
        i = int(data[idx]); idx+=1
        j = int(data[idx]); idx+=1
        k = int(data[idx]); idx+=1
        
        # All pairs in this group
        pairs = []
        a, b = (i, j) if i < j else (j, i)
        pairs.append((a, b))
        a, b = (i, k) if i < k else (k, i)
        pairs.append((a, b))
        a, b = (j, k) if j < k else (k, j)
        pairs.append((a, b))
        
        for p in pairs:
            if p in dont:
                violations += 1
        
        # Check "want" violations: pairs that wanted to be together but aren't in same group
        # Actually we need to check if want pairs are NOT in same group
        # We'll handle this after building group assignments
    
    # We need to reconsider: want violations = want pairs NOT in same group
    # dont violations = dont pairs IN same group
    # Let's redo with group assignment map
    
    # Reset and redo
    idx = 3 + 2*M + 2*D
    
    # Build student -> group mapping
    group_of = [0] * (E + 1)
    
    for g in range(num_groups):
        i = int(data[idx]); idx+=1
        j = int(data[idx]); idx+=1
        k = int(data[idx]); idx+=1
        group_of[i] = g
        group_of[j] = g
        group_of[k] = g
    
    violations = 0
    
    # Check want pairs: violated if NOT in same group
    for (x, y) in want:
        if group_of[x] != group_of[y]:
            violations += 1
    
    # Check dont pairs: violated if IN same group
    for (u, v) in dont:
        if group_of[u] == group_of[v]:
            violations += 1
    
    print(violations)

main()