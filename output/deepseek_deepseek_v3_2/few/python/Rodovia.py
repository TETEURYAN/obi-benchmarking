import sys
sys.setrecursionlimit(300000)

def kosaraju(n, adj, radj):
    visited = [False] * (n + 1)
    order = []
    def dfs(v):
        visited[v] = True
        for to in adj[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(v)
    comp = [-1] * (n + 1)
    def rdfs(v, label):
        comp[v] = label
        for to in radj[v]:
            if comp[to] == -1:
                rdfs(to, label)
    label = 0
    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, label)
            label += 1
    return comp, label

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        radj[v].append(u)
        edges.append((u, v))
    comp, num_comp = kosaraju(n, adj, radj)
    if num_comp == 1:
        print(-1)
        return
    comp_adj = [set() for _ in range(num_comp)]
    for u, v in edges:
        cu, cv = comp[u], comp[v]
        if cu != cv:
            comp_adj[cu].add(cv)
    out_deg = [len(comp_adj[i]) for i in range(num_comp)]
    zero_out = [i for i in range(num_comp) if out_deg[i] == 0]
    if not zero_out:
        print(-1)
        return
    sink = zero_out[0]
    source_candidates = [i for i in range(num_comp) if i != sink and out_deg[i] > 0]
    if not source_candidates:
        print(-1)
        return
    source = source_candidates[0]
    nodes_in_sink = [v for v in range(1, n + 1) if comp[v] == sink]
    nodes_in_source = [v for v in range(1, n + 1) if comp[v] == source]
    a = nodes_in_source[0]
    b = nodes_in_sink[0]
    existing = set(edges)
    if (a, b) in existing:
        if len(nodes_in_source) > 1:
            a = nodes_in_source[1]
        elif len(nodes_in_sink) > 1:
            b = nodes_in_sink[1]
        else:
            print(-1)
            return
    print(a, b)

if __name__ == "__main__":
    main()