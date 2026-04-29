import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        c = int(next(it))
        edges.append((c, u - 1, v - 1))

    edges.sort()

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total = 0
    used = 0

    for c, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if rank[ru] < rank[rv]:
                parent[ru] = rv
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
            else:
                parent[rv] = ru
                rank[ru] += 1
            total += c
            used += 1
            if used == n - 1:
                break

    print(total)

if __name__ == "__main__":
    main()
