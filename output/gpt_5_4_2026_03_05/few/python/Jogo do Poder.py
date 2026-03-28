import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n = data[0]
m = data[1]
tot = n * m
p = data[2:2 + tot]

parent = list(range(tot))
size = [1] * tot
active = [False] * tot
sum_power = [0] * tot
ans = [0] * tot

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

order = sorted(range(tot), key=lambda i: p[i])

i = 0
while i < tot:
    v = p[order[i]]
    j = i
    while j < tot and p[order[j]] == v:
        idx = order[j]
        active[idx] = True
        parent[idx] = idx
        size[idx] = 1
        sum_power[idx] = p[idx]
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
        k = j
        while k < tot:
            idx = order[k]
            val = p[idx]
            root = find(idx)
            if sum_power[root] >= val:
                t = k
                while t < tot and p[order[t]] == val:
                    idx2 = order[t]
                    root2 = find(idx2)
                    if sum_power[root2] >= val:
                        ans[idx2] = sum_power[root2]
                        t += 1
                    else:
                        break
                if t == k:
                    break
                while k < t:
                    idx2 = order[k]
                    r = idx2 // m
                    c = idx2 - r * m
                    if r > 0:
                        nb = idx2 - m
                        if active[nb]:
                            union(idx2, nb)
                    if r + 1 < n:
                        nb = idx2 + m
                        if active[nb]:
                            union(idx2, nb)
                    if c > 0:
                        nb = idx2 - 1
                        if active[nb]:
                            union(idx2, nb)
                    if c + 1 < m:
                        nb = idx2 + 1
                        if active[nb]:
                            union(idx2, nb)
                    k += 1
                changed = True
            else:
                k += 1

    for k in range(i, j):
        idx = order[k]
        root = find(idx)
        ans[idx] = sum_power[root]

    i = j

out = []
for r in range(n):
    base = r * m
    out.append(' '.join(str(ans[base + c]) for c in range(m)))
sys.stdout.write('\n'.join(out))