import sys
sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.extend(map(int, input().split()))
    K = N * M

    parent = list(range(K))
    size = [1] * K
    active = [False] * K
    comp_sum = [0] * K
    comp_ans = [0] * K
    members = [[] for _ in range(K)]

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
        if len(members[ra]) < len(members[rb]):
            members[ra], members[rb] = members[rb], members[ra]
        members[ra].extend(members[rb])
        members[rb].clear()
        return ra

    order = sorted(range(K), key=lambda i: A[i])
    idx = 0

    while idx < K:
        v = A[order[idx]]
        j = idx
        while j < K and A[order[j]] == v:
            x = order[j]
            active[x] = True
            parent[x] = x
            size[x] = 1
            comp_sum[x] = v
            members[x] = [x]
            r = x // M
            c = x % M
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
            j += 1

        changed = True
        while changed:
            changed = False
            roots = set()
            for t in range(idx, j):
                roots.add(find(order[t]))
            for r in list(roots):
                if find(r) != r:
                    continue
                if comp_sum[r] >= 2 * v:
                    comp_ans[r] = comp_sum[r]
                    changed = True
                    cur = members[r][:]
                    for x in cur:
                        rr = x // M
                        cc = x % M
                        if rr > 0:
                            y = x - M
                            if active[y]:
                                nr = find(y)
                                if nr != find(r):
                                    union(r, nr)
                        if rr + 1 < N:
                            y = x + M
                            if active[y]:
                                nr = find(y)
                                if nr != find(r):
                                    union(r, nr)
                        if cc > 0:
                            y = x - 1
                            if active[y]:
                                nr = find(y)
                                if nr != find(r):
                                    union(r, nr)
                        if cc + 1 < M:
                            y = x + 1
                            if active[y]:
                                nr = find(y)
                                if nr != find(r):
                                    union(r, nr)
        idx = j

    ans = [0] * K
    seen = {}
    for i in range(K):
        r = find(i)
        if r not in seen:
            total = comp_sum[r]
            for x in members[r]:
                ans[x] = total

    out = []
    for i in range(N):
        out.append(" ".join(map(str, ans[i*M:(i+1)*M])))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
