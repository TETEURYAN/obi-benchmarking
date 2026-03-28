import sys
import random

sys.setrecursionlimit(2000000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

ptr = 0
N = data[ptr]
ptr += 1

initial = data[ptr:ptr + N]
ptr += N

Q = data[ptr]
ptr += 1

ops = []
all_heights = initial[:]
for _ in range(Q):
    t = data[ptr]
    i = data[ptr + 1]
    x = data[ptr + 2]
    ptr += 3
    ops.append((t, i, x))
    if t == 0:
        all_heights.append(x)

vals = sorted(set(all_heights))
comp = {v: i + 1 for i, v in enumerate(vals)}
M = len(vals)

class SegTree:
    __slots__ = ('n', 'tree')
    def __init__(self, n):
        size = 1
        while size < n:
            size <<= 1
        self.n = size
        self.tree = [0] * (size << 1)

    def update(self, pos, val):
        i = pos + self.n - 1
        if val > self.tree[i]:
            self.tree[i] = val
            i >>= 1
            while i:
                nv = self.tree[i << 1]
                rv = self.tree[i << 1 | 1]
                if rv > nv:
                    nv = rv
                if self.tree[i] == nv:
                    break
                self.tree[i] = nv
                i >>= 1

    def query_suffix(self, l):
        if l > self.n:
            return 0
        l = l + self.n - 1
        r = (self.n << 1) - 1
        res = 0
        while l <= r:
            if (l & 1) == 1:
                if self.tree[l] > res:
                    res = self.tree[l]
                l += 1
            if (r & 1) == 0:
                if self.tree[r] > res:
                    res = self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

seg = SegTree(M)

class Node:
    __slots__ = ('h', 'prio', 'l', 'r', 'sz', 'mx')
    def __init__(self, h):
        self.h = h
        self.prio = random.getrandbits(64)
        self.l = None
        self.r = None
        self.sz = 1
        self.mx = h

def sz(t):
    return t.sz if t else 0

def mx(t):
    return t.mx if t else 0

def upd(t):
    if t:
        t.sz = 1 + sz(t.l) + sz(t.r)
        m = t.h
        lm = mx(t.l)
        rm = mx(t.r)
        if lm > m:
            m = lm
        if rm > m:
            m = rm
        t.mx = m

def split(t, k):
    if not t:
        return (None, None)
    if sz(t.l) >= k:
        a, b = split(t.l, k)
        t.l = b
        upd(t)
        return (a, t)
    else:
        a, b = split(t.r, k - sz(t.l) - 1)
        t.r = a
        upd(t)
        return (t, b)

def merge(a, b):
    if not a or not b:
        return a or b
    if a.prio > b.prio:
        a.r = merge(a.r, b)
        upd(a)
        return a
    else:
        b.l = merge(a, b.l)
        upd(b)
        return b

def insert(root, pos, node):
    a, b = split(root, pos)
    return merge(merge(a, node), b)

def get_kth_height(t, k):
    while t:
        ls = sz(t.l)
        if k <= ls:
            t = t.l
        elif k == ls + 1:
            return t.h
        else:
            k -= ls + 1
            t = t.r
    return 0

def find_last_gt(t, threshold, add):
    if not t or t.mx <= threshold:
        return 0
    rr = t.r
    if rr and rr.mx > threshold:
        return find_last_gt(rr, threshold, add + sz(t.l) + 1)
    if t.h > threshold:
        return add + sz(t.l) + 1
    return find_last_gt(t.l, threshold, add)

root = None
for idx, h in enumerate(initial):
    root = insert(root, idx, Node(h))
    seg.update(comp[h], idx + 1)

out = []

for t, i, x in ops:
    if t == 0:
        root = insert(root, i, Node(x))
        seg.update(comp[x], i + 1)
    else:
        hi = get_kth_height(root, i)
        threshold = hi + x
        import bisect
        p = bisect.bisect_right(vals, threshold) + 1
        if p > M:
            out.append("0")
            continue
        cand = seg.query_suffix(p)
        if cand == 0 or cand >= i:
            out.append("0")
            continue
        a, b = split(root, i - 1)
        ans = find_last_gt(a, threshold, 0)
        root = merge(a, b)
        out.append(str(ans))

sys.stdout.write("\n".join(out))