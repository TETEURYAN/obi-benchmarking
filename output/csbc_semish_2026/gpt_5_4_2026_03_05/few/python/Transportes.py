import sys
import heapq

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = 0
N = data[it]
it += 1
M = data[it]
it += 1
K = data[it]
it += 1

P = [0] + data[it:it + K]
it += K

station_systems = [[] for _ in range(N + 1)]
pair_to_id = {}
next_id = N + 1

for _ in range(M):
    u = data[it]
    v = data[it + 1]
    t = data[it + 2]
    it += 3

    key1 = (u, t)
    node1 = pair_to_id.get(key1)
    if node1 is None:
        node1 = next_id
        next_id += 1
        pair_to_id[key1] = node1
        station_systems[u].append((t, node1))

    key2 = (v, t)
    node2 = pair_to_id.get(key2)
    if node2 is None:
        node2 = next_id
        next_id += 1
        pair_to_id[key2] = node2
        station_systems[v].append((t, node2))

A = data[it]
B = data[it + 1]

total_nodes = next_id - 1
adj = [[] for _ in range(total_nodes + 1)]

for (s, t), node in pair_to_id.items():
    cost = P[t]
    adj[s].append((node, cost))
    adj[node].append((s, 0))

it2 = 0
for s in range(1, N + 1):
    lst = station_systems[s]
    if len(lst) <= 1:
        continue
    base = next_id
    next_id += len(lst)
    total_nodes = next_id - 1
    adj.extend([[] for _ in range(len(lst))])
    for _, node in lst:
        aux = base + it2
        it2 += 1
        adj[node].append((aux, 0))
        adj[aux].append((node, 0))
        adj[s].append((aux, 0))
        adj[aux].append((s, 0))
    it2 = 0

INF = 10**30
dist = [INF] * (len(adj))
dist[A] = 0
pq = [(0, A)]

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    if u == B:
        print(d)
        sys.exit()
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(-1)