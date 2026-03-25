import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, a, b = data[0], data[1], data[2]

adj = [[] for _ in range(n + 1)]
idx = 3
for _ in range(n - 1):
    p = data[idx]
    q = data[idx + 1]
    adj[p].append(q)
    adj[q].append(p)
    idx += 2

dist = [-1] * (n + 1)
dist[a] = 0
dq = deque([a])

while dq:
    u = dq.popleft()
    if u == b:
        break
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            dq.append(v)

print(dist[b])