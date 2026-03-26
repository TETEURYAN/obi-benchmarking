import sys

# Define recursion limit to handle deep trees (up to 10^5 nodes)
sys.setrecursionlimit(300000)

def solve():
    # Read all input at once for performance
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        B = int(next(iterator))
    except StopIteration:
        return

    edges = []
    for _ in range(B):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        edges.append((w, u, v))

    # Sort edges by weight in descending order to build Maximum Spanning Tree
    edges.sort(reverse=True)

    # Union-Find (Disjoint Set Union) data structure
    parent = list(range(N + 1))
    rank = [0] * (N + 1)

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            elif rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        return False

    # Build Maximum Spanning Tree
    adj = [[] for _ in range(N + 1)]
    for w, u, v in edges:
        if union(u, v):
            adj[u].append((v, w))
            adj[v].append((u, w))

    # LCA Preprocessing
    LOG = (N + 1).bit_length()
    up = [[0] * (N + 1) for _ in range(LOG)]
    min_edge = [[float('inf')] * (N + 1) for _ in range(LOG)]
    depth = [0] * (N + 1)
    
    # DFS to compute depth, parents, and min_edge to parent
    def dfs(u, p, w):
        up[0][u] = p
        min_edge[0][u] = w
        depth[u] = depth[p] + 1 if p != 0 else 0
        
        for v, weight in adj[u]:
            if v != p:
                dfs(v, u, weight)

    # Assuming graph is connected, start DFS from node 1
    # Node 0 is used as a sentinel for the root's parent
    dfs(1, 0, float('inf'))

    # Build sparse table for LCA and min_edge
    for k in range(1, LOG):
        for v in range(1, N + 1):
            up[k][v] = up[k-1][up[k-1][v]]
            min_edge[k][v] = min(min_edge[k-1][v], min_edge[k-1][up[k-1][v]])

    # Process Queries
    try:
        C = int(next(iterator))
    except StopIteration:
        C = 0

    results = []
    
    for _ in range(C):
        X = int(next(iterator))
        Y = int(next(iterator))
        
        # Ensure X is the deeper node
        if depth[X] < depth[Y]:
            X, Y = Y, X
            
        ans = float('inf')
        diff = depth[X] - depth[Y]
        
        # Lift X to the same depth as Y
        for k in range(LOG):
            if (diff >> k) & 1:
                ans = min(ans, min_edge[k][X])
                X = up[k][X]
        
        if X == Y:
            results.append(str(int(ans)))
            continue
            
        # Lift both X and Y to just below LCA
        for k in range(LOG - 1, -1, -1):
            if up[k][X] != up[k][Y]:
                ans = min(ans, min_edge[k][X])
                ans = min(ans, min_edge[k][Y])
                X = up[k][X]
                Y = up[k][Y]
        
        # Now X and Y are direct children of LCA
        ans = min(ans, min_edge[0][X])
        ans = min(ans, min_edge[0][Y])
        
        results.append(str(int(ans)))

    print('\n'.join(results))

if __name__ == '__main__':
    solve()