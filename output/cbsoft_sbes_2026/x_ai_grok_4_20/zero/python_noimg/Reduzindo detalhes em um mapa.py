
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

edges = []
index = 2
for i in range(M):
    u = int(data[index])
    v = int(data[index + 1])
    c = int(data[index + 2])
    edges.append((c, u, v))
    index += 3

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
    if px == py:
        return False
    if rank[px] < rank[py]:
        parent[px] = py
    elif rank[px] > rank[py]:
        parent[py] = px
    else:
        parent[py] = px
        rank[px] += 1
    return True

total = 0
used = 0

for cost, u, v in edges:
    if union(u, v):
        total += cost
        used += 1
        if used == N - 1:
            break

print(total)
