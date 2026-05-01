
import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while True:
        N = int(input[ptr])
        ptr += 1
        if N == 0:
            break
        if N == 1:
            print(f"Teste {test_num}")
            print(1)
            print()
            test_num += 1
            continue

        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            X = int(input[ptr])
            Y = int(input[ptr+1])
            ptr += 2
            adj[X].append(Y)
            adj[Y].append(X)

        def bfs(start):
            dist = [-1] * (N + 1)
            q = deque()
            q.append(start)
            dist[start] = 0
            last = start
            while q:
                u = q.popleft()
                last = u
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return last, dist

        node, _ = bfs(1)
        node, dist1 = bfs(node)
        _, dist2 = bfs(node)

        max_dist = max(max(dist1), max(dist2))
        candidates = [i for i in range(1, N+1) if dist1[i] == max_dist and dist2[i] == max_dist]

        print(f"Teste {test_num}")
        print(candidates[0])
        print()
        test_num += 1

solve()
