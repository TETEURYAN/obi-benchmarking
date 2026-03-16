import sys

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

n = next(it)
parent = [0] * (n + 1)
children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    p = next(it)
    parent[i] = p
    children[p].append(i)

tin = [0] * (n + 1)
tout = [0] * (n + 1)
depth0 = [0] * (n + 1)
order = [0] * (n + 1)

timer = 0
stack = [(1, 0)]
while stack:
    v, state = stack.pop()
    if state == 0:
        timer += 1
        tin[v] = timer
        order[timer] = v
        stack.append((v, 1))
        for u in reversed(children[v]):
            depth0[u] = depth0[v] + 1
            stack.append((u, 0))
    else:
        tout[v] = timer

q = next(it)
ops = []
queries = []
for _ in range(q):
    t = next(it)
    if t == 1:
        v = next(it)
        k = next(it)
        ops.append((1, v, k))
        queries.append((v, k))
    else:
        v = next(it)
        ops.append((2, v))

m = len(queries)
if m == 0:
    sys.exit(0)

vals = []
for v, k in queries:
    vals.append(depth0[v] - k)
vals = sorted(set(vals))
comp = {x: i + 1 for i, x in enumerate(vals)}
M = len(vals)

class BIT:
    __slots__ = ("n", "bit")
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)
    def add(self, i, v):
        n = self.n
        bit = self.bit
        while i <= n:
            bit[i] += v
            i += i & -i
    def sum(self, i):
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

bit = BIT(M)
ans = []
for op in reversed(ops):
    if op[0] == 1:
        _, v, k = op
        target = depth0[v] - k
        idx = comp[target]
        x = bit.sum(idx)
        cur_depth = depth0[v] - x
        need = cur_depth - k
        l, r = tin[v], tout[v]
        while l < r:
            mid = (l + r) >> 1
            u = order[mid]
            val = depth0[u] - bit.sum(comp[depth0[u]])
            if val >= need:
                r = mid
            else:
                l = mid + 1
        ans.append(order[l])
    else:
        _, v = op
        d = depth0[v]
        idx = comp[d]
        bit.add(idx, 1)

sys.stdout.write("\n".join(map(str, reversed(ans))))