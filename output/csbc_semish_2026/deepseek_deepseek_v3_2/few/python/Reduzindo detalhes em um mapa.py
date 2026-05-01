import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    edges = []

    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        c = int(data[idx + 2])
        edges.append((c, u, v))
        idx += 3

    edges.sort()

    parent = list(range(n + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx != ry:
            parent[ry] = rx
            return True
        return False

    total_cost = 0
    count = 0

    for cost, u, v in edges:
        if union(u, v):
            total_cost += cost
            count += 1
            if count == n - 1:
                break

    print(total_cost)

if __name__ == "__main__":
    main()