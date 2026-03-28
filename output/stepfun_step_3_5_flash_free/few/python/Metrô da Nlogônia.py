import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj1 = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = int(next(it))
        v = int(next(it))
        adj1[u].append(v)
        adj1[v].append(u)
    adj2 = [[] for _ in range(m+1)]
    for _ in range(m-1):
        u = int(next(it))
        v = int(next(it))
        adj2[u].append(v)
        adj2[v].append(u)

    def find_center(adj, total):
        def bfs(start):
            dist = [-1] * (total+1)
            q = deque([start])
            dist[start] = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            far = start
            for i in range(1, total+1):
                if dist[i] > dist[far]:
                    far = i
            return far, dist

        A, _ = bfs(1)
        B, distA = bfs(A)
        _, distB = bfs(B)
        min_ecc = 10**9
        center = -1
        for i in range(1, total+1):
            ecc = max(distA[i], distB[i])
            if ecc < min_ecc:
                min_ecc = ecc
                center = i
        return center

    u = find_center(adj1, n)
    v = find_center(adj2, m)
    print(u, v)

if __name__ == "__main__":
    main()