import sys

data = sys.stdin.read().split()
idx = 0
N = int(data[idx])
idx += 1
adj = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    line = data[idx]
    idx += 1
    for j in range(1, N + 1):
        if line[j - 1] == '1':
            adj[i].append(j)
E = int(data[idx])
idx += 1

component = [0] * (N + 1)
visited = [False] * (N + 1)
comp_id = 0

def dfs(node, cid):
    stack = [node]
    visited[node] = True
    component[node] = cid
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                component[v] = cid
                stack.append(v)

for i in range(1, N + 1):
    if not visited[i]:
        comp_id += 1
        dfs(i, comp_id)

for _ in range(E):
    K = int(data[idx])
    idx += 1
    candidates = []
    for _ in range(K):
        c = int(data[idx])
        idx += 1
        candidates.append(c)
    comps = set()
    has_friend = False
    for c in candidates:
        cid = component[c]
        if cid in comps:
            has_friend = True
            break
        comps.add(cid)
    if has_friend:
        print('S')
    else:
        print('N')