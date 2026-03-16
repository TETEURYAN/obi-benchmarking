import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    vals = data[2:]
    k = n * m

    parent = list(range(k))
    size = [1] * k
    active = [False] * k
    comp_sum = [0] * k
    comp_ans = [0] * k
    comp_min = [0] * k
    comp_max = [0] * k

    for i, v in enumerate(vals):
        comp_sum[i] = v
        comp_min[i] = v
        comp_max[i] = v

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
        comp_sum[ra] += comp_sum[rb]
        if comp_min[rb] < comp_min[ra]:
            comp_min[ra] = comp_min[rb]
        if comp_max[rb] > comp_max[ra]:
            comp_max[ra] = comp_max[rb]
        return ra

    order = sorted(range(k), key=vals.__getitem__)
    pos = 0

    while pos < k:
        v = vals[order[pos]]
        start = pos
        while pos < k and vals[order[pos]] == v:
            idx = order[pos]
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

            pos += 1

        roots = []
        seen = set()
        for t in range(start, pos):
            rt = find(order[t])
            if rt not in seen:
                seen.add(rt)
                roots.append(rt)

        changed = True
        while changed:
            changed = False
            for r in roots:
                rr = find(r)
                if rr != r:
                    continue
                if comp_ans[rr] == 0 and comp_sum[rr] >= comp_max[rr]:
                    comp_ans[rr] = comp_sum[rr]
                    changed = True

            if not changed:
                break

            for r in roots:
                rr = find(r)
                if rr != r:
                    continue
                if comp_ans[rr] == 0:
                    continue
                mn = comp_min[rr]
                if mn == 1:
                    continue

                while True:
                    target = mn - 1
                    if target < 0 or not active[target]:
                        break
                    rt = find(target)
                    rr2 = find(rr)
                    if rt == rr2:
                        break
                    if comp_ans[rt] == 0:
                        break
                    newr = union(rr2, rt)
                    comp_ans[newr] = comp_sum[newr]
                    rr = newr
                    mn = comp_min[rr]
                    changed = True
                    if mn == 1:
                        break

        # compress roots list representatives after possible merges
        # no action needed here

    root_to_answer = {}
    ans = [0] * k
    for i in range(k):
        r = find(i)
        if r not in root_to_answer:
            root_to_answer[r] = comp_ans[r] if comp_ans[r] != 0 else vals[i]
        ans[i] = root_to_answer[r]

    out = []
    for i in range(n):
        row = ans[i*m:(i+1)*m]
        out.append(' '.join(map(str, row)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()