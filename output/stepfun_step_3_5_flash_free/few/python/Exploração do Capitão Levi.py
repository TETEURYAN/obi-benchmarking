import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    def query(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    P = int(next(it))
    Q = int(next(it))
    points = []
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        points.append((x, y))
    points.sort(key=lambda p: p[0])
    B = [y * Q - P * x for x, y in points]
    all_B = sorted(set(B))
    rank_map = {val: i + 1 for i, val in enumerate(all_B)}
    ranks = [rank_map[b] for b in B]
    fenwick = Fenwick(len(all_B))
    total_inseridos = 0
    ans = 0
    if Q > 0:
        for i in range(n - 1, -1, -1):
            r = ranks[i]
            cnt = total_inseridos - fenwick.query(r - 1)
            ans += cnt
            fenwick.update(r, 1)
            total_inseridos += 1
    else:
        for i in range(n - 1, -1, -1):
            r = ranks[i]
            cnt = fenwick.query(r)
            ans += cnt
            fenwick.update(r, 1)
            total_inseridos += 1
    print(ans)

if __name__ == "__main__":
    main()