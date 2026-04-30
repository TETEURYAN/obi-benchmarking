import sys
from sys import setrecursionlimit

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        adj[a].append(b)
        adj[b].append(a)
    
    # Compute subtree sizes using iterative DFS
    subtree_size = [1] * (n + 1)
    parent = [0] * (n + 1)
    order = []
    
    visited = [False] * (n + 1)
    stack = [1]
    visited[1] = True
    parent[1] = 0
    
    while stack:
        node = stack.pop()
        order.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                stack.append(neighbor)
    
    # Process in reverse order to compute subtree sizes
    for node in reversed(order):
        if parent[node] != 0:
            subtree_size[parent[node]] += subtree_size[node]
    
    # For each edge (parent[node], node), removing it gives subtrees of size
    # subtree_size[node] and n - subtree_size[node]
    best = float('inf')
    for node in range(2, n + 1):
        s = subtree_size[node]
        diff = abs(s - (n - s))
        if diff < best:
            best = diff
    
    print(best)

main()