import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    C = [int(next(it)) for _ in range(N)]
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Pares para cada label (1 a N//2)
    pairs = [[] for _ in range(N//2 + 1)]
    for i in range(1, N+1):
        label = C[i-1]
        pairs[label].append(i)
    
    # BFS para depth e parent0
    from collections import deque
    depth = [0]*(N+1)
    parent0 = [0]*(N+1)
    queue = deque([1])
    depth[1] = 0
    parent0[1] = 0
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v == parent0[u]:
                continue
            depth[v] = depth[u] + 1
            parent0[v] = u
            queue.append(v)
    
    # Binary lifting
    LOG = (N).bit_length()
    parent = [[0]*(N+1) for _ in range(LOG)]
    for v in range(1, N+1):
        parent[0][v] = parent0[v]
    for k in range(1, LOG):
        for v in range(1, N+1):
            parent[k][v] = parent[k-1][parent[k-1][v]]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        # Levantar u
        diff = depth[u] - depth[v]
        bit = 0
        while diff:
            if diff & 1:
                u = parent[bit][u]
            diff >>= 1
            bit += 1
        if u == v:
            return u
        for k in range(LOG-1, -1, -1):
            if parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]
        return parent0[u]
    
    cnt = [0]*(N+1)
    for label in range(1, N//2+1):
        u, v = pairs[label]
        l = lca(u, v)
        cnt[u] += 1
        cnt[v] += 1
        cnt[l] -= 2
    
    # Ordem pós-ordem iterativa
    stack = [(1, 0, 0)]  # (nó, pai, próximo índice)
    order = []
    while stack:
        u, p, i = stack.pop()
        if i < len(adj[u]):
            v = adj[u][i]
            stack.append((u, p, i+1))
            if v != p:
                stack.append((v, u, 0))
        else:
            order.append(u)
    
    ans = 0
    for u in order:
        if u == 1:
            continue
        ans += cnt[u]
        cnt[parent0[u]] += cnt[u]
    
    print(ans)

if __name__ == "__main__":
    main()