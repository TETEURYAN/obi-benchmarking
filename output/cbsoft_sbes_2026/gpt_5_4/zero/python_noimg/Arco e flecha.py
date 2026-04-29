import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]

    dists = []
    prev_p = 0
    for i, (x, y) in enumerate(data):
        if i == 0:
            xr, yr = x, y
        else:
            xr, yr = x + prev_p, y + prev_p
        d = xr * xr + yr * yr
        dists.append(d)
        prev_p = 0

    vals = sorted(set(dists))
    comp = {v: i + 1 for i, v in enumerate(vals)}
    m = len(vals)

    bit = [0] * (m + 2)

    def add(i, v):
        while i <= m:
            bit[i] += v
            i += i & -i

    def sum_(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    out = []
    prev_p = 0
    for i, (x, y) in enumerate(data):
        if i == 0:
            xr, yr = x, y
        else:
            xr, yr = x + prev_p, y + prev_p
        d = xr * xr + yr * yr
        idx = comp[d]
        p = sum_(idx)
        out.append(str(p))
        add(idx, 1)
        prev_p = p

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()