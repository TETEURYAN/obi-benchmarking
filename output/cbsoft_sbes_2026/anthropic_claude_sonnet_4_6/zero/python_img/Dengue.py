import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    results = []
    
    while idx < len(input_data):
        N = int(input_data[idx]); idx += 1
        
        if N == 0:
            break
        
        test_num += 1
        
        if N == 1:
            # Only one village
            results.append(f"Teste {test_num}\n1\n")
            continue
        
        adj = [[] for _ in range(N + 1)]
        
        for _ in range(N - 1):
            x = int(input_data[idx]); idx += 1
            y = int(input_data[idx]); idx += 1
            adj[x].append(y)
            adj[y].append(x)
        
        # Find the center of the tree (minimizes eccentricity = max distance)
        # Algorithm: repeatedly remove leaves until 1 or 2 nodes remain
        # Those are the centers
        
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
        # Find distances from v
        _, dist_v = bfs(v)
        
        # The diameter path goes from u to v
        # We need to find the middle node(s)
        diameter = dist_u[v]
        
        # Find the center: node(s) on the path from u to v at distance diameter//2 from u
        # We can find the path by tracing back from v using dist_u
        # Reconstruct path from u to v
        
        # BFS from u with parent tracking
        parent = [-1] * (N + 1)
        dist2 = [-1] * (N + 1)
        dist2[u] = 0
        q = deque([u])
        while q:
            node = q.popleft()
            for nb in adj[node]:
                if dist2[nb] == -1:
                    dist2[nb] = dist2[node] + 1
                    parent[nb] = node
                    q.append(nb)
        
        # Reconstruct path from u to v
        path = []
        cur = v
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()  # path[0] = u, path[-1] = v
        
        # Center is at index diameter//2
        center_idx = diameter // 2
        center = path[center_idx]
        
        results.append(f"Teste {test_num}\n{center}\n")
    
    print('\n'.join(results))

solve()