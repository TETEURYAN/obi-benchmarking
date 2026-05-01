import sys

sys.setrecursionlimit(1_000_000)

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

    # Remove peripheral nodes to identify the unique cycle
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

    in_cycle = [False] * (N + 1)
    cycle_nodes = []
    for i in range(1, N + 1):
        if not removed[i]:
            in_cycle[i] = True
            cycle_nodes.append(i)

    # Order cycle
    start = cycle_nodes[0]
    cycle = []
    pos = {}
    cur = start
    idx = 0
    while True:
        cycle.append(cur)
        pos[cur] = idx
        idx += 1
        cur = F[cur]
        if cur == start:
            break
    C = len(cycle)

    # For each node: root cycle node and distance to cycle
    root = [0] * (N + 1)
    depth = [0] * (N + 1)

    # Binary lifting on peripheral trees (parent towards cycle)
    LOG = (N).bit_length()
    up = [[0] * (N + 1) for _ in range(LOG)]

    dq = deque()
    for c in cycle:
        root[c] = c
        depth[c] = 0
        up[0][c] = 0
        dq.append(c)

    while dq:
        u = dq.popleft()
        for v in rev[u]:
            if in_cycle[v]:
                continue
            root[v] = root[u]
            depth[v] = depth[u] + 1
            up[0][v] = u
            dq.append(v)

    for k in range(1, LOG):
        uk = up[k - 1]
        uk2 = up[k]
        for v in range(1, N + 1):
            p = uk[v]
            uk2[v] = uk[p] if p else 0

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

    Q = int(input())
    out = []

    for _ in range(Q):
        A, B = map(int, input().split())

        if root[A] == root[B]:
            x = lca(A, B)
            ans = max(depth[A] - depth[x], depth[B] - depth[x])
        else:
            da = depth[A]
            db = depth[B]
            pa = pos[root[A]]
            pb = pos[root[B]]
            d = abs(pa - pb)
            cyc = d if d < C - d else C - d
            ans = max(da, db) + (cyc + abs(da - db)) // 2

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
