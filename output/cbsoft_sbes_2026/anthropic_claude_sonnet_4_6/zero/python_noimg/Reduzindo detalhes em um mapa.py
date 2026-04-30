import sys

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1
    return True

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx]); idx += 1
M = int(input_data[idx]); idx += 1

edges = []
for _ in range(M):
    u = int(input_data[idx]); idx += 1
    v = int(input_data[idx]); idx += 1
    c = int(input_data[idx]); idx += 1
    edges.append((c, u, v))

edges.sort()

parent = list(range(N + 1))
rank = [0] * (N + 1)

total = 0
for c, u, v in edges:
    if union(parent, rank, u, v):
        total += c

print(total)