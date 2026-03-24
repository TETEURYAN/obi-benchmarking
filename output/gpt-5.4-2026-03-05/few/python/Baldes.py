import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

it = iter(data)
n = next(it)
m = next(it)

INF = 10**30

size = 1
while size < n:
    size <<= 1

mn1 = [INF] * (2 * size)
mx1 = [-INF] * (2 * size)
mn2 = [INF] * (2 * size)
mx2 = [-INF] * (2 * size)

bucket_min = [0] * (n + 1)
bucket_max = [0] * (n + 1)

for i in range(1, n + 1):
    x = next(it)
    bucket_min[i] = x
    bucket_max[i] = x
    p = size + i - 1
    mn1[p] = x
    mx1[p] = x

for p in range(size - 1, 0, -1):
    l = p << 1
    r = l | 1

    a1, a2 = mn1[l], mn1[r]
    if a1 <= a2:
        mn1[p], mn2[p] = a1, min(mn2[l], a2)
    else:
        mn1[p], mn2[p] = a2, min(a1, mn2[r])

    b1, b2 = mx1[l], mx1[r]
    if b1 >= b2:
        mx1[p], mx2[p] = b1, max(mx2[l], b2)
    else:
        mx1[p], mx2[p] = b2, max(b1, mx2[r])

def update(pos, val):
    if val < bucket_min[pos]:
        bucket_min[pos] = val
    if val > bucket_max[pos]:
        bucket_max[pos] = val
    p = size + pos - 1
    mn1[p] = bucket_min[pos]
    mx1[p] = bucket_max[pos]
    p >>= 1
    while p:
        l = p << 1
        r = l | 1

        a1, a2 = mn1[l], mn1[r]
        if a1 <= a2:
            mn1[p], mn2[p] = a1, min(mn2[l], a2)
        else:
            mn1[p], mn2[p] = a2, min(a1, mn2[r])

        b1, b2 = mx1[l], mx1[r]
        if b1 >= b2:
            mx1[p], mx2[p] = b1, max(mx2[l], b2)
        else:
            mx1[p], mx2[p] = b2, max(b1, mx2[r])

        p >>= 1

def query(lq, rq):
    l = lq + size - 1
    r = rq + size - 1

    minv = INF
    minidx = -1
    second_min = INF

    maxv = -INF
    maxidx = -1
    second_max = -INF

    while l <= r:
        if l & 1:
            v = mn1[l]
            if v < minv:
                second_min = min(second_min, minv, mn2[l])
                minv = v
                minidx = l
            else:
                second_min = min(second_min, v, mn2[l])

            v = mx1[l]
            if v > maxv:
                second_max = max(second_max, maxv, mx2[l])
                maxv = v
                maxidx = l
            else:
                second_max = max(second_max, v, mx2[l])
            l += 1

        if not (r & 1):
            v = mn1[r]
            if v < minv:
                second_min = min(second_min, minv, mn2[r])
                minv = v
                minidx = r
            else:
                second_min = min(second_min, v, mn2[r])

            v = mx1[r]
            if v > maxv:
                second_max = max(second_max, maxv, mx2[r])
                maxv = v
                maxidx = r
            else:
                second_max = max(second_max, v, mx2[r])
            r -= 1

        l >>= 1
        r >>= 1

    if minidx != maxidx:
        return maxv - minv
    a = maxv - second_min
    b = second_max - minv
    if a < 0:
        a = -INF
    if b < 0:
        b = -INF
    return a if a > b else b

out = []
for _ in range(m):
    t = next(it)
    x = next(it)
    y = next(it)
    if t == 1:
        p = x
        i = y
        update(i, p)
    else:
        a = x
        b = y
        out.append(str(query(a, b)))

sys.stdout.write("\n".join(out))