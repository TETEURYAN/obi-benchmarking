import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])

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
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1

idx = 2
for _ in range(m):
    u = int(data[idx])
    v = int(data[idx + 1])
    union(u, v)
    idx += 2

components = set()
for i in range(1, n + 1):
    components.add(find(i))

print(len(components))