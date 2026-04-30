
import sys
sys.setrecursionlimit(10**6)

N, M, I = map(int, input().split())
ages = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N+1)]
parent = [0] * (N+1)
depth = [0] * (N+1)
min_up = [[10**9] * 9 for _ in range(N+1)]
order = []
in_time = [0] * (N+1)
out_time = [0] * (N+1)
timer = 0

def dfs(u, p, d):
    global timer
    parent[u] = p
    depth[u] = d
    in_time[u] = timer
    timer += 1
    order.append(u)
    min_up[u][0] = ages[p] if p != 0 else 10**9
    for i in range(1, 9):
        if min_up[u][i-1] != 10**9:
            min_up[u][i] = min(min_up[u][i-1], min_up[parent[u]][i-1] if parent[u] != 0 else 10**9)
        else:
            min_up[u][i] = 10**9
    for v in adj[u]:
        if v != p:
            dfs(v, u, d+1)
    out_time[u] = timer

for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    parent[y] = x

roots = []
for i in range(1, N+1):
    if parent[i] == 0:
        roots.append(i)

for root in roots:
    dfs(root, 0, 0)

def is_ancestor(a, b):
    return in_time[a] <= in_time[b] and out_time[a] >= out_time[b]

def get_min_manager(u):
    if parent[u] == 0:
        return -1
    res = 10**9
    cur = u
    for i in range(8, -1, -1):
        if min_up[cur][i] != 10**9:
            res = min(res, min_up[cur][i])
            cur = parent[cur] if i == 0 else parent[cur]
            if cur == 0:
                break
    return res

def swap_positions(a, b):
    if a == b:
        return
    pa = parent[a]
    pb = parent[b]
    da = depth[a]
    db = depth[b]
    if da > db:
        a, b = b, a
        pa, pb = pb, pa
        da, db = db, da
    if is_ancestor(a, b):
        if pa != 0:
            adj[pa].remove(a)
            adj[pa].append(b)
        parent[b] = pa
        parent[a] = b
        adj[a] = [b]
        if pb != 0:
            adj[pb].remove(b)
            adj[pb].append(a)
        parent[a] = pb
        adj[b] = []
        for v in adj[a]:
            if v != b:
                parent[v] = b
        return
    if pa != 0:
        for i in range(len(adj[pa])):
            if adj[pa][i] == a:
                adj[pa][i] = b
                break
    if pb != 0:
        for i in range(len(adj[pb])):
            if adj[pb][i] == b:
                adj[pb][i] = a
                break
    parent[a] = pb
    parent[b] = pa
    adj[a], adj[b] = adj[b], adj[a]
    for v in adj[a]:
        parent[v] = a
    for v in adj[b]:
        parent[v] = b

for _ in range(I):
    line = input().split()
    if line[0] == 'T':
        a = int(line[1])
        b = int(line[2])
        swap_positions(a, b)
        for i in range(1, N+1):
            if parent[i] == 0:
                dfs(i, 0, 0)
    else:
        e = int(line[1])
        mn = get_min_manager(e)
        if mn == -1 or mn == 10**9:
            print('*')
        else:
            print(mn)
