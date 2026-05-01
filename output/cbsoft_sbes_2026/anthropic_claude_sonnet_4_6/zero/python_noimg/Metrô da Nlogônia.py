import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    # Build tree for Circle system (N nodes, 1-indexed)
    adj_c = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        adj_c[a].append(b)
        adj_c[b].append(a)
    
    # Build tree for Square system (M nodes, 1-indexed)
    adj_s = [[] for _ in range(M + 1)]
    for _ in range(M - 1):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        adj_s[x].append(y)
        adj_s[y].append(x)
    
    def bfs(adj, start, n):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        farthest = start
        max_d = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if dist[v] > max_d:
                        max_d = dist[v]
                        farthest = v
                    q.append(v)
        return farthest, max_d, dist
    
    # Find diameter of Circle tree and eccentricity-like info
    # For tree diameter: BFS from any node, find farthest u, BFS from u find farthest v
    # diameter = dist(u,v)
    # For minimizing the new diameter after connecting:
    # The new diameter = max(diam_C, diam_S, ceil(diam_C/2) + ceil(diam_S/2) + 1)
    # We want to connect the center of C's diameter path to center of S's diameter path
    
    def get_diameter_and_centers(adj, n):
        # BFS from node 1 to find one end of diameter
        u, _, _ = bfs(adj, 1, n)
        # BFS from u to find other end v and distances from u
        v, diam, dist_u = bfs(adj, u, n)
        # BFS from v to get distances from v
        _, _, dist_v = bfs(adj, v, n)
        
        # The center(s) of the diameter path: nodes at distance floor(diam/2) from u on the path
        # A node is on the diameter path if dist_u[node] + dist_v[node] == diam
        # The center is the node on the path with dist_u[node] == diam // 2
        # (or (diam//2, diam//2+1) for even/odd)
        
        # Find center node: on diameter path, dist_u[node] = diam // 2
        # Actually we want the node that minimizes max(dist_u[node], dist_v[node])
        # which is the node where dist_u[node] = floor(diam/2)
        
        center = -1
        half = diam // 2
        for node in range(1, n + 1):
            if dist_u[node] + dist_v[node] == diam and dist_u[node] == half:
                center = node
                break
        
        return diam, center, dist_u, dist_v
    
    diam_c, center_c, dist_uc, dist_vc = get_diameter_and_centers(adj_c, N)
    diam_s, center_s, dist_us, dist_vs = get_diameter_and_centers(adj_s, M)
    
    # The optimal new diameter is max(diam_c, diam_s, (diam_c+1)//2 + (diam_s+1)//2 + 1)
    # The best nodes to connect are the centers of each tree's diameter
    
    print(center_c, center_s)

solve()