import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

N, M = data[0], data[1]
Xe, Ye = data[2], data[3]
Xs, Ys = data[4], data[5]

Xe -= 1
Ye -= 1
Xs -= 1
Ys -= 1

cells = [(i, j) for i in range(N) for j in range(M)]
idx_of = {(i, j): i * M + j for i, j in cells}
total_cells = N * M

base_blocked = 0
cabinets = []
for i in range(1, N, 2):
    for j in range(1, M, 2):
        c = idx_of[(i, j)]
        opts = []
        if j + 1 < M:
            opts.append((1 << c) | (1 << idx_of[(i, j + 1)]))
        if j - 1 >= 0:
            opts.append((1 << c) | (1 << idx_of[(i, j - 1)]))
        if i + 1 < N:
            opts.append((1 << c) | (1 << idx_of[(i + 1, j)]))
        if i - 1 >= 0:
            opts.append((1 << c) | (1 << idx_of[(i - 1, j)]))
        cabinets.append(opts)
        base_blocked |= (1 << c)

s = idx_of[(Xe, Ye)]
t = idx_of[(Xs, Ys)]

neighbors = [[] for _ in range(total_cells)]
for i in range(N):
    for j in range(M):
        u = idx_of[(i, j)]
        if i > 0:
            neighbors[u].append(idx_of[(i - 1, j)])
        if i + 1 < N:
            neighbors[u].append(idx_of[(i + 1, j)])
        if j > 0:
            neighbors[u].append(idx_of[(i, j - 1)])
        if j + 1 < M:
            neighbors[u].append(idx_of[(i, j + 1)])

def shortest_path_len(blocked):
    if (blocked >> s) & 1 or (blocked >> t) & 1:
        return -1
    dist = [-1] * total_cells
    q = deque([s])
    dist[s] = 1
    while q:
        u = q.popleft()
        if u == t:
            return dist[u]
        for v in neighbors[u]:
            if dist[v] == -1 and ((blocked >> v) & 1) == 0:
                dist[v] = dist[u] + 1
                q.append(v)
    return -1

best = -1
seen = {}

def dfs(k, blocked):
    global best
    key = (k, blocked)
    prev = seen.get(key)
    if prev is not None and prev >= best:
        return
    seen[key] = best

    if k == len(cabinets):
        d = shortest_path_len(blocked)
        if d > best:
            best = d
        return

    for mask in cabinets[k]:
        dfs(k + 1, blocked | mask)

dfs(0, 0)
print(best)