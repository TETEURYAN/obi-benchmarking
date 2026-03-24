import sys

sys.setrecursionlimit(2000000)
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, k = data[0], data[1]

adj = [[] for _ in range(n + 1)]
idx = 2
for _ in range(n - 1):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    adj[a].append(b)
    adj[b].append(a)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
order = []

stack = [1]
parent[1] = -1
while stack:
    u = stack.pop()
    order.append(u)
    for v in adj[u]:
        if v != parent[u]:
            parent[v] = u
            depth[v] = depth[u] + 1
            stack.append(v)

max_log = (n).bit_length()
up = [[0] * (n + 1) for _ in range(max_log)]
for v in range(1, n + 1):
    p = parent[v]
    up[0][v] = 0 if p == -1 else p

for j in range(1, max_log):
    prev = up[j - 1]
    cur = up[j]
    for v in range(1, n + 1):
        cur[v] = prev[prev[v]]

order_by_depth = sorted(range(1, n + 1), key=lambda x: depth[x], reverse=True)

def ancestor(v, dist):
    bit = 0
    while dist:
        if dist & 1:
            v = up[bit][v]
            if v == 0:
                return 1
        dist >>= 1
        bit += 1
    return v

def can_cover(R):
    covered = [False] * (n + 1)
    centers = 0

    for u in order_by_depth:
        if covered[u]:
            continue
        if depth[u] <= R:
            continue

        c = ancestor(u, R)
        centers += 1
        if centers > k:
            return False

        stack = [(c, 0, parent[c])]
        while stack:
            x, d, p = stack.pop()
            if covered[x]:
                continue
            covered[x] = True
            if d == R:
                continue
            for y in adj[x]:
                if y != p:
                    stack.append((y, d + 1, x))

    for u in range(1, n + 1):
        if not covered[u]:
            centers += 1
            if centers > k:
                return False
    return True

lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if can_cover(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)