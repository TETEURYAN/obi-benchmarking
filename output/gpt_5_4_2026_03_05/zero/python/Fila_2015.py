import sys
sys.setrecursionlimit(1_500_000)

class Node:
    __slots__ = ('val', 'prio', 'left', 'right', 'size', 'mx')
    def __init__(self, val, prio):
        self.val = val
        self.prio = prio
        self.left = None
        self.right = None
        self.size = 1
        self.mx = val

def sz(t):
    return t.size if t else 0

def mxv(t):
    return t.mx if t else -1

def upd(t):
    if t:
        t.size = 1 + sz(t.left) + sz(t.right)
        m = t.val
        if t.left and t.left.mx > m:
            m = t.left.mx
        if t.right and t.right.mx > m:
            m = t.right.mx
        t.mx = m

def split(t, k):
    if not t:
        return (None, None)
    if sz(t.left) >= k:
        a, b = split(t.left, k)
        t.left = b
        upd(t)
        return (a, t)
    else:
        a, b = split(t.right, k - sz(t.left) - 1)
        t.right = a
        upd(t)
        return (t, b)

def merge(a, b):
    if not a or not b:
        return a or b
    if a.prio > b.prio:
        a.right = merge(a.right, b)
        upd(a)
        return a
    else:
        b.left = merge(a, b.left)
        upd(b)
        return b

def kth(t, k):
    while t:
        ls = sz(t.left)
        if k <= ls:
            t = t.left
        elif k == ls + 1:
            return t.val
        else:
            k -= ls + 1
            t = t.right
    return None

def rightmost_greater(t, threshold, add):
    cur = t
    pos_add = add
    ans = 0
    while cur:
        if cur.right and cur.right.mx > threshold:
            pos_add += sz(cur.left) + 1
            cur = cur.right
        elif cur.val > threshold:
            ans = pos_add + sz(cur.left) + 1
            break
        else:
            cur = cur.left
    return ans

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

N = next(it)
A = [next(it) for _ in range(N)] if N > 0 else []
Q = next(it)

seed = 123456789
def rnd():
    global seed
    seed = (seed * 1103515245 + 12345) & 0x7fffffff
    return seed

root = None
for v in A:
    root = merge(root, Node(v, rnd()))

out = []

for _ in range(Q):
    T = next(it)
    I = next(it)
    X = next(it)
    if T == 0:
        newnode = Node(X, rnd())
        a, b = split(root, I)
        root = merge(merge(a, newnode), b)
    else:
        hi = kth(root, I)
        threshold = hi + X
        a, b = split(root, I - 1)
        ans = rightmost_greater(a, threshold, 0) if a and a.mx > threshold else 0
        out.append(str(ans))
        root = merge(a, b)

sys.stdout.write("\n".join(out))