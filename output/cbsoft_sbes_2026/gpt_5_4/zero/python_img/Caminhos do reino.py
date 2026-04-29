import sys

def main():
    input = sys.stdin.readline

    N = int(input())
    F = [0] + list(map(int, input().split()))

    indeg = [0] * (N + 1)
    rev = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        indeg[F[i]] += 1
        rev[F[i]].append(i)

    from collections import deque

    q = deque()
    removed = [False] * (N + 1)
    for i in range(1, N + 1):
        if indeg[i] == 0:
            q.append(i)

    while q:
        u = q.popleft()
        removed[u] = True
        v = F[u]
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

    on_cycle = [False] * (N + 1)
    cycle_nodes = []
    for i in range(1, N + 1):
        if not removed[i]:
            on_cycle[i] = True
            cycle_nodes.append(i)

    cycle_pos = [-1] * (N + 1)
    start = cycle_nodes[0]
    cur = start
    cycle_len = 0
    while True:
        cycle_pos[cur] = cycle_len
        cycle_len += 1
        cur = F[cur]
        if cur == start:
            break

    root = [0] * (N + 1)
    depth = [0] * (N + 1)

    LOG = (N).bit_length()
    up = [[0] * (N + 1) for _ in range(LOG)]

    dq = deque()
    for c in cycle_nodes:
        root[c] = c
        depth[c] = 0
        up[0][c] = 0
        dq.append(c)

    while dq:
        u = dq.popleft()
        for v in rev[u]:
            if on_cycle[v]:
                continue
            root[v] = root[u]
            depth[v] = depth[u] + 1
            up[0][v] = u
            dq.append(v)

    for k in range(1, LOG):
        prev = up[k - 1]
        curr = up[k]
        for i in range(1, N + 1):
            p = prev[i]
            curr[i] = prev[p] if p else 0

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        diff = depth[a] - depth[b]
        bit = 0
        while diff:
            if diff & 1:
                a = up[bit][a]
            diff >>= 1
            bit += 1
        if a == b:
            return a
        for k in range(LOG - 1, -1, -1):
            if up[k][a] != up[k][b]:
                a = up[k][a]
                b = up[k][b]
        return up[0][a]

    def cycle_dist(i, j):
        d = abs(i - j)
        return min(d, cycle_len - d)

    Q = int(input())
    out = []

    for _ in range(Q):
        A, B = map(int, input().split())

        if root[A] == root[B]:
            c = lca(A, B)
            ans = max(depth[A] - depth[c], depth[B] - depth[c])
        else:
            da = depth[A]
            db = depth[B]
            pa = cycle_pos[root[A]]
            pb = cycle_pos[root[B]]
            dc = cycle_dist(pa, pb)
            ans = max(da, db)
            if da < db + dc:
                ans = min(ans, (da + db + dc + 1) // 2)
            if db < da + dc:
                ans = min(ans, (da + db + dc + 1) // 2)
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
