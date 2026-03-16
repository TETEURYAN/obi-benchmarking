import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
vals = data[2:]
k = n * m

parent = list(range(k))
size = [1] * k
sum_power = vals[:]
active = [False] * k
ans = [0] * k

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return ra
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    sum_power[ra] += sum_power[rb]
    return ra

order = sorted(range(k), key=lambda i: vals[i])
i = 0

while i < k:
    v = vals[order[i]]
    j = i
    while j < k and vals[order[j]] == v:
        idx = order[j]
        active[idx] = True
        r = idx // m
        c = idx - r * m

        if r > 0:
            nb = idx - m
            if active[nb]:
                union(idx, nb)
        if r + 1 < n:
            nb = idx + m
            if active[nb]:
                union(idx, nb)
        if c > 0:
            nb = idx - 1
            if active[nb]:
                union(idx, nb)
        if c + 1 < m:
            nb = idx + 1
            if active[nb]:
                union(idx, nb)
        j += 1

    changed = True
    while changed:
        changed = False
        t = i
        while t < j:
            idx = order[t]
            r0 = find(idx)
            s = sum_power[r0]
            rr = idx // m
            cc = idx - rr * m

            if rr > 0:
                nb = idx - m
                if active[nb]:
                    rb = find(nb)
                    if rb != r0 and vals[rb] <= s:
                        r0 = union(r0, rb)
                        s = sum_power[r0]
                        changed = True
            if rr + 1 < n:
                nb = idx + m
                if active[nb]:
                    rb = find(nb)
                    if rb != r0 and vals[rb] <= s:
                        r0 = union(r0, rb)
                        s = sum_power[r0]
                        changed = True
            if cc > 0:
                nb = idx - 1
                if active[nb]:
                    rb = find(nb)
                    if rb != r0 and vals[rb] <= s:
                        r0 = union(r0, rb)
                        s = sum_power[r0]
                        changed = True
            if cc + 1 < m:
                nb = idx + 1
                if active[nb]:
                    rb = find(nb)
                    if rb != r0 and vals[rb] <= s:
                        r0 = union(r0, rb)
                        s = sum_power[r0]
                        changed = True
            t += 1

    roots_done = set()
    t = i
    while t < j:
        r0 = find(order[t])
        roots_done.add(r0)
        t += 1
    for r0 in roots_done:
        ans[r0] = sum_power[r0]

    i = j

for idx in range(k):
    ans[idx] = ans[find(idx)]

out = []
for r in range(n):
    base = r * m
    out.append(' '.join(str(ans[base + c]) for c in range(m)))
sys.stdout.write('\n'.join(out))