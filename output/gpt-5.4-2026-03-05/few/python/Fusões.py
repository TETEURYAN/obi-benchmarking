import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
k = int(data[1])

parent = list(range(n + 1))
size = [1] * (n + 1)

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
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

out = []
idx = 2

for _ in range(k):
    op = data[idx]
    a = int(data[idx + 1])
    b = int(data[idx + 2])
    if op == 'F':
        union(a, b)
    else:
        out.append('S' if find(a) == find(b) else 'N')
    idx += 3

sys.stdout.write('\n'.join(out))