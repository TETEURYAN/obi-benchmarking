import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

def main():
    input = sys.stdin.readline
    n = int(input())
    raw = [tuple(map(int, input().split())) for _ in range(n)]

    penalties = [0] * n
    dists = [0] * n

    prev_p = 0
    for i in range(n):
        x, y = raw[i]
        if i == 0:
            xr, yr = x, y
        else:
            xr, yr = x + prev_p, y + prev_p
        d = xr * xr + yr * yr
        dists[i] = d
        prev_p = 0  # placeholder, actual penalties computed later

    vals = sorted(set(dists))
    comp = {v: i + 1 for i, v in enumerate(vals)}
    bit = Fenwick(len(vals))

    out = []
    prev_p = 0
    for i in range(n):
        x, y = raw[i]
        if i == 0:
            xr, yr = x, y
        else:
            xr, yr = x + prev_p, y + prev_p
        d = xr * xr + yr * yr
        idx = comp[d]
        p = bit.sum(idx)
        penalties[i] = p
        out.append(str(p))
        bit.add(idx, 1)
        prev_p = p

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()