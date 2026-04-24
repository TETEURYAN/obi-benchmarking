import sys
sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj = [[] for _ in range(n + 1)]
radj = [[] for _ in range(n + 1)]
edges = []
edge_set = set()

idx = 2
for _ in range(m):
    u = data[idx]
    v = data[idx + 1]
    idx += 2
    adj[u].append(v)
    radj[v].append(u)
    edges.append((u, v))
    edge_set.add((u, v))

visited = [False] * (n + 1)
order = []

for s in range(1, n + 1):
    if visited[s]:
        continue
    stack = [(s, 0)]
    visited[s] = True
    while stack:
        u, it = stack[-1]
        if it < len(adj[u]):
            v = adj[u][it]
            stack[-1] = (u, it + 1)
            if not visited[v]:
                visited[v] = True
                stack.append((v, 0))
        else:
            order.append(u)
            stack.pop()

comp = [-1] * (n + 1)
cid = 0

for s in reversed(order):
    if comp[s] != -1:
        continue
    stack = [s]
    comp[s] = cid
    while stack:
        u = stack.pop()
        for v in radj[u]:
            if comp[v] == -1:
                comp[v] = cid
                stack.append(v)
    cid += 1

k = cid

if k == 1:
    total_possible = n * (n - 1)
    if m < total_possible:
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a != b and (a, b) not in edge_set:
                    print(a, b)
                    sys.exit()
    print(-1)
    sys.exit()

members = [[] for _ in range(k)]
for v in range(1, n + 1):
    members[comp[v]].append(v)

dag = [[] for _ in range(k)]
indeg = [0] * k
outdeg = [0] * k
dag_edge_set = set()

for u, v in edges:
    cu = comp[u]
    cv = comp[v]
    if cu != cv and (cu, cv) not in dag_edge_set:
        dag_edge_set.add((cu, cv))
        dag[cu].append(cv)
        indeg[cv] += 1
        outdeg[cu] += 1

sources = [i for i in range(k) if indeg[i] == 0]
sinks = [i for i in range(k) if outdeg[i] == 0]

if len(sources) != 1 or len(sinks) != 1:
    print(-1)
    sys.exit()

source = sources[0]
sink = sinks[0]

topo = []
q = sources[:]
ptr = 0
while ptr < len(q):
    u = q[ptr]
    ptr += 1
    topo.append(u)
    for v in dag[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

dp = [0] * k
dp[source] = 1
for u in topo:
    val = dp[u]
    if val == 0:
        continue
    for v in dag[u]:
        nv = val + dp[v]
        if nv >= 2:
            dp[v] = 2
        else:
            dp[v] = nv

if dp[sink] != 1:
    print(-1)
    sys.exit()

cur = source
path = [cur]
while cur != sink:
    nxt = -1
    for v in dag[cur]:
        if dp[v] == 1:
            nxt = v
            break
    if nxt == -1:
        print(-1)
        sys.exit()
    cur = nxt
    path.append(cur)

if len(path) == k:
    print(-1)
    sys.exit()

in_path = [False] * k
for c in path:
    in_path[c] = True

for i in range(len(path) - 1):
    a = path[i]
    b = path[i + 1]
    if len(dag[a]) != 1 or dag[a][0] != b:
        u = members[a][0]
        v = members[b][0]
        if (u, v) not in edge_set:
            print(u, v)
            sys.exit()

for c in range(k):
    if not in_path[c]:
        u = members[source][0]
        v = members[c][0]
        if (u, v) not in edge_set:
            print(u, v)
            sys.exit()
        u = members[c][0]
        v = members[sink][0]
        if (u, v) not in edge_set:
            print(u, v)
            sys.exit()

print(-1)