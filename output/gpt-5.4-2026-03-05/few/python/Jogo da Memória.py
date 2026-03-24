import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
c = [0] + data[1:n+1]

adj = [[] for _ in range(n + 1)]
idx = n + 1
for _ in range(n - 1):
    a = data[idx]
    b = data[idx + 1]
    adj[a].append(b)
    adj[b].append(a)
    idx += 2

first = [0] * (n // 2 + 1)
pairs = []
for i in range(1, n + 1):
    x = c[i]
    if first[x] == 0:
        first[x] = i
    else:
        pairs.append((first[x], i))

LOG = (n).bit_length()
parent = [[0] * (n + 1) for _ in range(LOG)]
depth = [0] * (n + 1)

stack = [1]
order = [1]
parent[0][1] = 0
while stack:
    u = stack.pop()
    for v in adj[u]:
        if v != parent[0][u]:
            parent[0][v] = u
            depth[v] = depth[u] + 1
            stack.append(v)
            order.append(v)

for k in range(1, LOG):
    pk = parent[k - 1]
    ck = parent[k]
    for v in range(1, n + 1):
        ck[v] = pk[pk[v]]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    bit = 0
    while diff:
        if diff & 1:
            a = parent[bit][a]
        diff >>= 1
        bit += 1
    if a == b:
        return a
    for k in range(LOG - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    return parent[0][a]

ans = 0
for u, v in pairs:
    w = lca(u, v)
    ans += depth[u] + depth[v] - 2 * depth[w]

print(ans)