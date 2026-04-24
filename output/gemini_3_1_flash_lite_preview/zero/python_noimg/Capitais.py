import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    if n == 2:
        print(1)
        return
    
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
        idx += 2
        
    leaves = deque([i for i in range(1, n + 1) if degree[i] == 1])
    
    dist = [0] * (n + 1)
    removed = [False] * (n + 1)
    
    remaining_nodes = n
    layers = 0
    
    while remaining_nodes > 2:
        layers += 1
        num_leaves = len(leaves)
        remaining_nodes -= num_leaves
        
        for _ in range(num_leaves):
            u = leaves.popleft()
            removed[u] = True
            for v in adj[u]:
                if not removed[v]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        leaves.append(v)
                        
    if remaining_nodes == 2:
        print(2 * layers + 1)
    else:
        print(2 * layers)

solve()