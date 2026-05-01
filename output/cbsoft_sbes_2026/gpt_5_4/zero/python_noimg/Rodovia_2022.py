import sys

sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    edges = set()

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        gr[b].append(a)
        edges.add((a, b))

    # Kosaraju iterative
    vis = [False] * N
    order = []

    for s in range(N):
        if vis[s]:
            continue
        stack = [(s, 0)]
        vis[s] = True
        while stack:
            v, i = stack[-1]
            if i < len(g[v]):
                to = g[v][i]
                stack[-1] = (v, i + 1)
                if not vis[to]:
                    vis[to] = True
                    stack.append((to, 0))
            else:
                order.append(v)
                stack.pop()

    comp = [-1] * N
    comp_cnt = 0

    for s in reversed(order):
        if comp[s] != -1:
            continue
        stack = [s]
        comp[s] = comp_cnt
        while stack:
            v = stack.pop()
            for to in gr[v]:
                if comp[to] == -1:
                    comp[to] = comp_cnt
                    stack.append(to)
        comp_cnt += 1

    # Representative vertex of each SCC
    rep = [-1] * comp_cnt
    size = [0] * comp_cnt
    for v in range(N):
        c = comp[v]
        if rep[c] == -1:
            rep[c] = v
        size[c] += 1

    # If some SCC has size >= 2, any missing edge inside it is redundant
    # Need a pair A != B without original edge A->B
    members = [[] for _ in range(comp_cnt)]
    for v in range(N):
        members[comp[v]].append(v)

    for c in range(comp_cnt):
        if size[c] >= 2:
            verts = members[c]
            if size[c] == 2:
                a, b = verts
                if (a, b) not in edges:
                    print(a + 1, b + 1)
                    return
                if (b, a) not in edges:
                    print(b + 1, a + 1)
                    return
            else:
                # In SCC with k>=3, if all ordered pairs existed it'd have k*(k-1) edges.
                # Since checking all pairs is expensive, use adjacency set membership while scanning.
                # Total scan over vertices of one SCC is acceptable because we stop at first missing pair.
                in_comp = set(verts)
                for a in verts:
                    cnt = 0
                    for b in g[a]:
                        if b in in_comp and b != a:
                            cnt += 1
                    if cnt < size[c] - 1:
                        neigh = set()
                        for b in g[a]:
                            if b in in_comp:
                                neigh.add(b)
                        for b in verts:
                            if b != a and b not in neigh:
                                print(a + 1, b + 1)
                                return

    # Build condensation DAG
    dag = [[] for _ in range(comp_cnt)]
    indeg = [0] * comp_cnt
    dag_edge_set = set()

    for a, b in edges:
        ca = comp[a]
        cb = comp[b]
        if ca != cb and (ca, cb) not in dag_edge_set:
            dag_edge_set.add((ca, cb))
            dag[ca].append(cb)
            indeg[cb] += 1

    # Topological order
    from collections import deque
    q = deque([i for i in range(comp_cnt) if indeg[i] == 0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in dag[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)

    K = comp_cnt

    # Bitset DP of reachability among SCCs in condensation DAG
    reach = [0] * K
    for v in reversed(topo):
        bits = 0
        for to in dag[v]:
            bits |= reach[to] | (1 << to)
        reach[v] = bits

    # Need pair of SCCs (u, v), u != v, no path u->v, and no direct edge u->v in original condensation
    # Then any representative vertices form a redundant new road.
    allmask = (1 << K) - 1
    for u in range(K):
        forbidden = reach[u] | (1 << u)
        missing = allmask ^ forbidden
        if missing:
            lsb = missing & -missing
            v = lsb.bit_length() - 1
            print(rep[u] + 1, rep[v] + 1)
            return

    print(-1)

if __name__ == "__main__":
    main()
