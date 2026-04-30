
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    adj_rev = [[] for _ in range(n+1)]
    edges = set()
    for _ in range(m):
        x = int(next(it))
        y = int(next(it))
        adj[x].append(y)
        adj_rev[y].append(x)
        edges.add((x, y))

    visited = [False] * (n+1)
    order = []
    def dfs(u):
        stack = [u]
        visited[u] = True
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
            order.append(node)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    visited = [False] * (n+1)
    scc = [0] * (n+1)
    scc_count = 0
    order.reverse()
    for node in order:
        if not visited[node]:
            stack = [node]
            visited[node] = True
            component = []
            while stack:
                u = stack.pop()
                component.append(u)
                for v in adj_rev[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            scc_count += 1
            for u in component:
                scc[u] = scc_count

    if scc_count == n:
        print(-1)
        return

    scc_adj = [[] for _ in range(scc_count+1)]
    scc_adj_rev = [[] for _ in range(scc_count+1)]
    scc_in_degree = [0] * (scc_count+1)
    scc_out_degree = [0] * (scc_count+1)
    scc_nodes = [[] for _ in range(scc_count+1)]
    for u in range(1, n+1):
        scc_nodes[scc[u]].append(u)
        for v in adj[u]:
            if scc[u] != scc[v]:
                scc_adj[scc[u]].append(scc[v])
                scc_adj_rev[scc[v]].append(scc[u])

    for u in range(1, scc_count+1):
        scc_out_degree[u] = len(set(scc_adj[u]))
        for v in scc_adj[u]:
            scc_in_degree[v] += 1

    sources = []
    sinks = []
    for u in range(1, scc_count+1):
        if scc_in_degree[u] == 0:
            sources.append(u)
        if scc_out_degree[u] == 0:
            sinks.append(u)

    if not sources or not sinks:
        print(-1)
        return

    source = sources[0]
    sink = sinks[0]

    for u in scc_nodes[source]:
        for v in scc_nodes[sink]:
            if (u, v) not in edges:
                print(u, v)
                return

    print(-1)

if __name__ == "__main__":
    main()
