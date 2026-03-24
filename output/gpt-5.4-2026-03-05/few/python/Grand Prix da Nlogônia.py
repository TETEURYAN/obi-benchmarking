import sys

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
plans = [None] * (m + 1)
p = 2
for i in range(1, m + 1):
    u = data[p]
    l = data[p + 1]
    r = data[p + 2]
    plans[i] = (u, l, r)
    p += 3

size = 1
while size < n:
    size <<= 1

seg_nodes = 2 * size
total_nodes = n + seg_nodes
base = n

seg_adj = [[] for _ in range(total_nodes + 1)]
for i in range(1, size):
    parent = base + i
    left = base + (i << 1)
    right = base + (i << 1 | 1)
    seg_adj[parent].append(left)
    seg_adj[parent].append(right)

for pos in range(1, n + 1):
    leaf = base + size + pos - 1
    seg_adj[leaf].append(pos)

def range_cover_nodes(l, r):
    res = []
    l = l + size - 1
    r = r + size - 1
    while l <= r:
        if l & 1:
            res.append(base + l)
            l += 1
        if not (r & 1):
            res.append(base + r)
            r -= 1
        l >>= 1
        r >>= 1
    return res

plan_nodes = [None] * (m + 1)
for i in range(1, m + 1):
    _, l, r = plans[i]
    plan_nodes[i] = range_cover_nodes(l, r)

def has_cycle(x):
    adj = [lst[:] for lst in seg_adj]
    for i in range(1, x + 1):
        u, _, _ = plans[i]
        for node in plan_nodes[i]:
            adj[u].append(node)

    state = bytearray(total_nodes + 1)

    for s in range(1, total_nodes + 1):
        if state[s]:
            continue
        stack = [(s, 0)]
        state[s] = 1
        while stack:
            v, it = stack[-1]
            if it < len(adj[v]):
                to = adj[v][it]
                stack[-1] = (v, it + 1)
                st = state[to]
                if st == 0:
                    state[to] = 1
                    stack.append((to, 0))
                elif st == 1:
                    return True
            else:
                state[v] = 2
                stack.pop()
    return False

if not has_cycle(m):
    print(-1)
    sys.exit()

lo, hi = 1, m
while lo < hi:
    mid = (lo + hi) >> 1
    if has_cycle(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)