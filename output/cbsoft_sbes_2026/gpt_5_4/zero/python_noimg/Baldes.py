import sys

INF = 10**30

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.mn1 = [INF] * (2 * size)
        self.mn2 = [INF] * (2 * size)
        self.mx1 = [-INF] * (2 * size)
        self.mx2 = [-INF] * (2 * size)

        for i, v in enumerate(arr):
            p = size + i
            self.mn1[p] = v
            self.mx1[p] = v

        for p in range(size - 1, 0, -1):
            self._pull(p)

    def _pull(self, p):
        l = p << 1
        r = l | 1

        a1, a2 = self.mn1[l], self.mn2[l]
        b1, b2 = self.mn1[r], self.mn2[r]
        if a1 <= b1:
            self.mn1[p] = a1
            self.mn2[p] = a2 if a2 <= b1 else b1
        else:
            self.mn1[p] = b1
            self.mn2[p] = b2 if b2 <= a1 else a1

        a1, a2 = self.mx1[l], self.mx2[l]
        b1, b2 = self.mx1[r], self.mx2[r]
        if a1 >= b1:
            self.mx1[p] = a1
            self.mx2[p] = a2 if a2 >= b1 else b1
        else:
            self.mx1[p] = b1
            self.mx2[p] = b2 if b2 >= a1 else a1

    def update(self, idx, val):
        p = self.size + idx
        if val < self.mn1[p]:
            self.mn2[p] = self.mn1[p]
            self.mn1[p] = val
        elif val < self.mn2[p]:
            self.mn2[p] = val

        if val > self.mx1[p]:
            self.mx2[p] = self.mx1[p]
            self.mx1[p] = val
        elif val > self.mx2[p]:
            self.mx2[p] = val

        p >>= 1
        while p:
            self._pull(p)
            p >>= 1

    def query(self, l, r):
        l += self.size
        r += self.size

        left_mn1 = INF
        left_mn2 = INF
        left_mx1 = -INF
        left_mx2 = -INF

        right_mn1 = INF
        right_mn2 = INF
        right_mx1 = -INF
        right_mx2 = -INF

        while l <= r:
            if l & 1:
                a1, a2 = left_mn1, left_mn2
                b1, b2 = self.mn1[l], self.mn2[l]
                if a1 <= b1:
                    left_mn1 = a1
                    left_mn2 = a2 if a2 <= b1 else b1
                else:
                    left_mn1 = b1
                    left_mn2 = b2 if b2 <= a1 else a1

                a1, a2 = left_mx1, left_mx2
                b1, b2 = self.mx1[l], self.mx2[l]
                if a1 >= b1:
                    left_mx1 = a1
                    left_mx2 = a2 if a2 >= b1 else b1
                else:
                    left_mx1 = b1
                    left_mx2 = b2 if b2 >= a1 else a1
                l += 1

            if not (r & 1):
                a1, a2 = self.mn1[r], self.mn2[r]
                b1, b2 = right_mn1, right_mn2
                if a1 <= b1:
                    right_mn1 = a1
                    right_mn2 = a2 if a2 <= b1 else b1
                else:
                    right_mn1 = b1
                    right_mn2 = b2 if b2 <= a1 else a1

                a1, a2 = self.mx1[r], self.mx2[r]
                b1, b2 = right_mx1, right_mx2
                if a1 >= b1:
                    right_mx1 = a1
                    right_mx2 = a2 if a2 >= b1 else b1
                else:
                    right_mx1 = b1
                    right_mx2 = b2 if b2 >= a1 else a1
                r -= 1

            l >>= 1
            r >>= 1

        a1, a2 = left_mn1, left_mn2
        b1, b2 = right_mn1, right_mn2
        if a1 <= b1:
            mn1 = a1
            mn2 = a2 if a2 <= b1 else b1
        else:
            mn1 = b1
            mn2 = b2 if b2 <= a1 else a1

        a1, a2 = left_mx1, left_mx2
        b1, b2 = right_mx1, right_mx2
        if a1 >= b1:
            mx1 = a1
            mx2 = a2 if a2 >= b1 else b1
        else:
            mx1 = b1
            mx2 = b2 if b2 >= a1 else a1

        return mx1 - mn2 if mx1 - mn2 > mx2 - mn1 else mx2 - mn1


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    arr = [next(it) for _ in range(n)]

    st = SegTree(arr)
    out = []

    for _ in range(m):
        t = next(it)
        if t == 1:
            p = next(it)
            i = next(it) - 1
            st.update(i, p)
        else:
            a = next(it) - 1
            b = next(it) - 1
            out.append(str(st.query(a, b)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
