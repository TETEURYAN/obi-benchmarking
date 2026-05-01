import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    
    while idx < len(input_data):
        n = int(input_data[idx]); idx += 1
        if n == 0:
            break
        
        test_num += 1
        
        pieces = []
        for _ in range(n):
            x = int(input_data[idx]); idx += 1
            y = int(input_data[idx]); idx += 1
            pieces.append((x, y))
        
        # Build graph - dominoes form an Eulerian path problem
        # Each domino is an edge between x and y
        # We need to find if an Eulerian path exists
        
        # Conditions for Eulerian path in undirected graph:
        # 1. The graph must be connected (considering only vertices with edges)
        # 2. Either all vertices have even degree (Eulerian circuit)
        #    or exactly 2 vertices have odd degree (Eulerian path)
        
        degree = defaultdict(int)
        adj = defaultdict(list)
        
        for x, y in pieces:
            degree[x] += 1
            degree[y] += 1
            adj[x].append(y)
            if x != y:
                adj[y].append(x)
        
        # Check connectivity using Union-Find
        parent = list(range(7))
        
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        
        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                parent[a] = b
        
        for x, y in pieces:
            union(x, y)
        
        # Find all vertices that appear in pieces
        vertices_used = set()
        for x, y in pieces:
            vertices_used.add(x)
            vertices_used.add(y)
        
        # Check connectivity among used vertices
        connected = True
        if len(vertices_used) > 0:
            roots = set(find(v) for v in vertices_used)
            if len(roots) > 1:
                connected = False
        
        # Count odd degree vertices
        odd_count = 0
        for v in vertices_used:
            if degree[v] % 2 == 1:
                odd_count += 1
        
        # Eulerian path exists if connected and (0 or 2 odd degree vertices)
        if connected and (odd_count == 0 or odd_count == 2):
            result = "sim"
        else:
            result = "nao"
        
        print(f"Teste {test_num}")
        print(result)
        print()

solve()