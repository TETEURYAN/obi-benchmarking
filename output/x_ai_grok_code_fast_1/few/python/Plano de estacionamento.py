import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & -idx
        return s

    def query_range(self, l, r):
        return self.query(r) - self.query(l - 1)

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
V = []
for _ in range(M):
    V.append(int(input_data[idx]))
    idx += 1

ft = Fenwick(N)
for i in range(1, N + 1):
    ft.update(i, 1)

count = 0
for vi in V:
    low = 1
    high = min(vi, N)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if ft.query_range(mid, mid) == 1:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    if ans != -1:
        ft.update(ans, -1)
        count += 1
    else:
        break

print(count)