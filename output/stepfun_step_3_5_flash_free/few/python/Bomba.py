import sys
from collections import deque

data = sys.stdin.read().split()
if not data:
    exit()
it = iter(data)
N = int(next(it)); E = int(next(it)); S = int(next(it)); M = int(next(it))
adj = [[] for _ in range(N)]
for _ in range(M):
    a = int(next(it)); b = int(next(it)); t = int(next(it))
    adj[a].append((b, t))
INF = 10**9
dist = [[INF]*3 for _ in range(N)]
dist[E][0] = 0
q = deque([(E, 0)])
while q:
    u, mod = q.popleft()
    d = dist[u][mod]
    for v, T in adj[u]:
        if T == 1:
            if mod != 0:
                continue
        else:
            if mod == 0:
                continue
        new_mod = (mod + 1) % 3
        if d + 1 < dist[v][new_mod]:
            dist[v][new_mod] = d + 1
            q.append((v, new_mod))
ans = min(dist[S])
print('*' if ans == INF else ans)