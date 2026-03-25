import sys
sys.setrecursionlimit(200000)

def bfs(start, target, adj):
    from collections import deque
    visited = [False] * (len(adj))
    dist = [0] * (len(adj))
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        u = q.popleft()
        if u == target:
            return dist[u]
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.append(v)
    return -1

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    A = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        P = int(next(it))
        Q = int(next(it))
        adj[P].append(Q)
        adj[Q].append(P)
    result = bfs(A, B, adj)
    print(result)

if __name__ == "__main__":
    main()