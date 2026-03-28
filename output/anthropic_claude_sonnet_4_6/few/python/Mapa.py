import sys
from collections import defaultdict

def solve():
    sys.setrecursionlimit(300000)
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        adj[a].append((b, c))
        adj[b].append((a, c))
    
    # We need to count pairs (A, B) such that there's at least one white (c=1) edge on the path.
    # Total pairs = n*(n-1)/2
    # Pairs with NO white edge = pairs where path uses only blue edges
    # Blue edges form a forest (subgraph of the tree with only blue edges)
    # In each connected component of the blue subgraph, all pairs have no white edge on path
    # So answer = total_pairs - sum over blue components of size s: s*(s-1)/2
    
    total = n * (n - 1) // 2
    
    # Find connected components using only blue edges (c=0)
    visited = [False] * (n + 1)
    blue_components = []
    
    for start in range(1, n + 1):
        if not visited[start]:
            # BFS
            stack = [start]
            visited[start] = True
            size = 0
            while stack:
                node = stack.pop()
                size += 1
                for (nb, c) in adj[node]:
                    if not visited[nb] and c == 0:
                        visited[nb] = True
                        stack.append(nb)
            blue_components.append(size)
    
    blue_pairs = sum(s * (s - 1) // 2 for s in blue_components)
    
    print(total - blue_pairs)

solve()