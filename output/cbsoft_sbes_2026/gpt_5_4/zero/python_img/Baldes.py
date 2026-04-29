import sys

INF = 10**18

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.mn1 = [INF] * (2 * size)
        self.mn1i = [-1] * (2 * size)
        self.mn2 = [INF] * (2 * size)
        self.mn2i = [-1] * (2 * size)
        self.mx1 = [-INF] * (2 * size)
        self.mx1i = [-1] * (2 * size)
        self.mx2 = [-INF] * (2 * size)
        self.mx2i = [-1] * (2 * size)
        for i, v in enumerate(arr):
            p = size + i
            self.mn1[p] = v
            self.mn1i[p] = i
            self.mx1[p] = v
            self.mx1i[p] = i
        for p in range(size - 1, 0, -1):
            self._pull(p)

    def _pull(self, p):
        l = p << 1
        r = l | 1

        cand_min = [
            (self.mn1[l], self.mn1i[l]),
            (self.mn2[l], self.mn2i[l]),
            (self.mn1[r], self.mn1i[r]),
            (self.mn2[r], self.mn2i[r]),
        ]
        cand_min.sort()
        self.mn1[p], self.mn1i[p] = cand_min[0]
        self.mn2[p], self.mn2i[p] = INF, -1
        idx1 = self.mn1i[p]
        for v, idx in cand_min[1:]:
            if idx != idx1:
                self.mn2[p], self.mn2i[p] = v, idx
                break

        cand_max = [
            (self.mx1[l], self.mx1i[l]),
            (self.mx2[l], self.mx2i[l]),
            (self.mx1[r], self.mx1i[r]),
            (self.mx2[r], self.mx2i[r]),
        ]
        cand_max.sort(reverse=True)
        self.mx1[p], self.mx1i[p] = cand_max[0]
        self.mx2[p], self.mx2i[p] = -INF, -1
        idx1 = self.mx1i[p]
        for v, idx in cand_max[1:]:
            if idx != idx1:
                self.mx2[p], self.mx2i[p] = v, idx
                break

    def update(self, pos, val):
        p = self.size + pos
        if val < self.mn1[p]:
            self.mn1[p] = val
            self.mn1i[p] = pos
        if val > self.mx1[p]:
            self.mx1[p] = val
            self.mx1i[p] = pos
        p >>= 1
        while p:
            self._pull(p)
            p >>= 1

    def query(self, l, r):
        l += self.size
        r += self.size

        left_min = []
        right_min = []
        left_max = []
        right_max = []

        while l <= r:
            if l & 1:
                left_min.append((self.mn1[l], self.mn1i[l]))
                left_min.append((self.mn2[l], self.mn2i[l]))
                left_max.append((self.mx1[l], self.mx1i[l]))
                left_max.append((self.mx2[l], self.mx2i[l]))
                l += 1
            if not (r & 1):
                right_min.append((self.mn1[r], self.mn1i[r]))
                right_min.append((self.mn2[r], self.mn2i[r]))
                right_max.append((self.mx1[r], self.mx1i[r]))
                right_max.append((self.mx2[r], self.mx2i[r]))
                r -= 1
            l >>= 1
            r >>= 1

        mins = left_min + right_min
        maxs = left_max + right_max

        mins.sort()
        maxs.sort(reverse=True)

        mn1v, mn1i = mins[0]
        mn2v, mn2i = INF, -1
        for v, idx in mins[1:]:
            if idx != mn1i:
                mn2v, mn2i = v, idx
                break

        mx1v, mx1i = maxs[0]
        mx2v, mx2i = -INF, -1
        for v, idx in maxs[1:]:
            if idx != mx1i:
                mx2v, mx2i = v, idx
                break

        if mx1i != mn1i:
            return mx1v - mn1v
        a = mx1v - mn2v if mn2i != -1 else -INF
        b = mx2v - mn1v if mx2i != -1 else -INF
        return max(a, b)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    seg = SegTree(arr)
    out = []

    for _ in range(M):
        t, x, y = map(int, input().split())
        if t == 1:
            p, i = x, y
            seg.update(i - 1, p)
        else:
            a, b = x, y
            out.append(str(seg.query(a - 1, b - 1)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
