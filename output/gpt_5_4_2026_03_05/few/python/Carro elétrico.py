import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

X, Y = data[0], data[1]
N, A = data[2], data[3]

coords = []
idx = 4
for _ in range(N):
    x = data[idx]
    y = data[idx + 1]
    coords.append((x, y))
    idx += 2

limit = A // 100

parent = list(range(N))
rank = [0] * N

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1

for i in range(N):
    xi, yi = coords[i]
    for j in range(i + 1, N):
        xj, yj = coords[j]
        if abs(xi - xj) + abs(yi - yj) <= limit:
            union(i, j)

roots = set()
for i in range(N):
    roots.add(find(i))

print(len(roots) - 1)