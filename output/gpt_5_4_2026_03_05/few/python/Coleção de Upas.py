import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj = [[] for _ in range(n + 1)]
idx = 2
for _ in range(m):
    u = data[idx]
    v = data[idx + 1]
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

chosen = []
in_chosen = [False] * (n + 1)
mark = [0] * (n + 1)
cur = 1

for v in range(n, 0, -1):
    bad = False
    for u in adj[v]:
        if mark[u] == cur:
            bad = True
            break
    if not bad:
        chosen.append(v)
        in_chosen[v] = True
        cur += 1
        for u in adj[v]:
            if in_chosen[u]:
                mark[u] = cur

chosen.reverse()
print(len(chosen))
print(*chosen)