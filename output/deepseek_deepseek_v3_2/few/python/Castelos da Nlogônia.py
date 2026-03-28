import sys
sys.setrecursionlimit(200000)

def dfs(u, p, depth):
    parent[0][u] = p
    level[u] = depth
    for v in adj[u]:
        if v != p:
            dfs(v, u, depth + 1)

def lca(a, b):
    if level[a] < level[b]:
        a, b = b, a
    diff = level[a] - level[b]
    for i in range(LOG):
        if diff & (1 << i):
            a = parent[i][a]
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        if parent[i][a] != parent[i][b]:
            a = parent[i][a]
            b = parent[i][b]
    return parent[0][a]

def paint_path(a, b, c):
    l = lca(a, b)
    while a != l:
        color[a] = c
        a = parent[0][a]
    while b != l:
        color[b] = c
        b = parent[0][b]
    color[l] = c

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    global adj, parent, level, color, LOG
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    LOG = 1
    while (1 << LOG) <= N:
        LOG += 1
    parent = [[0] * (N + 1) for _ in range(LOG)]
    level = [0] * (N + 1)
    color = [0] * (N + 1)
    dfs(1, 0, 0)
    for i in range(1, LOG):
        for v in range(1, N + 1):
            parent[i][v] = parent[i - 1][parent[i - 1][v]]
    for _ in range(M):
        p = int(next(it))
        q = int(next(it))
        c = int(next(it))
        paint_path(p, q, c)
    print(' '.join(str(color[i]) for i in range(1, N + 1)))

if __name__ == "__main__":
    main()