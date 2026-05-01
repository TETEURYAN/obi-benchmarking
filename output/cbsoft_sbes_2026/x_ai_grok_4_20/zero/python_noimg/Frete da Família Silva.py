
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
edges = []
index = 2
for i in range(M):
    P = int(data[index])
    Q = int(data[index + 1])
    U = int(data[index + 2])
    edges.append((U, P, Q))
    index += 3

edges.sort()

parent = list(range(N))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        parent[px] = py
        return True
    return False

total = 0
used = 0
for cost, u, v in edges:
    if union(u, v):
        total += cost
        used += 1
        if used == N - 1:
            break

print(total)
