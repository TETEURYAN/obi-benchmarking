import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

idx = 0
teste = 1
out = []

while idx < len(data):
    n = data[idx]
    idx += 1
    if n == 0:
        break

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        adj[x].append(y)
        adj[y].append(x)

    if n == 1:
        center = 1
    else:
        degree = [0] * (n + 1)
        q = deque()
        for i in range(1, n + 1):
            degree[i] = len(adj[i])
            if degree[i] <= 1:
                q.append(i)

        remaining = n
        while remaining > 2:
            sz = len(q)
            remaining -= sz
            for _ in range(sz):
                u = q.popleft()
                for v in adj[u]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        q.append(v)

        center = min(q) if q else 1

    out.append(f"Teste {teste}")
    out.append(str(center))
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))