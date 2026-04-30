
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [0] * (N+1)
depth = [0] * (N+1)
color = [0] * (N+1)

def dfs(u, p, d):
    parent[u] = p
    depth[u] = d
    for v in adj[u]:
        if v != p:
            dfs(v, u, d+1)

dfs(1, 0, 0)

def get_path(a, b):
    path = []
    if depth[a] > depth[b]:
        a, b = b, a
    while depth[b] > depth[a]:
        path.append(b)
        b = parent[b]
    while a != b:
        path.append(a)
        path.append(b)
        a = parent[a]
        b = parent[b]
    path.append(a)
    return path

for _ in range(M):
    p, q, c = map(int, input().split())
    path = get_path(p, q)
    for node in path:
        color[node] = c

print(' '.join(map(str, color[1:])))
