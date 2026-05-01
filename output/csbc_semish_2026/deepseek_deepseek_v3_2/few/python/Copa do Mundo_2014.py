import sys

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    total_cost = 0
    used_edges = 0
    for u, v, w in edges:
        if union(u, v):
            total_cost += w
            used_edges += 1
            if used_edges == n - 1:
                break
    return total_cost

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    N = int(data[idx]); idx += 1
    F = int(data[idx]); idx += 1
    R = int(data[idx]); idx += 1

    ferrovias = []
    for _ in range(F):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        ferrovias.append((a, b, c))

    rodovias = []
    for _ in range(R):
        i = int(data[idx]); j = int(data[idx+1]); k = int(data[idx+2])
        idx += 3
        rodovias.append((i, j, k))

    cost_f = kruskal(ferrovias, N)
    cost_r = kruskal(rodovias, N)
    print(cost_f + cost_r)

if __name__ == "__main__":
    main()