import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, a, b = data[0], data[1], data[2]
adj = [[] for _ in range(n + 1)]

idx = 3
for _ in range(n - 1):
    p = data[idx]
    q = data[idx + 1]
    d = data[idx + 2]
    adj[p].append((q, d))
    adj[q].append((p, d))
    idx += 3

visited = [False] * (n + 1)
stack = [(a, 0)]
visited[a] = True

while stack:
    u, dist = stack.pop()
    if u == b:
        print(dist)
        break
    for v, w in adj[u]:
        if not visited[v]:
            visited[v] = True
            stack.append((v, dist + w))