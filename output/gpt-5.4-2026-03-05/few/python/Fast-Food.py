import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n = data[0]
xs = data[1:1+n]
ys = data[1+n:1+2*n]

u = [xs[i] + ys[i] for i in range(n)]
v = [xs[i] - ys[i] for i in range(n)]

umin = min(u)
umax = max(u)
vmin = min(v)
vmax = max(v)

lo = 0
hi = max(umax - umin, vmax - vmin)

def feasible(D):
    Lu1 = umax - D
    Ru1 = umin + D
    Lv1 = vmax - D
    Rv1 = vmin + D

    if Lu1 <= Ru1 and Lv1 <= Rv1:
        return True

    Lu2 = Lu1
    Ru2 = Ru1
    Lv2 = -10**30
    Rv2 = 10**30

    Lu3 = -10**30
    Ru3 = 10**30
    Lv3 = Lv1
    Rv3 = Rv1

    Lu4 = Lu1
    Ru4 = Ru1
    Lv4 = Lv1
    Rv4 = Rv1

    c2 = c3 = c4 = 0

    for i in range(n):
        ui = u[i]
        vi = v[i]

        in2 = (Lu2 <= ui <= Ru2)
        in3 = (Lv3 <= vi <= Rv3)
        in4 = (Lu4 <= ui <= Ru4 and Lv4 <= vi <= Rv4)

        if in2:
            c2 += 1
        if in3:
            c3 += 1
        if in4:
            c4 += 1

    return c2 == 0 or c3 == 0 or c4 == 0

while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)