import sys
sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    edges = set()
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        g[x].append(y)
        gr[y].append(x)
        edges.add((x, y))

    visited = [False] * N
    order = []

    for s in range(N):
        if visited[s]:
            continue
        stack = [(s, 0)]
        visited[s] = True
        while stack:
            v, i = stack[-1]
            if i < len(g[v]):
                to = g[v][i]
                stack[-1] = (v, i + 1)
                if not visited[to]:
                    visited[to] = True
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

    comps = [[] for _ in range(comp_cnt)]
    for v in range(N):
        comps[comp[v]].append(v)

    if comp_cnt < N:
        for nodes in comps:
            if len(nodes) >= 2:
                a = nodes[0]
                for b in nodes[1:]:
                    if (a, b) not in edges:
                        print(a + 1, b + 1)
                        return
                    if (b, a) not in edges:
                        print(b + 1, a + 1)
                        return

    dag = [[] for _ in range(comp_cnt)]
    indeg = [0] * comp_cnt
    seen_dag = set()
    for u in range(N):
        cu = comp[u]
        for v in g[u]:
            cv = comp[v]
            if cu != cv and (cu, cv) not in seen_dag:
                seen_dag.add((cu, cv))
                dag[cu].append(cv)
                indeg[cv] += 1

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

    bitsets = [0] * comp_cnt
    for c in reversed(topo):
        bs = 1 << c
        for to in dag[c]:
            bs |= bitsets[to]
        bitsets[c] = bs

    for i in range(comp_cnt):
        bi = bitsets[i]
        for j in range(comp_cnt):
            if i == j:
                continue
            if ((bi >> j) & 1) == 0:
                a = comps[i][0]
                b = comps[j][0]
                print(a + 1, b + 1)
                return

    print(-1)

if __name__ == "__main__":
    main()