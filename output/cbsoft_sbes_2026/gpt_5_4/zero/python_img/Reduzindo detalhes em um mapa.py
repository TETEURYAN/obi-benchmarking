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

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        edges.append((c, u, v))

    edges.sort()
    dsu = DSU(n)
    total = 0
    used = 0

    for c, u, v in edges:
        if dsu.union(u, v):
            total += c
            used += 1
            if used == n - 1:
                break

    print(total)

if __name__ == "__main__":
    main()
