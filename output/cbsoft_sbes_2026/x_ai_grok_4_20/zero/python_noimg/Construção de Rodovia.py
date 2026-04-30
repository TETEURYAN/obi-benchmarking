
import sys
sys.setrecursionlimit(10**6)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px = find(parent, x)
    py = find(parent, y)
    if px != py:
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1
        return True
    return False

N, M = map(int, input().split())
edges = []
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    edges.append((x, y))
    adj[x].append(y)
    adj[y].append(x)

parent = list(range(N+1))
rank = [0] * (N+1)
components = []
comp_id = [-1] * (N+1)
cid = 0
size = []

for i in range(1, N+1):
    if find(parent, i) == i:
        components.append([])
        comp_id[i] = cid
        size.append(0)
        cid += 1

for i in range(1, N+1):
    root = find(parent, i)
    if comp_id[root] == -1:
        comp_id[root] = len(components)
        components.append([])
        size.append(0)
    cid = comp_id[root]
    components[cid].append(i)
    size[cid] += 1
    comp_id[i] = cid

bridges = []
disc = [-1] * (N+1)
low = [-1] * (N+1)
time = 0
parent_bridge = [-1] * (N+1)

def dfs(u):
    global time
    disc[u] = low[u] = time
    time += 1
    for v in adj[u]:
        if disc[v] == -1:
            parent_bridge[v] = u
            dfs(v)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                bridges.append((min(u,v), max(u,v)))
        elif v != parent_bridge[u]:
            low[u] = min(low[u], disc[v])

for i in range(1, N+1):
    if disc[i] == -1:
        dfs(i)

bridge_set = set(bridges)

non_bridge_edges = []
for u, v in edges:
    if (min(u,v), max(u,v)) not in bridge_set:
        non_bridge_edges.append((u, v))

parent = list(range(N+1))
rank = [0] * (N+1)
for u, v in non_bridge_edges:
    union(parent, rank, u, v)

comp = {}
cid = 0
comp_list = []
comp_size = []
node_to_comp = [-1] * (N+1)

for i in range(1, N+1):
    p = find(parent, i)
    if p not in comp:
        comp[p] = cid
        comp_list.append([])
        comp_size.append(0)
        cid += 1
    c = comp[p]
    comp_list[c].append(i)
    comp_size[c] += 1
    node_to_comp[i] = c

if len(comp_size) == 1:
    print(-1)
    sys.exit(0)

tree_adj = [[] for _ in range(len(comp_size))]
bridge_to_comps = {}

for u, v in bridges:
    cu = node_to_comp[u]
    cv = node_to_comp[v]
    if cu != cv:
        tree_adj[cu].append(cv)
        tree_adj[cv].append(cu)
        bridge_to_comps[(min(cu,cv), max(cu,cv))] = (u, v)

leaves = [i for i in range(len(comp_size)) if len(tree_adj[i]) == 1]
if not leaves:
    print(-1)
    sys.exit(0)

leaf = leaves[0]
target_comp = -1
for nei in tree_adj[leaf]:
    target_comp = nei
    break

if comp_size[leaf] >= 2:
    a = comp_list[leaf][0]
    b = comp_list[leaf][1]
    if (min(a,b), max(a,b)) not in bridge_set:
        print(a, b)
        sys.exit(0)

if comp_size[target_comp] >= 2:
    a = comp_list[target_comp][0]
    b = comp_list[target_comp][1]
    if (min(a,b), max(a,b)) not in bridge_set:
        print(a, b)
        sys.exit(0)

a = comp_list[leaf][0]
b = comp_list[target_comp][0]
if (min(a,b), max(a,b)) not in bridge_set:
    print(a, b)
else:
    print(-1)
