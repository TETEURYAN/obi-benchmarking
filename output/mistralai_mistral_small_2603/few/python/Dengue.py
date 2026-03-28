
import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    ptr = 0
    test_case = 1
    while True:
        N = int(input_data[ptr]) if ptr < len(input_data) else 0
        ptr += 1
        if N == 0:
            break

        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u = int(input_data[ptr])
            v = int(input_data[ptr + 1])
            ptr += 2
            adj[u].append(v)
            adj[v].append(u)

        if N == 1:
            print(f"Teste {test_case}")
            print(1)
            print()
            test_case += 1
            continue

        def bfs(start):
            dist = [-1] * (N + 1)
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
        node, dist1 = bfs(node)
        node, dist2 = bfs(node)

        max_dist = max(dist2[1:])
        candidates = [i for i in range(1, N + 1) if dist2[i] == max_dist]

        print(f"Teste {test_case}")
        print(candidates[0])
        print()
        test_case += 1

if __name__ == "__main__":
    main()
