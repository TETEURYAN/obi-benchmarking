import sys
sys.setrecursionlimit(200000)

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
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)

    down_len = [0] * n
    down_cnt = [1] * n

    for u in reversed(order):
        best_len = 0
        best_cnt = 1
        has_child = False
        for v in g[u]:
            if parent[v] == u:
                has_child = True
                cand = down_len[v] + 1
                if cand > best_len:
                    best_len = cand
                    best_cnt = down_cnt[v]
                elif cand == best_len:
                    best_cnt += down_cnt[v]
        if has_child:
            down_len[u] = best_len
            down_cnt[u] = best_cnt
        else:
            down_len[u] = 0
            down_cnt[u] = 1

    up_len = [-1] * n
    up_cnt = [0] * n

    for u in order:
        vals = []
        cnts = []
        srcs = []

        if up_len[u] >= 0:
            vals.append(up_len[u])
            cnts.append(up_cnt[u])
            srcs.append(-1)

        for v in g[u]:
            if parent[v] == u:
                vals.append(down_len[v] + 1)
                cnts.append(down_cnt[v])
                srcs.append(v)

        m = len(vals)
        if m == 0:
            continue

        pref_max = [0] * m
        pref_cnt = [0] * m
        pref_ways = [0] * m

        cur_max = -1
        cur_cnt = 0
        cur_ways = 0
        for i in range(m):
            val = vals[i]
            cnt = cnts[i]
            if val > cur_max:
                cur_max = val
                cur_cnt = 1
                cur_ways = cnt
            elif val == cur_max:
                cur_cnt += 1
                cur_ways += cnt
            pref_max[i] = cur_max
            pref_cnt[i] = cur_cnt
            pref_ways[i] = cur_ways

        suf_max = [0] * m
        suf_cnt = [0] * m
        suf_ways = [0] * m

        cur_max = -1
        cur_cnt = 0
        cur_ways = 0
        for i in range(m - 1, -1, -1):
            val = vals[i]
            cnt = cnts[i]
            if val > cur_max:
                cur_max = val
                cur_cnt = 1
                cur_ways = cnt
            elif val == cur_max:
                cur_cnt += 1
                cur_ways += cnt
            suf_max[i] = cur_max
            suf_cnt[i] = cur_cnt
            suf_ways[i] = cur_ways

        child_index = {}
        for i, s in enumerate(srcs):
            if s != -1:
                child_index[s] = i

        for v in g[u]:
            if parent[v] != u:
                continue
            idx = child_index[v]

            best_len = -1
            best_cnt_sources = 0
            best_ways = 0

            if idx > 0:
                best_len = pref_max[idx - 1]
                best_cnt_sources = pref_cnt[idx - 1]
                best_ways = pref_ways[idx - 1]

            if idx + 1 < m:
                rlen = suf_max[idx + 1]
                rcnt = suf_cnt[idx + 1]
                rways = suf_ways[idx + 1]
                if rlen > best_len:
                    best_len = rlen
                    best_cnt_sources = rcnt
                    best_ways = rways
                elif rlen == best_len:
                    best_cnt_sources += rcnt
                    best_ways += rways

            if best_len == -1:
                up_len[v] = 1
                up_cnt[v] = 1
            else:
                up_len[v] = best_len + 1
                up_cnt[v] = best_ways

    ecc = [0] * n
    for u in range(n):
        if up_len[u] > down_len[u]:
            ecc[u] = up_len[u]
        else:
            ecc[u] = down_len[u]

    diameter_edges = max(ecc)
    diameter_vertices = diameter_edges + 1

    count_centers = 0
    center = -1
    for u in range(n):
        if ecc[u] == diameter_edges // 2 and diameter_edges % 2 == 0:
            count_centers += 1
            center = u

    if diameter_edges % 2 == 0 and count_centers == 1:
        D = diameter_edges
        target = D // 2

        branch_counts = []
        for v in g[center]:
            if parent[v] == center:
                dist = down_len[v] + 1
                cnt = down_cnt[v]
            else:
                dist = up_len[center] - 1 if up_len[center] >= 1 else -1
                cnt = up_cnt[center] if up_len[center] >= 1 else 0
                if parent[center] != v:
                    dist = -1
                    cnt = 0
            if dist == target:
                branch_counts.append(cnt)

        total = 0
        ans_count = 0
        for c in branch_counts:
            ans_count += total * c
            total += c
    else:
        a = b = -1
        for u in range(n):
            for v in g[u]:
                if u < v:
                    if ecc[u] == diameter_edges // 2 and ecc[v] == diameter_edges // 2 and ecc[u] + ecc[v] + 1 == diameter_edges:
                        a, b = u, v
                        break
            if a != -1:
                break

        def count_side(start, blocked, target):
            stack = [(start, blocked, 0)]
            cnt = 0
            while stack:
                u, p, d = stack.pop()
                if d == target:
                    cnt += 1
                    continue
                for w in g[u]:
                    if w != p:
                        stack.append((w, u, d + 1))
            return cnt

        target = diameter_edges // 2
        ca = count_side(a, b, target)
        cb = count_side(b, a, target)
        ans_count = ca * cb

    print(diameter_vertices)
    print(ans_count)

if __name__ == "__main__":
    main()
