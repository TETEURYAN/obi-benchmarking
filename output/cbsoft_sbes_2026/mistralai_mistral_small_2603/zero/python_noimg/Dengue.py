
import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while True:
        N = int(input[ptr])
        ptr += 1
        if N == 0:
            break
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            x = int(input[ptr])
            y = int(input[ptr+1])
            ptr += 2
            adj[x].append(y)
            adj[y].append(x)

        if N == 1:
            print(f"Teste {test_num}")
            print(1)
            print()
            test_num += 1
            continue

        def bfs(start):
            dist = [-1] * (N+1)
            q = deque()
            q.append(start)
            dist[start] = 0
            last_node = start
            while q:
                u = q.popleft()
                last_node = u
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return last_node, dist

        node, _ = bfs(1)
        farthest_node, dist1 = bfs(node)
        _, dist2 = bfs(farthest_node)

        max_dist = max(dist2[1:])
        candidates = [i for i in range(1, N+1) if dist2[i] == max_dist]

        if len(candidates) == 1:
            print(f"Teste {test_num}")
            print(candidates[0])
            print()
        else:
            print(f"Teste {test_num}")
            print(candidates[0])
            print()
        test_num += 1

if __name__ == "__main__":
    main()
