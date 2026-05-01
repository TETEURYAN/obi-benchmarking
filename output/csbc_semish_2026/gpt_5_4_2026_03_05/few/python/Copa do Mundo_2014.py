import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
f = int(next(it))
r = int(next(it))

rail = []
road = []

for _ in range(f):
    a = int(next(it)) - 1
    b = int(next(it)) - 1
    c = int(next(it))
    rail.append((c, a, b))

for _ in range(r):
    i = int(next(it)) - 1
    j = int(next(it)) - 1
    k = int(next(it))
    road.append((k, i, j))

parent = list(range(n))
rank = [0] * n

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

rail.sort()
cost = 0
components = n

for c, a, b in rail:
    if union(a, b):
        cost += c
        components -= 1

road.sort()
for k, i, j in road:
    if components == 1:
        break
    if union(i, j):
        cost += k
        components -= 1

print(cost)