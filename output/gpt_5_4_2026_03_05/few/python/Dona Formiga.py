import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

s = int(data[0])
t = int(data[1])
p = int(data[2]) - 1

h = list(map(int, data[3:3 + s]))

adj = [[] for _ in range(s)]
idx = 3 + s
for _ in range(t):
    a = int(data[idx]) - 1
    b = int(data[idx + 1]) - 1
    if h[a] > h[b]:
        adj[a].append(b)
    elif h[b] > h[a]:
        adj[b].append(a)
    idx += 2

order = sorted(range(s), key=lambda x: h[x])

dp = [0] * s
for u in order:
    best = 0
    for v in adj[u]:
        val = 1 + dp[v]
        if val > best:
            best = val
    dp[u] = best

print(dp[p])