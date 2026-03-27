import sys

data = sys.stdin.read().split()
idx = 0
N = int(data[idx])
idx += 1
K = int(data[idx])
idx += 1

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        if rank[pa] > rank[pb]:
            parent[pb] = pa
        elif rank[pa] < rank[pb]:
            parent[pa] = pb
        else:
            parent[pb] = pa
            rank[pa] += 1

for _ in range(K):
    op = data[idx]
    idx += 1
    a = int(data[idx])
    idx += 1
    b = int(data[idx])
    idx += 1
    if op == 'F':
        union(a, b)
    elif op == 'C':
        if find(a) == find(b):
            print('S')
        else:
            print('N')