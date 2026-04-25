import sys

sys.setrecursionlimit(200000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = 0
n = data[it]
it += 1
b = data[it]
it += 1

edges = []
for _ in range(b):
    u = data[it]
    v = data[it + 1]
    w = data[it + 2]
    it += 3
    edges.append((w, u, v))

edges.sort(reverse=True)

parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

mst = [[] for _ in range(n + 1)]
added = 0

for w, u, v in edges:
    ru = find(u)
    rv = find(v)
    if ru != rv:
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
        mst[u].append((v, w))
        mst[v].append((u, w))
        added += 1
        if added == n - 1:
            break

LOG = (n).bit_length()
up = [[0] * (n + 1) for _ in range(LOG)]
mn = [[10**18] * (n + 1) for _ in range(LOG)]
depth = [0] * (n + 1)

stack = [1]
visited = [False] * (n + 1)
visited[1] = True

while stack:
    u = stack.pop()
    for v, w in mst[u]:
        if not visited[v]:
            visited[v] = True
            depth[v] = depth[u] + 1
            up[0][v] = u
            mn[0][v] = w
            stack.append(v)

for k in range(1, LOG):
    upk = up[k]
    upkm1 = up[k - 1]
    mnk = mn[k]
    mnkm1 = mn[k - 1]
    for v in range(1, n + 1):
        mid = upkm1[v]
        upk[v] = upkm1[mid]
        a = mnkm1[v]
        b2 = mnkm1[mid]
        mnk[v] = a if a < b2 else b2

def query(a, b):
    if a == b:
        return 0
    ans = 10**18
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    bit = 0
    while diff:
        if diff & 1:
            val = mn[bit][a]
            if val < ans:
                ans = val
            a = up[bit][a]
        diff >>= 1
        bit += 1
    if a == b:
        return ans
    for k in range(LOG - 1, -1, -1):
        if up[k][a] != up[k][b]:
            va = mn[k][a]
            vb = mn[k][b]
            if va < ans:
                ans = va
            if vb < ans:
                ans = vb
            a = up[k][a]
            b = up[k][b]
    va = mn[0][a]
    vb = mn[0][b]
    if va < ans:
        ans = va
    if vb < ans:
        ans = vb
    return ans

c = data[it]
it += 1
out = []
for _ in range(c):
    x = data[it]
    y = data[it + 1]
    it += 2
    out.append(str(query(x, y)))

sys.stdout.write("\n".join(out))