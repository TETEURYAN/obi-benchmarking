import sys
from collections import deque

data = sys.stdin.read().split()
if not data:
    sys.exit()

idx = 0
teste = 1
out = []

while True:
    C = int(data[idx]); E = int(data[idx + 1]); L = int(data[idx + 2]); P = int(data[idx + 3])
    idx += 4

    if C == 0 and E == 0 and L == 0 and P == 0:
        break

    adj = [[] for _ in range(C + 1)]
    for _ in range(E):
        x = int(data[idx]); y = int(data[idx + 1])
        idx += 2
        adj[x].append(y)
        adj[y].append(x)

    dist = [-1] * (C + 1)
    q = deque([L])
    dist[L] = 0

    while q:
        u = q.popleft()
        if dist[u] == P:
            continue
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if dist[v] <= P:
                    q.append(v)

    reachable = [str(i) for i in range(1, C + 1) if i != L and dist[i] != -1 and dist[i] <= P]

    out.append(f"Teste {teste}")
    out.append(" ".join(reachable))
    out.append("")

    teste += 1

sys.stdout.write("\n".join(out))