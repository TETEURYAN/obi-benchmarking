import sys
from collections import defaultdict

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    
    N = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    edges = []
    for _ in range(B):
        i = int(input_data[idx]); idx += 1
        j = int(input_data[idx]); idx += 1
        p = int(input_data[idx]); idx += 1
        edges.append((p, i, j))
    
    C = int(input_data[idx]); idx += 1
    queries = []
    for _ in range(C):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        queries.append((x, y))
    
    # Maximum spanning tree (Kruskal) to answer bottleneck queries
    # Sort edges in descending order of capacity
    edges.sort(reverse=True)
    
    # Union-Find
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True
    
    # Build maximum spanning tree using Kruskal
    # We'll build an adjacency list for the MST
    mst_adj = defaultdict(list)
    
    for p, i, j in edges:
        if find(i) != find(j):
            union(i, j)
            mst_adj[i].append((j, p))
            mst_adj[j].append((i, p))
    
    # For each query (x, y), find the minimum edge weight on the path in MST
    # Use LCA with binary lifting
    
    LOG = 17
    
    # Build tree rooted at 1
    # BFS to set up parent and depth
    from collections import deque
    
    depth = [0] * (N + 1)
    up = [[-1] * (N + 1) for _ in range(LOG)]
    min_cap = [[0] * (N + 1) for _ in range(LOG)]
    
    visited = [False] * (N + 1)
    queue = deque([1])
    visited[1] = True
    up[0][1] = 1
    min_cap[0][1] = float('inf')
    
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for (nb, w) in mst_adj[node]:
            if not visited[nb]:
                visited[nb] = True
                depth[nb] = depth[node] + 1
                up[0][nb] = node
                min_cap[0][nb] = w
                queue.append(nb)
    
    # Fill binary lifting table
    for k in range(1, LOG):
        for v in range(1, N + 1):
            anc = up[k-1][v]
            up[k][v] = up[k-1][anc]
            min_cap[k][v] = min(min_cap[k-1][v], min_cap[k-1][anc])
    
    def query_lca(u, v):
        res = float('inf')
        if depth[u] < depth[v]:
            u, v = v, u
        # Bring u to same depth as v
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                res = min(res, min_cap[k][u])
                u = up[k][u]
        if u == v:
            return res
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                res = min(res, min_cap[k][u])
                res = min(res, min_cap[k][v])
                u = up[k][u]
                v = up[k][v]
        res = min(res, min_cap[0][u])
        res = min(res, min_cap[0][v])
        return res
    
    out = []
    for (x, y) in queries:
        ans = query_lca(x, y)
        out.append(str(ans))
    
    print('\n'.join(out))

main()