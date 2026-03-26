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

def kruskal(n, edges):
    # edges sorted by (num_roads, cost)
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total_roads = 0
    total_cost = 0
    count = 0
    for (is_road, cost, u, v) in edges:
        if union(parent, rank, u, v):
            total_roads += is_road
            total_cost += cost
            count += 1
            if count == n - 1:
                break
    return total_roads, total_cost

data = sys.stdin.read().split()
idx = 0
N = int(data[idx]); idx+=1
F = int(data[idx]); idx+=1
R = int(data[idx]); idx+=1

edges = []

for _ in range(F):
    a = int(data[idx]); idx+=1
    b = int(data[idx]); idx+=1
    c = int(data[idx]); idx+=1
    # is_road=0 (railway), sort key: (0, cost)
    edges.append((0, c, a, b))

for _ in range(R):
    i = int(data[idx]); idx+=1
    j = int(data[idx]); idx+=1
    k = int(data[idx]); idx+=1
    # is_road=1 (road), sort key: (1, cost)
    edges.append((1, k, i, j))

# Sort: minimize roads first (is_road), then minimize cost
edges.sort(key=lambda x: (x[0], x[1]))

total_roads, total_cost = kruskal(N, edges)
print(total_cost)