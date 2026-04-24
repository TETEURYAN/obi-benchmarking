import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    N = int(data[idx]); idx += 1
    
    # Read friendship matrix
    # Since friendship is transitive and forms equivalence classes,
    # we can use Union-Find to group candidates
    
    parent = list(range(N + 1))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    rows = []
    for i in range(1, N + 1):
        row = data[idx]; idx += 1
        rows.append(row)
        for j in range(N):
            if row[j] == '1':
                union(i, j + 1)
    
    E = int(data[idx]); idx += 1
    
    out = []
    for _ in range(E):
        K = int(data[idx]); idx += 1
        candidates = []
        for _ in range(K):
            candidates.append(int(data[idx])); idx += 1
        
        # Check if any two candidates share the same group
        groups = set()
        found = False
        for c in candidates:
            g = find(c)
            if g in groups:
                found = True
                break
            groups.add(g)
        
        out.append('S' if found else 'N')
    
    print('\n'.join(out))

main()