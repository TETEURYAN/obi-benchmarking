import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    rects = []
    xs = []
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        rects.append((x1, y1, x2, y2, i))
        xs.append((x1, 1, i))   # open
        xs.append((x2, -1, i))  # close

    rects_by_id = rects[:]
    parent = [-1] * n
    depth = [0] * n

    # Sweep line on x, maintaining active rectangles ordered by containment in y.
    # Because rectangles are laminar (nested or disjoint), among active rectangles
    # the parent of a rectangle is exactly the active rectangle with smallest y1
    # greater than its y1 (equivalently immediate container).
    ys = sorted(rects, key=lambda r: r[1])  # by y1 ascending
    pos_in_y = [0] * n
    for p, (_, _, _, _, idx) in enumerate(ys):
        pos_in_y[idx] = p

    active = [False] * n

    class BIT:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 2)

        def add(self, i, v):
            i += 1
            n = self.n + 1
            bit = self.bit
            while i <= n:
                bit[i] += v
                i += i & -i

        def sum(self, i):
            i += 1
            s = 0
            bit = self.bit
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def kth(self, k):
            idx = 0
            bitmask = 1 << (self.n + 1).bit_length()
            bit = self.bit
            while bitmask:
                t = idx + bitmask
                if t <= self.n + 1 and bit[t] < k:
                    idx = t
                    k -= bit[t]
                bitmask >>= 1
            return idx  # 0-based after external adjustment

    bit = BIT(n)

    events = sorted(xs, key=lambda e: (e[0], e[1]))  # close before open at same x

    for x, typ, idx in events:
        p = pos_in_y[idx]
        if typ == -1:
            bit.add(p, -1)
            active[idx] = False
        else:
            cnt = bit.sum(n - 1) - bit.sum(p)
            if cnt == 0:
                parent[idx] = -1
                depth[idx] = 0
            else:
                before = bit.sum(p)
                total = bit.sum(n - 1)
                target_rank = before + 1
                pp = bit.kth(target_rank)
                par_idx = ys[pp][4]
                parent[idx] = par_idx
                depth[idx] = depth[par_idx] + 1
            bit.add(p, 1)
            active[idx] = True

    max_depth = max(depth)
    ans = (max_depth + 2) // 2
    print(ans)

if __name__ == "__main__":
    main()
