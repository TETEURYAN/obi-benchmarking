import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

N, E, S, M = data[0], data[1], data[2], data[3]

adj = [[] for _ in range(N)]
rev = [[] for _ in range(N)]
idx = 4
for _ in range(M):
    A = data[idx]
    B = data[idx + 1]
    T = data[idx + 2]
    idx += 3
    adj[A].append((B, T))
    rev[B].append((A, T))

INF = 10**18

dist = [[INF] * 3 for _ in range(N)]
in_queue = [[False] * 3 for _ in range(N)]
reachable = [[False] * 3 for _ in range(N)]

q = deque()
for r in range(3):
    dist[S][r] = 0
    reachable[S][r] = True
    q.append((S, r))

while q:
    u, r = q.popleft()
    for p, t in rev[u]:
        if t == 1:
            ok = (r == 0)
        else:
            ok = (r != 0)
        if not ok:
            continue
        pr = (r - 1) % 3
        if not reachable[p][pr]:
            reachable[p][pr] = True
            q.append((p, pr))

q = deque()
start_r = 0
if reachable[E][start_r]:
    dist[E][start_r] = 0
    q.append((E, start_r))
    in_queue[E][start_r] = True

while q:
    u, r = q.popleft()
    in_queue[u][r] = False
    cur = dist[u][r]
    nr = (r + 1) % 3
    for v, t in adj[u]:
        if t == 1:
            ok = (r == 0)
        else:
            ok = (r != 0)
        if not ok or not reachable[v][nr]:
            continue
        nd = cur + 1
        if nd < dist[v][nr]:
            dist[v][nr] = nd
            if not in_queue[v][nr]:
                q.append((v, nr))
                in_queue[v][nr] = True

ans = min(dist[S])
if ans >= INF:
    print('*')
else:
    print(ans)