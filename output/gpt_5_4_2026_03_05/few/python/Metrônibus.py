import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k1, k2, p = data[0], data[1], data[2], data[3]
idx = 4

metro = [[] for _ in range(n + 1)]
bus = [[] for _ in range(n + 1)]

for _ in range(k1):
    u = data[idx]
    v = data[idx + 1]
    idx += 2
    metro[u].append(v)
    metro[v].append(u)

for _ in range(k2):
    u = data[idx]
    v = data[idx + 1]
    idx += 2
    bus[u].append(v)
    bus[v].append(u)

a, b = data[idx], data[idx + 1]

INF = 10**18
dist = [INF] * (n + 1)
dist[a] = 0
q = deque([a])

while q:
    u = q.popleft()
    nd = dist[u] + 1

    if metro[u]:
        comp_nodes = []
        dq = deque([u])
        metro[u] = None
        while dq:
            x = dq.popleft()
            comp_nodes.append(x)
            for y in metro[x] if metro[x] is not None else ():
                if metro[y] is not None:
                    metro[y] = None
                    dq.append(y)
        for x in comp_nodes:
            if dist[x] == INF:
                dist[x] = nd
                q.append(x)

    if bus[u]:
        comp_nodes = []
        dq = deque([u])
        bus[u] = None
        while dq:
            x = dq.popleft()
            comp_nodes.append(x)
            for y in bus[x] if bus[x] is not None else ():
                if bus[y] is not None:
                    bus[y] = None
                    dq.append(y)
        for x in comp_nodes:
            if dist[x] == INF:
                dist[x] = nd
                q.append(x)

if dist[b] == INF:
    print(-1)
else:
    print(dist[b] * p)