import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

data = sys.stdin.read().strip().split()
i = 0
teste = 1
out = []

while i < len(data):
    n = int(data[i])
    m = int(data[i + 1])
    i += 2

    if n == 0:
        break

    edges = []
    for _ in range(m):
        x = int(data[i])
        y = int(data[i + 1])
        z = int(data[i + 2])
        i += 3
        edges.append((z, x, y))

    edges.sort()
    dsu = DSU(n)
    mst = []

    for z, x, y in edges:
        if dsu.union(x, y):
            if x > y:
                x, y = y, x
            mst.append((x, y))
            if len(mst) == n - 1:
                break

    out.append(f"Teste {teste}")
    for x, y in mst:
        out.append(f"{x} {y}")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))