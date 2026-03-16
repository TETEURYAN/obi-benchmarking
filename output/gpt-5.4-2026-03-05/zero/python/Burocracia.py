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
    ujm = up[j - 1]
    for v in range(1, N + 1):
        uj[v] = ujm[ujm[v]]

def kth_ancestor(v, k):
    b = 0
    while k:
        if k & 1:
            v = up[b][v]
        k >>= 1
        b += 1
    return v

class SegTree:
    def __init__(self, n):
        self.n = n
        size = 4 * n + 5
        self.mx = [0] * size
        self.tag = [0] * size

    def _apply(self, idx, val):
        if val > self.mx[idx]:
            self.mx[idx] = val
        if val > self.tag[idx]:
            self.tag[idx] = val

    def _push(self, idx):
        t = self.tag[idx]
        if t:
            self._apply(idx << 1, t)
            self._apply(idx << 1 | 1, t)
            self.tag[idx] = 0

    def chmax(self, ql, qr, val, idx=1, l=1, r=None):
        if r is None:
            r = self.n
        if ql <= l and r <= qr:
            self._apply(idx, val)
            return
        self._push(idx)
        m = (l + r) >> 1
        if ql <= m:
            self.chmax(ql, qr, val, idx << 1, l, m)
        if qr > m:
            self.chmax(ql, qr, val, idx << 1 | 1, m + 1, r)
        self.mx[idx] = self.mx[idx << 1] if self.mx[idx << 1] > self.mx[idx << 1 | 1] else self.mx[idx << 1 | 1]

    def query(self, pos, idx=1, l=1, r=None):
        if r is None:
            r = self.n
        if l == r:
            return self.mx[idx]
        self._push(idx)
        m = (l + r) >> 1
        if pos <= m:
            return self.query(pos, idx << 1, l, m)
        return self.query(pos, idx << 1 | 1, m + 1, r)

seg = SegTree(N)

Q = int(input())
out = []

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 2:
        v = op[1]
        if tin[v] < tout[v]:
            seg.chmax(tin[v] + 1, tout[v], depth0[v])
    else:
        v, k = op[1], op[2]
        d = seg.query(tin[v])
        target_depth = d + k - 1
        ans = kth_ancestor(v, depth0[v] - target_depth)
        out.append(str(ans))

sys.stdout.write("\n".join(out))