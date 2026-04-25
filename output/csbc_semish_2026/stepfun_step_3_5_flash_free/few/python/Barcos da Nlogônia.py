import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); b = int(next(it))
    edges = []
    for _ in range(b):
        u = int(next(it)); v = int(next(it)); p = int(next(it))
        edges.append((p, u, v))
    edges.sort(key=lambda x: x[0], reverse=True)
    
    parent_dsu = list(range(n+1))
    rank = [0]*(n+1)
    def find(x):
        while parent_dsu[x] != x:
            parent_dsu[x] = parent_dsu[parent_dsu[x]]
            x = parent_dsu[x]
        return x
    def union(x, y):
        rx = find(x); ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent_dsu[rx] = ry
        elif rank[rx] > rank[ry]:
            parent_dsu[ry] = rx
        else:
            parent_dsu[ry] = rx
            rank[rx] += 1
        return True
    
    tree = [[] for _ in range(n+1)]
    count_edges = 0
    for p, u, v in edges:
        if union(u, v):
            tree[u].append((v, p))
            tree[v].append((u, p))
            count_edges += 1
            if count_edges == n-1:
                break
    
    LOG = (n).bit_length()
    parent = [[0]*(n+1) for _ in range(LOG)]
    min_edge = [[10**9+1]*(n+1) for _ in range(LOG)]
    depth = [0]*(n+1)
    
    from collections import deque
    q = deque([1])
    depth[1] = 0
    parent[0][1] = 0
    min_edge[0][1] = 10**9+1
    visited = [False]*(n+1)
    visited[1] = True
    while q:
        u = q.popleft()
        for v, w in tree[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                parent[0][v] = u
                min_edge[0][v] = w
                q.append(v)
    
    for k in range(1, LOG):
        for v in range(1, n+1):
            p = parent[k-1][v]
            parent[k][v] = parent[k-1][p]
            min_edge[k][v] = min(min_edge[k-1][v], min_edge[k-1][p])
    
    c = int(next(it))
    out_lines = []
    for _ in range(c):
        x = int(next(it)); y = int(next(it))
        if depth[x] < depth[y]:
            x, y = y, x
        min_val = 10**9+1
        diff = depth[x] - depth[y]
        k = 0
        while diff:
            if diff & 1:
                min_val = min(min_val, min_edge[k][x])
                x = parent[k][x]
            diff >>= 1
            k += 1
        if x == y:
            out_lines.append(str(min_val))
            continue
        for k in range(LOG-1, -1, -1):
            if parent[k][x] != parent[k][y]:
                min_val = min(min_val, min_edge[k][x], min_edge[k][y])
                x = parent[k][x]
                y = parent[k][y]
        min_val = min(min_val, min_edge[0][x], min_edge[0][y])
        out_lines.append(str(min_val))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()