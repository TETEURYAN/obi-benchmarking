import sys
from collections import deque

def bfs(start, adj, n):
    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    far = start

    while q:
        u = q.popleft()
        if dist[u] > dist[far]:
            far = u
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
    return far, dist, parent

data = list(map(int, sys.stdin.read().split()))
i = 0
teste = 1
out = []

while i < len(data):
    n = data[i]
    i += 1
    if n == 0:
        break

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x = data[i]
        y = data[i + 1]
        i += 2
        adj[x].append(y)
        adj[y].append(x)

    if n == 1:
        center = 1
    else:
        a, _, _ = bfs(1, adj, n)
        b, _, parent = bfs(a, adj, n)

        path = []
        cur = b
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        center = path[(len(path) - 1) // 2]

    out.append(f"Teste {teste}")
    out.append(str(center))
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))