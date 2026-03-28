import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
M = int(input_data[1])

edges = []
idx = 2
for i in range(M):
    U = int(input_data[idx])
    V = int(input_data[idx + 1])
    C = int(input_data[idx + 2])
    edges.append((C, U, V))
    idx += 3

edges.sort()

parent = list(range(N + 1))
rank = [0] * (N + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        if rank[px] > rank[py]:
            parent[py] = px
        elif rank[px] < rank[py]:
            parent[px] = py
        else:
            parent[py] = px
            rank[px] += 1
        return True
    return False

total = 0
for c, u, v in edges:
    if union(u, v):
        total += c

print(total)