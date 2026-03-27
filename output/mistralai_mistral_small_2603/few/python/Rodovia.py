
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

    adj = [[] for _ in range(n + 1)]
    adj_rev = [[] for _ in range(n + 1)]
    edges = set()

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj_rev[v].append(u)
        edges.add((u, v))

    visited = [False] * (n + 1)
    order = []

    def dfs(u):
        stack = [u]
        visited[u] = True
        while stack:
            node = stack[-1]
            has_unvisited = False
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
                    has_unvisited = True
                    break
            if not has_unvisited:
                order.append(stack.pop())

    for u in range(1, n + 1):
        if not visited[u]:
            dfs(u)

    visited = [False] * (n + 1)
    scc_id = [0] * (n + 1)
    current_id = 0

    order.reverse()
    for u in order:
        if not visited[u]:
            stack = [u]
            visited[u] = True
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for neighbor in adj_rev[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            for node in component:
                scc_id[node] = current_id
            current_id += 1

    scc_adj = [[] for _ in range(current_id)]
    scc_in_degree = [0] * current_id
    scc_out_degree = [0] * current_id

    for u in range(1, n + 1):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_adj[scc_id[u]].append(scc_id[v])

    for u in range(current_id):
        scc_adj[u] = list(set(scc_adj[u]))

    for u in range(current_id):
        for v in scc_adj[u]:
            scc_out_degree[u] += 1
            scc_in_degree[v] += 1

    sources = []
    sinks = []
    for i in range(current_id):
        if scc_in_degree[i] == 0:
            sources.append(i)
        if scc_out_degree[i] == 0:
            sinks.append(i)

    if len(sources) == 0 or len(sinks) == 0:
        print(-1)
        return

    s = sources[0]
    t = sinks[0]

    for u in range(1, n + 1):
        if scc_id[u] == s:
            for v in range(1, n + 1):
                if scc_id[v] == t and (u, v) not in edges:
                    print(u, v)
                    return

    print(-1)

if __name__ == "__main__":
    main()
