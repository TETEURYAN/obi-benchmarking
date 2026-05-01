import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    us = [xs[i] + ys[i] for i in range(n)]
    vs = [xs[i] - ys[i] for i in range(n)]

    min_u = min(us)
    max_u = max(us)
    min_v = min(vs)
    max_v = max(vs)

    lo, hi = -1, max(max_u - min_u, max_v - min_v)

    def feasible(D):
        intervals = []

        a = max_u - D
        b = min_u + D
        if a > b:
            intervals.append((b, a))

        a = max_v - D
        b = min_v + D
        if a > b:
            intervals.append((b, a))

        if not intervals:
            return True

        cand = []
        for l, r in intervals:
            cand.append(l)
            cand.append(r)

        for t in cand:
            ok = True
            for l, r in intervals:
                if l < t < r:
                    ok = False
                    break
            if ok:
                return True
        return False

    while hi - lo > 1:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid

    print(hi)

if __name__ == "__main__":
    main()
