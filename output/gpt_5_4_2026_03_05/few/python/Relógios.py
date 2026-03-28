import sys
import heapq

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

L, C, K = data[0], data[1], data[2]
grid = []
idx = 3
for _ in range(L):
    grid.append(data[idx:idx + C])
    idx += C

INF = 10**30
n = L * C

def vid(r, c):
    return r * C + c

dist = [INF] * n
start = 0
target = n - 1

if target == start:
    print(0)
    sys.exit()

dist[start] = 0
pq = [(0, start)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while pq:
    t, u = heapq.heappop(pq)
    if t != dist[u]:
        continue
    if u == target:
        print(t)
        sys.exit()

    r = u // C
    c = u % C

    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= L or nc < 0 or nc >= C:
            continue

        v = vid(nr, nc)
        p = grid[nr][nc]
        nt = t + 1

        if p == -1:
            if nt < dist[v]:
                dist[v] = nt
                heapq.heappush(pq, (nt, v))
        else:
            rem = nt % K
            wait = (p - rem) % K
            nt2 = nt + wait
            if nt2 < dist[v]:
                dist[v] = nt2
                heapq.heappush(pq, (nt2, v))

print(-1)