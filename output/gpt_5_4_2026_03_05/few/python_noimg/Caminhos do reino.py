import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

it = 0
n = data[it]
it += 1

f = [0] * (n + 1)
indeg = [0] * (n + 1)
rev = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    to = data[it]
    it += 1
    f[i] = to
    indeg[to] += 1
    rev[to].append(i)

from collections import deque

q = deque()
removed = [False] * (n + 1)
for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)

while q:
    u = q.popleft()
    removed[u] = True
    v = f[u]
    indeg[v] -= 1
    if indeg[v] == 0:
        q.append(v)

on_cycle = [False] * (n + 1)
cycle_nodes = []
for i in range(1, n + 1):
    if not removed[i]:
        on_cycle[i] = True
        cycle_nodes.append(i)

cycle_order = []
start = cycle_nodes[0]
u = start
pos = [-1] * (n + 1)
while True:
    pos[u] = len(cycle_order)
    cycle_order.append(u)
    u = f[u]
    if u == start:
        break

m = len(cycle_order)

root = [0] * (n + 1)
depth = [0] * (n + 1)
LOG = (n).bit_length()
up = [[0] * (n + 1) for _ in range(LOG)]

dq = deque()
for c in cycle_order:
    root[c] = c
    depth[c] = 0
    up[0][c] = 0
    dq.append(c)

while dq:
    u = dq.popleft()
    for v in rev[u]:
        if on_cycle[v]:
            continue
        root[v] = root[u]
        depth[v] = depth[u] + 1
        up[0][v] = u
        dq.append(v)

for k in range(1, LOG):
    prev = up[k - 1]
    curr = up[k]
    for i in range(1, n + 1):
        p = prev[i]
        curr[i] = prev[p] if p else 0

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    bit = 0
    while diff:
        if diff & 1:
            a = up[bit][a]
        diff >>= 1
        bit += 1
    if a == b:
        return a
    for k in range(LOG - 1, -1, -1):
        if up[k][a] != up[k][b]:
            a = up[k][a]
            b = up[k][b]
    return up[0][a]

def cycle_dist(i, j):
    d = pos[j] - pos[i]
    if d < 0:
        d += m
    return d

out = []
Q = data[it]
it += 1

for _ in range(Q):
    a = data[it]
    b = data[it + 1]
    it += 2

    if root[a] == root[b]:
        c = lca(a, b)
        out.append(str(max(depth[a] - depth[c], depth[b] - depth[c])))
    else:
        da = depth[a]
        db = depth[b]
        ra = root[a]
        rb = root[b]
        d1 = cycle_dist(ra, rb)
        d2 = cycle_dist(rb, ra)
        out.append(str(min(max(da + d1, db), max(da, db + d2))))

sys.stdout.write("\n".join(out))