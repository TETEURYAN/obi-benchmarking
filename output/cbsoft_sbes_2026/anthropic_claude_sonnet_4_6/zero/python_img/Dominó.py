import sys
from collections import defaultdict

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
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    
    while idx < len(input_data):
        n = int(input_data[idx]); idx += 1
        if n == 0:
            break
        
        test_num += 1
        
        degree = defaultdict(int)
        parent = list(range(7))
        rank = [0] * 7
        
        edges = []
        nodes_used = set()
        
        for _ in range(n):
            x = int(input_data[idx]); idx += 1
            y = int(input_data[idx]); idx += 1
            edges.append((x, y))
            degree[x] += 1
            degree[y] += 1
            nodes_used.add(x)
            nodes_used.add(y)
            union(parent, rank, x, y)
        
        # Check connectivity among used nodes
        if len(nodes_used) == 0:
            print(f"Teste {test_num}")
            print("sim")
            print()
            continue
        
        roots = set()
        for node in nodes_used:
            roots.add(find(parent, node))
        
        connected = len(roots) == 1
        
        # Check Eulerian path condition
        # For Eulerian path: 0 or 2 nodes with odd degree
        odd_count = sum(1 for node in nodes_used if degree[node] % 2 == 1)
        
        eulerian = connected and (odd_count == 0 or odd_count == 2)
        
        print(f"Teste {test_num}")
        print("sim" if eulerian else "nao")
        print()

solve()