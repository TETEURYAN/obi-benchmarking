
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0] * (N+1)
depth = [0] * (N+1)
color = [0] * (N+1)

def dfs(node, par, dep):
    parent[node] = par
    depth[node] = dep
    for nei in graph[node]:
        if nei != par:
            dfs(nei, node, dep+1)

dfs(1, 0, 0)

def get_path(u, v):
    path = []
    if depth[u] > depth[v]:
        u, v = v, u
    while depth[v] > depth[u]:
        path.append(v)
        v = parent[v]
    while u != v:
        path.append(u)
        path.append(v)
        u = parent[u]
        v = parent[v]
    path.append(u)
    return path

for _ in range(M):
    p, q, c = map(int, input().split())
    path = get_path(p, q)
    for node in path:
        color[node] = c

print(' '.join(map(str, color[1:])))
