
import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N+1)]
    adj_rev = [[] for _ in range(N+1)]
    edges = set()

    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
        adj[x].append(y)
        adj_rev[y].append(x)
        edges.add((x, y))

    visited = [False] * (N + 1)
    order = []

    def dfs(u):
        stack = [(u, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                order.append(node)
                continue
            if visited[node]:
                continue
            visited[node] = True
            stack.append((node, True))
            for v in adj[node]:
                if not visited[v]:
                    stack.append((v, False))

    for u in range(1, N+1):
        if not visited[u]:
            dfs(u)

    visited = [False] * (N + 1)
    scc_id = [0] * (N + 1)
    current_id = 0

    order.reverse()

    def reverse_dfs(u, pid):
        stack = [u]
        visited[u] = True
        scc_id[u] = pid
        while stack:
            node = stack.pop()
            for v in adj_rev[node]:
                if not visited[v]:
                    visited[v] = True
                    scc_id[v] = pid
                    stack.append(v)

    for u in order:
        if not visited[u]:
            reverse_dfs(u, current_id)
            current_id += 1

    scc_size = [0] * current_id
    for u in range(1, N+1):
        scc_size[scc_id[u]] += 1

    scc_adj = [[] for _ in range(current_id)]
    scc_adj_rev = [[] for _ in range(current_id)]

    for x in range(1, N+1):
        for y in adj[x]:
            if scc_id[x] != scc_id[y]:
                scc_adj[scc_id[x]].append(scc_id[y])
                scc_adj_rev[scc_id[y]].append(scc_id[x])

    scc_in_degree = [0] * current_id
    for u in range(current_id):
        for v in scc_adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_in_degree[v] += 1

    q = deque()
    for u in range(current_id):
        if scc_in_degree[u] == 0:
            q.append(u)

    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in scc_adj[u]:
            scc_in_degree[v] -= 1
            if scc_in_degree[v] == 0:
                q.append(v)

    scc_pos = [0] * current_id
    for i in range(len(topo_order)):
        scc_pos[topo_order[i]] = i

    scc_adj_sorted = [[] for _ in range(current_id)]
    for u in range(current_id):
        for v in scc_adj[u]:
            if scc_pos[u] < scc_pos[v]:
                scc_adj_sorted[scc_pos[u]].append(scc_pos[v])

    max_reachable = [0] * current_id
    for u in reversed(topo_order):
        max_r = 0
        for v in scc_adj_sorted[scc_pos[u]]:
            if max_r < max_reachable[v]:
                max_r = max_reachable[v]
        max_reachable[scc_pos[u]] = max_r + scc_size[u]

    total_reachable = 0
    for u in range(current_id):
        total_reachable += max_reachable[u]

    for x in range(1, N+1):
        for y in range(1, N+1):
            if x == y:
                continue
            if (x, y) in edges:
                continue
            if scc_id[x] == scc_id[y]:
                print(f"{x} {y}")
                return

    for x in range(1, N+1):
        for y in range(1, N+1):
            if x == y:
                continue
            if (x, y) in edges:
                continue
            if scc_pos[scc_id[x]] < scc_pos[scc_id[y]]:
                new_reachable = total_reachable + scc_size[scc_id[y]]
                if new_reachable == total_reachable:
                    print(f"{x} {y}")
                    return

    print(-1)

if __name__ == "__main__":
    main()
