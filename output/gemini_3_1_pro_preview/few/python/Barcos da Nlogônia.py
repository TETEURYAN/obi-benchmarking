import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    B = int(input_data[1])
    
    idx = 2
    edges = []
    for _ in range(B):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((u, v, w))
        idx += 3
        
    C = int(input_data[idx])
    idx += 1
    queries = []
    for _ in range(C):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        queries.append((u, v))
        idx += 2

    edges.sort(key=lambda x: x[2], reverse=True)
    
    parent = list(range(N + 1))
    rank = [0] * (N + 1)

    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        return False

    mst_adj = [[] for _ in range(N + 1)]
    for u, v, w in edges:
        if union(u, v):
            mst_adj[u].append((v, w))
            mst_adj[v].append((u, w))

    LOG = 18
    up = [[0] * LOG for _ in range(N + 1)]
    min_w = [[float('inf')] * LOG for _ in range(N + 1)]
    depth = [0] * (N + 1)
    
    visited = [False] * (N + 1)
    q = deque()
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            up[i][0] = i
            q.append(i)
            while q:
                u = q.popleft()
                for v, w in mst_adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        depth[v] = depth[u] + 1
                        up[v][0] = u
                        min_w[v][0] = w
                        q.append(v)

    for j in range(1, LOG):
        for i in range(1, N + 1):
            up[i][j] = up[up[i][j-1]][j-1]
            min_w[i][j] = min(min_w[i][j-1], min_w[up[i][j-1]][j-1])

    out = []
    for u, v in queries:
        ans = float('inf')
        if depth[u] < depth[v]:
            u, v = v, u
        
        diff = depth[u] - depth[v]
        for j in range(LOG):
            if (diff >> j) & 1:
                ans = min(ans, min_w[u][j])
                u = up[u][j]
                
        if u == v:
            out.append(str(ans))
            continue
            
        for j in range(LOG - 1, -1, -1):
            if up[u][j] != up[v][j]:
                ans = min(ans, min_w[u][j], min_w[v][j])
                u = up[u][j]
                v = up[v][j]
                
        ans = min(ans, min_w[u][0], min_w[v][0])
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()