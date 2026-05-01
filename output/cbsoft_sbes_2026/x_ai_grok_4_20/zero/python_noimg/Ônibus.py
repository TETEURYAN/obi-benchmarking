
import sys
from collections import deque

sys.setrecursionlimit(20000)

N, A, B = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    P, Q = map(int, input().split())
    graph[P].append(Q)
    graph[Q].append(P)

dist = [-1] * (N + 1)
queue = deque([A])
dist[A] = 0

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)

print(dist[B])
