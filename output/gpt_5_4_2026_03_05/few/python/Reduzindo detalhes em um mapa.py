import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
m = data[1]

parent = list(range(n + 1))
rank = [0] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

edges = []
idx = 2
for _ in range(m):
    u = data[idx]
    v = data[idx + 1]
    c = data[idx + 2]
    edges.append((c, u, v))
    idx += 3

edges.sort()

total = 0
used = 0
for c, u, v in edges:
    if union(u, v):
        total += c
        used += 1
        if used == n - 1:
            break

print(total)