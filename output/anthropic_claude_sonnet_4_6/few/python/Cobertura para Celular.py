import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    coords = []
    for _ in range(n):
        x = int(data[idx]); y = int(data[idx+1]); idx += 2
        coords.append((x, y))
    A = int(data[idx]); idx += 1

    # Union-Find
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

    A2 = A * A
    for i in range(n):
        for j in range(i+1, n):
            dx = coords[i][0] - coords[j][0]
            dy = coords[i][1] - coords[j][1]
            if dx*dx + dy*dy <= A2:
                union(i, j)

    root = find(0)
    for i in range(1, n):
        if find(i) != root:
            print("N")
            return
    print("S")

main()