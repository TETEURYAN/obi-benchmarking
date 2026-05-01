import sys

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, i, v):
        n = self.n
        bit = self.bit
        while i <= n:
            bit[i] += v
            i += i & -i

    def range_add(self, l, r, v):
        if l > r:
            return
        self.add(l, v)
        if r + 1 <= self.n:
            self.add(r + 1, -v)

    def query(self, i):
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    bit_a = BIT(N)
    bit_b = BIT(N)

    out = []

    for _ in range(M):
        parts = list(map(int, input().split()))
        t = parts[0]

        if t == 1:
            i, V = parts[1], parts[2]
            r = min(N, i + V - 1)
            l = i
            bit_a.range_add(l, r, -1)
            bit_b.range_add(l, r, V + i)
        elif t == 2:
            i, V = parts[1], parts[2]
            l = max(1, i - V + 1)
            r = i
            bit_a.range_add(l, r, 1)
            bit_b.range_add(l, r, V - i)
        else:
            i = parts[1]
            a = bit_a.query(i)
            b = bit_b.query(i)
            out.append(str(a * i + b))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
