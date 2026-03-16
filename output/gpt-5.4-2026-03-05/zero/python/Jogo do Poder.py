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

    for i in range(n):
        comp_sum[i] = A[i]
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
        comp_nodes[rb].clear()
        return ra

    order = sorted(range(n), key=A.__getitem__)
    ans = [0] * n

    idx = 0
    while idx < n:
        v = A[order[idx]]
        j = idx
        while j < n and A[order[j]] == v:
            j += 1

        for k in range(idx, j):
            x = order[k]
            active[x] = True
            r = x // M
            c = x - r * M
            if r > 0:
                y = x - M
                if active[y]:
                    union(x, y)
            if r + 1 < N:
                y = x + M
                if active[y]:
                    union(x, y)
            if c > 0:
                y = x - 1
                if active[y]:
                    union(x, y)
            if c + 1 < M:
                y = x + 1
                if active[y]:
                    union(x, y)

        roots = set()
        for k in range(idx, j):
            roots.add(find(order[k]))

        changed = True
        while changed:
            changed = False
            for r in list(roots):
                rr = find(r)
                if rr != r:
                    roots.discard(r)
                    roots.add(rr)
                    continue
                if comp_ans[rr] == 0 and comp_sum[rr] >= 2 * v:
                    comp_ans[rr] = comp_sum[rr]
                    changed = True
                    nodes = comp_nodes[rr]
                    t = 0
                    while t < len(nodes):
                        x = nodes[t]
                        row = x // M
                        col = x - row * M
                        if row > 0:
                            y = x - M
                            if active[y]:
                                ry = find(y)
                                if ry != rr and comp_ans[ry] != 0 and comp_ans[ry] <= comp_sum[rr]:
                                    rr = union(rr, ry)
                                    roots.add(rr)
                        if row + 1 < N:
                            y = x + M
                            if active[y]:
                                ry = find(y)
                                if ry != rr and comp_ans[ry] != 0 and comp_ans[ry] <= comp_sum[rr]:
                                    rr = union(rr, ry)
                                    roots.add(rr)
                        if col > 0:
                            y = x - 1
                            if active[y]:
                                ry = find(y)
                                if ry != rr and comp_ans[ry] != 0 and comp_ans[ry] <= comp_sum[rr]:
                                    rr = union(rr, ry)
                                    roots.add(rr)
                        if col + 1 < M:
                            y = x + 1
                            if active[y]:
                                ry = find(y)
                                if ry != rr and comp_ans[ry] != 0 and comp_ans[ry] <= comp_sum[rr]:
                                    rr = union(rr, ry)
                                    roots.add(rr)
                        t += 1
                    comp_ans[rr] = comp_sum[rr]

        idx = j

    for i in range(n):
        r = find(i)
        ans[i] = comp_ans[r] if comp_ans[r] else A[i]

    out = []
    for i in range(N):
        base = i * M
        out.append(" ".join(map(str, ans[base:base + M])))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
