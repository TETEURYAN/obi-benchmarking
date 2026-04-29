import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    pts = []
    for x, y in zip(xs, ys):
        u = x + y
        v = x - y
        pts.append((u, v))

    us = sorted(u for u, _ in pts)
    vs = sorted(v for _, v in pts)

    def feasible(D):
        INF = 10**30

        lu1 = us[0]
        ru1 = us[0] + D
        lv1 = vs[0]
        rv1 = vs[0] + D

        lu2 = INF
        ru2 = -INF
        lv2 = INF
        rv2 = -INF

        for u, v in pts:
            in1 = (lu1 <= u <= ru1 and lv1 <= v <= rv1)
            in2 = (lu2 <= u <= ru2 and lv2 <= v <= rv2)

            if in1 and in2:
                nlu1 = max(lu1, u - D)
                nru1 = min(ru1, u)
                nlv1 = max(lv1, v - D)
                nrv1 = min(rv1, v)

                nlu2 = max(lu2, u - D)
                nru2 = min(ru2, u)
                nlv2 = max(lv2, v - D)
                nrv2 = min(rv2, v)

                if nlu1 <= nru1 and nlv1 <= nrv1:
                    lu1, ru1, lv1, rv1 = nlu1, nru1, nlv1, nrv1
                else:
                    lu2, ru2, lv2, rv2 = nlu2, nru2, nlv2, nrv2

            elif in1:
                lu1 = max(lu1, u - D)
                ru1 = min(ru1, u)
                lv1 = max(lv1, v - D)
                rv1 = min(rv1, v)

            elif in2:
                lu2 = max(lu2, u - D)
                ru2 = min(ru2, u)
                lv2 = max(lv2, v - D)
                rv2 = min(rv2, v)

            else:
                if lu2 == INF:
                    lu2 = u - D
                    ru2 = u
                    lv2 = v - D
                    rv2 = v
                else:
                    return False

        return True

    lo, hi = -1, max(us[-1] - us[0], vs[-1] - vs[0])
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid

    print(hi)

if __name__ == "__main__":
    main()
