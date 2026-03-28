import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    results = []
    
    while idx < len(data):
        N = int(data[idx]); idx += 1
        
        if N == 0:
            break
        
        test_num += 1
        
        if N == 1:
            results.append(f"Teste {test_num}\n1\n")
            continue
        
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            x = int(data[idx]); y = int(data[idx+1]); idx += 2
            adj[x].append(y)
            adj[y].append(x)
        
        # Find the center of the tree (minimizes eccentricity = max distance)
        # Algorithm: repeatedly remove leaves until 1 or 2 nodes remain
        # Those are the center(s)
        
        # BFS from any node to find farthest, then BFS from farthest to find diameter endpoints
        # Center is the middle node(s) of the diameter path
        
        def bfs(start):
            dist = [-1] * (N + 1)
            dist[start] = 0
            q = deque([start])
            farthest = start
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
                        if dist[v] > dist[farthest]:
                            farthest = v
            return farthest, dist
        
        # Find one end of diameter
        u, _ = bfs(1)
        # Find other end of diameter
        v, dist_u = bfs(u)
        # Get diameter length
        diameter = dist_u[v]
        
        # Reconstruct path from u to v using BFS parent tracking
        parent = [-1] * (N + 1)
        visited = [False] * (N + 1)
        visited[u] = True
        q = deque([u])
        while q:
            node = q.popleft()
            for nb in adj[node]:
                if not visited[nb]:
                    visited[nb] = True
                    parent[nb] = node
                    q.append(nb)
        
        # Reconstruct path from v back to u
        path = []
        cur = v
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        # path goes from v to u
        
        # Center is at position diameter//2 from u (which is at end of path)
        # path[0] = v, path[-1] = u
        # distance from u to center = diameter//2
        center_idx = len(path) - 1 - diameter // 2
        center = path[center_idx]
        
        results.append(f"Teste {test_num}\n{center}\n")
    
    print('\n'.join(results))

solve()