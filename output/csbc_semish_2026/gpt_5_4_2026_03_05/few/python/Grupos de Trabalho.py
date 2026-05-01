import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

E, M, D = data[0], data[1], data[2]
idx = 3

group = [0] * (E + 1)
gid = 0

for _ in range(M):
    idx += 2

for _ in range(D):
    idx += 2

num_groups = E // 3
groups_start = idx
for _ in range(num_groups):
    a = data[idx]
    b = data[idx + 1]
    c = data[idx + 2]
    gid += 1
    group[a] = gid
    group[b] = gid
    group[c] = gid
    idx += 3

ans = 0
idx = 3

for _ in range(M):
    x = data[idx]
    y = data[idx + 1]
    if group[x] != group[y]:
        ans += 1
    idx += 2

for _ in range(D):
    u = data[idx]
    v = data[idx + 1]
    if group[u] == group[v]:
        ans += 1
    idx += 2

print(ans)