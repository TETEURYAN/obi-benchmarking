import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    f = int(next(it))
    r = int(next(it))
    edges = []
    for _ in range(f):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        edges.append((0, c, a, b))
    for _ in range(r):
        i = int(next(it)); j = int(next(it)); k = int(next(it))
        edges.append((1, k, i, j))
    edges.sort(key=lambda x: (x[0], x[1]))
    parent = list(range(n+1))
    rank = [0]*(n+1)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    total_cost = 0
    edges_used = 0
    for tipo, custo, u, v in edges:
        if union(u, v):
            total_cost += custo
            edges_used += 1
            if edges_used == n-1:
                break
    print(total_cost)

if __name__ == "__main__":
    main()