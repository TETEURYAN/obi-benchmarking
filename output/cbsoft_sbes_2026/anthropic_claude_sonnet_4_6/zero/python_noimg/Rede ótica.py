import sys

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1
    return True

input_data = sys.stdin.read().split()
idx = 0
test_num = 1

while True:
    N = int(input_data[idx]); M = int(input_data[idx+1])
    idx += 2
    if N == 0:
        break
    
    edges = []
    for _ in range(M):
        x = int(input_data[idx]); y = int(input_data[idx+1]); z = int(input_data[idx+2])
        idx += 3
        edges.append((z, x, y))
    
    edges.sort()
    parent = list(range(N+1))
    rank = [0] * (N+1)
    
    result = []
    for z, x, y in edges:
        if union(parent, rank, x, y):
            if x < y:
                result.append((x, y))
            else:
                result.append((y, x))
    
    result.sort()
    print(f"Teste {test_num}")
    for a, b in result:
        print(f"{a} {b}")
    print()
    test_num += 1