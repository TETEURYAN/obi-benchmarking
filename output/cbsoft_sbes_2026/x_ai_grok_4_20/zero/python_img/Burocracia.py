
import sys
sys.setrecursionlimit(200000)

N = int(input())
P = [0] * (N + 1)
parent = list(map(int, input().split()))
for i in range(2, N + 1):
    P[i] = parent[i - 2]

Q = int(input())

children = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    children[P[i]].append(i)

depth = [0] * (N + 1)
anc = [[0] * 18 for _ in range(N + 1)]

def dfs(u, d, par):
    depth[u] = d
    anc[u][0] = par
    for i in range(1, 18):
        if anc[u][i - 1] != 0:
            anc[u][i] = anc[anc[u][i - 1]][i - 1]
        else:
            anc[u][i] = 0
    for v in children[u]:
        if v != par:
            dfs(v, d + 1, u)

dfs(1, 0, 0)

def get_kth_ancestor(u, k):
    for i in range(18):
        if k & (1 << i):
            u = anc[u][i]
            if u == 0:
                return 0
    return u

def find_lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    diff = depth[b] - depth[a]
    b = get_kth_ancestor(b, diff)
    if a == b:
        return a
    for i in range(17, -1, -1):
        if anc[a][i] != anc[b][i]:
            a = anc[a][i]
            b = anc[b][i]
    return anc[a][0]

def distance(u, v):
    l = find_lca(u, v)
    return depth[u] + depth[v] - 2 * depth[l]

cur_parent = P[:]
cur_depth = depth[:]
cur_anc = [row[:] for row in anc]

def rebuild(v):
    global cur_parent, cur_depth, cur_anc
    new_p = [0] * (N + 1)
    new_d = [0] * (N + 1)
    new_anc = [[0] * 18 for _ in range(N + 1)]
    
    def rec(u, par, d):
        new_p[u] = par
        new_d[u] = d
        new_anc[u][0] = par
        for i in range(1, 18):
            if new_anc[u][i - 1] != 0:
                new_anc[u][i] = new_anc[new_anc[u][i - 1]][i - 1]
            else:
                new_anc[u][i] = 0
        for child in children[u]:
            if child != par and cur_parent[child] == u:
                rec(child, u, d + 1)
    
    rec(v, cur_parent[v], cur_depth[v])
    
    stack = []
    for child in children[v]:
        if cur_parent[child] == v:
            stack.append((child, v))
    
    while stack:
        u, par = stack.pop()
        new_p[u] = par
        new_d[u] = new_d[par] + 1
        new_anc[u][0] = par
        for i in range(1, 18):
            if new_anc[u][i - 1] != 0:
                new_anc[u][i] = new_anc[new_anc[u][i - 1]][i - 1]
            else:
                new_anc[u][i] = 0
        for child in children[u]:
            if cur_parent[child] == u:
                stack.append((child, u))
    
    cur_parent = new_p
    cur_depth = new_d
    cur_anc = new_anc

for _ in range(Q):
    line = list(map(int, input().split()))
    if line[0] == 2:
        v = line[1]
        rebuild(v)
    else:
        v = line[1]
        k = line[2]
        u = v
        for i in range(18):
            if k & (1 << i):
                u = cur_anc[u][i]
        print(u)
