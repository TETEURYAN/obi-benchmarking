import sys
sys.setrecursionlimit(200000)

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj = [[] for _ in range(n + 1)]

idx = 2
for _ in range(n - 1):
    u = data[idx]
    v = data[idx + 1]
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

parent = [0] * (n + 1)
depth = [0] * (n + 1)

stack = [1]
parent[1] = -1
order = [1]

while stack:
    u = stack.pop()
    for v in adj[u]:
        if v != parent[u]:
            parent[v] = u
            depth[v] = depth[u] + 1
            stack.append(v)
            order.append(v)

colors = [0] * (n + 1)

for _ in range(m):
    p = data[idx]
    q = data[idx + 1]
    c = data[idx + 2]
    idx += 3

    a, b = p, q
    path_a = []
    path_b = []

    while depth[a] > depth[b]:
        path_a.append(a)
        a = parent[a]
    while depth[b] > depth[a]:
        path_b.append(b)
        b = parent[b]
    while a != b:
        path_a.append(a)
        path_b.append(b)
        a = parent[a]
        b = parent[b]

    path = path_a + [a] + path_b[::-1]
    for node in path:
        colors[node] = c

print(*colors[1:])