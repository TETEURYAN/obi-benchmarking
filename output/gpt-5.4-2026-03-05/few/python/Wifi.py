import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
rects = []
idx = 1
for i in range(n):
    x1 = data[idx]
    y1 = data[idx + 1]
    x2 = data[idx + 2]
    y2 = data[idx + 3]
    rects.append((x1, y1, x2, y2, i))
    idx += 4

events = []
for x1, y1, x2, y2, i in rects:
    events.append((x1, 0, -y1, y2, i))
    events.append((x2, 1, -y1, y2, i))

events.sort()

INF = 10**30

class TreapNode:
    __slots__ = ('key', 'prio', 'left', 'right')
    def __init__(self, key, prio):
        self.key = key
        self.prio = prio
        self.left = None
        self.right = None

seed = 123456789

def rng():
    global seed
    seed = (seed * 1103515245 + 12345) & 0x7fffffff
    return seed

def rotate_right(p):
    q = p.left
    p.left = q.right
    q.right = p
    return q

def rotate_left(p):
    q = p.right
    p.right = q.left
    q.left = p
    return q

def insert(root, key):
    if root is None:
        return TreapNode(key, rng())
    if key < root.key:
        root.left = insert(root.left, key)
        if root.left.prio < root.prio:
            root = rotate_right(root)
    else:
        root.right = insert(root.right, key)
        if root.right.prio < root.prio:
            root = rotate_left(root)
    return root

def erase(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = erase(root.left, key)
    elif key > root.key:
        root.right = erase(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        if root.left.prio < root.right.prio:
            root = rotate_right(root)
            root.right = erase(root.right, key)
        else:
            root = rotate_left(root)
            root.left = erase(root.left, key)
    return root

def predecessor(root, key):
    res = None
    while root is not None:
        if key <= root.key:
            root = root.left
        else:
            res = root.key
            root = root.right
    return res

root = None
parent = [-1] * n

for x, typ, ny1, y2, i in events:
    key = (ny1, y2, i)
    if typ == 0:
        pkey = predecessor(root, key)
        if pkey is not None:
            parent[i] = pkey[2]
        root = insert(root, key)
    else:
        root = erase(root, key)

children = [[] for _ in range(n)]
root_id = -1
for i in range(n):
    if parent[i] == -1:
        root_id = i
    else:
        children[parent[i]].append(i)

dp0 = [0] * n
dp1 = [0] * n
stack = [(root_id, 0)]
order = []
while stack:
    u, state = stack.pop()
    if state == 0:
        stack.append((u, 1))
        for v in children[u]:
            stack.append((v, 0))
    else:
        s0 = 0
        s1 = 1
        for v in children[u]:
            s0 += dp1[v]
            a = dp0[v]
            b = dp1[v]
            s1 += a if a < b else b
        dp0[u] = s0
        dp1[u] = s1

print(dp1[root_id])