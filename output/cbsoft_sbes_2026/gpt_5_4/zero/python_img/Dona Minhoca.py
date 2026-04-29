import sys
sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        g[x].append(y)
        g[y].append(x)

    if n == 1:
        print(1)
        print(0)
        return

    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = -2
    while stack:
        u = stack.pop()
        order.append(u)
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)

    down_len = [0] * n
    down_cnt = [0] * n

    for u in reversed(order):
        best_len = 0
        best_cnt = 1
        has_child = False
        for v in g[u]:
            if v == parent[u]:
                continue
            has_child = True
            cand = down_len[v] + 1
            cnt = down_cnt[v]
            if cand > best_len:
                best_len = cand
                best_cnt = cnt
            elif cand == best_len:
                best_cnt += cnt
        if has_child:
            down_len[u] = best_len
            down_cnt[u] = best_cnt
        else:
            down_len[u] = 0
            down_cnt[u] = 1

    up_len = [-1] * n
    up_cnt = [0] * n
    up_len[0] = -1
    up_cnt[0] = 0

    for u in order:
        items = []
        if up_len[u] >= 0:
            items.append((up_len[u], up_cnt[u], -1))
        for v in g[u]:
            if v == parent[u]:
                continue
            items.append((down_len[v] + 1, down_cnt[v], v))

        m = len(items)
        pref_len = [-1] * m
        pref_cnt = [0] * m
        for i, (l, c, _) in enumerate(items):
            if i == 0:
                pref_len[i] = l
                pref_cnt[i] = c
            else:
                if l > pref_len[i - 1]:
                    pref_len[i] = l
                    pref_cnt[i] = c
                elif l == pref_len[i - 1]:
                    pref_len[i] = l
                    pref_cnt[i] = pref_cnt[i - 1] + c
                else:
                    pref_len[i] = pref_len[i - 1]
                    pref_cnt[i] = pref_cnt[i - 1]

        suff_len = [-1] * m
        suff_cnt = [0] * m
        for i in range(m - 1, -1, -1):
            l, c, _ = items[i]
            if i == m - 1:
                suff_len[i] = l
                suff_cnt[i] = c
            else:
                if l > suff_len[i + 1]:
                    suff_len[i] = l
                    suff_cnt[i] = c
                elif l == suff_len[i + 1]:
                    suff_len[i] = l
                    suff_cnt[i] = suff_cnt[i + 1] + c
                else:
                    suff_len[i] = suff_len[i + 1]
                    suff_cnt[i] = suff_cnt[i + 1]

        idx = 0
        if up_len[u] >= 0:
            idx = 1
        for v in g[u]:
            if v == parent[u]:
                continue
            best_l = -1
            best_c = 0

            left = idx - 1
            right = idx + 1

            if left >= 0:
                best_l = pref_len[left]
                best_c = pref_cnt[left]
            if right < m:
                l2 = suff_len[right]
                c2 = suff_cnt[right]
                if l2 > best_l:
                    best_l = l2
                    best_c = c2
                elif l2 == best_l and l2 >= 0:
                    best_c += c2

            if best_l == -1:
                up_len[v] = 1
                up_cnt[v] = 1
            else:
                up_len[v] = best_l + 1
                up_cnt[v] = best_c
            idx += 1

    ecc = [0] * n
    for u in range(n):
        ecc[u] = max(down_len[u], up_len[u])

    D = max(ecc)
    centers = [u for u in range(n) if ecc[u] == D]

    if len(centers) == 1:
        c = centers[0]
        branch_counts = []
        total = 0
        for v in g[c]:
            if v == parent[c]:
                dist = up_len[c]
                cnt = up_cnt[c]
            else:
                dist = down_len[v] + 1
                cnt = down_cnt[v]
            if dist == D:
                branch_counts.append(cnt)
                total += cnt

        ways = 0
        pref = 0
        for cnt in branch_counts:
            ways += pref * cnt
            pref += cnt

        print(D + 1)
        print(ways)
    else:
        a, b = centers[0], centers[1]

        def side_count(center, blocked):
            total = 0
            for v in g[center]:
                if v == blocked:
                    continue
                if v == parent[center]:
                    dist = up_len[center]
                    cnt = up_cnt[center]
                else:
                    dist = down_len[v] + 1
                    cnt = down_cnt[v]
                if dist == D - 1:
                    total += cnt
            return total

        ca = side_count(a, b)
        cb = side_count(b, a)

        print(D + 1)
        print(ca * cb)

if __name__ == "__main__":
    main()
