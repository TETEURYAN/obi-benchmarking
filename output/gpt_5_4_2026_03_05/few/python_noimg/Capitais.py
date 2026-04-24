import sys
from collections import deque

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit()

n = int(data[0])
adj = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)

idx = 1
for _ in range(n - 1):
    u = int(data[idx])
    v = int(data[idx + 1])
    idx += 2
    adj[u].append(v)
    adj[v].append(u)
    deg[u] += 1
    deg[v] += 1

if n == 2:
    print(1)
    sys.exit()

dist = [-1] * (n + 1)
q = deque()

for i in range(1, n + 1):
    if deg[i] == 1:
        dist[i] = 0
        q.append(i)

ans = 10**18

while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
        else:
            if dist[v] >= dist[u]:
                cand = dist[u] + dist[v] + 1
                if cand < ans:
                    ans = cand

print(ans)