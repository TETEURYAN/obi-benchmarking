
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = int(data[1])
B = int(data[2])

graph = [[] for _ in range(N + 1)]
index = 3
for i in range(N - 1):
    P = int(data[index])
    Q = int(data[index + 1])
    D = int(data[index + 2])
    graph[P].append((Q, D))
    graph[Q].append((P, D))
    index += 3

dist = [-1] * (N + 1)
dist[A] = 0
queue = deque([A])

while queue:
    u = queue.popleft()
    for v, d in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + d
            queue.append(v)

print(dist[B])
