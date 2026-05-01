
import sys

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def is_connected(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    components = n
    for u, v in edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            union(parent, rank, x, y)
            components -= 1
    return components == 1

test_num = 1
input_data = sys.stdin.read().split()
idx = 0

while True:
    E = int(input_data[idx])
    L = int(input_data[idx + 1])
    idx += 2
    if E == 0 and L == 0:
        break
    
    edges = []
    for _ in range(L):
        X = int(input_data[idx])
        Y = int(input_data[idx + 1])
        idx += 2
        edges.append((X, Y))
    
    state = "normal" if is_connected(E, edges) else "falha"
    
    print(f"Teste {test_num}")
    print(state)
    print()
    test_num += 1
