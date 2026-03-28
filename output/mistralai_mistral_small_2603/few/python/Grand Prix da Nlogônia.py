
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return

    it = iter(data)
    N = int(next(it))
    M = int(next(it))

    adj = [[] for _ in range(N + 1)]
    edges = []
    for _ in range(M):
        U = int(next(it))
        L = int(next(it))
        R = int(next(it))
        edges.append((U, L, R))

    def build_graph(X):
        adj = [[] for _ in range(N + 1)]
        for i in range(X):
            U, L, R = edges[i]
            for v in range(L, R + 1):
                adj[U].append(v)
        return adj

    def has_cycle(adj):
        visited = [False] * (N + 1)
        rec_stack = [False] * (N + 1)

        def dfs(u):
            visited[u] = True
            rec_stack[u] = True
            for v in adj[u]:
                if not visited[v]:
                    if dfs(v):
                        return True
                elif rec_stack[v]:
                    return True
            rec_stack[u] = False
            return False

        for u in range(1, N + 1):
            if not visited[u]:
                if dfs(u):
                    return True
        return False

    low = 1
    high = M
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        adj_mid = build_graph(mid)
        if has_cycle(adj_mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    print(answer if answer != -1 else -1)

if __name__ == "__main__":
    main()
