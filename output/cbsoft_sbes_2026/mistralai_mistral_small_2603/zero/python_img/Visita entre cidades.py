
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    A = int(data[idx+1])
    B = int(data[idx+2])
    idx += 3

    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        P = int(data[idx])
        Q = int(data[idx+1])
        D = int(data[idx+2])
        graph[P].append((Q, D))
        graph[Q].append((P, D))
        idx += 3

    def bfs(start):
        dist = [-1] * (N + 1)
        q = deque()
        q.append(start)
        dist[start] = 0
        while q:
            u = q.popleft()
            for v, d in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + d
                    q.append(v)
        return dist

    dist_a = bfs(A)
    print(dist_a[B])

if __name__ == "__main__":
    main()
