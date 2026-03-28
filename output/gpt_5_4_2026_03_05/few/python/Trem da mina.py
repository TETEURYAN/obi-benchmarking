import sys
sys.setrecursionlimit(200000)

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

it = iter(data)
E = next(it)
R = next(it)

adj = [[] for _ in range(E + 1)]
edges = []
for eid in range(R):
    a = next(it)
    b = next(it)
    c = next(it)
    edges.append((a, b, c))
    adj[a].append((b, c, eid))
    adj[b].append((a, c, eid))

K = next(it)
queries = [(next(it), next(it)) for _ in range(K)]

disc = [0] * (E + 1)
low = [0] * (E + 1)
parent = [-1] * (E + 1)
parent_edge = [-1] * (E + 1)
is_bridge = [False] * R
time = 0

def dfs_bridge(u):
    global time
    time += 1
    disc[u] = low[u] = time
    for v, w, eid in adj[u]:
        if eid == parent_edge[u]:
            continue
        if disc[v] == 0:
            parent[v] = u
            parent_edge[v] = eid
            dfs_bridge(v)
            if low[v] > disc[u]:
                is_bridge[eid] = True
            if low[v] < low[u]:
                low[u] = low[v]
        else:
            if disc[v] < low[u]:
                low[u] = disc[v]

for s in range(1, E + 1):
    if disc[s] == 0:
        dfs_bridge(s)

comp_id = [-1] * (E + 1)
comps = []
for s in range(1, E + 1):
    if comp_id[s] != -1:
        continue
    cid = len(comps)
    stack = [s]
    comp_id[s] = cid
    verts = []
    while stack:
        u = stack.pop()
        verts.append(u)
        for v, w, eid in adj[u]:
            if is_bridge[eid]:
                continue
            if comp_id[v] == -1:
                comp_id[v] = cid
                stack.append(v)
    comps.append(verts)

comp_size = [len(vs) for vs in comps]
cycle_len = [0] * len(comps)
in_cycle = [False] * (E + 1)
pos_in_cycle = [-1] * (E + 1)

for cid, verts in enumerate(comps):
    if len(verts) == 1:
        continue
    deg2 = True
    total = 0
    for u in verts:
        cnt = 0
        for v, w, eid in adj[u]:
            if not is_bridge[eid] and comp_id[v] == cid:
                cnt += 1
                total += w
        if cnt != 2:
            deg2 = False
            break
    if deg2:
        cycle_len[cid] = total // 2
        for idx2, u in enumerate(verts):
            in_cycle[u] = True
            pos_in_cycle[u] = idx2

tree_adj = [[] for _ in range(E + 1)]
for eid, (a, b, c) in enumerate(edges):
    if is_bridge[eid]:
        tree_adj[a].append((b, c))
        tree_adj[b].append((a, c))

visited = [False] * (E + 1)
dist_to_cycle = [0] * (E + 1)
root_cycle = [-1] * (E + 1)

for s in range(1, E + 1):
    if in_cycle[s]:
        visited[s] = True
        root_cycle[s] = s

for s in range(1, E + 1):
    if in_cycle[s]:
        stack = [(s, 0)]
        while stack:
            u, p = stack.pop()
            for v, w in tree_adj[u]:
                if v == p or visited[v]:
                    continue
                visited[v] = True
                dist_to_cycle[v] = dist_to_cycle[u] + w
                root_cycle[v] = root_cycle[u]
                stack.append((v, u))

for s in range(1, E + 1):
    if not visited[s]:
        stack = [(s, 0)]
        visited[s] = True
        root_cycle[s] = -1
        while stack:
            u, p = stack.pop()
            for v, w in tree_adj[u]:
                if v == p or visited[v]:
                    continue
                visited[v] = True
                dist_to_cycle[v] = dist_to_cycle[u] + w
                root_cycle[v] = -1
                stack.append((v, u))

ans = []
for x, t in queries:
    if in_cycle[x]:
        cid = comp_id[x]
        L = cycle_len[cid]
        if t <= L:
            ans.append(str(L))
        else:
            ans.append("-1")
    else:
        rc = root_cycle[x]
        if rc == -1:
            ans.append("-1")
        else:
            cid = comp_id[rc]
            L = cycle_len[cid]
            need = 2 * dist_to_cycle[x] + L
            if t <= need:
                ans.append(str(need))
            else:
                ans.append("-1")

sys.stdout.write("\n".join(ans))