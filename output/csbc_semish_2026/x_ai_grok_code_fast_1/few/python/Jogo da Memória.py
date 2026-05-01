import sys
from collections import defaultdict

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
C = [0] + [int(x) for x in input_data[idx:idx+N]]
idx += N
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a = int(input_data[idx])
    b = int(input_data[idx+1])
    adj[a].append(b)
    adj[b].append(a)
    idx += 2

pares = defaultdict(list)
for i in range(1, N+1):
    pares[C[i]].append(i)

depth = [0] * (N+1)
dist_to_root = [0] * (N+1)
parent = [[-1] * 17 for _ in range(N+1)]

def dfs(node, par, dep, dist):
    depth[node] = dep
    dist_to_root[node] = dist
    parent[node][0] = par
    for nei in adj[node]:
        if nei != par:
            dfs(nei, node, dep+1, dist+1)

dfs(1, -1, 0, 0)

for k in range(1, 17):
    for i in range(1, N+1):
        if parent[i][k-1] != -1:
            parent[i][k] = parent[parent[i][k-1]][k-1]

def get_lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    diff = depth[v] - depth[u]
    for k in range(17):
        if diff & (1 << k):
            v = parent[v][k]
    if u == v:
        return u
    for k in range(16, -1, -1):
        if parent[u][k] != parent[v][k]:
            u = parent[u][k]
            v = parent[v][k]
    return parent[u][0]

soma = 0
for num in range(1, N//2 + 1):
    u, v = pares[num]
    lca = get_lca(u, v)
    d = dist_to_root[u] + dist_to_root[v] - 2 * dist_to_root[lca]
    soma += d

print(soma)