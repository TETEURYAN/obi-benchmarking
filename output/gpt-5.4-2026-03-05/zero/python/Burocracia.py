import sys

sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

N = int(input())
par = [0] * (N + 1)
tmp = list(map(int, input().split()))
children = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    par[i] = tmp[i - 2]
    children[par[i]].append(i)

tin = [0] * (N + 1)
tout = [0] * (N + 1)
depth0 = [0] * (N + 1)
order = [0] * (N + 1)
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

LOG = (N + 1).bit_length()
up = [[0] * (N + 1) for _ in range(LOG)]
for v in range(1, N + 1):
    up[0][v] = par[v]
for j in range(1, LOG):
    uj = up[j]
    prev = up[j - 1]
    for v in range(1, N + 1):
        uj[v] = prev[prev[v]]

def lca(a, b):
    if depth0[a] < depth0[b]:
        a, b = b, a
    diff = depth0[a] - depth0[b]
    bit = 0
    while diff:
        if diff & 1:
            a = up[bit][a]
        diff >>= 1
        bit += 1
    if a == b:
        return a
    for j in range(LOG - 1, -1, -1):
        if up[j][a] != up[j][b]:
            a = up[j][a]
            b = up[j][b]
    return par[a]

class SegTree:
    def __init__(self, n):
        self.n = n
        self.mn = [0] * (4 * n)
        self.mx = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self._build(1, 1, n)

    def _build(self, idx, l, r):
        if l == r:
            v = order[l]
            self.mn[idx] = v
            self.mx[idx] = v
            return
        m = (l + r) >> 1
        self._build(idx << 1, l, m)
        self._build(idx << 1 | 1, m + 1, r)
        self.mn[idx] = min(self.mn[idx << 1], self.mn[idx << 1 | 1])
        self.mx[idx] = max(self.mx[idx << 1], self.mx[idx << 1 | 1])

    def _apply(self, idx, val):
        self.mn[idx] = val
        self.mx[idx] = val
        self.lazy[idx] = val

    def _push(self, idx):
        val = self.lazy[idx]
        if val:
            self._apply(idx << 1, val)
            self._apply(idx << 1 | 1, val)
            self.lazy[idx] = 0

    def assign(self, ql, qr, val):
        self._assign(1, 1, self.n, ql, qr, val)

    def _assign(self, idx, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self._apply(idx, val)
            return
        self._push(idx)
        m = (l + r) >> 1
        if ql <= m:
            self._assign(idx << 1, l, m, ql, qr, val)
        if m < qr:
            self._assign(idx << 1 | 1, m + 1, r, ql, qr, val)
        self.mn[idx] = min(self.mn[idx << 1], self.mn[idx << 1 | 1])
        self.mx[idx] = max(self.mx[idx << 1], self.mx[idx << 1 | 1])

    def query_min(self, ql, qr):
        return self._query_min(1, 1, self.n, ql, qr)

    def _query_min(self, idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.mn[idx]
        self._push(idx)
        m = (l + r) >> 1
        res = 10**18
        if ql <= m:
            res = min(res, self._query_min(idx << 1, l, m, ql, qr))
        if m < qr:
            res = min(res, self._query_min(idx << 1 | 1, m + 1, r, ql, qr))
        return res

    def query_max(self, ql, qr):
        return self._query_max(1, 1, self.n, ql, qr)

    def _query_max(self, idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.mx[idx]
        self._push(idx)
        m = (l + r) >> 1
        res = 0
        if ql <= m:
            res = max(res, self._query_max(idx << 1, l, m, ql, qr))
        if m < qr:
            res = max(res, self._query_max(idx << 1 | 1, m + 1, r, ql, qr))
        return res

seg = SegTree(N)

Q = int(input())
out = []

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 2:
        v = op[1]
        if tin[v] + 1 <= tout[v]:
            seg.assign(tin[v] + 1, tout[v], v)
    else:
        v, k = op[1], op[2]
        cur = v
        while k > 0:
            l, r = tin[cur], tout[cur]
            mn = seg.query_min(l, r)
            mx = seg.query_max(l, r)
            if mn == mx:
                anc = mn
            else:
                anc = lca(mn, mx)
            d = depth0[cur] - depth0[anc]
            if d == 0:
                cur = anc
                continue
            if d >= k:
                x = cur
                need = k
                bit = 0
                while need:
                    if need & 1:
                        x = up[bit][x]
                    need >>= 1
                    bit += 1
                cur = x
                k = 0
            else:
                cur = anc
                k -= d
        out.append(str(cur))

sys.stdout.write("\n".join(out))