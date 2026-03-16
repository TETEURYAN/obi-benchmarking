import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    total = n * m
    vals = data[2:2 + total]

    parent = list(range(total))
    size = [1] * total
    sum_power = vals[:]
    active = [False] * total

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

    order = sorted(range(total), key=vals.__getitem__)
    ans = [0] * total

    i = 0
    while i < total:
        v = vals[order[i]]
        j = i
        while j < total and vals[order[j]] == v:
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
            k = i
            while k < j:
                idx = order[k]
                root = find(idx)
                if sum_power[root] >= 2 * v:
                    r = idx // m
                    c = idx - r * m

                    if r > 0:
                        nb = idx - m
                        if active[nb]:
                            ra = find(idx)
                            rb = find(nb)
                            if ra != rb:
                                if vals[rb] <= sum_power[ra]:
                                    union(ra, rb)
                                    changed = True
                    if r + 1 < n:
                        nb = idx + m
                        if active[nb]:
                            ra = find(idx)
                            rb = find(nb)
                            if ra != rb:
                                if vals[rb] <= sum_power[ra]:
                                    union(ra, rb)
                                    changed = True
                    if c > 0:
                        nb = idx - 1
                        if active[nb]:
                            ra = find(idx)
                            rb = find(nb)
                            if ra != rb:
                                if vals[rb] <= sum_power[ra]:
                                    union(ra, rb)
                                    changed = True
                    if c + 1 < m:
                        nb = idx + 1
                        if active[nb]:
                            ra = find(idx)
                            rb = find(nb)
                            if ra != rb:
                                if vals[rb] <= sum_power[ra]:
                                    union(ra, rb)
                                    changed = True
                k += 1

        k = i
        while k < j:
            idx = order[k]
            ans[idx] = sum_power[find(idx)]
            k += 1

        i = j

    out = []
    for r in range(n):
        row = ans[r * m:(r + 1) * m]
        out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()