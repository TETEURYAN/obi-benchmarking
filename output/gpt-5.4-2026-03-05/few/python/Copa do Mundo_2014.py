import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, f, r = data[0], data[1], data[2]
idx = 3

rail = []
for _ in range(f):
    a = data[idx] - 1
    b = data[idx + 1] - 1
    c = data[idx + 2]
    rail.append((c, a, b))
    idx += 3

road = []
for _ in range(r):
    a = data[idx] - 1
    b = data[idx + 1] - 1
    c = data[idx + 2]
    road.append((c, a, b))
    idx += 3

class DSU:
    __slots__ = ("p", "r")
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        p = self.p
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.r[pa] < self.r[pb]:
            pa, pb = pb, pa
        self.p[pb] = pa
        if self.r[pa] == self.r[pb]:
            self.r[pa] += 1
        return True

dsu = DSU(n)
rail.sort()

cost = 0
components = n

for c, a, b in rail:
    if dsu.union(a, b):
        cost += c
        components -= 1

if components > 1:
    road.sort()
    for c, a, b in road:
        if dsu.union(a, b):
            cost += c
            components -= 1
            if components == 1:
                break

print(cost)