import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]

up = [[] for _ in range(n + 1)]
down = [[] for _ in range(n + 1)]

idx = 2
for _ in range(m):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    if a < b:
        up[a].append(b)
        down[b].append(a)
    else:
        up[b].append(a)
        down[a].append(b)

f0 = [1] * (n + 1)  # next step is odd position (must go up)
f1 = [1] * (n + 1)  # next step is even position (must go down)

for v in range(n, 0, -1):
    best = 1
    for u in up[v]:
        val = 1 + f1[u]
        if val > best:
            best = val
    f0[v] = best

for v in range(1, n + 1):
    best = 1
    for u in down[v]:
        val = 1 + f0[u]
        if val > best:
            best = val
    f1[v] = best

ans = [0] * n
for v in range(1, n + 1):
    ans[v - 1] = str(f0[v])

sys.stdout.write(" ".join(ans))