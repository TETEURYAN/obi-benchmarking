import sys
from sys import setrecursionlimit

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        adj[a].append(b)
        adj[b].append(a)
    
    # Compute subtree sizes using iterative DFS
    subtree_size = [1] * (N + 1)
    parent = [0] * (N + 1)
    order = []
    
    visited = [False] * (N + 1)
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
    
    # For each edge (parent[node], node), removing it creates two components:
    # subtree_size[node] and N - subtree_size[node]
    best = float('inf')
    for node in range(2, N + 1):
        s = subtree_size[node]
        diff = abs(N - 2 * s)
        if diff < best:
            best = diff
    
    print(best)

main()