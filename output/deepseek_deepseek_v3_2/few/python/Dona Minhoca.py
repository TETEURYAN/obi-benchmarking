import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        adj[b].append(a)

    # 1. Encontrar o diâmetro da árvore
    def bfs(start: int):
        dist = [-1] * (N + 1)
        q = [start]
        dist[start] = 0
        for u in q:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        far = max(range(1, N + 1), key=lambda x: dist[x])
        return far, dist

    end1, _ = bfs(1)
    end2, dist_from_end1 = bfs(end1)
    _, dist_from_end2 = bfs(end2)

    diameter = max(dist_from_end1)
    radius = (diameter + 1) // 2

    # 2. Encontrar o centro (ou os dois centros) da árvore
    center_candidates = []
    for i in range(1, N + 1):
        if dist_from_end1[i] + dist_from_end2[i] == diameter:
            if dist_from_end1[i] == radius or dist_from_end2[i] == radius:
                center_candidates.append(i)

    # 3. Raiz na árvore a partir de um centro
    root = center_candidates[0]
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    stack = [(root, 0)]
    order = []
    while stack:
        u, p = stack.pop()
        parent[u] = p
        order.append(u)
        for v in adj[u]:
            if v != p:
                depth[v] = depth[u] + 1
                stack.append((v, u))

    # 4. Calcular alturas (distância máxima até uma folha na subárvore)
    height = [0] * (N + 1)
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                height[u] = max(height[u], height[v] + 1)

    # 5. Ordenar filhos por altura decrescente
    for u in range(1, N + 1):
        adj[u].sort(key=lambda x: -height[x] if x != parent[u] else -1)

    # 6. Busca binária no raio R
    def can(R: int) -> bool:
        if R == 0:
            return K >= N
        used = 0
        visited = [False] * (N + 1)

        def dfs(u: int, p: int) -> int:
            nonlocal used
            max_depth = 0
            for v in adj[u]:
                if v == p:
                    continue
                child_depth = dfs(v, u) + 1
                if child_depth > R:
                    if p == 0:
                        used += 1
                    else:
                        max_depth = max(max_depth, child_depth)
                else:
                    max_depth = max(max_depth, child_depth)
            return max_depth

        dfs(root, 0)
        used += 1
        return used <= K

    lo, hi = 0, diameter
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    solve()