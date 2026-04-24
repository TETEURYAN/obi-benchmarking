import sys
import math
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    points = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); y = int(data[idx+1]); idx += 2
        points.append((x, y))
    A = int(data[idx])
    A2 = A * A

    if n == 1:
        print('S')
        return

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    dx = max_x - min_x
    dy = max_y - min_y
    if dx*dx + dy*dy <= A2:
        print('S')
        return

    L = max(1, math.isqrt(A*A // 2))

    grid = {}
    for i, (x, y) in enumerate(points):
        cell = (x // L, y // L)
        if cell not in grid:
            grid[cell] = []
        grid[cell].append(i)

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    for lst in grid.values():
        if len(lst) > 1:
            first = lst[0]
            for p in lst[1:]:
                union(first, p)

    for lst in grid.values():
        lst.sort()

    for p in range(n):
        x1, y1 = points[p]
        i = x1 // L
        j = y1 // L
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                cell = (i + di, j + dj)
                if cell not in grid:
                    continue
                lst = grid[cell]
                pos = bisect.bisect_right(lst, p)
                for q in lst[pos:]:
                    x2, y2 = points[q]
                    dx = abs(x1 - x2)
                    if dx > A:
                        continue
                    dy = abs(y1 - y2)
                    if dy > A:
                        continue
                    if dx*dx + dy*dy <= A2:
                        union(p, q)

    comp = set()
    for i in range(n):
        comp.add(find(i))
    print('S' if len(comp) == 1 else 'N')

if __name__ == "__main__":
    main()