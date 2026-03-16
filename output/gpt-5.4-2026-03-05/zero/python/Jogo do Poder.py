import sys
sys.setrecursionlimit(1_000_000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    N, M = data[0], data[1]
    A = data[2:]
    n = N * M

    parent = list(range(n))
    size = [1] * n
    active = [False] * n
    comp_sum = [0] * n
    comp_ans = [0] * n
    comp_nodes = [[] for _ in range(n)]

    for i, v in enumerate(A):
        comp_sum[i] = v
        comp_nodes[i].append(i)

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
        if len(comp_nodes[ra]) < len(comp_nodes[rb]):
            comp_nodes[ra], comp_nodes[rb] = comp_nodes[rb], comp_nodes[ra]
        comp_nodes[ra].extend(comp_nodes[rb])
        comp_nodes[rb] = []
        return ra

    order = sorted(range(n), key=A.__getitem__)
    ans = [0] * n

    i = 0
    while i < n:
        v = A[order[i]]
        j = i
        while j < n and A[order[j]] == v:
            idx = order[j]
            active[idx] = True
            r = idx // M
            c = idx - r * M
            if r > 0:
                nb = idx - M
                if active[nb]:
                    union(idx, nb)
            if r + 1 < N:
                nb = idx + M
                if active[nb]:
                    union(idx, nb)
            if c > 0:
                nb = idx - 1
                if active[nb]:
                    union(idx, nb)
            if c + 1 < M:
                nb = idx + 1
                if active[nb]:
                    union(idx, nb)
            j += 1

        roots = set()
        for k in range(i, j):
            roots.add(find(order[k]))

        changed = True
        while changed:
            changed = False
            root_list = list(roots)
            for r in root_list:
                rr = find(r)
                if rr != r:
                    roots.discard(r)
                    roots.add(rr)
                    continue
                total = comp_sum[rr]
                nodes = comp_nodes[rr]
                merged = False
                for idx in nodes:
                    row = idx // M
                    col = idx - row * M
                    if row > 0:
                        nb = idx - M
                        if not active[nb] and A[nb] <= total:
                            active[nb] = True
                            nr = union(rr, nb)
                            roots.discard(rr)
                            roots.add(find(nr))
                            changed = True
                            merged = True
                    if row + 1 < N:
                        nb = idx + M
                        if not active[nb] and A[nb] <= total:
                            active[nb] = True
                            nr = union(rr, nb)
                            roots.discard(rr)
                            roots.add(find(nr))
                            changed = True
                            merged = True
                    if col > 0:
                        nb = idx - 1
                        if not active[nb] and A[nb] <= total:
                            active[nb] = True
                            nr = union(rr, nb)
                            roots.discard(rr)
                            roots.add(find(nr))
                            changed = True
                            merged = True
                    if col + 1 < M:
                        nb = idx + 1
                        if not active[nb] and A[nb] <= total:
                            active[nb] = True
                            nr = union(rr, nb)
                            roots.discard(rr)
                            roots.add(find(nr))
                            changed = True
                            merged = True
                    if merged:
                        break
                if changed:
                    break

        for r in roots:
            rr = find(r)
            val = comp_sum[rr]
            for idx in comp_nodes[rr]:
                if ans[idx] == 0:
                    ans[idx] = val

        i = j

    out = []
    for r in range(N):
        base = r * M
        out.append(' '.join(map(str, ans[base:base + M])))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
