import sys

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    results = []
    
    while idx < len(data):
        n = int(data[idx]); idx += 1
        if n == 0:
            break
        test_num += 1
        
        degree = [0] * 7
        parent = list(range(7))
        rank = [0] * 7
        
        pieces = []
        for _ in range(n):
            x = int(data[idx]); y = int(data[idx+1]); idx += 2
            pieces.append((x, y))
            degree[x] += 1
            degree[y] += 1
            union(parent, rank, x, y)
        
        # Check Eulerian path/circuit conditions
        # 1. All vertices with non-zero degree must be connected
        # 2. Number of vertices with odd degree must be 0 or 2
        
        # Find all nodes that appear in pieces
        used = set()
        for x, y in pieces:
            used.add(x)
            used.add(y)
        
        # Check connectivity among used nodes
        if len(used) == 0:
            results.append((test_num, "sim"))
            continue
        
        roots = set()
        for v in used:
            roots.add(find(parent, v))
        
        connected = len(roots) == 1
        
        odd_count = sum(1 for v in used if degree[v] % 2 == 1)
        
        if connected and (odd_count == 0 or odd_count == 2):
            results.append((test_num, "sim"))
        else:
            results.append((test_num, "nao"))
    
    output = []
    for num, ans in results:
        output.append(f"Teste {num}")
        output.append(ans)
        output.append("")
    
    print('\n'.join(output))

solve()