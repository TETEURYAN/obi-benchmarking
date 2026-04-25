import sys
sys.setrecursionlimit(200000)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    X = int(next(it))
    Y = int(next(it))
    N = int(next(it))
    A = int(next(it))
    cities = []
    for i in range(N):
        x = int(next(it))
        y = int(next(it))
        cities.append((x, y))
    
    edges = []
    for i in range(N):
        xi, yi = cities[i]
        for j in range(i + 1, N):
            xj, yj = cities[j]
            dist = (abs(xi - xj) + abs(yi - yj)) * 100
            if dist <= A:
                edges.append((dist, i, j))
    
    edges.sort()
    parent = list(range(N))
    rank = [0] * N
    components = N
    for d, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            components -= 1
            if components == 1:
                break
    
    print(components - 1)

if __name__ == "__main__":
    main()